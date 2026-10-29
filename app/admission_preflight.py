"""Pure, fail-closed authorization-declaration preflight.

The local file is an UNTRUSTED operator declaration, not an MCP/GitHub
authority or an authenticated permission grant. No public or P2 crawl may
be admitted on its strength, even when all fields match.
"""
from datetime import datetime, timezone
import json
from pathlib import Path
import re

from .core import Scope, Target
from .url_intake import preview_url_scope

_MAX_BYTES = 8192
_MAX_DURATION_SECONDS = 86400
_REF = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,79}")
_FIELDS = {
    "schema_version", "declaration_type", "mandate_reference", "subject",
    "asset_hostname", "scope", "not_before_utc", "expires_at_utc",
    "max_pages", "requests_per_minute",
}
_TIME = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")


def _time(value):
    if not isinstance(value, str) or not _TIME.fullmatch(value):
        raise ValueError("Expected UTC timestamp YYYY-MM-DDTHH:MM:SSZ")
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("Invalid UTC timestamp") from exc


def _load(path):
    file = Path(path)
    if (file.is_symlink() or not file.is_file()
            or file.stat().st_size > _MAX_BYTES):
        raise ValueError("Declaration must be a bounded local regular JSON file")
    try:
        claim = json.loads(file.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError, OSError) as exc:
        raise ValueError("Invalid local mandate declaration") from exc
    if not isinstance(claim, dict) or set(claim) != _FIELDS:
        raise ValueError("Unexpected or missing mandate fields")
    if (claim["schema_version"] != "0.2"
            or claim["declaration_type"] != "UNVERIFIED_OPERATOR_MANDATE"):
        raise ValueError("Only unverified operator declarations are supported")
    for key in ("mandate_reference", "subject"):
        if not isinstance(claim[key], str) or not _REF.fullmatch(claim[key]):
            raise ValueError("Malformed mandate identifier")
    if not isinstance(claim["asset_hostname"], str):
        raise ValueError("Invalid mandate hostname")
    normalized_host = Target(claim["asset_hostname"], Scope.PUBLIC).hostname
    if "." not in normalized_host:
        raise ValueError("Mandate hostname needs a DNS suffix")
    try:
        scope = Scope(claim["scope"])
    except (ValueError, TypeError) as exc:
        raise ValueError("Unknown mandate scope") from exc
    valid_from = _time(claim["not_before_utc"])
    valid_until = _time(claim["expires_at_utc"])
    seconds = (valid_until - valid_from).total_seconds()
    if not 0 < seconds <= _MAX_DURATION_SECONDS:
        raise ValueError("Mandate validity interval must be positive and <= 24h")
    if (type(claim["max_pages"]) is not int or not 1 <= claim["max_pages"] <= 100
            or type(claim["requests_per_minute"]) is not int
            or not 1 <= claim["requests_per_minute"] <= 30):
        raise ValueError("Invalid declared mandate budgets")
    return claim, normalized_host, scope, valid_from, valid_until


