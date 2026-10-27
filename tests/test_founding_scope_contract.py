"""Non-regression contract for the original PHP2SHELL mission and its expansion.

Offline, deterministic documentation checks. No network requests or vulnerability probes.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parent.parent
CONTINUITY_ID = "PHP2SHELL-CONT-20261027-ROOT-01"
CANONICAL_ANCHOR = "github.com/chainsolutions-wealthtech/Php2shell/issues/5"


class FoundingScopeTests(unittest.TestCase):
    def _read(self, relative_path):
        path = ROOT / relative_path
        self.assertTrue(path.is_file(), str(path))
        data = path.read_text(encoding="utf-8")
        self.assertIn(CONTINUITY_ID, data)
        self.assertIn(CANONICAL_ANCHOR, data)
        return data

    def test_original_six_lots_are_preserved(self):
        doc = self._read("continuity/FOUNDING_SPECIFICATION.md")
        for identifier in ("L1", "L2", "L3", "L4", "L5", "L6"):
            with self.subTest(lot=identifier):
                self.assertRegex(doc, r"(?m)^\| \*\*" + identifier + r"\*\*")

    def test_five_versions_and_original_technology_stack(self):
        doc = self._read("continuity/FOUNDING_SPECIFICATION.md")
        for version in ("V0.1", "V0.2", "V0.3", "V0.4", "V1.0"):
            self.assertIn(version, doc)
        for name in ("Python", "FastAPI", "PostgreSQL", "Redis", "Docker", "MCP"):
            self.assertIn(name, doc)

    def test_original_scope_and_passive_campaigns_cannot_be_dropped(self):
        doc = self._read("continuity/FOUNDING_SPECIFICATION.md")
        for name in (
            "CSV/JSON/TXT", "P1", "P2", "public_metadata", "owned_source",
            "CAP-01", "CAP-02", "CAP-03", "CAP-04", "CAP-05",
            "CAP-06", "CAP-07", "CAP-08", "CAP-09", "CAP-10",
            "SSRF", "redirections", "milliers",
        ):
            with self.subTest(requirement=name):
                self.assertIn(name, doc)

    def test_requirements_matrix_contains_every_id_once(self):
        doc = self._read("continuity/REQUIREMENTS_TRACEABILITY.md")
        entries = re.findall(r"(?m)^\| \*\*(REQ-\d{3})\*\*\s", doc)
        expected = [f"REQ-{i:03d}" for i in range(1, 23)]
        self.assertEqual(entries, expected)
        self.assertEqual(len(entries), len(set(entries)))
        for key in ("Non implémenté", "Partiel", "V0.2", "V0.3", "V0.4", "V1.0"):
            self.assertIn(key, doc)

    def test_php_advisories_and_corrections_are_sourced(self):
        doc = self._read("continuity/CVE_SOURCE_REGISTER.md")
        for key in (
            "CVE-2026-109618", "CVE-2026-109619",
            "GHSA-w8hw-w9fx-j79w", "GHSA-6wmf-4rv5-p3rp",
            "CERTFR-2026-ALE-014",
            "8.5.12", "8.4.27", "8.3.36", "8.2.35",
            "portail-demo.example", "backport", "runtime",
        ):
            with self.subTest(key=key):
                self.assertIn(key, doc)
        self.assertIn("ne doit plus être interprétée", doc)

    def test_dual_s1_domains_and_no_premature_deploy(self):
        doc = self._read("continuity/FOUNDING_SPECIFICATION.md")
        for host in ("php2shell.wealthtechinnovations.com",
                     "phppatch.wealthtechinnovations.com"):
            self.assertIn(host, doc)
        self.assertIn("non implément", self._read("continuity/REQUIREMENTS_TRACEABILITY.md"))

    def test_canonical_entry_links_to_all_added_contracts(self):
        start = self._read("00_START_HERE.md")
        for name in ("FOUNDING_SPECIFICATION.md", "REQUIREMENTS_TRACEABILITY.md",
                     "CVE_SOURCE_REGISTER.md"):
            self.assertIn(name, start)

    def test_foundational_decisions_are_append_only_unique(self):
        decisions = self._read("continuity/DECISIONS_LOG.md")
        ids = re.findall(r"(?m)^\| (P2S-DEC-\d{3}) \|", decisions)
        self.assertEqual(ids, [f"P2S-DEC-{i:03d}" for i in range(1, 12)])

if __name__ == "__main__":
    unittest.main()
