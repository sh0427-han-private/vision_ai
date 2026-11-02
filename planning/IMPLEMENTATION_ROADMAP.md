# Implementation Roadmap — 단계별 구현 및 검증

## 프로젝트 경계

작업 저장소: [sh0427-han-private/vision_ai](https://github.com/sh0427-han-private/vision_ai). 참고 저장소는 design-template-library이며 읽기 전용입니다. vision_ai_lecture는 별도 강의 프로젝트로, 이 브랜치에서 변경하지 않습니다.

기준 main SHA: e2b2c2f377c1c97c3b6d010cb34c63988d0fca05. 원본 페이지·기존 URL·수식·디자인을 보존합니다. 별도 승인 없이 main merge 및 Pages deploy를 수행하지 않습니다.

## 단계

| Phase | 작업 | 완료 조건 | 이번 설계 브랜치 상태 |
|---|---|---|---|
| P1 Audit | Python 빌더·70개 Section·JS/CSS·Workflow·Legacy URL 및 반도체 메뉴 조사 | 누락 없이 기존 자산 분류 | 인벤토리 작성, 독립 리뷰 대기 |
| P2 Curriculum | PART 00–15, 248개 후보 개념, 선수/후속 DAG, 여러 학습 경로 | 그래프 검사 + 의미론적 선수 검수 | 구조 자체 검사 완료, 독립 의미 검토 대기 |
| P3 Design | 기존 note/section, Figure, URL/탐색 확장 설계 | 새 Framework 없음, 호환 계약 | 문서 작성, 독립 리뷰 대기 |
| P4 Vertical Slice | Scalar→Vector→Matrix→Tensor→Image Tensor→Convolution→Feature Map→CNN | 계산·Shape·Python·Figure·링크/브라우저 검사 | **미착수** |
| P5 Track Expansion | Foundation/ML/DL/CV/Anomaly/Video/Geometry/Time-series/MLOps/Research | Chapter별 근거와 독립 검수 | 미착수 |
| P6 Site QA | Build·Validator·JS·Browser·Pages/CI 확인 | 실행 근거·기존 URL 회귀 | 미착수 |

## P4 구현 단계

1. Scalar/Vector/Matrix/Tensor의 원고 중복을 CS231n·PRML에서 확인하고, 필요한 만큼만 추가합니다. 기존 구조에 없는 기초 Section이면 작은 주제별 모듈을 설계할 수 있습니다.
2. Image Tensor 설명은 기존 [pixels](../notes/pixels.html#layout)를 canonical로 유지하며 차원과 축 순서를 연결합니다.
3. Convolution은 기존 [CNN 수치 실습](../notes/cnn.html#convolution)을 재사용하여 고정 필터와 실제 학습되는 가중치를 구분하고 연산을 검산합니다.
4. Feature Map·Channel·CNN을 기존 [channels](../notes/cnn.html#channels) 및 [overview](../notes/cnn.html#overview)에 연결합니다.
5. 선수/후속 개념 링크를 추가하되 없는 페이지는 클릭 가능 URL로 렌더링하지 않습니다. 기존 resnet/unet redirect와 종합 PRML/CS231n Anchor를 유지합니다.
6. 반도체 탐색을 제거할 때 build.py TOPIC_LABELS/nav/render, assets/site.js topic_copy, index.html, README/PROJECT_CONTEXT 및 검증 스크립트를 일관되게 변경합니다. 외부 출처 링크는 탐색에서 제외하되 안전한 기록으로 보존합니다.
7. 빌드 시 변경된 원고와 생성된 HTML을 함께 관리합니다. 신규 의존성 도입은 원칙적으로 제외합니다.

## 실제 실행해야 할 검증 명령

~~~bash
python scripts/build.py
python scripts/validate.py
python scripts/validate_concept_graph.py
node --check assets/site.js
python -m http.server 8000
~~~

Browser에서는 Desktop 1440px/모바일 390px 기준으로 H1, Sidebar 열기·닫기, MathJax 수식, Figure overflow, 클릭/키보드 인터랙션, Slider 값·행렬·출력 동기화를 확인합니다. 단순 소스 검사만으로 시각 검증 성공이라고 쓰지 않습니다.

## 충돌·변경 관리

확인 당시 열려 있던 PR #35는 CNN 내용 검토, PR #36은 구 저장소 주소/Pages 안내 수정입니다. 이들이 main에 병합되면 먼저 현재 파일과 diff를 새로 읽고 P4 변경을 조정해야 합니다. 기존 페이지가 바뀌었다면 현재 최신 Anchor로 재검증합니다. Pages 실제 URL은 브라우저/배포 결과 확인 전 단정하지 않습니다.

## Reviewer 인계 — 독립 검토 대기

독립 Reviewer는 반드시 Builder와 다른 Agent 또는 분리된 세션에서, 실제 최신 브랜치·원본 코드·이 설계 문서·DAG를 다시 조회합니다.

- 원본 8개 주제 문서 및 70개 Section의 누락·중복 여부, 기존 링크 호환성 확인
- 선수 관계의 필수/선택 여부와 난이도 검수, 특히 ml.softmax 및 an.ae 등 복합 Concept 분할 검토
- 반도체 메뉴 제외와 기존 문서 보존 계획의 안전성 검토
- 새 URL이 없는 planned 개념을 완성/작동 상태로 노출하지 않는지 확인
- Python Graph Validator와 별도 cycle 검사를 **실제 실행**
- 수학·도식·기존 Interactive 설계에서 구현할 때 필요한 테스트 기준 확인

판정은 PASS / REVISE / BLOCKED. 결함은 심각도·파일·근거·영향·재작업 담당자를 적습니다. 재검토는 최대 3회. 별도 Reviewer가 없으면 PENDING이며 완료 승인으로 간주하지 않습니다.

## 승인 게이트

P1–3 설계의 독립 검토 전에는 그 설계를 검증된 정본처럼 취급하지 않습니다. P4 구현은 독립 검토/최신 main 대조 이후 진행하고, main merge/배포는 별도 승인 후 수행합니다.
