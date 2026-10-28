"""Offline PHPPATCH packet integrity and denial-of-authority tests."""
from copy import deepcopy
import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app.audit_dossier import build_audit_dossier
from app.patch_review_packet import build_patch_review_packet
from app.patch_packet_verifier import (
    verify_local_review_packet, load_and_verify_local_review_packet,
)


class PatchPacketVerifierTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.target = self.root / "php.ini"
        self.target.write_bytes(
            b"display_errors=On\n"
            b"session.secret=PRIVATE_NEVER_EXPORT\n"
        )
        dossier = build_audit_dossier(self.root, "2026-10-28")
        self.evidence = next(
            row["evidence_id"] for row in dossier["observations"]
            if row["rule"] == "PHP-CONFIG-DISPLAY-ERRORS"
        )
        self.packet = build_patch_review_packet(
            self.root, "2026-10-28", self.evidence,
        )

    def verify(self, packet):
        return verify_local_review_packet(
            packet, self.root, "2026-10-28", self.evidence,
        )

    def test_current_packet_matches_without_authorizing_anything(self):
        before = self.target.read_bytes()
        with patch.object(socket.socket, "connect", side_effect=AssertionError("network")):
            result = self.verify(self.packet)
        self.assertEqual(self.target.read_bytes(), before)
        self.assertTrue(result["local_lineage_matches"])
        self.assertEqual(result["packet_sha256"], self.packet["packet_sha256"])
        for field in (
            "packet_signature_verified", "identity_and_mandate_verified",
            "independent_approval_received", "patch_applied",
            "sandbox_tests_executed", "production_rollback_proven",
            "ready_for_production",
        ):
            with self.subTest(field=field):
                self.assertIs(result[field], False)
        self.assertNotIn("PRIVATE_NEVER_EXPORT", json.dumps(result))
        self.assertNotIn(str(self.root), json.dumps(result))

    def test_tampered_proof_and_elevated_flags_are_rejected(self):
        for field, value in (
            ("ready_for_production", True),
            ("ready_for_production", 0),
            ("identity_and_mandate_verified", True),
        ):
            with self.subTest(field=field, value=value):
                forged = deepcopy(self.packet)
                forged[field] = value
                with self.assertRaises(ValueError):
                    self.verify(forged)
        forged = deepcopy(self.packet)
        forged["proof"]["source_file_sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            self.verify(forged)

    def test_extra_fields_and_type_substitutions_are_rejected(self):
        forged = deepcopy(self.packet)
        forged["operator_authorized"] = True
        with self.assertRaises(ValueError):
            self.verify(forged)
        forged = deepcopy(self.packet)
        forged["source_files_written"] = 0.0
        with self.assertRaises(ValueError):
            self.verify(forged)
        with self.assertRaises(ValueError):
            self.verify([self.packet])

    def test_stale_source_cannot_reuse_prior_packet(self):
        self.target.write_bytes(
            b"display_errors=On\n"
            b"session.secret=CHANGED_VALUE\n"
        )
        with self.assertRaises(ValueError):
            self.verify(self.packet)

    def test_local_json_file_load_and_no_writes(self):
        path = self.root / "packet.json"
        path.write_text(json.dumps(self.packet), encoding="utf-8")
        before = self.target.read_bytes()
        result = load_and_verify_local_review_packet(
            path, self.root, "2026-10-28", self.evidence,
        )
        self.assertTrue(result["local_lineage_matches"])
        self.assertEqual(self.target.read_bytes(), before)
        self.assertFalse(result["ready_for_production"])

    def test_duplicate_json_fields_and_nonfinite_numbers_rejected(self):
        path = self.root / "packet.json"
        path.write_text('{"x":1,"x":2}', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            load_and_verify_local_review_packet(
                path, self.root, "2026-10-28", self.evidence,
            )
        path.write_text('{"value":NaN}', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Non-finite"):
            load_and_verify_local_review_packet(
                path, self.root, "2026-10-28", self.evidence,
            )

    def test_oversized_and_symlinked_packet_files_rejected(self):
        path = self.root / "packet.json"
        path.write_bytes(b" " * 16_385)
        with self.assertRaises(ValueError):
            load_and_verify_local_review_packet(
                path, self.root, "2026-10-28", self.evidence,
            )
        alias = self.root / "packet-alias.json"
        try:
            alias.symlink_to(path)
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks unsupported")
        with self.assertRaisesRegex(ValueError, "Symlinked"):
            load_and_verify_local_review_packet(
                alias, self.root, "2026-10-28", self.evidence,
            )

    def test_wrong_evidence_or_date_cannot_match(self):
        with self.assertRaises(ValueError):
            verify_local_review_packet(
                self.packet, self.root, "2026-10-28", "P2S-EV-" + "0" * 16,
            )
        with self.assertRaises(ValueError):
            verify_local_review_packet(
                self.packet, self.root, "2026-10-27", self.evidence,
            )


if __name__ == "__main__":
    unittest.main()
