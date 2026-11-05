"""Beginner math chapters and targeted P4 additions to the existing chapters.

All chapters use the original note()/section() registration contract.
No external runtime dependencies, model training, or new UI framework.
"""
from html import escape


def code(source: str, output: str) -> str:
    # Multiple print() calls must preserve stdout row boundaries. Escape content
    # before rendering it inside <pre><code>; single-line examples stay inline.
    output_html = (
        f'<p>예상 출력:</p><pre><code>{escape(output)}</code></pre>'
        '<p>실제 학습 모델의 출력이 아닌 고정 예제입니다.</p>'
    ) if '\n' in output else (
        f'<p>예상 출력: <code>{escape(output)}</code>. 실제 학습 모델의 출력이 아닌 고정 예제입니다.</p>'
    )
    return (
        '<p><strong>Python 3 표준 라이브러리 예제</strong> — 아래 셀은 독립 실행할 수 있습니다.</p>'
        f'<pre><code>{escape(source.strip())}</code></pre>'
        f'{output_html}'
    )


def related(items: list[tuple[str, str]], missing: str = "") -> str:
    links = "".join(
        f'<li><a href="{escape(href)}">{escape(label)}</a></li>'
        for label, href in items
    )
    note = (
        f'<p>아직 독립 페이지가 없는 연관 개념: {escape(missing)}'
        ' (학습 계획이며 클릭 가능한 링크로 제공하지 않습니다).</p>'
        if missing else ""
    )
    return '<nav aria-label="선수·후속 학습"><h3>연결 학습</h3><ul>' + links + '</ul></nav>' + note


