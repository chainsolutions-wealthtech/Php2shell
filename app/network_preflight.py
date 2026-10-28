"""Offline DNS/IP and redirect policy preflight for future authorized crawling.

Not a resolver, connector, redirect follower, or SSRF-safe HTTP client.
A peer address MUST be re-resolved/validated and pinned by a later
mandated network worker at connect time (including every redirect).
"""
import ipaddress
from datetime import datetime
import re

from .core import Scope, Target
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
    if not isinstance(hostname, str):
        raise ValueError("Invalid DNS hostname")
    host = Target(hostname, Scope.PUBLIC).hostname
    if "." not in host:
        raise ValueError("DNS hostname requires a suffix")
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
        if not ip.is_global or (
                isinstance(ip, ipaddress.IPv6Address)
                and ip.ipv4_mapped is not None):
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


def check_same_origin_redirects(start_url, destinations, max_hops=5):
    """Dry-run a supplied redirect chain; never fetch or follow URLs."""
    if type(max_hops) is not int or not 0 <= max_hops <= 10:
        raise ValueError("Invalid redirect hop limit")
    first = preview_url_scope(start_url)
    if not isinstance(destinations, list) or len(destinations) > max_hops:
        raise ValueError("Redirect chain exceeds configured limit")
    validated = []
    for location in destinations:
        next_page = preview_url_scope(location)
        if next_page["hostname"] != first["hostname"]:
            raise ValueError("Cross-origin redirect not admitted")
        validated.append(next_page["normalized_url"])
    return {
        "schema_version": "0.2",
        "evaluation_type": "OFFLINE_REDIRECT_CHAIN_PREVIEW_NOT_HTTP_FOLLOW",
        "start_url": first["normalized_url"],
        "redirects_previewed": len(validated),
        "candidate_urls": validated,
        "same_origin_by_syntax": True,
        "each_peer_resolved_and_verified": False,
        "http_redirects_followed": False,
        "network_requests_made": False,
        "authorized_to_crawl": False,
        "limitations": (
            "Supplied URLs only; TLS, DNS, redirects, timing, consent, robots, "
            "source ownership and real HTTP responses have not been checked."
        ),
    }
