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

- 컷 번호: `장-두자리` 또는 `장-세자리`(`2-042`), 에필로그 `E-001`. 장 번호는 1~3자리(`10-001`)까지 읽고, 정렬은 숫자 순(0 → 1 → … → 10 → E)이다. 형식이 어긋난 번호(`3-01a` 등)는 import 때 경고를 내고 건너뛴다. 4열(샷 칸 없음) 표도 읽는다.
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
  "notes": {"webtoon_real": "트랙 전용 추가 지시"},
  "flags_override": ["intimate"],
  "edited_fields": ["screen"]
}
```

- import가 원본 md에서 다시 채우는 필드: chapter, scene, shot, screen, summary, lines, width, height, flags. 이 필드를 편집기에서 고쳐도 다음 import 때 md 값으로 돌아간다.
- import 뒤에도 남는 필드: `notes`(트랙별 추가 지시, 프롬프트에 '추가 지시' 줄로 들어감), `flags_override`(손으로 정한 수위 태그, 있으면 자동 태그 대신 쓴다. 지우면 자동으로 돌아감), `thumb`.
- `edited_fields`: merge-edits가 기록하는 '편집기에서 고친 md 필드' 목록. 다음 import에서 md 값과 다르면 경고하고 편집값을 `data/edits_replaced.json`에 남긴 뒤 지운다.

## data/characters.json

두 형식을 모두 읽는다. 화면·샷·대사 텍스트에 이름이나 별칭이 나오면 그 컷 프롬프트에 외형이 자동 첨부된다.

- 킷 형식: `[{"name": "무진", "aliases": ["권무진"], "look": "외형 고정값 한 문단"}]`
- 스튜디오 형식(webtoon-story-studio의 `design/characters.json`): `look`이 없으면 age·adult·height·build·head_ratio·hair·hair_color·skin·face·accessories·outfits·acting으로 외형 문구를 조합한다. `aliases`가 없으면 빈 목록. 직접 쓴 `look`이 있으면 그것이 우선한다.

## data/style.json

- 킷 형식: `era`(시대·장소), `palette_hint`(색·광원), `fonts`, `bubbles`, `tone`.
- 스튜디오 형식: `palette`(이름·HEX 목록)로 `palette_hint`를 만들고, name·line·color·shading·background·proportion으로 프롬프트의 '그림체' 줄을 만든다. `era`는 스튜디오 형식에 없으므로 넣어야 '시대·장소' 줄이 나온다.

## data/flags.json (작품별 수위 단서)

```json
{"intimate": {"strong": ["사우나 탈의실"], "weak": ["수건"], "remove": ["이불"]},
 "violence": {"strong": [], "weak": [], "remove": []},
 "self_harm_theme": {"strong": [], "weak": [], "remove": []}}
```

- kit.py의 기본 단서(`DEFAULT_FLAG_KW`, 어느 작품에나 통하는 낱말)에 더하고 뺀다. strong은 그 장면 전체로, weak는 그 컷에만 태그를 붙인다. `_`로 시작하는 키는 설명으로 무시한다.
- 낱말은 화면·연출과 대사 칸 원문에서 찾는다. 대사 표기(`인물(속삭임):` 등)도 원문에 들어 있으니 흔한 표기 낱말은 넣지 않는다.

## data/tracks.json

`tracks.<코드>.{title, brief, style}`와 공통 규칙 `global_negative`, `intimate_rule`, `violence_rule`, `self_harm_rule`.
