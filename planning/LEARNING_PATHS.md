# Learning Paths — 여러 분야로 분기하는 학습 경로

현재는 **설계 단계**이며 planned 개념을 실제 완성된 페이지처럼 표시하지 않습니다. 개념별 직접 선수는 [Dependency Graph](CONCEPT_DEPENDENCIES.md)에 기록합니다.

## 1. AI/ML Foundations

Scalar → Vector → Matrix → Tensor와 Function → Derivative에서 Gradient·Chain Rule로 분기합니다. Gradient + Objective → Gradient Descent는 파라미터 업데이트 원리입니다. Gradient + Chain Rule + Forward + Loss → 수동 Backpropagation을 먼저 계산할 수 있습니다. Forward + Chain Rule → Computation Graph/Autograd는 Backprop 미분 계산을 자동화하는 별도 선택 경로입니다. Probability → Bayes Rule → Likelihood → Classification/Loss도 병행합니다.

기존 시작: [CS231n 최적화](../notes/cs231n.html#optimization), [PRML 확률](../notes/prml.html#ch1), [학습/평가](../notes/training.html#loop). 별도의 기초 수학 페이지는 아직 작성되지 않았습니다.

## 2. Computer Vision

Pixel → RGB는 Tensor를 전제로 하지 않는 시작 경로입니다. Scalar/Vector/Matrix/Tensor/Shape + Dot Product는 Image Tensor에서 합류하는 수학 경로이며, Kernel → Convolution → Stride → Feature Map + Activation → CNN → Classification/Detection/Segmentation으로 이어집니다. Feature Map → Pooling은 CNN에서 사용할 수 있는 선택적 연산이며 2×2 Pooling 수치 계산은 별도 실습으로 남깁니다. Polygon/Mask는 Pixel 기반의 데이터 형식으로 모델보다 먼저 학습할 수 있습니다. 형상/채널 예시는 실제 계산과 일치해야 합니다.

기존 활용: [이미지](../notes/pixels.html), [CNN](../notes/cnn.html#convolution), [Vision Tasks](../notes/tasks.html).

## 3. Anomaly Detection

Outlier/Novelty → One-class → Feature Extraction → Embedding → Memory Bank → Coreset + Nearest Neighbor → PatchCore를 학습합니다. Anomaly Score/Threshold는 PatchCore에 종속되지 않는 공통 개념으로 별도 학습합니다. 합성 정상 특징과 검사 점으로 NN 거리를 검산합니다.

기존 활용: [Anomaly Detection·PatchCore](../notes/patchcore.html).

## 4. Video Understanding

Frame/FPS → Sampling/Window → Video Classification → RNN/GRU 또는 Temporal Transformer 또는 3D CNN → Temporal Aggregation → Persistence/Event Detection. frame-level과 event-level을 구분합니다.

미작성: 독립 Video AI 학습 페이지. 기존 이미지/CNN/Transformer 기초를 재사용합니다.

## 5. Geometry & Boundary

Coordinate → Affine/Homography, Circle/Ellipse → Least Squares/MAD/RANSAC → Robust Ellipse Fitting → Subpixel Edge → Boundary Refinement. 타원이 아닌 객체나 부분 가림에 대한 한계를 명시합니다.

실습: 합성 점·이상점으로 피팅 전후를 비교합니다. 실제 내부 원본 데이터는 사용하지 않습니다.

## 6. Time-series Anomaly

Moving Median → Z-score/Robust Threshold → Step Change → Baseline Update/Freeze → CUSUM/EWMA 또는 Change-point Detection은 시계열 탐지 방법의 예시입니다. Data/Concept Drift는 일반 확률분포 비교에서 독립적으로 정의하고, Change-point/CUSUM은 선택 탐지 방식으로 연결합니다. 경보 지연과 false alarm을 함께 다룹니다.

실습: 합성 시간별 시계열의 직전 5개 중앙값, 연속 두 번 초과, 베이스라인 홀드를 각각 계산합니다.

## 7. AI Engineering / MLOps

Project Structure → Tests → PyTorch → Batch Inference/Latency를 먼저 다루고, 선택적으로 ONNX → ONNX Runtime 또는 Triton Serving을 학습합니다. Model Registry는 모델 아티팩트와 버전을 독립적으로 관리하며 Dataset Versioning 연계는 추적성 예시입니다. Temporal Split은 일반 Train/Validation/Test Split에서 학습하며 Group Split과 Video Frame 기반 분할은 선택 응용입니다. 모델·데이터·모니터링을 결합해 Pipeline을 설계하되 Kafka/S3/Triton은 필수 선수 아닌 적용 예시입니다. 영상 데이터 경로는 RTSP/FFmpeg와 Timestamp/NTP를 함께 살핍니다.

실습: shape·dtype·채널 순서 계약, 단일 vs 배치 추론, 배포 회귀를 검증합니다.

## 8. Advanced Research

확률 기초 → PRML Bayesian → Graphical Models/GMM → EM/VI/MCMC 또는 State-space → HMM/Kalman으로 분기합니다. CNN/Transformer → Self-supervised Learning → DINO(자기지도) 또는 Contrastive Learning → CLIP을 학습할 수 있습니다. 객체 탐지 경로의 DETR → DINO-DETR → Grounding DINO는 별도로 학습합니다. OOD 점수 평가에서 먼저 Positive Class·score direction을 정의하고 AUROC/AP(AUPR) 및 FPR@95TPR을 계산합니다. Covariance/Multivariate Gaussian을 PaDiM·GMM·Kalman에 연결하고 PCA/SVD 심화로 확장합니다. OOD 및 Domain Adaptation은 PatchCore/CLIP을 필수로 요구하지 않습니다.

기존 활용: [PRML 종합](../notes/prml.html), [CS231n 종합](../notes/cs231n.html). 모델이나 논문명을 별도의 최상위 카테고리로 놓지 않습니다.

## 탐색 UI 계약

홈에서 시작 경로를 선택할 수 있고, 각 개념 설명 옆에 필수 선수·관련 후속·기존 출처를 표시합니다. 관련 concept가 planned라면 링크 없는 계획 상태로 표시합니다. 기존 index.html?topic=ai 와 ?topic=vision 북마크를 고려하되 기존 notes/*.html 및 #anchor는 바꾸지 않습니다. 반도체 전용 탐색을 제외한 뒤 과거 ?topic=semiconductor는 overview로 안전하게 fallback 합니다.

개념 커버리지의 `needs-expansion`은 기존 설명이 있지만 보강 대상이라는 의미이며, 기존 링크를 새 독립 학습 페이지로 오해하지 않습니다. 자세한 연결은 [Dependency Graph](CONCEPT_DEPENDENCIES.md)를 기준으로 합니다.


## P4 폐포·수치 재현 — R2 설계

<!-- graph-snapshot: parts=16 concepts=263 edges=390 existing-section=42 needs-expansion=21 planned=200 -->

P4는 핵심 8개 + 필수 보조 8개(총 16개)를 포함하며 각 Concept의 신규 페이지·기존 Section·P4 내부 Section을 [Roadmap](IMPLEMENTATION_ROADMAP.md)에 지정했습니다. 기초 Pixel/Mask에는 고급 모델이 필요하지 않습니다.

**OOD 평가 예제 (합성값)**: Positive=OOD인 `y=[1,1,1,0,0,0]`, 높은 값이 OOD인 `score=[0.9,0.8,0.4,0.7,0.3,0.1]`. 정렬 순서 P,P,N,P,N,N. AUROC=`8/9≈0.8889`(9개 양성-음성 쌍 중 8개 순위 성공). AP 방식 AUPR=`(1+1+3/4)/3=11/12≈0.9167`. TPR≥95%를 충족하려면 score≥0.4가 필요하여 `FPR@95TPR=1/3≈0.3333`(TPR=1)입니다. 소수 Positive로 정확히 95% 운영점을 만들 수 없으며, PR의 trapezoidal AUC와 AP는 다를 수 있습니다. Score tie, ID/OOD convention, 클래스 비율을 항상 보고합니다. AUROC/AP는 threshold-free, FPR@95TPR은 threshold-dependent입니다.

**Covariance 예제**: 2D feature `[1,2],[3,4]`의 평균 `[2,3]`, 표본 공분산(분모 n−1)은 `[[2,2],[2,2]]`. Singular covariance이므로 Mahalanobis 역행렬을 그대로 사용할 수 없고 regularization이 필요합니다. PaDiM(위치별 Gaussian), Kalman(process/measurement noise), GMM(성분별 Gaussian), PCA(주축/분산)의 수학적 역할을 따로 다룹니다.

**IoU/Dice 학습**: 집합 A, B의 IoU는 |A∩B|/|A∪B|, Dice는 2|A∩B|/(|A|+|B|)로 소개합니다. Bounding Box/Mask는 선택적 표현 사례입니다. 두 집합이 모두 비어 분모가 0일 때는 값을 임의 단정하지 않고 적용 평가 프로토콜/라이브러리 정책을 먼저 정의합니다.
