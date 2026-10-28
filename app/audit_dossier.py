"""Safe PHP2SHELL offline audit dossier; read-only, never a vulnerability verdict."""
from collections import Counter
from datetime import date
from hashlib import sha256
import json
from pathlib import PurePosixPath
import re

from .static_analysis import scan_project
from .runtime_evidence import review_declared_runtime_evidence

_ACTIONS = {
    "PHP-DYNAMIC-EVAL": "Review user-input flow; replace dynamic evaluation with an allowlisted dispatcher and unit tests.",
    "PHP-UNSERIALIZE": "Review trust boundaries, prefer strict data formats and test compatibility.",
    "PHP-SHELL-EXEC": "Review command arguments and privileges, avoid shell execution and test authorization.",
    "PHP-CONFIG-EXPOSE-PHP": "Verify the active SAPI's PHP exposure and minimize unnecessary disclosures.",
    "PHP-CONFIG-DISPLAY-ERRORS": "Verify production error display and private logging policy.",
    "PHP-CONFIG-URL-INCLUDE": "Verify remote include policy in effective PHP and FPM settings.",
    "PHP-CONFIG-COOKIE-HTTPONLY": "Review session cookie HTTP-only policy and compatibility.",
    "PHP-CONFIG-COOKIE-SECURE": "Review session cookie Secure policy with HTTPS proxy termination.",
    "PHP-CONFIG-SESSION-STRICT": "Verify active PHP session strict mode with compatibility tests.",
}
_MAX_OBSERVATIONS = 2000
_SEVERITIES = {"low", "medium", "high", "critical"}
_GATES = [
    "Confirm authorization and project ownership using governed mandating.",
    "Review and reproduce local indicators in an isolated authorized lab.",
    "Attest the effective PHP HTTP SAPI and installed vendor package/backports.",
    "Reconcile official advisories against authenticated runtime evidence.",
    "Create PHPPATCH proposals and run isolated non-regression tests.",
    "Obtain independent approval, backup and rollback before production change.",
]


