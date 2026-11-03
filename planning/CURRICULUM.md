# AI/ML Knowledge Curriculum — PART 00–15

> 작업 대상: `sh0427-han-private/vision_ai`. **논문명이나 산업 도메인이 아닌 AI 개념 중심**. 정본: [개념 카탈로그](CONCEPT_CATALOG.md) · [DAG JSON](concepts.v1.json) · [기존 자료 전수 조사](EXISTING_CONTENT_AUDIT.md).

## 목표·역할

기초 → 원리 → 수식 → 계산 예시 → Python 구현 → 응용 → 한계 → 논문/공식 구현의 연결을 지향합니다. PART 번호는 읽기 순서를 제안하는 **정보 계층**이지, 모든 학습자가 한 줄로 반드시 완주해야 하는 단일 순서는 아닙니다. 선수 관계는 DAG를 정본으로 하며, 상위 PART의 심화 개념에 선수가 부족하면 다른 경로를 거쳐 진입합니다.

**난이도**: Foundation (처음 도입), Basic (기본 알고리즘), Intermediate (수식·구현), Advanced (최적화·시스템 설계), Research (논문 재현). 수준은 PART 단위로 일괄 지정하지 않고 Concept마다 선수 지식을 기준으로 설정했습니다. 해당 값도 설계안이며 독립 Reviewer 검수가 필요합니다.

## PART별 교육 목표와 Chapter

### PART 00. AI & Mathematical Foundations

**학습 목표:** AI·ML의 차이를 이해하고 선형대수·미적분·확률·Python을 복습한다.

**Chapter 후보:** CH 00.1 Python & 배열 · CH 00.2 선형대수 · CH 00.3 미적분 · CH 00.4 확률·통계.

**Concept (27개):** AI·ML·Deep Learning의 관계 · Python 기본 문법 · NumPy 배열 · Matplotlib · Scalar · Vector · Matrix · Tensor · Shape·Dimension·Axis · Dot Product · Matrix Multiplication · Norm·Euclidean Distance · Cosine Similarity · Function·Linear/Nonlinear · Derivative·Partial Derivative · Gradient (Partial Derivatives) · Chain Rule · Probability·Random Variable · Conditional Probability·Bayes Rule · Mean·Variance·Standard Deviation · Covariance·Covariance Matrix · Median·Quantile · Probability Distributions · Multivariate Gaussian Distribution · Likelihood·Log-likelihood · Entropy·KL Divergence · Sampling·Random Seed

**대표 연결:** 기초 수학과 Python → ML / Image Tensor.

### PART 01. Machine Learning Fundamentals

**학습 목표:** 문제를 분류·회귀·비지도학습으로 정식화하고 일반화와 누수를 구분한다.

**Chapter 후보:** CH 01.1 데이터·과업 · CH 01.2 모델·손실 · CH 01.3 일반화·검증.

**Concept (21개):** Supervised·Unsupervised·Self-supervised · Sample·Feature·Label · Classification · Regression · Linear Regression · Logistic Regression · Loss Function · Softmax · Sigmoid · Cross-entropy · MAE·MSE·RMSE · Optimization Objective · Train·Validation·Test · Generalization·Overfitting · Bias–Variance Trade-off · L1·L2 Regularization · Cross-validation · Data Leakage · k-Nearest Neighbors · SVM·Decision Boundary · Probability Calibration

**대표 연결:** 선수 개념에서 시작해 관련 응용·검증·논문으로 확장.

### PART 02. Deep Learning

**학습 목표:** 파라미터 갱신 과정과 gradient 계산, 최적화 선택을 설명한다.

**Chapter 후보:** CH 02.1 MLP·forward · CH 02.2 backprop·optimizer · CH 02.3 regularization·transfer.

**Concept (21개):** Perceptron · Multi-layer Perceptron · Activation·ReLU·GELU · Forward Propagation·Weight·Bias · Computation Graph·Automatic Differentiation · Backpropagation · Gradient Descent · Stochastic Gradient Descent (SGD) · Momentum·Adam·AdamW · Learning Rate · Epoch·Batch·Mini-batch · Weight Initialization · Vanishing·Exploding Gradient · Dropout · Batch Normalization · Layer Normalization · Residual Connection · Transfer Learning · Representation Learning · Fine-tuning · Mixed Precision

**대표 연결:** 선수 개념에서 시작해 관련 응용·검증·논문으로 확장.

### PART 03. Image Processing

**학습 목표:** 파일과 픽셀 배열의 차이, 전처리·주파수·경계 신호를 이해한다.

