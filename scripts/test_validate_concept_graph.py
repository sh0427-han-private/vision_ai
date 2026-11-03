"""Mutation regression tests for the canonical concept graph and its documents."""
from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import validate_concept_graph as validator


class GraphMutationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.baseline = json.loads(
            validator.GRAPH_PATH.read_text(encoding="utf-8")
        )

    def check_mutation(self, mutate, message: str) -> None:
        graph = copy.deepcopy(self.baseline)
        by_id = {n["id"]: n for n in graph["concepts"]}
        mutate(graph, by_id)
        with tempfile.TemporaryDirectory() as dirname:
            graph_path = Path(dirname) / "mutated.json"
            graph_path.write_text(
                json.dumps(graph, ensure_ascii=False), encoding="utf-8"
            )
            with patch.object(validator, "GRAPH_PATH", graph_path):
                errors = validator.validate()
        self.assertTrue(
            any(message in err for err in errors),
            msg=f"Expected {message!r}, got: {errors}",
        )

    def test_valid_graph(self) -> None:
        self.assertEqual(validator.validate(), [])

    def test_missing_fragment(self) -> None:
        self.check_mutation(
            lambda g, by: by["m.entropy"].update(
                legacy_url="notes/prml.html"
            ),
            "Mapped concept missing fragment: m.entropy",
        )

    def test_missing_anchor(self) -> None:
        self.check_mutation(
            lambda g, by: by["m.entropy"].update(
                legacy_url="notes/prml.html#nonexistent-r1-anchor"
            ),
            "Missing anchor: m.entropy",
        )

    def test_duplicate_id(self) -> None:
        self.check_mutation(
            lambda g, by: g["concepts"].append(
                copy.deepcopy(by["m.scalar"])
            ),
            "Duplicate concept ID: m.scalar",
        )

    def test_cycle(self) -> None:
        def mutate(graph: dict, by: dict) -> None:
            by["m.scalar"]["prerequisites"].append("cnn.base")
            by["cnn.base"]["next_topics"].append("m.scalar")

        self.check_mutation(mutate, "Graph cycle or invalid references")

    def test_missing_reverse_reference(self) -> None:
        self.check_mutation(
            lambda g, by: by["img.pixel"]["next_topics"].remove("img.rgb"),
            "Reverse dependency missing: img.pixel -> img.rgb",
        )

    def test_overrestrictive_edge(self) -> None:
        def mutate(graph: dict, by: dict) -> None:
            by["eval.ood"]["prerequisites"].append("an.threshold")
            by["an.threshold"]["next_topics"].append("eval.ood")

        self.check_mutation(
            mutate, "Over-restrictive curriculum edge: eval.ood <- an.threshold"
        )

    def test_level_catalog_drift(self) -> None:
        self.check_mutation(
            lambda g, by: by["m.entropy"].update(level="Advanced"),
            "Catalog level/status/title mismatch: m.entropy",
        )

    def test_status_catalog_drift(self) -> None:
        self.check_mutation(
            lambda g, by: by["m.entropy"].update(status="existing-section"),
            "Catalog level/status/title mismatch: m.entropy",
        )

    def test_backprop_does_not_require_autograd(self) -> None:
        def mutate(graph: dict, by: dict) -> None:
            by["dl.backprop"]["prerequisites"].append("dl.autograd")
            by["dl.autograd"]["next_topics"].append("dl.backprop")

        self.check_mutation(
            mutate,
            "Over-restrictive curriculum edge: dl.backprop <- dl.autograd",
        )

    def test_cnn_does_not_require_pooling(self) -> None:
        def mutate(graph: dict, by: dict) -> None:
            by["cnn.base"]["prerequisites"].append("cnn.pool")
            by["cnn.pool"]["next_topics"].append("cnn.base")

        self.check_mutation(
            mutate, "Over-restrictive curriculum edge: cnn.base <- cnn.pool"
        )

    def test_temporal_split_does_not_require_video(self) -> None:
        def mutate(graph: dict, by: dict) -> None:
            by["data.temporal"]["prerequisites"].append("video.frame")
            by["video.frame"]["next_topics"].append("data.temporal")

        self.check_mutation(
            mutate,
            "Over-restrictive curriculum edge: data.temporal <- video.frame",
        )

    def test_transitive_redundant_direct_edge(self) -> None:
        def mutate(graph: dict, by: dict) -> None:
            by["cnn.base"]["prerequisites"].append("cnn.stride")
            by["cnn.stride"]["next_topics"].append("cnn.base")

        self.check_mutation(
            mutate, "Transitively redundant edge: cnn.base <- cnn.stride"
        )


if __name__ == "__main__":
    unittest.main()
