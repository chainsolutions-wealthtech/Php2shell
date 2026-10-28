"""Local-only FastAPI prototype. Importing this module opens no sockets.

No real user identity, P1/P2 mandate, role or project ownership is verified;
therefore this API MUST NOT start a crawler, scan, patch or deploy. Only a
request/response contract for read-only URL parsing is exposed for tests.
"""
from ipaddress import ip_address
import os

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field

from app.url_intake import preview_url_scope
from app.public_summary import build_guest_public_summary


class PreviewRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    url: str = Field(min_length=1, max_length=2048)
    scope: str = Field(default="public_metadata", pattern=r"^public_metadata$")
    max_pages: int = Field(default=20, ge=1, le=100)
    requests_per_minute: int = Field(default=6, ge=1, le=30)


app = FastAPI(
    title="PHP2SHELL local contract prototype",
    version="0.2",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["127.0.0.1", "localhost", "[::1]", "testserver"],
)


@app.middleware("http")
async def privacy_headers(request: Request, call_next):
    # A request body over 4 KiB has no place in a tiny preview endpoint.
    # Header check alone is not an enforcement guarantee for streaming clients;
    # a hardened reverse proxy must enforce actual bytes on future deployment.
    if request.method in {"POST", "PUT", "PATCH"}:
        length = request.headers.get("content-length")
        if length is not None:
            if not length.isdecimal() or int(length) > 4096:
                response = JSONResponse({"error": "REQUEST_TOO_LARGE"}, status_code=413)
                response.headers["Cache-Control"] = "no-store"
                return response
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    return response


@app.exception_handler(RequestValidationError)
async def hide_validation_input(request: Request, exc: RequestValidationError):
    # Pydantic's default 422 error may reflect private URLs or credentials.
    return JSONResponse({"error": "INVALID_REQUEST"}, status_code=422)


@app.get("/health")
async def health():
    return {
        "service": "php2shell-local-api-prototype",
        "status": "CONTRACT_ONLY_NOT_DEPLOYED",
        "ready_for_production": False,
        "real_audit_enabled": False,
        "real_patch_enabled": False,
    }


@app.get("/api/v0.2/capabilities")
async def capabilities():
    return {
        "url_preview_offline": True,
        "authenticated_user": False,
        "mandate_verified": False,
        "dns_connection_enforced": False,
        "crawl_enabled": False,
        "source_inspection_enabled": False,
        "phppatch_enabled": False,
        "deployment_enabled": False,
        "api_production_ready": False,
    }


def _is_loopback_peer(request: Request) -> bool:
    try:
        return request.client is not None and ip_address(request.client.host).is_loopback
    except ValueError:
        return False


@app.post("/api/v0.2/url/preview")
async def preview_url(payload: PreviewRequest, request: Request):
    # Environment flag is a LOCAL DEVELOPMENT switch, not an authorization.
    # Loopback peer is an additional barrier, not a substitute for future
    # authentication, revocation, scoped mandate or production proxies.
    if os.getenv("P2S_ENABLE_LOCAL_API_PREVIEW") != "1" or not _is_loopback_peer(request):
        raise HTTPException(status_code=403, detail="PREVIEW_NOT_AVAILABLE")
    try:
        return preview_url_scope(
            payload.url,
            scope=payload.scope,
            max_pages=payload.max_pages,
            requests_per_minute=payload.requests_per_minute,
        )
    except ValueError as exc:
        # Do not echo full operator-supplied URL/hostname in 422 exceptions.
        raise HTTPException(status_code=422, detail="INVALID_URL_PREVIEW") from exc


class GuestSummaryRequest(BaseModel):
    """Strict local-only prototype; external evidence is always UNVERIFIED."""
    model_config = ConfigDict(extra="forbid", strict=True)

    url: str = Field(min_length=1, max_length=2048)
    public_response_evidence: dict[str, object] | None = None


@app.post("/api/v0.2/guest/summary")
async def guest_short_summary(payload: GuestSummaryRequest, request: Request):
    """Return an honest public *preview*, never an audit or stored report."""
    if (os.getenv("P2S_ENABLE_LOCAL_GUEST_SUMMARY") != "1"
            or not _is_loopback_peer(request)):
        raise HTTPException(status_code=403, detail="GUEST_SUMMARY_NOT_AVAILABLE")
    try:
        return build_guest_public_summary(
            payload.url, payload.public_response_evidence)
    except (ValueError, TypeError) as exc:
        raise HTTPException(status_code=422, detail="INVALID_GUEST_PREVIEW") from exc


class _ActualBodyLimitMiddleware:
    """ASGI request-body bound, independent of Content-Length and chunk framing.

    This contract-only application is never a deployment target. The adapter
    buffers at most 4 KiB; streaming traffic larger than the bound is rejected
    before Pydantic or endpoint code processes the untrusted body. It must not
    be presented as a production reverse-proxy size/rate limit.
    """

    MAX_BODY_BYTES = 4096

    def __init__(self, app):
        self.app = app

    @staticmethod
    async def reject(scope, receive, send):
        response = JSONResponse(
            {"error": "REQUEST_TOO_LARGE"},
            status_code=413,
            headers={
                "Cache-Control": "no-store",
                "X-Content-Type-Options": "nosniff",
                "X-Frame-Options": "DENY",
            },
        )
        await response(scope, receive, send)

    async def __call__(self, scope, receive, send):
        if (scope["type"] != "http"
                or scope.get("method") not in {"POST", "PUT", "PATCH"}):
            return await self.app(scope, receive, send)

        # Duplicate/malformed declared lengths are ambiguous even when a
        # frontend proxy has already accepted the request.
        lengths = [
            value for key, value in scope.get("headers", [])
            if key.lower() == b"content-length"
        ]
        if len(lengths) > 1 or (
            lengths and (
                not lengths[0].isascii() or not lengths[0].isdigit()
                or len(lengths[0]) > 5 or int(lengths[0]) > self.MAX_BODY_BYTES
            )
        ):
            return await self.reject(scope, receive, send)

        total = 0
        parts = []
        while True:
            event = await receive()
            if event["type"] == "http.disconnect":
                return
            if event["type"] != "http.request":
                return
            chunk = event.get("body", b"")
            total += len(chunk)
            if total > self.MAX_BODY_BYTES:
                return await self.reject(scope, receive, send)
            parts.append(chunk)
            if not event.get("more_body", False):
                break

        # Replay exactly one small bounded body to the existing FastAPI/ASGI
        # contract. Further reads go to the original transport for disconnect.
        initial = True

        async def bounded_receive():
            nonlocal initial
            if initial:
                initial = False
                return {
                    "type": "http.request",
                    "body": b"".join(parts),
                    "more_body": False,
                }
            return await receive()

        return await self.app(scope, bounded_receive, send)


# Installed last so the byte-boundary executes before request parsing and
# the existing privacy/TrustedHost checks. No listener is started by import.
app.add_middleware(_ActualBodyLimitMiddleware)
