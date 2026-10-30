#!/usr/bin/env python3
"""Read-only continuity router checks. No network, no Git writes."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CANONICAL = "PHP2SHELL-CONT-20261027-ROOT-01"

def load(file):
    return json.loads((ROOT / file).read_text(encoding="utf-8"))

def main():
    manifest = load("CANONICAL_CONTINUITY_MANIFEST.json")
    directory = load("MASTER_IDENTIFIERS_REGISTRY.json")
    relations = load("MASTER_RELATIONSHIPS_REGISTRY.json")
    graph = load("CONTINUITY_ROUTING_GRAPH.json")
    protocol = load("REJOIN_PROTOCOL.json")
    target = "CONTINUITY:" + CANONICAL
    if any(item.get("continuity_id") != CANONICAL for item in (manifest,directory,relations,protocol)):
        raise ValueError("Continuity root mismatch")
    if manifest["canonical_root_id"] != CANONICAL or graph["root"] != CANONICAL:
        raise ValueError("Multiple or mismatched roots")
    if target not in directory["index"]:
        raise ValueError("Root is missing from master identifiers")
    if directory["total_records"] != len(set(directory["index"])):
        raise ValueError("Non-unique or wrong identifier count")
    if manifest["master_index"]["baseline"]["relations"] != relations["total_relations"]:
        raise ValueError("Relation totals not reconciled")
    if manifest["master_index"]["baseline"]["identifiers"] != directory["total_records"]:
        raise ValueError("Master totals not reconciled")
    if not all(ROOT.joinpath(p).exists() for p in ["JOIN_THIS_PROJECT.md","NO_COLLISION_REJOIN_PROTOCOL.md","CONTINUITY_ACTIVITY_LEDGER.jsonl","MASTER_RELATIONSHIPS_REGISTRY.json"]):
        raise ValueError("Missing referenced handoff component")
    if protocol["collision_policy"]["force_push"] or protocol["collision_policy"]["concurrent_writes_without_verified_claim"]:
        raise ValueError("Collision-unsafe rule")
    print(json.dumps({"status":"PASS","root":CANONICAL,
        "identifiers":directory["total_records"],"relations":relations["total_relations"],
        "mode":"read-only structural check"},ensure_ascii=False))
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError,ValueError,KeyError,json.JSONDecodeError) as exc:
        print("FAIL:",exc,file=sys.stderr)
        sys.exit(1)
