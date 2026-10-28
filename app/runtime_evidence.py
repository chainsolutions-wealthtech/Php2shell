"""Offline review of *declared* PHP runtime evidence from authorized projects.

Does NOT execute PHP, connect to any host, validate the asserted mandate,
verify a signature or attest which runtime serves live HTTP requests.
"""
from datetime import date, datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re

from .core import parse_version, Scope, Target
from .security_advisories import review_declared_php_version

_MAX_EVIDENCE_BYTES = 16_384
_MAX_AGE_DAYS = 30
_SAPIS = {"apache2handler", "fpm-fcgi", "cgi-fcgi", "cli", "litespeed",
          "frankenphp", "phpdbg", "other", "unknown"}
_SOURCES = {"operator_supplied", "laboratory_fixture"}
_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,79}")


def _date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError("as_of_utc must be YYYY-MM-DD")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("Invalid as_of_utc") from exc


def _timestamp(value):
    if not isinstance(value, str) or not re.fullmatch(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", value
    ):
        raise ValueError("collected_at_utc must be an explicit UTC timestamp")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("Invalid collected_at_utc") from exc
    return dt.astimezone(timezone.utc)


def _file(path):
    p = Path(path)
    if p.is_symlink() or not p.is_file() or p.stat().st_size > _MAX_EVIDENCE_BYTES:
        raise ValueError("Runtime evidence must be a bounded regular local JSON file")
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (UnicodeError, OSError, ValueError) as exc:
        raise ValueError("Invalid runtime evidence JSON") from exc
    if not isinstance(data, dict):
        raise ValueError("Runtime evidence must be a JSON object")
    return data


def review_declared_runtime_evidence(path, as_of_utc):
    """Evaluate operator-supplied metadata without asserting a real P2 mandate.

    Scope/evidence strings are UNVERIFIED declarations; no caller can turn a
    local JSON flag into a trusted authorization, signature or patch approval.
    """
    observed = _date(as_of_utc)
    source = _file(path)
    expected = {
        "schema_version", "evidence_type", "asset_hostname", "mandate_reference",
        "source_channel", "collected_at_utc", "php_version", "sapi",
        "vendor_backport_status",
    }
    if set(source) != expected:
        raise ValueError("Runtime evidence has missing or unexpected fields")
    if source["schema_version"] != "0.2" or source["evidence_type"] != "DECLARED_PHP_RUNTIME":
        raise ValueError("Unexpected runtime evidence schema")
    name = source["asset_hostname"]
    if not isinstance(name, str):
        raise ValueError("Invalid asset hostname")
    # Validation does not attest ownership, scope or authority.
    hostname = Target(name, Scope.PUBLIC).hostname
    mandate = source["mandate_reference"]
    if not isinstance(mandate, str) or not _ID.fullmatch(mandate):
        raise ValueError("Invalid mandate reference")
    if source["source_channel"] not in _SOURCES:
        raise ValueError("Unknown evidence channel")
    if source["vendor_backport_status"] != "not_verified":
        raise ValueError("Backports must remain unverified until trusted provenance is available")
    sapi = source["sapi"]
    if not isinstance(sapi, str) or sapi not in _SAPIS:
        raise ValueError("Unrecognized PHP SAPI")
    php_version = source["php_version"]
    if not isinstance(php_version, str):
        raise ValueError("Invalid PHP version")
    parse_version(php_version)
    collected = _timestamp(source["collected_at_utc"])
    if collected.date() > observed:
        raise ValueError("Runtime evidence cannot have a future timestamp")
    age = (observed - collected.date()).days
    # A SHA-256 is a content fingerprint only, never an authenticity proof.
    canonical = json.dumps(
        source, sort_keys=True, ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8")
    review = review_declared_php_version(php_version)
    return {
        "schema_version": "0.2",
        "review_type": "DECLARED_RUNTIME_EVIDENCE_NOT_ATTESTATION",
        "asset_hostname": hostname,
        "mandate_reference": mandate,
        "mandate_authorization_verified": False,
        "source_channel": source["source_channel"],
        "collected_at_utc": source["collected_at_utc"],
        "as_of_utc": as_of_utc,
        "snapshot_age_days": age,
        "snapshot_stale": age > _MAX_AGE_DAYS,
        "php_version": php_version,
        "sapi": sapi,
        "vendor_backport_status": "not_verified",
        "declaration_sha256": sha256(canonical).hexdigest(),
        "signature_verified": False,
        "effective_http_runtime_attested": False,
        "asset_applicability": "insufficient_evidence",
        "upstream_version_comparisons": [
            {
                "cve": item["cve"],
                "status": item["status"],
                "reference_fix": item["reference_fix"],
                "asset_applicability": "insufficient_evidence",
            }
            for item in review["results"]
        ],
        "limitations": (
            "Local operator declaration only; mandate, asset ownership, "
            "capture provenance, PHP HTTP SAPI and vendor backports are "
            "not independently authenticated. Source values and a hash "
            "cannot confirm a deployed CVE or authorize a patch."
        ),
    }
