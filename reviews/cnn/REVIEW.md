# CNN 1차 검토 · v1.0 적용

기준 vision_ai main: e2b2c2f377c1c97c3b6d010cb34c63988d0fca05.
브랜치 feat/cnn-v1-review. 사용자 선택으로 CNN·ResNet 챕터만 검토한다. 공개/Pages 설정이나 main 병합은 수행하지 않는다.

## 변경

- 별도 cnn-review.css를 CNN에만 로드. 로컬 Pretendard/일반 숫자/−1pt와 제목·본문·실습 간격을 적용한다. 긴 학습 문서이므로 기존 Scroll·목차·모바일 구조를 유지하며 전체를16:9슬라이드로 강제하지 않는다.
- 제목은 핵심 한글 명칭, 약어는 본문 첫 사용에서 뜻을 연결한다. 기존 자동 용어 주석과 중복되지 않도록 확인했다.
- 개요의 generic flow와 합성곱의 중복 단일 SVG를 제거. 해당 다중 패널 figure는 유지한다. CNN caption의 제작 메타 문구를 제거했다.
- stride/padding 정의를 실습 위 본문으로 옮겨 작은 실습 라벨을 길게 만들지 않는다.
- 브라우저에서 외부 MathJax가 로딩되지 않는 것을 발견해 CNN에만 로컬 MathJax3.2.2 SVG 조판을 연결했다. 공식 배포·LICENSE·SHA를 저장했다.

## 실제 검증

python scripts/build.py →9개 생성. python scripts/validate.py →11페이지/18 paper/68 reference SVG 통과. node --check assets/site.js 통과.

python reviews/cnn/verify.py → PC1600×950/1440×810/1366×768/1280×720, 기존사이트모바일390×844/430×900 총6조건 통과. 실제MathJax 로딩/수식오류0, 본문Pretendard 실제CDP, 자간, 이미지 정상로딩, 전체가로넘침0, 중복figure 제거를 검사한다. lazy이미지는 eager로 로드한 뒤 검사해 아직 로딩되지 않은 이미지를 결손으로 오판하지 않는다.

커널9위치를 모두 바꿔 출력[3,3,0]×3, 선택셀, 입력선택9칸을 확인했다. 채널파라미터896, bottleneck69632, 비교589824를 별도Python정수계산으로 확인했다. ResNet 덧셈/출력shape 설명은 기존 값을 유지했다.

[첫 화면](desktop.png) · [개요](overview.png) · [합성곱/실습](convolution.png) · [모바일](mobile.png) · [JSON](validation.json).

## 남은 검토

이는1차 수정이며 챕터 전체 과학적 검수 완료나 사용자 승인이 아니다. 기존 외부 paper SVG는 자체 서체를 유지한다. SVG 패널 내부 서체/영문라벨/정밀 Bounding Box와 모든 inline code 수식의 추가 조판 검토는 남아 있다. 외부 SVG까지 Pretendard로 검사했다고 주장하지 않는다. SVG실험조건과 기술적으로 필요한 한계는 출처/본문에 보존한다.

다른 챕터의 생성HTML은 변경되지 않았다. 각종 generated diagram은 전체빌드에서 생성되며 이PR에는 CNN이 직접 참조하는 새8개만 동봉한다. 공통 generator의 다른 주제내용은 바꾸지 않았다.

현재 Pages API는 legacy source이며 주소는 https://sh0427-han-private.github.io/vision_ai/ 이다. README의 예전sh0427-han주소와 다르다. 배포workflow는 GitHub Actions를 사용하므로 사용자가 Pages Source를Actions로 설정할지 확인해야 한다. 이PR을 main에 병합/배포하지 않았다.
