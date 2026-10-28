"""Bounded offline CSV export for *declared*, unverified PHP runtime evidence.

Only a fixed allowlist of non-secret fields is emitted. No network, disk
writes, PHP execution, mandate validation or vulnerability confirmation.
"""
import csv
import io
import re

from .reporting import _safe_cell

_COLUMNS = (
    "asset_hostname", "declared_php_version", "declared_sapi",
    "snapshot_stale", "cve", "upstream_version_status",
    "reference_fix", "asset_applicability", "mandate_verified",
    "runtime_attested", "signature_verified", "vendor_backport_status",
    "interpretation",
)
_CVE = re.compile(r"CVE-\d{4}-\d{4,}", re.ASCII)


def export_runtime_review_csv(result):
    """Render an explicitly non-attested runtime review as a safe CSV table.

    Reject unexpected trust escalation rather than silently converting it to
    a purportedly verified report. Source declarations never authorize scans.
    """
    if not isinstance(result, dict) or result.get("schema_version") != "0.2":
        raise ValueError("Expected V0.2 runtime review")
    if result.get("review_type") != "DECLARED_RUNTIME_EVIDENCE_NOT_ATTESTATION":
        raise ValueError("Not a declared runtime review")
    if (result.get("mandate_authorization_verified") is not False
            or result.get("signature_verified") is not False
            or result.get("effective_http_runtime_attested") is not False
            or result.get("asset_applicability") != "insufficient_evidence"
            or result.get("vendor_backport_status") != "not_verified"):
        raise ValueError("Unexpected attestation or applicability claim")
    rows = result.get("upstream_version_comparisons")
    if not isinstance(rows, list) or not 1 <= len(rows) <= 128:
        raise ValueError("Invalid upstream comparisons")
    for key in ("asset_hostname", "php_version", "sapi"):
        value = result.get(key)
        if not isinstance(value, str) or not value or len(value) > 256:
            raise ValueError("Invalid runtime report field")
    if type(result.get("snapshot_stale")) is not bool:
        raise ValueError("Invalid snapshot staleness")
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(_COLUMNS)
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Invalid upstream comparison")
        cve = row.get("cve")
        if not isinstance(cve, str) or not _CVE.fullmatch(cve):
            raise ValueError("Invalid CVE identifier")
        if row.get("asset_applicability") != "insufficient_evidence":
            raise ValueError("Unexpected CVE applicability claim")
        status, reference = row.get("status"), row.get("reference_fix")
        if (not isinstance(status, str) or not isinstance(reference, str)
                or len(status) > 128 or len(reference) > 128):
            raise ValueError("Invalid upstream comparison fields")
        writer.writerow([_safe_cell(v) for v in (
            result["asset_hostname"], result["php_version"], result["sapi"],
            result["snapshot_stale"], cve, status, reference,
            "insufficient_evidence", False, False, False, "not_verified",
            "Declared offline snapshot only; runtime and CVE applicability unverified",
        )])
    return output.getvalue()
