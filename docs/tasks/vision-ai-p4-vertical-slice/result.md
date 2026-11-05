# VISION-AI-P4-VERTICAL-SLICE — Builder Result (R1)

- Task: `VISION-AI-P4-VERTICAL-SLICE`; Cycle: **R1**; date: **2026-11-05 (KST)**
- Role / status: **Builder / BUILT_READY_FOR_REVIEW** — 독립 R1 Reviewer **PENDING**, 사용자 수용 **PENDING**
- Frozen Plan: [R1 plan@32acdcc995dc82672a26c272978e6fdfbb3007fb](https://github.com/sh0427-han-private/vision_ai/blob/32acdcc995dc82672a26c272978e6fdfbb3007fb/docs/tasks/vision-ai-p4-vertical-slice/plan.md)
- Frozen input main: `2024db2b91e0fe9137fdd527357046f173cb0a4d`; Builder 작업 시작 HEAD/Plan: `32acdcc995dc82672a26c272978e6fdfbb3007fb` (main에서 Plan 파일만 추가)
- Verified **implementation code HEAD**: `fc24bbdcfa81dfa99624d69fe81ec97c95fa2f89`; 이 Result 파일은 그 이후 별도 보고 Commit으로 추가. 최종 PR ref와 전체 파일 Diff는 [Draft PR #39](https://github.com/sh0427-han-private/vision_ai/pull/39/files)에서 확인하며, PR 대화의 제출 기록에 보고 Commit 최종 SHA를 명시한다.
- Branch: `docs/vision-ai-p4-r1-main-20261105` → base `main`; #38은 미변경 Draft/Open; #35/#36 변경 미포함
- GitHub connector 기반 별도 branch에만 일반 Commit/Push. 작업 대상에 대한 외부 로컬 dirty checkout은 조회하지 않았고, 기존 원격 ref를 `expected_sha`로 보호했다. Force push / main merge / Pages deploy 없음.

## 1. 확정 Plan 범위와 구현

### R1-DEF-02 — 문서 시점·탐색 계약

- `PROJECT_CONTEXT.md`: 현재 활성 **AI/Vision AI**만 안내; `?topic=semiconductor`는 Overview fallback, Memory/Process 외부 메뉴 비활성.
- `planning/SEMANTIC_AUDIT.md`: R0 `260/411`, R1 `263/394`, R2 `263/390` 및 R2 coverage `42/21/200`은 **과거 스냅샷**. 현행 P4/main은 `16 PART / 263 ID / 390 Edge / 53 existing-section / 19 needs-expansion / 191 planned`. R2 자체 감사 상태와 P4/R0 Reviewer의 **BLOCKED** 판정을 구분. Graph snapshot marker는 변경하지 않음.
- `planning/IMPLEMENTATION_ROADMAP.md`, `README.md`: P4/R0이 현재 main에 구현·배포된 이력과 #38 Draft/Open, 현 R1 main 기준, 신규 merge/deploy 금지를 정확히 표현. 과거 정책/설계 기록은 보존.

### R1-DEF-03 — stdout 정확성

- `scripts/foundations_note.py`의 `code(source, output)`: 여러 줄 stdout은 HTML-escaped `<pre><code>`로 표시, 1행 stdout의 기존 inline 서식은 유지. 출력이 HTML로 실행되지 않도록 `escape()` 유지.
- 두 출력 문자열과 생성 HTML `notes/shape.html`, `notes/cnn.html` 수정. 원본 source와 생성 결과가 새 코드의 빌드 출력과 일치함을 CI 테스트로 검증.

```text
Shape:
(3, 2, 3)
[0, 3, 6] 18

GELU:
[0.0, 0.5, 3]
0.3457
```

- `scripts/test_p4_examples.py`: 생성 HTML에서 2행 블록에 바로 붙은 Python 소스를 추출하고 실제 Python subprocess stdout과 문자열·행수 비교, XSS escaping·기존 1행 형식 검증. 초기 CI에서 테스트 regex가 과거 코드블록까지 포착하는 결함 발생 → **R1-DEF-03 수정 1회**로 HTML 코드 블록 경계를 제한한 뒤 재검증 PASS.

### R1-VIS-01 — 390px Function 수식

- 첫 실제 Chromium 측정(수정 전 코드 HEAD `0afe1fbd19bcd3d73208074c855e8e1eaba20340`): `notes/function.html`, viewport **390px**, equation clientWidth `349`, scrollWidth `473`, MathJax 컨테이너 폭 약 `424.7`; 페이지 전체 scrollWidth는 `390` (패널 내부만 가로 스크롤 필요).
- `scripts/build.py`의 `P4_FUNCTION` 수식을 동일 의미의 MathJax `aligned` 3행으로 분리하고 `notes/function.html` 재생성. **VIS-01 수정 1회**.
- 재검증: **390px equation clientWidth=349, scrollWidth=349, pageWidth=390**. 1440px에서 clientWidth/scrollWidth=959/959; 실제 MathJax CHTML 요소 확인. 브라우저 스크립트에 수식 패널 비오버플로 assertion과 캡처 추가.
- CSS/JS 디자인, 원래 `#function` 및 페이지 API는 변경하지 않음.

## 2. 보존 계약 — R2 및 현재 main과 직접 대조

- `planning/concepts.v1.json`의 **blob SHA 동일**(R1 main 기준); R2와 현재 Graph를 재파싱해 16 PART, 263 Stable ID와 순서 동일, 390 직접 prerequisite Edge, `next_topics`/PART 의미론 변화 **0** 확인.
- 현행 Coverage **53/19/191**, 총 연결 72개(기존 R2 legacy mapping 63개 **내용 그대로**, P4 mapping 9개 추가 이력). R2 기준 P4 필수 폐포 16개 동일.
- R2 원고 8개에서 기존 학습 Section **70개 + Sources Section 8개 = 78개**; 현행 원고 80개(과거 P4에서 추가한 CNN `kernel`, `pooling` 포함). R2 대비 삭제 Anchor **0**, 신규 P4 추가 2개 유지. R1의 CNN Section ID 목록은 current main과 순서까지 동일.
- `assets/site.js`, `assets/site.css`, 기존 `notes/pixels.html` 등 다른 원고, `notes/resnet.html`/`notes/unet.html` redirect, 네 가지 JavaScript lab 소스, `.github/workflows/*` 파일은 main baseline과 **blob SHA 동일**. 그 외의 새 수업 페이지/Graph는 수정하지 않음.

## 3. 실제 실행·검증 증거 — code HEAD `fc24bbdcfa81dfa99624d69fe81ec97c95fa2f89`

| 검사 | 실제 증거 / 판정 |
| --- | --- |
| Site PR CI | [run 41947694269](https://github.com/sh0427-han-private/vision_ai/actions/runs/41947694269) **SUCCESS**; `python3 scripts/build.py`, `scripts/validate.py`, `node --check assets/site.js`, `test_p4_examples.py` **11/11 PASS** |
| Graph CI | [run 41947694143](https://github.com/sh0427-han-private/vision_ai/actions/runs/41947694143) **SUCCESS**; 16/263/390, Coverage 53/19/191; Graph mutation unittest **13/13 PASS**, Numeric/build unittest **11/11 PASS** |
| Static page/figure/link | Validator `Validated 18 pages plus 18 paper and 68 reference SVGs.` |
| Deterministic HTML | 신규 테스트가 `scripts/build.py`를 **2회 추가 실행**, `index.html`+모든 `notes/*.html` fingerprint 원본과 두 번 모두 동일; Git `diff --exit-code` 성공 |
| P4 Chromium 1440 + 390 | [run 41947694108](https://github.com/sh0427-han-private/vision_ai/actions/runs/41947694108) **SUCCESS** / `BROWSER CHECKS ALL PASS 0`; 7 foundation URL, CNN/Pixel, MathJax CHTML, Kernel/Pooling, 출력 표시, 딥링크, 4개 JS labs, AI/Vision/semiconductor fallback 및 Back/Forward, 모바일 sidebar/Escape |
| Screenshot evidence | 위 Browser run의 `p4-desktop-mobile-screenshots` artifact ID `13379257667` (1440/390px 전체 페이지 + Function equation 및 Shape/GELU 출력 캡처 포함) |
| Pages deployment | Site PR workflow의 `deploy` job **SKIPPED** — R1 배포 없음 |

- 첫 CI 실패: 신규 stdout 정규식 과다 매칭(계산 함수/콘텐츠의 오류 아님). 원인 및 수정 후 Graph/Site/Browser 재실행 PASS. 검증 환경은 GitHub Actions 실제 runner; 외부 로컬 체크아웃으로 전체 repo CLI 테스트를 실행했다고 주장하지 않는다.
- `.github/workflows/p4-build.yml`의 push-trigger는 과거 `feat/p4-foundations-20261103`에만 설정되어 R1 브랜치에서 **미트리거**. 이를 PASS로 보고하지 않으며, 이번 실제 PR CI와 독립 2회 빌드 검증으로 필수 deterministic 조건 확인.
- 자동 Chromium이 수식을 실제 조판하고 픽셀 스크린샷을 아티팩트로 저장했으며, 수식 가로폭/패널/페이지 overflow와 인터랙션을 자동 검증했다. **이미지 픽셀을 사람이 직접 열어 수행하는 시각적 의미·미감 검수는 독립 Reviewer 단계의 확인 대상**으로 남긴다.

## 4. Reviewer 인계 및 후속 상태

- Reviewer 대상: **P4/R1, independent**. 이전 P4/R0 Reviewer verdict **BLOCKED**는 역사적으로 유지; R1 PASS는 아직 주장하지 않음.
- 기준: [frozen Plan](https://github.com/sh0427-han-private/vision_ai/blob/32acdcc995dc82672a26c272978e6fdfbb3007fb/docs/tasks/vision-ai-p4-vertical-slice/plan.md), `main@2024db2` → [Draft PR #39 전체 Diff](https://github.com/sh0427-han-private/vision_ai/pull/39/files), **code HEAD `fc24bbdcfa81dfa99624d69fe81ec97c95fa2f89`**, 이후 Result commit을 포함한 최종 PR HEAD는 제출 댓글 참고.
- 집중 확인: 현행/역사 문서 문장, 출력 source→stdout→generated HTML, MathJax 모바일 화면(수정 전후 수치 및 캡처), 브라우저 조작, Graph/Anchor/Mapping/Redirect 회귀, CI Test 및 deploy=skipped.
- 신규 main Merge·Pages deployment·PR #38 상태 변경·Force Push 없음. 사용자의 R1 수용, 별도 독립 Reviewer 판정 및 Merge/배포 승인 모두 **미실시**.
