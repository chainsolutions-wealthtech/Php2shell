"""Bounded public GitHub advisory acquisition for already-curated PHP GHSAs.

Network access occurs ONLY when this function is explicitly invoked. There is
no arbitrary URL input, no target website interaction, no redirects or proxy,
no credentials, no local writes and no automatic catalog promotion.
"""
from datetime import date, datetime, timezone
from hashlib import sha256
import json
import re
import ssl
from urllib.error import HTTPError, URLError
from urllib.request import (
    HTTPRedirectHandler, HTTPSHandler, ProxyHandler, Request, build_opener,
)

from .security_advisories import load_advisory_catalog

_GHSA = re.compile(r"GHSA-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}")
_API_ORIGIN = "https://api.github.com"
_MAX_RESPONSE_BYTES = 128_000
_ALLOWED_SEVERITIES = {"low", "medium", "moderate", "high", "critical"}


class _NoRedirects(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


def _date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError("Observation date must be YYYY-MM-DD")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("Invalid observation calendar date") from exc


def _utc_timestamp(value, field):
    if not isinstance(value, str) or len(value) > 40 or not value.endswith("Z"):
        raise ValueError(f"Invalid {field} in upstream advisory")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"Invalid {field} in upstream advisory") from exc
    if dt.tzinfo is None or dt.utcoffset().total_seconds() != 0:
        raise ValueError(f"Invalid {field} timezone")
    return dt.astimezone(timezone.utc)


def _https_opener():
    # Disable environment proxies and all redirects, use OS trusted roots.
    return build_opener(
        ProxyHandler({}),
        HTTPSHandler(context=ssl.create_default_context()),
        _NoRedirects(),
    )


def _read_bounded_response(opener, ghsa):
    endpoint = f"{_API_ORIGIN}/advisories/{ghsa}"
    request = Request(endpoint, headers={
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2026-03-10",
        "User-Agent": "PHP2SHELL-Defensive-Advisory-Review/0.2",
    }, method="GET")
    try:
        with opener.open(request, timeout=8.0) as response:
            if response.status != 200:
                raise ValueError("Official advisory endpoint returned non-200 status")
            content_type = response.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()
            if content_type not in {"application/json", "application/vnd.github+json"}:
                raise ValueError("Unexpected official API content type")
            length = response.headers.get("Content-Length")
            if length is not None:
                if not length.isdecimal() or int(length) > _MAX_RESPONSE_BYTES:
                    raise ValueError("Advisory API body exceeds maximum permitted size")
            raw = response.read(_MAX_RESPONSE_BYTES + 1)
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        # Do not leak credentials, proxy settings or response bodies in errors.
        raise ValueError("Official GitHub advisory request failed or was rejected") from exc
    if len(raw) > _MAX_RESPONSE_BYTES:
        raise ValueError("Advisory API body exceeds maximum permitted size")
    try:
        data = json.loads(raw.decode("utf-8"))
    except (UnicodeError, ValueError) as exc:
        raise ValueError("Malformed upstream GitHub advisory JSON") from exc
    if not isinstance(data, dict):
        raise ValueError("Upstream advisory must be a JSON object")
    return data, sha256(raw).hexdigest(), endpoint


def fetch_curated_php_advisory(ghsa, as_of_utc, *, opener=None):
    """Get public metadata from the fixed official API for a known GHSA only.

    This is NOT vendor backport verification, PHP runtime attestation,
    exploitability analysis, or permission to update the canonical catalog.
    """
    observed_date = _date(as_of_utc)
    if not isinstance(ghsa, str) or not _GHSA.fullmatch(ghsa):
        raise ValueError("Expected a valid GHSA identifier")
    catalog = load_advisory_catalog()
    matches = [x for x in catalog["advisories"] if x["ghsa"] == ghsa]
    if len(matches) != 1:
        raise ValueError("Only GHSA identifiers already admitted to the curated catalog can be fetched")
    reference = matches[0]
    response, digest, endpoint = _read_bounded_response(
        _https_opener() if opener is None else opener, ghsa
    )
    if response.get("ghsa_id") != ghsa or response.get("cve_id") != reference["cve"]:
        raise ValueError("Official response GHSA or CVE does not match catalog reference")
    expected_html = {
        f"https://github.com/advisories/{ghsa}",
        f"https://github.com/php/php-src/security/advisories/{ghsa}",
    }
    if response.get("html_url") not in expected_html:
        raise ValueError("Official response has an unexpected advisory HTML URL")
    if "url" in response and response["url"] != endpoint:
        raise ValueError("Upstream API URL conflicts with requested endpoint")
    if response.get("type") not in {"reviewed", "unreviewed"}:
        raise ValueError("Unexpected global advisory type")
    severity = response.get("severity")
    if severity not in _ALLOWED_SEVERITIES:
        raise ValueError("Unknown upstream advisory severity")
    published = _utc_timestamp(response.get("published_at"), "published_at")
    updated = _utc_timestamp(response.get("updated_at"), "updated_at")
    if updated < published:
        raise ValueError("Upstream update precedes publication")
    if updated.date() > observed_date:
        raise ValueError("Upstream update date exceeds explicit observation date")
    withdrawn_value = response.get("withdrawn_at")
    withdrawn = withdrawn_value is not None
    if withdrawn:
        withdrawn_at = _utc_timestamp(withdrawn_value, "withdrawn_at")
        if withdrawn_at < published or withdrawn_at.date() > observed_date:
            raise ValueError("Invalid upstream withdrawal date")

    drift = []
    if severity != reference["severity"]:
        drift.append("severity")
    if response["type"] != "reviewed":
        drift.append("review_status")
    if withdrawn:
        drift.append("withdrawn")
    return {
        "schema_version": "0.2",
        "fetch_type": "PUBLIC_OFFICIAL_GITHUB_ADVISORY_METADATA_NOT_ASSET_DIAGNOSIS",
        "network_request_performed": True,
        "data_source": "GitHub global security advisories REST API",
        "request_endpoint": endpoint,
        "observed_as_of_utc": as_of_utc,
        "ghsa": ghsa,
        "cve": reference["cve"],
        "upstream_html_url": response["html_url"],
        "upstream_published_at": response["published_at"],
        "upstream_updated_at": response["updated_at"],
        "upstream_severity": severity,
        "upstream_review_type": response["type"],
        "upstream_withdrawn": withdrawn,
        "raw_response_sha256": digest,
        "catalog_reviewed_on_utc": catalog["reviewed_on_utc"],
        "metadata_drift_fields": drift,
        "proposed_action": ("BLOCK_FOR_INDEPENDENT_REVIEW" if drift else
                            "REVIEW_UPSTREAM_METADATA_ONLY"),
        "canonical_catalog_modified": False,
        "independent_upstream_reverification_required": True,
        "asset_applicability": "insufficient_evidence",
        "limitations": (
            "Bounded metadata lookup from GitHub API, not an authenticated "
            "vendor-specific attestation or approval. Does not validate "
            "backported packages, fixed version ranges, installed runtime, "
            "SAPI, exploitability, or any URL-based asset. No patch deployed."
        ),
    }
