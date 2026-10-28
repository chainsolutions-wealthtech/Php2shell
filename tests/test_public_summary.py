"""RED tests: anonymous short public summary, never a fabricated live scan.

All HTTP evidence is deliberately caller-supplied and unverified. This
module never performs HTTP, checks an actual website, stores a report, or
claims the user owns a target.
"""
import json
import socket
import unittest
from unittest.mock import patch

from app.public_summary import build_guest_public_summary


URL = "https://example.com/site/"
EVIDENCE = {
    "schema_version": "0.2",
    "evidence_type": "UNVERIFIED_SUPPLIED_PUBLIC_RESPONSE",
    "http_status": 200,
    "response_headers_present": [
        "content-type", "x-content-type-options"
    ],
}


class GuestPublicSummaryTests(unittest.TestCase):
    def test_url_only_never_fabricates_live_audit(self):
        with patch.object(socket.socket, "connect", side_effect=AssertionError("network")):
            d = build_guest_public_summary(URL)
        self.assertEqual(d["status"], "NOT_ANALYZED")
        self.assertEqual(d["hostname"], "example.com")
        self.assertEqual(d["summary_type"], "ANONYMOUS_SHORT_PREVIEW")
        self.assertEqual(d["observations"], [])
        self.assertFalse(d["site_contacted"])
        self.assertFalse(d["audit_performed"])
        self.assertFalse(d["detailed_report_available"])
        self.assertFalse(d["report_stored"])
        self.assertTrue(d["account_required_for_report_storage"])

    def test_supplied_evidence_yields_short_unverified_observations(self):
        result = build_guest_public_summary(URL, EVIDENCE)
        self.assertEqual(result["status"], "UNVERIFIED_SUPPLIED_EVIDENCE")
        self.assertLessEqual(len(result["observations"]), 3)
        self.assertTrue(result["observations"])
        self.assertTrue(all(i["evidence_verified"] is False
                            for i in result["observations"]))
        self.assertFalse(result["site_contacted"])
        self.assertFalse(result["audit_performed"])
        self.assertFalse(result["report_stored"])
        self.assertFalse(result["site_ownership_verified"])
        self.assertFalse(result["vulnerability_confirmed"])
        self.assertNotIn("CVE-", json.dumps(result))

    def test_evidence_cannot_claim_privileged_actions(self):
        for injected in (
            {"report_stored": True}, {"audit_performed": True},
            {"site_ownership_verified": True}, {"source_code": "<?php"},
            {"authenticated": True}, {"severity": "critical"},
            {"evidence_type": "TRUSTED_HTTP_COLLECTOR"},
        ):
            with self.subTest(injected=injected), self.assertRaises(ValueError):
                build_guest_public_summary(URL, dict(EVIDENCE, **injected))

    def test_malformed_or_local_urls_rejected(self):
        for url in (
            "http://example.com/", "https://127.0.0.1/",
            "https://localhost/", "https://user:pass@example.com/",
            "https://example.com/%2e%2e/",
        ):
            with self.subTest(url=url), self.assertRaises(ValueError):
                build_guest_public_summary(url)

    def test_no_header_value_or_secret_reflection(self):
        bad = dict(EVIDENCE, response_headers_present=[
            "content-security-policy: secret-token=abc"
        ])
        with self.assertRaises(ValueError):
            build_guest_public_summary(URL, bad)
        d = build_guest_public_summary(URL, EVIDENCE)
        self.assertNotIn("secret", json.dumps(d).lower())
        self.assertNotIn("cookie", json.dumps(d).lower())

    def test_reject_duplicate_unknown_noncanonical_headers_and_status(self):
        for headers in (
            ["content-type", "content-type"],
            ["Content-Type"],
            ["set-cookie"],
            ["server"],
            ["x-custom-header"],
        ):
            with self.subTest(headers=headers), self.assertRaises(ValueError):
                build_guest_public_summary(
                    URL, dict(EVIDENCE, response_headers_present=headers))
        for status in (True, "200", 0, 99, 600):
            with self.subTest(status=status), self.assertRaises(ValueError):
                build_guest_public_summary(URL, dict(EVIDENCE, http_status=status))

    def test_untrusted_evidence_requires_complete_strict_shape(self):
        for key in EVIDENCE:
            invalid = dict(EVIDENCE)
            invalid.pop(key)
            with self.subTest(key=key), self.assertRaises(ValueError):
                build_guest_public_summary(URL, invalid)

    def test_anonymous_preview_is_not_a_detailed_persistent_report(self):
        result = build_guest_public_summary(URL, EVIDENCE)
        self.assertEqual(result["next_action"], "SIGN_IN_FOR_PERSISTENT_DETAILED_REPORT")
        self.assertFalse(result["can_read_private_source"])
        self.assertFalse(result["can_patch"])
        self.assertFalse(result["can_deploy"])
        self.assertFalse(result["can_read_detailed_report"])

    def test_does_not_use_disk_or_network_for_evidence_processing(self):
        with patch.object(socket.socket, "connect", side_effect=AssertionError("network")):
            data = build_guest_public_summary(URL, EVIDENCE)
        self.assertEqual(data["status"], "UNVERIFIED_SUPPLIED_EVIDENCE")
        self.assertFalse(data["network_requests_made"])


if __name__ == "__main__":
    unittest.main()
