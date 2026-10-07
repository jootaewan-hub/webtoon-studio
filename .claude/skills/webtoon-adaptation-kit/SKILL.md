---
name: webtoon-adaptation-kit
description: 소설을 웹툰 문법에 맞게 장면·동작 단위로 잘게 쪼갠 콘티로 만들고, 소설과 콘티(컷 번호·크기·샷·화면·대사 표)를 실사·성인(19세) 웹툰 이미지 프롬프트, 쇼츠(9:16), 애니메이션 샷 리스트로 옮기는 제작 킷을 만들고 갱신하는 스킬. 소설·콘티 원본을 Markdown과 Word(docx)로 함께 저장하는 일, 콘티 형식·원작 대사 자동 검사, 컷별 프롬프트에 인물·장소 LOCK과 장면 조명·의상 메모를 자동으로 붙이는 일도 포함한다. 사용자가 소설이나 콘티를 Codex·ChatGPT·이미지 생성 도구로 넘기려 할 때, 원본을 md·docx로 정리해 두려 할 때, 컷별 이미지 프롬프트·레터링 대본·쇼츠 대본·애니 샷 리스트를 원할 때, 콘티를 편집하기 쉬운 형태(JSON, 편집기)로 바꾸려 할 때, 콘티가 '웹소설에 그림만 붙인' 느낌이라 더 세분화하려 할 때, 웹툰을 쇼츠나 애니로 각색하려 할 때는 "킷"이라는 말이 없어도 반드시 이 스킬을 사용한다.
---

# 웹툰 각색 제작 킷

소설·콘티·콘티 이미지를 하나의 작업 폴더(킷)로 묶는다.
- 원본은 Markdown(작업용)과 Word(읽기·공유용)로 함께 보관한다.
- 컷 번호가 모든 파일을 잇는다.
- 원본을 고치면 import 한 번으로 트랙별 산출물이 다시 생성된다.

기획·인물·소설·그림체·캐릭터 디자인·연출 노트·애니 콘티·작화 인계는 상위 스킬 `webtoon-story-studio`가 맡는다.
- 그 스킬의 G9(웹툰 콘티) 단계가 이 킷을 부른다.
- 이때 킷 폴더는 스튜디오 프로젝트의 `storyboard/`다.
- `scripts/from_studio.py`가 프로젝트의 소설·콘티·바이블 LOCK·장소 SET LOCK·트랙 문구를 킷 입력으로 가져온다.

## 결과물

| 구분 | 내용 |
|---|---|
| 원본 문서 | `source/novel.md`·`novel.docx`, `source/storyboard.md`·`storyboard.docx` |
| `webtoon_real` / `webtoon_adult` | 컷별 이미지 프롬프트 + 레터링 목록. 아래 내용이 자동으로 붙는다 |
| `shorts` | 장별 9:16 쇼츠 대본(컷 길이·카메라·자막/VO) + ffmpeg 러프컷 스크립트 |
| `anim` | 24fps 샷 리스트(길이·카메라·레이어·립싱크 대사) |
| 편집기 | `tools/editor_ready.html`: 컷 편집, 트랙별 프롬프트 복사, 결과 이미지 비교 |

이미지 프롬프트에 자동으로 붙는 것:
- 트랙 문구. `[트랙2]`·`[트랙3]` 컷은 자동으로 전환된다.
- 장면 연출 메모(조명·의상)
- 장소 SET LOCK
- 등장인물 외형 LOCK
- 금지·수위 규칙. 아이 장면이면 아동 보호 규칙도 붙는다.

트랙은 작품에 맞게 고른다. 예를 들어 성인 작품은 `webtoon_adult`·`shorts`·`anim`만 둔다(data/tracks.json).

## 작업 순서

### 1. 킷 생성
- `assets/kit_template/`를 작업 위치로 복사한다.
- `scripts/kit.py`, `scripts/thumbgen.py`, `scripts/check_board.py`를 그 루트에 둔다. 스튜디오 프로젝트면 `scripts/from_studio.py`도 둔다.
- `tools/md2docx.js`는 템플릿에 이미 있다.

### 2. 원본 문서 만들기 (md + docx)
원본이 어디 있든 `source/novel.md`, `source/storyboard.md` 두 파일로 정리한다.

