---
name: webtoon-adaptation-kit
description: 소설을 웹툰 문법에 맞게 장면·동작 단위로 잘게 쪼갠 콘티로 만들고, 소설과 콘티(컷 번호·크기·샷·화면·대사 표)와 콘티 썸네일을 실사 웹툰, 성인(19세 드라마) 웹툰, 쇼츠(9:16), 애니메이션 샷 리스트로 옮기기 위한 제작 킷을 만들고 갱신하는 스킬. 소설·콘티 원본을 Markdown과 Word(docx)로 함께 저장하는 일도 포함한다. 사용자가 소설이나 콘티를 Codex·ChatGPT·이미지 생성 도구로 넘기려 할 때, 원본을 md·docx로 정리해 두려 할 때, 컷별 이미지 프롬프트·레터링 대본·쇼츠 대본·애니 샷 리스트를 원할 때, 콘티를 편집하기 쉬운 형태(JSON, 편집기)로 바꾸려 할 때, 콘티가 '웹소설에 그림만 붙인' 느낌이라 더 세분화하려 할 때, 웹툰을 쇼츠나 애니로 각색하려 할 때는 "킷"이라는 말이 없어도 반드시 이 스킬을 사용한다.
---

# 웹툰 각색 제작 킷

소설·콘티·콘티 이미지를 하나의 작업 폴더(킷)로 묶는다. 원본은 Markdown(작업용)과 Word(읽기·공유용)로 함께 보관하고, 컷 번호가 모든 파일을 잇는다. 원본을 고치면 import 한 번으로 트랙별 산출물이 다시 생성된다.

짧은 에피소드에서 출발해 기획·인물·그림체·캐릭터 디자인·연출 노트·애니메이션 콘티까지 사용자와 함께 정해 나가는 일은 상위 스킬 `webtoon-story-studio`가 맡는다. 그 스킬의 G9(웹툰 콘티) 단계가 이 킷을 부르며, 그때는 스튜디오 프로젝트의 `story/novel.md`·`story/script.md`·`design/characters.json`·`design/style.json`을 킷 입력으로 쓰고 킷 폴더는 스튜디오 프로젝트의 `storyboard/`에 둔다.

## 결과물

| 구분 | 내용 |
|---|---|
| 원본 문서 | `source/novel.md`·`novel.docx`, `source/storyboard.md`·`storyboard.docx` |
| `webtoon_real` | 컷별 사실적(실사풍) 이미지 프롬프트 + 레터링 목록 |
| `webtoon_adult` | 19세 드라마 톤 이미지 프롬프트. 수위 상한은 콘티와 같다(아래 '넘지 않는 선') |
| `shorts` | 장별 9:16 쇼츠 대본(컷 길이·카메라·자막/VO) + ffmpeg 러프컷 스크립트 |
| `anim` | 24fps 샷 리스트(길이·카메라·레이어·립싱크 대사) |
| 편집기 | `tools/editor_ready.html` — 컷 편집, 트랙별 프롬프트 복사, 결과 이미지 비교 |

## 작업 순서

### 1. 킷 생성
`assets/kit_template/`를 작업 위치로 복사하고 `scripts/kit.py`와 `scripts/thumbgen.py`를 그 루트에 둔다. `tools/md2docx.js`는 템플릿에 이미 들어 있다.

### 2. 원본 문서 만들기 (md + docx)
원본이 어디 있든 `source/novel.md`, `source/storyboard.md` 두 파일로 정리한다.

- **원본이 Claude Docs에 있을 때:** export(markdown)로 받는다. 받은 결과를 컨테이너에 옮길 수 없으면, 대화에 남아 있는 해당 문서의 작성·수정 내용을 순서대로 이어 붙여 그대로 다시 쓴다. 다시 쓴 뒤에는 export 결과의 바이트 수와 비교해 내용이 일치하는지 확인하고, 차이(날짜·작성자 줄 등)를 사용자에게 알린다.
- **사용자가 파일을 줬을 때:** 그 파일을 그대로 쓴다. docx만 있으면 `pandoc -t markdown`으로 변환한다.
- **형식:** 소설은 `# 제목` 아래 `## 장 제목`으로 장을 나눈다. 콘티는 `### 장 제목` 아래 `| 컷 | 크기 | 화면·연출 | 대사·내레이션·SFX |` 표다. 상세 형식은 references/schema.md.
- **원문을 바꾸지 않는다.** 정리 과정에서 문장을 다듬거나 요약하지 않는다. 고칠 점이 보이면 따로 알린다.

