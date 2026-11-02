# Content Design — 기존 정적 빌더 확장 규칙

기준: [PROJECT_CONTEXT.md](../PROJECT_CONTEXT.md), [기존 원고 조사](EXISTING_CONTENT_AUDIT.md). 신규 웹 프레임워크 없이 scripts/build.py의 note/section 함수를 우선 재사용합니다.

## 1. 각 개념의 설명 순서

Why (필요성) → Intuition (직관적 Figure) → Definition (정의/기호) → Mechanism (입력→계산→출력) → Mathematics (수식/차원) → Example (손으로 계산) → Implementation (Python) → Application (일반 활용) → Limitations (한계) → Related (선행·후속/출처).

전 항목을 기초 용어에 강제하지 않습니다. 논문/연구 주제는 원문 문제 설정, 제안의 실제 차별점, 실험 조건, 보고된 결과, 구현과의 차이를 추가합니다.

## 2. 정확한 수식과 shape 표기

- HWC [224,224,3]과 NCHW [B,3,224,224]는 축 순서가 달라 reshape만으로 변경할 수 없습니다. transpose/permute 같은 실제 축 교환이 필요합니다.
- PyTorch Conv2d의 공간 크기는 H_out = floor((H + 2P − D(K−1) − 1)/S + 1). H=5,K=3,P=0,S=1,D=1이면 H_out=3입니다.
- CNN에서 보통 Convolution이라고 부르는 것은 필터를 뒤집지 않는 Cross-correlation입니다.
- 예: [B,3,224,224] 입력, [32,3,3,3] Conv weight, stride=1/padding=1, groups=1, bias=True라면 출력은 [B,32,224,224], 파라미터는 32×3×3×3+32=896개입니다.
- 학습은 θ_(t+1)=θ_t−η∇L(θ_t)처럼 Gradient 계산과 파라미터 갱신의 역할을 분리합니다.
- 분류 지표에서는 분모 0 처리, Video 지표에서는 frame-level vs event-level, Segmentation에서는 객체 전체와 Boundary 지표의 정의역을 명확히 표시합니다.

## 3. 기존 웹 UI 재사용

assets/site.js의 4개 실습(밝기, Conv Kernel 위치, ViT Patch Size, Threshold/Confusion Metrics)을 유지합니다. 입력·강조 Matrix·중간 계산·최종 결과는 하나의 데이터에서 계산하고 서로 일치해야 합니다. 단순 슬라이더 장식은 Interactive로 승인하지 않습니다.

Python 구현은 경로/파라미터를 상단 설정으로 관리하고 출력 type/shape를 검증합니다. 고정 필터·합성 데이터 실습을 실제 GPU 학습 결과로 포장하지 않습니다. 데이터 누수, Train/Val/Test, dtype/channel/shape 계약을 지킵니다.

## 4. Figure 자산 선택

| 설명 대상 | 우선 수단 | 필수 검증 |
|---|---|---|
| 실제 사과·채널·조명 | 기존 WebP / 같은 Raster에서 유도 | 동일 위치의 R/G/B 값 |
| 행렬·커널·Shape | SVG·HTML Table | 선택 범위·곱셈·출력 수치 |
| Residual/U-Net | Branch Architecture SVG | add vs concatenate와 Shape |
| Loss/ROC/Trend | SVG Plot | 축·수치·단위·범례 |
| 모델 비교 | 동일 조건 데이터 | 학습 조건·지표·출처·버전 |

Paper Figure를 인용하거나 재구성하면 원본 논문/자료 링크를 표시합니다. 숫자 없는 장식적 도형으로 정확한 기술 개념을 대체하지 않습니다.

## 5. 소스와 생성 페이지 운영

새 개념을 기존 Section에 보강할지 독립 note로 승격할지 결정합니다. 대형 원고만 별도 scripts/*_note.py 모듈로 분리하고 registry 등록은 기존 reference_notes.py 패턴을 따릅니다.

build.py의 TOPIC_LABELS/nav/render와 assets/site.js의 topic_copy/data-topic-panel/data-topic-nav를 함께 변경해야 홈의 반도체 항목을 안전하게 제외할 수 있습니다. index.html과 notes/*.html은 build.py 산출물이므로 변경 시 소스·생성본을 같이 관리합니다.

기존 notes/resnet.html → cnn.html#resnet_problem, notes/unet.html → tasks.html#unet_architecture 리다이렉트, 모든 기존 Topic Anchor, CS231n/PRML 링크를 보존합니다. index.html?topic=semiconductor는 overview로 fallback하며 외부 Memory Book/Process Book 주소를 문서 아카이브에는 기록할 수 있지만 AI 메뉴에서는 제거합니다.

과거 저장소 주소는 README.md/PROJECT_CONTEXT.md/TODO.md/빌더/생성 HTML에 있으나 이미 PR #36이 열려 있으므로 해당 PR 상태를 재조회한 뒤 충돌 없이 변경합니다. 확인하지 못한 GitHub Pages URL을 추정하여 적지 않습니다.

## 6. 검증 기준

python scripts/build.py, python scripts/validate.py, python scripts/validate_concept_graph.py, node --check assets/site.js 실행을 기본으로 합니다. Browser에서 Desktop/Mobile 수식·Figure·스크롤·키보드·동작·숨김 패널을 검증합니다. 단순 소스 검사만 수행했다면 실제 렌더링 PASS로 표시하지 않습니다.

독립 Reviewer는 수학 수치·계산 단계·Shape·출처·중복·누수·레거시 URL 호환·시각적 깨짐을 직접 확인합니다. 미실행 검사는 미검증으로 기록합니다.
