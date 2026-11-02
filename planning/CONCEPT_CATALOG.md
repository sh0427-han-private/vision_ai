# AI/ML Concept Catalog

> 기존 기준: `main@e2b2c2f`. 정본: [concepts.v1.json](concepts.v1.json). **계획 목록**이며 신규 HTML 페이지를 구현했다고 뜻하지 않습니다.

## ID·상태·중복 관리

- `existing-section`: 검토한 기존 `notes/*.html#anchor`에 설명이 있음. 개념별 독립 페이지나 설명 완성도를 보장하지 않음.
- `planned`: 새 원고 작성 또는 기존 내용 보강 후보. 비어 있는 링크는 노출하지 않음.
- Stable ID를 변경하기 전 사용처 전수 검색. `CNN kernel`과 `Gaussian kernel`, `MAD`와 `MAE`, `이미지 stride`와 `시간 stride`는 별도 정의.
- 같은 개념을 CS231n과 PRML·주제 페이지에 복제하지 않고 주제 페이지 하나를 canonical로 지정하고 종합 문서에서는 교차 링크.

## PART 00 — AI & Mathematical Foundations

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `m.ai` | AI·ML·Deep Learning의 관계 | Foundation | 추가/보강 계획 |
| `m.python` | Python 기본 문법 | Foundation | 추가/보강 계획 |
| `m.numpy` | NumPy 배열 | Foundation | 추가/보강 계획 |
| `m.plot` | Matplotlib | Foundation | 추가/보강 계획 |
| `m.scalar` | Scalar | Foundation | 추가/보강 계획 |
| `m.vector` | Vector | Foundation | 추가/보강 계획 |
| `m.matrix` | Matrix | Foundation | 추가/보강 계획 |
| `m.tensor` | Tensor | Foundation | 추가/보강 계획 |
| `m.shape` | Shape·Dimension·Axis | Foundation | 추가/보강 계획 |
| `m.dot` | Dot Product | Foundation | 추가/보강 계획 |
| `m.matmul` | Matrix Multiplication | Foundation | 추가/보강 계획 |
| `m.norm` | Norm·Euclidean Distance | Foundation | 추가/보강 계획 |
| `m.cosine` | Cosine Similarity | Foundation | 추가/보강 계획 |
| `m.function` | Function·Linear/Nonlinear | Foundation | 추가/보강 계획 |
| `m.derivative` | Derivative·Partial Derivative | Foundation | 추가/보강 계획 |
| `m.gradient` | Gradient·Chain Rule | Foundation | 추가/보강 계획 |
| `m.prob` | Probability·Random Variable | Foundation | 추가/보강 계획 |
| `m.bayes` | Conditional Probability·Bayes Rule | Foundation | 추가/보강 계획 |
| `m.mean` | Mean·Variance·Standard Deviation | Foundation | 추가/보강 계획 |
| `m.median` | Median·Quantile | Foundation | 추가/보강 계획 |
| `m.distribution` | Probability Distributions | Foundation | 추가/보강 계획 |
| `m.likelihood` | Likelihood·Log-likelihood | Foundation | 추가/보강 계획 |
| `m.entropy` | Entropy·KL Divergence | Foundation | 추가/보강 계획 |
| `m.sample` | Sampling·Random Seed | Foundation | 추가/보강 계획 |