def register_foundation_notes(note, section, table, callout, equation, svg):
    """Register seven original beginner pages before the eight legacy notes."""
    render_svg = svg

    def svg(body, height, caption):
        """Show an explicit horizontal-swipe hint above narrow mobile diagrams."""
        html = render_svg(body, height, caption)
        return html.replace(
            '<figure><div class="diagram">',
            '<figure><p class="small">도식이 화면보다 넓다면 그림 영역을 '
            '좌우로 스크롤해 입력·출력을 확인하세요.</p><div class="diagram">',
            1,
        )

    note(
        "scalar", "Scalar: 값 하나에서 시작하기",
        "한 개의 수, 자료형, 단위를 구분하고 다른 개념의 입력값으로 연결합니다.",
        "기초 수학", "P4 · 01 SCALAR", 12, [
            section("scalar", "Scalar는 왜 필요한가?", """
<p>Scalar(스칼라)는 하나의 수치입니다. 이미지 밝기 한 값이나 학습률, 길이와 같은 양을 표현할 수 있지만, 값이 하나라고 단위까지 자동으로 정해지지는 않습니다. 예를 들어 <code>5</code>는 정수(int)일 수 있고 <code>5.0</code>은 부동소수점(float)일 수 있습니다.</p>
<p><strong>입력 → 처리 → 출력:</strong> 거리 5 m와 시간 2 s → 나누기 → 평균 속력 2.5 m/s. 두 값을 같은 단위의 숫자로 취급하지 않고 양과 단위를 함께 기록합니다.</p>"""
                + svg('<rect x="50" y="58" width="210" height="72" rx="12" fill="#eaf1ff"/><text x="155" y="98" text-anchor="middle" fill="#18345b" font-size="20">거리 5 m</text><rect x="295" y="58" width="160" height="72" rx="12" fill="#e6f5f0"/><text x="375" y="98" text-anchor="middle" fill="#18345b" font-size="20">시간 2 s</text><path d="M475 94 H527" stroke="#5379b8" stroke-width="3"/><rect x="535" y="58" width="178" height="72" rx="12" fill="#edf3ff"/><text x="624" y="98" text-anchor="middle" fill="#18345b" font-size="20">2.5 m/s</text>', 180, 'Scalar 두 개의 값과 단위를 이용한 속력 계산 (합성값).')),
            section("example", "값·자료형·단위 계산",
                equation("P4_SCALAR") +
                table(["양", "값", "자료형·단위"], [
                    ("거리", "<code>5.0</code>", "float · m"),
                    ("시간", "<code>2.0</code>", "float · s"),
                    ("속력", "<code>2.5</code>", "float · m/s"),
                ]) + callout("주의", "동일한 숫자라도 단위가 다르면 직접 더할 수 없습니다. float의 소수 표현에는 반올림 오차가 생길 수 있습니다.")),
            section("python", "재현 가능한 Python",
                code("distance_m = 5.0\nseconds = 2.0\nprint(distance_m / seconds)", "2.5")
                + related([("Vector로 여러 Scalar 묶기", "vector.html#vector"), ("Function에서 입출력 보기", "function.html#function"), ("기존 PRML 개요", "prml.html#ch1")], "Mean / Variance")),
        ],
        [("Python Documentation · Numeric Types", "https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex", "정수와 부동소수점의 의미와 연산"),
         ("NIST · SI Units", "https://www.nist.gov/pml/owm/metric-si/si-units", "값과 단위 구분")],
    )
    note(
        "vector", "Vector: 순서 있는 수치들",
        "원소·축·차원을 구분하고 벡터의 길이를 수치로 검산합니다.",
        "기초 수학", "P4 · 02 VECTOR", 14, [
            section("vector", "Vector의 원소와 좌표",
                """<p>Vector(벡터)는 숫자를 순서대로 놓아 만든 수학적 객체입니다. 예를 들어 <code>[3,4]</code>는 2차원 벡터이며 숫자 3과 4가 각각 두 축의 성분입니다. 이때 <strong>수학의 벡터 차원</strong>과 배열의 <strong>축 개수(rank)</strong>를 혼동하지 않습니다. 리스트 [3,4]는 길이 2의 1축 배열입니다.</p><p>위치 벡터 (3,4)는 원점에서 x 방향 3, y 방향 4만큼 이동한 화살표로 생각할 수 있습니다.</p>"""
                + svg('<path d="M95 160 H420 M95 160 V25" stroke="#5379b8" stroke-width="2"/><path d="M95 160 L285 40" stroke="#2454d8" stroke-width="5"/><path d="M285 40 L266 45 L276 63 Z" fill="#2454d8"/><path d="M285 40 V160" stroke="#95a8cf" stroke-dasharray="6 5"/><text x="190" y="183" fill="#18345b" font-size="19">x = 3</text><text x="297" y="98" fill="#18345b" font-size="19">y = 4</text><text x="425" y="80" fill="#18345b" font-size="22">|v| = 5</text>', 210, '벡터 (3,4)의 직교 좌표와 유클리드 길이 5.')),
            section("example", "원소·축·길이 계산",
                equation("P4_VECTOR") +
                table(["입력", "처리", "출력"], [
                    ("[3, 4]", "3² + 4² = 25, 제곱근", "5"),
                    ("[1, 2, 3]", "원소 개수", "3"),
                ]) + callout("조건", "두 벡터를 원소별로 더하려면 같은 좌표계와 호환되는 차원이 필요합니다.")),
            section("python", "재현 가능한 Python",
                code("v = [3, 4]\nlength = sum(x * x for x in v) ** 0.5\nprint(length)", "5.0")
                + related([("선수 Scalar", "scalar.html#scalar"), ("Matrix로 확장", "matrix.html#matrix"), ("Dot Product 계산", "dot-product.html#dot-product")], "Norm·Cosine Similarity")),
        ],
        [("NumPy · ndarray", "https://numpy.org/doc/stable/reference/arrays.ndarray.html", "shape·axis와 원소 표현의 공식 정의")],
    )
    note(
        "matrix", "Matrix: 행과 열, 그리고 곱셈",
        "2차원 행렬의 shape와 두 행렬의 곱을 직접 계산합니다.",
        "기초 수학", "P4 · 03 MATRIX", 18, [
            section("matrix", "행(row)과 열(column)",
                """<p>Matrix(행렬)는 행과 열로 수치를 배치합니다. <code>[[1,2],[3,4]]</code>는 2행 2열(shape [2,2])입니다. 각 행은 길이 2의 벡터이고, 열도 두 개 존재합니다. 행렬의 곱은 원소별 곱이 아니라 <strong>왼쪽 행 × 오른쪽 열의 Dot Product</strong>입니다.</p>"""
                + svg('<rect x="36" y="38" width="173" height="119" rx="10" fill="#edf3ff"/><text x="120" y="84" text-anchor="middle" font-size="23" fill="#203455">1    2</text><text x="120" y="129" text-anchor="middle" font-size="23" fill="#203455">3    4</text><text x="250" y="108" font-size="26" fill="#203455">×</text><rect x="295" y="38" width="173" height="119" rx="10" fill="#e5f5f2"/><text x="382" y="84" text-anchor="middle" font-size="23" fill="#203455">2    0</text><text x="382" y="129" text-anchor="middle" font-size="23" fill="#203455">1    2</text><text x="490" y="108" font-size="26" fill="#203455">=</text><rect x="533" y="38" width="181" height="119" rx="10" fill="#edf3ff"/><text x="622" y="84" text-anchor="middle" font-size="23" fill="#203455">4    4</text><text x="622" y="129" text-anchor="middle" font-size="23" fill="#203455">10    8</text>', 195, '두 2×2 행렬의 곱; 결과 행렬의 값은 행과 열의 내적으로 계산합니다.')),
            section("example", "Matrix Multiplication 수동 검산",
                equation("P4_MATRIX") +
                table(["출력 원소", "행 × 열", "값"], [
                    ("C[0,0]", "1×2 + 2×1", "4"),
                    ("C[0,1]", "1×0 + 2×2", "4"),
                    ("C[1,0]", "3×2 + 4×1", "10"),
                    ("C[1,1]", "3×0 + 4×2", "8"),
                ]) + callout("Shape 계약", "일반적으로 [m,k] @ [k,n] → [m,n]입니다. 안쪽 k가 일치하지 않으면 행렬곱은 정의되지 않습니다.")),
            section("python", "재현 가능한 Python",
                code("a = [[1, 2], [3, 4]]\nb = [[2, 0], [1, 2]]\nc = [[sum(a[i][k] * b[k][j] for k in range(2))\n      for j in range(2)] for i in range(2)]\nprint(c)", "[[4, 4], [10, 8]]")
                + related([("선수 Vector", "vector.html#vector"), ("Tensor·다차원 배열", "tensor.html#tensor"), ("Dot Product 원리", "dot-product.html#dot-product")], "일반 Matrix Multiplication")),
        ],
        [("NumPy · matmul", "https://numpy.org/doc/stable/reference/generated/numpy.matmul.html", "행렬곱과 차원 계약")],
    )
    note(
        "tensor", "Tensor: Rank와 Shape 이해하기",
        "여러 축을 가진 배열의 크기와 요소 수를 구분합니다.",
        "기초 수학", "P4 · 04 TENSOR", 16, [
            section("tensor", "Tensor의 Rank는 무엇인가?",
                """<p>Tensor(텐서)는 수치 배열을 일반화한 표현입니다. 초급 실습에서 Scalar는 rank 0, Vector는 rank 1, Matrix는 rank 2로 볼 수 있으며, RGB 이미지처럼 축이 여러 개인 배열도 Tensor로 표현합니다. 여기서 rank는 <strong>배열의 축 수(ndim)</strong>를 뜻하며 선형대수학의 행렬 rank와 다릅니다.</p><p>예제 shape <code>[2,2,3]</code>은 첫 번째 축에 항목 2개, 두 번째에 2개, 세 번째에 채널 3개로 <strong>총 12개 값</strong>입니다. 축 이름과 물리 의미는 배열만 보고 자동 결정되지 않습니다.</p>"""
                + svg('<rect x="65" y="50" width="240" height="105" rx="8" fill="#edf3ff" stroke="#9eb7e9"/><rect x="110" y="34" width="240" height="105" rx="8" fill="#dbe7fa" stroke="#7d9fdd"/><rect x="155" y="18" width="240" height="105" rx="8" fill="#c3d4f4" stroke="#5682c8"/><text x="445" y="74" fill="#203455" font-size="21">[2, 2, 3]</text><text x="445" y="108" fill="#526681" font-size="18">2 × 2 × 3 = 12</text>', 196, '축 3개를 가진 Tensor의 개념도; 실제 배열 요소 수는 12개입니다.')),
            section("example", "축 수와 요소 수",
                equation("P4_TENSOR") +
                table(["표현", "shape", "rank / 값 수"], [
                    ("Scalar", "[]", "0 / 1"),
                    ("Vector", "[4]", "1 / 4"),
                    ("Matrix", "[2,3]", "2 / 6"),
                    ("RGB 배열", "[2,2,3]", "3 / 12"),
                ]) + callout("주의", "PyTorch의 Tensor와 수학적 텐서 이론은 관련되지만 완전히 같은 범위를 뜻하지 않습니다. 축 순서, dtype, device 및 단위를 구분해야 합니다.")),
            section("python", "재현 가능한 Python",
                code("x = [[[0, 1, 2], [3, 4, 5]],\n     [[6, 7, 8], [9, 10, 11]]]\nshape = (len(x), len(x[0]), len(x[0][0]))\nprint(shape, shape[0] * shape[1] * shape[2])", "(2, 2, 3) 12")
                + related([("선수 Matrix", "matrix.html#matrix"), ("Shape/Axis", "shape.html#shape"), ("Image Tensor 기존 설명", "pixels.html#layout")], "NumPy ndarray 사용법")),
        ],
        [("PyTorch · Tensor", "https://docs.pytorch.org/docs/stable/tensors.html", "Tensor의 shape·dtype·device")],
    )
    note(
        "shape", "Shape·Dimension·Axis: 숫자의 위치를 읽기",
        "축의 순서를 실제로 바꿔도 18개 값이 보존되는지 확인합니다.",
        "기초 수학", "P4 · 05 SHAPE", 18, [
            section("shape", "Shape는 무엇을 정하는가?",
                """<p>Shape(형상)는 축별 길이를 모아 놓은 튜플입니다. Dimension(차원)은 문맥에 따라 축 수 또는 축 길이를 뜻할 수 있으므로 모호하면 <strong>rank=축 수</strong>, <strong>axis=축 번호</strong>, <strong>size=해당 축 길이</strong>로 분리해 적습니다.</p><p>이미지 HWC <code>(2,3,3)</code>은 높이 2, 너비 3, 채널 3이며 총 <strong>18개 원소</strong>입니다. 채널을 첫 축으로 옮긴 CHW는 <code>(3,2,3)</code>입니다. 같은 18개 값이라도 요소의 위치를 바르게 옮기려면 <code>transpose</code>를 사용합니다.</p>"""
                + svg('<rect x="40" y="40" width="272" height="116" rx="9" fill="#edf3ff"/><text x="175" y="82" text-anchor="middle" fill="#203455" font-size="24">HWC</text><text x="175" y="120" text-anchor="middle" fill="#526681" font-size="22">(2, 3, 3)</text><path d="M334 98 H424" stroke="#2454d8" stroke-width="4"/><path d="M424 98 l-15 -8 v16 z" fill="#2454d8"/><rect x="448" y="40" width="272" height="116" rx="9" fill="#e5f5f2"/><text x="580" y="82" text-anchor="middle" fill="#203455" font-size="24">CHW</text><text x="580" y="120" text-anchor="middle" fill="#526681" font-size="22">(3, 2, 3)</text>', 198, 'Transpose로 HWC에서 CHW 축 순서 변경: 18개 원소 보존.')),
            section("example", "Reshape와 Transpose를 구분",
                equation("P4_SHAPE") +
                table(["연산", "shape", "의미"], [
                    ("HWC 시작", "[2,3,3]", "h,w,c"),
                    ("CHW = transpose", "[3,2,3]", "c,h,w"),
                    ("원소 개수", "2×3×3 = 3×2×3 = 18", "값 수 동일"),
                ]) + callout("중요", "reshape는 데이터 배열을 다른 크기로 해석할 뿐 HWC 축을 CHW로 바꾸지 않습니다. transpose/permute가 필요합니다.")),
            section("python", "18개 값 보존 검산",
                code("hwc = [[[9*h + 3*w + c for c in range(3)]\n        for w in range(3)] for h in range(2)]\nchw = [[[hwc[h][w][c] for w in range(3)]\n        for h in range(2)] for c in range(3)]\nprint((len(chw), len(chw[0]), len(chw[0][0])))\nprint(chw[0][0], sum(len(row) for plane in chw for row in plane))", "(3, 2, 3)\n[0, 3, 6] 18")
                + related([("선수 Tensor", "tensor.html#tensor"), ("Image Tensor HWC/CHW/NCHW", "pixels.html#layout"), ("Kernel로 연결", "cnn.html#kernel")], "Broadcasting과 Strides")),
        ],
        [("NumPy · transpose", "https://numpy.org/doc/stable/reference/generated/numpy.transpose.html", "Axis permutation의 정확한 의미"),
         ("PyTorch · permute", "https://docs.pytorch.org/docs/stable/generated/torch.permute.html", "Tensor 차원 교환")],
    )
    note(
        "dot-product", "Dot Product: 곱하고 모두 더하기",
        "입력의 대응 원소를 곱해 더한 결과가 Scalar 32임을 검산합니다.",
        "기초 수학", "P4 · 06 DOT PRODUCT", 16, [
            section("dot-product", "왜 Dot Product를 배우는가?",
                """<p>Dot Product(내적)는 길이가 같은 두 벡터의 대응 원소끼리 곱한 뒤 전부 더하는 연산입니다. 예를 들어 입력 <code>[1,2,3]</code>과 가중치 <code>[4,5,6]</code>을 합치면 결과는 <strong>Scalar 하나</strong>입니다. Kernel의 원소별 곱·합이나 Matrix Multiplication도 이 계산을 반복합니다.</p>"""
                + svg('<rect x="24" y="35" width="335" height="116" rx="9" fill="#edf3ff"/><text x="190" y="75" text-anchor="middle" fill="#203455" font-size="22">1×4  +  2×5  +  3×6</text><text x="190" y="119" text-anchor="middle" fill="#526681" font-size="22">4  +  10  +  18</text><path d="M375 90 H468" stroke="#2454d8" stroke-width="4"/><path d="M468 90 l-15 -8 v16 z" fill="#2454d8"/><rect x="495" y="35" width="217" height="116" rx="9" fill="#e5f5f2"/><text x="600" y="99" text-anchor="middle" fill="#203455" font-size="33">32</text>', 190, 'Dot Product의 세 쌍 원소별 곱셈·합산: 4 + 10 + 18 = 32.')),
            section("example", "단계별 수치 검산",
                equation("P4_DOT") +
                table(["위치", "곱", "누적 합"], [
                    ("0", "1×4 = 4", "4"),
                    ("1", "2×5 = 10", "14"),
                    ("2", "3×6 = 18", "32"),
                ]) + callout("조건", "두 벡터의 길이가 같아야 합니다. Dot Product는 원소별 곱 배열이 아니라 곱의 합인 Scalar를 반환합니다.")),
            section("python", "재현 가능한 Python",
                code("a = [1, 2, 3]\nb = [4, 5, 6]\nassert len(a) == len(b)\nprint(sum(x * y for x, y in zip(a, b)))", "32")
                + related([("선수 Vector", "vector.html#vector"), ("Matrix Multiplication", "matrix.html#matrix"), ("Spatial Kernel", "cnn.html#kernel")], "Cosine Similarity")),
        ],
        [("NumPy · dot", "https://numpy.org/doc/stable/reference/generated/numpy.dot.html", "1차원 배열의 Dot Product")],
    )
    note(
        "function", "Function: 입력과 출력을 연결하기",
        "선형·Affine·비선형 함수를 구분하고 출력값을 직접 계산합니다.",
        "기초 수학", "P4 · 07 FUNCTION", 16, [
            section("function", "Function(함수)은 무엇을 하는가?",
                """<p>Function(함수)는 입력을 정해진 규칙에 따라 출력으로 변환하는 대응입니다. 같은 입력에는 같은 출력이 나와야 하는 일반적인 결정적 함수 예시를 먼저 봅니다. <code>f(x)=2x</code>는 선형(linear), <code>g(x)=2x+1</code>은 상수항이 있는 Affine, <code>h(x)=max(0,x)</code>는 ReLU 비선형 함수입니다.</p><p>MLP와 CNN의 Activation은 여러 층이 단순한 하나의 Affine 변환으로 합쳐지는 것을 막고 복잡한 대응을 학습하게 합니다.</p>"""
                + svg('<rect x="50" y="45" width="160" height="107" rx="12" fill="#edf3ff"/><text x="130" y="107" text-anchor="middle" fill="#203455" font-size="26">x = −2</text><path d="M222 98 H298" stroke="#2454d8" stroke-width="4"/><rect x="314" y="45" width="169" height="107" rx="12" fill="#e5f5f2"/><text x="397" y="108" text-anchor="middle" fill="#203455" font-size="22">ReLU(x)</text><path d="M497 98 H556" stroke="#2454d8" stroke-width="4"/><rect x="570" y="45" width="145" height="107" rx="12" fill="#edf3ff"/><text x="643" y="108" text-anchor="middle" fill="#203455" font-size="30">0</text>', 192, 'ReLU는 음수 입력 −2를 0으로 바꾸는 비선형 함수입니다.')),
            section("example", "선형·Affine·ReLU의 출력 비교",
                equation("P4_FUNCTION") +
                table(["입력", "선형 f(x)=2x", "Affine g(x)=2x+1", "ReLU h(x)"], [
                    ("−2", "−4", "−3", "0"),
                    ("0", "0", "1", "0"),
                    ("3", "6", "7", "3"),
                ]) + callout("주의", "머신러닝 문맥에서 Linear Layer는 bias가 있어도 관례적으로 Linear라고 부르지만, 수학적으로 Wx+b는 b가 0이 아니면 Affine입니다.")),
            section("python", "재현 가능한 Python",
                code("f = lambda x: 2*x\ng = lambda x: 2*x + 1\nh = lambda x: max(0, x)\nprint(f(-2), g(-2), h(-2))", "-4 -3 0")
                + related([("선수 Scalar", "scalar.html#scalar"), ("CNN Activation · ReLU/GELU", "cnn.html#nonlinear")], "Derivative와 Chain Rule")),
        ],
        [("PyTorch · ReLU", "https://docs.pytorch.org/docs/stable/generated/torch.nn.ReLU.html", "비선형 Activation"),
         ("PyTorch · Linear", "https://docs.pytorch.org/docs/stable/generated/torch.nn.Linear.html", "y=xA^T+b (Affine) 계층")],
    )