- **스튜디오 프로젝트**: `python3 from_studio.py`
  - 소설을 복사하고, `parts/ep*.md`를 합본한다.
  - 바이블 LOCK, SET LOCK, 트랙 문구를 data로 가져온다.
- **Claude Docs에 있을 때**: export(markdown)로 받는다. 옮길 수 없으면 대화의 작성 내용을 순서대로 이어 붙이고, export 바이트 수와 비교해 차이를 알린다.
- **사용자가 파일을 줬을 때**: 그대로 쓴다. docx만 있으면 `pandoc -t markdown`으로 바꾼다.
- **형식**: 소설은 `# 제목` 아래 `## 장 제목`이다. 콘티는 `### 장 제목` 아래 5열 표다. 상세는 references/schema.md에 있다.
- **원문을 바꾸지 않는다.** 고칠 점은 따로 알린다.

`python kit.py docx`로 Word 사본을 만든다.
- 소설은 A4 세로, 콘티는 A4 가로로 나온다.
- 만든 뒤 PDF로 렌더해 눈으로 확인한다(`soffice --headless --convert-to pdf` → `pdftoppm`).
- 기본 글꼴은 맑은 고딕이고, Mac에서는 다른 한글 글꼴로 대체된다.

### 3. 프로젝트 설정 (data/)
- `characters.json`: 인물별 외형 LOCK과 별칭. 별칭에 '나', '아내' 같은 흔한 단어를 넣지 않는다.
- `style.json`: 시대·장소·색·글꼴·말풍선을 적는다.
  - 썸네일을 그리지 않는 작품은 `"thumbnails": false`로 둔다. 작화를 ChatGPT·Codex·작가에게 맡기는 경우다.
- `flags.json`: 수위 태그 키워드, 아동 장면 규칙(`child_names`, `child_scene_memo`), 인계 도구 경로 B 단서를 둔다. 작품 어휘에 맞춘다. 템플릿 값은 예시 작품 기준이다.
- `sets.json`: 장소별 SET LOCK이다. 연출 메모의 `장소 N`으로 찾는다.
- `tracks.json`: 트랙 문구(`style`, `style_track2`, `style_track3`)와 금지 규칙(`global_negative`, `intimate_rule`, `child_rule` …)을 둔다.

### 3-1. 콘티를 웹툰 밀도로 쓰기 (콘티가 없거나 성길 때)
references/storyboard_spec.md를 읽고, 작품용 `SPEC.md`를 만들어 그 규격으로 쓴다. 핵심은 다음과 같다.
- 한 컷 = 한 동작·감정·정보다. 세분화판은 회차당 75~95컷이다.
- 장면 소제목에 S#를 달고, 연출 메모 다섯 요소를 쓴다(장소 ID·조명·의상 HEX·트랙·감정 목표).
- 5열 표로 쓴다. 인물 칸에는 화면에 나오는 사람만 쉼표로 나열한다.
- 원작 대사·해설 내레이션은 원문 그대로 쓰고, 동작 묘사는 화면 칸으로 옮긴다.
- 반복 장치는 같은 구도로, 회차 경계는 같은 구도로 잇는다.
- 분량이 크면 회차별로 서브에이전트에 **병렬**로 맡긴다.
  - 각자 `check_board.py`가 형식 0·대사 누락 0이 될 때까지 고친다.
  - 합친 뒤 **작성자와 다른 서브에이전트**로 검수한다(수위·안전 1, 연속성은 반씩 2).
- 이전 콘티는 `storyboard_v1.md`처럼 남긴다. 번호 체계가 바뀌면 `python kit.py import --replace`.

### 4. 썸네일 (선택)
- `python kit.py thumbs-auto`가 샷·앵글·인물 칸을 읽어 `thumbs/<컷>.svg` 레이아웃 썸네일을 만든다. `python kit.py board`는 썸네일 보드를 만든다.
- 사용자가 "그림은 다른 도구가 그린다"고 했으면 썸네일도 만들지 않고 `thumbnails: false`로 둔다.

### 5. 변환
```
python kit.py import --replace
python kit.py validate
python kit.py prompts --track all
python kit.py shorts-script
python kit.py editor
python kit.py docx
```
- validate의 문제 건수와 수위 태그 집계를 보고한다.
- 태그는 2단계다. 강한 단서는 장면 전체로, 약한 단서는 그 컷에만 붙는다.
- import 뒤에 확인한다:
  - 민감 장면 대표 컷 몇 개에 태그가 붙었는지
  - 엉뚱한 장면(비유 문장, '수위 장치: 없음' 메모)에 태그가 붙지 않았는지
