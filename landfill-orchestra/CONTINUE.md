# 이어서 작업하기 — 「깡통 바이올린」 / landfill-orchestra

최종 정리: 2026-10-09 10:30 KST. 진행은 `skills/webtoon-story-studio`의 결정 게이트를 따른다. 결정 기준은 `decisions.md`.

## Claude Code에게 처음 할 말
> landfill-orchestra/CONTINUE.md를 읽고, 「깡통 바이올린」 G9 웹툰 콘티부터 이어서 진행해.

## 진행 상태

| 게이트 | 상태 | 산출물 |
|---|---|---|
| G0 접수 | 확정: 파라과이 카테우라 재활용 악기 오케스트라 모티프, 3화, 인물·지명 가공, 12세 이상, 감동·희망 | `project.md`, `source/original.md` |
| G1 방향 | 확정: 1980년대 서울 변두리 가공 '갈대섬', 13세 소녀 주인공, 정공법 성공 결말 | `story/pitch.md` |
| G2 인물 | 확정: 하은주('귀신', 조용한 귀) 외 10명 | `story/bible.md`, `design/characters.json`, `design/sheets/*.svg`(러프) |
| G3 구성 | 확정: 발견→위기→무대, 청소년 합주제 우승, 창작곡 「섬의 하루」 | `story/synopsis.md`, `story/beats.md`(28비트), `story/beats.json`, `design/colorscript.svg` |
| 연속성 | 이름·장소·악기·시간·복선·사건 순서의 기준 문서 | `story/continuity.md` |
| G4 소설 | 확정(문체 A: 3인칭 근접). 약 3만 9,600자. 검수 완료(구조 0건, 단순 10건 반영) | `story/novel.md`, `story/parts/ep1~3.md`, `docx/story_novel.docx` |
| G5 대본 | 확정: 애니형, 3화 80씬(1화 17·2화 29·3화 34), 예상 1화 약 25분·2화 약 26분·3화 약 43분. 길이는 마스터로 유지 | `story/script.md`, `story/script_format.md`(형식·이름표), `story/script_cut_candidates.md`(축소 후보), `story/sfx_list.md`(소리 표기 초안), `docx/story_script.docx` |
| G6 그림체 | 확정: 정밀 셀 반실사 「소리의 색」(콘티 정합형). 선 2px·셀 2단·질감 없음, 소리 색 규칙, 이미지에 글자 없음. 대본 80씬 씬 프리셋(빛·색·의상·소리 색·영어 [SCENE] 문장) | `design/style_guide.md`(규칙·장소 기준 문장·인물 고정 문구), `design/style.json`, `design/scene_presets.md`·`.json`, `design/style_options.md`(1~3안 비교), `design/style/`(맛보기 SVG), `research/notes.md`(시각 고증) |
| G7 캐릭터 | 확정: 16명(주요 10 + 섬 아이 6) + 단역 7 고정 문구. 계절·본선·2003 의상과 씬별 일정표. 섬 아이 본선 의상 = 제일 좋은 옷 + 빨간 손수건 | `design/characters.json`(design_choice), `design/style_guide.md` 6절, `design/outfit_schedule.json`, `design/outfits_en.json`, `design/sheets/*.svg`(러프), `design/gen/character_prompts.md`(GPT 시트 프롬프트: 턴어라운드·표정·의상·2003·회상) |
| G8 소품·배경 | 확정: 소품 176개(A 29·상태 64단계) + 배경 39곳, 모두 고증·출처·GPT 프롬프트. 의상·용어·지역명 고증 반영 | `design/props.*`, `design/gen/prop_prompts.md`, `design/sets.*`, `design/gen/set_prompts.md`, `design/costume_research.md`, `story/era_terms_research.md`, 생성기 `tools/props_src/`·`tools/sets.py` |
| G9 웹툰 콘티 | **다음 작업.** | — |
| G10~G12 | 대기 | — |

## 바로 다음 할 일
1. **G9 웹툰 콘티.** `webtoon-adaptation-kit`로 `storyboard/` 킷을 만든다(아동 주인공이라 tracks.json을 "아동 인물 성적·선정적 연출 금지, webtoon_adult 미사용"으로). 장면 소제목에 대본 S#. 컷 프롬프트는 `tools/prompt.py`(인물 고정 문구·씬 프리셋·의상 일정표) + 소품(`design/props.json`의 prompt·상태 키) + 배경(`design/sets.json`의 배치 문장, 참고 이미지 `renders/sets/<id>.png`)을 합친다. 화당 60~80컷으로 줄일 때 `story/script_cut_candidates.md`. 먼저 한 장면 샘플(밀도 2안)을 보여 주고 고르게 한다.
2. 사용자는 `design/gen/character_prompts.md` → `prop_prompts.md` → `set_prompts.md` 순서로 GPT 이미지를 만들어 `renders/characters/`, `renders/props/`, `renders/sets/`에 저장한다.
3. 원고·디자인을 고치면 재생성 순서: `tools/presets_src/gen_ep12.py`·`gen_ep3.py` → `tools/presets.py` → `tools/sets.py` → `tools/props_src/build.py`·`gen_md.py`·`check.py` → `tools/char_prompts.py` → `tools/script_check.py check`.

