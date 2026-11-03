"""Pure standard-library arithmetic used by the P4 learning examples."""

from __future__ import annotations

from math import erf, floor, sqrt


def dot_product(a: list[float], b: list[float]) -> float:
    if not a or len(a) != len(b):
        raise ValueError("dot_product requires nonempty vectors of equal length")
    return sum(x * y for x, y in zip(a, b))


def matrix_multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    if not a or not b or not b[0]:
        raise ValueError("matrices must not be empty")
    inner = len(a[0])
    if not inner or any(len(row) != inner for row in a):
        raise ValueError("invalid left matrix shape")
    columns = len(b[0])
    if any(len(row) != columns for row in b) or len(b) != inner:
        raise ValueError("matrix inner dimensions must match")
    return [
        [sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(columns)]
        for i in range(len(a))
    ]


def hwc_to_chw(hwc: list[list[list[int]]]) -> list[list[list[int]]]:
    if not hwc or not hwc[0] or not hwc[0][0]:
        raise ValueError("HWC must have nonempty axes")
    height, width, channels = len(hwc), len(hwc[0]), len(hwc[0][0])
    if any(len(row) != width or any(len(pixel) != channels for pixel in row)
           for row in hwc):
        raise ValueError("ragged HWC array")
    return [
        [[hwc[h][w][c] for w in range(width)] for h in range(height)]
        for c in range(channels)
    ]


def cross_correlation(image: list[list[int]], kernel: list[list[int]]) -> list[list[int]]:
    if not image or not kernel or not image[0] or not kernel[0]:
        raise ValueError("empty input")
    h, w, kh, kw = len(image), len(image[0]), len(kernel), len(kernel[0])
    if any(len(row) != w for row in image) or any(len(row) != kw for row in kernel):
        raise ValueError("ragged matrix")
    if kh > h or kw > w:
        raise ValueError("kernel larger than image")
    return [
        [
            sum(image[y + ky][x + kx] * kernel[ky][kx]
                for ky in range(kh) for kx in range(kw))
            for x in range(w - kw + 1)
        ]
        for y in range(h - kh + 1)
    ]


def conv_output_dim(length: int, kernel: int, stride: int = 1,
                    padding: int = 0, dilation: int = 1) -> int:
    if min(length, kernel, stride, dilation) <= 0 or padding < 0:
        raise ValueError("invalid convolution arguments")
    output = floor((length + 2 * padding - dilation * (kernel - 1) - 1) / stride + 1)
    if output <= 0:
        raise ValueError("kernel has no valid output")
    return output


def pool2x2(values: list[list[float]], mode: str) -> float:
    if len(values) != 2 or any(len(row) != 2 for row in values):
        raise ValueError("pool2x2 requires 2 x 2 input")
    flat = [value for row in values for value in row]
    if mode == "max":
        return max(flat)
    if mode == "average":
        return sum(flat) / 4
    raise ValueError("mode must be max or average")


def relu(x: float) -> float:
    return max(0.0, x)


def gelu(x: float) -> float:
    return 0.5 * x * (1.0 + erf(x / sqrt(2.0)))


if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    b = [[2, 0], [1, 2]]
    hwc = [[[h * 9 + w * 3 + c for c in range(3)]
            for w in range(3)] for h in range(2)]
    kernel = [[-1, 0, 1]] * 3
    image = [[5 * y + x for x in range(5)] for y in range(5)]
    print("dot", dot_product([1, 2, 3], [4, 5, 6]))
    print("matmul", matrix_multiply(a, b))
    print("CHW shape", (len(hwc_to_chw(hwc)), 2, 3))
    print("cross-correlation", cross_correlation(image, kernel))
    print("pool", pool2x2([[1, 2], [3, 4]], "max"),
          pool2x2([[1, 2], [3, 4]], "average"))
