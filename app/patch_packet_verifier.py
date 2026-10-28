"""Strict offline revalidation of a PHPPATCH review-only packet.

Recompute the packet from current local evidence; never treat a matching
digest, packet, or user-provided JSON as identity, mandate or approval.
No network, PHP execution, patch application or production mutation.
"""
import json
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


def load_and_verify_local_review_packet(packet_file, project_path, as_of_utc,
                                        evidence_id):
    """Load a bounded, regular local JSON file without following symlinks."""
    if not isinstance(packet_file, (str, Path)):
        raise ValueError("Invalid local review packet file")
    path = Path(packet_file)
    if any(part.is_symlink() for part in (path, *path.parents)):
        raise ValueError("Symlinked local review packet path is forbidden")
    if not path.is_file() or path.stat().st_size > _MAX_PACKET_BYTES:
        raise ValueError("Local review packet unavailable or oversized")
    data = path.read_bytes()
    if len(data) > _MAX_PACKET_BYTES:
        raise ValueError("Local review packet exceeds size limit")
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
