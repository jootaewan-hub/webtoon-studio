# 「깡통 바이올린」 인계 패키지 (G12)

웹툰 3화(353컷)와 애니메이션 3화(1,252샷, 약 94분)를 만드는 데 필요한 기준, 프롬프트, 작업 순서, 검수표를 모았다. **이 패키지에는 그림이 없다.** 그림은 ChatGPT(이미지 생성)가 그리고, Codex가 파일 정리·검수 보조·레터링·회차 조립을 맡는다. 애니메이션·사운드 팀은 애니 콘티와 큐 시트를 쓴다.

작품: 1987~88년 서울 변두리 쓰레기 산 마을 '갈대섬'(가공)의 13세 소녀 하은주가 버려진 깡통으로 만든 바이올린 '동그리'로 섬 아이들과 합주단을 꾸린다. 파라과이 카테우라 재활용 악기 오케스트라 실화 모티프, 인물·지명·회사는 모두 가공. 12세 이상, 감동·희망.

## 1. 지도 — 누가 무엇을 쓰나

| 경로 | 내용 | 누가 |
|---|---|---|
| `handoff/README.md` | 이 문서 | 모두 |
| `handoff/AGENTS.md` | Codex 작업 지침(파일 이름, 대장, 검수, 레터링, 회차 조립) | Codex |
| `handoff/CHATGPT_PROJECT_INSTRUCTIONS.md` | ChatGPT 프로젝트 '지침' 칸에 붙여 넣을 문구 | ChatGPT |
| `handoff/asset_manifest.csv` | 그릴 그림 691장 대장(인물 시트 59·소품 240·배경 39·컷 353), 모두 `todo` | Codex, 사람 |
| `decisions.md` | 결정 로그(G0~G12). 모든 기준의 맨 위 | 모두 |
| `design/style_guide.md` | 그림체 「소리의 색」: 선·셀·소리 색·폰트·넘지 않는 선·장소 기준 문장 | 모두 |
| `design/gen/character_prompts.md` | 인물 16명 시트 프롬프트(턴어라운드·표정·의상·2003·회상) | ChatGPT |
| `design/gen/prop_prompts.md` | 소품 240항목(A 핵심·B 반복·C 디테일, 상태 단계 포함) | ChatGPT |
| `design/gen/set_prompts.md` | 배경 39곳 | ChatGPT |
| `storyboard/out/cel/` | **컷 이미지 프롬프트 정본** 353개(`_cel_ALL_ep1~3.md`, 컷별 `<컷>.md`, `cel_prompts.jsonl`) | ChatGPT, Codex |
| `storyboard/source/storyboard.md`(.docx) | 웹툰 콘티 정본(컷 크기·샷·화면·대사·효과음) | 모두 |
| `storyboard/thumbs/`, `storyboard/tools/board.html`, `storyboard/tools/editor_ready.html` | 썸네일, 콘티 보드, 편집기 | 사람 |
| `story/direction.md` | 연출 노트: 세로 스크롤 여백·효과음 위계·무음·말풍선(1부), 장면별 포인트 75장면(2부) | Codex(레터링), 사람 |
| `story/sfx_list.md` | 효과음 표기 정본, 소리 서명 7종 모양, 316종 전수(글꼴·크기·사운드 큐) | Codex, 사운드 |
| `anim/storyboard_anim.md` | 애니메이션 콘티 80장면 1,252샷(카메라·키포즈·립싱크·SFX·BGM·대사·전환) | 애니 팀 |
| `anim/sound_cues.md` | 사운드 큐 시트(화별 타임코드) | 사운드 팀 |
| `anim/cut_shots.md` | 웹툰 컷 → 애니 샷 대응표 | 애니 팀 |
| `story/novel.md`, `story/script.md` | 소설(약 3만 9천 자), 애니형 대본 80씬 — 장면 사실의 기준 | 모두 |
| `story/bible.md`, `design/characters.json`, `design/outfit_schedule.json` | 인물 바이블, 외형 고정값, 씬별 의상 | 모두 |
| `design/scene_presets.md` | 대본 80씬의 빛·대표 색·의상·소리 색 | ChatGPT, 애니 |
| `research/notes.md`, `design/costume_research.md`, `story/era_terms_research.md` | 1987~88 고증(출처) | 사람 |
| `docx/` | 주요 문서 Word 사본 | 사람 |