def _calendar_day(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError("as_of_utc must be YYYY-MM-DD")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("Invalid as_of_utc date") from exc


def _path(value):
    if (not isinstance(value, str) or not 0 < len(value) <= 320
            or any(ord(c) < 32 or ord(c) == 127 for c in value)
            or "\\" in value or value.startswith("/")
            or ".." in PurePosixPath(value).parts):
        raise ValueError("Unsafe local evidence path")
    return value


def _indicator(item, category):
    if not isinstance(item, dict):
        raise ValueError("Invalid local indicator")
    path, rule, severity, line = (
        item.get("path"), item.get("rule"), item.get("severity"), item.get("line"),
    )
    if (rule not in _ACTIONS or severity not in _SEVERITIES
            or type(line) is not int or not 0 < line <= 10_000_000):
        raise ValueError("Unknown or malformed local indicator")
    if category == "php_lexical" and not rule.startswith("PHP-") :
        raise ValueError("Unexpected PHP rule")
    path = _path(path)
    key = json.dumps([category, path, line, rule], ensure_ascii=False)
    return {
        "evidence_id": "P2S-EV-" + sha256(key.encode("utf-8")).hexdigest()[:16],
        "category": category,
        "rule": rule,
        "severity_hint": severity,
        "source_relative_path": path,
        "source_line": line,
        "confidence": "review_required",
        "asset_vulnerability_confirmed": False,
        "remediation_proposal": _ACTIONS[rule],
        "patch_status": "NOT_GENERATED",
        "review_gate": "HUMAN_SECURITY_REVIEW",
    }


def build_audit_dossier(project_path, as_of_utc, runtime_file=None):
    """Return a bounded dossier without raw source, config values or absolute root."""
    _calendar_day(as_of_utc)
    scan = scan_project(project_path)
    observations = (
        [_indicator(item, "php_lexical") for item in scan["findings"]]
        + [_indicator(item, "php_config")
           for item in scan["php_configuration"]["config_indicators"]]
    )
    if len(observations) > _MAX_OBSERVATIONS:
        raise ValueError("Too many observations; partition the authorized project")
    observations.sort(key=lambda x: (
        x["source_relative_path"], x["source_line"], x["rule"]
    ))
    if len({x["evidence_id"] for x in observations}) != len(observations):
        raise ValueError("Duplicate evidence IDs need human reconciliation")

    declared_runtime = None
    if runtime_file is not None:
        proof = review_declared_runtime_evidence(runtime_file, as_of_utc)
        declared_runtime = {
            "asset_hostname": proof["asset_hostname"],
            "php_version_declared": proof["php_version"],
            "sapi_declared": proof["sapi"],
            "snapshot_age_days": proof["snapshot_age_days"],
            "snapshot_stale": proof["snapshot_stale"],
            "mandate_authorization_verified": False,
            "signature_verified": False,
            "effective_http_runtime_attested": False,
            "vendor_backport_status": "not_verified",
            "asset_applicability": "insufficient_evidence",
            "comparisons": [
                {
                    "cve": item["cve"],
                    "status": item["status"],
                    "reference_fix": item["reference_fix"],
                    "asset_applicability": "insufficient_evidence",
                    "remediation_proposal": "Verify the HTTP SAPI, installed vendor package and backports before any runtime update.",
                    "patch_status": "NOT_GENERATED",
                }
                for item in proof["upstream_version_comparisons"]
            ],
        }
    skip = scan["skipped"] + scan["php_configuration"]["config_skipped"]
    reasons = dict(sorted(Counter(item["reason"] for item in skip).items()))
    summary = {
        "php_files_scanned": scan["scanned_php_files"],
        "observations_for_review": len(observations),
        "lexical_indicators": sum(o["category"] == "php_lexical" for o in observations),
        "configuration_indicators": sum(o["category"] == "php_config" for o in observations),
        "composer_lock_present": scan["composer_lock_present"],
        "composer_locked_package_count": len(scan["locked_dependencies"]),
        "skipped_file_counts_by_reason": reasons,
    }
    canonical = json.dumps([as_of_utc, summary, observations, declared_runtime],
                           sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return {
        "schema_version": "0.2",
        "document_type": "PHP2SHELL_LOCAL_AUDIT_DOSSIER_DRAFT",
        "as_of_utc": as_of_utc,
        "report_fingerprint_sha256": sha256(canonical.encode("utf-8")).hexdigest(),
        "report_fingerprint_is_signature": False,
        "authorization_status": "NOT_VERIFIED_BY_THIS_REPORT",
        "analysis_mode": "OFFLINE_LOCAL_SOURCE_AND_OPTIONAL_DECLARED_RUNTIME",
        "vulnerability_verdict": "INSUFFICIENT_EVIDENCE",
        "production_safe_to_patch": False,
        "summary": summary,
        "observations": observations,
        "declared_runtime": declared_runtime,
        "next_gates": list(_GATES),
        "limitations": (
            "Local lexical/config indicators and optional unverified runtime "
            "declaration only. No AST/data-flow analysis, authenticated source "
            "or HTTP runtime attestation, verified backports, PHP exploitability "
            "test, remote crawl or patch. No observed signal is not proof of safety."
        ),
    }


def _markdown(text):
    # Source paths cannot introduce headings, clickable links or code blocks.
    value = str(text).replace("\r", " ").replace("\n", " ")
    value = value.replace(chr(96), chr(92) + chr(96))
    return re.sub(r"([\\*_{}\[\]()#+.!|<>])", r"\\\1", value)


def render_audit_dossier_markdown(report):
    """Render only a report draft; fail closed on elevated status/patch claims."""
    if (not isinstance(report, dict)
            or report.get("document_type") != "PHP2SHELL_LOCAL_AUDIT_DOSSIER_DRAFT"
            or report.get("vulnerability_verdict") != "INSUFFICIENT_EVIDENCE"
            or report.get("production_safe_to_patch") is not False):
        raise ValueError("Untrusted or elevated dossier")
    observations = report.get("observations")
    if not isinstance(observations, list) or len(observations) > _MAX_OBSERVATIONS:
        raise ValueError("Invalid dossier observations")
    result = [
        "# PHP2SHELL — Dossier d'audit local (brouillon)",
        "",
        "**Statut : indices à examiner, aucune vulnérabilité d'actif confirmée.**",
        "",
        "Date de revue : " + _markdown(report["as_of_utc"]),
        "Fichiers PHP examinés : " + _markdown(report["summary"]["php_files_scanned"]),
        "Constats : " + _markdown(len(observations)),
        "",
        "## Constats techniques", "",
    ]
    if not observations:
        result += ["Aucun indicateur identifié ; cela ne prouve pas l'absence de vulnérabilité.", ""]
    for row in observations:
        if (not isinstance(row, dict)
                or row.get("asset_vulnerability_confirmed") is not False
                or row.get("patch_status") != "NOT_GENERATED"
                or row.get("rule") not in _ACTIONS):
            raise ValueError("Elevated or malformed observation")
        result += [
            "### " + _markdown(row["evidence_id"]) + " — " + _markdown(row["rule"]),
            "",
            "Emplacement : " + _markdown(row["source_relative_path"]) + " ; ligne " +
            _markdown(row["source_line"]),
            "Révision proposée : " + _markdown(row["remediation_proposal"]), "",
        ]
    runtime = report.get("declared_runtime")
    if runtime is not None:
        if (not isinstance(runtime, dict)
                or runtime.get("asset_applicability") != "insufficient_evidence"
                or runtime.get("signature_verified") is not False
                or runtime.get("effective_http_runtime_attested") is not False):
            raise ValueError("Untrusted runtime attestation")
        result += [
            "## Version PHP déclarée, non attestée", "",
            "Hôte déclaré : " + _markdown(runtime["asset_hostname"]),
            "Version déclarée : " + _markdown(runtime["php_version_declared"]),
            "SAPI déclarée : " + _markdown(runtime["sapi_declared"]), "",
        ]
        for item in runtime["comparisons"]:
            if item.get("asset_applicability") != "insufficient_evidence":
                raise ValueError("Unexpected CVE applicability")
            result.append(
                "- " + _markdown(item["cve"]) + " : " + _markdown(item["status"]) +
                ", seuil upstream " + _markdown(item["reference_fix"]) +
                " ; applicabilité non déterminée."
            )
        result.append("")
    result += [
        "## Conditions préalables à PHPPATCH", "",
        *("- " + _markdown(item) for item in report["next_gates"]),
        "", "## Limites", "", _markdown(report["limitations"]), "",
    ]
    return "\n".join(result)