def extend_p4_notes(notes, section, table, callout, equation, svg):
    """Augment precise existing anchors, retaining their authored bodies."""
    p4_additions = {
        "pixels": {
            "pixels": (
                '<h3>P4 보강 · Decode와 RGB 채널을 분리하기</h3>'
                '<p>Pixel은 공간 격자 한 위치의 샘플 값입니다. JPEG/PNG의 압축 바이트는 곧바로 '
                '숫자 배열이 아니며, <strong>Decode 이후</strong> RGB가 [220,60,30]이면 R=220, '
                'G=60, B=30인 한 위치의 세 값입니다. Tensor 이론을 배우지 않아도 '
                '한 픽셀의 색을 먼저 이해할 수 있습니다. 8-bit unsigned 정수 값의 범위는 '
                '채널마다 0~255이고, 3개 값을 더한 310은 색의 다른 채널이 아니라 단순 합계입니다.</p>'
                + table(["위치", "채널", "8-bit 값"], [
                    ("(y=0,x=0)", "R", "220"),
                    ("(y=0,x=0)", "G", "60"),
                    ("(y=0,x=0)", "B", "30"),
                ])
                + related([("Scalar", "scalar.html#scalar"), ("Vector", "vector.html#vector"),
                           ("Image Tensor·Axis", "pixels.html#layout")])
            ),
            "layout": (
                '<h3>P4 보강 · 실제 HWC→CHW 축 재배치</h3>'
                '<p>입력 HWC <code>(2,3,3)</code>은 18개 int 값입니다. '
                '<code>hwc[h][w][c]</code>를 <code>chw[c][h][w]</code>로 옮기면 '
                'CHW는 <code>(3,2,3)</code>이고, R 채널 첫 행은 <code>[0,3,6]</code>입니다. '
                '가상 18개 원소를 보존하되 각 채널의 위치는 바뀝니다. '
                '<strong>reshape만으로 HWC를 CHW로 변환하지 않습니다.</strong></p>'
                + code("hwc = [[[9*h+3*w+c for c in range(3)] for w in range(3)] for h in range(2)]\n"
                       "chw = [[[hwc[h][w][c] for w in range(3)] for h in range(2)] for c in range(3)]\n"
                       "print(len(chw), len(chw[0]), len(chw[0][0]), chw[0][0])",
                       "3 2 3 [0, 3, 6]")
                + related([("Shape·Axis 수학 선행", "shape.html#shape"), ("Kernel", "cnn.html#kernel")])
            ),
        },
        "cnn": {
            "overview": (
                '<h3>P4 보강 · Feature Map과 Pooling 없는 CNN</h3>'
                '<p>단일 채널 5×5 입력에 3×3 Kernel, stride=1, padding=0을 적용하면 '
                '공간 Feature Map은 3×3입니다. 출력 채널 32개를 학습하는 3×3 Conv가 '
                '[B,3,224,224] 입력을 받으면 결과는 [B,32,224,224](stride=1, padding=1)입니다. '
                '32개 출력 채널은 각각 3개 입력 채널의 가중합으로 계산됩니다.</p>'
                '<p><strong>구성 예:</strong> Conv → ReLU → Conv → ReLU → (필요하면 Pooling) '
                '→ Task Head. Pooling 없이도 CNN은 정의되며, 학습 중 달라지는 것은 '
                'Conv 가중치·bias 등의 파라미터입니다. 여기의 Kernel 수치는 고정된 설명용 필터입니다.</p>'
                + related([("Shape 계산", "cnn.html#shape"), ("Kernel 수치 예제", "cnn.html#kernel"),
                           ("선택 Pooling", "cnn.html#pooling")])
            ),
            "convolution": (
                '<h3>P4 보강 · 5×5 연속 정수 입력과 좌우 차분</h3>'
                '<p>입력 행렬은 첫 행 [0,1,2,3,4], 다음 행 [5,6,7,8,9], 마지막 행 '
                '[20,21,22,23,24]인 <strong>고정된 합성 5×5 값</strong>입니다. '
                'Kernel은 3개 행 모두 <code>[-1,0,1]</code>, bias=0입니다. '
                '좌상단 3×3 패치의 합은 (−0+2)+(−5+7)+(−10+12)=<strong>6</strong>입니다. '
                '오른쪽으로 숫자가 증가할 때 양수가 되는 부호 방향입니다. '
                'Stride 1, Padding 0 결과는 모든 칸이 6인 <strong>3×3</strong> 출력입니다.</p>'
                '<p>PyTorch <code>Conv2d</code>의 일반적인 공간 연산은 필터를 뒤집지 않은 '
                'Cross-correlation이며, 수학의 엄밀한 Convolution과 구분합니다. '
                '기존 인터랙티브의 이진 이미지 [0,0,1,1,1]은 별개의 고정 예제입니다.</p>'
                + related([("Dot Product", "dot-product.html#dot-product"), ("Kernel", "cnn.html#kernel")])
            ),
            "channels": (
                '<h3>P4 보강 · 채널 혼합과 파라미터 수</h3>'
                '<p>가중치 shape <code>[32,3,3,3]</code>는 32개 출력 필터 각각에 '
                '3개 입력 채널 × 3×3 공간 가중치가 존재한다는 뜻입니다. '
                'bias=True, groups=1이면 <strong>32×3×3×3+32=896개</strong> 학습 가능 '
                '파라미터입니다. batch 크기 B는 가중치 수에 곱하지 않습니다. '
                '공간 크기 224×224를 유지하려면 stride=1, padding=1, dilation=1입니다.</p>'
            ),
            "shape": (
                '<h3>P4 보강 · 출력 Shape 직접 검산</h3>'
                + equation("P4_CONV_SHAPE") +
                '<p>H=W=5, K=3, stride=1, padding=0, dilation=1이면 '
                '(5−3)/1+1=3이므로 결과는 3×3입니다. 각 방향별로 따로 계산하고 '
                'floor와 0 이하 출력 같은 경계조건을 확인합니다. '
                'padding=1인 224×224 입력에서는 224×224를 보존합니다.</p>'
                + related([("Shape/Axis", "shape.html#shape"), ("Feature Map", "cnn.html#overview")])
            ),
            "nonlinear": (
                '<h3>P4 보강 · ReLU와 GELU를 구분하기</h3>'
                '<p><strong>ReLU(x)=max(0,x)</strong>: 입력 [-2,0.5,3] → [0,0.5,3]. '
                '<strong>GELU(x)=0.5x[1+erf(x/√2)]</strong>는 음수도 작은 음수로 '
                '남을 수 있는 매끄러운 비선형 함수입니다. 예를 들어 '
                'GELU(0.5)≈0.3457이고 ReLU(0.5)=0.5입니다. '
                'ReLU는 x&lt;0에서 도함수 0, x&gt;0에서 1이며 x=0의 미분은 '
                '정의되지 않으므로 구현에서 convention을 사용합니다. '
                'GELU는 ReLU를 단순히 이름만 바꾼 함수가 아닙니다.</p>'
                + code("from math import erf, sqrt\n"
                       "relu = lambda x: max(0.0, x)\n"
                       "gelu = lambda x: 0.5*x*(1+erf(x/sqrt(2)))\n"
                       "print([relu(x) for x in [-2, 0.5, 3]])\n"
                       "print(round(gelu(0.5), 4))",
                       "[0.0, 0.5, 3]\n0.3457")
                + related([("Function·Linear/Nonlinear", "function.html#function"),
                           ("Feature Map과 CNN", "cnn.html#overview")])
            ),
        },
    }
    for item in notes:
        if item["slug"] in p4_additions:
            updates = p4_additions[item["slug"]]
            item["sections"] = [
                (anchor, title, body + updates.get(anchor, ""))
                for anchor, title, body in item["sections"]
            ]

    cnn = next(item for item in notes if item["slug"] == "cnn")
    sections = cnn["sections"]
    kernel = section(
        "kernel", "Kernel: 고정 필터와 학습 가중치의 차이",
        """<p>Kernel(공간 필터)은 작은 2차원 가중치 격자입니다. 여기서는 3×3 좌우 차분 Kernel을 사용하며 각 행이 [-1,0,1]입니다. 각 입력 패치와 같은 위치의 9개 값을 곱해 합산합니다. 입력은 5×5 int 합성 데이터, 출력은 bias=0인 3×3 Cross-correlation입니다.</p>"""
        + equation("P4_KERNEL")
        + table(["좌상단 3×3 패치 행", "Kernel 행", "행별 합"], [
            ("[0,1,2]", "[-1,0,1]", "(−0)+0+2=2"),
            ("[5,6,7]", "[-1,0,1]", "−5+0+7=2"),
            ("[10,11,12]", "[-1,0,1]", "−10+0+12=2"),
        ])
        + '<p>세 행 합계는 <strong>6</strong>입니다. 양의 오른쪽 기울기에 양의 반응을 갖습니다. '
          '기존 라이브러리의 Conv는 Kernel을 뒤집지 않는 Cross-correlation로 계산합니다. '
          '이 수업은 <strong>고정 가중치의 순전파 계산</strong>이며 역전파로 Kernel을 '
          '학습하거나 학습 정확도를 평가하지 않습니다.</p>'
        + code("image = [[5*y+x for x in range(5)] for y in range(5)]\n"
               "k = [[-1, 0, 1]]*3\n"
               "value = sum(image[dy][dx]*k[dy][dx]\n"
               "            for dy in range(3) for dx in range(3))\n"
               "print(value)", "6")
        + related([("Image Tensor", "pixels.html#layout"),
                   ("Dot Product", "dot-product.html#dot-product"),
                   ("Convolution 전체 과정", "cnn.html#convolution")])
    )
    pooling = section(
        "pooling", "선택 실습: 2×2 Max / Average Pooling",
        """<p>Pooling은 특징을 작은 격자로 요약하는 <strong>선택 연산</strong>입니다. Conv 없이도 연산을 정의할 수 있고, 반대로 Pooling 없는 CNN도 가능합니다. 2×2 입력 [[1,2],[3,4]]에 Kernel 2×2, stride 2, padding 0을 사용하면 출력 shape는 <strong>1×1</strong>입니다. Max Pooling은 4, Average Pooling은 (1+2+3+4)/4=2.5를 반환합니다.</p>"""
        + equation("P4_POOL")
        + table(["모드", "연산", "출력 shape 및 값"], [
            ("Max", "max(1,2,3,4)", "[1,1] · 4"),
            ("Average", "(1+2+3+4)/4", "[1,1] · 2.5"),
        ])
        + '<p>Max는 큰 반응 하나를 남기고 Average는 평균 반응을 남깁니다. '
          '여기서는 채널별 독립 Pooling이고 학습 파라미터가 없습니다. '
          '추가 CNN 구성 블록이지 필수 선수 Edge는 아닙니다.</p>'
        + code("values = [[1, 2], [3, 4]]\n"
               "flat = [value for row in values for value in row]\n"
               "print(max(flat), sum(flat)/len(flat))", "4 2.5")
        + related([("Feature Map", "cnn.html#overview"), ("CNN 구성", "cnn.html#architectures")])
    )
    sections.insert(next(i for i, s in enumerate(sections) if s[0] == "convolution"), kernel)
    sections.insert(next(i for i, s in enumerate(sections) if s[0] == "architectures"), pooling)
