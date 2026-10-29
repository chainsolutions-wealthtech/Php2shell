"""Strict offline revalidation of a PHPPATCH review-only packet.

Recompute the packet from current local evidence; never treat a matching
digest, packet, or user-provided JSON as identity, mandate or approval.
No network, PHP execution, patch application or production mutation.
"""
import json
import os
import stat
from pathlib import Path

from .patch_review_packet import build_patch_review_packet

_MAX_PACKET_BYTES = 16_384


def _canonical(value):
    try:
        serialized = json.dumps(
            value, sort_keys=True, separators=(",", ":"), ensure_ascii=True,
            allow_nan=False,
        )
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError("Invalid local review packet") from exc
    if len(serialized.encode("utf-8")) > _MAX_PACKET_BYTES:
        raise ValueError("Local review packet exceeds size limit")
    return serialized


def _reject_duplicate_keys(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError("Duplicate JSON field in local review packet")
        obj[key] = value
    return obj


def _reject_json_constant(_value):
    raise ValueError("Non-finite JSON value in local review packet")


def verify_local_review_packet(packet, project_path, as_of_utc, evidence_id):
    """Compare *every* field against a fresh local, non-authoritative packet.

    A hash alone is not sufficient: this comparison also rejects added fields,
    elevated capability flags, stale evidence and JSON type substitutions.
    """
    if not isinstance(packet, dict):
        raise ValueError("Local review packet must be a JSON object")
    supplied = _canonical(packet)
    expected = build_patch_review_packet(project_path, as_of_utc, evidence_id)
    if supplied != _canonical(expected):
        raise ValueError("Local review packet does not match current evidence")
    return {
        "schema_version": "0.3-preview",
        "verification_scope": "LOCAL_REVIEW_PACKET_MATCH_ONLY_NOT_AUTHORITY",
        "packet_sha256": expected["packet_sha256"],
        "local_lineage_matches": True,
        "packet_signature_verified": False,
        "identity_and_mandate_verified": False,
        "independent_approval_received": False,
        "patch_applied": False,
        "sandbox_tests_executed": False,
        "production_rollback_proven": False,
        "ready_for_production": False,
    }


def _read_bounded_regular_packet(path):
    """Read a regular local file via a pinned descriptor, without following a final symlink.

    This is a defensive offline input reader, NOT an atomic snapshot of a
    mutable filesystem or a proof of the caller's identity/mandate.
    """
    nofollow = getattr(os, "O_NOFOLLOW", None)
    # A missing, zero, negative or non-integer flag cannot prevent symlink following.
    if type(nofollow) is not int or nofollow <= 0:
        raise ValueError("Secure local packet opening unsupported")
    flags = (os.O_RDONLY | nofollow | getattr(os, "O_CLOEXEC", 0)
             | getattr(os, "O_NONBLOCK", 0))
    try:
        fd = os.open(path, flags)
    except OSError as exc:
        raise ValueError("Local review packet unavailable") from exc
    try:
        before = os.fstat(fd)
        if not stat.S_ISREG(before.st_mode) or before.st_size > _MAX_PACKET_BYTES:
            raise ValueError("Local review packet must be a bounded regular file")
        data = bytearray()
        while len(data) <= _MAX_PACKET_BYTES:
            block = os.read(fd, min(4096, _MAX_PACKET_BYTES + 1 - len(data)))
            if not block:
                break
            data.extend(block)
        if len(data) > _MAX_PACKET_BYTES:
            raise ValueError("Local review packet exceeds size limit")
        after = os.fstat(fd)
        if (not stat.S_ISREG(after.st_mode)
                or after.st_size != before.st_size
                or after.st_size != len(data)
                or after.st_mtime_ns != before.st_mtime_ns
                or after.st_ctime_ns != before.st_ctime_ns):
            raise ValueError("Local review packet changed during read")
        return bytes(data)
    except OSError as exc:
        raise ValueError("Local review packet unavailable") from exc
    finally:
        os.close(fd)


def load_and_verify_local_review_packet(packet_file, project_path, as_of_utc,
                                        evidence_id):
    """Load a bounded, regular local JSON file without following symlinks."""
    if not isinstance(packet_file, (str, Path)):
        raise ValueError("Invalid local review packet file")
    path = Path(packet_file)
    if any(part.is_symlink() for part in (path, *path.parents)):
        raise ValueError("Symlinked local review packet path is forbidden")
    data = _read_bounded_regular_packet(path)
    try:
        packet = json.loads(
            data.decode("utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_json_constant,
        )
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError("Invalid local review packet JSON") from exc
    return verify_local_review_packet(
        packet, project_path, as_of_utc, evidence_id,
    )
