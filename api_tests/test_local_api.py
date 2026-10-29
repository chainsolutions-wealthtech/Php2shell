"""ASGI contract tests: no real network, scanning, approval or deployment."""
import os
import socket
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from service.local_api import app


def client(*, peer="127.0.0.1", host="127.0.0.1"):
    return TestClient(
        app, base_url="http://" + host, client=(peer, 50203),
        raise_server_exceptions=True,
    )


class LocalApiContractTests(unittest.TestCase):
    def test_health_does_not_claim_running_scan_or_production(self):
        with client() as api:
            res = api.get("/health")
            self.assertEqual(res.status_code, 200)
            self.assertFalse(res.json()["ready_for_production"])
            self.assertFalse(res.json()["real_audit_enabled"])
            self.assertFalse(res.json()["real_patch_enabled"])
            self.assertEqual(res.headers["cache-control"], "no-store")
            self.assertEqual(res.headers["x-frame-options"], "DENY")

    def test_all_mutating_capabilities_remain_disabled(self):
        with client() as api:
            res = api.get("/api/v0.2/capabilities")
            self.assertEqual(res.status_code, 200)
            self.assertTrue(res.json()["url_preview_offline"])
            for key in (
                "authenticated_user", "mandate_verified",
                "dns_connection_enforced", "crawl_enabled",
                "source_inspection_enabled", "phppatch_enabled",
                "deployment_enabled", "api_production_ready",
            ):
                self.assertIs(res.json()[key], False)

    def test_preview_disabled_by_default_and_requires_loopback(self):
        request = {"url": "https://example.com/"}
        with patch.dict(os.environ, {"P2S_ENABLE_LOCAL_API_PREVIEW": "0"}):
            with client() as api:
                res = api.post("/api/v0.2/url/preview", json=request)
                self.assertEqual(res.status_code, 403)
        with patch.dict(os.environ, {"P2S_ENABLE_LOCAL_API_PREVIEW": "1"}):
            with client(peer="192.0.2.3") as api:
                res = api.post("/api/v0.2/url/preview", json=request)
                self.assertEqual(res.status_code, 403)

    def test_loopback_preview_never_admits_audit(self):
        with patch.dict(os.environ, {"P2S_ENABLE_LOCAL_API_PREVIEW": "1"}):
            with patch.object(socket.socket, "connect", side_effect=AssertionError("network")):
                with client() as api:
                    res = api.post("/api/v0.2/url/preview", json={
                        "url": "https://www.example.com/about/",
                        "scope": "public_metadata",
                        "max_pages": 12,
                        "requests_per_minute": 4,
                    })
        self.assertEqual(res.status_code, 200)
        obj = res.json()
        self.assertEqual(obj["preview_type"], "OFFLINE_URL_SCOPE_PREVIEW_NOT_ADMISSION")
        self.assertEqual(obj["hostname"], "www.example.com")
        self.assertEqual(obj["max_pages_requested"], 12)
        self.assertFalse(obj["allowed_to_crawl"])
        self.assertFalse(obj["allowed_to_inspect_source"])
        self.assertFalse(obj["dns_and_public_ip_validated"])
        self.assertFalse(obj["mandate_authentication_verified"])
        self.assertFalse(obj["network_requests_made"])

    def test_p2_scope_is_not_available_without_real_mandate(self):
        with patch.dict(os.environ, {"P2S_ENABLE_LOCAL_API_PREVIEW": "1"}):
            with client() as api:
                res = api.post("/api/v0.2/url/preview", json={
                    "url": "https://example.com/",
                    "scope": "owned_source",
                })
        self.assertEqual(res.status_code, 422)
        self.assertEqual(res.json(), {"error": "INVALID_REQUEST"})

    def test_invalid_urls_and_unknown_fields_are_never_echoed(self):
        secret = "https://private:SECRET_TOKEN@example.com/"
        with patch.dict(os.environ, {"P2S_ENABLE_LOCAL_API_PREVIEW": "1"}):
            with client() as api:
                a = api.post("/api/v0.2/url/preview", json={"url": secret})
                b = api.post("/api/v0.2/url/preview", json={
                    "url": "https://example.com",
                    "authorization": "SECRET_TOKEN",
                })
                c = api.post("/api/v0.2/url/preview", json={
                    "url": "https://example.com",
                    "max_pages": True,
                })
        self.assertEqual(a.status_code, 422)
        self.assertEqual(b.status_code, 422)
        self.assertEqual(c.status_code, 422)
        self.assertNotIn("SECRET_TOKEN", a.text + b.text + c.text)

    def test_no_unimplemented_scan_patch_or_docs_endpoints(self):
        with client() as api:
            for route in (
                "/openapi.json", "/docs", "/redoc",
                "/api/v0.2/audit/start", "/api/v0.2/phppatch/approve",
            ):
                with self.subTest(route=route):
                    result = api.get(route)
                    self.assertEqual(result.status_code, 404)

    def test_request_body_limit_denies_oversized_preview(self):
        with patch.dict(os.environ, {"P2S_ENABLE_LOCAL_API_PREVIEW": "1"}):
            with client() as api:
                result = api.post("/api/v0.2/url/preview", content=b" " * 4200,
                                  headers={"Content-Type": "application/json"})
        self.assertEqual(result.status_code, 413)
        self.assertEqual(result.json()["error"], "REQUEST_TOO_LARGE")

    def test_host_header_must_be_local(self):
        with client(host="untrusted.example.com") as api:
            response = api.get("/health")
        self.assertEqual(response.status_code, 400)


    def test_chunked_actual_body_limit_without_content_length(self):
        """A streaming caller must not bypass the 4 KiB cap by omitting Content-Length."""
        with patch.dict(os.environ, {"P2S_ENABLE_LOCAL_API_PREVIEW": "1"}):
            with client() as api:
                response = api.post(
                    "/api/v0.2/url/preview",
                    content=iter([b" " * 2500, b" " * 1700]),
                    headers={"Content-Type": "application/json"},
                )
        self.assertEqual(response.status_code, 413)
        self.assertEqual(response.json(), {"error": "REQUEST_TOO_LARGE"})
        self.assertEqual(response.headers["cache-control"], "no-store")

    def test_actual_body_limit_defeats_forged_small_length(self):
        """ASGI must enforce bytes received, not just an untrusted declared length."""
        with patch.dict(os.environ, {"P2S_ENABLE_LOCAL_API_PREVIEW": "1"}):
            with client() as api:
                response = api.post(
                    "/api/v0.2/url/preview",
                    content=b" " * 4200,
                    headers={"Content-Type": "application/json",
                             "Content-Length": "8"},
                )
        self.assertEqual(response.status_code, 413)
        self.assertEqual(response.json(), {"error": "REQUEST_TOO_LARGE"})
        self.assertEqual(response.headers["x-content-type-options"], "nosniff")

    def test_chunked_small_body_remains_functional(self):
        """Within the cap, chunked JSON must still reach the existing preview contract."""
        with patch.dict(os.environ, {"P2S_ENABLE_LOCAL_API_PREVIEW": "1"}):
            with client() as api:
                response = api.post(
                    "/api/v0.2/url/preview",
                    content=iter([b'{"url":', b'"https://example.com/"}']),
                    headers={"Content-Type": "application/json"},
                )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()["allowed_to_crawl"])


if __name__ == "__main__":
    unittest.main()
