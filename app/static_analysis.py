"""Conservative offline PHP source inventory. No execution, network, or mutation."""
from dataclasses import asdict, dataclass
from pathlib import Path
import json
import re

MAX_FILE_BYTES = 2_000_000
MAX_FILES = 5000
EXCLUDED = {".git", "vendor", "node_modules", ".venv", "__pycache__"}
PHP_SUFFIXES = {".php", ".phtml", ".inc"}

@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    rule: str
    severity: str
    evidence: str
    confidence: str = "review_required"

_RULES = (
    ("PHP-DYNAMIC-EVAL", "high", re.compile(r"\beval\s*\(", re.I)),
    ("PHP-UNSERIALIZE", "medium", re.compile(r"\bunserialize\s*\(", re.I)),
    ("PHP-SHELL-EXEC", "high", re.compile(r"\b(?:shell_exec|system|passthru|exec)\s*\(", re.I)),
)

def scan_project(root):
    """Read only files below a trusted local directory; findings are review leads, not CVE proofs."""
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Project root must be a directory")
    findings = []
    scanned = 0
    skipped = []
    import os
    for current, directories, filenames in os.walk(root, followlinks=False):
        directories[:] = sorted(d for d in directories if d not in EXCLUDED and not (Path(current) / d).is_symlink())
        for filename in sorted(filenames):
            path = Path(current) / filename
            if path.is_symlink() or not path.is_file() or path.suffix.lower() not in PHP_SUFFIXES:
                continue
            scanned += 1
            if scanned > MAX_FILES:
                raise ValueError("Project exceeds file scan limit")
            rel = path.relative_to(root).as_posix()
            if path.stat().st_size > MAX_FILE_BYTES:
                skipped.append({"path": rel, "reason": "file_too_large"})
                continue
            try:
                source = path.read_text(encoding="utf-8")
            except (UnicodeError, OSError):
                skipped.append({"path": rel, "reason": "unreadable"})
                continue
            for number, line in enumerate(source.splitlines(), 1):
                for rule, severity, pattern in _RULES:
                    if pattern.search(line):
                        findings.append(Finding(rel, number, rule, severity, "Pattern matched; manual context review required"))
    composer = root / "composer.json"
    dependencies = {}
    if composer.is_file() and not composer.is_symlink() and composer.stat().st_size <= MAX_FILE_BYTES:
        try:
            manifest = json.loads(composer.read_text(encoding="utf-8"))
            if isinstance(manifest, dict):
                for section in ("require", "require-dev"):
                    value = manifest.get(section, {})
                    if isinstance(value, dict):
                        dependencies[section] = {str(k): str(v) for k, v in value.items()}
        except (ValueError, UnicodeError, OSError):
            skipped.append({"path": "composer.json", "reason": "invalid_manifest"})
    return {"root": str(root), "scanned_php_files": scanned,
            "findings": [asdict(item) for item in findings],
            "composer_requirements": dependencies, "skipped": skipped,
            "limitations": "Regex indicators only; not vulnerability confirmation; no data-flow or reachability analysis."}
