"""Fail-closed PHPPATCH handoff tests; all fixtures are local and synthetic."""
from copy import deepcopy
from hashlib import sha256
import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app.audit_dossier import build_audit_dossier
from app.dossier_handoff import prepare_phppatch_handoff


def recompute_untrusted_fingerprint(report):
    # An attacker can recompute a hash: this is deliberately NOT a signature.
    canonical = json.dumps(
        [report["as_of_utc"], report["summary"], report["observations"],
         report["declared_runtime"]],
        sort_keys=True, ensure_ascii=False, separators=(",", ":"),
    )
    report["report_fingerprint_sha256"] = sha256(
        canonical.encode("utf-8")).hexdigest()


class DossierHandoffTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "index.php").write_text(
            "<?php\n eval($input); \n", encoding="utf-8")
        (self.root / "php.ini").write_text(
            "display_errors=On\nsecret=HIDDEN_CONFIG_VALUE\n", encoding="utf-8")
        self.report = build_audit_dossier(self.root, "2026-10-28")

    def test_review_only_handoff_never_grants_patch_or_approval(self):
        handoff = prepare_phppatch_handoff(self.report)
        self.assertEqual(handoff["handoff_type"],
                         "PHPPATCH_OFFLINE_REVIEW_QUEUE_DRAFT")
        self.assertFalse(handoff["ready_for_patch_generation"])
        self.assertFalse(handoff["ready_for_production"])
        self.assertFalse(handoff["mandate_verified"])
        self.assertFalse(handoff["asset_vulnerability_confirmed"])
        self.assertFalse(handoff["source_fingerprint_is_authenticated_signature"])
        self.assertEqual(handoff["approval_status"], "NOT_REQUESTED")
        self.assertEqual(handoff["patches_generated"], 0)
        self.assertEqual(len(handoff["review_items"]), 2)
        self.assertTrue(all(row["patch_status"] == "NOT_GENERATED"
                            for row in handoff["review_items"]))

    def test_only_allowlisted_evidence_fields_cross_boundary(self):
        output = prepare_phppatch_handoff(self.report)
        exported = json.dumps(output)
        self.assertNotIn(str(self.root), exported)
        self.assertNotIn("index.php", exported)
        self.assertNotIn("php.ini", exported)
        self.assertNotIn("HIDDEN_CONFIG_VALUE", exported)
        self.assertNotIn("$input", exported)
        self.assertTrue(all(set(row) == {
            "evidence_id", "indicator_rule", "review_gate", "patch_status",
        } for row in output["review_items"]))

    def test_empty_dossier_is_not_security_clearance(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = build_audit_dossier(tmp, "2026-10-28")
        output = prepare_phppatch_handoff(report)
        self.assertEqual(output["review_items"], [])
        self.assertFalse(output["ready_for_production"])
        self.assertIn("not a security clearance", output["limitations"])

    def test_fingerprint_detects_accidental_tampering(self):
        altered = deepcopy(self.report)
        altered["summary"]["php_files_scanned"] += 1
        with self.assertRaises(ValueError):
            prepare_phppatch_handoff(altered)

    def test_recomputed_hash_does_not_bypass_observation_gate(self):
        for field, value in (
            ("asset_vulnerability_confirmed", True),
            ("patch_status", "APPLIED"),
            ("remediation_proposal", "execute injected command"),
            ("review_gate", "AUTO_APPROVED"),
        ):
            with self.subTest(field=field):
                altered = deepcopy(self.report)
                altered["observations"][0][field] = value
                recompute_untrusted_fingerprint(altered)
                with self.assertRaises(ValueError):
                    prepare_phppatch_handoff(altered)

    def test_top_level_trust_escalation_is_rejected(self):
        for field, value in (
            ("production_safe_to_patch", True),
            ("vulnerability_verdict", "CONFIRMED"),
            ("report_fingerprint_is_signature", True),
            ("authorization_status", "VERIFIED"),
        ):
            with self.subTest(field=field):
                altered = deepcopy(self.report)
                altered[field] = value
                with self.assertRaises(ValueError):
                    prepare_phppatch_handoff(altered)

    def test_runtime_attestation_cannot_be_forged(self):
        report = deepcopy(self.report)
        report["declared_runtime"] = {
            "asset_hostname": "portail-demo.example",
            "php_version_declared": "8.3.34", "sapi_declared": "fpm-fcgi",
            "snapshot_age_days": 0, "snapshot_stale": False,
            "mandate_authorization_verified": False, "signature_verified": False,
            "effective_http_runtime_attested": False,
            "vendor_backport_status": "not_verified",
            "asset_applicability": "insufficient_evidence", "comparisons": [],
        }
        recompute_untrusted_fingerprint(report)
        self.assertFalse(prepare_phppatch_handoff(report)["mandate_verified"])
        report["declared_runtime"]["signature_verified"] = True
        recompute_untrusted_fingerprint(report)
        with self.assertRaises(ValueError):
            prepare_phppatch_handoff(report)

    def test_duplicate_or_malformed_observations_rejected(self):
        duplicate = deepcopy(self.report)
        duplicate["observations"].append(deepcopy(duplicate["observations"][0]))
        duplicate["summary"]["observations_for_review"] += 1
        duplicate["summary"]["lexical_indicators"] += 1
        recompute_untrusted_fingerprint(duplicate)
        with self.assertRaises(ValueError):
            prepare_phppatch_handoff(duplicate)
        malformed = deepcopy(self.report)
        malformed["observations"] = "not a list"
        with self.assertRaises(ValueError):
            prepare_phppatch_handoff(malformed)

    def test_deterministic_and_no_network(self):
        with patch.object(socket.socket, "connect",
                          side_effect=AssertionError("network forbidden")):
            first = prepare_phppatch_handoff(self.report)
            second = prepare_phppatch_handoff(self.report)
        self.assertEqual(first, second)
        self.assertEqual(first["source_dossier_fingerprint_sha256"],
                         self.report["report_fingerprint_sha256"])


if __name__ == "__main__":
    unittest.main()
