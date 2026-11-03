# Concept Dependencies — 선수 관계와 DAG

정본: [concepts.v1.json](concepts.v1.json). `prerequisites`는 직접 **필수** 선행 개념, `next_topics`는 정확한 역방향 연결입니다. 관련 개념·권장 탐색 경로는 필수 의존성과 구분합니다. PART 번호와 위상 정렬은 다릅니다.

## 설계 원칙

1. 선수 관계는 정의·계산·모델 기법의 이해에 실제로 필요한 개념만 연결합니다. 특정 라이브러리, 논문, 적용 사례가 일반 개념의 필수 선수가 되어서는 안 됩니다.
2. 전이 관계를 복제하지 않습니다. `an.score`처럼 여러 이상탐지 방법에 공통되는 개념을 PatchCore 같은 단일 알고리즘에 종속시키지 않습니다.
3. 동명이의어를 명확히 분리합니다. `tr.dino`는 Caron et al.의 Self-supervised DINO이고, `cv.dino_detr`는 Object Detection의 DINO-DETR이며, `cv.grounding`은 이를 기반으로 한 언어 조건부 탐지입니다.
4. 필수 의존성이 아닌 예제 구현 환경(예: Triton을 이용한 Batch Inference, Kafka·S3 기반 End-to-end Pipeline)은 응용 예제로 제시합니다.
5. 기존 URL/Anchor는 유지하고 `needs-expansion`은 기존 소개가 있지만 상세 학습 목표를 완성하지 않았다는 의미로 기록합니다.

## 핵심 학습 경로 및 반례

### Scalar → CNN

`m.scalar` → `m.vector` → `m.matrix` → `m.tensor`은 수학 경로이고, `img.pixel` → `img.rgb`는 Tensor가 필요 없는 기초 경로입니다. `img.tensor`에서 `m.shape`·RGB가 합류해 `cnn.kernel` → `cnn.conv` → `cnn.stride` → `cnn.map`과 Activation(`dl.activation`)이 `cnn.base`에서 합류합니다. `cnn.pool`은 Feature Map 이후 학습하는 **선택적 다운샘플링 블록**이며 CNN 자체의 필수 선수는 아닙니다.

Convolution의 Dot Product와 CNN의 Activation은 필수 선수이며, Pooling은 선택적 응용입니다. HWC/NCHW 축 순서·출력 Shape는 별도 수치 검산합니다.

### Calculus → Training

`m.function` → `m.derivative`에서 `m.gradient`와 `m.chain`으로 분기합니다. 수동 Backpropagation(`dl.backprop`)은 `m.gradient` + `m.chain` + `dl.forward` + `ml.loss`에서 직접 시작합니다. `dl.forward` + `m.chain` → `dl.autograd`는 동일한 미분 계산을 계산 그래프에서 자동화하는 **별도 구현 학습 경로**입니다.  `dl.gd` → `dl.sgd` → `dl.adam`은 갱신 알고리즘입니다. 개념적 Gradient Descent의 이해에 Backpropagation이 반드시 선행할 필요는 없습니다.

### Normal Features → PatchCore

`an.outlier` → `an.one` → `an.feature` → `an.embedding` → `an.memory` → `an.coreset` → `an.patchcore`. `an.nearest`도 PatchCore에 합류합니다. 반면 `an.score` → `an.threshold`는 **알고리즘 공통**의 이상 점수 및 운영 기준이며 PatchCore·Memory Bank가 필수 선행이 아닙니다.

### Open-Vocabulary Grounding

`cv.detect` + `tr.encoder` → `cv.detr` → `cv.dino_detr` → `cv.grounding`. Token/Language 관련 개념은 `tr.token`으로 연결합니다. `tr.clip`은 별도 Contrastive Vision–Language Model이지 Grounding DINO의 필수 선행 기술은 아닙니다. `tr.dino`(Self-supervised DINO)와 혼동하지 않습니다.

### Probabilistic Sequential Models

`m.distribution` + `m.matrix` + `ts.series` → `res.state`. 여기서 HMM(`res.hmm`)과 Kalman Filter(`res.kalman`)가 분기합니다. HMM은 Kalman Filter의 필수 선행이 아닙니다.

### Serving과 평가

Batch Inference(`ops.batch`)는 `ops.pytorch`를 통해 일반적 배치 축·벡터화 개념을 다룹니다. `ops.triton`은 그중 하나의 배포 환경입니다. `eval.ood`은 `eval.auc`(점수 기반 ROC/PR) 및 `an.score`에서 진입하며 특정 이상탐지 모델이나 Threshold Calibration을 강제하지 않습니다. `eval.robust`는 별도 견고성 평가 개념입니다.

### Geometry·Time-series

`geo.circle` + `geo.ls` + `geo.mad` → `geo.fit`; `geo.fit` + `geo.subpixel` + `cv.semantic` → `geo.boundary`. 타원 가정이 맞지 않는 객체에 적용하지 않습니다.

