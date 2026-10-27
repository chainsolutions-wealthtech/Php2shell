"""Guard the repository's public, durable PHP2SHELL continuity contract.

These tests are intentionally offline and do not touch production or GitHub APIs.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parent.parent
CONTINUITY_ID = "PHP2SHELL-CONT-20261027-ROOT-01"

REQUIRED_FILES = (
    "00_START_HERE.md",
    "continuity/MISSION_AND_OPERATION.md",
    "continuity/CURRENT_STATE.md",
    "continuity/DECISIONS_LOG.md",
    "continuity/EVENT_LOG.md",
    "continuity/NEXT_ACTION.md",
    "continuity/PROTOCOL.md",
    "continuity/HANDOFF.md",
)


class ContinuityContractTests(unittest.TestCase):
    def test_canonical_documents_exist_with_stable_anchor(self):
        for path in REQUIRED_FILES:
            with self.subTest(path=path):
                document = ROOT / path
                self.assertTrue(document.is_file(), path)
                text = document.read_text(encoding="utf-8")
                self.assertIn(CONTINUITY_ID, text)
                self.assertIn("github.com/chainsolutions-wealthtech/Php2shell/issues/5", text)

    def test_original_five_versions_preserved(self):
        charter = (ROOT / "00_START_HERE.md").read_text(encoding="utf-8")
        mission = (ROOT / "continuity/MISSION_AND_OPERATION.md").read_text(encoding="utf-8")
        for version in ("V0.1", "V0.2", "V0.3", "V0.4", "V1.0"):
            with self.subTest(version=version):
                self.assertIn(version, charter)
                self.assertIn(version, mission)

    def test_two_domains_and_single_engine_preserved(self):
        documents = ((ROOT / "00_START_HERE.md").read_text(encoding="utf-8")
                     + (ROOT / "continuity/MISSION_AND_OPERATION.md").read_text(encoding="utf-8"))
        for name in ("php2shell.wealthtechinnovations.com",
                     "phppatch.wealthtechinnovations.com"):
            self.assertIn(name, documents)
        self.assertIn("moteur", documents.lower())
        self.assertIn("S1", documents)

    def test_key_decision_and_event_identifiers_are_unique(self):
        for path, pattern in (
            ("continuity/DECISIONS_LOG.md", r"P2S-DEC-\d{3}"),
            ("continuity/EVENT_LOG.md", r"P2S-EVT-\d{3}"),
        ):
            with self.subTest(path=path):
                text = (ROOT / path).read_text(encoding="utf-8")
                ids = re.findall(r"^\|[^\n]*?\b(P2S-(?:DEC|EVT)-\d{3})\b[^\n]*\|", text, flags=re.M)
                self.assertGreaterEqual(len(ids), 7, path)
                self.assertEqual(len(ids), len(set(ids)), path)

    def test_handoff_and_checkpoint_protocol_exist(self):
        protocol = (ROOT / "continuity/PROTOCOL.md").read_text(encoding="utf-8")
        handoff = (ROOT / "continuity/HANDOFF.md").read_text(encoding="utf-8")
        for marker in ("checkpoint_id:", "head_before:", "head_after:", "next_action:", "evidence:"):
            self.assertIn(marker, protocol)
        self.assertIn("issues/5", handoff)
        self.assertIn("NEXT_ACTION", handoff)


if __name__ == "__main__":
    unittest.main()
