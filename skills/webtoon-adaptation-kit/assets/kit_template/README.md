# 웹툰 각색 제작 킷

소설·콘티·콘티 이미지를 Codex나 ChatGPT로 넘겨 네 가지 결과물을 만들기 위한 작업 폴더입니다.

| 트랙 | 결과물 | 코드 |
|---|---|---|
| 실사 웹툰 | 컷별 사실적 이미지 + 레터링 대본 | `webtoon_real` |
| 성인 웹툰 | 19세 드라마 톤 이미지 (수위 상한: 실루엣·암시) | `webtoon_adult` |
| 쇼츠 | 장별 9:16 영상 대본 (컷별 길이·카메라·자막) | `shorts` |
| 애니메이션 | 24fps 샷 리스트 (길이·카메라·레이어·립싱크) | `anim` |

## 폴더 구조

```
kit.py              변환 도구 (Python 3.9+, 외부 패키지 불필요. docx 명령만 node+docx 또는 pandoc 사용)
AGENTS.md           Codex가 읽는 작업 지침
source/             소설·콘티 원본 (.md 작업용, .docx 읽기·공유용)
data/cuts.json      컷 데이터 (번호·장·크기·요약·화면·대사·수위 태그·썸네일 경로)
data/characters.json  인물 외형 고정값 (처음엔 자리표시 견본 — 작품 값으로 바꿉니다)
data/style.json     시대·색·글꼴·말풍선 규칙 (처음엔 자리표시 견본)
data/tracks.json    트랙별 스타일과 금지·수위 규칙
data/flags.json     작품 고유의 수위 단서(기본 단서에 더하기·빼기)
thumbs/             콘티 썸네일 (컷 번호.png 또는 자동 생성 .svg)
renders/<트랙>/     생성한 결과 이미지를 컷 번호.png로 넣으면 편집기에서 나란히 보입니다
tools/editor_ready.html  컷 편집기 (데이터 내장, 브라우저로 열기)
outputs/            kit.py가 만드는 트랙별 프롬프트
```

## 실행 순서

source/에 novel.md, storyboard.md를 넣고, 썸네일을 thumbs/<컷번호>.png로 넣은 뒤 킷 폴더에서 실행합니다. 원본을 고친 뒤에도 같은 순서로 다시 실행합니다.

```
python kit.py import      # source/*.md → data/cuts.json (컷 번호 체계가 바뀌면 --replace)
python kit.py validate    # 빠진 칸·썸네일 확인, 수위 태그 집계, 설정 점검([주의])
python kit.py prompts --track all   # outputs/<트랙>/ 컷별 .md와 _ALL.md
python kit.py shorts-script         # 장별 쇼츠 러프컷 ffmpeg 스크립트
python kit.py thumbs-auto  # 샷·앵글·인물 칸으로 레이아웃 썸네일(SVG) 자동 생성
python kit.py board       # tools/board.html 썸네일 보드
python kit.py editor      # 편집기에 최신 데이터 내장
python kit.py docx        # source/*.md → source/*.docx (node+docx 또는 pandoc 필요)
```

## 편집 흐름

- `tools/editor_ready.html`을 브라우저로 엽니다.
- 컷을 고르고 화면·연출, 대사, 수위 태그, 트랙별 추가 지시를 고칩니다. 변경은 브라우저에 자동 저장됩니다.
- "이 컷 프롬프트 복사"로 ChatGPT에 바로 붙여 넣을 수 있습니다.
- 다 고쳤으면 "cuts.json 내려받기" 후 `python kit.py merge-edits 내려받은파일.json`, 그리고 `python kit.py prompts --track all`을 다시 실행합니다.
- 수위 태그와 트랙별 추가 지시는 다음 import 뒤에도 남습니다. 화면·연출·대사 같은 콘티 칸은 원본 md가 기준이라 다음 import 때 md 값으로 돌아갑니다(경고가 뜨고 이전 값은 data/edits_replaced.json에 남음). 오래 남길 수정은 source/storyboard.md에 하세요.
- 수위 태그가 자꾸 빠지거나 잘못 붙는 낱말이 있으면 data/flags.json에 더하거나(strong·weak) 뺍니다(remove).
- 썸네일을 바꾸려면 `thumbs/컷번호.png`를 같은 이름으로 덮어씁니다.

## ChatGPT에서 쓰는 법

트랙의 `_<트랙>_ALL.md`를 열어 컷 단위로 복사해 넣습니다. 인물 일관성을 위해 먼저 data/characters.json으로 인물별 기준 이미지를 만들고, 이후 컷마다 그 이미지를 함께 첨부하세요.

## Codex에서 쓰는 법

킷 폴더 전체를 저장소로 열면 Codex가 AGENTS.md를 읽고 같은 규칙으로 작업합니다.

## 지켜야 할 규칙 (모든 트랙 공통)

- 모든 얼굴은 창작된 가상 성인입니다. 실존 인물을 닮게 만들지 않습니다. 실화 기반 작품이면 특히 중요합니다.
- 실제 기관(병원·방송사·학교·회사 등)·브랜드 로고를 쓰지 않습니다.
- 성인 트랙도 수위 상한은 콘티와 같습니다. 정사 장면은 실루엣·역광·손·반지·소품으로만 암시합니다.
- 폭력은 집중선과 효과음으로, 투신은 남겨진 소품과 이후 장면으로만 처리합니다.
