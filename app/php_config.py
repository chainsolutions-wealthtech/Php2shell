"""Read-only, secret-minimizing PHP configuration indicators.

This parses only explicitly named local PHP ini / PHP-FPM config files.
It never executes PHP, reads outside the project root, or makes requests.
Results are indicators from files, NOT effective runtime settings.
"""
from pathlib import Path
import os
import re

MAX_CONFIG_FILES = 100
MAX_CONFIG_BYTES = 1_000_000
EXCLUDED = {".git", "vendor", "node_modules", ".venv", "__pycache__"}
PHP_INI_NAMES = {"php.ini", ".user.ini", "php-fpm.conf"}
FPM_POOL_DIRECTORIES = {"php-fpm.d", "pool.d"}

# A conservative, intentionally small ruleset. Unknown values are ignored.
DIRECTIVES = {
    "expose_php": ("PHP-CONFIG-EXPOSE-PHP", "low", "enabled"),
    "display_errors": ("PHP-CONFIG-DISPLAY-ERRORS", "medium", "enabled"),
    "allow_url_include": ("PHP-CONFIG-URL-INCLUDE", "high", "enabled"),
    "session.cookie_httponly": ("PHP-CONFIG-COOKIE-HTTPONLY", "medium", "disabled"),
    "session.cookie_secure": ("PHP-CONFIG-COOKIE-SECURE", "medium", "disabled"),
    "session.use_strict_mode": ("PHP-CONFIG-SESSION-STRICT", "low", "disabled"),
}
_DIRECTIVE_PATTERN = re.compile(
    r"^\s*(?:php_(?:admin_)?value\s*\[\s*)?"
    r"(?P<key>[a-z][a-z0-9_.]*)\s*\]?\s*=\s*(?P<value>.*)$", re.I
)
_TRUTHY = frozenset({"on", "1", "yes", "true"})
_FALSY = frozenset({"off", "0", "no", "false"})


def _is_candidate(path):
    name = path.name.lower()
    return name in PHP_INI_NAMES or (
        name.endswith(".conf") and path.parent.name.lower() in FPM_POOL_DIRECTORIES
    )


def _boolean_value(value):
    # Do not try to interpret dynamic/quoted expressions or interpolate config
    # variables. Only unambiguous ini booleans are recognized.
    raw = value.strip().split(";", 1)[0].split("#", 1)[0].strip().lower()
    if raw in _TRUTHY:
        return True
    if raw in _FALSY:
        return False
    return None


def inspect_php_configs(root):
    """Summarize visible local config files without returning raw values.

    A local configuration indicator is NOT evidence of the active SAPI,
    precedence order, runtime effective value, or a confirmed vulnerability.
    """
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Project root must be a directory")
    indicators, skipped = [], []
    scanned = 0
    for current, directories, filenames in os.walk(root, followlinks=False):
        directories[:] = sorted(
            d for d in directories
            if d not in EXCLUDED and not (Path(current) / d).is_symlink()
        )
        for name in sorted(filenames):
            path = Path(current) / name
            if not _is_candidate(path):
                continue
            rel = path.relative_to(root).as_posix()
            if path.is_symlink() or not path.is_file():
                skipped.append({"path": rel, "reason": "unsafe_config_path"})
                continue
            scanned += 1
            if scanned > MAX_CONFIG_FILES:
                raise ValueError("Project exceeds PHP config file limit")
            try:
                if path.stat().st_size > MAX_CONFIG_BYTES:
                    skipped.append({"path": rel, "reason": "config_too_large"})
                    continue
                source = path.read_text(encoding="utf-8")
            except (UnicodeError, OSError):
                skipped.append({"path": rel, "reason": "config_unreadable"})
                continue
            for line_number, line in enumerate(source.splitlines(), 1):
                if not line.strip() or line.lstrip().startswith(("#", ";")):
                    continue
                match = _DIRECTIVE_PATTERN.match(line)
                if match is None:
                    continue
                key = match.group("key").lower()
                policy = DIRECTIVES.get(key)
                if policy is None:
                    continue
                actual = _boolean_value(match.group("value"))
                if actual is None:
                    continue
                rule, severity, undesired = policy
                if actual != (undesired == "enabled"):
                    continue
                indicators.append({
                    "path": rel,
                    "line": line_number,
                    "directive": key,
                    "rule": rule,
                    "severity": severity,
                    "confidence": "review_required",
                    "observation": "A local configuration file contains a value requiring review.",
                    "effective_runtime_confirmed": False,
                })
    return {
        "config_files_examined": scanned,
        "config_indicators": indicators,
        "config_skipped": skipped,
        "limitations": (
            "Offline PHP config-file indicators only; files may be inactive or "
            "overridden by other SAPIs, server settings or deployment. "
            "No values, credentials, effective runtime or CVE exposure inferred."
        ),
    }
