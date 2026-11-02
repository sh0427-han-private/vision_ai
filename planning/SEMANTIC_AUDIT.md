# Semantic Audit — 선수 개념 의미론 정정 (2026-11-02)

> 대상: [Draft PR #37](https://github.com/sh0427-han-private/vision_ai/pull/37). 작성자 자체 설계 감사로서 **독립 Reviewer PASS가 아닙니다(PENDING)**. 원본 HTML/JS/CSS 학습 페이지는 수정하지 않았습니다.

## 범위 및 정량 결과

- 이전: 16 PART, 248 Concept, 390 prerequisite edge
- 현재: 16 PART, 260 Concept, 411 prerequisite edge
- 현재 커버리지: `existing-section` 42, `needs-expansion` 16, `planned` 202
- `existing-section`은 기존 절에 이미 대응, `needs-expansion`은 기존 절에 내용이 있으나 독립 학습 목표의 설명·예제 보강 필요, `planned`은 아직 확인된 기존 Anchor 없이 신규 작성 예정입니다. 이 중 어느 상태도 완성도 보증은 아닙니다.

## 주요 변경 결정

| 심각도 | 문제 | 수정 및 의도 |
|---|---|---|
| P0 | OOD 평가가 `an.threshold`를 통해 PatchCore 학습까지 요구 | `eval.ood`을 공통 Outlier/평가 개념으로 연결, `eval.robust` 분리. 특정 AD 알고리즘 의존 제거 |
| P0 | Grounding DINO가 CLIP을 필수로 요구 | `cv.detr` → `cv.dino_detr` → `cv.grounding` 연결. SSL의 `tr.dino`와 DINO-DETR을 명시적으로 구분 |
| P0 | 서로 다른 연산·방법 통합 | `m.chain`(Chain Rule), `ml.sigmoid`, `dl.repr`(Representation Learning), `an.reverse`(Reverse Distillation) 분리 |
| P0 | Transformer Encoder가 BatchNorm 필수 선수 | `dl.ln` 추가 후 `tr.encoder`가 LayerNorm을 참조하도록 수정 |
| P1 | `an.score`가 PatchCore만을 전제 | 일반 이상 점수·Heatmap으로 독립. Threshold도 특정 Calibration 모델 대신 검증 분할과 연결 |
| P1 | Kalman Filter가 HMM 필수 선수 | `res.state` State-space Models를 추가하고 HMM·Kalman을 분기 |
| P1 | 일반 Batch Inference가 Triton에 종속 | PyTorch 배치 추론을 일반 경로로 사용, ONNX/Triton은 선택 구현 |
| P1 | End-to-end Pipeline에 Kafka/S3/Triton 모두 필수 | 일반 프로젝트와 모니터링 개념으로 수정하고 서비스별 도구는 선택 적용 |
| P1 | STFPM과 EfficientAD의 잘못된 필수 체인 | Feature / Representation 기반으로 분기 |
| P1 | Self-supervised·Contrastive, Threshold·Domain Shift, OOD·Robustness 통합 | `tr.contrast`, `an.shift`, `eval.robust` 추가 |
| P1 | Learning Rate·Epoch·Batch가 단일 ID | `dl.lr` 및 `dl.epoch`로 분리 |
| P1 | 개념 수준을 PART별로 동일하게 일괄 분류 | 학습 난이도별로 Foundation/Basic/Intermediate/Advanced/Research 재분류 |
| P1 | PRML·CS231n에서 이미 일부 설명한 개념이 새 원고 계획으로만 표시 | 16개를 `needs-expansion`으로 분류하고 기존 Anchor 매핑 |
| P1 | 기존 원고 수정 시 Graph CI가 항상 실행되지 않음 | 원고 스크립트·생성 notes 변경을 트리거에 추가하고 페이지 재생성 후 Anchor 검사 |

## 참고 자료와 구분 원칙

- Caron et al., *Emerging Properties in Self-Supervised Vision Transformers*, ICCV 2021: https://openaccess.thecvf.com/content/ICCV2021/html/Caron_Emerging_Properties_in_Self-Supervised_Vision_Transformers_ICCV_2021_paper.html
- Zhang et al., *DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection*, ICLR 2023: https://arxiv.org/abs/2203.03605
- Liu et al., *Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection*, ECCV 2024: https://arxiv.org/abs/2303.05499

## 검증 및 남은 일

1. Graph 구조: 유일 ID, PART 멤버십, 직접 참조와 역참조의 대칭성, Kahn 위상 정렬을 재검사합니다. 단순 cycle-free는 의미론적 적합성 보장이 아닙니다.
2. `scripts/validate_concept_graph.py`에 지정된 필수·금지 선수 관계를 회귀 규칙으로 추가했습니다. 일반적 개념 타당성까지 전부 보증하지 않습니다.
3. 기존 실제 HTML Anchor와 원고 빌드는 CI에서 재확인하며, 16개 `needs-expansion`의 설명 깊이는 독립 Reviewer가 재판단해야 합니다.
4. 독립 Reviewer는 별도 Agent/세션에서 최신 PR Diff와 기본 브랜치를 비교하고 PASS/REVISE/BLOCKED를 판정합니다. 병합·배포는 하지 않습니다.