## 2. 기준 우선순위

1. `decisions.md`의 확정 줄
2. `design/style_guide.md`(그림 규칙·소리 색·인물 고정 문구·넘지 않는 선)
3. `design/characters.json`·`design/outfit_schedule.json`·`design/scene_presets.md`·`design/props.md`·`design/sets.md`
4. `storyboard/source/storyboard.md`(컷)와 `storyboard/out/cel/`(컷 프롬프트)
5. `story/direction.md`·`story/sfx_list.md`(화면 위 글자·소리), `anim/storyboard_anim.md`(애니)
6. `story/script.md`·`story/novel.md`(장면 사실). 그림이 대본과 다르면 그림을 고친다.

## 3. 작업 순서 — 웹툰 작화

**1단계 · 기준 이미지(레퍼런스).** 결과는 `renders/characters|props|sets/`에 저장하고 대장의 `status`를 바꾼다.
1. 인물 16명: 사람마다 ① 턴어라운드 → (승인) → ② 표정 · ③ 의상 · ④ 2003 · ⑤ 회상(만석만). ②부터는 ①의 이미지를 첨부하고 "same character as the attached image"를 앞에 붙인다. 순서: 은주 → 동민 → 만석 → 곽 영감 → 미자 → 덕수 → 선영 → 순례 할머니 → 태준 → 최 계장 → 섬 아이 6명.
2. 소품: A 핵심(동그리 상태 9단계 등)부터, 그다음 B·C.
3. 배경 39곳(빈 배경, 사람 없음).

**2단계 · 컷 353장.** `storyboard/out/cel/_cel_ALL_ep1.md`부터 한 컷씩. 결과는 `storyboard/renders/cel/<컷>.png`(예: `1-003.png`).
- 컷마다 등장인물 턴어라운드, 그 컷의 소품·배경 기준 이미지를 함께 첨부한다.
- **합주 컷 17개**(프롬프트 6천 자 이상, 대장 notes에 표시)는 참고 이미지를 반드시 함께 올린다.
- 분할 컷(가로 2~3분할)이 한 장에 칸대로 나오는지는 아직 시험하지 않았다(미확인). 처음 몇 컷에서 확인하고, 안 되면 칸마다 따로 만든 뒤 Codex가 붙인다.
- 이미지 안에 글자를 넣지 않는다. 말풍선·효과음·내레이션·게시판 글자는 3단계에서 얹는다.

**3단계 · 레터링과 회차 조립(Codex).** `story/direction.md` 1부(여백 40/160/240/80px, 무음 칸 4곳, 말풍선·내레이션 형식)와 `story/sfx_list.md`(위계 ①②③, 소리 서명 모양, 글꼴·크기·색)를 따른다. 자세한 절차는 `handoff/AGENTS.md`.

## 4. 작업 순서 — 애니메이션·사운드

- `anim/storyboard_anim.md`가 정본이다(대본 [예상 길이] 고정, 24fps). 장면 머리의 BGM·앰비언스 줄과 샷 표의 10칸을 따른다.
- 사운드: `anim/sound_cues.md`(타임코드는 샷 길이를 컷 편집처럼 더한 값. 디졸브 겹침은 빼지 않았다) + `story/sfx_list.md` 부록의 사운드 큐 칸. 소리 색 샷 = 그 소리 시작에 맞춰 0.5초에 걸쳐 주변음 -15dB(덕킹) + 화면 채도 60% 낮춤. 소리 서명(리어카·국자·합판 벽·문 두드림·라디오·소리굽쇠 A440)은 작품 내내 같은 오디오 자산. 두드림 간격 8f, 국자 18f.
- 완전 무음(앰비언스까지 끔)은 무음 칸 4곳, 3-100·3-117, 2화 S#29, 회차 시작 타이틀 블랙뿐이다. 그 밖의 '무음'은 룸톤 -30dB.
- **BGM은 대본 `M:`이나 화면 속 음악(연습·연주·라디오·극장 반주)에만 있다.** 94분 대부분은 생활 소리와 아이들의 악기가 음악을 맡는다.
- 비발디 「사계」 '여름'·「도라지 타령」은 공개 저작물의 선율로만 쓴다(특정 녹음·편곡 금지, 가사 없음). 「섬의 하루」는 작중 창작곡이다.
- 킷의 `storyboard/outputs/`(컷당 1샷 요약)는 이 패키지에 넣지 않았다. 참고용이었고, 애니 정본은 `anim/`이다.

