"""Offline DNS-snapshot freshness contract; no resolver, network or admission."""
import socket
import unittest
from unittest.mock import patch

from app.network_preflight import check_public_address_answers


class DnsSnapshotFreshnessTests(unittest.TestCase):
    def evaluate(self, observed="2026-10-28T03:00:00Z", evaluated="2026-10-28T03:00:30Z", ttl=60):
        with patch.object(socket.socket, "connect", side_effect=AssertionError("network forbidden")):
            return check_public_address_answers(
                "example.com", ["8.8.8.8"], observed,
                ttl_seconds=ttl, evaluated_at_utc=evaluated,
            )

    def test_fresh_supplied_snapshot_remains_non_authoritative(self):
        result = self.evaluate()
        self.assertTrue(result["snapshot_freshness_checked"])
        self.assertTrue(result["supplied_snapshot_within_ttl"])
        self.assertEqual(result["candidate_public_addresses"], ["8.8.8.8"])
        self.assertFalse(result["dns_answers_authenticated"])
        self.assertFalse(result["peer_connection_authorized"])
        self.assertFalse(result["network_requests_made"])

    def test_expired_snapshot_discards_candidates(self):
        result = self.evaluate(evaluated="2026-10-28T03:01:00Z")
        self.assertFalse(result["supplied_snapshot_within_ttl"])
        self.assertEqual(result["candidate_public_addresses"], [])
        self.assertIn("STALE_OR_FUTURE_DNS_SNAPSHOT", result["blockers"])

    def test_future_dated_snapshot_discards_candidates(self):
        result = self.evaluate(evaluated="2026-10-28T02:59:59Z")
        self.assertFalse(result["supplied_snapshot_within_ttl"])
        self.assertEqual(result["candidate_public_addresses"], [])
        self.assertFalse(result["peer_connection_authorized"])

    def test_invalid_evaluation_clock_fails_closed(self):
        for clock in ("", "not-time", "2026-02-30T03:00:00Z", 0):
            with self.subTest(clock=clock), self.assertRaises(ValueError):
                self.evaluate(evaluated=clock)

    def test_mixed_private_ip_remains_blocked_even_when_fresh(self):
        result = check_public_address_answers(
            "example.com", ["8.8.8.8", "127.0.0.1"],
            "2026-10-28T03:00:00Z", evaluated_at_utc="2026-10-28T03:00:01Z",
        )
        self.assertTrue(result["supplied_snapshot_within_ttl"])
        self.assertFalse(result["all_supplied_addresses_globally_routable"])
        self.assertEqual(result["candidate_public_addresses"], [])
        self.assertIn("NON_GLOBAL_OR_MAPPED_IP_IN_DNS_SNAPSHOT", result["blockers"])

    def test_legacy_caller_does_not_implicitly_assert_freshness(self):
        result = check_public_address_answers(
            "example.com", ["8.8.8.8"], "2026-10-28T03:00:00Z",
        )
        self.assertFalse(result["peer_connection_authorized"])
        self.assertNotIn("snapshot_freshness_checked", result)


    def test_boolean_ttl_is_rejected_not_treated_as_one_second(self):
        with self.assertRaises(ValueError):
            self.evaluate(ttl=True)

    def test_fractional_ttl_is_rejected(self):
        with self.assertRaises(ValueError):
            self.evaluate(ttl=1.5)

    def test_zero_age_is_fresh_but_exact_ttl_is_expired(self):
        self.assertTrue(self.evaluate(evaluated="2026-10-28T03:00:00Z")["supplied_snapshot_within_ttl"])
        self.assertFalse(self.evaluate(evaluated="2026-10-28T03:01:00Z")["supplied_snapshot_within_ttl"])

    def test_malformed_observation_clock_fails_closed(self):
        with self.assertRaises(ValueError):
            self.evaluate(observed="2026-10-28T03:00:00+01:00")



if __name__ == "__main__":
    unittest.main()
