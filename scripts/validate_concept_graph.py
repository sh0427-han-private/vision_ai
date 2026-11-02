"""Validate the versioned AI knowledge DAG using Python standard library."""
from __future__ import annotations

import json
from collections import Counter, deque
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
GRAPH_PATH = ROOT / "planning" / "concepts.v1.json"
LEVELS = {"Foundation", "Basic", "Intermediate", "Advanced", "Research"}
STATUSES = {"existing-section", "needs-expansion", "planned"}


class AnchorParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.anchors: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if attrs_dict.get("id"):
            self.anchors.add(attrs_dict["id"])


def validate() -> list[str]:
    payload = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    nodes = payload["concepts"]
    parts = payload["parts"]
    errors: list[str] = []

    ids = [node["id"] for node in nodes]
    part_ids = [part["id"] for part in parts]
    node_by_id = {node["id"]: node for node in nodes}
    part_by_id = {part["id"]: part for part in parts}

    for node_id, count in Counter(ids).items():
        if count != 1:
            errors.append(f"Duplicate concept ID: {node_id} ({count})")
    for part_id, count in Counter(part_ids).items():
        if count != 1:
            errors.append(f"Duplicate PART ID: {part_id} ({count})")

    memberships: Counter[str] = Counter()
    for part in parts:
        for node_id in part["concept_ids"]:
            memberships[node_id] += 1
            if node_id not in node_by_id:
                errors.append(f"PART {part['id']} contains unknown concept: {node_id}")
            elif node_by_id[node_id]["part"] != part["id"]:
                errors.append(f"PART mismatch: {node_id} vs {part['id']}")

    for node in nodes:
        node_id = node["id"]
        if node["part"] not in part_by_id:
            errors.append(f"Unknown PART for {node_id}: {node['part']}")
        if memberships[node_id] != 1:
            errors.append(f"Concept {node_id} listed in {memberships[node_id]} PARTs")
        if node["level"] not in LEVELS:
            errors.append(f"Invalid level for {node_id}: {node['level']}")
        if node["status"] not in STATUSES:
            errors.append(f"Invalid status for {node_id}: {node['status']}")

        prerequisites = node["prerequisites"]
        successors = node["next_topics"]
        if len(prerequisites) != len(set(prerequisites)):
            errors.append(f"Duplicate prerequisite for {node_id}")
        if len(successors) != len(set(successors)):
            errors.append(f"Duplicate successor for {node_id}")
        for prerequisite in prerequisites:
            if prerequisite not in node_by_id:
                errors.append(f"Missing prerequisite: {node_id} <- {prerequisite}")
            elif prerequisite == node_id:
                errors.append(f"Self-dependency: {node_id}")
            elif node_id not in node_by_id[prerequisite]["next_topics"]:
                errors.append(f"Reverse dependency missing: {prerequisite} -> {node_id}")
        for successor in successors:
            if successor not in node_by_id:
                errors.append(f"Missing successor: {node_id} -> {successor}")
            elif node_id not in node_by_id[successor]["prerequisites"]:
                errors.append(f"Forward dependency missing: {node_id} -> {successor}")

        legacy_url = node["legacy_url"]
        if node["status"] in {"existing-section", "needs-expansion"} and not legacy_url:
            errors.append(f"Existing section has no URL: {node_id}")
        if node["status"] == "planned" and legacy_url:
            errors.append(f"Planned node unexpectedly has URL: {node_id}")
        if legacy_url:
            parsed = urlsplit(legacy_url)
            target = (ROOT / unquote(parsed.path)).resolve()
            if not target.is_relative_to(ROOT) or not target.is_file():
                errors.append(f"Missing or unsafe legacy page: {node_id} -> {legacy_url}")
            elif parsed.fragment:
                anchors = AnchorParser()
                anchors.feed(target.read_text(encoding="utf-8"))
                if unquote(parsed.fragment) not in anchors.anchors:
                    errors.append(f"Missing anchor: {node_id} -> {legacy_url}")

    in_degree = {node_id: 0 for node_id in ids}
    neighbors = {node_id: [] for node_id in ids}
    for node in nodes:
        for prerequisite in node["prerequisites"]:
            if prerequisite in in_degree and node["id"] in in_degree:
                in_degree[node["id"]] += 1
                neighbors[prerequisite].append(node["id"])

    ready = deque(node_id for node_id, degree in in_degree.items() if degree == 0)
    visited = 0
    while ready:
        current = ready.popleft()
        visited += 1
        for next_id in neighbors[current]:
            in_degree[next_id] -= 1
            if in_degree[next_id] == 0:
                ready.append(next_id)
    if visited != len(ids):
        cyclic = [node_id for node_id, degree in in_degree.items() if degree > 0]
        errors.append(f"Graph cycle or invalid references: {cyclic[:20]}")

    # Targeted curriculum regression checks: not a replacement for human review.
    mandatory_edges = {
        ("dl.backprop", "m.chain"),
        ("tr.encoder", "dl.ln"),
        ("cv.grounding", "cv.dino_detr"),
        ("res.kalman", "res.state"),
    }
    forbidden_edges = {
        ("eval.ood", "an.threshold"),
        ("cv.grounding", "tr.clip"),
        ("res.kalman", "res.hmm"),
        ("ops.batch", "ops.triton"),
        ("an.efficientad", "an.stfpm"),
        ("tr.encoder", "dl.bn"),
    }
    for concept_id, prerequisite in mandatory_edges:
        if concept_id not in node_by_id or prerequisite not in node_by_id:
            errors.append(f"Semantic invariant concept missing: {concept_id}, {prerequisite}")
        elif prerequisite not in node_by_id[concept_id]["prerequisites"]:
            errors.append(f"Required curriculum edge missing: {concept_id} <- {prerequisite}")
    for concept_id, prerequisite in forbidden_edges:
        if (concept_id in node_by_id
                and prerequisite in node_by_id[concept_id]["prerequisites"]):
            errors.append(f"Over-restrictive curriculum edge: {concept_id} <- {prerequisite}")

    catalog_path = ROOT / "planning" / "CONCEPT_CATALOG.md"
    catalog = catalog_path.read_text(encoding="utf-8")
    for node in nodes:
        expected = f"| `{node['id']}` | {node['title']} |"
        if catalog.count(expected) != 1:
            errors.append(f"Catalog concept missing or duplicated: {node['id']}")

    if not errors:
        edges = sum(len(node["prerequisites"]) for node in nodes)
        print(f"Validated {len(parts)} PARTs, {len(nodes)} concepts, {edges} edges.")
    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        raise SystemExit("\n".join(failures))
