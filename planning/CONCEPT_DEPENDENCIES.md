# Concept Dependencies — 선수 관계와 DAG

정본: [concepts.v1.json](concepts.v1.json). 각 concept의 prerequisites는 직접 선행 개념 ID 목록이고 next_topics는 직접 후속 개념 ID 목록입니다. PART 번호와 위상 정렬 순서는 다릅니다. 입문 후 여러 경로로 분기할 수 있습니다.

## 개념 관계 설계 규칙

1. 직접 선행 관계는 정의·수식·계산을 이해하는 데 실제로 필요한 것만 둡니다. 권장 복습이나 관련 주제를 무조건 필수 선행 관계로 만들지 않습니다.
2. 직접 선수는 전이 관계를 모두 복사하지 않습니다. 예컨대 Convolution이 Matrix에서 시작하는 경로에 있다 해도 모든 조상 개념을 다시 연결하지 않습니다.
3. 여러 직접 선행 조건이 필요한 개념은 DAG의 합류 노드입니다. 예컨대 PatchCore는 k-NN과 Memory Bank 및 Coreset을 연결합니다.
4. 이미 있는 기존 HTML Anchor를 보존하며, 아직 작성되지 않은 concept는 클릭 가능한 새 페이지로 표시하지 않습니다.
5. 같은 말의 별칭은 중복 개념을 만들지 않습니다. Image filter kernel과 Neural Network weight kernel, Mean Absolute Error와 Median Absolute Deviation 등 다른 대상은 반드시 분리해 설명합니다.

## 핵심 학습 연쇄

### Image → CNN

m.scalar → m.vector → m.matrix → m.tensor → img.pixel → img.rgb → img.tensor → cnn.kernel → cnn.conv → cnn.stride → cnn.map → cnn.base

이것은 핵심 직관 경로의 한 부분입니다. 실제 그래프는 Convolution에 m.dot가 합류하며, CNN에 Activation 및 Pooling이 들어옵니다. 이미지의 축 순서는 HWC와 NCHW의 사용 문맥을 명시합니다.

### Gradient → Training

m.function → m.derivative → m.gradient → dl.gd → dl.sgd → dl.adam.

별도로 dl.perceptron → dl.mlp → dl.forward → dl.backprop으로 Gradient를 계산합니다. Backpropagation과 SGD/Adam의 파라미터 갱신 역할을 동일시하지 않습니다.

### Normal Features → PatchCore

an.outlier → an.one → an.feature → an.embedding → an.nearest → an.memory → an.coreset → an.patchcore → an.score → an.threshold.

실제 score의 패치/이미지 집계 및 reweighting은 논문·해당 구현 버전 확인 후 별도로 설명합니다.

### Segmentation → Boundary Refinement

cv.semantic + geo.circle + geo.ls + geo.mad + geo.subpixel → geo.boundary 경로. 타원 가정이 성립하지 않는 객체에 Ellipse Fitting을 만능 보정처럼 적용하지 않습니다. Boundary IoU·ASSD·HD95는 전체 IoU와 구분합니다.

### Video, Time-series, Serving

video.frame → video.sample → video.class → video.aggregate → video.persist.

ts.series → ts.moving → ts.threshold → ts.step → ts.baseline.

ops.pytorch → ops.onnx → ops.ort → ops.triton → ops.batch → ops.latency → ops.monitor.

## 그래프 데이터 계약

| 필드 | 의미 | 검증 |
|---|---|---|
| id | 영속 개념 ID | 유일성, 변경 최소화 |
| part | 카테고리 | 등록된 PART 참조 |
| level | Foundation / Basic / Intermediate / Advanced / Research | 선수 지식 수준과 일치 |
| prerequisites | 직접 선행 ID | 존재성, 중복, 자기 참조, 순환 없음 |
| next_topics | 직접 후속 ID | 역방향 참조 일치 |
| status | existing-section 또는 planned | 구현 현황의 과장 금지 |
| legacy_url | 기존 HTML/Anchor | 기존 파일·ID 검사 |

Builder 자체 구조 검사: 16 PART, 248 node, 직접 선수 edge 390개, 중복·없는 선수 0, Kahn 방식으로 248 node 모두 처리. 교육학적 의미론 검토·독립 Reviewer의 확인은 수행되지 않았습니다.

## 의미론적 리뷰 쟁점

- ml.softmax에 Sigmoid와 Softmax를 묶을지, 별도 단원으로 나누는 편이 나은지 검토합니다.
- dl.transfer의 Representation Learning/Transfer Learning은 독립 설명이 필요할 수 있습니다.
- an.ae의 Autoencoder와 Reverse Distillation은 근거와 목적이 달라 분리 후보입니다.
- cv.sam2는 PART 08의 video.frame을 선수로 가지므로 PART 05를 모두 읽는 순차 강제는 불가능합니다.
- 선행 관계가 독자의 실제 이해를 돕는 최소·충분 조건인지 별도 Reviewer가 검증해야 합니다.

검증 도구는 scripts/validate_concept_graph.py를 사용합니다. 자세한 단계는 [Roadmap](IMPLEMENTATION_ROADMAP.md)을 참고합니다.
