# VISION-AI-P4-VERTICAL-SLICE — R1 Follow-up Plan

- Revision: R1 / 2026-11-05 (KST)
- Kind: REPO_TARGET; owner/repo: sh0427-han-private/vision_ai
- Status at planning: PLANNED / BUILDER NOT_STARTED; reviewer R0=BLOCKED; R1 not implemented or reviewed
- Reused Task: VISION-AI-P4-VERTICAL-SLICE; this is not a new P5 task
- Frozen **code baseline**: main@2024db2b91e0fe9137fdd527357046f173cb0a4d
- Plan/Builder branch: docs/vision-ai-p4-r1-main-20261105 (created directly from the baseline)
- Historical P4 R0: aa73e714191e27aa34adabc8934a02a08f709daa → 0a2a1e1ec7d753d6ed0877a8bdcbfaa360704d97
- Historical PRs: [#37](https://github.com/sh0427-han-private/vision_ai/pull/37) merged; [#38](https://github.com/sh0427-han-private/vision_ai/pull/38) still Draft/Open/Unmerged, branch behind the current main
- Other PRs: #35 and #36 were separately open/unmerged at planning; do not absorb their unrelated changes
- Previous live Pages deployment: [run 41575560115](https://github.com/sh0427-han-private/vision_ai/actions/runs/41575560115), success for main@2024db2 (historical execution, not R1 test)
- Central pointer group: [agent-workflow-control/docs/tasks/vision_ai](https://github.com/sh0427-han/agent-workflow-control/tree/main/docs/tasks/vision_ai)
- Evidence destination: docs/tasks/vision-ai-p4-vertical-slice/result.md on implementation branch and a new Draft PR conversation/CI; central Result is only a summary
- **Do not put a future Plan Commit SHA in this file.** The handoff uses the real commit SHA of this file after saving.

## 1. User decision / permission boundary

On 2026-11-05 the user explicitly instructed the Planner: **“main기준으로 계속 진행해줘. 그리고 작업 이어서 진행할수있게 해보자.”** This authorizes the current main as the starting code baseline for the next P4 follow-up and permits a safe implementation planning handoff. It does **not** retrospectively prove prior Merge/Pages approval, declare R0 PASS, or grant a new main Merge/Pages deployment.

The P4 R0 independent Reviewer verdict was BLOCKED. The original governance issue involved main already containing P4 R0 and a successful deployment even though PR #38 remained Draft. For R1, continue from the user-selected current main; keep those historical facts and the R0 verdict, but do not force an unnecessary rollback or block planning on retrospective approval. User acceptance of P4 R1 remains pending.

No code changes have yet been performed under R1. Planner may write this plan to the feature branch; Builder performs implementation and self-validation. Independent technical review was already specified for this P4 task and is preserved for the R1 changed HEAD.

## 2. Read First (priority, frozen baseline)

1. PROJECT_CONTEXT.md — subject area, educational writing, browser/accessibility, current conflicting navigation contract; README.md — build contract and Pages
2. planning/IMPLEMENTATION_ROADMAP.md and planning/CONTENT_DESIGN.md — P4 target, 16 prerequisite closure, existing links, mandatory QA, retained decisions
3. planning/SEMANTIC_AUDIT.md and planning/concepts.v1.json — R0/R1/R2 historical snapshots, current coverage, immutable concept graph
4. scripts/foundations_note.py — code(source, output) renderer; Shape and GELU output strings; generated notes/shape.html, notes/cnn.html, notes/function.html
5. scripts/build.py, scripts/validate.py, scripts/validate_concept_graph.py, scripts/p4_examples.py, scripts/test_p4_examples.py, scripts/p4_browser.mjs, .github/workflows/p4-browser.yml, .github/workflows/p4-build.yml, .github/workflows/concept-graph.yml, .github/workflows/pages.yml
6. PR #38 Builder report and Reviewer R0 BLOCKED handoff supplied by user; PR #37 R2 record and current main→P4 ancestry

There is no root AGENTS.md and no separate prior docs/tasks Plan or Result in the inspected main tree. Do not create AGENTS.md merely to satisfy a template. Re-check remote main/branch HEAD, PR state, and any working-tree/user changes before editing; GitHub connector cannot inspect an unrelated local checkout's dirty working tree, so preserve any detected local changes.

## 3. Scope, data, and interfaces

### Fixed invariants (must not alter)

- Graph: 16 PART; 263 stable concept IDs; 390 direct prerequisite edges and matching next_topics, DAG and P4 required closure (16)
- Current P4 coverage: existing-section=53, needs-expansion=19, planned=191; retain 63 original legacy mappings and 9 P4 mappings (72 total)
- Original 8 authored notes, 70 original Section/Anchor IDs, plus the P4 CNN kernel and pooling additions
- Seven foundation pages: scalar, vector, matrix, tensor, shape, dot-product, function; all valid deep links
- ResNet/U-Net redirect URLs; existing four JS lab interactions; calculations, dtype, axes, mathematical outputs, and fixed-computation-versus-model-training distinction
- Existing CSS and builder note()/section() API, Python standard-library site build, generated HTML committed with source
- No modification to vision_ai_lecture, design-template-library, or PR #35/#36 changes.

### R1-DEF-02 — current navigation and audit text

**Observed evidence:**
- PROJECT_CONTEXT.md lines 107–113 still describe semiconductor/AI/Vision tabs as the current UI, while the P4 section declares only AI/Vision tabs with legacy ?topic=semiconductor → overview fallback.
- SEMANTIC_AUDIT.md heading “R2 현행” and historical paragraphs (including lines near 3, 43, 81, 99) still use present-tense R2 coverage 42/21/200 or reviewer PENDING, while P4 main Graph is 53/19/191.

**Required change:**
- Make PROJECT_CONTEXT.md describe current **AI / Vision AI** tabs and legacy semiconductor query fallback, removing the contradictory active-tab claim. Preserve historical references where explicitly historical.
- Make SEMANTIC_AUDIT.md distinguish historical R0 (260/411), R1 (263/394), R2 (263/390; coverage 42/21/200) from **current P4 main** (263/390; coverage 53/19/191). Retain original historical evidence and defect rationale. P4 Reviewer R0 remains BLOCKED, not PASS; P4 implemented/deployed is not equivalent to reviewed/accepted.
- Inspect related current-status claims in planning/IMPLEMENTATION_ROADMAP.md and README.md; correct only stale present-tense claims materially contradicted by current main. Keep earlier stages clearly historical and do not bulk rewrite the roadmap.
- Graph marker: preserve the exact current 16/263/390/53/19/191 values where the validator expects it.

**Acceptance:** No current-state contradiction between docs, current UI, and graph; past snapshots still clearly traceable.

### R1-DEF-03 — Python example stdout accuracy

**Observed evidence:** scripts/foundations_note.py code(source, output) currently inserts the escaped output inside a single inline HTML code node; the Shape and GELU examples use a “ / ” separator even though each Python example executes two separate print() calls.

**Required precise output:**

Shape:
~~~text
(3, 2, 3)
[0, 3, 6] 18
~~~

GELU:
~~~text
[0.0, 0.5, 3]
0.3457
~~~

- Change only the two expected output arguments and the shared display helper as needed to render newlines faithfully (e.g. safe escaped code block or explicit line-break markup). Do not turn escaped output text into HTML injection.
- Preserve one-line outputs in the other foundation examples and the source code block formatting.
- Add or extend a focused test comparing actual independently executed Python stdout to the displayed rows/values and generated HTML, in addition to existing numeric unit tests.
- Rebuild generated HTML and include notes/shape.html and notes/cnn.html changes.

**Acceptance:** Exact row count, ordering and text of outputs match the Python stdout in 3.12-compatible standard Python environments and in actual browser display.

### R1-VIS-01 — 390px Function equation legibility (LOW)

- Reproduce in a real 390px browser (notes/function.html); inspect the initial viewport, actual MathJax CHTML equation, and any internal horizontal scroll.
- Prefer a mathematically correct line break within authored TeX; if unsuitable, ensure explicit readable swipe cue and contained horizontal scroll, while preventing full page overflow.
- Keep desktop 1440px visual regression, font contrast and keyboard accessibility.
- If visual evidence shows the current rendering already satisfies legibility, report evidence and leave code unchanged rather than making cosmetic changes for their own sake.

### Changes permitted only as direct consequences

- scripts/foundations_note.py; affected generated notes/shape.html, notes/cnn.html and optionally notes/function.html
- PROJECT_CONTEXT.md, planning/SEMANTIC_AUDIT.md, only necessary related current-state passages in planning/IMPLEMENTATION_ROADMAP.md and README.md
- focused tests / scripts/p4_browser.mjs only if needed for the exact defects; minimal styles only if VIS-01 actually needs them
- docs/tasks/vision-ai-p4-vertical-slice/result.md to be authored by Builder
- No graph structure/status changes, no new course pages, no broad refactor, no workflow/platform rewrite.

## 4. Builder execution sequence

1. Confirm branch and code ancestry: the Planner plan branch must have an immutable Plan Commit; compare the source against main@2024db2 and re-check main for concurrent changes. If source diverged materially, halt destructive operations and report.
2. Record exact existing output, docs sentences, and 390px function screenshot as pre-change evidence.
3. Apply R1-DEF-02 minimal documentation corrections and verify current/historical numbers against actual graph.
4. Apply R1-DEF-03 stdout display and small focused tests; rebuild and inspect source + generated HTML diffs.
5. Investigate R1-VIS-01 in actual desktop/mobile Chromium, applying a minimal adjustment only if necessary.
6. Run all mandatory static/numeric/browser regressions and collect URLs/screenshots/logs tied to **the new R1 HEAD**, not the old R0 SHA.
7. Commit source + generated files to the P4-R1 branch; create a **new Draft PR against main**, if the connector/Builder has permission. Keep PR #38 untouched pending separate bookkeeping decision. Do not merge or deploy.
8. Publish Builder Result in the same task group and prepare the exact HEAD/diff for the separate Independent Reviewer R1 review.

## 5. Validation (required unless explicitly not applicable)

### Static / numeric
~~~bash
python3 scripts/build.py
python3 scripts/validate.py
python3 scripts/validate_concept_graph.py
python3 -m unittest discover -s scripts -p test_validate_concept_graph.py -v
python3 -m unittest discover -s scripts -p test_p4_examples.py -v
node --check assets/site.js
~~~

Additionally, independently compare R1 graph contents to main@2024db2 to assert identical ID/order/PART, prerequisites, next_topics, status, legacy mappings and 16-item P4 closure. Recalculate 16/263/390 and 53/19/191. Compare all original 70 anchors, 63 mappings, two redirect destinations, and the pre-existing four lab source/behavior contracts.

Generated HTML must match a fresh build; run a second build and verify no unintended diff. It is important that .github/workflows/p4-build.yml has a **push trigger pinned to the old feat/p4-foundations-20261103 branch**: it will not run on the new branch. The Builder must perform deterministic-build verification explicitly; do not claim that legacy workflow tested this branch.

### Browser / CI
- Run actual 1440px and 390px Chromium against the new branch via PR workflow and/or an equivalent direct test environment. Use the existing scripts/p4_browser.mjs, extend minimally for visual/output assertions where useful.
- Visually check Function equation, Shape and CNN GELU output blocks; verify pages not blank, MathJax rendered, no accidental page-level horizontal overflow.
- Confirm all seven foundation pages, Pixel/CNN links, AI/Vision navigation and semiconductor legacy fallback, sidebar/Escape and all four existing JavaScript numeric interactions, legacy redirects.
- Inspect Graph CI, Site PR CI and browser workflow conclusions for **the exact new R1 SHA**. New PR Site deploy should be skipped. If CI does not trigger due to path filters, report and run the corresponding required commands via supported workflow/manual execution; do not invent PASS.
- Include screenshot/artifact URLs and which viewports and URLs were actually inspected. Site source checks alone do not establish mobile visual PASS.

### Required acceptance
- DEF-02 current/historical docs consistent with real main/Graph
- DEF-03 expected output visibly 2 lines and values exactly correct in both examples
- VIS-01 mobile legible or documented already-correct with visual evidence; no regression
- All invariants retained and required tests/CI/browser verification passed
- New HEAD and diff documented, separate reviewer given the actual changed snapshot.

## 6. Existing reviewer and revision handling

Historical P4 R0 Reviewer verdict: **BLOCKED**, not PASS. R1 is the first follow-up modification cycle; do not count it as P4 R0 pass or reset earlier unsuccessful fixes. There are no observed R1 modification attempts yet; Builder must record actual attempts/failures under the project self-fix cap (maximum 3 fixes for one unresolved defect after initial implementation) and report a blocker if mandatory checks cannot be run.

The independent P4 review was explicitly part of the original task. Preserve it for R1; it is not a global extra Reviewer required on unrelated work. Reviewer must inspect the new R1 HEAD and full main-based diff, not automatically reuse R0 findings as current PASS.

## 7. Rights, evidence and end state

Allowed: work on the P4-R1 branch, modify only the scoped files, run tests/CI, push non-destructive commits on that branch, create Draft PR and document results.

Not allowed without separate authorization: main Merge, direct main Push, Pages deployment, release, Force Push, rewrite of shared history, PR #38 close/rebase/retarget, or changes to other repos (central status pointer updates are Planner-owned and separate).

Builder result path: docs/tasks/vision-ai-p4-vertical-slice/result.md. Include frozen Plan Commit URL/SHA, input main baseline, implementation HEAD, worktree/commit distinction, old/new outputs, exact tests, screenshots, Build/Graph/Browser CI, changes to generated files, preservation evidence, unresolved issues, user acceptance not yet assumed, and Reviewer R1 handoff. New Draft PR is recommended for review; if it cannot be created, report the exact branch/commit and limitation.

Target transition: PLANNED → BUILDING → READY_FOR_USER (only after required verification and applicable independent R1 review), then user acceptance; no silent Merge/deploy.
