# 이어서 작업하기 — 「깡통 바이올린」 / landfill-orchestra

최종 정리: 2026-10-09 07:40 KST. 진행은 `skills/webtoon-story-studio`의 결정 게이트를 따른다. 결정 기준은 `decisions.md`.

## Claude Code에게 처음 할 말
> landfill-orchestra/CONTINUE.md를 읽고, 「깡통 바이올린」 G6 그림체 3안부터 이어서 진행해.

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
| G6 그림체 | **다음 작업.** 3안 제안 | — |
| G7~G12 | 대기 | — |

## 바로 다음 할 일
1. **G6 그림체 3안.** `references/art_direction.md`의 3안 형식(샘플 스케치·팔레트·폰트). 12세 이상 감동·희망 톤, 1987~88년 서울 변두리, 소리가 주인공인 작품이라는 점(효과음 레터링이 그림체와 맞아야 함)을 안의 기준으로. 그림체 전에 시각 고증 리서치(1980년대 난지도·판잣집·고물상, 재활용 악기 실물)를 `research/notes.md`에 남긴다.
2. 그다음 G7 캐릭터 시안(`studio.py sketch --variants`) → G8 소품·배경(동그리·뚱보·꽥꽥이·뼈다귀 북 삽화).
3. G9 콘티에서 대본 씬 번호(S#)를 장면 소제목에 그대로 쓴다. 화당 60~80컷으로 줄일 때 `story/script_cut_candidates.md`를 참고한다.

## 꼭 알아 둘 것
- **대본 정본은 `story/script.md`** (교정 반영본). `python landfill-orchestra/tools/script_check.py check`로 소설 대사 누락과 S# 연속을 점검한다(지금 누락 0). `merge`는 조각(`story/script_parts/`, 지금은 지움)을 합치는 명령인데, 정본이 있으면 덮어쓰지 않고 멈춘다.
- 대본 이름표: 아버지는 대사·지문 모두 '만석'(대사 속 호칭은 "아빠"). 내레이션은 모두 어른 은주 목소리 `은주<탭>(N)`. 고정 목록은 `story/script_format.md`.
- 은주는 태준에게 첫 대면부터 반말(사용자 확정). 미자에게는 존댓말.
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