`ts.series` → `ts.moving` → `ts.threshold` → `ts.step` → `ts.baseline`. `ts.z`는 일반 통계 기반이며 Geometry의 MAD 단원에 종속되지 않습니다.

## Graph 계약

| 속성 | 조건 |
|---|---|
| id / part | 유일한 Stable ID, PART에서 한 번 등록 |
| level | Foundation / Basic / Intermediate / Advanced / Research; PART별 획일 지정 금지 |
| prerequisites / next_topics | 존재성·중복·역방향 대칭·비순환 DAG |
| status | `existing-section` 기존 절 매핑, `needs-expansion` 기존 소개·보강, `planned` 신규 계획 |
| legacy_url | 기존 매핑 두 상태에는 URL/Anchor 필수; planned에는 없음 |

현재 R2 정본은 16 PART / 263 concepts / 390 direct edges입니다. 검사기는 구조와 알려진 의미론적 회귀 규칙을 검사하지만 **교육과정 전체의 교육학적 타당성을 자동 보장하지 않습니다.** 독립 Reviewer는 별도 세션/Agent에서 검토해야 합니다.

## 참고 원 논문

- Caron et al. (ICCV 2021), *Emerging Properties in Self-Supervised Vision Transformers*: https://openaccess.thecvf.com/content/ICCV2021/html/Caron_Emerging_Properties_in_Self-Supervised_Vision_Transformers_ICCV_2021_paper.html
- Zhang et al. (ICLR 2023), *DINO: DETR with Improved DeNoising Anchor Boxes*: https://arxiv.org/abs/2203.03605
- Liu et al. (ECCV 2024), *Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection*: https://arxiv.org/abs/2303.05499

상세 수정 의사결정: [SEMANTIC_AUDIT.md](SEMANTIC_AUDIT.md).


## R1 선수 의미론·정본 개념

<!-- graph-snapshot: parts=16 concepts=263 edges=390 existing-section=42 needs-expansion=21 planned=200 -->

- Pixel 기초(`img.pixel`)는 Tensor에, Polygon/Mask(`cv.mask`)는 Semantic Segmentation에 필수로 의존하지 않습니다.
- `m.covariance` → `m.gaussian_multi`는 PaDiM/GMM/Kalman의 확률 선행입니다. PCA/SVD(`geo.svd`)는 중심화·Covariance와 연관하되 SVD 자체가 Covariance 역행렬을 계산한다는 뜻은 아닙니다.
- R1에서는 Chain Rule → Computation Graph/Autograd(`dl.autograd`) → Backpropagation으로 기재했지만, R2는 이를 정정했습니다. 수동 Backprop에는 Gradient·Chain Rule·Forward·Loss가 직접 필요하며 Autograd는 선택적 계산 그래프 자동화 구현입니다.
- OOD 예제는 y=1:OOD, score 높음:OOD를 기본으로 설정합니다. AUROC/AP(AUPR 계단 적분)는 threshold-free 요약, FPR@95TPR은 TPR≥0.95의 임계점 기반 값입니다.
- `cv.map`에서 AP/mAP 정의·정렬·적분; `eval.iou`에서 IoU 임계값/평가 프로토콜. `ml.mse`에서 MAE/MSE/RMSE 수식; `eval.reg`에서 오차 평가. BatchNorm `dl.bn`과 LayerNorm `dl.ln`, Epoch/Mini-batch `dl.epoch`와 SGD 업데이트 `dl.sgd`를 분리합니다.
- ViT→SSL-DINO, NMS→AP/mAP, Calibration→Threshold, CUSUM→Change-point, GMM→EM, 평가→OOD Detection, Transfer→Distillation, ONNX→Model Registry, Agent→Independent Validation은 필수 정의가 아닌 권장·선택 학습 경로입니다.
- R0에서 전이 중복 26개 직접 Edge 후보를 검토하고 변경 후 남은 중복을 제거했습니다. 필수/권장 분리는 [Semantic Audit](SEMANTIC_AUDIT.md)에 기록합니다.

## R2 필수/선택 관계 정정 (2026-11-03)

- `cnn.base`의 필수 선수는 `cnn.map`과 `dl.activation`입니다. Pooling(`cnn.pool`)은 Feature Map에 적용할 수 있는 **선택 구성 요소**입니다.
- Temporal Split(`data.temporal`)은 `ml.split`로, Drift(`ts.drift`)는 `m.distribution`으로 진입합니다. Group/Video 분할 및 Change-point/CUSUM은 선택 응용입니다.
- Model Registry(`ops.registry`)는 특정 Dataset Versioning 시스템을 필수로 요구하지 않습니다. 아티팩트/모델 버전과 데이터 버전의 연계는 추적성 사례입니다.
- IoU/Dice(`cv.iou`)는 일반 집합/영역 교집합÷합집합을 먼저 정의합니다. Box/Mask 표현은 독립 응용 사례이며, 합집합이 0인 경우는 사전 정의한 정책과 라이브러리 관례를 구분합니다.
