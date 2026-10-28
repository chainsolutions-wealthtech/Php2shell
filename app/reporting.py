"""Safe, offline CSV summary of source and configuration review indicators.

CSV is a portable *finding inventory*, not a complete vulnerability report.
Inputs are local scan_project() results. No file writes or network activity.
"""
import csv
import io

_COLUMNS = ("finding_type", "rule", "severity", "confidence",
            "path", "line", "note")


def _safe_cell(value):
    """Prevent common spreadsheet-formula injection, even after leading spaces."""
    if value is None:
        return ""
    if not isinstance(value, (str, int, float, bool)):
        raise ValueError("Unexpected report value")
    text = str(value).replace("\x00", "")
    # Spreadsheet viewers may ignore leading whitespace/control characters.
    # Do not interpret data as a formula; preserve the visible original value.
    if text.lstrip(" \t\r\n").startswith(("=", "+", "-", "@")):
        return "'" + text
    return text


def export_findings_csv(result):
    """Emit findings without executing code, disclosing config values or
    claiming CVEs are applicable to the scanned runtime.
    """
    if not isinstance(result, dict) or result.get("schema_version") != "0.2":
        raise ValueError("Expected a V0.2 local analysis result")
    php = result.get("findings", [])
    config = result.get("php_configuration", {}).get("config_indicators", [])
    if not isinstance(php, list) or not isinstance(config, list):
        raise ValueError("Malformed local analysis findings")
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(_COLUMNS)
    for category, rows in (("php_lexical", php), ("php_config", config)):
        for item in rows:
            if not isinstance(item, dict):
                raise ValueError("Malformed local analysis finding")
            writer.writerow([_safe_cell(value) for value in (
                category, item.get("rule"), item.get("severity"),
                item.get("confidence"), item.get("path"),
                item.get("line"), (
                    "Lexical indicator: contextual review required"
                    if category == "php_lexical" else
                    "Local configuration only: effective runtime unverified"
                ),
            )])
    return output.getvalue()
