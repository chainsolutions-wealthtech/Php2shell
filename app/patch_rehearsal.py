"""In-memory, no-write PHPPATCH config candidate and rollback rehearsal.

This is deliberately narrower than a production patch executor. Only a
previously reported, unambiguous local PHP display_errors=On assignment is
eligible. The module regenerates the proposal, constructs exactly one
replacement in memory, verifies all other bytes and undoes it in memory.

It does not run PHP, apply a diff on disk, authenticate mandates, touch Git,
execute a sandbox/container, or authorize release. No raw file content,
secrets or absolute project paths are returned.
"""
from hashlib import sha256
from pathlib import Path
import re

from .patch_preview import propose_local_ini_patch

_MAX_SOURCE_BYTES = 65_536
_DIFF = re.compile(
    r"\A--- a/(?P<oldpath>[^\r\n]+)\n"
    r"\+\+\+ b/(?P<newpath>[^\r\n]+)\n"
    r"@@ -(?P<line>[1-9]\d*) \+(?P=line) @@\n"
    r"-(?P<before>[^\r\n]*)\n"
    r"\+(?P<after>[^\r\n]*)\n\Z"
)
_ALLOWED_AFTER = "display_errors=Off"


def _safe_source_path(root, relative_name):
    """Reject path escapes and symlinked components before local read."""
    if not isinstance(relative_name, str):
        raise ValueError("Invalid patch target")
    rel = Path(relative_name)
    if (not relative_name or rel.is_absolute() or ".." in rel.parts
            or rel.name.lower() not in {"php.ini", ".user.ini"}):
        raise ValueError("Invalid patch target path")
    path = root
    for part in rel.parts:
        path = path / part
        if path.is_symlink():
            raise ValueError("Symlinked patch target is forbidden")
    if not path.is_file() or path.stat().st_size > _MAX_SOURCE_BYTES:
        raise ValueError("Patch target unavailable or oversized")
    return path


def rehearse_local_ini_patch(project_path, as_of_utc, evidence_id):
    """Recreate a candidate then simulate and reverse one change in memory.

    The returned checks are LOCAL BYTE-LEVEL CHECKS, not PHP runtime
    verification, actual sandbox execution, or production rollback proof.
    """
    root = Path(project_path)
    if root.is_symlink() or not root.is_dir():
        raise ValueError("Project must be a regular local directory")
    root = root.resolve(strict=True)

    # Recompute from the current on-disk evidence; never trust a caller's
    # arbitrary diff or a stale cached scan as executable source.
    proposal = propose_local_ini_patch(root, as_of_utc, evidence_id)
    if (proposal.get("proposal_type") != "LOCAL_PHP_INI_UNAPPLIED_REVIEW_DIFF"
            or proposal.get("mandate_verified") is not False
            or proposal.get("patch_applied") is not False
            or proposal.get("ready_for_production") is not False):
        raise ValueError("Proposal has invalid security gates")
    diff = proposal["unified_diff"]
    match = _DIFF.fullmatch(diff)
    if not match or match["oldpath"] != match["newpath"]:
        raise ValueError("Unexpected patch syntax")
    if match["oldpath"] != proposal["relative_file"]:
        raise ValueError("Patch target disagrees with evidence")
    if match["after"] != _ALLOWED_AFTER:
        raise ValueError("Unsupported candidate setting")
    if sha256(diff.encode("utf-8")).hexdigest() != proposal["diff_sha256"]:
        raise ValueError("Patch fingerprint mismatch")

    path = _safe_source_path(root, proposal["relative_file"])
    data = path.read_bytes()
    if len(data) > _MAX_SOURCE_BYTES or b"\0" in data:
        raise ValueError("Unsafe patch source bytes")
    try:
        original_text = data.decode("utf-8")
    except UnicodeError as exc:
        raise ValueError("Patch source must be UTF-8") from exc

    original_lines = original_text.splitlines(keepends=True)
    line_number = int(match["line"])
    if line_number > len(original_lines):
        raise ValueError("Evidence line missing")
    old_full_line = original_lines[line_number - 1]
    old_body = old_full_line.rstrip("\r\n")
    newline = old_full_line[len(old_body):]
    if old_body != match["before"]:
        raise ValueError("Stale local source or invalid patch context")
    if newline not in {"", "\n", "\r\n"}:
        raise ValueError("Noncanonical line ending")
    replacement = _ALLOWED_AFTER + newline

    candidate_lines = original_lines.copy()
    candidate_lines[line_number - 1] = replacement
    candidate = "".join(candidate_lines).encode("utf-8")
    old_parts = original_text.splitlines(keepends=True)
    changed = [i for i, (before, after) in enumerate(zip(
        old_parts, candidate_lines), 1) if before != after]
    if (changed != [line_number] or len(old_parts) != len(candidate_lines)
            or len(candidate) > _MAX_SOURCE_BYTES):
        raise ValueError("Candidate is not a single, bounded replacement")

    # Simulate rollback with a byte-for-byte check. Never write to disk.
    rolled_back = candidate_lines.copy()
    rolled_back[line_number - 1] = old_full_line
    restored = "".join(rolled_back).encode("utf-8")
    if restored != data:
        raise ValueError("Candidate could not be reversed in memory")
    # Read once more to detect ordinary concurrent file edits. A future
    # authorized worker still needs fd pinning, locks and atomic IO.
    if path.is_symlink() or path.read_bytes() != data:
        raise ValueError("Source changed during local review")
    source_hash = sha256(data).hexdigest()
    return {
        "schema_version": "0.3-preview",
        "evaluation_type": "IN_MEMORY_PHP_INI_CANDIDATE_REHEARSAL_NOT_APPLY",
        "source_evidence_id": evidence_id,
        "source_dossier_fingerprint_sha256":
            proposal["source_dossier_fingerprint_sha256"],
        "relative_file": proposal["relative_file"],
        "source_file_sha256": source_hash,
        "proposed_diff_sha256": proposal["diff_sha256"],
        "candidate_file_sha256": sha256(candidate).hexdigest(),
        "in_memory_rollback_sha256": sha256(restored).hexdigest(),
        "candidate_differs_from_source": candidate != data,
        "exactly_one_line_changed": True,
        "candidate_setting": _ALLOWED_AFTER,
        "in_memory_rollback_matches_original": restored == data,
        "candidate_is_limited_to_php_ini": True,
        "source_files_written": 0,
        "sandbox_container_executed": False,
        "php_runtime_tests_performed": False,
        "mandate_verified": False,
        "independent_approval_received": False,
        "patch_applied": False,
        "production_rollback_proven": False,
        "ready_for_production": False,
        "next_gates": [
            "Authenticate P2 source ownership and permitted repository scope.",
            "Confirm that this ini file is actually active for the HTTP SAPI.",
            "Perform a real isolated apply/test/rollback under an approved mandate.",
            "Compare behavior, compatibility and application regression tests.",
            "Approve and deploy only through the governed GitHub/MCP workflow.",
        ],
        "limitations": (
            "In-memory candidate with one config assignment only. SHA-256 is "
            "not a signature. No PHP executed, no sandbox container started, "
            "no source file changed, no CVE repaired, and no production "
            "rollback or environment compatibility established."
        ),
    }
