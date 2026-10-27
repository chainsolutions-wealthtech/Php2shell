"""Protect URL-based, mandate-scoped audit and PHPPATCH handoff requirements.

These are deterministic documentation tests, not web scanners or vulnerability tests.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROOT_ID = "PHP2SHELL-CONT-20261027-ROOT-01"


class UrlAuditContractTests(unittest.TestCase):
    def doc(self, rel):
        source = ROOT / rel
        self.assertTrue(source.is_file(), rel)
        content = source.read_text(encoding="utf-8")
        self.assertIn(ROOT_ID, content)
        self.assertIn("github.com/chainsolutions-wealthtech/Php2shell/issues/5", content)
        return content

    def test_frontend_url_to_report_to_patch_flow_preserved(self):
        doc = self.doc("continuity/URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md")
        for term in ("URL", "frontend", "php2shell.wealthtechinnovations.com",
                     "phppatch.wealthtechinnovations.com", "HTML", "JavaScript",
                     "headers", "cookies", "PDF/JSON/CSV", "diff", "rollback"):
            with self.subTest(term=term):
                self.assertIn(term, doc)
        self.assertIn("NON IMPLÉMENTÉE", doc)

    def test_remote_php_source_limit_and_p2_requirements(self):
        doc = self.doc("continuity/URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md")
        for term in ("code PHP exécuté côté serveur", "P1", "P2",
                     "Git", "SAPI", "composer.lock", "INSUFFICIENT_EVIDENCE",
                     "CONFIRMED_APPLICABILITY", "VENDOR_PATCHED",
                     "CVE-2026-109618", "CVE-2026-109619"):
            with self.subTest(term=term):
                self.assertIn(term, doc)

    def test_network_access_requires_scope_and_bounds(self):
        doc = self.doc("continuity/URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md")
        for term in ("SSRF", "rebinding", "loopback", "link-local",
                     "autorisation", "hors périmètre", "quota",
                     "refuser", "mandat", "reprise", "annulation"):
            with self.subTest(term=term):
                self.assertIn(term.lower(), doc.lower())
        self.assertIn("Aucune URL publique", doc)

    def test_all_ten_added_requirements_preserved(self):
        matrix = self.doc("continuity/REQUIREMENTS_TRACEABILITY.md")
        found = re.findall(r"(?m)^\| \*\*(REQ-\d{3})\*\* ", matrix)
        self.assertEqual(found, [f"REQ-{i:03d}" for i in range(1, 33)])
        for label in ("REQ-023", "REQ-024", "REQ-025", "REQ-026",
                      "REQ-027", "REQ-028", "REQ-029", "REQ-030",
                      "REQ-031", "REQ-032"):
            self.assertIn(label, matrix)

    def test_reprise_and_existing_phase_remain_unchanged(self):
        for rel in ("00_START_HERE.md", "continuity/HANDOFF.md",
                    "continuity/FOUNDING_SPECIFICATION.md",
                    "continuity/NEXT_ACTION.md"):
            with self.subTest(path=rel):
                content = self.doc(rel)
                self.assertIn("URL_SITE_AUDIT_AND_PATCH_WORKFLOW.md", content)
                self.assertIn("REQ-023", content)
        action = self.doc("continuity/NEXT_ACTION.md")
        self.assertIn("P2S-NEXT-001", action)
        self.assertIn("PR #6", action)
        self.assertIn("PR #1", action)

    def test_new_decision_and_event_are_unique(self):
        decisions = self.doc("continuity/DECISIONS_LOG.md")
        events = self.doc("continuity/EVENT_LOG.md")
        self.assertEqual(len(re.findall(r"(?m)^\| P2S-DEC-012 \|", decisions)), 1)
        self.assertEqual(len(re.findall(r"(?m)^\| 2026-10-27 \| P2S-EVT-012 \|", events)), 1)


if __name__ == "__main__":
    unittest.main()
