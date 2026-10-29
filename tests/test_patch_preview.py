"""Read-only local PHP configuration patch proposal regression tests."""
import json
import socket
import subprocess
import sys
import tempfile
import unittest
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch

from app.audit_dossier import build_audit_dossier
from app.patch_preview import propose_local_ini_patch


class IniPatchPreviewTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.config = self.root / "php.ini"
        self.config.write_text(
            "display_errors = On\n"
            "session.secret=DO_NOT_LEAK_SESSION_SECRET\n"
            "expose_php=Off\n", encoding="utf-8"
        )

    def evidence(self, rule="PHP-CONFIG-DISPLAY-ERRORS"):
        dossier = build_audit_dossier(self.root, "2026-10-28")
        items = [x for x in dossier["observations"] if x["rule"] == rule]
        self.assertEqual(len(items), 1)
        return items[0]["evidence_id"]

    def test_proposes_exact_minimal_diff_without_modifying_file(self):
        evidence = self.evidence()
        before = sha256(self.config.read_bytes()).hexdigest()
        with patch.object(socket.socket, "connect", side_effect=AssertionError("network")):
            proposal = propose_local_ini_patch(self.root, "2026-10-28", evidence)
        after = sha256(self.config.read_bytes()).hexdigest()
        self.assertEqual(before, after)
        self.assertEqual(proposal["relative_file"], "php.ini")
        self.assertEqual(proposal["source_evidence_id"], evidence)
        self.assertEqual(proposal["unified_diff"],
                         "--- a/php.ini\n+++ b/php.ini\n@@ -1 +1 @@\n"
                         "-display_errors = On\n+display_errors=Off\n")
        self.assertEqual(proposal["files_modified"], 0)
        for key in ("patch_applied", "mandate_verified",
                    "effective_php_configuration_verified",
                    "tests_run_on_candidate", "independent_approval_received",
                    "ready_for_production"):
            self.assertIs(proposal[key], False)
        self.assertNotIn("DO_NOT_LEAK_SESSION_SECRET", json.dumps(proposal))
        self.assertNotIn(str(self.root), json.dumps(proposal))
        self.assertEqual(len(proposal["diff_sha256"]), 64)

    def test_deterministic_and_rejects_bad_evidence_identifiers(self):
        id = self.evidence()
        self.assertEqual(
            propose_local_ini_patch(self.root, "2026-10-28", id),
            propose_local_ini_patch(self.root, "2026-10-28", id),
        )
        for bad in ("", "unknown", "P2S-EV-" + "0"*16, 7,
                    "P2S-EV-" + "x"*16):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                propose_local_ini_patch(self.root, "2026-10-28", bad)

    def test_diff_not_generated_for_unsupported_rule(self):
        self.config.write_text("expose_php=On\n", encoding="utf-8")
        identifier = self.evidence("PHP-CONFIG-EXPOSE-PHP")
        with self.assertRaisesRegex(ValueError, "No supported"):
            propose_local_ini_patch(self.root, "2026-10-28", identifier)

    def test_ambiguous_commented_setting_refused(self):
        self.config.write_text(
            "display_errors = On ; SECRET_COMMENT\n", encoding="utf-8"
        )
        identifier = self.evidence()
        with self.assertRaisesRegex(ValueError, "Ambiguous"):
            propose_local_ini_patch(self.root, "2026-10-28", identifier)

    def test_project_symlink_and_oversize_file_rejected(self):
        identifier = self.evidence()
        link = self.root.parent / (self.root.name + "-link")
        try:
            link.symlink_to(self.root, target_is_directory=True)
        except (OSError, NotImplementedError):
            pass
        else:
            self.addCleanup(link.unlink)
            with self.assertRaises(ValueError):
                propose_local_ini_patch(link, "2026-10-28", identifier)
        self.config.write_text(
            "display_errors=On\n" + "a" * 66_000, encoding="utf-8"
        )
        identifier = self.evidence()
        with self.assertRaisesRegex(ValueError, "too large"):
            propose_local_ini_patch(self.root, "2026-10-28", identifier)

    def test_nested_ini_file_and_crlf_line_endings(self):
        self.config.unlink()
        p = self.root / "settings"
        p.mkdir()
        target = p / ".user.ini"
        target.write_bytes(
            b"expose_php=Off\r\ndisplay_errors=On\r\npassword=SECRET\r\n"
        )
        identifier = self.evidence()
        result = propose_local_ini_patch(self.root, "2026-10-28", identifier)
        self.assertEqual(result["relative_file"], "settings/.user.ini")
        self.assertIn("@@ -2 +2 @@", result["unified_diff"])
        self.assertNotIn("password", result["unified_diff"])

    def test_cli_does_not_write_source_and_legacy_reports_remain(self):
        identifier = self.evidence()
        before = self.config.read_bytes()
        proc = subprocess.run(
            [sys.executable, "-m", "app.cli", "propose-config-patch",
             "--path", str(self.root), "--as-of", "2026-10-28",
             "--evidence-id", identifier],
            capture_output=True, text=True, check=True,
        )
        result = json.loads(proc.stdout)
        self.assertEqual(result["proposal_type"], "LOCAL_PHP_INI_UNAPPLIED_REVIEW_DIFF")
        self.assertFalse(result["ready_for_production"])
        self.assertEqual(before, self.config.read_bytes())
        self.assertNotIn("DO_NOT_LEAK_SESSION_SECRET", proc.stdout)


    def test_duplicate_active_display_errors_refused(self):
        """A single-line diff cannot claim to fix conflicting active ini entries."""
        self.config.write_text(
            "display_errors=On\n"
            "session.secret=DO_NOT_LEAK_SESSION_SECRET\n"
            "display_errors=Off\n", encoding="utf-8"
        )
        dossier = build_audit_dossier(self.root, "2026-10-28")
        candidates = [row for row in dossier["observations"]
                      if row["rule"] == "PHP-CONFIG-DISPLAY-ERRORS"]
        self.assertGreaterEqual(len(candidates), 1)
        before = self.config.read_bytes()
        with self.assertRaisesRegex(ValueError, "Multiple active"):
            propose_local_ini_patch(
                self.root, "2026-10-28", candidates[0]["evidence_id"]
            )
        self.assertEqual(before, self.config.read_bytes())

    def test_commented_second_setting_is_not_an_active_override(self):
        """Inactive comments are not interpreted as an overriding directive."""
        self.config.write_text(
            "display_errors=On\n"
            "; display_errors=Off\n"
            "session.secret=DO_NOT_LEAK_SESSION_SECRET\n",
            encoding="utf-8",
        )
        result = propose_local_ini_patch(
            self.root, "2026-10-28", self.evidence()
        )
        self.assertFalse(result["patch_applied"])
        self.assertNotIn("DO_NOT_LEAK_SESSION_SECRET", result["unified_diff"])


if __name__ == "__main__":
    unittest.main()