- 틀리면 `data/flags.json`을 고친다. cuts.json을 손으로 고치면 다음 import 때 덮어써진다.
- 아이가 샷 칸에 나오는 장면은 `child_present`가 되어 관능 태그가 빠진다. 대표 컷으로 확인한다.
- 쇼츠는 세분화 콘티를 그대로 쓰면 60초를 크게 넘는다. '60초 초과' 표시를 보고 하이라이트 컷만 고르게 안내한다.

### 6. 전달
- 킷 폴더를 zip으로 묶고, 원본 md·docx 네 파일도 개별로 전달한다.
- 무엇이 채워졌는지 짧게 알린다: 컷 수, 문제 건수, 태그 집계, 확인하지 못한 것.
- 스튜디오 프로젝트면 작화 인계 패키지(G12, 스튜디오 `build_handoff.py`)가 이 킷 데이터로 컷별 완성 프롬프트와 도구 경로를 만든다.

## 갱신 루프
- **원본을 고쳤으면**: `.md` 수정 → (스튜디오면 `from_studio.py`) → `import --replace` → `prompts` → `docx`. `.docx`를 직접 고치지 않는다.
- **편집기에서 고쳤으면**: "cuts.json 내려받기" → `merge-edits <파일>` → `prompts`.
- **결과 이미지**는 `renders/<트랙>/<컷번호>.png`에 두면 편집기에서 비교된다.

## 넘지 않는 선

이 규칙은 data/tracks.json에도 들어 있고 모든 프롬프트 끝에 자동으로 붙는다. 사용자가 완화를 요청해도 유지한다.

- 모든 얼굴은 창작된 성인이다. 실존 인물·유명인을 닮게 만들지 않는다. 실화 기반 작품이면 특히 지킨다.
- 실제 브랜드 로고·화폐 도안·기관 휘장을 쓰지 않는다.
- `intimate` 컷의 수위
  - 상한은 작품 수위 줄을 따른다(기본 15세: 실루엣·역광·손·소품으로 암시. 19세 확장은 storyboard_spec.md 참고).
  - 등급과 상관없이 성기·유두 노출, 성행위의 직접 묘사, 체액은 만들지 않는다.
- `child_present` 컷: 관능 요소가 없다.
- `violence` 컷: 타격은 집중선·실루엣·효과음으로 그리고, 상처·출혈은 그리지 않는다.
- `self_harm_theme` 컷: 투신·자해 순간을 그리지 않는다.
- 이미지 생성기의 이용 정책을 피해 가는 프롬프트는 만들지 않는다. 정책이 허용하지 않는 컷은 허용하는 도구나 사람 작가로 보내거나 가림 장치판으로 만든다(references/tracks.md).

규칙과 부딪히는 요청을 받으면 거절로 끝내지 말고 규칙 안의 대체 연출을 제안한다.

## 파일 지도

- `scripts/kit.py`(v2): import(--replace), validate, prompts, editor, merge-edits, shorts-script, docx, thumbs-auto, board, pack.
- `scripts/from_studio.py`: 스튜디오 프로젝트 → source/·data/(LOCK·SET LOCK·트랙 문구).
- `scripts/check_board.py`: 콘티 형식·번호·크기·샷 표기·원작 대사 대조.
- `scripts/thumbgen.py`: 레이아웃 썸네일 SVG. kit.py와 같은 폴더에 둔다.
- `scripts/md2docx.js`: Markdown → docx. `node md2docx.js 입력.md 출력.docx [landscape]`.
- `assets/kit_template/`: 킷 폴더 템플릿(README, AGENTS.md, 편집기, md2docx.js, data 템플릿).
- `references/storyboard_spec.md`: 콘티 작성 규격(세분화판, 연출 메모, 5열, 수위, 반복 장치, 회차 경계, 검수).
- `references/schema.md`: 소설·콘티 형식과 data 파일들(cuts, characters, flags, sets, tracks, style, chapter_notes).
- `references/tracks.md`: 트랙별 제작 요령, 이미지 도구 경로와 생성기 거절·임의 변경 대응.