## 5. 검수 체크리스트 (그림 한 장마다)

- [ ] 인물 얼굴·머리·체형이 `design/style_guide.md` 6절 고정 문구와 턴어라운드에 맞는가. 고유 표식: 은주 이마를 드러낸 잔머리·소리굽쇠 목걸이(목걸이 상태는 컷 프롬프트대로), 동민 빠진 앞니·무릎 반창고, 만석 낡은 작업모·긴 손가락, 곽 영감 이마의 돋보기·귀의 연필·굽은 오른손 약지·새끼, 선영 둥근 금테 안경, 최 계장 뿔테·땀·손수건, 미자 코의 반창고, 덕수 한 칸 밀린 단추.
- [ ] 의상이 그 씬의 의상(`design/outfit_schedule.json`, 컷 프롬프트 [CHAR])과 같은가. 은주 장갑: 쓰레기 산·일상은 일반 목장갑, 2화 겨울 연주는 손끝 자른 목장갑, 집 안·실내 무대·3화 여름 연주는 맨손.
- [ ] 빛·대표 색·그림자 색이 씬 프리셋과 맞는가. 그림자에 검정·회색을 섞지 않았는가.
- [ ] 소리 색은 프롬프트에 [SOUND]가 있는 컷에만 있는가. 조롱 웃음·에필로그 이중주에는 색이 없는가.
- [ ] 넘지 않는 선: 아이들은 제 나이의 평범한 아이(꾸밈·노출 없음), 쓰레기 산에서 목장갑·장화, 위험물 맨손 없음, 던지는 컷은 물건만, 엄마 얼굴 없음, 최 계장 얼굴은 1화 S#16까지 없음, 부상·피 없음, 실제 로고·화폐·올림픽 마스코트 없음.
- [ ] 1987~88 고증: 쓰레기 산은 꼭대기가 평평한 탁자형·층진 비탈, 판잣집 동네(의도적 각색), 국민학교 자유복.
- [ ] 이미지 안에 글자가 없는가.

## 6. 미확인·잠정·후속

- 분할 컷 한 장 생성 가능 여부(미확인, 2단계 처음에 시험).
- 2화 웹툰 순서: 2-053(장갑 손끝 자르기)이 1월 장면(2-054~)보다 앞이다. 애니는 대본 순서(S#17부터). 웹툰 2-059·2-061 작화 때 장갑 상태 확인.
- G9 잠정: 연습실·공방 실내 신발은 worn canvas sneakers.
- 디자인 데이터 정리 후보(콘티 사양에서 컷별로 덮어썼으므로 그림에는 영향 없음): 씬 프리셋 3-34 동민 중복, 3-17 동그리 상태 키, 반복 단역 고정 문구.
- 1987년 쓰레기 산 높이는 미확인(최종 높이보다 낮게).

## 7. 다시 만들기·점검 (원본 저장소에서)

```
python3 tools/handoff.py manifest && python3 tools/handoff.py check && python3 tools/handoff.py pack
python3 tools/cut_prompts.py build                 # 컷 프롬프트
python3 tools/direction_scenes.py check && python3 tools/direction_scenes.py merge   # 연출 노트
python3 tools/anim_check.py check && python3 tools/anim_check.py build             # 애니 콘티·큐 시트
```
