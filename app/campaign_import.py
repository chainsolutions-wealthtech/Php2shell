"""Read-only local campaign imports. No DNS, HTTP, or authorization escalation.

This interface accepts declarations, NOT proofs of ownership or scope consent.
Network-capable jobs must verify mandates separately before any connection.
"""
import csv
import io
import json
from pathlib import Path

from .core import Scope, Target, inventory

MAX_IMPORT_BYTES = 5_000_000
MAX_IMPORT_ROWS = 10_000
ALLOWED_FORMATS = {".json": "json", ".csv": "csv", ".txt": "txt"}


def _record_target(raw, index, fmt):
    if not isinstance(raw, dict):
        raise ValueError(f"{fmt} record {index}: expected an object")
    host = raw.get("hostname")
    scope = raw.get("scope")
    evidence = raw.get("evidence", "")
    if not isinstance(host, str) or not isinstance(scope, str):
        raise ValueError(f"{fmt} record {index}: hostname and scope must be strings")
    if not isinstance(evidence, str):
        raise ValueError(f"{fmt} record {index}: evidence must be a string")
    try:
        return Target(host, Scope(scope), evidence)
    except ValueError as exc:
        raise ValueError(f"{fmt} record {index}: {exc}") from exc


def _read_rows(path, fmt):
    raw = path.read_text(encoding="utf-8-sig")
    if fmt == "json":
        data = json.loads(raw)
        if not isinstance(data, list):
            raise ValueError("JSON input must be a list of targets")
        return data
    if fmt == "csv":
        reader = csv.DictReader(io.StringIO(raw))
        if reader.fieldnames is None or any(x not in reader.fieldnames for x in ("hostname", "scope")):
            raise ValueError("CSV must contain hostname and scope header columns")
        if len(set(reader.fieldnames)) != len(reader.fieldnames) or None in reader.fieldnames:
            raise ValueError("CSV contains duplicate or invalid header names")
        rows = []
        for record in reader:
            if None in record:
                raise ValueError("CSV row contains too many columns")
            if any(value is None for value in record.values()):
                raise ValueError("CSV row contains too few columns")
            rows.append(record)
            if len(rows) > MAX_IMPORT_ROWS:
                raise ValueError("Campaign exceeds maximum row count")
        return rows
    # TXT: one hostname per nonempty line, public_metadata ONLY. No P2 in TXT.
    return [{"hostname": line.strip(), "scope": Scope.PUBLIC.value}
            for line in raw.splitlines() if line.strip() and not line.lstrip().startswith("#")]


def import_targets(path):
    """Return an offline campaign preview; never connects to target domains.

    De-duplicate on canonical hostname while rejecting conflicting permissions
    or evidence. TXT is intentionally P1-only; P2 needs explicit JSON/CSV.
    """
    file = Path(path)
    if file.is_symlink() or not file.is_file():
        raise ValueError("Import input must be a regular non-symlink file")
    if file.stat().st_size > MAX_IMPORT_BYTES:
        raise ValueError("Import input exceeds maximum size")
    fmt = ALLOWED_FORMATS.get(file.suffix.lower())
    if fmt is None:
        raise ValueError("Supported campaign formats: JSON, CSV, TXT")
    records = _read_rows(file, fmt)
    if len(records) > MAX_IMPORT_ROWS:
        raise ValueError("Campaign exceeds maximum row count")
    unique = {}
    for index, raw in enumerate(records, 1):
        target = _record_target(raw, index, fmt)
        previous = unique.get(target.hostname)
        if previous is None:
            unique[target.hostname] = target
        elif previous.scope != target.scope or previous.evidence != target.evidence:
            raise ValueError(f"Conflicting scope or evidence for duplicate hostname at record {index}")
    return {
        "schema_version": "0.2",
        "mode": "offline_inventory_only",
        "source_format": fmt,
        "rows_received": len(records),
        "unique_targets": len(unique),
        "duplicates_removed": len(records) - len(unique),
        "targets": inventory(unique.values()),
        "limitations": ("Scopes and evidence are operator declarations, not validated mandates. "
                        "This import performs no DNS, HTTP, PHP audit or vulnerability verification."),
    }
