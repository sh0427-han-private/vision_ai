# AI/ML Concept Catalog

> 정본: [concepts.v1.json](concepts.v1.json). **계획 목록이며 완성된 페이지 목록이 아닙니다.**

## ID·범위·상태

- `existing-section`: 현재 URL의 기존 원고에서 해당 개념을 다룹니다. 설명의 완전성·독립 페이지 완성을 의미하지 않습니다.
- `needs-expansion`: 기존 URL에 개념이 소개되어 있지만 교육과정의 독립 학습 목표에 맞게 보강할 필요가 있습니다. URL은 기존 보조 자료로 사용합니다.
- `planned`: 현재 확인된 기존 절과 직접 대응하지 않는 신규 개념입니다. 아직 생성되지 않은 페이지로 연결하지 않습니다.
- 한 개념의 Stable ID는 그대로 유지하고 필요한 경우 별도 Concept을 추가합니다. PART 순서는 필수 선수 순서와 동일하지 않습니다.
- 각 수준은 PART 전체에 일괄 적용하지 않고 실제 설명 및 수학적·시스템적 선수 지식에 따라 지정합니다. 추가 콘텐츠 검증 시 조정합니다.
- 기존 CS231n·PRML의 개요/논문 지도를 새 상세 학습 페이지로 오인하지 않습니다. [기존 콘텐츠 인벤토리](EXISTING_CONTENT_AUDIT.md) 참조.

<!-- graph-snapshot: parts=16 concepts=263 edges=390 existing-section=53 needs-expansion=19 planned=191 -->

