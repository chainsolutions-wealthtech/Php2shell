"""Official-source snapshot tests: no remote probing or vulnerability claims."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import socket

from app.security_advisories import (
    list_verified_advisories, load_advisory_catalog, review_declared_php_version,
)


class AdvisoryCatalogTests(unittest.TestCase):
    def _modified_catalog(self, transform):
        source = load_advisory_catalog()
        custom = copy.deepcopy(source)
        transform(custom)
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        path = Path(temp.name) / "curated.json"
        path.write_text(json.dumps(custom), encoding="utf-8")
        return path

    def test_php_and_certfr_source_provenance_are_explicit(self):
        catalog = load_advisory_catalog()
        self.assertEqual(catalog["catalog_type"], "CURATED_OFFLINE_SNAPSHOT")
        self.assertEqual(catalog["source_freshness"], "NOT_A_LIVE_FEED")
        self.assertEqual(catalog["reviewed_on_utc"], "2026-10-28")
        self.assertEqual(
            {x["cve"] for x in catalog["advisories"]},
            {"CVE-2026-109618", "CVE-2026-109619"},
        )
        for advisory in catalog["advisories"]:
            with self.subTest(cve=advisory["cve"]):
                self.assertEqual(advisory["cvss_v4_base_score"], 9.2)
                self.assertEqual(advisory["fixed_upstream"], {
                    "8.2": "8.2.35", "8.3": "8.3.36",
                    "8.4": "8.4.27", "8.5": "8.5.12",
                })
                self.assertIn(
                    "PHP", [source["publisher"] for source in advisory["sources"]])
                self.assertIn(
                    "CERT-FR", [source["publisher"] for source in advisory["sources"]])

    def test_versions_never_claim_confirmed_asset_vulnerability(self):
        for version, status in (
            ("8.2.34", "below_reference_fix"),
            ("8.2.35", "at_or_above_reference_fix"),
            ("8.3.34", "below_reference_fix"),
            ("8.3.36", "at_or_above_reference_fix"),
            ("8.4.26", "below_reference_fix"),
            ("8.4.27", "at_or_above_reference_fix"),
            ("8.5.11", "below_reference_fix"),
            ("8.5.12", "at_or_above_reference_fix"),
            ("8.1.42", "review_vendor_support"),
            ("8.6.0", "review_vendor_support"),
        ):
            with self.subTest(version=version):
                result = review_declared_php_version(version)
                self.assertEqual(len(result["results"]), 2)
                self.assertTrue(result["review_type"].endswith("NOT_ASSET_DIAGNOSIS"))
                for finding in result["results"]:
                    self.assertEqual(finding["status"], status)
                    self.assertEqual(finding["asset_applicability"], "insufficient_evidence")
                    self.assertEqual(finding["version_provenance"], "user_supplied_unverified")
                    self.assertTrue(finding["needs_runtime_and_vendor_backport_attestation"])
                    self.assertTrue(finding["advisory_source_verified_in_snapshot"])
                    self.assertTrue(finding["sources"])

    def test_cli_new_commands_compatible_with_existing_check_version(self):
        cmds = (
            ["check-version", "--php", "8.3.34"],
            ["advisories"],
            ["review-version", "--php", "8.3.34"],
        )
        outputs = []
        for cmd in cmds:
            with self.subTest(cmd=cmd):
                proc = subprocess.run(
                    [sys.executable, "-m", "app.cli"] + cmd,
                    check=True, capture_output=True, text=True,
                )
                outputs.append(json.loads(proc.stdout))
        self.assertIsInstance(outputs[0], list)
        self.assertIn("reference_fix", outputs[0][0])
        self.assertEqual(outputs[1]["source_freshness"], "NOT_A_LIVE_FEED")
        self.assertEqual(outputs[2]["results"][0]["asset_applicability"],
                         "insufficient_evidence")

    def test_reading_catalog_is_network_free(self):
        with patch.object(socket.socket, "connect", side_effect=AssertionError("network")):
            self.assertEqual(len(list_verified_advisories()["advisories"]), 2)
            self.assertEqual(len(review_declared_php_version("8.3.34")["results"]), 2)

    def test_duplicate_cve_rejected(self):
        path = self._modified_catalog(
            lambda c: c["advisories"].append(copy.deepcopy(c["advisories"][0])))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            load_advisory_catalog(path)

    def test_url_spoofing_and_missing_primary_sources_rejected(self):
        for method in (
            lambda c: c["advisories"][0]["sources"][0].update(
                {"url": "https://github.com.attacker.example/php/php-src"}),
            lambda c: c["advisories"][0]["sources"][0].update(
                {"url": "http://github.com/php/php-src/security/advisories/"
                        "GHSA-w8hw-w9fx-j79w"}),
            lambda c: c["advisories"][0]["sources"][0].update(
                {"url": "https://github.com/php/php-src/security/advisories/"
                        "GHSA-w8hw-w9fx-j79w?token=secret"}),
            lambda c: c["advisories"][0].update({"sources": [
                c["advisories"][0]["sources"][1]]}),
        ):
            with self.subTest(case=str(method)):
                path = self._modified_catalog(method)
                with self.assertRaises(ValueError):
                    load_advisory_catalog(path)

    def test_invalid_reference_fix_rejected(self):
        for replacement in ("8.4.27", "8.3.36-dev", 8.3):
            with self.subTest(replacement=replacement):
                def mutate(c):
                    c["advisories"][0]["fixed_upstream"]["8.3"] = replacement
                path = self._modified_catalog(mutate)
                with self.assertRaises(ValueError):
                    load_advisory_catalog(path)

    def test_snapshot_disclaimers_cannot_be_removed(self):
        for key in ("source_freshness", "catalog_type", "limitations"):
            with self.subTest(key=key):
                path = self._modified_catalog(lambda c: c.pop(key))
                with self.assertRaises(ValueError):
                    load_advisory_catalog(path)

    def test_catalog_file_symlinks_and_oversized_files_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "large.json"
            source.write_bytes(b" " * 250_001)
            with self.assertRaises(ValueError):
                load_advisory_catalog(source)
            target = root / "small.json"
            target.write_text(json.dumps(load_advisory_catalog()), encoding="utf-8")
            link = root / "link.json"
            try:
                link.symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("No symlink support")
            with self.assertRaises(ValueError):
                load_advisory_catalog(link)


if __name__ == "__main__":
    unittest.main()
