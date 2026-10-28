"""Bind existing offline Ed25519 verification to canonical URL intake.

This is a NON-EXECUTING adapter, not a user login, token issuer, ACL service,
MCP runtime claim provider or crawler. All parameters labelled 'trusted' must
ultimately originate from a secure backend (IdP session, project registry and
issuer trust store) and NEVER from browser-controlled input.
"""
from .signed_attestation import verify_external_attestation
from .url_intake import preview_url_scope


_ACTION_SCOPE = {
    "public_crawl": "public_metadata",
    "source_read": "owned_source",
    "patch_propose": "owned_source",
    "patch_apply": "owned_source",
    "deploy": "owned_source",
}


def verify_scoped_attestation_preflight(
        *, url, declared_scope, action,
        subject_from_trusted_session, project_from_trusted_registry,
        mandate_reference=None, max_pages=20, requests_per_minute=6,
        external_attestation, trusted_public_keys, expected_issuer,
        expected_audience, observed_at_epoch, revocation_checker):
    """Verify request/attestation consistency without authorizing operations.

    'Trusted' inputs are an integration obligation, NOT a claim that those
    authorities are already available or configured in this prototype.
    """
    # Do not interpolate the untrusted URL/token into any error or response.
    try:
        if (not isinstance(action, str)
                or action not in _ACTION_SCOPE
                or declared_scope != _ACTION_SCOPE[action]):
            raise ValueError("Invalid action/scope")
        preview = preview_url_scope(
            url, scope=declared_scope, mandate_reference=mandate_reference,
            max_pages=max_pages, requests_per_minute=requests_per_minute)
        binding = {
            "subject": subject_from_trusted_session,
            "project_id": project_from_trusted_registry,
            "asset_hostname": preview["hostname"],
            "base_path": preview["base_path"],
            "scope": preview["declared_scope"],
            "action": action,
        }
        if action == "public_crawl":
            binding["max_pages"] = preview["max_pages_requested"]
            binding["requests_per_minute"] = preview["requests_per_minute_requested"]
        else:
            # A P2 declaration is never trust evidence. Verify it is the
            # very same reference in the externally signed attestation.
            binding["mandate_id"] = mandate_reference
        decision = verify_external_attestation(
            external_attestation,
            trusted_public_keys=trusted_public_keys,
            expected_issuer=expected_issuer,
            expected_audience=expected_audience,
            request_binding=binding,
            observed_at_epoch=observed_at_epoch,
            revocation_checker=revocation_checker,
        )
    except (ValueError, TypeError, KeyError) as exc:
        raise ValueError("Scoped attestation preflight refused") from None

    # Do not return subject/mandate identifiers, URLs, raw claims or JWTs.
    # The trusted verification decision is STILL not runtime authorization.
    if (decision.get("decision") !=
            "VERIFIED_ATTESTATION_NOT_EXECUTION_ADMISSION"
            or decision.get("authorized") is not False
            or decision.get("execution_enabled") is not False):
        raise ValueError("Scoped attestation preflight refused")
    return {
        "schema_version": "0.2",
        "verification_type": "SIGNED_URL_SCOPE_PREFLIGHT_NOT_ADMISSION",
        "signature_verified": True,
        "request_bound": True,
        "revocation_checked": True,
        "authorized": False,
        "execution_enabled": False,
        "user_session_authenticated": False,
        "project_acl_verified": False,
        "mcp_claim_verified": False,
        "ready_for_production": False,
        "missing_gates": [
            "TRUSTED_IDP_SESSION",
            "TRUSTED_PROJECT_AND_ASSET_ACL",
            "APPROVED_ISSUER_KEY_ROTATION_AND_LIVE_REVOCATION",
            "MCP_RUNTIME_MANDATE_AND_CLAIM",
            "NETWORK_SSRF_RATE_LIMIT_AND_APPROVAL",
        ],
    }