## PART 00 — AI & Mathematical Foundations

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `m.ai` | AI·ML·Deep Learning의 관계 | Foundation | 신규 작성 계획 |
| `m.python` | Python 기본 문법 | Foundation | 신규 작성 계획 |
| `m.numpy` | NumPy 배열 | Basic | 신규 작성 계획 |
| `m.plot` | Matplotlib | Basic | 신규 작성 계획 |
| `m.scalar` | Scalar | Foundation | [기존 절](../notes/scalar.html#scalar) |
| `m.vector` | Vector | Foundation | [기존 절](../notes/vector.html#vector) |
| `m.matrix` | Matrix | Foundation | [기존 절](../notes/matrix.html#matrix) |
| `m.tensor` | Tensor | Foundation | [기존 절](../notes/tensor.html#tensor) |
| `m.shape` | Shape·Dimension·Axis | Foundation | [기존 절](../notes/shape.html#shape) |
| `m.dot` | Dot Product | Foundation | [기존 절](../notes/dot-product.html#dot-product) |
| `m.matmul` | Matrix Multiplication | Foundation | 신규 작성 계획 |
| `m.norm` | Norm·Euclidean Distance | Foundation | 신규 작성 계획 |
| `m.cosine` | Cosine Similarity | Foundation | 신규 작성 계획 |
| `m.function` | Function·Linear/Nonlinear | Foundation | [기존 절](../notes/function.html#function) |
| `m.derivative` | Derivative·Partial Derivative | Foundation | 신규 작성 계획 |
| `m.gradient` | Gradient (Partial Derivatives) | Foundation | 신규 작성 계획 |
| `m.chain` | Chain Rule | Foundation | 신규 작성 계획 |
| `m.prob` | Probability·Random Variable | Foundation | [기존 소개·보강 필요](../notes/prml.html#ch1) |
| `m.bayes` | Conditional Probability·Bayes Rule | Basic | [기존 소개·보강 필요](../notes/prml.html#ch1) |
| `m.mean` | Mean·Variance·Standard Deviation | Foundation | 신규 작성 계획 |
| `m.covariance` | Covariance·Covariance Matrix | Basic | 신규 작성 계획 |
| `m.median` | Median·Quantile | Foundation | 신규 작성 계획 |
| `m.distribution` | Probability Distributions | Basic | [기존 소개·보강 필요](../notes/prml.html#ch2) |
| `m.gaussian_multi` | Multivariate Gaussian Distribution | Intermediate | 신규 작성 계획 |
| `m.likelihood` | Likelihood·Log-likelihood | Basic | [기존 소개·보강 필요](../notes/prml.html#ch1) |
| `m.entropy` | Entropy·KL Divergence | Basic | [기존 소개·보강 필요](../notes/prml.html#ch1) |
| `m.sample` | Sampling·Random Seed | Foundation | 신규 작성 계획 |

## PART 01 — Machine Learning Fundamentals

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `ml.paradigm` | Supervised·Unsupervised·Self-supervised | Basic | 신규 작성 계획 |
| `ml.dataset` | Sample·Feature·Label | Foundation | 신규 작성 계획 |
| `ml.classification` | Classification | Foundation | 신규 작성 계획 |
| `ml.regression` | Regression | Foundation | 신규 작성 계획 |
| `ml.linear` | Linear Regression | Basic | [기존 소개·보강 필요](../notes/prml.html#ch3) |
| `ml.logistic` | Logistic Regression | Basic | [기존 소개·보강 필요](../notes/prml.html#ch4) |
| `ml.loss` | Loss Function | Basic | [기존 절](../notes/cs231n.html#linear) |
| `ml.softmax` | Softmax | Basic | [기존 소개·보강 필요](../notes/prml.html#ch4) |
| `ml.sigmoid` | Sigmoid | Basic | [기존 소개·보강 필요](../notes/prml.html#ch4) |
| `ml.ce` | Cross-entropy | Basic | 신규 작성 계획 |
| `ml.mse` | MAE·MSE·RMSE | Basic | 신규 작성 계획 |
| `ml.optim` | Optimization Objective | Basic | 신규 작성 계획 |
| `ml.split` | Train·Validation·Test | Basic | [기존 절](../notes/training.html#split) |
| `ml.generalize` | Generalization·Overfitting | Basic | 신규 작성 계획 |
| `ml.bias` | Bias–Variance Trade-off | Basic | 신규 작성 계획 |
| `ml.regularize` | L1·L2 Regularization | Basic | 신규 작성 계획 |
| `ml.cv` | Cross-validation | Intermediate | [기존 절](../notes/training.html#cv) |
| `ml.leakage` | Data Leakage | Basic | [기존 절](../notes/training.html#split) |
| `ml.knn` | k-Nearest Neighbors | Basic | [기존 소개·보강 필요](../notes/cs231n.html#classification) |
| `ml.svm` | SVM·Decision Boundary | Intermediate | 신규 작성 계획 |
| `ml.calibration` | Probability Calibration | Intermediate | 신규 작성 계획 |

## PART 02 — Deep Learning

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `dl.perceptron` | Perceptron | Basic | 신규 작성 계획 |
| `dl.mlp` | Multi-layer Perceptron | Basic | [기존 소개·보강 필요](../notes/cs231n.html#nn) |
| `dl.activation` | Activation·ReLU·GELU | Basic | [기존 절](../notes/cnn.html#nonlinear) |
| `dl.forward` | Forward Propagation·Weight·Bias | Basic | 신규 작성 계획 |
| `dl.autograd` | Computation Graph·Automatic Differentiation | Intermediate | 신규 작성 계획 |
| `dl.backprop` | Backpropagation | Intermediate | [기존 절](../notes/cs231n.html#optimization) |
| `dl.gd` | Gradient Descent | Basic | 신규 작성 계획 |
| `dl.sgd` | Stochastic Gradient Descent (SGD) | Intermediate | 신규 작성 계획 |
| `dl.adam` | Momentum·Adam·AdamW | Intermediate | 신규 작성 계획 |
| `dl.lr` | Learning Rate | Basic | 신규 작성 계획 |
| `dl.epoch` | Epoch·Batch·Mini-batch | Basic | 신규 작성 계획 |
| `dl.init` | Weight Initialization | Intermediate | 신규 작성 계획 |
| `dl.vanish` | Vanishing·Exploding Gradient | Intermediate | 신규 작성 계획 |
| `dl.dropout` | Dropout | Intermediate | 신규 작성 계획 |
| `dl.bn` | Batch Normalization | Intermediate | 신규 작성 계획 |
| `dl.ln` | Layer Normalization | Intermediate | 신규 작성 계획 |
| `dl.residual` | Residual Connection | Intermediate | 신규 작성 계획 |
| `dl.transfer` | Transfer Learning | Intermediate | [기존 소개·보강 필요](../notes/cs231n.html#transfer) |
| `dl.repr` | Representation Learning | Intermediate | [기존 소개·보강 필요](../notes/cs231n.html#transfer) |
| `dl.finetune` | Fine-tuning | Intermediate | 신규 작성 계획 |
| `dl.mixed` | Mixed Precision | Advanced | 신규 작성 계획 |

## PART 03 — Image Processing

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `img.pixel` | Pixel·Image Decode | Foundation | [기존 절](../notes/pixels.html#pixels) |
| `img.rgb` | RGB·Channel | Foundation | [기존 절](../notes/pixels.html#pixels) |
| `img.tensor` | Image Tensor·HWC/CHW/NCHW | Foundation | [기존 절](../notes/pixels.html#layout) |
| `img.dtype` | Dtype·Scaling·Normalization | Basic | [기존 절](../notes/pixels.html#normalization) |
| `img.resize` | Resize·Crop·ROI | Basic | [기존 절](../notes/pixels.html#resize) |
| `img.color` | BGR·HSV·Grayscale | Basic | 신규 작성 계획 |
| `img.hist` | Histogram | Basic | 신규 작성 계획 |
| `img.blur` | Blur·Sharpening | Basic | 신규 작성 계획 |
| `img.edge` | Sobel·Canny Edge | Intermediate | 신규 작성 계획 |
| `img.threshold` | Thresholding·Otsu | Basic | 신규 작성 계획 |
| `img.morph` | Morphology | Basic | 신규 작성 계획 |
| `img.contour` | Contour·Connected Components | Basic | 신규 작성 계획 |
| `img.fft` | FFT·DCT | Basic | 신규 작성 계획 |
| `img.quality` | Noise·Image Quality | Basic | 신규 작성 계획 |
| `img.augment` | Data Augmentation | Basic | 신규 작성 계획 |

## PART 04 — CNN & Vision Architectures

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `cnn.kernel` | Spatial Filter Kernel | Basic | [기존 절](../notes/cnn.html#kernel) |
| `cnn.conv` | Convolution·Cross-correlation | Intermediate | [기존 절](../notes/cnn.html#convolution) |
| `cnn.stride` | Stride·Padding·Dilation | Basic | [기존 절](../notes/cnn.html#shape) |
| `cnn.map` | Feature Map·Channel | Basic | [기존 절](../notes/cnn.html#overview) |
| `cnn.multi` | Multi-channel Convolution | Intermediate | [기존 절](../notes/cnn.html#channels) |
| `cnn.rf` | Receptive Field | Intermediate | [기존 절](../notes/cnn.html#shape) |
| `cnn.pool` | Pooling | Basic | [기존 절](../notes/cnn.html#pooling) |
| `cnn.base` | CNN·Activation Blocks | Intermediate | [기존 절](../notes/cnn.html#overview) |
| `cnn.bnh` | Backbone·Neck·Head | Intermediate | 신규 작성 계획 |
| `cnn.vgg` | VGG | Intermediate | 신규 작성 계획 |
| `cnn.resnet` | ResNet | Intermediate | [기존 절](../notes/cnn.html#resnet_problem) |
| `cnn.bottleneck` | Bottleneck·1×1 Conv | Intermediate | [기존 절](../notes/cnn.html#resnet_bottleneck) |
| `cnn.efficient` | EfficientNet | Intermediate | 신규 작성 계획 |
| `cnn.fpn` | Feature Pyramid·Multi-scale | Intermediate | 신규 작성 계획 |
| `cnn.design` | Architecture Design·Compute | Intermediate | 신규 작성 계획 |

## PART 05 — Computer Vision Tasks

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `cv.task` | Classification·Detection·Segmentation Output | Foundation | [기존 절](../notes/tasks.html#overview) |
| `cv.class` | Image Classification | Basic | [기존 절](../notes/tasks.html#overview) |
| `cv.box` | Bounding Box·Coordinates | Basic | 신규 작성 계획 |
| `cv.detect` | Object Detection | Intermediate | [기존 절](../notes/tasks.html#overview) |
| `cv.semantic` | Semantic Segmentation | Intermediate | [기존 절](../notes/tasks.html#segmentation_context) |
| `cv.instance` | Instance Segmentation | Intermediate | [기존 절](../notes/tasks.html#overview) |
| `cv.panoptic` | Panoptic Segmentation | Intermediate | 신규 작성 계획 |
| `cv.mask` | Polygon·Mask·Hole | Basic | 신규 작성 계획 |
| `cv.iou` | IoU·Dice | Basic | [기존 절](../notes/tasks.html#iou) |
| `cv.nms` | Non-maximum Suppression | Intermediate | 신규 작성 계획 |
| `cv.map` | AP·mAP | Intermediate | 신규 작성 계획 |
| `cv.yolo` | YOLO Detection·Segmentation | Intermediate | 신규 작성 계획 |
| `cv.small` | Small Object Detection | Intermediate | 신규 작성 계획 |
| `cv.unet` | U-Net | Intermediate | [기존 절](../notes/tasks.html#unet_architecture) |
| `cv.sam` | SAM | Advanced | 신규 작성 계획 |
| `cv.sam2` | SAM2 Video Segmentation | Advanced | 신규 작성 계획 |
| `cv.grounding` | Grounding DINO (Open-Vocabulary Detection) | Advanced | 신규 작성 계획 |
| `cv.detr` | DETR·Object Queries | Advanced | 신규 작성 계획 |
| `cv.dino_detr` | DINO-DETR (Denoising Detector) | Advanced | 신규 작성 계획 |

## PART 06 — Transformer & Foundation Models

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `tr.token` | Token·Embedding | Basic | [기존 절](../notes/vit.html#tokens) |
| `tr.position` | Positional Encoding | Basic | 신규 작성 계획 |
| `tr.qkv` | Query·Key·Value | Intermediate | [기존 절](../notes/vit.html#attention) |
| `tr.attention` | Self-attention | Intermediate | [기존 절](../notes/vit.html#attention) |
| `tr.multi` | Multi-head Attention | Intermediate | [기존 소개·보강 필요](../notes/vit.html#attention) |
| `tr.encoder` | Transformer Encoder | Intermediate | [기존 절](../notes/vit.html#encoder) |
| `tr.vit` | Vision Transformer | Advanced | [기존 절](../notes/vit.html#patches) |
| `tr.ssl` | Self-Supervised Learning | Intermediate | [기존 소개·보강 필요](../notes/cs231n.html#modern) |
| `tr.contrast` | Contrastive Learning | Intermediate | 신규 작성 계획 |
| `tr.dino` | DINO·Teacher–Student | Advanced | [기존 소개·보강 필요](../notes/cs231n.html#modern) |
| `tr.dinov2` | DINOv2 | Advanced | 신규 작성 계획 |
| `tr.clip` | CLIP | Advanced | [기존 소개·보강 필요](../notes/cs231n.html#modern) |
| `tr.foundation` | Foundation Model | Advanced | 신규 작성 계획 |
| `tr.open` | Open-vocabulary Recognition | Advanced | 신규 작성 계획 |
| `tr.relative` | Relative Position Bias | Advanced | 신규 작성 계획 |

## PART 07 — Anomaly Detection

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `an.outlier` | Outlier·Novelty Detection | Basic | [기존 절](../notes/patchcore.html#problem) |
| `an.one` | One-class Learning | Basic | 신규 작성 계획 |
| `an.recon` | Reconstruction-based Detection | Intermediate | 신규 작성 계획 |
| `an.feature` | Feature-based Detection | Intermediate | 신규 작성 계획 |
| `an.embedding` | Patch Embedding | Intermediate | 신규 작성 계획 |
| `an.nearest` | Nearest Neighbor | Intermediate | [기존 절](../notes/patchcore.html#score) |
| `an.memory` | Memory Bank | Intermediate | [기존 절](../notes/patchcore.html#memory) |
| `an.coreset` | Coreset Sampling | Advanced | 신규 작성 계획 |
| `an.ann` | Approximate Nearest Neighbor | Advanced | 신규 작성 계획 |
| `an.patchcore` | PatchCore | Advanced | [기존 절](../notes/patchcore.html#pipeline) |
| `an.padim` | PaDiM | Advanced | 신규 작성 계획 |
| `an.spade` | SPADE | Advanced | 신규 작성 계획 |
| `an.stfpm` | STFPM | Advanced | 신규 작성 계획 |
| `an.efficientad` | EfficientAD | Advanced | 신규 작성 계획 |
| `an.svdd` | Deep SVDD | Advanced | 신규 작성 계획 |
| `an.ae` | Autoencoder for Anomaly Detection | Advanced | 신규 작성 계획 |
| `an.reverse` | Reverse Distillation | Advanced | 신규 작성 계획 |
| `an.score` | Anomaly Score·Heatmap | Basic | [기존 소개·보강 필요](../notes/patchcore.html#score) |
| `an.threshold` | Anomaly Threshold Selection | Intermediate | 신규 작성 계획 |
| `an.shift` | Anomaly Domain Shift | Advanced | 신규 작성 계획 |

## PART 08 — Video AI & Temporal Models

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `video.frame` | Frame·FPS·Timestamp | Basic | 신규 작성 계획 |
| `video.sample` | Sampling·Temporal Window | Basic | 신규 작성 계획 |
| `video.class` | Video Classification | Intermediate | 신규 작성 계획 |
| `video.rnn` | RNN·LSTM·GRU | Intermediate | 신규 작성 계획 |
| `video.temporal` | Temporal Transformer | Intermediate | 신규 작성 계획 |
| `video.cnn3d` | 3D CNN | Intermediate | 신규 작성 계획 |
| `video.mae` | VideoMAE | Intermediate | 신규 작성 계획 |
| `video.flow` | Optical Flow | Intermediate | 신규 작성 계획 |
| `video.track` | Object Tracking | Intermediate | 신규 작성 계획 |
| `video.aggregate` | Temporal Aggregation | Basic | 신규 작성 계획 |
| `video.persist` | Persistence·Hysteresis | Basic | 신규 작성 계획 |
| `video.anomaly` | Video Anomaly Detection | Intermediate | 신규 작성 계획 |

## PART 09 — Geometry & Mathematical Vision

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `geo.coords` | Coordinate Systems | Basic | 신규 작성 계획 |
| `geo.affine` | Affine Transform | Intermediate | 신규 작성 계획 |
| `geo.homo` | Perspective·Homography | Advanced | 신규 작성 계획 |
| `geo.calib` | Camera Calibration | Advanced | 신규 작성 계획 |
| `geo.circle` | Circle·Ellipse Geometry | Basic | 신규 작성 계획 |
| `geo.ls` | Least Squares | Intermediate | 신규 작성 계획 |
| `geo.eigen` | Eigenvalue·Eigenvector | Intermediate | 신규 작성 계획 |
| `geo.svd` | SVD·PCA | Intermediate | [기존 소개·보강 필요](../notes/prml.html#ch12) |
| `geo.ransac` | RANSAC | Intermediate | 신규 작성 계획 |
| `geo.mad` | MAD·Robust Statistics | Intermediate | 신규 작성 계획 |
| `geo.fit` | Robust Ellipse Fitting | Advanced | 신규 작성 계획 |
| `geo.subpixel` | Subpixel Edge | Advanced | 신규 작성 계획 |
| `geo.boundary` | Boundary Refinement | Advanced | 신규 작성 계획 |

## PART 10 — Statistics & Time-series

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `ts.series` | Time-series·Autocorrelation | Basic | 신규 작성 계획 |
| `ts.moving` | Moving Average·Median | Basic | 신규 작성 계획 |
| `ts.z` | Z-score·IQR·MAD | Basic | 신규 작성 계획 |
| `ts.threshold` | Static·Adaptive Threshold | Basic | 신규 작성 계획 |
| `ts.step` | Step Change Detection | Intermediate | 신규 작성 계획 |
| `ts.ewma` | EWMA | Intermediate | 신규 작성 계획 |
| `ts.cusum` | CUSUM | Intermediate | 신규 작성 계획 |
| `ts.ph` | Page–Hinkley | Advanced | 신규 작성 계획 |
| `ts.changepoint` | Change-point Detection | Intermediate | 신규 작성 계획 |
| `ts.drift` | Concept Drift·Data Drift | Intermediate | 신규 작성 계획 |
| `ts.baseline` | Baseline Freeze·Online Update | Intermediate | 신규 작성 계획 |
| `ts.event` | Event-level Evaluation | Intermediate | 신규 작성 계획 |

## PART 11 — Dataset & Model Training

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `data.label` | Annotation·Taxonomy | Basic | 신규 작성 계획 |
| `data.format` | Box·Polygon·Mask Formats | Basic | 신규 작성 계획 |
| `data.collect` | Data Collection·Cleaning | Basic | 신규 작성 계획 |
| `data.auto` | Auto-labeling·QA | Intermediate | 신규 작성 계획 |
| `data.augment` | Augmentation·Train-only | Intermediate | 신규 작성 계획 |
| `data.imbalance` | Class Imbalance·Sampling | Intermediate | 신규 작성 계획 |
| `data.hard` | Hard Negative Mining | Intermediate | 신규 작성 계획 |
| `data.group` | Group Split·Leakage | Intermediate | [기존 절](../notes/training.html#split) |
| `data.kfold` | Group K-fold | Intermediate | 신규 작성 계획 |
| `data.temporal` | Temporal Split | Intermediate | 신규 작성 계획 |
| `data.version` | Dataset Versioning | Intermediate | 신규 작성 계획 |
| `data.experiment` | Experiment Tracking | Intermediate | 신규 작성 계획 |
| `data.repro` | Reproducibility·Seed | Intermediate | 신규 작성 계획 |
| `data.privacy` | Privacy·License | Basic | 신규 작성 계획 |

## PART 12 — Model Evaluation

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `eval.confusion` | Confusion Matrix | Basic | 신규 작성 계획 |
| `eval.prf` | Accuracy·Precision·Recall·F1 | Basic | [기존 절](../notes/training.html#metrics) |
| `eval.auc` | ROC-AUC·PR-AUC | Intermediate | 신규 작성 계획 |
| `eval.iou` | Detection Evaluation Protocols (IoU Thresholds) | Intermediate | 신규 작성 계획 |
| `eval.boundary` | Boundary IoU·ASSD·HD95 | Intermediate | 신규 작성 계획 |
| `eval.reg` | Regression Evaluation·Error Diagnostics | Basic | 신규 작성 계획 |
| `eval.threshold` | Threshold Analysis | Intermediate | 신규 작성 계획 |
| `eval.error` | Error Analysis | Intermediate | 신규 작성 계획 |
| `eval.ci` | Confidence Interval·Bootstrap | Intermediate | 신규 작성 계획 |
| `eval.effect` | Significance·Effect Size | Intermediate | 신규 작성 계획 |
| `eval.ablation` | Ablation Study | Intermediate | 신규 작성 계획 |
| `eval.ood` | OOD Detection Evaluation | Intermediate | 신규 작성 계획 |
| `eval.robust` | Robustness Evaluation | Intermediate | 신규 작성 계획 |

## PART 13 — AI Deployment & MLOps

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `ops.pytorch` | PyTorch·CUDA | Basic | 신규 작성 계획 |
| `ops.onnx` | ONNX·Opset | Intermediate | 신규 작성 계획 |
| `ops.ort` | ONNX Runtime | Intermediate | 신규 작성 계획 |
| `ops.trt` | TensorRT | Advanced | 신규 작성 계획 |
| `ops.triton` | Triton Inference Server | Advanced | 신규 작성 계획 |
| `ops.batch` | Batch Inference | Basic | 신규 작성 계획 |
| `ops.gpu` | GPU Memory·Precision | Intermediate | 신규 작성 계획 |
| `ops.latency` | Latency·Throughput | Intermediate | 신규 작성 계획 |
| `ops.airflow` | Airflow·DAG | Advanced | 신규 작성 계획 |
| `ops.kafka` | Kafka | Advanced | 신규 작성 계획 |
| `ops.s3` | S3·MinIO | Advanced | 신규 작성 계획 |
| `ops.rtsp` | RTSP·FFmpeg | Intermediate | 신규 작성 계획 |
| `ops.ntp` | Timestamp·NTP | Intermediate | 신규 작성 계획 |
| `ops.monitor` | Logging·Monitoring | Advanced | 신규 작성 계획 |
| `ops.registry` | Model Registry·Versioning | Intermediate | 신규 작성 계획 |
| `ops.cicd` | CI/CD·Regression | Advanced | 신규 작성 계획 |
| `ops.pipeline` | End-to-end Pipeline | Advanced | 신규 작성 계획 |

## PART 14 — Software Engineering for AI

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `eng.project` | Python Project Structure | Foundation | 신규 작성 계획 |
| `eng.venv` | Virtual Environment | Basic | 신규 작성 계획 |
| `eng.jupyter` | Jupyter | Basic | 신규 작성 계획 |
| `eng.deps` | Dependency Management | Basic | 신규 작성 계획 |
| `eng.config` | Configuration·Secrets | Basic | 신규 작성 계획 |
| `eng.module` | Modular Design | Basic | 신규 작성 계획 |
| `eng.test` | Unit·Integration Tests | Intermediate | 신규 작성 계획 |
| `eng.git` | Git·GitHub | Basic | 신규 작성 계획 |
| `eng.review` | Code Review | Intermediate | 신규 작성 계획 |
| `eng.repro` | Reproducible Development | Intermediate | 신규 작성 계획 |
| `eng.agent` | Multi-Agent Workflow | Advanced | 신규 작성 계획 |
| `eng.independent` | Independent Validation | Intermediate | 신규 작성 계획 |

## PART 15 — Advanced Research

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `res.bayes` | Bayesian Inference | Intermediate | [기존 절](../notes/prml.html#ch1) |
| `res.graph` | Graphical Models | Advanced | 신규 작성 계획 |
| `res.gmm` | Gaussian Mixture | Intermediate | [기존 절](../notes/prml.html#ch9) |
| `res.em` | EM Algorithm | Advanced | [기존 절](../notes/prml.html#ch9) |
| `res.vi` | Variational Inference·ELBO | Advanced | [기존 절](../notes/prml.html#ch10) |
| `res.mcmc` | Monte Carlo·MCMC | Advanced | [기존 절](../notes/prml.html#ch11) |
| `res.hmm` | HMM | Advanced | [기존 절](../notes/prml.html#ch13) |
| `res.state` | State-space Models | Advanced | 신규 작성 계획 |
| `res.kalman` | Kalman Filter | Advanced | [기존 절](../notes/prml.html#ch13) |
| `res.domain` | Domain Adaptation | Advanced | 신규 작성 계획 |
| `res.continual` | Continual Learning | Research | 신규 작성 계획 |
| `res.ood` | OOD Detection | Advanced | 신규 작성 계획 |
| `res.quant` | Quantization | Advanced | 신규 작성 계획 |
| `res.prune` | Pruning | Advanced | 신규 작성 계획 |
| `res.distill` | Knowledge Distillation | Advanced | 신규 작성 계획 |
| `res.diffusion` | Diffusion Models | Research | 신규 작성 계획 |
| `res.research` | Research Reproduction | Research | 신규 작성 계획 |

## 현재 범위

- 16 PART · 263 Concept · 394 직접 prerequisite edge. 커버리지: existing-section 42, needs-expansion 21, planned 200.
- 기존 260개 ID 유지; 추가 Stable ID는 `m.covariance`, `m.gaussian_multi`, `dl.autograd`.
- AP/mAP 정의는 `cv.map`, Detection 평가 프로토콜은 `eval.iou`; MAE/MSE/RMSE의 정의는 `ml.mse`, 평가 응용은 `eval.reg`을 정본으로 합니다.

## P4/R0 실제 콘텐츠 반영

2026-11-03 P4 신규 독립 URL 7개와 기존 CNN 내부 Section 2개를 실제 빌더에서 생성하도록 등록했습니다. `cnn.map`, `dl.activation`은 기존 Section을 P4 수치 목표로 보강했습니다. 263 Stable ID·390 필수 Edge는 유지하고, 현재 `existing-section` 53 / `needs-expansion` 19 / `planned` 191입니다. 상태는 Anchor·학습 목표의 매핑을 나타내며 독립 Reviewer 승인과는 별개입니다.
