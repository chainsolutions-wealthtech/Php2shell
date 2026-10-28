"""Offline DNS/IP and redirect policy preflight for future authorized crawling.

Not a resolver, connector, redirect follower, or SSRF-safe HTTP client.
A peer address MUST be re-resolved/validated and pinned by a later
mandated network worker at connect time (including every redirect).
"""
import ipaddress
from datetime import datetime
import re

from .url_intake import preview_url_scope

_MAX_ANSWERS = 32
_TIME = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")


def _timestamp(value):
    if not isinstance(value, str) or not _TIME.fullmatch(value):
        raise ValueError("Invalid DNS observation UTC timestamp")
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("Invalid DNS observation UTC timestamp") from exc


def check_public_address_answers(hostname, answers, observed_at_utc,
                                 ttl_seconds=60):
    """Classify *supplied* A/AAAA records with an all-public policy.

    The caller's records are untrusted, and this does not confirm the actual
    resolved DNS chain, TLS peer or intended server. If one address is not
    globally routable the snapshot is rejected as a whole.
    """
    _timestamp(observed_at_utc)
    if (not isinstance(hostname, str)
            or not re.fullmatch(r"[A-Za-z0-9.-]{1,253}", hostname)):
        raise ValueError("Invalid DNS hostname")
    # A supplied DNS snapshot must not smuggle an IP literal, local suffix,
    # URL path, credentials or an ambiguous numeric host into the preview.
    # This is syntax validation only, never DNS or ownership attestation.
    host = preview_url_scope("https://" + hostname)["hostname"]
    if type(ttl_seconds) is not int or not 1 <= ttl_seconds <= 300:
        raise ValueError("Invalid TTL policy bound")
    if not isinstance(answers, list) or not 1 <= len(answers) <= _MAX_ANSWERS:
        raise ValueError("Expected 1..32 supplied A/AAAA answers")
    accepted, blocked = [], []
    seen = set()
    for value in answers:
        if (not isinstance(value, str) or not value or len(value) > 45
                or value != value.strip() or "%" in value):
            raise ValueError("Malformed or scoped IP address")
        try:
            ip = ipaddress.ip_address(value)
        except ValueError as exc:
            raise ValueError("DNS A/AAAA answer is not an IP literal") from exc
        if ip.compressed != value.lower() and isinstance(ip, ipaddress.IPv4Address):
            # Canonical IPv4 only; reject ambiguous forms and whitespace.
            raise ValueError("Noncanonical IPv4 address")
        rendered = ip.compressed
        if rendered in seen:
            raise ValueError("Duplicate DNS address")
        seen.add(rendered)
        transition_ipv6 = (
            isinstance(ip, ipaddress.IPv6Address)
            and (ip.ipv4_mapped is not None
                 or ip.sixtofour is not None
                 or ip.teredo is not None)
        )
        if not ip.is_global or transition_ipv6:
            blocked.append(rendered)
        else:
            accepted.append(rendered)
    return {
        "schema_version": "0.2",
        "evaluation_type": "OFFLINE_DNS_ANSWER_PREFLIGHT_NOT_PEER_VALIDATION",
        "hostname": host,
        "observed_at_utc": observed_at_utc,
        "ttl_seconds_declared": ttl_seconds,
        "all_supplied_addresses_globally_routable": not blocked,
        "public_ip_count": len(accepted),
        "blocked_ip_count": len(blocked),
        "candidate_public_addresses": accepted if not blocked else [],
        "network_requests_made": False,
        "dns_answers_authenticated": False,
        "cname_chain_verified": False,
        "address_pinned_to_connection": False,
        "peer_connection_authorized": False,
        "blockers": (
            ["NON_GLOBAL_OR_MAPPED_IP_IN_DNS_SNAPSHOT"] if blocked else []
        ),
        "limitations": (
            "Untrusted supplied DNS answers only. Re-resolve CNAME/A/AAAA at "
            "the actual connection, verify ALL answers, pin the selected "
            "socket peer, validate TLS and repeat on every redirect. "
            "A clean sample cannot grant network admission."
        ),
    }


def _inside_base_path(path, base_path):
    """Compare complete path segments, never string prefixes alone."""
    return (base_path == "/" or path == base_path
            or path.startswith(base_path.rstrip("/") + "/"))


def check_same_origin_redirects(start_url, destinations, max_hops=5,
                                allowed_base_path=None):
    """Dry-run supplied redirects, optionally constrained to a path scope.

    A path scope is an additional local restriction, not a crawler mandate.
    Existing same-origin-only callers remain compatible when it is omitted.
    """
    if type(max_hops) is not int or not 0 <= max_hops <= 10:
        raise ValueError("Invalid redirect hop limit")
    first = preview_url_scope(start_url)
    if allowed_base_path is not None:
        if not isinstance(allowed_base_path, str):
            raise ValueError("Invalid declared base path")
        # The URL parser enforces path canonicalization and rejects encoded
        # traversal, queries, fragments, repeated slashes and unsafe bytes.
        scoped = preview_url_scope(
            "https://" + first["hostname"] + allowed_base_path
        )
        if scoped["base_path"] != allowed_base_path:
            raise ValueError("Invalid declared base path")
        if not _inside_base_path(first["base_path"], allowed_base_path):
            raise ValueError("Start URL outside declared base path")
    if not isinstance(destinations, list) or len(destinations) > max_hops:
        raise ValueError("Redirect chain exceeds configured limit")
    validated = []
    for location in destinations:
        next_page = preview_url_scope(location)
        if next_page["hostname"] != first["hostname"]:
            raise ValueError("Cross-origin redirect not admitted")
        if (allowed_base_path is not None
                and not _inside_base_path(
                    next_page["base_path"], allowed_base_path)):
            raise ValueError("Redirect outside declared base path")
        validated.append(next_page["normalized_url"])
    return {
        "schema_version": "0.2",
        "evaluation_type": "OFFLINE_REDIRECT_CHAIN_PREVIEW_NOT_HTTP_FOLLOW",
        "start_url": first["normalized_url"],
        "redirects_previewed": len(validated),
        "candidate_urls": validated,
        "same_origin_by_syntax": True,
        "base_path_scope_enforced": allowed_base_path is not None,
        "allowed_base_path": allowed_base_path,
        "each_peer_resolved_and_verified": False,
        "http_redirects_followed": False,
        "network_requests_made": False,
        "authorized_to_crawl": False,
        "limitations": (
            "Supplied URLs only; TLS, DNS, redirects, timing, consent, robots, "
            "source ownership and real HTTP responses have not been checked. "
            "An optional path boundary is only an offline syntactic preview."
        ),
    }