## PART 01 — Machine Learning Fundamentals

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `ml.paradigm` | Supervised·Unsupervised·Self-supervised | Basic | 추가/보강 계획 |
| `ml.dataset` | Sample·Feature·Label | Basic | 추가/보강 계획 |
| `ml.classification` | Classification | Basic | 추가/보강 계획 |
| `ml.regression` | Regression | Basic | 추가/보강 계획 |
| `ml.linear` | Linear Regression | Basic | 추가/보강 계획 |
| `ml.logistic` | Logistic Regression | Basic | 추가/보강 계획 |
| `ml.loss` | Loss Function | Basic | [기존 절](../notes/cs231n.html#linear) |
| `ml.softmax` | Sigmoid·Softmax | Basic | 추가/보강 계획 |
| `ml.ce` | Cross-entropy | Basic | 추가/보강 계획 |
| `ml.mse` | MAE·MSE·RMSE | Basic | 추가/보강 계획 |
| `ml.optim` | Optimization Objective | Basic | 추가/보강 계획 |
| `ml.split` | Train·Validation·Test | Basic | [기존 절](../notes/training.html#split) |
| `ml.generalize` | Generalization·Overfitting | Basic | 추가/보강 계획 |
| `ml.bias` | Bias–Variance Trade-off | Basic | 추가/보강 계획 |
| `ml.regularize` | L1·L2 Regularization | Basic | 추가/보강 계획 |
| `ml.cv` | Cross-validation | Basic | [기존 절](../notes/training.html#cv) |
| `ml.leakage` | Data Leakage | Basic | [기존 절](../notes/training.html#split) |
| `ml.knn` | k-Nearest Neighbors | Basic | 추가/보강 계획 |
| `ml.svm` | SVM·Decision Boundary | Basic | 추가/보강 계획 |
| `ml.calibration` | Probability Calibration | Basic | 추가/보강 계획 |

## PART 02 — Deep Learning

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `dl.perceptron` | Perceptron | Intermediate | 추가/보강 계획 |
| `dl.mlp` | Multi-layer Perceptron | Intermediate | 추가/보강 계획 |
| `dl.activation` | Activation·ReLU·GELU | Intermediate | 추가/보강 계획 |
| `dl.forward` | Forward Propagation·Weight·Bias | Intermediate | 추가/보강 계획 |
| `dl.backprop` | Backpropagation | Intermediate | [기존 절](../notes/cs231n.html#optimization) |
| `dl.gd` | Gradient Descent | Intermediate | 추가/보강 계획 |
| `dl.sgd` | SGD·Mini-batch | Intermediate | 추가/보강 계획 |
| `dl.adam` | Momentum·Adam·AdamW | Intermediate | 추가/보강 계획 |
| `dl.lr` | Learning Rate·Epoch·Batch | Intermediate | 추가/보강 계획 |
| `dl.init` | Weight Initialization | Intermediate | 추가/보강 계획 |
| `dl.vanish` | Vanishing·Exploding Gradient | Intermediate | 추가/보강 계획 |
| `dl.dropout` | Dropout | Intermediate | 추가/보강 계획 |
| `dl.bn` | Batch·Layer Normalization | Intermediate | 추가/보강 계획 |
| `dl.residual` | Residual Connection | Intermediate | 추가/보강 계획 |
| `dl.transfer` | Representation·Transfer Learning | Intermediate | 추가/보강 계획 |
| `dl.finetune` | Fine-tuning | Intermediate | 추가/보강 계획 |
| `dl.mixed` | Mixed Precision | Intermediate | 추가/보강 계획 |

## PART 03 — Image Processing

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `img.pixel` | Pixel·Image Decode | Basic | [기존 절](../notes/pixels.html#pixels) |
| `img.rgb` | RGB·Channel | Basic | [기존 절](../notes/pixels.html#pixels) |
| `img.tensor` | Image Tensor·HWC/CHW/NCHW | Basic | [기존 절](../notes/pixels.html#layout) |
| `img.dtype` | Dtype·Scaling·Normalization | Basic | [기존 절](../notes/pixels.html#normalization) |
| `img.resize` | Resize·Crop·ROI | Basic | [기존 절](../notes/pixels.html#resize) |
| `img.color` | BGR·HSV·Grayscale | Basic | 추가/보강 계획 |
| `img.hist` | Histogram | Basic | 추가/보강 계획 |
| `img.blur` | Blur·Sharpening | Basic | 추가/보강 계획 |
| `img.edge` | Sobel·Canny Edge | Basic | 추가/보강 계획 |
| `img.threshold` | Thresholding·Otsu | Basic | 추가/보강 계획 |
| `img.morph` | Morphology | Basic | 추가/보강 계획 |
| `img.contour` | Contour·Connected Components | Basic | 추가/보강 계획 |
| `img.fft` | FFT·DCT | Basic | 추가/보강 계획 |
| `img.quality` | Noise·Image Quality | Basic | 추가/보강 계획 |
| `img.augment` | Data Augmentation | Basic | 추가/보강 계획 |

## PART 04 — CNN & Vision Architectures

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `cnn.kernel` | Spatial Filter Kernel | Intermediate | 추가/보강 계획 |
| `cnn.conv` | Convolution·Cross-correlation | Intermediate | [기존 절](../notes/cnn.html#convolution) |
| `cnn.stride` | Stride·Padding·Dilation | Intermediate | [기존 절](../notes/cnn.html#shape) |
| `cnn.map` | Feature Map·Channel | Intermediate | 추가/보강 계획 |
| `cnn.multi` | Multi-channel Convolution | Intermediate | [기존 절](../notes/cnn.html#channels) |
| `cnn.rf` | Receptive Field | Intermediate | [기존 절](../notes/cnn.html#shape) |
| `cnn.pool` | Pooling | Intermediate | 추가/보강 계획 |
| `cnn.base` | CNN·Activation Blocks | Intermediate | [기존 절](../notes/cnn.html#overview) |
| `cnn.bnh` | Backbone·Neck·Head | Intermediate | 추가/보강 계획 |
| `cnn.vgg` | VGG | Intermediate | 추가/보강 계획 |
| `cnn.resnet` | ResNet | Intermediate | [기존 절](../notes/cnn.html#resnet_problem) |
| `cnn.bottleneck` | Bottleneck·1×1 Conv | Intermediate | [기존 절](../notes/cnn.html#resnet_bottleneck) |
| `cnn.efficient` | EfficientNet | Intermediate | 추가/보강 계획 |
| `cnn.fpn` | Feature Pyramid·Multi-scale | Intermediate | 추가/보강 계획 |
| `cnn.design` | Architecture Design·Compute | Intermediate | 추가/보강 계획 |

## PART 05 — Computer Vision Tasks

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `cv.task` | Classification·Detection·Segmentation Output | Intermediate | [기존 절](../notes/tasks.html#overview) |
| `cv.class` | Image Classification | Intermediate | [기존 절](../notes/tasks.html#overview) |
| `cv.box` | Bounding Box·Coordinates | Intermediate | 추가/보강 계획 |
| `cv.detect` | Object Detection | Intermediate | [기존 절](../notes/tasks.html#overview) |
| `cv.semantic` | Semantic Segmentation | Intermediate | [기존 절](../notes/tasks.html#segmentation_context) |
| `cv.instance` | Instance Segmentation | Intermediate | [기존 절](../notes/tasks.html#overview) |
| `cv.panoptic` | Panoptic Segmentation | Intermediate | 추가/보강 계획 |
| `cv.mask` | Polygon·Mask·Hole | Intermediate | 추가/보강 계획 |
| `cv.iou` | IoU·Dice | Intermediate | [기존 절](../notes/tasks.html#iou) |
| `cv.nms` | Non-maximum Suppression | Intermediate | 추가/보강 계획 |
| `cv.map` | AP·mAP | Intermediate | 추가/보강 계획 |
| `cv.yolo` | YOLO Detection·Segmentation | Intermediate | 추가/보강 계획 |
| `cv.small` | Small Object Detection | Intermediate | 추가/보강 계획 |
| `cv.unet` | U-Net | Intermediate | [기존 절](../notes/tasks.html#unet_architecture) |
| `cv.sam` | SAM | Intermediate | 추가/보강 계획 |
| `cv.sam2` | SAM2 Video Segmentation | Intermediate | 추가/보강 계획 |
| `cv.grounding` | Grounding DINO | Intermediate | 추가/보강 계획 |

## PART 06 — Transformer & Foundation Models

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `tr.token` | Token·Embedding | Advanced | [기존 절](../notes/vit.html#tokens) |
| `tr.position` | Positional Encoding | Advanced | 추가/보강 계획 |
| `tr.qkv` | Query·Key·Value | Advanced | [기존 절](../notes/vit.html#attention) |
| `tr.attention` | Self-attention | Advanced | [기존 절](../notes/vit.html#attention) |
| `tr.multi` | Multi-head Attention | Advanced | 추가/보강 계획 |
| `tr.encoder` | Transformer Encoder | Advanced | [기존 절](../notes/vit.html#encoder) |
| `tr.vit` | Vision Transformer | Advanced | [기존 절](../notes/vit.html#patches) |
| `tr.ssl` | Self-supervised·Contrastive Learning | Advanced | 추가/보강 계획 |
| `tr.dino` | DINO·Teacher–Student | Advanced | 추가/보강 계획 |
| `tr.dinov2` | DINOv2 | Advanced | 추가/보강 계획 |
| `tr.clip` | CLIP | Advanced | 추가/보강 계획 |
| `tr.foundation` | Foundation Model | Advanced | 추가/보강 계획 |
| `tr.open` | Open-vocabulary Recognition | Advanced | 추가/보강 계획 |
| `tr.relative` | Relative Position Bias | Advanced | 추가/보강 계획 |

## PART 07 — Anomaly Detection

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `an.outlier` | Outlier·Novelty Detection | Advanced | [기존 절](../notes/patchcore.html#problem) |
| `an.one` | One-class Learning | Advanced | 추가/보강 계획 |
| `an.recon` | Reconstruction-based Detection | Advanced | 추가/보강 계획 |
| `an.feature` | Feature-based Detection | Advanced | 추가/보강 계획 |
| `an.embedding` | Patch Embedding | Advanced | 추가/보강 계획 |
| `an.nearest` | Nearest Neighbor | Advanced | [기존 절](../notes/patchcore.html#score) |
| `an.memory` | Memory Bank | Advanced | [기존 절](../notes/patchcore.html#memory) |
| `an.coreset` | Coreset Sampling | Advanced | 추가/보강 계획 |
| `an.ann` | Approximate Nearest Neighbor | Advanced | 추가/보강 계획 |
| `an.patchcore` | PatchCore | Advanced | [기존 절](../notes/patchcore.html#pipeline) |
| `an.padim` | PaDiM | Advanced | 추가/보강 계획 |
| `an.spade` | SPADE | Advanced | 추가/보강 계획 |
| `an.stfpm` | STFPM | Advanced | 추가/보강 계획 |
| `an.efficientad` | EfficientAD | Advanced | 추가/보강 계획 |
| `an.svdd` | Deep SVDD | Advanced | 추가/보강 계획 |
| `an.ae` | Autoencoder·Reverse Distillation | Advanced | 추가/보강 계획 |
| `an.score` | Anomaly Score·Heatmap | Advanced | 추가/보강 계획 |
| `an.threshold` | Threshold Calibration·Domain Shift | Advanced | 추가/보강 계획 |

## PART 08 — Video AI & Temporal Models

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `video.frame` | Frame·FPS·Timestamp | Intermediate | 추가/보강 계획 |
| `video.sample` | Sampling·Temporal Window | Intermediate | 추가/보강 계획 |
| `video.class` | Video Classification | Intermediate | 추가/보강 계획 |
| `video.rnn` | RNN·LSTM·GRU | Intermediate | 추가/보강 계획 |
| `video.temporal` | Temporal Transformer | Intermediate | 추가/보강 계획 |
| `video.cnn3d` | 3D CNN | Intermediate | 추가/보강 계획 |
| `video.mae` | VideoMAE | Intermediate | 추가/보강 계획 |
| `video.flow` | Optical Flow | Intermediate | 추가/보강 계획 |
| `video.track` | Object Tracking | Intermediate | 추가/보강 계획 |
| `video.aggregate` | Temporal Aggregation | Intermediate | 추가/보강 계획 |
| `video.persist` | Persistence·Hysteresis | Intermediate | 추가/보강 계획 |
| `video.anomaly` | Video Anomaly Detection | Intermediate | 추가/보강 계획 |

## PART 09 — Geometry & Mathematical Vision

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `geo.coords` | Coordinate Systems | Advanced | 추가/보강 계획 |
| `geo.affine` | Affine Transform | Advanced | 추가/보강 계획 |
| `geo.homo` | Perspective·Homography | Advanced | 추가/보강 계획 |
| `geo.calib` | Camera Calibration | Advanced | 추가/보강 계획 |
| `geo.circle` | Circle·Ellipse Geometry | Advanced | 추가/보강 계획 |
| `geo.ls` | Least Squares | Advanced | 추가/보강 계획 |
| `geo.eigen` | Eigenvalue·Eigenvector | Advanced | 추가/보강 계획 |
| `geo.svd` | SVD·PCA | Advanced | 추가/보강 계획 |
| `geo.ransac` | RANSAC | Advanced | 추가/보강 계획 |
| `geo.mad` | MAD·Robust Statistics | Advanced | 추가/보강 계획 |
| `geo.fit` | Robust Ellipse Fitting | Advanced | 추가/보강 계획 |
| `geo.subpixel` | Subpixel Edge | Advanced | 추가/보강 계획 |
| `geo.boundary` | Boundary Refinement | Advanced | 추가/보강 계획 |

## PART 10 — Statistics & Time-series

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `ts.series` | Time-series·Autocorrelation | Intermediate | 추가/보강 계획 |
| `ts.moving` | Moving Average·Median | Intermediate | 추가/보강 계획 |
| `ts.z` | Z-score·IQR·MAD | Intermediate | 추가/보강 계획 |
| `ts.threshold` | Static·Adaptive Threshold | Intermediate | 추가/보강 계획 |
| `ts.step` | Step Change Detection | Intermediate | 추가/보강 계획 |
| `ts.ewma` | EWMA | Intermediate | 추가/보강 계획 |
| `ts.cusum` | CUSUM | Intermediate | 추가/보강 계획 |
| `ts.ph` | Page–Hinkley | Intermediate | 추가/보강 계획 |
| `ts.changepoint` | Change-point Detection | Intermediate | 추가/보강 계획 |
| `ts.drift` | Concept Drift·Data Drift | Intermediate | 추가/보강 계획 |
| `ts.baseline` | Baseline Freeze·Online Update | Intermediate | 추가/보강 계획 |
| `ts.event` | Event-level Evaluation | Intermediate | 추가/보강 계획 |

## PART 11 — Dataset & Model Training

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `data.label` | Annotation·Taxonomy | Intermediate | 추가/보강 계획 |
| `data.format` | Box·Polygon·Mask Formats | Intermediate | 추가/보강 계획 |
| `data.collect` | Data Collection·Cleaning | Intermediate | 추가/보강 계획 |
| `data.auto` | Auto-labeling·QA | Intermediate | 추가/보강 계획 |
| `data.augment` | Augmentation·Train-only | Intermediate | 추가/보강 계획 |
| `data.imbalance` | Class Imbalance·Sampling | Intermediate | 추가/보강 계획 |
| `data.hard` | Hard Negative Mining | Intermediate | 추가/보강 계획 |
| `data.group` | Group Split·Leakage | Intermediate | [기존 절](../notes/training.html#split) |
| `data.kfold` | Group K-fold | Intermediate | 추가/보강 계획 |
| `data.temporal` | Temporal Split | Intermediate | 추가/보강 계획 |
| `data.version` | Dataset Versioning | Intermediate | 추가/보강 계획 |
| `data.experiment` | Experiment Tracking | Intermediate | 추가/보강 계획 |
| `data.repro` | Reproducibility·Seed | Intermediate | 추가/보강 계획 |
| `data.privacy` | Privacy·License | Intermediate | 추가/보강 계획 |

## PART 12 — Model Evaluation

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `eval.confusion` | Confusion Matrix | Intermediate | 추가/보강 계획 |
| `eval.prf` | Accuracy·Precision·Recall·F1 | Intermediate | [기존 절](../notes/training.html#metrics) |
| `eval.auc` | ROC-AUC·PR-AUC | Intermediate | 추가/보강 계획 |
| `eval.iou` | IoU·mAP | Intermediate | 추가/보강 계획 |
| `eval.boundary` | Boundary IoU·ASSD·HD95 | Intermediate | 추가/보강 계획 |
| `eval.reg` | MAE·MSE·RMSE | Intermediate | 추가/보강 계획 |
| `eval.threshold` | Threshold Analysis | Intermediate | 추가/보강 계획 |
| `eval.error` | Error Analysis | Intermediate | 추가/보강 계획 |
| `eval.ci` | Confidence Interval·Bootstrap | Intermediate | 추가/보강 계획 |
| `eval.effect` | Significance·Effect Size | Intermediate | 추가/보강 계획 |
| `eval.ablation` | Ablation Study | Intermediate | 추가/보강 계획 |
| `eval.ood` | OOD·Robustness Evaluation | Intermediate | 추가/보강 계획 |

## PART 13 — AI Deployment & MLOps

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `ops.pytorch` | PyTorch·CUDA | Advanced | 추가/보강 계획 |
| `ops.onnx` | ONNX·Opset | Advanced | 추가/보강 계획 |
| `ops.ort` | ONNX Runtime | Advanced | 추가/보강 계획 |
| `ops.trt` | TensorRT | Advanced | 추가/보강 계획 |
| `ops.triton` | Triton Inference Server | Advanced | 추가/보강 계획 |
| `ops.batch` | Batch Inference | Advanced | 추가/보강 계획 |
| `ops.gpu` | GPU Memory·Precision | Advanced | 추가/보강 계획 |
| `ops.latency` | Latency·Throughput | Advanced | 추가/보강 계획 |
| `ops.airflow` | Airflow·DAG | Advanced | 추가/보강 계획 |
| `ops.kafka` | Kafka | Advanced | 추가/보강 계획 |
| `ops.s3` | S3·MinIO | Advanced | 추가/보강 계획 |
| `ops.rtsp` | RTSP·FFmpeg | Advanced | 추가/보강 계획 |
| `ops.ntp` | Timestamp·NTP | Advanced | 추가/보강 계획 |
| `ops.monitor` | Logging·Monitoring | Advanced | 추가/보강 계획 |
| `ops.registry` | Model Registry·Versioning | Advanced | 추가/보강 계획 |
| `ops.cicd` | CI/CD·Regression | Advanced | 추가/보강 계획 |
| `ops.pipeline` | End-to-end Pipeline | Advanced | 추가/보강 계획 |

## PART 14 — Software Engineering for AI

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `eng.project` | Python Project Structure | Intermediate | 추가/보강 계획 |
| `eng.venv` | Virtual Environment | Intermediate | 추가/보강 계획 |
| `eng.jupyter` | Jupyter | Intermediate | 추가/보강 계획 |
| `eng.deps` | Dependency Management | Intermediate | 추가/보강 계획 |
| `eng.config` | Configuration·Secrets | Intermediate | 추가/보강 계획 |
| `eng.module` | Modular Design | Intermediate | 추가/보강 계획 |
| `eng.test` | Unit·Integration Tests | Intermediate | 추가/보강 계획 |
| `eng.git` | Git·GitHub | Intermediate | 추가/보강 계획 |
| `eng.review` | Code Review | Intermediate | 추가/보강 계획 |
| `eng.repro` | Reproducible Development | Intermediate | 추가/보강 계획 |
| `eng.agent` | Multi-Agent Workflow | Intermediate | 추가/보강 계획 |
| `eng.independent` | Independent Validation | Intermediate | 추가/보강 계획 |

## PART 15 — Advanced Research

| ID | 개념 | 수준 | 현재 대응 |
|---|---|---|---|
| `res.bayes` | Bayesian Inference | Research | [기존 절](../notes/prml.html#ch1) |
| `res.graph` | Graphical Models | Research | 추가/보강 계획 |
| `res.gmm` | Gaussian Mixture | Research | [기존 절](../notes/prml.html#ch9) |
| `res.em` | EM Algorithm | Research | [기존 절](../notes/prml.html#ch9) |
| `res.vi` | Variational Inference·ELBO | Research | [기존 절](../notes/prml.html#ch10) |
| `res.mcmc` | Monte Carlo·MCMC | Research | [기존 절](../notes/prml.html#ch11) |
| `res.hmm` | HMM | Research | [기존 절](../notes/prml.html#ch13) |
| `res.kalman` | Kalman Filter | Research | [기존 절](../notes/prml.html#ch13) |
| `res.domain` | Domain Adaptation | Research | 추가/보강 계획 |
| `res.continual` | Continual Learning | Research | 추가/보강 계획 |
| `res.ood` | OOD Detection | Research | 추가/보강 계획 |
| `res.quant` | Quantization | Research | 추가/보강 계획 |
| `res.prune` | Pruning | Research | 추가/보강 계획 |
| `res.distill` | Knowledge Distillation | Research | 추가/보강 계획 |
| `res.diffusion` | Diffusion Models | Research | 추가/보강 계획 |
| `res.research` | Research Reproduction | Research | 추가/보강 계획 |

## 개념 페이지 승격 기준

핵심 선수 개념이면서 독립된 수식·계산 실습·도식이 필요할 때만 별도 `note(...)`로 승격합니다. 기존 주제 원고의 하위 절만으로 설명 가능한 것은 기존 Anchor를 확장합니다. 신규 ID는 참조 존재·중복·순환 확인 후 등록합니다.
