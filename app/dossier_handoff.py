"""Fail-closed, offline PHP2SHELL dossier handoff preview for future PHPPATCH.

A dossier fingerprint is only a consistency check, NEVER an authenticated
signature. This module cannot approve an asset, generate a patch, or deploy.
Only fixed, non-sensitive fields are exported across the proposed boundary.
"""
from hashlib import sha256
import json
import re

from .audit_dossier import _indicator

_EVIDENCE_ID = re.compile(r"P2S-EV-[0-9a-f]{16}", re.ASCII)
_CVE = re.compile(r"CVE-\d{4}-\d{4,}", re.ASCII)
_MAX_ITEMS = 2000
_RUNTIME_KEYS = {
    "asset_hostname", "php_version_declared", "sapi_declared",
    "snapshot_age_days", "snapshot_stale", "mandate_authorization_verified",
    "signature_verified", "effective_http_runtime_attested",
    "vendor_backport_status", "asset_applicability", "comparisons",
}
_COMPARISON_KEYS = {
    "cve", "status", "reference_fix", "asset_applicability",
    "remediation_proposal", "patch_status",
}


def _verify_dossier(dossier):
    if not isinstance(dossier, dict):
        raise ValueError("Expected offline audit dossier")
    required = {
        "schema_version": "0.2",
        "document_type": "PHP2SHELL_LOCAL_AUDIT_DOSSIER_DRAFT",
        "report_fingerprint_is_signature": False,
        "authorization_status": "NOT_VERIFIED_BY_THIS_REPORT",
        "analysis_mode": "OFFLINE_LOCAL_SOURCE_AND_OPTIONAL_DECLARED_RUNTIME",
        "vulnerability_verdict": "INSUFFICIENT_EVIDENCE",
        "production_safe_to_patch": False,
    }
    for field, value in required.items():
        if type(dossier.get(field)) is not type(value) or dossier[field] != value:
            raise ValueError("Elevated or malformed dossier field: " + field)
    observations = dossier.get("observations")
    if not isinstance(observations, list) or len(observations) > _MAX_ITEMS:
        raise ValueError("Invalid dossier observations")
    summary = dossier.get("summary")
    if not isinstance(summary, dict):
        raise ValueError("Invalid dossier summary")
    for field in ("php_files_scanned", "observations_for_review",
                  "lexical_indicators", "configuration_indicators",
                  "composer_locked_package_count"):
        if type(summary.get(field)) is not int or summary[field] < 0:
            raise ValueError("Invalid summary count")
    if (summary["observations_for_review"] != len(observations)
            or summary["lexical_indicators"] != sum(
                item.get("category") == "php_lexical"
                for item in observations if isinstance(item, dict))
            or summary["configuration_indicators"] != sum(
                item.get("category") == "php_config"
                for item in observations if isinstance(item, dict))):
        raise ValueError("Inconsistent dossier counts")
    seen = set()
    for item in observations:
        if not isinstance(item, dict) or item.get("category") not in (
                "php_lexical", "php_config"):
            raise ValueError("Invalid dossier indicator category")
        expected = _indicator({
            "path": item.get("source_relative_path"),
            "rule": item.get("rule"),
            "severity": item.get("severity_hint"),
            "line": item.get("source_line"),
        }, item["category"])
        if item != expected or not _EVIDENCE_ID.fullmatch(item["evidence_id"]):
            raise ValueError("Forged or elevated dossier indicator")
        if item["evidence_id"] in seen:
            raise ValueError("Duplicate dossier evidence ID")
        seen.add(item["evidence_id"])
    if observations != sorted(observations, key=lambda item: (
            item["source_relative_path"], item["source_line"], item["rule"])):
        raise ValueError("Noncanonical observation order")
    runtime = dossier.get("declared_runtime")
    if runtime is not None:
        if not isinstance(runtime, dict) or set(runtime) != _RUNTIME_KEYS:
            raise ValueError("Malformed declared runtime")
        if (runtime["mandate_authorization_verified"] is not False
                or runtime["signature_verified"] is not False
                or runtime["effective_http_runtime_attested"] is not False
                or runtime["vendor_backport_status"] != "not_verified"
                or runtime["asset_applicability"] != "insufficient_evidence"):
            raise ValueError("Elevated runtime declaration")
        comparisons = runtime.get("comparisons")
        if not isinstance(comparisons, list) or len(comparisons) > 128:
            raise ValueError("Invalid runtime comparisons")
        for row in comparisons:
            if (not isinstance(row, dict) or set(row) != _COMPARISON_KEYS
                    or not isinstance(row["cve"], str)
                    or not _CVE.fullmatch(row["cve"])
                    or row["asset_applicability"] != "insufficient_evidence"
                    or row["patch_status"] != "NOT_GENERATED"):
                raise ValueError("Elevated CVE comparison")
    as_of = dossier.get("as_of_utc")
    if not isinstance(as_of, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", as_of):
        raise ValueError("Invalid dossier date")
    canonical = json.dumps(
        [as_of, summary, observations, runtime], sort_keys=True,
        ensure_ascii=False, separators=(",", ":"),
    )
    digest = sha256(canonical.encode("utf-8")).hexdigest()
    if (not isinstance(dossier.get("report_fingerprint_sha256"), str)
            or dossier["report_fingerprint_sha256"] != digest):
        raise ValueError("Dossier fingerprint mismatch")
    return observations


def prepare_phppatch_handoff(dossier):
    """Create an untrusted review queue draft; no patch or permission grant."""
    observations = _verify_dossier(dossier)
    return {
        "schema_version": "0.2",
        "handoff_type": "PHPPATCH_OFFLINE_REVIEW_QUEUE_DRAFT",
        "source_dossier_fingerprint_sha256": dossier["report_fingerprint_sha256"],
        "source_fingerprint_is_authenticated_signature": False,
        "mandate_verified": False,
        "asset_vulnerability_confirmed": False,
        "ready_for_patch_generation": False,
        "ready_for_production": False,
        "approval_status": "NOT_REQUESTED",
        "patches_generated": 0,
        "review_items": [
            {
                "evidence_id": item["evidence_id"],
                "indicator_rule": item["rule"],
                "review_gate": "HUMAN_SECURITY_REVIEW",
                "patch_status": "NOT_GENERATED",
            }
            for item in observations
        ],
        "next_gates": [
            "Authenticate the project owner and P2 mandate in existing governance.",
            "Verify original source, evidence and effective PHP/SAPI/backports.",
            "Produce candidate diffs only in an isolated authorized workspace.",
            "Run regression tests, obtain independent approval and prove rollback.",
        ],
        "limitations": (
            "Offline review-only queue. No verified authorization, source "
            "attestation, confirmed CVE applicability, patch, Docker execution "
            "or deployment. An empty queue is not a security clearance."
        ),
    }