그다음 Word 사본을 만든다.

```
python kit.py docx
```

- node와 `docx` 패키지가 있으면 `tools/md2docx.js`를 쓴다. 소설은 A4 세로, 콘티는 A4 가로이고, 표 행이 페이지에서 쪼개지지 않으며 머리글이 매 쪽 반복된다. 둘 다 없으면 pandoc 기본 서식으로 대체된다.
- 만든 뒤에는 PDF로 렌더해 눈으로 확인한다(`soffice --headless --convert-to pdf` → `pdftoppm`). 표가 잘리거나 글꼴이 깨지면 고치고 다시 만든다.
- 기본 글꼴은 맑은 고딕이다. Mac에서는 다른 한글 글꼴로 대체되어 보인다는 점을 사용자에게 알린다.

### 3. 프로젝트 설정
`data/characters.json`(인물별 외형 고정값과 별칭), `data/style.json`(시대·장소·색·글꼴·말풍선)을 작품에 맞게 다시 쓴다. 템플릿 값은 예시 작품의 것이다. 별칭에 '나', '아내'처럼 다른 문장에 흔히 섞이는 짧은 단어를 넣지 않는다(오탐).

### 3-1. 콘티를 웹툰 밀도로 쓰기 (콘티가 없거나 성길 때)
소설 문단 하나를 컷 하나로 옮기면 웹툰이 아니라 삽화가 된다. references/storyboard_spec.md를 읽고 그 규격으로 쓴다. 핵심:
- 한 컷 = 한 동작·한 감정·한 정보, 대사는 컷당 최대 2개. 원작 문단 1개당 3~6컷.
- 장면마다 `#### 장면: 이름 (장소, 시각)` 소제목. 설정샷 → 인물 → 대사 교차 → 무음 리액션 → 소품 인서트 → 여운.
- 표는 5열: `| 컷 | 크기 | 샷·앵글·인물 | 화면·연출 | 대사·내레이션·SFX |`. 컷 번호는 `장-세자리`(2-007). 샷·앵글·인물 칸은 `BS · 오버숄더(정만 너머) · 인턴(중), 정만(좌·전경)` 형식.
- 원작 대사·내레이션은 원문 그대로. 새 사건·설정 추가 금지.
- 분량이 크면 장면 범위를 나눠 여러 서브에이전트에게 병렬로 맡기고(각자 같은 규격 파일을 읽게 함), 합친 뒤 재번호한다. 합친 다음에는 **별도 서브에이전트로 검수**(원작 대사 전수 대조·수위·형식·연속성)하고 지적을 반영한다.
- 이전 콘티는 `storyboard_v1.md`처럼 남겨 둔다. 컷 번호 체계가 바뀌면 `python kit.py import --replace`.

### 4. 썸네일
`python kit.py thumbs-auto`가 샷·앵글·인물 칸을 읽어 `thumbs/<컷번호>.svg` 레이아웃 썸네일을 만든다(샷 크기 → 인물 크기, 좌·중·우·전경·후경 → 배치, 실루엣·분할·POV 문틈·집중선·말풍선·내레이션·효과음 자리 표시). 손으로 그린 콘티 이미지가 있으면 같은 이름의 `.png`로 넣으면 그것이 우선한다. `python kit.py board`로 장·장면별 썸네일 보드(tools/board.html, 단일 파일)를 만들어 artifact로 게시한다.

