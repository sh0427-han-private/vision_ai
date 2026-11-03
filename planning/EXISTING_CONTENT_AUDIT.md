# Existing Content Audit — 실제 `vision_ai` 기준

> 읽기 전용 조사 기준: [main@e2b2c2f](https://github.com/sh0427-han-private/vision_ai/tree/e2b2c2f377c1c97c3b6d010cb34c63988d0fca05), 2026-11-02. 이 문서는 기존 코드 변경이 아닌 **현황 조사**입니다.

## 사이트와 생성 구조

- `scripts/build.py`가 `NOTES`를 누적하고 `note(slug,title,subtitle,group,label,minutes,sections,sources)`와 `section(anchor,title,body)`로 원고를 정의합니다. `scripts/reference_notes.py`는 CS231n·PRML 등록을 연결합니다.
- 주요 원고는 `build.py`, `cs231n_note.py`, `prml_note.py`. 추가 Figure 생성은 `extra_diagrams.py`, `paper_figures.py`, `reference_figures.py`입니다. 원본 에셋은 `assets/diagrams/illustrations/` 등에도 존재합니다.
- 산출 경로는 `index.html`과 `notes/<slug>.html`; 원고의 `section.anchor`가 기존 Deep Link를 구성합니다. `resnet.html` → `cnn.html#resnet_problem`, `unet.html` → `tasks.html#unet_architecture`는 리다이렉트용 호환 문서로 보존합니다.
- `scripts/validate.py`는 HTML별 h1·ID·링크·fragment, 필수 Anchor·term-inline·수식 fallback, reference/paper SVG XML·viewBox 등 회귀 조건을 점검합니다.
- `.github/workflows/pages.yml`은 PR에서 build·validate·JS 문법을 검사하고, `main` push에서만 Pages artifact를 만들어 배포합니다. `_site`는 `.gitignore` 제외; **현재 브랜치에 새 사이트 HTML은 아직 없습니다**.

## 실제 원고 섹션 전수 인벤토리

기존 문서 **8개**: 주제별 6개 + CS231n + PRML. 소스의 `section(...)` 선언으로 확인된 **70개** 섹션(주제별 42개, CS231n 12개, PRML 16개). 기존 설계 설명에 없는 별도 학습 파일은 만들지 않으며, 모든 항목을 기존 Anchor로 재사용합니다.

### [`notes/pixels.html`](../notes/pixels.html) · 7개 절

- [`#overview`](../notes/pixels.html#overview): 이미지 파일과 픽셀 배열은 같은 것이 아니다
- [`#pixels`](../notes/pixels.html#pixels): 한 픽셀에는 무엇이 들어 있을까?
- [`#layout`](../notes/pixels.html#layout): HWC, CHW, NCHW는 무엇이 다른가?
- [`#resize`](../notes/pixels.html#resize): Resize는 단순히 픽셀 수만 줄이지 않는다
- [`#illumination`](../notes/pixels.html#illumination): 같은 대상이어도 픽셀 값은 달라진다
- [`#normalization`](../notes/pixels.html#normalization): dtype, scaling, normalization을 따로 확인하기
- [`#check`](../notes/pixels.html#check): 스스로 설명해 보기

### [`notes/cnn.html`](../notes/cnn.html) · 11개 절

- [`#overview`](../notes/cnn.html#overview): 왜 작은 커널을 반복해서 사용할까?
- [`#convolution`](../notes/cnn.html#convolution): 3 × 3 합성곱을 손으로 계산하기
- [`#channels`](../notes/cnn.html#channels): 채널은 어떻게 섞일까?
- [`#shape`](../notes/cnn.html#shape): Stride · Padding · Receptive field
- [`#nonlinear`](../notes/cnn.html#nonlinear): 왜 비선형 함수와 학습이 필요할까?
- [`#architectures`](../notes/cnn.html#architectures): CNN 아키텍처는 무엇이 바뀌어 왔을까?
- [`#resnet_problem`](../notes/cnn.html#resnet_problem): ResNet 논문: 깊게 쌓았는데 training error가 커지는 문제
- [`#residual_block`](../notes/cnn.html#residual_block): Residual block: F(x)와 identity shortcut
- [`#residual_shape`](../notes/cnn.html#residual_shape): Shape가 다르면 projection shortcut이 필요하다
- [`#resnet_bottleneck`](../notes/cnn.html#resnet_bottleneck): Bottleneck block: 1×1 Conv의 또 다른 역할
- [`#resnet_scope`](../notes/cnn.html#resnet_scope): ResNet 논문에서 실제로 확인한 범위

### [`notes/vit.html`](../notes/vit.html) · 6개 절

- [`#problem`](../notes/vit.html#problem): 논문이 던진 질문
- [`#patches`](../notes/vit.html#patches): Patch → Flatten → Linear projection
- [`#tokens`](../notes/vit.html#tokens): CLS와 위치 임베딩은 왜 더할까?
- [`#attention`](../notes/vit.html#attention): Q · K · V: 무엇을 비교하고 무엇을 가져올까?
- [`#encoder`](../notes/vit.html#encoder): Encoder 블록 내부의 두 번의 업데이트
- [`#limits`](../notes/vit.html#limits): CNN과 비교할 때 살펴볼 점

### [`notes/tasks.html`](../notes/tasks.html) · 8개 절

- [`#overview`](../notes/tasks.html#overview): 모델을 고르기 전에 출력부터 정하기
- [`#visual`](../notes/tasks.html#visual): 같은 장면에서 결과를 비교하기
- [`#pipeline`](../notes/tasks.html#pipeline): Backbone · Neck · Head
- [`#iou`](../notes/tasks.html#iou): 겹친 정도를 수치로 표현하기
- [`#segmentation_context`](../notes/tasks.html#segmentation_context): Segmentation에서는 왜 encoder–decoder가 필요한가?
- [`#unet_architecture`](../notes/tasks.html#unet_architecture): U-Net 논문: context와 localization을 함께 연결하기
- [`#unet_original`](../notes/tasks.html#unet_original): 원 U-Net과 현대 same-padding 구현을 구분하기
- [`#unet_scope`](../notes/tasks.html#unet_scope): U-Net 논문의 문제 설정과 한계

### [`notes/training.html`](../notes/training.html) · 5개 절

- [`#loop`](../notes/training.html#loop): 학습에서 실제로 바뀌는 것은 무엇일까?
- [`#split`](../notes/training.html#split): 비율보다 먼저 독립성을 지키기
- [`#cv`](../notes/training.html#cv): 3-fold CV는 전체 데이터를 세 번 나눠 평가하기
- [`#metrics`](../notes/training.html#metrics): Threshold를 바꾸면 어떤 오류가 달라질까?
- [`#report`](../notes/training.html#report): 실험 기록에 남길 최소 정보

### [`notes/patchcore.html`](../notes/patchcore.html) · 5개 절

- [`#problem`](../notes/patchcore.html#problem): 불량 종류를 모두 모으기 어려울 때
- [`#pipeline`](../notes/patchcore.html#pipeline): 정상 데이터 준비와 검사 과정을 분리하기
- [`#memory`](../notes/patchcore.html#memory): 모든 정상 특징을 저장하면 얼마나 커질까?
- [`#score`](../notes/patchcore.html#score): 최근접 거리가 이상 점수가 되는 이유
- [`#limits`](../notes/patchcore.html#limits): 정상과 다르다고 반드시 불량은 아니다

### [`notes/cs231n.html`](../notes/cs231n.html) · 12개 절

- [`#map`](../notes/cs231n.html#map): CS231n을 하나의 데이터 흐름으로 보기
- [`#classification`](../notes/cs231n.html#classification): 1. Image Classification: 데이터가 곧 경험이다
- [`#linear`](../notes/cs231n.html#linear): 2. Linear Classifier: 점수와 loss를 분리해서 보기
- [`#optimization`](../notes/cs231n.html#optimization): 3. Optimization과 Backpropagation: W를 어떻게 바꿀까?
- [`#nn`](../notes/cs231n.html#nn): 4. Neural Network: 선형 변환 사이에 비선형성을 넣는 이유
- [`#training`](../notes/cs231n.html#training): 5. Learning & Evaluation: 학습이 되는지 먼저 진단하기
- [`#cnn`](../notes/cs231n.html#cnn): 6. Convolutional Network: 공간 구조를 보존한 채 특징을 계산하기
- [`#architectures`](../notes/cs231n.html#architectures): 7. CNN Architecture: 블록 이름보다 계산과 정보 흐름을 보기
- [`#visualization`](../notes/cs231n.html#visualization): 8. Understanding CNN: 모델이 무엇을 봤는지 확인하는 도구
- [`#transfer`](../notes/cs231n.html#transfer): 9. Transfer Learning: 처음부터 학습할지, 어디까지 풀지
- [`#modern`](../notes/cs231n.html#modern): 10. 2026 확장: Transformer · SSL · Diffusion · CLIP · DINO
- [`#study-path`](../notes/cs231n.html#study-path): 11. 이 사이트에서 어떤 순서로 다시 보면 좋을까?

### [`notes/prml.html`](../notes/prml.html) · 16개 절

- [`#map`](../notes/prml.html#map): PRML을 14개의 독립 알고리즘이 아니라 하나의 확률적 언어로 보기
- [`#ch1`](../notes/prml.html#ch1): 1장. Introduction: 확률, 결정, 정보량을 한 프레임에 넣기
- [`#ch2`](../notes/prml.html#ch2): 2장. Probability Distributions: 데이터 타입에 맞는 분포 선택
- [`#ch3`](../notes/prml.html#ch3): 3장. Linear Models for Regression: basis와 Bayesian regression
- [`#ch4`](../notes/prml.html#ch4): 4장. Linear Models for Classification: 경계와 확률을 구분
- [`#ch5`](../notes/prml.html#ch5): 5장. Neural Networks: 비선형 basis를 데이터로 학습하기
- [`#ch6`](../notes/prml.html#ch6): 6장. Kernel Methods: 명시적 고차원 변환 없이 유사도 계산
- [`#ch7`](../notes/prml.html#ch7): 7장. Sparse Kernel Machines: 결정에 필요한 일부 샘플에 집중
- [`#ch8`](../notes/prml.html#ch8): 8장. Graphical Models: 복잡한 확률분포의 구조를 그림으로 표현
- [`#ch9`](../notes/prml.html#ch9): 9장. Mixture Models and EM: 보이지 않는 군집 변수를 추론
- [`#ch10`](../notes/prml.html#ch10): 10장. Approximate Inference: 정확한 posterior가 너무 어려울 때
- [`#ch11`](../notes/prml.html#ch11): 11장. Sampling Methods: 적분 대신 샘플로 기대값 계산
- [`#ch12`](../notes/prml.html#ch12): 12장. Continuous Latent Variables: 고차원 데이터를 낮은 좌표로 설명
- [`#ch13`](../notes/prml.html#ch13): 13장. Sequential Data: 시간 순서를 확률 모델에 넣기
- [`#ch14`](../notes/prml.html#ch14): 14장. Combining Models: 여러 예측을 어떻게 결합할까?
- [`#vision-bridge`](../notes/prml.html#vision-bridge): PRML 개념을 Vision AI 개발에 다시 연결하기

## 기존 구현 중 활용 가능한 것

| 기존 내용 | 유지·재사용 목적 | 새 교육과정 연결 |
|---|---|---|
| `pixels` + 사과 R/G/B WebP | 실제 픽셀·채널, resize·illumination·normalization, 밝기 실습 | PART 00/03, Scalar–Tensor 경로 |
| `cnn` + Conv slider + ResNet | 커널 이동·채널 합산·shape·residual / 원 논문 구분 | PART 02/04 |
| `vit` + patch size slider | Patch·CLS·QKV·Transformer Encoder | PART 06 |
| `tasks` + U-Net | Classification/Detection/Segmentation, IoU/Dice, encoder–decoder | PART 05/12 |
| `training` + threshold slider | Split·CV·누수·Precision/Recall/F1 | PART 01/11/12 |
| `patchcore` + memory 설명 | 정상 특징·Memory Bank·최근접 거리·Score | PART 07 |
| `cs231n` | 분류→Loss→Optimization→Backprop→CNN의 학습 순서와 심화 | PART 01–06 교차 링크 |
| `prml` | 확률·회귀/분류·잠재변수·GMM/EM·VI/MCMC·HMM | PART 00/01/09/10/15 교차 링크 |
| Figure 생성기·참고 Atlas | 계산 기반 정확한 SVG 구조 유지 | 각 개념 설명에서 필요한 도식만 재사용 |

## 부족하거나 독립 설명이 필요한 영역

- **핵심 기초의 깊이**: Scalar→Vector→Matrix→Tensor / 미분→Chain Rule→Backprop은 기존 종합 원고에 등장하지만 단계별 수치·Python 설명이 충분한지 심층 검증되지 않았습니다.
- **도메인 확장 미작성**: 타임시리즈 CUSUM/EWMA, 영상 RNN/GRU, 기하학 Ellipse/RANSAC, 모델 배포 ONNX/Triton, Python 엔지니어링 문서는 현재 독립 페이지가 확인되지 않았습니다.
- **연결 정보 미구현**: 개념별 선수/후속 네비게이션, DAG 기반 Learning Paths, 구현/검증 상태 표시가 없습니다.
- **기존 자료의 중복/표면적 언급**: CS231n·PRML에 여러 분야 개념이 재등장합니다. 본문 전체의 의미론적 중복 여부는 별도 교육 Reviewer의 확인 대상입니다.
- **출처 범위**: 각 페이지의 원 논문/공식 링크를 유지하며, API·모델 버전은 향후 페이지 작성 시 재확인합니다.

## 반도체 메뉴·옛 주소 조사와 변경 방향

- `scripts/build.py`의 `TOPIC_LABELS`, `nav`, `render` 홈/탭/외부 카드와 `assets/site.js`의 `topic_copy.semiconductor`·`data-topic-*` 전환 로직에 반도체 항목이 있습니다. 생성된 `index.html`에도 외부 Memory Book·Process Book 링크가 노출됩니다.
- `PROJECT_CONTEXT.md` 마지막 '분야별 탐색'은 이전의 반도체/AI/Vision 탭 계약이며 이번 교육 범위와 불일치합니다. 제거가 아니라 **현재 설계와 역사 문맥을 구분해 갱신**해야 합니다.
- `README.md`, `PROJECT_CONTEXT.md`, `TODO.md`, `scripts/build.py`의 GitHub 링크, 생성 HTML footer/sidebar는 과거 계정 주소를 사용합니다. PR #36(주소 정정)가 현재 열려 있으므로 **충돌·중복 수정을 피하고 해당 PR 결과를 재조회**해야 합니다. 실제 Pages URL은 미확인 상태라 새 주소를 추정 배포 주소로 단정하지 않습니다.
- 현 `?topic=semiconductor` 북마크는 삭제하지 않고 `overview`로 안전하게 fallback 하되 기존 문서 주소 자체는 유지하고, 외부 링크는 필요하다면 역사/아카이브 문서에서만 보존합니다. 새 AI 홈·네비게이션에서는 제외합니다.

## 변경 불가 기준

기존 `notes/*.html` URL·Anchor(특히 두 legacy redirect), 소스 등록 순서의 의미, 수식·figure의 실측/합성 구분, 기존 4개 JS 실습, Pages 배포 방식은 초기 설계·Vertical Slice 동안 보존합니다. 전면 재작성·대규모 프레임워크 전환·산업 비공개 데이터 복사는 제외합니다.

## 의미론적 감사 이후: 기존 소개와 신규 작성의 구분 (R1)

<!-- graph-snapshot: parts=16 concepts=263 edges=390 existing-section=53 needs-expansion=19 planned=191 -->

기존 8개 원고·70개 Section 및 R0의 기존 58개 Concept 매핑을 보존하면서 5개 기존 설명을 `needs-expansion`으로 재분류합니다. 아래 URL은 실제 기존 Anchor에 대응하나 독립 본문 완성을 뜻하지 않습니다.

| Concept | 기존 소개 위치 | 보강 학습 목표 |
|---|---|---|
| `m.prob` | [notes/prml.html#ch1](../notes/prml.html#ch1) | 기존 개요와 독립 단원 차이를 예제·수식으로 보강 |
| `m.bayes` | [notes/prml.html#ch1](../notes/prml.html#ch1) | 기존 개요와 독립 단원 차이를 예제·수식으로 보강 |
| `m.distribution` | [notes/prml.html#ch2](../notes/prml.html#ch2) | 기존 개요와 독립 단원 차이를 예제·수식으로 보강 |
| `m.likelihood` | [notes/prml.html#ch1](../notes/prml.html#ch1) | 기존 개요와 독립 단원 차이를 예제·수식으로 보강 |
| `m.entropy` | [notes/prml.html#ch1](../notes/prml.html#ch1) | Entropy/KL 실제 계산과 조건 |
| `ml.linear` | [notes/prml.html#ch3](../notes/prml.html#ch3) | 기존 개요와 독립 단원 차이를 예제·수식으로 보강 |
| `ml.logistic` | [notes/prml.html#ch4](../notes/prml.html#ch4) | 기존 개요와 독립 단원 차이를 예제·수식으로 보강 |
| `ml.softmax` | [notes/prml.html#ch4](../notes/prml.html#ch4) | 기존 개요와 독립 단원 차이를 예제·수식으로 보강 |
| `ml.sigmoid` | [notes/prml.html#ch4](../notes/prml.html#ch4) | 기존 개요와 독립 단원 차이를 예제·수식으로 보강 |
| `ml.knn` | [notes/cs231n.html#classification](../notes/cs231n.html#classification) | 기존 개요와 독립 단원 차이를 예제·수식으로 보강 |
| `dl.mlp` | [notes/cs231n.html#nn](../notes/cs231n.html#nn) | 기존 개요와 독립 단원 차이를 예제·수식으로 보강 |
| `dl.transfer` | [notes/cs231n.html#transfer](../notes/cs231n.html#transfer) | 기존 개요와 독립 단원 차이를 예제·수식으로 보강 |
| `dl.repr` | [notes/cs231n.html#transfer](../notes/cs231n.html#transfer) | 기존 개요와 독립 단원 차이를 예제·수식으로 보강 |
| `tr.multi` | [notes/vit.html#attention](../notes/vit.html#attention) | Head 분할·합산 및 projection |
| `tr.ssl` | [notes/cs231n.html#modern](../notes/cs231n.html#modern) | 기존 개요와 독립 단원 차이를 예제·수식으로 보강 |
| `tr.dino` | [notes/cs231n.html#modern](../notes/cs231n.html#modern) | 기존 개요와 독립 단원 차이를 예제·수식으로 보강 |
| `tr.clip` | [notes/cs231n.html#modern](../notes/cs231n.html#modern) | 기존 개요와 독립 단원 차이를 예제·수식으로 보강 |
| `an.score` | [notes/patchcore.html#score](../notes/patchcore.html#score) | PatchCore 이외의 score 정의 및 heatmap/threshold 분리 |
| `geo.svd` | [notes/prml.html#ch12](../notes/prml.html#ch12) | 기존 개요와 독립 단원 차이를 예제·수식으로 보강 |

R1 당시 총 existing-section 42, needs-expansion 21이었으며, P4 이후 현재는 existing-section 53, needs-expansion 19입니다. R2 기존 63개 Mapping과 기존 70개 Anchor/Redirect, JS 실습 4개는 유지합니다.

## P4/R0 신규 학습 및 기존 소개 확장 (2026-11-03)

기존 8개 원고의 70개 Section은 원본 Anchor를 모두 보존합니다. `notes/cnn.html#kernel`과 `notes/cnn.html#pooling` 두 Section이 추가되어 빌드 후 총 72개 Section입니다. 신규 독립 페이지는 Scalar, Vector, Matrix, Tensor, Shape, Dot Product, Function이며 각각 독립적인 첫 학습 Anchor를 가집니다. 기존 `dl.activation`과 `cnn.map`의 P4 수치 학습 목표를 보강해 기존 Section 매핑으로 분류했습니다. 다른 19개 `needs-expansion` 항목은 계획 상태를 보존합니다.
