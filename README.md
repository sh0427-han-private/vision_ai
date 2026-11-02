# Vision AI Notes

Vision AI 지식을 개념, 데이터 흐름, 수치 예시와 도식으로 정리하는 개인 학습 사이트.

- 사이트: https://sh0427-han-private.github.io/vision_ai/
- 저장소: https://github.com/sh0427-han-private/vision_ai
- 프로젝트 기준: [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md)

## 현재 자료

자료는 **논문 이름이 아니라 학습 주제**를 중심으로 관리합니다. 대표 논문은 해당 주제 안에서
문제 설정·구조·수식·실험 범위·한계를 설명하는 근거로 붙입니다.

1. 이미지·CNN
   - 이미지와 텐서: RGB, shape, 정규화, 밝기-픽셀 실험
   - CNN: 합성곱, 채널, stride/padding/dilation, receptive field
   - ResNet: CNN architecture의 확장으로 degradation, residual, projection, bottleneck 설명
2. Transformer·Attention
   - token, positional embedding, Q/K/V, multi-head attention
   - ViT 논문을 대표 사례로 patch embedding과 encoder 구조 연결
3. Vision Tasks·Segmentation
   - classification, detection, semantic/instance segmentation, IoU/Dice
   - U-Net 논문을 대표 사례로 encoder-decoder와 skip concatenate 설명
4. 학습·평가
   - grouped split, cross-validation, metric, threshold, leakage
5. Anomaly Detection
   - 정상 특징 기반 anomaly detection
   - PatchCore를 대표 사례로 memory bank, coreset, nearest-neighbor score 설명
6. 종합 이론
   - CS231n: 분류 → loss → optimization → CNN → transfer/modern vision
   - PRML: 확률 → 회귀/분류 → graphical/latent model → inference/sampling → sequential/ensemble

## 구조와 수정

`scripts/build.py`의 `NOTES`와 `scripts/*_note.py`에 각 문서의 설명과 출처가 들어 있습니다.
HTML은 빌드 결과도 함께 커밋해 브라우저에서 직접 열 수 있게 유지합니다.

```text
index.html             홈
notes/*.html           개별 학습 문서 (생성 결과)
assets/site.css        공통 스타일
assets/site.js         메뉴와 4개 계산 실험
scripts/build.py       핵심 콘텐츠와 정적 페이지 생성
scripts/cs231n_note.py CS231n 전체 정리 원고
scripts/prml_note.py   PRML 14장 전체 정리 원고
scripts/reference_notes.py 추가 원고 등록
scripts/validate.py    링크·ID·문서 기본 구조 검사
```

Python 3 표준 라이브러리만으로 빌드합니다. JavaScript도 외부 의존성이 없습니다.

```bash
python scripts/build.py
python scripts/validate.py
python -m http.server 8000
```

`http://localhost:8000`에서 확인합니다. 새 문서를 추가할 때 `note(...)`로 등록하고
내비게이션 이름과 홈 카드 도식을 함께 추가합니다. 상세 기준은 프로젝트 문서를 참고하세요.

## GitHub Pages

- 배포 주소: https://sh0427-han-private.github.io/vision_ai/
- 배포 설정: Settings → Pages → Build and deployment → Source → **GitHub Actions**
- 배포 workflow: [Deploy study notes](.github/workflows/pages.yml)

`main` 변경 시 빌드·정적 검증 후 Pages에 배포합니다. 수동 실행은 Actions → Deploy study notes → Run workflow에서 `main`을 선택합니다. PR에서는 검증만 하고 배포하지 않으므로, 초안 PR의 수정 화면은 아직 공개 사이트에 반영되지 않습니다.

Actions 실행 결과의 `validate`와 `deploy`가 모두 성공했는지 확인하고, Settings → Pages의 게시 주소로 접속합니다. Source 설정을 바꾼 사실만으로 새 배포 실행이 성공한 것으로 보지는 않습니다. 커스텀 도메인 없이 위 기본 주소를 사용합니다.

저장소 소유 계정은 `sh0427-han-private`입니다. 도메인/경로를 변경할 때는 이 README, PROJECT_CONTEXT, TODO의 주소와 `scripts/build.py`의 저장소 링크를 함께 수정하고 빌드합니다.

## 출처와 예시

각 문서 하단에 논문과 공식 문서 링크를 적었습니다. SVG 구조도는 설명을 위해 직접
재구성한 자료이며 원문 figure를 복사하지 않았습니다. 인터랙티브 실험은 학습용 숫자를
사용하며 실제 모델을 실행하거나 실제 공정 성능을 표시하지 않습니다.
