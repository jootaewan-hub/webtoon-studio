# 이어서 작업하기 — 「깡통 바이올린」(가제) / landfill-orchestra

최종 정리: 2026-10-08 12:45 KST. 진행은 `skills/webtoon-story-studio`의 결정 게이트를 따른다. 결정 기준은 `decisions.md`.

## Claude Code에게 처음 할 말
> landfill-orchestra/CONTINUE.md를 읽고, 「깡통 바이올린」 G5 대본(애니형)부터 이어서 진행해.

## 진행 상태

| 게이트 | 상태 | 산출물 |
|---|---|---|
| G0 접수 | 확정: 파라과이 카테우라 재활용 악기 오케스트라 모티프, 3화, 인물·지명 가공, 12세 이상, 감동·희망 | `project.md`, `source/original.md` |
| G1 방향 | 확정: 1980년대 서울 변두리 가공 '갈대섬', 13세 소녀 주인공, 정공법 성공 결말 | `story/pitch.md` |
| G2 인물 | 확정: 하은주('귀신', 조용한 귀) 외 10명 | `story/bible.md`, `design/characters.json`, `design/sheets/*.svg`(러프) |
| G3 구성 | 확정: 발견→위기→무대, 청소년 합주제 우승, 창작곡 「섬의 하루」 | `story/synopsis.md`, `story/beats.md`(28비트), `story/beats.json`, `design/colorscript.svg` |
| 연속성 | 이름·장소·악기·시간·복선·사건 순서의 기준 문서 | `story/continuity.md` |
| G4 소설 | 완료(문체 A: 3인칭 근접). 약 3만 9,600자 | `story/novel.md`, `story/parts/ep1~3.md`, `docx/story_novel.docx` |
| G5 대본 | **다음 작업.** 형식 확정: 애니형(예상 길이·카메라 의도·연기 메모) | `story/script.md`(아직 템플릿) |
| G6~G12 | 대기 | — |

## 바로 다음 할 일
1. **소설 검수(아직 안 함).** 별도 에이전트로 한 번 돌린다: 화 사이 연속성(호칭, 날짜, 동그리 행방, 여분 줄 유무), 28비트 누락, 복선 회수, 12세 기준, 시대 착오, 40자 넘는 대사. 지적만 받아 반영한다.
2. **G5 대본(애니형).** `references/story.md`의 애니형 형식. 화별로 앞·뒤 두 조각씩 6개 에이전트에 병렬로 맡기면 조각당 5분 안팎이다(한 화를 통째로 맡기면 25~30분 걸렸다). 소설 대사를 그대로 쓰고, 바꾼 곳은 대본 끝 '변경 기록'에. 씬 번호(S#)는 화마다 1부터, 이후 콘티·애니 콘티 장면 소제목에 그대로 쓴다.
3. 그다음 G6 그림체 3안 → G7 캐릭터 시안(`studio.py sketch --variants`) → G8 소품·배경(동그리·뚱보·꽥꽥이·뼈다귀 북 삽화).

## 꼭 알아 둘 것
- **2화 정본은 `story/parts/ep2.md`.** 같은 내용을 세 조각으로 다시 쓴 판은 `story/parts/ep2_alt_split.md`(대안, 쓰지 않음).
- 호칭: 대사에서 은주·동민은 "아빠", 지문은 "아버지". 1987년 학교는 '국민학교'.
- 3화 전제: 곽 영감에게 여분 바이올린 줄이 없다("공장 시절 줄은 그게 마지막이었다"). 본선에서 E현이 끊어지면 태준의 여분 줄로 바꾼다.
- 3화 작가가 만든 작은 인물: 섬 아이 6명(봉구, 영란, 경호·경민 쌍둥이, 순이, 석이). 소품: 미자의 '찾을 돈' 깡통, 순례 할머니의 국자 신호 '탕탕탕'.
- 1화 작가가 더한 대회 참가 자격: "국민학교·중학교 학생 합주단"(1988년 중1 은주와 중2 태준이 함께 나가도록).
- **G9 메모:** 이 작품은 아동 인물이 주인공이다. 킷 기본 규칙의 "미성년자로 보이는 인물 금지"는 성인 웹툰용이므로, 킷의 `storyboard/data/tracks.json`을 "아동 인물은 어떤 경우에도 성적·선정적 연출 금지, 성인 트랙(webtoon_adult) 미사용"으로 바꿔서 쓴다.
- 작화는 Claude가 하지 않는다(ChatGPT·Codex 몫). Claude는 사양·프롬프트·콘티를 만든다.

## 도구
- `python3 landfill-orchestra/tools/studio.py <명령> --dir landfill-orchestra` (sketch, colorscript, board, docx, pack)
- docx 변환에는 Node와 `npm i -g docx`가 필요하다.
