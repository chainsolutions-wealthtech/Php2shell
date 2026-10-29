"""Deterministic, network-free provenance audit for the curated PHP advisory snapshot.

This reports the age and fingerprint of *local reviewed data*, never the
freshness of an upstream feed or the vulnerability of a deployed asset.
"""
from datetime import date
from hashlib import sha256
import json
import re

from .security_advisories import load_advisory_catalog


def audit_catalog_snapshot(as_of_utc, path=None):
    """Audit local catalog at an explicit UTC calendar date, without network I/O.

    An explicit date avoids silently presenting an offline catalog as a live
    feed. The digest fingerprints canonical parsed JSON, not its file layout.
    """
    if not isinstance(as_of_utc, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", as_of_utc):
        raise ValueError("as_of_utc must be an ISO calendar date YYYY-MM-DD")
    try:
        observed = date.fromisoformat(as_of_utc)
    except ValueError as exc:
        raise ValueError("Invalid as_of_utc calendar date") from exc

    catalog = load_advisory_catalog(path)
    reviewed = date.fromisoformat(catalog["reviewed_on_utc"])
    if reviewed > observed:
        raise ValueError("Catalog review date is in the future relative to as_of_utc")
    serialized = json.dumps(
        catalog, sort_keys=True, ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8")
    return {
        "schema_version": "0.2",
        "audit_type": "OFFLINE_CATALOG_PROVENANCE_NOT_LIVE_VALIDATION",
        "as_of_utc": as_of_utc,
        "catalog_reviewed_on_utc": catalog["reviewed_on_utc"],
        "snapshot_age_days": (observed - reviewed).days,
        "canonical_json_sha256": sha256(serialized).hexdigest(),
        "advisory_count": len(catalog["advisories"]),
        "source_freshness": catalog["source_freshness"],
        "independent_upstream_reverification_required": True,
        "asset_applicability": "insufficient_evidence",
        "limitations": (
            "Local snapshot fingerprint and review age only; no live feed, "
            "runtime attestation, vendor backport verification, remote scan "
            "or CVE applicability determination."
        ),
    }
