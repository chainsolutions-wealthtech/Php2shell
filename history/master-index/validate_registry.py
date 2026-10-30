#!/usr/bin/env python3
"""PHP2SHELL archive-only index validation; read-only, stdlib only."""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def main() -> int:
    root = load("MASTER_IDENTIFIERS_REGISTRY.json")
    nodes = []
    for kind, path in root["shards"].items():
        shard = load(path)
        if shard["type"] != kind:
            raise ValueError(f"Shard type mismatch: {kind}")
        if len(shard["items"]) != root["counts"][kind]:
            raise ValueError(f"Shard count mismatch: {kind}")
        nodes.extend(shard["items"])
    keys = [n["key"] for n in nodes]
    if len(keys) != len(set(keys)) or set(keys) != set(root["index"]):
        raise ValueError("Duplicate IDs or master index divergence")
    valid = set(keys)
    index = load("MASTER_RELATIONSHIPS_REGISTRY.json")
    edges = []
    for family in index["families"].values():
        if "path" in family:
            edges.extend(load(family["path"])["edges"])
        else:
            for shard in family["subshards"].values():
                edges.extend(load(shard["path"])["edges"])
    if len(edges) != index["total_relations"]:
        raise ValueError("Relations count mismatch")
    seen = set()
    for edge in edges:
        if edge["from"] not in valid or edge["to"] not in valid:
            raise ValueError(f"Dangling edge: {edge}")
        key = (edge["from"], edge["to"], edge["relation"])
        if key in seen:
            raise ValueError(f"Duplicate edge: {key}")
        seen.add(key)
    tasks = load("matrices/MATRIX_ACTIVITIES_TASKS_ACTIONS.json")["tasks"]
    wp = {t["key"]: t for t in tasks}
    state = {}
    def visit(key):
        if state.get(key) == 1:
            raise ValueError(f"Cycle in work packages: {key}")
        if state.get(key) == 2:
            return
        state[key] = 1
        for d in wp[key]["dependency_keys"]:
            if d not in wp:
                raise ValueError(f"Missing dependency: {d}")
            visit(d)
        state[key] = 2
    for key in wp:
        visit(key)
    chronology = load("matrices/MATRIX_WORK_CHRONOLOGY.json")
    if chronology["entry_count"] != len(chronology["entries"]):
        raise ValueError("Chronology count mismatch")
    for item in chronology["entries"]:
        if item["key"] not in valid:
            raise ValueError(f"Chronology item missing: {item['key']}")
    print(json.dumps({"status": "PASS", "identifiers": len(valid),
      "relations": len(edges), "work_packages": len(tasks),
      "chronology": len(chronology["entries"])}, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