**Chapter 후보:** CH 03.1 Pixel·Color · CH 03.2 Sampling·Filtering · CH 03.3 Morphology·Frequency.

**Concept (15개):** Pixel·Image Decode · RGB·Channel · Image Tensor·HWC/CHW/NCHW · Dtype·Scaling·Normalization · Resize·Crop·ROI · BGR·HSV·Grayscale · Histogram · Blur·Sharpening · Sobel·Canny Edge · Thresholding·Otsu · Morphology · Contour·Connected Components · FFT·DCT · Noise·Image Quality · Data Augmentation

**대표 연결:** 선수 개념에서 시작해 관련 응용·검증·논문으로 확장.

### PART 04. CNN & Vision Architectures

**학습 목표:** 합성곱의 수치 연산과 아키텍처의 정보 흐름을 추적한다.

**Chapter 후보:** CH 04.1 Kernel·Shape · CH 04.2 Feature Map · CH 04.3 Backbone·ResNet·FPN.

**Concept (15개):** Spatial Filter Kernel · Convolution·Cross-correlation · Stride·Padding·Dilation · Feature Map·Channel · Multi-channel Convolution · Receptive Field · Pooling · CNN·Activation Blocks · Backbone·Neck·Head · VGG · ResNet · Bottleneck·1×1 Conv · EfficientNet · Feature Pyramid·Multi-scale · Architecture Design·Compute

**대표 연결:** Image Tensor → Kernel → Convolution → Feature Map → CNN → ResNet.

### PART 05. Computer Vision Tasks

**학습 목표:** CV 과업별 출력·라벨·지표를 정하고 대표 구조를 비교한다.

**Chapter 후보:** CH 05.1 Classification·Box · CH 05.2 Segmentation·Mask · CH 05.3 U-Net·YOLO·SAM.

**Concept (19개):** Classification·Detection·Segmentation Output · Image Classification · Bounding Box·Coordinates · Object Detection · Semantic Segmentation · Instance Segmentation · Panoptic Segmentation · Polygon·Mask·Hole · IoU·Dice · Non-maximum Suppression · AP·mAP · YOLO Detection·Segmentation · Small Object Detection · U-Net · SAM · SAM2 Video Segmentation · Grounding DINO (Open-Vocabulary Detection) · DETR·Object Queries · DINO-DETR (Denoising Detector)

**대표 연결:** 선수 개념에서 시작해 관련 응용·검증·논문으로 확장.

### PART 06. Transformer & Foundation Models

**학습 목표:** Attention을 행렬·토큰으로 계산하고 Vision Foundation Model을 설명한다.

**Chapter 후보:** CH 06.1 Token·QKV · CH 06.2 Encoder·ViT · CH 06.3 SSL·CLIP·DINO.

**Concept (15개):** Token·Embedding · Positional Encoding · Query·Key·Value · Self-attention · Multi-head Attention · Transformer Encoder · Vision Transformer · Self-Supervised Learning · Contrastive Learning · DINO·Teacher–Student · DINOv2 · CLIP · Foundation Model · Open-vocabulary Recognition · Relative Position Bias

**대표 연결:** Embedding → QKV → Self-attention → ViT → SSL / CLIP.

### PART 07. Anomaly Detection

**학습 목표:** 정상 표현과 이상 점수의 구성을 이해하고 오류와 도메인 변화를 분석한다.

**Chapter 후보:** CH 07.1 One-class · CH 07.2 Feature·Memory · CH 07.3 PatchCore·PaDiM·Calibration.

**Concept (20개):** Outlier·Novelty Detection · One-class Learning · Reconstruction-based Detection · Feature-based Detection · Patch Embedding · Nearest Neighbor · Memory Bank · Coreset Sampling · Approximate Nearest Neighbor · PatchCore · PaDiM · SPADE · STFPM · EfficientAD · Deep SVDD · Autoencoder for Anomaly Detection · Reverse Distillation · Anomaly Score·Heatmap · Anomaly Threshold Selection · Anomaly Domain Shift

**대표 연결:** 정상 특징 → Patch Embedding → NN → Memory → Coreset → PatchCore.

### PART 08. Video AI & Temporal Models

**학습 목표:** 시간 축의 샘플·시퀀스·모델·집계를 설계한다.

**Chapter 후보:** CH 08.1 Frame·Sampling · CH 08.2 Recurrent·Transformer · CH 08.3 Tracking·Event Detection.

**Concept (12개):** Frame·FPS·Timestamp · Sampling·Temporal Window · Video Classification · RNN·LSTM·GRU · Temporal Transformer · 3D CNN · VideoMAE · Optical Flow · Object Tracking · Temporal Aggregation · Persistence·Hysteresis · Video Anomaly Detection