def evaluate_mandate_declaration(preview, declaration_file, observed_at_utc):
    """Evaluate consistency and temporal limits, NEVER grant permissions."""
    now = _time(observed_at_utc)
    if not isinstance(preview, dict):
        raise ValueError("Expected URL intake preview")
    if preview.get("preview_type") != "OFFLINE_URL_SCOPE_PREVIEW_NOT_ADMISSION":
        raise ValueError("Not a URL preflight preview")
    # Rebuild from the URL rather than trusting attacker-controlled flags in
    # a serialized preview. Requiring an exact match catches forged claims.
    scope = preview.get("declared_scope")
    if scope not in (Scope.PUBLIC.value, Scope.OWNED.value):
        raise ValueError("Invalid URL scope")
    canonical = preview_url_scope(
        preview.get("normalized_url"),
        scope=scope,
        mandate_reference=("DECLARED-BUT-UNVERIFIED" if scope == Scope.OWNED.value else None),
        max_pages=preview.get("max_pages_requested"),
        requests_per_minute=preview.get("requests_per_minute_requested"),
    )
    for field in (
        "normalized_url", "hostname", "base_path", "declared_scope",
        "max_pages_requested", "requests_per_minute_requested",
        "allowed_to_crawl", "allowed_to_inspect_source",
        "mandate_authentication_verified", "target_ownership_verified",
        "dns_and_public_ip_validated", "network_requests_made",
    ):
        if type(preview.get(field)) is not type(canonical[field]) or preview[field] != canonical[field]:
            raise ValueError("Elevated or modified URL preview")

    claim, host, declared_scope, issued, expires = _load(declaration_file)
    blockers = []
    if host != preview["hostname"]:
        blockers.append("HOSTNAME_MISMATCH")
    if declared_scope.value != scope:
        blockers.append("SCOPE_MISMATCH")
    if now < issued:
        blockers.append("NOT_YET_VALID")
    if now >= expires:
        blockers.append("EXPIRED")
    if preview["max_pages_requested"] > claim["max_pages"]:
        blockers.append("PAGE_BUDGET_EXCEEDED")
    if preview["requests_per_minute_requested"] > claim["requests_per_minute"]:
        blockers.append("RATE_BUDGET_EXCEEDED")
    if scope == Scope.OWNED.value and not preview.get("operator_mandate_supplied"):
        blockers.append("MISSING_P2_REFERENCE")
    # Even a matching claim is not an authenticated authority decision.
    return {
        "schema_version": "0.2",
        "evaluation_type": "OFFLINE_MANDATE_DECLARATION_PREFLIGHT_NOT_AUTHORIZATION",
        "observed_at_utc": observed_at_utc,
        "hostname": preview["hostname"],
        "declared_scope": scope,
        "declaration_present": True,
        "declaration_matches_request": not blockers,
        "declaration_validity_window_matched": issued <= now < expires,
        "blockers": blockers,
        "mandate_signature_verified": False,
        "subject_authenticated": False,
        "asset_ownership_verified": False,
        "mcp_claim_verified": False,
        "network_peer_verified": False,
        "authorized_to_crawl": False,
        "authorized_to_inspect_source": False,
        "ready_for_production": False,
        "limitations": (
            "Local mandate data is untrusted and cannot authorize public "
            "HTTP crawling, source inspection, PHP execution, PHPPATCH or "
            "production operations. A future verifier must consult existing "
            "MCP identities, mandates, claims, revocations and expiry."
        ),
    }


# Additive contract, intentionally NON-executable. It consumes only the
# existing *unverified* local preflight object and can NEVER grant a right.
# Trusted identity, revocation, signature, project ACL, claims and delegation
# must later be read from the authorized MCP control plane, not client JSON.
_ACTION_GATES = {
    "public_crawl": (
        "SUBJECT_IDENTITY_AUTHENTICATED",
        "P1_TARGET_SCOPE_ADMITTED",
        "LIVE_DNS_PEER_AND_REDIRECT_POLICY",
        "MCP_CLAIM_AND_BUDGET_VERIFIED",
    ),
    "source_read": (
        "SUBJECT_IDENTITY_AUTHENTICATED",
        "P2_SOURCE_DELEGATION_VERIFIED",
        "PROJECT_RESOURCE_ACL_VERIFIED",
        "MCP_CLAIM_AND_EXPIRY_VERIFIED",
    ),
    "patch_propose": (
        "SUBJECT_IDENTITY_AUTHENTICATED",
        "P2_SOURCE_DELEGATION_VERIFIED",
        "EVIDENCE_AND_PROJECT_BOUND",
        "ISOLATED_CANDIDATE_PREPARED",
        "MCP_CLAIM_AND_EXPIRY_VERIFIED",
    ),
    "patch_apply": (
        "SUBJECT_IDENTITY_AUTHENTICATED",
        "P2_SOURCE_DELEGATION_VERIFIED",
        "SANDBOX_REGRESSION_AND_ROLLBACK_VERIFIED",
        "INDEPENDENT_PATCH_APPROVAL",
        "MCP_CLAIM_AND_EXPIRY_VERIFIED",
    ),
    "deploy": (
        "SUBJECT_IDENTITY_AUTHENTICATED",
        "PROJECT_RESOURCE_ACL_VERIFIED",
        "EXACT_SHA_CI_AND_RELEASE_GATES",
        "INDEPENDENT_DEPLOYMENT_APPROVAL",
        "GOVERNED_MCP_DEPLOY_MANDATE_AND_CLAIM",
    ),
}
_KNOWN_BLOCKERS = {
    "HOSTNAME_MISMATCH", "SCOPE_MISMATCH", "NOT_YET_VALID", "EXPIRED",
    "PAGE_BUDGET_EXCEEDED", "RATE_BUDGET_EXCEEDED", "MISSING_P2_REFERENCE",
}
_UNTRUSTED_FALSE_FLAGS = (
    "mandate_signature_verified", "subject_authenticated",
    "asset_ownership_verified", "mcp_claim_verified",
    "network_peer_verified", "authorized_to_crawl",
    "authorized_to_inspect_source", "ready_for_production",
)


