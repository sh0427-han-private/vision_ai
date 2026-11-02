# Design Template Mapping — 참고 저장소는 읽기 전용

참고: [Design Template Library](https://github.com/sh0427-han/design-template-library), DESIGN_SYSTEM.md, TEMPLATE_CATALOG.md, docs/FIGURE_PRODUCTION_STANDARD.md, docs/DESIGN_COMPONENT_RECIPES.md.

실제 수정 대상은 오직 sh0427-han-private/vision_ai입니다. 기존 assets/site.css, note/section 문서 구조, 직접 작성한 WebP/SVG, 가독성 규칙이 우선입니다. 참고 템플릿의 고정 크기 슬라이드 레이아웃이나 전용 예제 수치를 그대로 복사하지 않습니다. 참고 저장소가 PC 중심이어도 현재 사이트는 모바일까지 검수해야 합니다.

| 패턴 | 적용 목표 | 기본 재사용 | 정확도 기준 |
|---|---|---|---|
| [Concept](https://github.com/sh0427-han/design-template-library/blob/main/templates/html/concept.html) | 이미지→RGB→픽셀·Tensor | 기존 pixels 원고·사과 WebP | 동일 픽셀/채널 위치·실제 계산 값 |
| [Process](https://github.com/sh0427-han/design-template-library/blob/main/templates/html/process.html) | 데이터 수집→전처리→모델→출력 | build.py flow | 입력/출력 및 독립 분기 정확성 |
| [Comparison](https://github.com/sh0427-han/design-template-library/blob/main/templates/html/comparison.html) | MAE/MSE, CNN/Transformer, Split 정책 | HTML table | 같은 데이터·축·조건으로 비교 |
| [Step-by-Step](https://github.com/sh0427-han/design-template-library/blob/main/templates/html/step-by-step.html) | 3×3 Kernel 수치 합산 | cnn.html#convolution | 입력 5×5, 출력 3×3 일치 |
| [Interactive](https://github.com/sh0427-han/design-template-library/blob/main/templates/html/interactive.html) | Kernel Position·Threshold·Window | site.js 4개 기존 실습 | 변경값→실제 재계산→DOM 출력 일치 |
| [Architecture](https://github.com/sh0427-han/design-template-library/blob/main/templates/html/architecture.html) | CNN Feature Stack·ResNet·U-Net | paper_figures.py | Add/Concat·Shape·채널·차원 |
| [Experiment](https://github.com/sh0427-han/design-template-library/blob/main/templates/html/experiment.html) | CUSUM/EWMA·성능 지표 비교 | SVG plot/table | 합성/실측/논문값 구분 |
| [Executive Summary](https://github.com/sh0427-han/design-template-library/blob/main/templates/html/executive-summary.html) | 학습 내용의 응용·한계 요약 | 기존 callout | 시각 강조 남용 금지 |

## 시각화 운영 지침

- HTML은 본문·Table·Control, SVG는 정확한 도형·축·Matrix, Canvas는 실제 Pixel 계산에 사용합니다. 값이 바뀌는 Figure는 하나의 데이터 계산을 기준으로 그립니다.
- 참조 #1의 특정 RGB Pixel/ROI 좌표, #4의 특수 Filter 값, #6의 장식 Stack 수는 각 레퍼런스만의 값입니다. vision_ai의 입력 데이터를 그대로 바꿔 사용하지 않습니다.
- 실제 영상/물체의 시각적 직관은 기존 WebP 또는 공개된 이미지 자산을 사용합니다. 단순 픽토그램으로 근거를 대신하지 않습니다.
- 문구·화살표·글자·캡션 충돌은 실제 폰트 로딩 후 Desktop/Mobile 렌더링으로 확인합니다.
- 커다란 템플릿 프레임을 페이지마다 추가하지 않습니다. 본문 안에 필요한 Figure만 삽입합니다.
- 논문 Figure를 변형하거나 일부 구성 참조 시 원본 논문/공식 URL 및 Adapted from 표기를 검토합니다.

## 초기 Vertical Slice 연결

Scalar/Vector/Matrix는 Concept/Step-by-Step; Tensor/Image Tensor는 기존 pixels.html#layout과 WebP; Kernel/Convolution은 cnn.html#convolution과 인터랙티브 계산; Feature Map/CNN은 cnn.html#channels 및 #overview와 Architecture 패턴을 권장합니다. 기존 데이터·계산과 새 템플릿이 다르면 기존의 기술적 정확성이 우선입니다.
