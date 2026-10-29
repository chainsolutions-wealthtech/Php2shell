"""Contract tests for read-only candidate selector; no network or execution."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("candidate_selector", ROOT / "select_candidates.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class SelectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads((ROOT / "WORK_PACKAGES.json").read_text())

    def test_canonical_registry_is_valid(self):
        self.assertIsInstance(module.select_candidates(self.registry, {"verified_done": {}}), list)

    def test_no_candidate_can_execute(self):
        result = module.select_candidates(self.registry, {"verified_done": {}})
        self.assertTrue(all(item["execution_authorized"] is False for item in result))
        self.assertTrue(all(item["decision"] == "READ_ONLY_CANDIDATE" for item in result))

    def test_review_blocked_root_not_admissible(self):
        result = module.select_candidates(self.registry, {"verified_done": {}})
        self.assertNotIn("P2S-WF-G01", {item["id"] for item in result})

    def test_wrong_root_rejected(self):
        doc = dict(self.registry, continuity_id="another-root")
        with self.assertRaises(ValueError):
            module.select_candidates(doc, {})

    def test_fake_completion_rejected(self):
        with self.assertRaises(ValueError):
            module.select_candidates(self.registry, {"verified_done": {"P2S-WF-G01": {}}})

    def test_cycle_rejected(self):
        doc = json.loads(json.dumps(self.registry))
        doc["work_packages"][0]["depends_on"] = [doc["work_packages"][0]["id"]]
        with self.assertRaises(ValueError):
            module.select_candidates(doc, {})

    def test_unknown_dependency_rejected(self):
        doc = json.loads(json.dumps(self.registry))
        doc["work_packages"][0]["depends_on"] = ["NOT_REAL"]
        with self.assertRaises(ValueError):
            module.select_candidates(doc, {})


    def test_forged_dependency_evidence_sha_rejected(self):
        record = {
            "head_sha": "not-a-git-sha",
            "ci_url": "https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40960376137",
            "checkpoint_url": "https://github.com/chainsolutions-wealthtech/Php2shell/issues/5#issuecomment-6507828949",
        }
        with self.assertRaises(ValueError):
            module.select_candidates(self.registry, {"verified_done": {"P2S-WF-G01": record}})

    def test_foreign_ci_evidence_rejected(self):
        record = {
            "head_sha": "a" * 40,
            "ci_url": "https://github.com/other-org/other-repo/actions/runs/123",
            "checkpoint_url": "https://github.com/chainsolutions-wealthtech/Php2shell/issues/5#issuecomment-6507828949",
        }
        with self.assertRaises(ValueError):
            module.select_candidates(self.registry, {"verified_done": {"P2S-WF-G01": record}})

    def test_noncanonical_checkpoint_reference_rejected(self):
        record = {
            "head_sha": "a" * 40,
            "ci_url": "https://github.com/chainsolutions-wealthtech/Php2shell/actions/runs/40960376137",
            "checkpoint_url": "https://example.com/unverified-checkpoint",
        }
        with self.assertRaises(ValueError):
            module.select_candidates(self.registry, {"verified_done": {"P2S-WF-G01": record}})


if __name__ == "__main__":
    unittest.main()
