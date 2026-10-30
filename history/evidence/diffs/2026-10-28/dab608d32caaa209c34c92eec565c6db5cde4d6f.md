# Commit exact dab608d32caaa209c34c92eec565c6db5cde4d6f

Date UTC 2026-10-28T06:36:38Z; source https://github.com/chainsolutions-wealthtech/Php2shell/commit/dab608d32caaa209c34c92eec565c6db5cde4d6f

Parents: 5e4a37b38759578fb1423047e6ccec0645f105e7

Fichiers 1; +109/-0

## tests/test_http_metadata_normalizer.py (added, +109/-0)

Blob 48c03e953cc0cbbd4548d577b256436bf87f91df; https://github.com/chainsolutions-wealthtech/Php2shell/blob/dab608d32caaa209c34c92eec565c6db5cde4d6f/tests%2Ftest_http_metadata_normalizer.py

```diff
@@ -0,0 +1,109 @@
+"""Local-only HTTP metadata normalization contract; no network or disk."""
+import json
+import socket
+import unittest
+from unittest.mock import patch
+
+from app.http_metadata_normalizer import normalize_untrusted_http_metadata
+from app.public_summary import build_guest_public_summary
+
+
+class UntrustedHttpMetadataTests(unittest.TestCase):
+    def test_canonical_header_names_only(self):
+        evidence = normalize_untrusted_http_metadata(200, [
+            ("Content-Type", "text/html; secret=TOKEN-123"),
+            ("STRICT-TRANSPORT-SECURITY", "max-age=3600"),
+            ("content-type", "text/plain"),
+            ("Set-Cookie", "session=TOP-SECRET"),
+            ("Authorization", "Bearer PRIVATE"),
+        ])
+        self.assertEqual(evidence["response_headers_present"],
+                         ["content-type", "strict-transport-security"])
+        self.assertEqual(evidence["evidence_type"],
+                         "UNVERIFIED_SUPPLIED_PUBLIC_RESPONSE")
+        self.assertNotIn("TOKEN-123", json.dumps(evidence))
+        self.assertNotIn("TOP-SECRET", json.dumps(evidence))
+        self.assertNotIn("PRIVATE", json.dumps(evidence))
+
+    def test_no_headers_is_valid_but_unverified(self):
+        result = normalize_untrusted_http_metadata(404, [])
+        self.assertEqual(result["http_status"], 404)
+        self.assertEqual(result["response_headers_present"], [])
+
+    def test_status_strict_int_and_range(self):
+        for status in (True, False, "200", None, 0, 99, 600, 1000, 200.0):
+            with self.subTest(status=status), self.assertRaises(ValueError):
+                normalize_untrusted_http_metadata(status, [])
+
+    def test_header_container_must_be_bounded(self):
+        for headers in (None, {}, "Content-Type", [("a", "b")] * 65):
+            with self.subTest(headers=str(type(headers))), self.assertRaises(ValueError):
+                normalize_untrusted_http_metadata(200, headers)
+
+    def test_header_pairs_must_be_exact(self):
+        for headers in ([("x",)], [("x", "y", "z")], ["x: y"], [(1, "x")],
+                        [("x", 1)], [[None, "y"]], [{"x": "y"}]):
+            with self.subTest(headers=repr(headers)), self.assertRaises(ValueError):
+                normalize_untrusted_http_metadata(200, headers)
+
+    def test_header_name_must_be_ascii_token(self):
+        for name in ("", "bad name", "bad:header", "é", "x\r\ny",
+                     "a" * 129, "x/y", "x\x00y"):
+            with self.subTest(name=repr(name)), self.assertRaises(ValueError):
+                normalize_untrusted_http_metadata(200, [(name, "safe")])
+
+    def test_value_controls_and_header_injection_rejected(self):
+        for value in ("hello\r\nSet-Cookie: secret", "a\x00b", "a\x7fb", "a\tb"):
+            with self.subTest(value=repr(value)), self.assertRaises(ValueError):
+                normalize_untrusted_http_metadata(200, [("content-type", value)])
+
+    def test_reject_oversized_value_and_total_budget(self):
+        with self.assertRaises(ValueError):
+            normalize_untrusted_http_metadata(200, [("content-type", "x" * 2049)])
+        with self.assertRaises(ValueError):
+            normalize_untrusted_http_metadata(
+                200, [("content-type", "x" * 2048)] * 9)
+
+    def test_unicode_header_value_is_not_reflected(self):
+        evidence = normalize_untrusted_http_metadata(200, [
+            ("content-type", "échantillon"),
+        ])
+        self.assertEqual(evidence["response_headers_present"], ["content-type"])
+        self.assertNotIn("échantillon", json.dumps(evidence, ensure_ascii=False))
+
+    def test_reject_invalid_unicode_surrogate(self):
+        with self.assertRaises(ValueError):
+            normalize_untrusted_http_metadata(200, [
+                ("content-type", "\ud800"),
+            ])
+
+    def test_feeds_guest_summary_without_upgrading_trust(self):
+        evidence = normalize_untrusted_http_metadata(200, [
+            ("Content-Type", "text/html"), ("Content-Security-Policy", "default-src 'self'")
+        ])
+        with patch.object(socket.socket, "connect",
+                          side_effect=AssertionError("network forbidden")):
+            summary = build_guest_public_summary("https://example.com/", evidence)
+        self.assertEqual(summary["status"], "UNVERIFIED_SUPPLIED_EVIDENCE")
+        self.assertFalse(summary["site_contacted"])
+        self.assertFalse(summary["audit_performed"])
+        self.assertFalse(summary["report_stored"])
+        self.assertFalse(summary["vulnerability_confirmed"])
+        self.assertTrue(all(x["evidence_verified"] is False
+                            for x in summary["observations"]))
+
+    def test_no_false_authorization_or_privileged_fields(self):
+        evidence = normalize_untrusted_http_metadata(302, [
+            ("Location", "http://127.0.0.1/private"),
+            ("Set-Cookie", "session=secret"),
+        ])
+        self.assertEqual(set(evidence), {
+            "schema_version", "evidence_type", "http_status",
+            "response_headers_present",
+        })
+        self.assertEqual(evidence["response_headers_present"], [])
+        self.assertNotIn("127.0.0.1", json.dumps(evidence))
+
+
+if __name__ == "__main__":
+    unittest.main()
```

Attention: inspection du diff Git, sans attestation de tests ou d'exploitation.