def evaluate_action_gates(declaration_preflight, action):
    """Describe future P1/P2 authorization gates, always DENY.

    A local operator declaration, even if its dates/scope match, can never be
    an authenticated session, a source-access grant or a production approval.
    No calls to MCP or the network occur; this is a machine-readable contract
    for future *trusted* policy enforcement only.
    """
    if not isinstance(action, str) or action not in _ACTION_GATES:
        raise ValueError("Unknown protected operation")
    p = declaration_preflight
    if (not isinstance(p, dict)
            or p.get("schema_version") != "0.2"
            or p.get("evaluation_type")
            != "OFFLINE_MANDATE_DECLARATION_PREFLIGHT_NOT_AUTHORIZATION"
            or p.get("declared_scope")
            not in (Scope.PUBLIC.value, Scope.OWNED.value)
            or type(p.get("declaration_matches_request")) is not bool
            or type(p.get("declaration_validity_window_matched")) is not bool
            or type(p.get("declaration_present")) is not bool
            or not p["declaration_present"]):
        raise ValueError("Not a valid untrusted declaration preflight")
    if any(type(p.get(flag)) is not bool or p[flag]
           for flag in _UNTRUSTED_FALSE_FLAGS):
        raise ValueError("Forged authority elevation in local preflight")
    blockers = p.get("blockers")
    if (not isinstance(blockers, list)
            or any(not isinstance(b, str) or b not in _KNOWN_BLOCKERS
                   for b in blockers)
            or len(blockers) != len(set(blockers))):
        raise ValueError("Unexpected preflight blockers")
    if (p["declaration_matches_request"] != (len(blockers) == 0)
            or (not p["declaration_validity_window_matched"]
                and not any(x in blockers for x in ("EXPIRED", "NOT_YET_VALID")))):
        raise ValueError("Inconsistent unverified preflight")
    return {
        "schema_version": "0.2",
        "decision_type": "OFFLINE_AUTHORIZATION_GATES_NOT_ADMISSION",
        "decision": "DENY_UNVERIFIED_AUTHORITY",
        "action": action,
        "declared_scope": p["declared_scope"],
        "blockers": list(blockers),
        "required_gates": list(_ACTION_GATES[action]),
        "identity_authenticated": False,
        "mandate_verified": False,
        "mcp_claim_verified": False,
        "authorized": False,
        "execution_enabled": False,
        "ready_for_production": False,
        "limitations": (
            "This contract has no trusted issuer, verified subject, "
            "delegated asset authorization, proof of possession, revocation "
            "check, approval or MCP claim. It is not an access token or "
            "a policy decision allowing execution."
        ),
    }
