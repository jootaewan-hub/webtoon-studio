# 데이터 형식

## 소설 Markdown (source/novel.md)

```
# 작품 제목

## 작품 소개
본문…

## 1장. 장 제목
본문 문단은 빈 줄로 구분합니다. **굵게**, *기울임*, "- " 목록을 쓸 수 있습니다.
```

- `## ` 제목마다 한 장으로 나뉘어 data/novel_chapters.json에 저장됩니다.
- docx 변환기는 `#`(제목), `##`, `###`, 문단, `- ` 목록(들여쓰기 2칸 = 2단계), 표, `**굵게**`, `*기울임*`을 지원합니다.

## 콘티 Markdown (import 입력)

```
### 2장. 불륜의 기술 (전반)

연출 메모: (선택) 장 전체에 적용할 연출 지시

#### 장면: 당직표 (의국, 오후)

| 컷 | 크기 | 샷·앵글·인물 | 화면·연출 | 대사·내레이션·SFX |
|---|---|---|---|---|
| 2-042 | 800×800 | MS · 오버숄더(치프 너머) · 무진(우), 치프(좌·전경) | 당직표 앞의 2인 숏... | 치프: 니는 와 맨날 수요일 금요일이고? |
```

- 컷 번호: `장-두자리` 또는 `장-세자리`(`2-042`), 에필로그 `E-001`. 4열(샷 칸 없음) 표도 읽는다.
- `#### 장면:` 소제목은 각 컷의 scene 필드가 된다.
- 크기: `폭×높이` (× 또는 x).
- 대사 칸은 ` / `로 구분. `화자: 내용` 형식이며 화자 이름으로 종류를 판별한다.
  - `내레이션…` → narration, `SFX…` → sfx, `…(생각)` → thought, `…(속삭임)` → whisper
  - `손글씨·메모·차트·고지문·초시계·제목·말풍선` → caption, 그 밖 → dialogue
- 표 칸 안에 `|` 문자를 쓰지 않는다.

## data/cuts.json (컷 1개)

```json
{
  "id": "2-042",
  "scene": "당직표 (의국, 오후)",
  "shot": "MS · 오버숄더(치프 너머) · 무진(우), 치프(좌·전경)",
  "chapter": "2장. 불륜의 기술 (전반)",
  "width": 800, "height": 800,
  "summary": "치프(실눈)와 태연한 무진",
  "screen": "당직표 앞의 2인 숏...",
  "lines": [{"type": "dialogue", "speaker": "치프", "text": "니는 와 맨날 수요일 금요일이고?"}],
  "flags": ["intimate" | "violence" | "self_harm_theme"],
  "thumb": "thumbs/2-042.svg",
  "notes": {"webtoon_real": "트랙 전용 추가 지시"}
}
```

## data/flags.json (kit.py v2)

수위 태그 키워드와 아동 장면 규칙. 없거나 비운 키는 kit.py 기본값을 쓴다.
```json
{"intimate": {"strong": ["키스", "나신"], "weak": ["입술", "쇄골"]},
 "violence": {"strong": ["타격"], "weak": ["폭력"]},
 "self_harm_theme": {"strong": ["투신"], "weak": []},
 "negations": "(수위 장치|관능 요소|관능)\\s*[:：]?\\s*(없음|해당 없음|불필요|전혀 없음)",
 "child_names": ["지호", "소이", "아이들"],
 "child_scene_memo": "장소\\s*6\\b",
 "route_b_keywords": ["나신", "속옷", "시트로 가린"]}
```
- 강한 단서(strong)는 장면 전체로 전파되고, 약한 단서(weak)는 그 컷에만 붙는다.
- 연출 메모에 흔히 쓰는 라벨(예: '수위 장치:')은 키워드로 쓰지 않는다. 폭력·법정 장면 메모에도 쓰여 오탐이 난다.
- 비유로 쓰인 낱말(예: "관리가 아니라 자해였다")이 오탐이면 그 낱말을 키워드에서 뺀다.
- `child_names`가 **샷·앵글·인물 칸**에 나오면 그 장면은 `child_present`가 된다. 이때 intimate는 지우고 tracks.json `child_rule`을 붙인다. 메모의 "아이는 외가에" 같은 언급은 등장으로 보지 않는다.
- `route_b_keywords`는 스튜디오 인계(build_handoff.py)의 도구 경로 B 판정에 쓴다.

## data/sets.json (kit.py v2)

`{"<장소 번호>": {"name": "장소 이름", "lock": "영어 SET LOCK"}}`.
- 장면 연출 메모에 `장소 2(…)`처럼 번호가 있으면 그 장소의 SET LOCK이 컷 프롬프트에 붙는다. 한 장면에 최대 2곳이다.
- 짧은 장소는 키를 `짧게 A`로 한다.
- 스튜디오 프로젝트면 `from_studio.py`가 `handoff/sets.md`에서 만든다.

## data/chapter_notes.json

import가 만든다. `{"<장 제목> / <장면 소제목>": "연출 메모 원문"}`이다. 컷 프롬프트의 '장면 연출 메모'와 SET LOCK 판정에 쓴다.

## data/characters.json

`[{"id": "mujin", "name": "무진", "aliases": ["권무진"], "look": "외형 고정값 한 문단(영어 CHARACTER LOCK 권장)", "lock_file": "…"}]`
- 화면·대사 텍스트에 이름이나 별칭이 나오면 그 컷 프롬프트에 외형이 자동으로 붙는다.
- `name`은 콘티 샷 칸에 쓰는 이름이다(보통 성을 뺀 이름).
- 스튜디오 프로젝트면 `from_studio.py`가 `design/characters.json`과 `handoff/characters/<id>.md`의 CHARACTER LOCK으로 만든다.

## data/tracks.json

`tracks.<코드>.{title, brief, style, style_track2?, style_track3?}`와 공통 규칙 `global_negative`, `intimate_rule`, `violence_rule`, `self_harm_rule`, `child_rule`.
- 콘티 화면 칸이 `[트랙2]`나 `[트랙3]`으로 시작하는 컷은 `style_track2`·`style_track3`을 쓴다.
- 트랙 코드는 작품에 맞게 줄일 수 있다. 예: 성인 작품은 `webtoon_adult`, `shorts`, `anim`만 둔다.

## data/style.json

`era`, `palette_hint`, `fonts`, `bubbles`, `tone`, `thumbnails`.
- `thumbnails: false`이면 썸네일을 그리지 않는 작품으로 본다. 이때 validate는 썸네일 없음을 문제로 세지 않는다. 작화를 외부에 맡기는 작품이 여기에 해당한다.
