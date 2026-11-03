# Semantic Audit — 선수 개념 의미론 정정 (2026-11-02)

> 대상: [Draft PR #37](https://github.com/sh0427-han-private/vision_ai/pull/37). 작성자 자체 설계 감사로서 **독립 Reviewer PASS가 아닙니다(PENDING)**. 원본 HTML/JS/CSS 학습 페이지는 수정하지 않았습니다.

## 범위 및 정량 결과 (R2 현행 / 이전 이력 구분)

- **초기 의미론적 감사 단계 (Historical)**: 16 PART, 248 Concept, 390 prerequisite edge
- **R0 완료 Snapshot (Historical)**: 16 PART, 260 Concept, 411 prerequisite edge; coverage `existing-section` 42, `needs-expansion` 16, `planned` 202
- **R1 완료 Snapshot (Historical)**: 16 PART, 263 Concept, 394 prerequisite edge; coverage `existing-section` 42, `needs-expansion` 21, `planned` 200
- **R2 완료 Snapshot (Historical)**: 16 PART, 263 Concept, 390 prerequisite edge; coverage `existing-section` 42, `needs-expansion` 21, `planned` 200
- **P4/R0 구현 후 현재 정본**: 16 PART, 263 Concept, 390 prerequisite edge; coverage `existing-section` 53, `needs-expansion` 19, `planned` 191
- `existing-section`은 기존 절에 이미 대응, `needs-expansion`은 기존 절에 내용이 있으나 독립 학습 목표의 설명·예제 보강 필요, `planned`은 아직 확인된 기존 Anchor 없이 신규 작성 예정입니다. 이 중 어느 상태도 완성도 보증은 아닙니다.

## 주요 변경 결정

| 심각도 | 문제 | 수정 및 의도 |
|---|---|---|
| P0 | OOD 평가가 `an.threshold`를 통해 PatchCore 학습까지 요구 | `eval.ood`을 공통 Outlier/평가 개념으로 연결, `eval.robust` 분리. 특정 AD 알고리즘 의존 제거 |
| P0 | Grounding DINO가 CLIP을 필수로 요구 | `cv.detr` → `cv.dino_detr` → `cv.grounding` 연결. SSL의 `tr.dino`와 DINO-DETR을 명시적으로 구분 |
| P0 | 서로 다른 연산·방법 통합 | `m.chain`(Chain Rule), `ml.sigmoid`, `dl.repr`(Representation Learning), `an.reverse`(Reverse Distillation) 분리 |
| P0 | Transformer Encoder가 BatchNorm 필수 선수 | `dl.ln` 추가 후 `tr.encoder`가 LayerNorm을 참조하도록 수정 |
| P1 | `an.score`가 PatchCore만을 전제 | 일반 이상 점수·Heatmap으로 독립. Threshold도 특정 Calibration 모델 대신 검증 분할과 연결 |
| P1 | Kalman Filter가 HMM 필수 선수 | `res.state` State-space Models를 추가하고 HMM·Kalman을 분기 |
| P1 | 일반 Batch Inference가 Triton에 종속 | PyTorch 배치 추론을 일반 경로로 사용, ONNX/Triton은 선택 구현 |
| P1 | End-to-end Pipeline에 Kafka/S3/Triton 모두 필수 | 일반 프로젝트와 모니터링 개념으로 수정하고 서비스별 도구는 선택 적용 |
| P1 | STFPM과 EfficientAD의 잘못된 필수 체인 | Feature / Representation 기반으로 분기 |
| P1 | Self-supervised·Contrastive, Threshold·Domain Shift, OOD·Robustness 통합 | `tr.contrast`, `an.shift`, `eval.robust` 추가 |
| P1 | Learning Rate·Epoch·Batch가 단일 ID | `dl.lr` 및 `dl.epoch`로 분리 |
| P1 | 개념 수준을 PART별로 동일하게 일괄 분류 | 학습 난이도별로 Foundation/Basic/Intermediate/Advanced/Research 재분류 |
| P1 | PRML·CS231n에서 이미 일부 설명한 개념이 새 원고 계획으로만 표시 | 16개를 `needs-expansion`으로 분류하고 기존 Anchor 매핑 |
| P1 | 기존 원고 수정 시 Graph CI가 항상 실행되지 않음 | 원고 스크립트·생성 notes 변경을 트리거에 추가하고 페이지 재생성 후 Anchor 검사 |

## 참고 자료와 구분 원칙

- Caron et al., *Emerging Properties in Self-Supervised Vision Transformers*, ICCV 2021: https://openaccess.thecvf.com/content/ICCV2021/html/Caron_Emerging_Properties_in_Self-Supervised_Vision_Transformers_ICCV_2021_paper.html
- Zhang et al., *DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection*, ICLR 2023: https://arxiv.org/abs/2203.03605
- Liu et al., *Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection*, ECCV 2024: https://arxiv.org/abs/2303.05499

## 검증 및 남은 일

1. Graph 구조: 유일 ID, PART 멤버십, 직접 참조와 역참조의 대칭성, Kahn 위상 정렬을 재검사합니다. 단순 cycle-free는 의미론적 적합성 보장이 아닙니다.
2. `scripts/validate_concept_graph.py`에 지정된 필수·금지 선수 관계를 회귀 규칙으로 추가했습니다. 일반적 개념 타당성까지 전부 보증하지 않습니다.
3. 기존 실제 HTML Anchor와 원고 빌드는 CI에서 재확인하며, R0 당시 16개(현행 R2에서는 21개) `needs-expansion`의 설명 깊이는 독립 Reviewer가 재판단해야 합니다.
4. 독립 Reviewer는 별도 Agent/세션에서 최신 PR Diff와 기본 브랜치를 비교하고 PASS/REVISE/BLOCKED를 판정합니다. 병합·배포는 하지 않습니다.


## R1 Reviewer DEF-01~11 수정 기록 (2026-11-02)

<!-- graph-snapshot: parts=16 concepts=263 edges=390 existing-section=53 needs-expansion=19 planned=191 -->

R0: 260 Concept, 411 Edge → R1: **263 Concept, 394 Edge**. 상태: existing-section 42, needs-expansion 21, planned 200. 기존 260개 Stable ID 및 기존 URL/Anchor를 보존하고 `m.covariance`, `m.gaussian_multi`, `dl.autograd`을 추가했습니다(삭제 0).

### DEF-04/05/06 — 과도한 필수 Edge 변경 전·후

| Concept | R0 직접 선수 | R1 직접 선수 | 의미론/권장 관계 |
|---|---|---|---|
| `tr.dino` | `tr.ssl`, `tr.vit` | `tr.ssl` | SSL 원리는 ViT 이외의 backbone에도 성립; ViT는 구현 예제 |
| `cv.map` | `cv.nms`, `ml.split` | `cv.detect`, `cv.iou`, `eval.prf` | AP/mAP는 정렬된 score·정답·IoU로 계산; NMS는 후처리 |
| `eval.threshold` | `eval.prf`, `ml.calibration` | `eval.prf` | 임계값 분석은 Calibration 없이 정의 가능 |
| `ts.changepoint` | `ts.step`, `ts.cusum` | `ts.series` | 변화점은 CUSUM보다 넓은 문제 정의 |
| `an.shift` | `an.feature`, `ml.generalize` | `an.outlier`, `ml.generalize` | Domain Shift는 특정 Feature Extractor와 무관 |
| `res.em` | `res.gmm`, `res.bayes` | `m.likelihood`, `ml.optim` | EM은 일반 잠재변수 Likelihood 최적화; GMM은 응용 |
| `res.ood` | `eval.ood` | `an.outlier`, `ml.generalize` | OOD 문제 정의는 특정 Evaluation보다 선행 가능 |
| `res.distill` | `dl.transfer` | `dl.forward`, `ml.loss` | Knowledge Distillation은 Teacher/Student Loss 기반; Transfer는 응용 |
| `ops.registry` | `ops.onnx`, `data.version` | `data.version` | 모델 Registry는 ONNX 포맷에 독립 |
| `eng.independent` | `eng.agent`, `eng.test` | `eng.test` | 독립 검증은 Multi-Agent 없이도 가능 |

### DEF-01/02/03/07/08/09/10/11 — 보강 범위

- DEF-01/02: `img.pixel`의 Tensor 선수 제거, `cv.mask`의 Semantic Segmentation 선수 제거. P4 핵심 8개 + 보조 9개, 17개 Closure 제공 위치를 Roadmap에서 개별 지정. 신규 페이지/Section은 계획으로만 표시.
- DEF-03: `eval.ood`의 직접 선수에 `eval.auc`·`an.score`를 배치. ID/OOD Positive, 점수 방향, AUROC·AP(AUPR)·FPR@95TPR 수치 예제를 Learning Paths에서 제공.
- DEF-09 (R1 역사적 설계): Covariance/Multivariate Gaussian 독립 Concept을 PaDiM·GMM·Kalman·PCA에 연결. R1에는 Chain Rule → Autograd → Backprop 필수 경로가 있었으나 R2에서 수동 Backprop의 Autograd 의존을 제거했습니다.
- DEF-07: BatchNorm `dl.bn`과 LayerNorm `dl.ln`, SGD 업데이트 `dl.sgd`와 Epoch/Mini-batch `dl.epoch` 책임 분리. AP/mAP는 `cv.map`, 평가 프로토콜 `eval.iou`; MAE/MSE/RMSE 수식 `ml.mse`, 평가 응용 `eval.reg`로 정본 구분.
- DEF-08: `m.entropy` → `notes/prml.html#ch1` (Entropy/KL), `an.score` → `notes/patchcore.html#score` (Patch Score/Heatmap), `cnn.map` → `notes/cnn.html#overview` (Feature Map), `tr.multi` → `notes/vit.html#attention` (Multi-head), `dl.activation` → `notes/cnn.html#nonlinear` (ReLU) 기존 소개 확인, 모두 `needs-expansion`으로 변경. 기존 Anchor의 부족한 목표만 보강하고 페이지 복제 금지.
- DEF-11: R0의 전이 중복 26개 후보를 검토; 변경된 선수 재배치로 자연 소멸한 후보를 제외하고 나머지 20개를 직접 제거. R1 직접 선수 Edge에는 전이적 중복이 남지 않도록 정규화.
- DEF-10: Fragment 필수, Catalog 수준·상태, Curriculum PART·개수·제목, 문서 Snapshot, 핵심 의미론, Mutation 5종 이상을 CI와 Validator에서 검사하도록 설계.
- DINO `tr.dino`(Self-supervised), `cv.dino_detr`(DETR), `cv.grounding`(Grounding)은 독립 ID 유지. `an.reverse`는 일반 Knowledge Distillation `res.distill`과 연결하되 `an.ae`와 통합하지 않음.

본 기록은 Builder의 수정 근거이지 Independent Reviewer의 PASS가 아닙니다.

## R2 Reviewer 결함 정정 — 현재 상태 (2026-11-03)

- **R1-DEF-01 / HIGH**: `dl.backprop`: R1 `m.gradient`, `dl.autograd`, `ml.loss` → R2 `m.gradient`, `m.chain`, `dl.forward`, `ml.loss`. Backprop의 수동 미분 원리를 Autograd 구현보다 먼저 학습할 수 있습니다. `dl.autograd` 자체는 `dl.forward`, `m.chain`에 의존하며 계산 그래프 자동화의 **선택적 구현 경로**입니다. Optimizer Update는 별도 개념입니다.
- **R1-DEF-02 / HIGH**: `cnn.base`: R1 `cnn.pool`, `dl.activation` → R2 `cnn.map`, `dl.activation`. Pooling은 `cnn.map` 이후에 익힐 수 있는 선택 다운샘플링 블록으로 유지하되 CNN의 필수 선수는 아닙니다. P4 2×2 Pooling 실습은 Roadmap의 선택 실습으로 이동했습니다.

### R1-DEF-03 / MEDIUM — 일반 Concept 필수 Edge 변경 전·후

| Concept | R1 직접 필수 선수 | R2 직접 필수 선수 | 제거한 필수 의존과 관련·선택 관계 근거 |
|---|---|---|---|
| `data.temporal` | `data.group`, `video.frame` | `ml.split` | Temporal Split의 시간 순서 분할 정의에는 Group Split과 Video Frame이 불필요합니다. Group+Temporal 또는 Video 사례는 선택 응용입니다. |
| `ops.registry` | `data.version` | 없음 | Model Registry는 데이터셋 버전 관리 시스템 없이 모델 아티팩트와 버전을 등록할 수 있습니다. Dataset Versioning 연결은 추적성 사례입니다. |
| `ts.drift` | `ts.changepoint`, `ml.generalize` | `m.distribution` | Data/Concept Drift의 분포 변화 정의에는 Change-point 탐지나 ML 일반화가 필요하지 않습니다. CUSUM/Change-point는 탐지 방법, Generalization 영향은 응용 사례입니다. |
| `cv.iou` | `cv.mask`, `cv.box` | 없음 | IoU/Dice는 교집합·합집합의 비율로 먼저 정의하며, Bounding Box/Mask는 서로 다른 표현 응용입니다. 둘 다 공집합일 때 분모가 0이므로 정책을 정해야 하며 라이브러리마다 관례가 다를 수 있습니다. |

위 변경에서 **제거한 기존 필수 Edge는 총 9개**(`dl.backprop` 1, `cnn.base` 1, `data.temporal` 2, `ops.registry` 1, `ts.drift` 2, `cv.iou` 2), 신규 필수 Edge는 5개로 직접 Edge 수가 R1 394 → R2 390으로 순감 4개입니다. `next_topics` 역참조를 함께 정정했습니다. Graph 스키마와 Stable ID는 변경하지 않았습니다.

### R1-DEF-04 / MEDIUM — 수치 시점 정정

초기 감사 248/390, R0 260/411, R1 263/394는 변경 당시 기록으로 유지합니다. 현행 Graph는 **16 PART / 263 Concept / 390 직접 Edge**, coverage **42/21/200**으로 다시 계산했으며 모든 계획 문서 Snapshot Marker에 R2 현재 수치를 반영합니다. R1의 17개 P4 폐포는 R2의 **16개(핵심 8 + 필수 보조 8)**로 재계산되며 Pooling은 선택 실습으로 유지합니다.

### R1-DEF-05 / LOW — 회귀 테스트

R2에서 제거한 Autograd/Pooling 및 일반 개념의 필수 Edge를 되살리는 Mutation, 전이 중복 Edge Mutation을 추가하여 Validator의 실제 오류 메시지를 검증하도록 보강했습니다. 기존 테스트와 함께 CI에서 실행합니다.

본 R2 기록은 당시 Builder의 설계·구현 근거이며, P4/R0의 독립 Reviewer PASS를 의미하지 않습니다.

## P4/R0 실제 구현 커버리지 (2026-11-03)

7개 신규 Scalar/Vector/Matrix/Tensor/Shape/Dot Product/Function 페이지와 CNN의 Kernel·Pooling Section이 생성되므로 `planned` 9개를 `existing-section`으로 매핑합니다. 기존 `cnn.map`과 `dl.activation`은 정량 예시·학습 연결을 추가하여 `needs-expansion`에서 `existing-section`으로 변경합니다. 기존 63개 URL Mapping은 정확히 유지하고 9개 신규 매핑을 추가해 72개로 확장합니다. P4 대상 중 미작성인 Concept는 없습니다. 기존 R2 필수 선수 Graph 390 Edge는 그대로이며 Pooling은 선택 학습입니다. 본 상태는 콘텐츠 구현·정적 검증 범위이며 최종 Reviewer PASS가 아닙니다.
