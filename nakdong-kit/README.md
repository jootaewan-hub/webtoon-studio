# 낙동강을 헤엄쳐 나온 남자 — 제작 킷

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
data/cuts.json      컷 95개 (번호·장·크기·요약·화면·대사·수위 태그·썸네일 경로)
data/characters.json  인물 외형 고정값
data/style.json     시대·색·글꼴·말풍선 규칙
data/tracks.json    트랙별 스타일과 금지·수위 규칙
thumbs/             콘티 썸네일 (컷 번호.svg 자동 생성, 같은 이름 .png를 넣으면 그것을 우선 사용. v1 썸네일은 thumbs/v1/)
renders/<트랙>/     생성한 결과 이미지를 컷 번호.png로 넣으면 편집기에서 나란히 보입니다
tools/editor_ready.html  컷 편집기 (데이터 내장, 브라우저로 열기)
outputs/            kit.py가 만드는 트랙별 프롬프트
```

## 바로 쓰기

원본(source/), 컷 데이터(data/), 트랙별 프롬프트(outputs/), 편집기(tools/editor_ready.html)가 모두 채워진 상태입니다. 압축을 풀고 바로 쓰면 됩니다.

원본을 고친 뒤에는 터미널에서 킷 폴더로 이동해 다시 실행합니다.

```
python kit.py import      # source/*.md → data/cuts.json (컷 번호 체계가 바뀌면 --replace)
python kit.py validate    # 빠진 칸·썸네일 확인, 수위 태그 집계
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
- 썸네일을 바꾸려면 `thumbs/컷번호.png`를 같은 이름으로 덮어씁니다.

## ChatGPT에서 쓰는 법

트랙의 `_<트랙>_ALL.md`를 열어 컷 단위로 복사해 넣습니다. 인물 일관성을 위해 먼저 data/characters.json으로 인물별 기준 이미지를 만들고, 이후 컷마다 그 이미지를 함께 첨부하세요.

## Codex에서 쓰는 법

킷 폴더 전체를 저장소로 열면 Codex가 AGENTS.md를 읽고 같은 규칙으로 작업합니다.

## 지켜야 할 규칙 (모든 트랙 공통)

- 모든 얼굴은 창작된 가상 인물입니다. 실존 인물을 닮게 만들지 않습니다. 이 이야기는 실제 사건을 바탕으로 하므로 특히 중요합니다.
- 실제 병원·방송사 로고를 쓰지 않습니다.
- 성인 트랙도 수위 상한은 콘티와 같습니다. 정사 장면은 실루엣·역광·손·반지·소품으로만 암시합니다.
- 폭력은 집중선과 효과음으로, 투신은 남겨진 소품과 이후 장면으로만 처리합니다.