### 5. 변환
```
python kit.py import
python kit.py thumbs-auto
python kit.py validate
python kit.py prompts --track all
python kit.py shorts-script
python kit.py board
python kit.py editor
```
validate의 문제 건수와 수위 태그 집계를 사용자에게 보고한다. 수위 태그는 2단계로 붙는다: 강한 단서(키스·맨살·타격·유서 등)는 그 장면 전체로 전파되고, 약한 단서(입술·단추·망치 등)는 그 컷에만 붙는다. import 후 민감 장면의 대표 컷 몇 개를 골라 태그가 붙었는지 직접 확인하고, 놓쳤으면 kit.py의 키워드 목록을 보강한다(cuts.json을 손으로 고치면 다음 import 때 덮어써진다).
- 쇼츠: 세분화 콘티를 장 단위로 그대로 쓰면 편당 60초를 크게 넘는다. 대본의 '60초 초과' 표시를 보고 하이라이트 컷만 골라 쓰도록 안내한다.

### 6. 전달
킷 폴더를 zip으로 묶고, 원본 md·docx 네 파일도 개별 파일로 함께 전달한다. 사용자에게는 무엇이 채워졌는지(컷 수, 문제 건수, 태그 집계)와 확인하지 못한 것을 짧게 알린다.

## 갱신 루프

- 원본을 고쳤으면: `.md` 수정 → `import` → `prompts` → `docx`. `.docx`를 직접 고치지 않는다(자동 반영되지 않음).
- 편집기에서 고쳤으면: 편집기의 "cuts.json 내려받기" → `merge-edits <파일>` → `prompts`.
- 결과 이미지는 `renders/<트랙>/<컷번호>.png`에 두면 편집기에서 콘티 썸네일과 나란히 비교된다. 쇼츠 러프컷은 renders/shorts → renders/webtoon_real → thumbs 순으로 이미지를 고른다.

## 트랙별 세부 지침

트랙 작업을 깊게 할 때만 references/tracks.md를 읽는다. 인물 일관성, 실사 트랙의 기준 이미지 만들기, 쇼츠 훅 배치, 애니 레이어 분리 요령이 있다.

## 넘지 않는 선

이 규칙은 data/tracks.json에도 들어 있고 모든 프롬프트 끝에 자동으로 붙는다. 사용자가 완화를 요청해도 유지한다.

- 모든 얼굴은 창작된 성인이다. 실존 인물·유명인을 닮게 만들지 않는다. 실화 기반 작품이면 특히 지킨다.
- 실제 병원·방송사·브랜드 로고를 쓰지 않는다.
- `intimate` 컷: 노출 없이 실루엣·역광·손·반지·흘러내린 옷·소품으로만 암시한다. 성기·가슴 노출과 성행위의 직접 묘사는 성인 트랙에서도 만들지 않는다.
- `violence` 컷: 타격은 집중선·실루엣·효과음으로 처리하고 상처·출혈을 그리지 않는다.
- `self_harm_theme` 컷: 투신·자해 순간을 그리지 않고 남겨진 소품과 이후 장면으로 잇는다.

규칙과 부딪히는 요청을 받으면 거절로 끝내지 말고 규칙 안의 대체 연출을 제안한다.

## 파일 지도

- `scripts/kit.py` — import(--replace), validate, prompts, editor, merge-edits, shorts-script, docx, thumbs-auto, board, pack.
- `scripts/thumbgen.py` — 샷·앵글·인물 칸으로 레이아웃 썸네일 SVG를 그리는 모듈(kit.py와 같은 폴더에 둔다). docx 외에는 Python 3.9+ 표준 라이브러리만 쓴다.
- `scripts/md2docx.js` — Markdown → docx 변환기(제목·문단·목록·표·굵게·기울임). `node md2docx.js 입력.md 출력.docx [landscape]`.
- `assets/kit_template/` — 킷 폴더 템플릿(README, AGENTS.md, 편집기, md2docx.js, 데이터 파일).
- `references/storyboard_spec.md` — 웹툰 밀도 콘티 작성 규격(컷 쪼개기, 5열 형식, 샷 표기, 수위, 검수).
- `references/schema.md` — 소설·콘티 Markdown 형식과 cuts.json 필드.
- `references/tracks.md` — 트랙별 제작 요령.