**대표 연결:** 선수 개념에서 시작해 관련 응용·검증·논문으로 확장.

### PART 09. Geometry & Mathematical Vision

**학습 목표:** 영상 좌표와 최적화·강건 통계를 연결해 경계를 정밀화한다.

**Chapter 후보:** CH 09.1 Transform · CH 09.2 Least Squares·SVD · CH 09.3 Robust Ellipse·Subpixel.

**Concept (13개):** Coordinate Systems · Affine Transform · Perspective·Homography · Camera Calibration · Circle·Ellipse Geometry · Least Squares · Eigenvalue·Eigenvector · SVD·PCA · RANSAC · MAD·Robust Statistics · Robust Ellipse Fitting · Subpixel Edge · Boundary Refinement

**대표 연결:** 선수 개념에서 시작해 관련 응용·검증·논문으로 확장.

### PART 10. Statistics & Time-series

**학습 목표:** 시계열 베이스라인과 변화점·드리프트를 구분한다.

**Chapter 후보:** CH 10.1 Moving Stats · CH 10.2 CUSUM·EWMA · CH 10.3 Drift·Online Update.

**Concept (12개):** Time-series·Autocorrelation · Moving Average·Median · Z-score·IQR·MAD · Static·Adaptive Threshold · Step Change Detection · EWMA · CUSUM · Page–Hinkley · Change-point Detection · Concept Drift·Data Drift · Baseline Freeze·Online Update · Event-level Evaluation

**대표 연결:** Moving Median → Threshold → Step Change → Baseline Freeze → Drift.

### PART 11. Dataset & Model Training

**학습 목표:** 수집부터 라벨·분할·버전·재현까지 데이터 생명주기를 설계한다.

**Chapter 후보:** CH 11.1 Label·Format · CH 11.2 Split·Augment · CH 11.3 Experiment & Governance.

**Concept (14개):** Annotation·Taxonomy · Box·Polygon·Mask Formats · Data Collection·Cleaning · Auto-labeling·QA · Augmentation·Train-only · Class Imbalance·Sampling · Hard Negative Mining · Group Split·Leakage · Group K-fold · Temporal Split · Dataset Versioning · Experiment Tracking · Reproducibility·Seed · Privacy·License

**대표 연결:** 선수 개념에서 시작해 관련 응용·검증·논문으로 확장.

### PART 12. Model Evaluation

**학습 목표:** 성능 지표의 의미·정의역·측정 단위를 확인하고 오류를 분석한다.

**Chapter 후보:** CH 12.1 Confusion Metrics · CH 12.2 Segmentation Boundary · CH 12.3 CI·Ablation.

**Concept (13개):** Confusion Matrix · Accuracy·Precision·Recall·F1 · ROC-AUC·PR-AUC · Detection Evaluation Protocols (IoU Thresholds) · Boundary IoU·ASSD·HD95 · Regression Evaluation·Error Diagnostics · Threshold Analysis · Error Analysis · Confidence Interval·Bootstrap · Significance·Effect Size · Ablation Study · OOD Detection Evaluation · Robustness Evaluation

**대표 연결:** 선수 개념에서 시작해 관련 응용·검증·논문으로 확장.

### PART 13. AI Deployment & MLOps

**학습 목표:** 모델 Export부터 Serving·Streaming·Monitoring까지 시스템을 연결한다.

**Chapter 후보:** CH 13.1 ONNX·GPU · CH 13.2 Triton·Batch · CH 13.3 Kafka·Airflow·RTSP.

**Concept (17개):** PyTorch·CUDA · ONNX·Opset · ONNX Runtime · TensorRT · Triton Inference Server · Batch Inference · GPU Memory·Precision · Latency·Throughput · Airflow·DAG · Kafka · S3·MinIO · RTSP·FFmpeg · Timestamp·NTP · Logging·Monitoring · Model Registry·Versioning · CI/CD·Regression · End-to-end Pipeline

**대표 연결:** 선수 개념에서 시작해 관련 응용·검증·논문으로 확장.

### PART 14. Software Engineering for AI

**학습 목표:** AI 프로젝트를 재현 가능하게 구성하고 독립적으로 검증한다.

**Chapter 후보:** CH 14.1 Environment·Configuration · CH 14.2 Tests·Git · CH 14.3 Independent Review.

