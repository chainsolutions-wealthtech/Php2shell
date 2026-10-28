"""Normalize caller-supplied HTTP metadata for an *unverified* guest preview.

This is a pure local transformation, NOT an HTTP collector or evidence
authenticator. Never persist or echo header values, URLs, credentials or cookies.
The output matches app.public_summary's deliberately untrusted input contract.
"""
import re

_ALLOWED_PUBLIC_HEADER_NAMES = frozenset({
    "content-type", "strict-transport-security", "content-security-policy",
    "x-content-type-options", "referrer-policy", "permissions-policy",
})
_HTTP_TOKEN = re.compile(r"^[!#$%&'*+.^_`|~0-9A-Za-z-]+$", re.ASCII)
_MAX_HEADERS = 64
_MAX_NAME = 128
_MAX_VALUE_BYTES = 2048
_MAX_TOTAL_BYTES = 16384


def normalize_untrusted_http_metadata(http_status, header_pairs):
    """Return only allowed header *names* and a declared status, never values.

    The caller is responsible for lawful acquisition and trustworthy origin.
    Even a well-formed result MUST NOT be labelled collected, verified or safe.
    Invalid values fail closed without reflecting input into exception text.
    """
    if type(http_status) is not int or not 100 <= http_status <= 599:
        raise ValueError("Invalid declared HTTP metadata")
    if not isinstance(header_pairs, (list, tuple)) or len(header_pairs) > _MAX_HEADERS:
        raise ValueError("Invalid declared HTTP metadata")

    present = set()
    total = 0
    for pair in header_pairs:
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            raise ValueError("Invalid declared HTTP metadata")
        name, value = pair
        if not isinstance(name, str) or not isinstance(value, str):
            raise ValueError("Invalid declared HTTP metadata")
        if not 1 <= len(name) <= _MAX_NAME or not _HTTP_TOKEN.fullmatch(name):
            raise ValueError("Invalid declared HTTP metadata")
        if any(ord(ch) < 32 or ord(ch) == 127 for ch in value):
            raise ValueError("Invalid declared HTTP metadata")
        try:
            encoded = value.encode("utf-8")
        except UnicodeEncodeError as exc:
            raise ValueError("Invalid declared HTTP metadata") from exc
        if len(encoded) > _MAX_VALUE_BYTES:
            raise ValueError("Invalid declared HTTP metadata")
        total += len(name.encode("ascii")) + len(encoded)
        if total > _MAX_TOTAL_BYTES:
            raise ValueError("Invalid declared HTTP metadata")
        normalized = name.lower()
        if normalized in _ALLOWED_PUBLIC_HEADER_NAMES:
            present.add(normalized)

    return {
        "schema_version": "0.2",
        "evidence_type": "UNVERIFIED_SUPPLIED_PUBLIC_RESPONSE",
        "http_status": http_status,
        "response_headers_present": sorted(present),
    }
