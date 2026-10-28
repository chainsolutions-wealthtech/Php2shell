"""No-network regression tests for URL/DNS policy."""
import socket
import unittest
from unittest.mock import patch

from app.network_preflight import (
    check_public_address_answers, check_same_origin_redirects,
)


class NetworkPreflightTests(unittest.TestCase):
    def test_public_dns_answers_are_only_candidates(self):
        with patch.object(socket.socket, "connect", side_effect=AssertionError("network")):
            report = check_public_address_answers(
                "EXAMPLE.COM", ["8.8.8.8", "2606:4700:4700::1111"],
                "2026-10-28T03:00:00Z",
            )
        self.assertEqual(report["hostname"], "example.com")
        self.assertTrue(report["all_supplied_addresses_globally_routable"])
        self.assertFalse(report["peer_connection_authorized"])
        self.assertFalse(report["dns_answers_authenticated"])
        self.assertFalse(report["network_requests_made"])

    def test_mixed_public_and_non_global_addresses_rejected(self):
        for address in ("127.0.0.1", "192.168.1.1", "::1", "2001:db8::1"):
            with self.subTest(address=address):
                report = check_public_address_answers(
                    "example.com", ["8.8.8.8", address],
                    "2026-10-28T03:00:00Z",
                )
                self.assertFalse(report["all_supplied_addresses_globally_routable"])
                self.assertEqual(report["candidate_public_addresses"], [])
                self.assertFalse(report["peer_connection_authorized"])

    def test_invalid_answers_and_policy_bounds(self):
        for values in ([], ["8.8.8.8", "8.8.8.8"], ["not-an-ip"], ["8.8.8.8"] * 33):
            with self.subTest(values=values), self.assertRaises(ValueError):
                check_public_address_answers(
                    "example.com", values, "2026-10-28T03:00:00Z")
        for ttl in (0, 301, True, -1):
            with self.subTest(ttl=ttl), self.assertRaises(ValueError):
                check_public_address_answers(
                    "example.com", ["8.8.8.8"], "2026-10-28T03:00:00Z", ttl)

    def test_same_origin_redirects_are_not_followed(self):
        report = check_same_origin_redirects(
            "https://example.com/start", ["https://example.com/next"])
        self.assertEqual(report["redirects_previewed"], 1)
        self.assertFalse(report["http_redirects_followed"])
        self.assertFalse(report["authorized_to_crawl"])

    def test_cross_origin_and_non_https_redirects_rejected(self):
        for redirect in ("https://other.example.com/", "http://example.com/"):
            with self.subTest(redirect=redirect), self.assertRaises(ValueError):
                check_same_origin_redirects("https://example.com/", [redirect])
        with self.assertRaises(ValueError):
            check_same_origin_redirects(
                "https://example.com/", ["https://example.com/"] * 6)
        with self.assertRaises(ValueError):
            check_same_origin_redirects(
                "https://example.com/", [], max_hops=True)


if __name__ == "__main__":
    unittest.main()
