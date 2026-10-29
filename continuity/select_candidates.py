"""Read-only, fail-closed candidate selection for the canonical PHP2SHELL backlog.

This module never acquires claims, executes work, writes GitHub or authorizes S1.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

CONTINUITY_ID = "PHP2SHELL-CONT-20261027-ROOT-01"
SAFE_GATE = "READ_ONLY"
COMPLETE = "VERIFIED_DONE"

def select_candidates(document: dict, evidence: dict) -> list[dict]:
    if document.get("continuity_id") != CONTINUITY_ID:
        raise ValueError("wrong continuity root")
    packages = document.get("work_packages")
    if not isinstance(packages, list) or len(packages) != 61:
        raise ValueError("expected exactly 61 canonical work packages")
    by_id = {}
    for task in packages:
        key = task.get("id")
        if not isinstance(key, str) or key in by_id:
            raise ValueError("invalid or duplicate work package")
        by_id[key] = task
    for task in packages:
        if not isinstance(task.get("depends_on"), list):
            raise ValueError("missing dependencies")
        if any(dep not in by_id for dep in task["depends_on"]):
            raise ValueError("unknown dependency")
    visited, visiting = set(), set()
    def visit(key):
        if key in visiting:
            raise ValueError("dependency cycle")
        if key in visited:
            return
        visiting.add(key)
        for dep in by_id[key]["depends_on"]:
            visit(dep)
        visiting.remove(key)
        visited.add(key)
    for key in by_id:
        visit(key)

    verified = evidence.get("verified_done", {})
    if not isinstance(verified, dict):
        raise ValueError("invalid verified evidence")
    for key, record in verified.items():
        if key not in by_id or not isinstance(record, dict) or not (
            record.get("head_sha") and record.get("ci_url") and record.get("checkpoint_url")
        ):
            raise ValueError("unsubstantiated completion")
    candidates = []
    for task in packages:
        # A pending review is a blocker, not an admissible READ_ONLY job.
        # Unknown and completed statuses must also fail closed.
        if task.get("gate") != SAFE_GATE or task.get("status") != "PLANNED_NOT_ADMITTED":
            continue
        if any(dep not in verified for dep in task["depends_on"]):
            continue
        if task["id"] in verified:
            continue
        candidates.append({"id": task["id"], "lane": task.get("lane"),
                           "title": task.get("title"), "decision": "READ_ONLY_CANDIDATE",
                           "execution_authorized": False,
                           "reason": "requires fresh authority/claim/HEAD checks"})
    return candidates

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=Path, default=Path(__file__).with_name("WORK_PACKAGES.json"))
    parser.add_argument("--evidence", type=Path, required=True)
    args = parser.parse_args()
    result = select_candidates(json.loads(args.registry.read_text()),
                               json.loads(args.evidence.read_text()))
    print(json.dumps({"continuity_id": CONTINUITY_ID, "candidates": result}, indent=2))

if __name__ == "__main__":
    main()
