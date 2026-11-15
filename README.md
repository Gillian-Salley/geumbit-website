# 금빛흑염소 홈페이지

빌드 과정이 없는 HTML/CSS/JavaScript 정적 웹사이트입니다.

## 미리보기와 배포

- `index.html`을 브라우저에서 열어 확인할 수 있습니다.
- 정적 호스팅에 저장소 루트를 배포합니다. HTML과 에셋의 상대 경로를 유지하세요.
- 도메인이 정해지면 `python3 configure_domain.py https://실제도메인`으로 canonical, 공유 이미지 URL, 사이트맵과 robots.txt를 설정합니다.
- 네이버 예약 링크는 `index.html` 하단의 `NAVER_BOOKING_URL`에 입력합니다. 현재는 준비 중 안내가 표시됩니다.

## 구성

- `index.html`: 페이지, 스타일, 메뉴 및 인터랙션
- `assets/`: 사용 중인 사진, SVG, 외관 영상
- `favicon*`, `apple-touch-icon.png`, `icon-*.png`: 브라우저 및 홈 화면 아이콘
- `site.webmanifest`, `robots.txt`: 웹앱 및 검색엔진 설정
- `social-preview.jpg`: 도메인 설정 스크립트에서 사용하는 공유 이미지

작업 기록·미사용 원본·중복 이미지는 로컬에 보관하고 `.gitignore`로 제외합니다.