**Concept (12개):** Python Project Structure · Virtual Environment · Jupyter · Dependency Management · Configuration·Secrets · Modular Design · Unit·Integration Tests · Git·GitHub · Code Review · Reproducible Development · Multi-Agent Workflow · Independent Validation

**대표 연결:** 선수 개념에서 시작해 관련 응용·검증·논문으로 확장.

### PART 15. Advanced Research

**학습 목표:** 확률모델과 고급 연구방법을 기존 주제의 확장으로 배치한다.

**Chapter 후보:** CH 15.1 PRML·Bayesian · CH 15.2 EM·VI·MCMC · CH 15.3 Domain·OOD·Compression.

**Concept (17개):** Bayesian Inference · Graphical Models · Gaussian Mixture · EM Algorithm · Variational Inference·ELBO · Monte Carlo·MCMC · HMM · State-space Models · Kalman Filter · Domain Adaptation · Continual Learning · OOD Detection · Quantization · Pruning · Knowledge Distillation · Diffusion Models · Research Reproduction

**대표 연결:** 선수 개념에서 시작해 관련 응용·검증·논문으로 확장.

## 기존 종합 자료의 위치

CS231n은 개념별 학습 뒤 해당 강의 흐름을 다시 연결하는 **교차 참고 경로**이고, PRML은 확률·회귀·잠재변수·근사추론·연속모형의 **심화 참고 경로**입니다. 두 자료를 신규 개념별 본문으로 무조건 분할/복제하지 않습니다. 기존 [CS231n](../notes/cs231n.html), [PRML](../notes/prml.html), [이미지](../notes/pixels.html), [CNN](../notes/cnn.html)은 기존 URL을 유지합니다.

## 범위·준거

반도체 공정·장비·소재를 독립 PART로 추가하지 않습니다. 제조 관련 기존 학습 사례가 필요한 경우 비식별 일반 이미지·합성 데이터를 사용하고 영상·세그멘테이션·변화감지 등 **일반 AI 원리**에만 연결합니다. 논의한 방법과 실제 검증된 구현의 구분을 강제합니다.

## 추가/중복 기준

새 용어가 이미 있는 Concept의 부분 개념이면 해당 페이지 내 Section으로 추가합니다. 별도 전제·수식·실습·재사용 수요가 있는 경우에만 Concept 승격을 제안합니다. 출처는 논문→공식 구현/문서→대학 강의 순서로 확인합니다.

<!-- graph-snapshot: parts=16 concepts=263 edges=390 existing-section=53 needs-expansion=19 planned=191 -->

## 의미론적 정정 및 상태

개념 분리, 과도한 의존성 제거, 기존 내용의 부분 커버리지 분류는 [SEMANTIC_AUDIT.md](SEMANTIC_AUDIT.md)에 기록했습니다. Curriculum의 개념명·수량은 DAG JSON과 동기화했습니다. 독립 Reviewer의 최종 PASS는 아직 받지 않았습니다.


R1 역사적 기록: 16 PART · 263 Concept · 394 직접 prerequisite edge. `m.covariance`·`m.gaussian_multi`·`dl.autograd` 신규 ID. Batch Normalization과 Layer Normalization, SGD 업데이트와 Epoch/Mini-batch 정의, AP/mAP·회귀 손실 공식과 평가 프로토콜을 분리합니다. R1 당시 P4의 17개 학습 위치는 [Roadmap](IMPLEMENTATION_ROADMAP.md)의 R2 재계산으로 대체되었으며 **구현되었다는 의미는 아닙니다**.

R2 현행: 16 PART · 263 Concept · 390 직접 prerequisite edge. Backpropagation은 Gradient·Chain Rule·Forward·Loss에서 독립적으로 도입하고 Autograd는 구현상의 선택 경로로 다룹니다. CNN은 Feature Map·Activation을 필수로 하고 Pooling은 선택적입니다. Temporal Split·Registry·Drift·IoU/Dice의 일반 정의에서도 불필요한 필수 선수를 제거했습니다. P4 핵심 8 + 필수 보조 8 = 16개 학습 위치이며 실제 구현은 아닙니다.

## P4/R0 Vertical Slice 구현 기록

기존 16 PART의 Concept 목록·Title·Level·ID는 변경하지 않았습니다. Foundation Mathematics 7개 독립 페이지와 기존 Image Tensor/CNN Section 및 Kernel·Pooling을 실제 URL에 매핑했습니다. Phase 4 필수 폐포 16개를 구현했으며 Pooling은 별도 선택 학습입니다. Coverage: existing-section **53**, needs-expansion **19**, planned **191**. 독립 Reviewer 검수 전에는 최종 승인으로 취급하지 않습니다.
