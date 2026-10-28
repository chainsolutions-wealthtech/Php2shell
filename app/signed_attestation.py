"""Verify an EXTERNALLY signed P1/P2 attestation in a local offline contract.

This module contains NO issuer, signer, trusted keys, MCP credentials, session,
network client, authorization grant, scanner, patch or deployment code.

A production control plane must supply pinned key material, trusted
issuer/audience, request binding and a live revocation provider from its own
secure configuration, NOT from an HTTP payload or the untrusted site owner.
Even successful cryptographic verification is NOT admission to execute.
"""
import base64
import binascii
import json
import re

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey


_ATT_TYPE = "p2s-mcp-attestation+jwt"
_HEADER = frozenset({"typ", "alg", "kid"})
_CLAIMS = frozenset({
    "iss", "aud", "sub", "project_id", "asset_hostname", "scope",
    "action", "mandate_id", "iat", "nbf", "exp", "jti",
})
_BINDING = frozenset({
    "subject", "project_id", "asset_hostname", "scope", "action",
})
_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,79}\Z", re.ASCII)
_B64 = re.compile(r"[A-Za-z0-9_-]+\Z", re.ASCII)
_ACTIONS = {
    "public_crawl": "public_metadata",
    "source_read": "owned_source",
    "patch_propose": "owned_source",
    "patch_apply": "owned_source",
    "deploy": "owned_source",
}
_MAX_TOKEN_CHARS = 4096
_MAX_ATTESTATION_SECONDS = 300


def _deny():
    # Errors must never echo JWTs, signed claims or secure configuration.
    raise ValueError("Untrusted or invalid external attestation")


def _decode_b64url(fragment, *, max_decoded=3000):
    if (not isinstance(fragment, str) or len(fragment) > 4000
            or not _B64.fullmatch(fragment)):
        _deny()
    try:
        value = base64.b64decode(
            fragment + "=" * (-len(fragment) % 4), altchars=b"-_",
            validate=True,
        )
    except (ValueError, binascii.Error):
        _deny()
    if len(value) > max_decoded or base64.urlsafe_b64encode(value).rstrip(
            b"=").decode("ascii") != fragment:
        _deny()
    return value


def _strict_json(fragment):
    def unique(pairs):
        obj = {}
        for key, value in pairs:
            if key in obj:
                _deny()
            obj[key] = value
        return obj

    try:
        obj = json.loads(_decode_b64url(fragment).decode("utf-8"),
                         object_pairs_hook=unique)
    except (ValueError, UnicodeError, TypeError):
        _deny()
    if not isinstance(obj, dict):
        _deny()
    return obj


def _valid_id(value):
    return isinstance(value, str) and bool(_ID.fullmatch(value))


def verify_external_attestation(token, *, trusted_public_keys,
                                expected_issuer, expected_audience,
                                request_binding, observed_at_epoch,
                                revocation_checker):
    """Validate a signed external claim; ALWAYS prohibit execution.

    trusted_public_keys and the revocation checker are supplied by the
    *trusted backend*; never expose them as caller-supplied request fields.
    This code does not discover trust by accepting untrusted JWT 'jku',
    'jwk', 'x5u' or algorithms, and does not manufacture MCP rights.
    """
    if (not isinstance(token, str)
            or len(token) > _MAX_TOKEN_CHARS
            or token.count(".") != 2
            or type(observed_at_epoch) is not int
            or observed_at_epoch < 0
            or not _valid_id(expected_issuer)
            or not _valid_id(expected_audience)
            or not isinstance(trusted_public_keys, dict)
            or not callable(revocation_checker)
            or not isinstance(request_binding, dict)
            or set(request_binding) != _BINDING):
        _deny()

    parts = token.split(".")
    header, claims = _strict_json(parts[0]), _strict_json(parts[1])
    if (set(header) != _HEADER or header.get("typ") != _ATT_TYPE
            or header.get("alg") != "EdDSA"
            or not _valid_id(header.get("kid"))
            or set(claims) != _CLAIMS):
        _deny()

    kid = header["kid"]
    raw = trusted_public_keys.get(kid)
    if not isinstance(raw, bytes) or len(raw) != 32:
        _deny()
    signature = _decode_b64url(parts[2], max_decoded=128)
    if len(signature) != 64:
        _deny()
    try:
        Ed25519PublicKey.from_public_bytes(raw).verify(
            signature, (parts[0] + "." + parts[1]).encode("ascii")
        )
    except (InvalidSignature, ValueError, TypeError):
        _deny()

    for field in ("iss", "aud", "sub", "project_id", "asset_hostname",
                  "scope", "action", "mandate_id", "jti"):
        if not _valid_id(claims[field]):
            _deny()
    if (claims["iss"] != expected_issuer
            or claims["aud"] != expected_audience
            or claims["scope"] not in ("public_metadata", "owned_source")
            or claims["action"] not in _ACTIONS
            or _ACTIONS[claims["action"]] != claims["scope"]):
        _deny()
    for key, claim_field in (
        ("subject", "sub"), ("project_id", "project_id"),
        ("asset_hostname", "asset_hostname"), ("scope", "scope"),
        ("action", "action")
    ):
        if (not _valid_id(request_binding[key])
                or request_binding[key] != claims[claim_field]):
            _deny()

    iat, nbf, exp = (claims["iat"], claims["nbf"], claims["exp"])
    if (any(type(x) is not int for x in (iat, nbf, exp))
            or not (0 <= iat <= nbf <= observed_at_epoch < exp)
            or exp - iat > _MAX_ATTESTATION_SECONDS):
        _deny()

    try:
        revoked = revocation_checker(claims["jti"])
    except Exception:
        _deny()
    if type(revoked) is not bool or revoked:
        _deny()

    return {
        "schema_version": "0.2",
        "verification_type": "EXTERNAL_ED25519_ATTESTATION_NOT_ADMISSION",
        "decision": "VERIFIED_ATTESTATION_NOT_EXECUTION_ADMISSION",
        "signature_verified": True,
        "claims_bound_to_request": True,
        "revocation_checked": True,
        "authorized": False,
        "execution_enabled": False,
        "mcp_claim_verified": False,
        "user_session_authenticated": False,
        "project_acl_verified": False,
        "ready_for_production": False,
        "limitations": (
            "Cryptographic claim verification only. The verifier cannot "
            "grant P1/P2 authority, prove a user session, verify MCP runtime "
            "claims, authorize a scanner or patch, or deploy anything. "
            "External issuer onboarding, key rotation and live revocation "
            "must be governed before production integration."
        ),
    }
