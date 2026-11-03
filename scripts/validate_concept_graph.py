"""Validate the versioned AI knowledge DAG using Python standard library."""
from __future__ import annotations

import json
from collections import Counter, deque
from html.parser import HTMLParser
from pathlib import Path
import re
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
        if node["status"] in {"existing-section", "needs-expansion"} and (
                not legacy_url or not urlsplit(legacy_url).fragment):
            errors.append(f"Mapped concept missing fragment: {node_id} -> {legacy_url}")
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
        ("dl.autograd", "m.chain"),
        ("dl.backprop", "m.chain"),
        ("dl.backprop", "dl.forward"),
        ("cnn.base", "cnn.map"),
        ("data.temporal", "ml.split"),
        ("ts.drift", "m.distribution"),
        ("eval.ood", "eval.auc"),
        ("eval.ood", "an.score"),
        ("m.gaussian_multi", "m.covariance"),
        ("cv.mask", "img.pixel"),
        ("an.reverse", "res.distill"),
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
        ("img.pixel", "m.tensor"),
        ("cv.mask", "cv.semantic"),
        ("tr.dino", "tr.vit"),
        ("cv.map", "cv.nms"),
        ("eval.threshold", "ml.calibration"),
        ("ts.changepoint", "ts.cusum"),
        ("an.shift", "an.feature"),
        ("res.em", "res.gmm"),
        ("res.ood", "eval.ood"),
        ("res.distill", "dl.transfer"),
        ("ops.registry", "ops.onnx"),
        ("eng.independent", "eng.agent"),
        ("dl.backprop", "dl.autograd"),
        ("cnn.base", "cnn.pool"),
        ("data.temporal", "data.group"),
        ("data.temporal", "video.frame"),
        ("ops.registry", "data.version"),
        ("ts.drift", "ts.changepoint"),
        ("ts.drift", "ml.generalize"),
        ("cv.iou", "cv.mask"),
        ("cv.iou", "cv.box"),
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

    # Canonical direct edges: no transitively redundant mandatory prerequisites.
    def is_ancestor(start_id: str, target_id: str) -> bool:
        stack = [start_id]
        seen: set[str] = set()
        while stack:
            item = stack.pop()
            if item == target_id:
                return True
            if item in seen or item not in node_by_id:
                continue
            seen.add(item)
            stack.extend(node_by_id[item]["prerequisites"])
        return False

    for node in nodes:
        for predecessor in node["prerequisites"]:
            if any(
                is_ancestor(other, predecessor)
                for other in node["prerequisites"]
                if other != predecessor
            ):
                errors.append(
                    f"Transitively redundant edge: {node['id']} <- {predecessor}"
                )

    summary = Counter(node["status"] for node in nodes)
    edge_count = sum(len(node["prerequisites"]) for node in nodes)
    stamp = (
        f"<!-- graph-snapshot: parts={len(parts)} concepts={len(nodes)} "
        f"edges={edge_count} existing-section={summary['existing-section']} "
        f"needs-expansion={summary['needs-expansion']} "
        f"planned={summary['planned']} -->"
    )
    docs = (
        "CONCEPT_CATALOG.md", "CURRICULUM.md", "CONCEPT_DEPENDENCIES.md",
        "LEARNING_PATHS.md", "IMPLEMENTATION_ROADMAP.md",
        "SEMANTIC_AUDIT.md", "EXISTING_CONTENT_AUDIT.md",
    )
    for filename in docs:
        document = (ROOT / "planning" / filename).read_text(encoding="utf-8")
        if document.count(stamp) != 1:
            errors.append(f"Graph snapshot mismatch: {filename}")

    catalog = (ROOT / "planning" / "CONCEPT_CATALOG.md").read_text(
        encoding="utf-8"
    )
    catalog_rows = catalog.splitlines()
    for node in nodes:
        if node["status"] == "planned":
            coverage = "신규 작성 계획"
        else:
            label = (
                "기존 절" if node["status"] == "existing-section"
                else "기존 소개·보강 필요"
            )
            coverage = f"[{label}](../{node['legacy_url']})"
        expected = (
            f"| `{node['id']}` | {node['title']} | "
            f"{node['level']} | {coverage} |"
        )
        if catalog_rows.count(expected) != 1:
            errors.append(f"Catalog level/status/title mismatch: {node['id']}")

    curriculum = (ROOT / "planning" / "CURRICULUM.md").read_text(
        encoding="utf-8"
    )
    headings = list(
        re.finditer(r"^### (PART \d{2})\. (.+)$", curriculum, re.MULTILINE)
    )
    if len(headings) != len(parts):
        errors.append("Curriculum PART heading count mismatch")
    else:
        for idx, (match, part) in enumerate(zip(headings, parts)):
            if match.group(1) != part["id"] or match.group(2) != part["name"]:
                errors.append(f"Curriculum PART title/order mismatch: {part['id']}")
            section_end = (
                headings[idx + 1].start() if idx + 1 < len(headings)
                else len(curriculum)
            )
            section = curriculum[match.end():section_end]
            concepts_match = re.search(
                r"\*\*Concept \((\d+)개\):\*\* ([^\n]+)", section
            )
            if concepts_match is None:
                errors.append(f"Curriculum concept block missing: {part['id']}")
                continue
            actual_titles = concepts_match.group(2).split(" · ")
            wanted_titles = [node_by_id[item]["title"] for item in part["concept_ids"]]
            if (int(concepts_match.group(1)) != len(part["concept_ids"])
                    or actual_titles != wanted_titles):
                errors.append(f"Curriculum members/count/title mismatch: {part['id']}")

    existing_audit = (ROOT / "planning" / "EXISTING_CONTENT_AUDIT.md").read_text(
        encoding="utf-8"
    )
    coverage_section = existing_audit.split(
        "## 의미론적 감사 이후: 기존 소개와 신규 작성의 구분 (R1)"
    )[-1]
    listed = re.findall(r"^\| `([^\x60]+)` \|", coverage_section, re.MULTILINE)
    expected_expansion = {
        node["id"] for node in nodes if node["status"] == "needs-expansion"
    }
    if len(listed) != len(expected_expansion) or set(listed) != expected_expansion:
        errors.append("Existing content audit needs-expansion status mismatch")

    roadmap = (ROOT / "planning" / "IMPLEMENTATION_ROADMAP.md").read_text(
        encoding="utf-8"
    )
    core = (
        "m.scalar", "m.vector", "m.matrix", "m.tensor",
        "img.tensor", "cnn.conv", "cnn.map", "cnn.base",
    )
    closure = set(core)
    stack = list(core)
    while stack:
        current = stack.pop()
        for predecessor in node_by_id[current]["prerequisites"]:
            if predecessor not in closure:
                closure.add(predecessor)
                stack.append(predecessor)
    p4_section = roadmap.split("## P4 필수 선수 폐포 — P4 구현 (R0)")[-1]
    p4_section = p4_section.split("## P4 구현 단계")[0]
    listed_p4 = re.findall(r"^\| `([^\x60]+)` \|", p4_section, re.MULTILINE)
    if set(listed_p4) != closure or len(listed_p4) != len(closure):
        errors.append(f"P4 prerequisite learning location mismatch: {sorted(closure)}")
    for concept_id in closure:
        p4row = next(
            (line for line in p4_section.splitlines()
             if line.startswith(f"| `{concept_id}` |")), None
        )
        if p4row and not any(
            marker in p4row for marker in ("구현된 신규 페이지", "기존 Section", "구현된 P4 Section")
        ):
            errors.append(f"P4 learning delivery type missing: {concept_id}")

    if not errors:
        edges = sum(len(node["prerequisites"]) for node in nodes)
        print(f"Validated {len(parts)} PARTs, {len(nodes)} concepts, {edges} edges; coverage {dict(summary)}.")
    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        raise SystemExit("\n".join(failures))
