"""CSV reporting must never promote an offline declaration into an attestation."""
import csv
from copy import deepcopy
import io
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from app.runtime_evidence import review_declared_runtime_evidence
from app.runtime_reporting import export_runtime_review_csv


class RuntimeCsvTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "runtime.json"
        self.path.write_text(json.dumps({
            "schema_version": "0.2",
            "evidence_type": "DECLARED_PHP_RUNTIME",
            "asset_hostname": "portail-demo.example",
            "mandate_reference": "LAB-P2-001",
            "source_channel": "laboratory_fixture",
            "collected_at_utc": "2026-10-28T00:00:00Z",
            "php_version": "8.3.34",
            "sapi": "fpm-fcgi",
            "vendor_backport_status": "not_verified",
        }), encoding="utf-8")

    def review(self):
        return review_declared_runtime_evidence(self.path, "2026-10-28")

    def test_csv_header_and_two_unverified_comparisons(self):
        rows = list(csv.DictReader(io.StringIO(export_runtime_review_csv(self.review()))))
        self.assertEqual(len(rows), 2)
        self.assertEqual({r["cve"] for r in rows},
                         {"CVE-2026-109618", "CVE-2026-109619"})
        for row in rows:
            self.assertEqual(row["asset_applicability"], "insufficient_evidence")
            self.assertEqual(row["runtime_attested"], "False")
            self.assertEqual(row["mandate_verified"], "False")
            self.assertEqual(row["signature_verified"], "False")
            self.assertEqual(row["vendor_backport_status"], "not_verified")
            self.assertEqual(row["reference_fix"], "8.3.36")

    def test_no_mandate_reference_or_hash_leaked(self):
        output = export_runtime_review_csv(self.review())
        self.assertNotIn("LAB-P2-001", output)
        self.assertNotIn("declaration_sha256", output)
        self.assertNotIn("source_channel", output)

    def test_rejects_false_trust_promotion(self):
        original = self.review()
        for field, value in (
            ("mandate_authorization_verified", True),
            ("signature_verified", True),
            ("effective_http_runtime_attested", True),
            ("asset_applicability", "confirmed"),
            ("vendor_backport_status", "verified"),
        ):
            with self.subTest(field=field):
                data = deepcopy(original)
                data[field] = value
                with self.assertRaises(ValueError):
                    export_runtime_review_csv(data)

    def test_rejects_forged_comparison(self):
        original = self.review()
        for field, value in (
            ("asset_applicability", "confirmed"),
            ("cve", "CVE-1=2"),
            ("status", ["unsafe"]),
        ):
            with self.subTest(field=field):
                data = deepcopy(original)
                data["upstream_version_comparisons"][0][field] = value
                with self.assertRaises(ValueError):
                    export_runtime_review_csv(data)

    def test_spreadsheet_formula_is_escaped(self):
        data = self.review()
        data["asset_hostname"] = "  =HYPERLINK(1)"
        output = export_runtime_review_csv(data)
        rows = list(csv.DictReader(io.StringIO(output)))
        self.assertTrue(rows[0]["asset_hostname"].startswith("'"))

    def test_cli_csv_and_json_backward_compatible(self):
        base = [sys.executable, "-m", "app.cli", "review-runtime-evidence",
                "--file", str(self.path), "--as-of", "2026-10-28"]
        csv_out = subprocess.run(base + ["--format", "csv"], capture_output=True,
                                 text=True, check=True).stdout
        self.assertEqual(len(list(csv.DictReader(io.StringIO(csv_out)))), 2)
        json_out = subprocess.run(base, capture_output=True,
                                  text=True, check=True).stdout
        self.assertEqual(json.loads(json_out)["review_type"],
                         "DECLARED_RUNTIME_EVIDENCE_NOT_ATTESTATION")

    def test_offline_no_socket_connect(self):
        with patch.object(socket.socket, "connect", side_effect=AssertionError("network")):
            self.assertIn("insufficient_evidence", export_runtime_review_csv(self.review()))


if __name__ == "__main__":
    unittest.main()
