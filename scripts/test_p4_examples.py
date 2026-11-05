"""Independent numeric assertions for the P4 teaching examples."""

import hashlib
import math
import re
import subprocess
import sys
import unittest
from html import unescape
from pathlib import Path

from foundations_note import code

from p4_examples import (
    conv_output_dim,
    cross_correlation,
    dot_product,
    gelu,
    hwc_to_chw,
    matrix_multiply,
    pool2x2,
    relu,
)


class P4ExampleTests(unittest.TestCase):
    def test_dot(self):
        self.assertEqual(dot_product([1, 2, 3], [4, 5, 6]), 32)

    def test_matrix(self):
        self.assertEqual(
            matrix_multiply([[1, 2], [3, 4]], [[2, 0], [1, 2]]),
            [[4, 4], [10, 8]],
        )

    def test_hwc_chw(self):
        hwc = [[[9 * h + 3 * w + c for c in range(3)]
                for w in range(3)] for h in range(2)]
        chw = hwc_to_chw(hwc)
        self.assertEqual((len(chw), len(chw[0]), len(chw[0][0])), (3, 2, 3))
        self.assertEqual(sum(len(row) for plane in chw for row in plane), 18)
        for h in range(2):
            for w in range(3):
                for c in range(3):
                    self.assertEqual(hwc[h][w][c], chw[c][h][w])

    def test_correlation(self):
        image = [[5 * y + x for x in range(5)] for y in range(5)]
        kernel = [[-1, 0, 1]] * 3
        result = cross_correlation(image, kernel)
        self.assertEqual(result, [[6, 6, 6]] * 3)
        self.assertEqual(result[0][0], 6)

    def test_shape(self):
        self.assertEqual(conv_output_dim(5, 3), 3)
        self.assertEqual(conv_output_dim(224, 3, stride=1, padding=1), 224)
        self.assertEqual(32 * 3 * 3 * 3 + 32, 896)

    def test_pooling(self):
        self.assertEqual(pool2x2([[1, 2], [3, 4]], "max"), 4)
        self.assertEqual(pool2x2([[1, 2], [3, 4]], "average"), 2.5)

    def test_activation(self):
        self.assertEqual([relu(x) for x in (-2, 0.5, 3)], [0, 0.5, 3])
        self.assertTrue(math.isclose(gelu(0.5), 0.34573123, abs_tol=1e-7))

    def test_invalid_shapes(self):
        with self.assertRaises(ValueError):
            dot_product([1, 2], [1])
        with self.assertRaises(ValueError):
            matrix_multiply([[1, 2]], [[1, 2]])
        with self.assertRaises(ValueError):
            pool2x2([[1, 2], [3]], "max")
        with self.assertRaises(ValueError):
            conv_output_dim(2, 3)

    def test_multiline_display_matches_executed_python_stdout(self):
        """Check authored snippets against real Python stdout and committed HTML."""
        root = Path(__file__).resolve().parents[1]
        cases = (
            ("notes/shape.html", "hwc = ", "(3, 2, 3)\n[0, 3, 6] 18"),
            ("notes/cnn.html", "from math import erf, sqrt", "[0.0, 0.5, 3]\n0.3457"),
        )
        pattern = re.compile(
            r"<pre><code>([^<]*)</code></pre><p>예상 출력:</p>"
            r"<pre><code>([^<]*)</code></pre>", re.DOTALL,
        )
        for rel_path, snippet_marker, expected in cases:
            with self.subTest(page=rel_path):
                html = (root / rel_path).read_text(encoding="utf-8")
                matched = [
                    (unescape(source), unescape(displayed))
                    for source, displayed in pattern.findall(html)
                    if snippet_marker in unescape(source)
                ]
                self.assertEqual(len(matched), 1, "missing or duplicated stdout block")
                source, displayed = matched[0]
                result = subprocess.run(
                    [sys.executable, "-c", source], capture_output=True,
                    text=True, check=True,
                )
                self.assertEqual(result.stdout, expected + "\n")
                self.assertEqual(displayed, result.stdout.rstrip("\n"))
                self.assertEqual(len(displayed.splitlines()), 2)

    def test_deterministic_build_and_committed_generated_pages(self):
        """Rebuild twice and check every generated HTML, not just R1 pages."""
        root = Path(__file__).resolve().parents[1]
        pages = [root / "index.html", *sorted((root / "notes").glob("*.html"))]

        def fingerprint():
            return {p.relative_to(root).as_posix():
                    hashlib.sha256(p.read_bytes()).hexdigest() for p in pages}

        before = fingerprint()
        for _ in range(2):
            subprocess.run(
                [sys.executable, "scripts/build.py"], cwd=root,
                capture_output=True, text=True, check=True,
            )
            self.assertEqual(fingerprint(), before, "build changed committed HTML")

        if (root / ".git").exists():
            clean = subprocess.run(
                ["git", "diff", "--exit-code", "--", "index.html", "notes"],
                cwd=root, capture_output=True, text=True,
            )
            self.assertEqual(clean.returncode, 0, clean.stdout + clean.stderr)

    def test_multiline_html_is_escaped_and_one_line_unchanged(self):
        rendered = code("print('<test>')", "<script>\n&value")
        self.assertIn("<pre><code>&lt;script&gt;\n&amp;value</code></pre>", rendered)
        self.assertNotIn("<script>", rendered)
        self.assertIn("<p>예상 출력: <code>1</code>. ", code("print(1)", "1"))


if __name__ == "__main__":
    unittest.main()
