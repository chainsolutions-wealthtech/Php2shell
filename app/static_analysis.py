"""Conservative, offline PHP source inventory. Never executes inspected source."""
from dataclasses import asdict, dataclass
from pathlib import Path
import json
import os
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
_PHP_OPEN = re.compile(r"<\?(?:php\b|=)?", re.I)
_HEREDOC_OPEN = re.compile(r"<<<[ \t]*(?P<quote>['\"]?)(?P<label>[A-Za-z_][A-Za-z_0-9]*)(?P=quote)[ \t]*(?:\r?\n)")


def _executable_php(source):
    """Mask HTML, PHP comments and literal strings while preserving newlines.

    This is a conservative lexer, NOT an AST or data-flow analysis. PHP edge
    cases may still create false positives/negatives; manual review is required.
    """
    visible = ["\n" if char == "\n" else " " for char in source]
    n = len(source)
    i = 0
    in_php = False
    while i < n:
        if not in_php:
            start = source.find("<?", i)
            if start < 0:
                break
            if source[start:start + 5].lower() == "<?xml":
                i = start + 2
                continue
            opener = _PHP_OPEN.match(source, start)
            if opener is None:
                i = start + 2
                continue
            in_php = True
            i = opener.end()
            continue
        if source.startswith("?>", i):
            in_php = False
            i += 2
            continue
        if source.startswith("//", i) or source[i] == "#":
            end = i
            while end < n and source[end] != "\n" and not source.startswith("?>", end):
                end += 1
            i = end
            continue
        if source.startswith("/*", i):
            end = source.find("*/", i + 2)
            i = n if end < 0 else end + 2
            continue
        if source[i] in ("'", '"', "`"):
            quote = source[i]
            i += 1
            while i < n:
                if source[i] == "\\":
                    i += 2
                elif source[i] == quote:
                    i += 1
                    break
                else:
                    i += 1
            continue
        if source.startswith("<<<", i):
            match = _HEREDOC_OPEN.match(source, i)
            if match:
                end_marker = re.compile(r"(?m)^[ \t]*" + re.escape(match.group("label")) + r"(?=\s*(?:;|\r?$))")
                closing = end_marker.search(source, match.end())
                if closing is None:
                    break  # Unknown/unterminated literal: no findings in its body
                i = closing.start()
                lineend = source.find("\n", i)
                i = n if lineend < 0 else lineend + 1
                continue
        visible[i] = source[i]
        i += 1
    return "".join(visible)


def scan_project(root):
    """Read only local files under an operator-authorized project directory."""
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Project root must be a directory")
    findings = []
    scanned = 0
    skipped = []
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
            code = _executable_php(source)
            for number, line in enumerate(code.splitlines(), 1):
                for rule, severity, pattern in _RULES:
                    if pattern.search(line):
                        findings.append(Finding(rel, number, rule, severity,
                                                "Lexical indicator; manual context review required"))
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
    return {"schema_version": "0.2", "root": str(root), "scanned_php_files": scanned,
            "findings": [asdict(item) for item in findings],
            "composer_requirements": dependencies, "skipped": skipped,
            "limitations": "Lexical indicators only; not vulnerability confirmation; no PHP AST, data-flow, or reachability analysis."}