## 꼭 알아 둘 것
- **고증 원칙(사용자 지시):** 배경·소품·의상·용어·지역명·제도·물가·말투를 모두 그 시대(본편 1987~88, 회상 1950·70년대, 에필로그 2003) 기준으로 고증하고 출처를 단다. 확인 못 하면 '미확인', 해석은 '추측'. 고증 보고서: `research/notes.md`, `design/costume_research.md`, `story/era_terms_research.md`, `design/props.md`·`design/sets.md`의 고증 칸.
- **그림체 원칙(사용자 지시):** "구체적인 콘티를 최대한 반영해야 GPT가 정확하게 그린다." 질감·우연에 맡기는 표현을 빼고 모든 것을 수치·HEX·영어 문장으로 고정한다. 장소 묘사는 `style_guide.md` 8절 문장을 글자 그대로 재사용한다.
- 소리 색 규칙은 대본 근거('귀로'·'그 소리만'·M:)가 있는 컷에만. 조롱 웃음 등 상처받는 소리와 에필로그 이중주는 색 없음. 3화 본선은 악기 색이 하나씩 늘어 '밤'에서 화면 전체.
- 고증: 1987~88 쓰레기 산은 꼭대기가 평평한 층진 탁자형. 판잣집 동네는 의도적 각색(실제는 조립식 주택).
- **대본 정본은 `story/script.md`** (교정 반영본). `python landfill-orchestra/tools/script_check.py check`로 소설 대사 누락과 S# 연속을 점검한다(지금 누락 0). `merge`는 조각(`story/script_parts/`, 지금은 지움)을 합치는 명령인데, 정본이 있으면 덮어쓰지 않고 멈춘다.
- 대본 이름표: 아버지는 대사·지문 모두 '만석'(대사 속 호칭은 "아빠"). 내레이션은 모두 어른 은주 목소리 `은주<탭>(N)`. 고정 목록은 `story/script_format.md`.
- 은주는 태준에게 첫 대면부터 반말(사용자 확정). 미자에게는 존댓말.
- 고증 결정: 신문은 「한강신보」, 선영이 가르치는 곳은 '강변교회 지하 공부방', 1988 가을 임시 거처 → 1990 임대아파트, 에필로그는 '개장 한 돌 음악회'(2003 봄). 나이는 1987년 기준 세는나이(은주 1975년생, 1988년 3월 중1).
- 섬 정리는 두 단계: 1987년 5월 정리 예정 알림(1화) → 1988년 1월 정식 통보, 8월 말까지(2화).
- 대본의 변경 기록은 씬 번호가 아니라 소설 줄 번호(`ep3.md:275`)로 가리킨다. 소설을 고치면 줄 번호가 밀리므로 함께 확인한다.
- **2화 정본은 `story/parts/ep2.md`.** 같은 내용을 세 조각으로 다시 쓴 판은 `story/parts/ep2_alt_split.md`(대안, 쓰지 않음).
- 호칭: 대사에서 은주·동민은 "아빠", 지문은 "아버지". 1987년 학교는 '국민학교'.
- 3화 전제: 곽 영감에게 여분 바이올린 줄이 없다("공장 시절 줄은 그게 마지막이었다"). 본선에서 E현이 끊어지면 태준의 여분 줄로 바꾼다.
- 3화 작가가 만든 작은 인물: 섬 아이 6명(봉구, 영란, 경호·경민 쌍둥이, 순이, 석이). 소품: 미자의 '찾을 돈' 깡통, 순례 할머니의 국자 신호 '탕탕탕'.
- 1화 작가가 더한 대회 참가 자격: "국민학교·중학교 학생 합주단"(1988년 중1 은주와 중2 태준이 함께 나가도록).
- **G9 메모:** 이 작품은 아동 인물이 주인공이다. 킷 기본 규칙의 "미성년자로 보이는 인물 금지"는 성인 웹툰용이므로, 킷의 `storyboard/data/tracks.json`을 "아동 인물은 어떤 경우에도 성적·선정적 연출 금지, 성인 트랙(webtoon_adult) 미사용"으로 바꿔서 쓴다.
- 작화는 Claude가 하지 않는다(ChatGPT·Codex 몫). Claude는 사양·프롬프트·콘티를 만든다.

## 도구
- `python3 landfill-orchestra/tools/studio.py <명령> --dir landfill-orchestra` (sketch, colorscript, board, docx, pack)
- docx 변환에는 Node와 `npm i -g docx`가 필요하다(전역 설치 없이 하려면 아무 폴더에 `npm i docx` 뒤 `NODE_PATH=<그 폴더>/node_modules`로 실행).
- `python landfill-orchestra/tools/script_check.py check` — 대본 대사·S# 점검.
- `python landfill-orchestra/tools/presets.py` — 씬 프리셋 합치기·점검(대본 S# 80개와 대조). 원본 생성기 `tools/presets_src/`.
- `python landfill-orchestra/tools/prompt.py 1-11 --chars eunju --cut "…" --sound 동그리` — 컷 프롬프트 조립.
- `python landfill-orchestra/design/style/gen.py` — 그림체 맛보기 SVG.
- `python landfill-orchestra/tools/char_prompts.py` — 캐릭터 시트 GPT 프롬프트(design/gen/character_prompts.md).
