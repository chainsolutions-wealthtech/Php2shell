"""Offline Composer manifest/lock consistency review; no install, network or CVE verdict.

This module deliberately avoids semantic-version solving. A lockfile is a
repository artifact, not evidence of installed production dependencies.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import stat
from pathlib import Path

MAX_BYTES = 2_000_000
MAX_PACKAGES = 5000
MAX_OBSERVATIONS = 200
_NAME = re.compile(r"^[a-z0-9_.-]+/[a-z0-9_.-]+$", re.ASCII)
_EXACT = re.compile(r"^v?(\d+\.\d+\.\d+(?:\.\d+)?)$", re.ASCII)
_PLATFORM = {"php", "hhvm", "composer-plugin-api", "composer-runtime-api"}


class _InvalidArtifact(ValueError):
    pass


def _unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise _InvalidArtifact("duplicate JSON key")
        result[key] = value
    return result


def _reject_constant(_value):
    raise _InvalidArtifact("non-finite JSON constant")


def _read_local_json(root: Path, filename: str):
    """Open the named regular file without following a final symlink.

    No path is accepted from a manifest. Linux O_NOFOLLOW prevents the usual
    symlink swap; this is not a general-purpose hostile filesystem sandbox.
    """
    flags = (os.O_RDONLY | getattr(os, "O_CLOEXEC", 0)
             | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0))
    try:
        fd = os.open(root / filename, flags)
    except FileNotFoundError:
        return None, "MISSING"
    except OSError:
        return None, "UNSAFE_OR_UNREADABLE"
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_size > MAX_BYTES:
            return None, "UNSAFE_OR_TOO_LARGE"
        with os.fdopen(fd, "rb", closefd=False) as file:
            raw = file.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            return None, "UNSAFE_OR_TOO_LARGE"
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=_unique_pairs,
                           parse_constant=_reject_constant)
        if not isinstance(value, dict):
            return None, "INVALID_JSON_OBJECT"
        return value, None
    except (UnicodeError, ValueError, OSError):
        return None, "INVALID_OR_UNREADABLE_JSON"
    finally:
        os.close(fd)


def _valid_name(value):
    return isinstance(value, str) and len(value) <= 200 and _NAME.fullmatch(value) is not None


def _is_platform(name):
    return name in _PLATFORM or name.startswith("ext-") or name.startswith("lib-")


def audit_composer_consistency(root):
    """Return a deterministic, redacted, local-only review (never an approval)."""
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Local project root must be a directory")

    manifest, manifest_error = _read_local_json(root, "composer.json")
    lock, lock_error = _read_local_json(root, "composer.lock")
    observations = []
    truncated = False

    def observe(rule, package=None, group=None):
        nonlocal truncated
        if len(observations) >= MAX_OBSERVATIONS:
            truncated = True
            return
        item = {"rule": rule, "confidence": "review_required"}
        if package is not None:
            item["package"] = package
        if group is not None:
            item["group"] = group
        observations.append(item)

    for name, error in (("composer.json", manifest_error), ("composer.lock", lock_error)):
        if error:
            observe("LOCAL_ARTIFACT_" + error, group=name)

    requirements = {}
    locked = {}
    providers = set()
    invalid = manifest_error not in (None, "MISSING") or lock_error not in (None, "MISSING")
    if manifest is not None:
        for group in ("require", "require-dev"):
            section = manifest.get(group, {})
            if not isinstance(section, dict):
                invalid = True
                observe("INVALID_REQUIRE_SECTION", group=group)
                continue
            for name, constraint in sorted(section.items(), key=lambda item: str(item[0])):
                if not isinstance(name, str) or not isinstance(constraint, str):
                    invalid = True
                    observe("INVALID_REQUIREMENT_ENTRY", group=group)
                    continue
                key = name.lower()
                if _is_platform(key):
                    continue
                if not _valid_name(name) or not constraint or len(constraint) > 256:
                    invalid = True
                    observe("INVALID_REQUIREMENT_ENTRY", group=group)
                    continue
                if key in requirements:
                    observe("DUPLICATE_DIRECT_REQUIREMENT", package=key, group=group)
                else:
                    requirements[key] = (group, constraint)
    if lock is not None:
        total = 0
        for group in ("packages", "packages-dev"):
            packages = lock.get(group, [])
            if not isinstance(packages, list):
                invalid = True
                observe("INVALID_LOCK_GROUP", group=group)
                continue
            total += len(packages)
            if total > MAX_PACKAGES:
                invalid = True
                observe("TOO_MANY_LOCK_PACKAGES", group=group)
                break
            for entry in packages:
                if not isinstance(entry, dict):
                    invalid = True
                    observe("INVALID_LOCK_ENTRY", group=group)
                    continue
                name, version = entry.get("name"), entry.get("version")
                if not _valid_name(name) or not isinstance(version, str) or not version or len(version) > 256:
                    invalid = True
                    observe("INVALID_LOCK_ENTRY", group=group)
                    continue
                key = name.lower()
                if key in locked:
                    observe("DUPLICATE_LOCK_PACKAGE", package=key, group=group)
                else:
                    locked[key] = (group, version)
                for field in ("provide", "replace"):
                    claims = entry.get(field, {})
                    if isinstance(claims, dict):
                        providers.update(k.lower() for k in claims if _valid_name(k))
    if manifest is not None and lock is not None and not invalid:
        for name, (group, constraint) in sorted(requirements.items()):
            if name not in locked:
                if name in providers:
                    observe("VIRTUAL_OR_REPLACED_REQUIREMENT_REVIEW", package=name, group=group)
                else:
                    observe("DECLARED_PACKAGE_ABSENT_FROM_LOCK", package=name, group=group)
                continue
            match = _EXACT.fullmatch(constraint)
            locked_match = _EXACT.fullmatch(locked[name][1])
            if match and locked_match and match.group(1) != locked_match.group(1):
                observe("EXACT_PIN_DIFFERS_FROM_LOCK", package=name, group=group)
    status = "insufficient_local_evidence" if invalid or manifest is None or lock is None else "review_required"
    return {
        "schema_version": "0.2",
        "review_type": "OFFLINE_COMPOSER_CONSISTENCY_ONLY",
        "status": status,
        "manifest_present": manifest is not None,
        "lock_present": lock is not None,
        "counts": {"direct_package_requirements": len(requirements), "unique_locked_packages": len(locked)},
        "observations": observations,
        "observations_truncated": truncated,
        "network_requests_made": False,
        "installed_versions_verified": False,
        "vulnerability_applicability": "insufficient_evidence",
        "authorized_for_patch": False,
        "limitations": "Local declared Composer metadata only; no semver solving, installed-package attestation, source/runtime proof, backport review, CVE applicability or authorization.",
    }


def main():
    parser = argparse.ArgumentParser(description="Offline Composer manifest/lock consistency review")
    parser.add_argument("--path", required=True, help="Operator-authorized local project directory")
    args = parser.parse_args()
    print(json.dumps(audit_composer_consistency(args.path), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
