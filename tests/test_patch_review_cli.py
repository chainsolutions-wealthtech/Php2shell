"""CLI-only PHPPATCH packet revalidation; never executes a patch or network call."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from app.audit_dossier import build_audit_dossier
from app.patch_review_packet import build_patch_review_packet


class PatchReviewCliTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "php.ini"
        self.source.write_bytes(
            b"display_errors=On\n"
            b"session.secret=PRIVATE_DO_NOT_PRINT\n"
        )
        dossier = build_audit_dossier(self.root, "2026-10-28")
        self.evidence = next(
            item["evidence_id"] for item in dossier["observations"]
            if item["rule"] == "PHP-CONFIG-DISPLAY-ERRORS"
        )
        self.packet = build_patch_review_packet(
            self.root, "2026-10-28", self.evidence
        )
        self.packet_file = self.root / "review-packet.json"
        self.write_packet(self.packet)

    def write_packet(self, packet):
        self.packet_file.write_text(
            json.dumps(packet), encoding="utf-8"
        )

    def run_cli(self, packet_file=None):
        return subprocess.run([
            sys.executable, "-m", "app.cli", "verify-patch-review",
            "--packet-file", str(packet_file or self.packet_file),
            "--path", str(self.root), "--as-of", "2026-10-28",
            "--evidence-id", self.evidence,
        ], capture_output=True, text=True, check=False)

    def test_valid_packet_matches_but_does_not_approve(self):
        before = self.source.read_bytes()
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        record = json.loads(result.stdout)
        self.assertTrue(record["local_lineage_matches"])
        self.assertEqual(record["packet_sha256"], self.packet["packet_sha256"])
        for key in (
            "packet_signature_verified", "identity_and_mandate_verified",
            "independent_approval_received", "patch_applied",
            "sandbox_tests_executed", "production_rollback_proven",
            "ready_for_production",
        ):
            self.assertIs(record[key], False)
        self.assertEqual(self.source.read_bytes(), before)
        self.assertNotIn("PRIVATE_DO_NOT_PRINT", result.stdout)
        self.assertNotIn(str(self.root), result.stdout)

    def test_forged_approval_fails_closed_without_sensitive_output(self):
        self.packet["ready_for_production"] = True
        self.write_packet(self.packet)
        result = self.run_cli()
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("Local PHPPATCH review packet rejected", result.stderr)
        self.assertNotIn("PRIVATE_DO_NOT_PRINT", result.stderr)

    def test_stale_source_fails_closed(self):
        self.source.write_bytes(
            b"display_errors=On\n"
            b"session.secret=CHANGED_SECRET_VALUE\n"
        )
        result = self.run_cli()
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertNotIn("CHANGED_SECRET_VALUE", result.stderr)

    def test_duplicate_json_fields_and_symlink_rejected(self):
        self.packet_file.write_text('{"x":1,"x":2}', encoding="utf-8")
        self.assertEqual(self.run_cli().returncode, 2)
        alias = self.root / "packet-link.json"
        try:
            alias.symlink_to(self.packet_file)
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks unsupported")
        self.assertEqual(self.run_cli(alias).returncode, 2)

    def test_legacy_cli_commands_remain_exposed(self):
        result = subprocess.run(
            [sys.executable, "-m", "app.cli", "--help"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        for command in (
            "prepare-patch-review", "verify-patch-review",
            "rehearse-config-patch", "check-version", "scan-local",
        ):
            self.assertIn(command, result.stdout)


if __name__ == "__main__":
    unittest.main()
