"""Offline campaign partition tests, with no queue or network execution."""
import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app.campaign_plan import plan_offline_campaign


class CampaignPlanTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.folder = Path(self.tmp.name)
        self.input = self.folder / "campaign.json"

    def write(self, targets):
        self.input.write_text(json.dumps(targets), encoding="utf-8")
        return self.input

    def test_deterministic_dedupe_and_partitioning(self):
        records = [
            {"hostname": "ZZ.EXAMPLE.COM", "scope": "public_metadata"},
            {"hostname": "aa.example.com", "scope": "public_metadata"},
            {"hostname": "zz.example.com", "scope": "public_metadata"},
            {"hostname": "owned.example.com", "scope": "owned_source",
             "evidence": "PRIVATE-MANDATE-DO-NOT-EXPORT"},
        ]
        self.write(records)
        with patch.object(socket.socket, "connect", side_effect=AssertionError("network")):
            first = plan_offline_campaign(self.input, shards=3)
        self.write(list(reversed(records)))
        second = plan_offline_campaign(self.input, shards=3)
        self.assertEqual(first, second)
        self.assertEqual(first["source_rows_received"], 4)
        self.assertEqual(first["unique_targets"], 3)
        self.assertEqual(first["duplicates_removed"], 1)
        self.assertEqual(first["partition_count"], 3)
        self.assertEqual(sum(x["target_count"] for x in first["partitions"]), 3)
        self.assertEqual(first["jobs_created"], 0)
        self.assertEqual(first["jobs_running"], 0)
        self.assertFalse(first["network_requests_made"])
        self.assertFalse(first["authorization_verified"])
        self.assertFalse(first["mcp_claims_acquired"])
        self.assertFalse(first["safe_to_execute"])
        serialized = json.dumps(first)
        self.assertNotIn("PRIVATE-MANDATE-DO-NOT-EXPORT", serialized)
        self.assertNotIn(str(self.folder), serialized)
        all_items = [item for p in first["partitions"] for item in p["targets"]]
        self.assertEqual(len({item["asset_ref"] for item in all_items}), 3)
        self.assertTrue(all(
            not item["mandate_authenticated"]
            and not item["source_access_authorized"]
            and not item["network_admission_granted"]
            for item in all_items
        ))

    def test_large_campaign_partition_is_bounded_and_deterministic(self):
        self.write([
            {"hostname": f"site-{i}.example.com", "scope": "public_metadata"}
            for i in range(1000)
        ])
        report = plan_offline_campaign(self.input, shards=16, pages_per_target=10)
        self.assertEqual(report["unique_targets"], 1000)
        self.assertEqual(len(report["partitions"]), 16)
        self.assertEqual(sum(x["target_count"] for x in report["partitions"]), 1000)
        self.assertFalse(report["safe_to_execute"])

    def test_p2_declaration_cannot_grant_patching(self):
        self.write([
            {"hostname": "owned.example.com", "scope": "owned_source",
             "evidence": "some-user-string"}
        ])
        report = plan_offline_campaign(self.input)
        row = next(x for p in report["partitions"] for x in p["targets"])
        self.assertEqual(row["declared_scope"], "owned_source")
        self.assertFalse(row["source_access_authorized"])
        self.assertEqual(row["execution_status"], "PLANNED_NOT_ADMITTED")
        self.assertEqual(report["declared_scopes"], {"owned_source": 1})

    def test_malformed_limits_and_tag_fail_closed(self):
        self.write([{"hostname": "example.com", "scope": "public_metadata"}])
        for kw in (
            {"shards": 0}, {"shards": 33}, {"shards": True},
            {"pages_per_target": 0}, {"pages_per_target": 101},
            {"requests_per_minute": 0}, {"requests_per_minute": 31},
            {"campaign_tag": "../run"},
            {"campaign_tag": ""},
        ):
            with self.subTest(kw=kw), self.assertRaises(ValueError):
                plan_offline_campaign(self.input, **kw)

    def test_conflicting_duplicates_remain_rejected(self):
        self.write([
            {"hostname": "example.com", "scope": "public_metadata"},
            {"hostname": "example.com", "scope": "owned_source", "evidence": "claim"},
        ])
        with self.assertRaisesRegex(ValueError, "Conflicting scope"):
            plan_offline_campaign(self.input)


if __name__ == "__main__":
    unittest.main()
