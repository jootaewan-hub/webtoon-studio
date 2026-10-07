# 이어서 작업하기 (Claude Code)

최종 정리: 2026-10-07 23:55 KST. 「단톡방에 그 남자가 있다」는 G0~G12 문서 작업이 끝났다. 남은 일은 그림(ChatGPT·Codex)과 사용자 검토다.

## 0. 다른 컴퓨터에서 시작하는 법

```bash
git clone https://github.com/jootaewan-hub/webtoon-studio.git
cd webtoon-studio
git checkout g9-g11-storyboard   # main에 합치기 전까지 최신 작업은 이 브랜치에 있다
npm i -g docx                    # 문서 변환(md → docx)에 필요. Node 18+
claude                           # Claude Code 실행
```

스킬 두 개(`webtoon-story-studio`, `webtoon-adaptation-kit`)는 `.claude/skills/`에 들어 있다. `skills/*.skill`은 claude.ai 업로드용 패키지본이다.

## 1. 저장소 구성

| 폴더 | 내용 |
|---|---|
| `five-doors/` | 「단톡방에 그 남자가 있다」 프로젝트(G0~G12) |
| `five-doors/handoff/` | **ChatGPT·Codex 최종 인계 패키지**. 여기부터 보면 된다 |
| `nakdong-kit/` | 이전 작품 「낙동강을 헤엄쳐 나온 남자」 제작 킷 |
| `skills/` | 스튜디오·킷 스킬 원본과 .skill 패키지 |
| `research/episode_candidates.md` | 소재 후보 조사 |

## 2. 「단톡방에 그 남자가 있다」 진행 상태

결정 로그는 `five-doors/decisions.md`에 있다.

| 게이트 | 상태 | 산출물 |
|---|---|---|
| G0~G8 | 확정(이전 세션) | `story/`, `design/`, `handoff/characters·props·sets·style_lock` |
| G9 웹툰 콘티 | 작성 완료. 571컷, 원작 대사 누락 0, 수위 검수 반영 | `storyboard/parts/ep1~6.md`, 합본 `storyboard/source/storyboard.md`·`.docx`, 킷(`storyboard/data`, `outputs`, `tools/editor_ready.html`) |
| G10 연출 노트·효과음 | 작성 완료. 효과음 표기와 BGM 체계는 추천안 잠정 | `story/direction.md`(1부 원칙 + 2부 장면 95개), `story/sfx_list.md` |
| G11 애니메이션 콘티 | 작성 완료. 혼합 밀도 잠정, 988샷, 약 69.8분 | `anim/parts/ep1~6.md`, 합본 `anim/storyboard_anim.md`, `anim/sound_cues.md` |
| G12 인계 | 완료 | `handoff/`(README, ChatGPT 지침, AGENTS, 컷 프롬프트 571개 md·jsonl, 매니페스트 636행) |

## 2-1. 2026-10-08 추가

- **스킬 개선**: `webtoon-story-studio`, `webtoon-adaptation-kit`.
  - G2 인물 심화를 소설 전 필수로 바꿨다.
  - 끝까지 진행 모드, 검사·인계 도구 5종, kit.py v2, 이미지 도구 경로 문서를 넣었다.
  - `skills/*.skill` 패키지와 `.claude/skills/`를 갱신했다.
- **five-doors 인계 보완**
  - 컷별 도구 경로: A 505컷 / B 66컷
  - `handoff/IMAGE_TOOLS.md` 추가
  - ChatGPT 지침에 임의 변경 금지·변경 보고를 넣었다.
- **남은 어긋남**: 소설 2곳의 '동그란 안경'이 바이블 0-2(금테 타원)와 다르다. 콘티·프롬프트는 바이블을 따른다.

## 3. 다음에 할 수 있는 일

1. **사용자 검토.**
   - 잠정 결정(G10 효과음·BGM, G11 밀도, 6화 마지막 컷 처리)을 확정한다.
   - 콘티의 '콘티 지정' 의상이 바이블에 없던 값인지 확인한다.
2. **연속성 정밀 검수.** 이번 세션에서는 사용자가 중단한 단계다. 자동 점검(날짜·요일, 인물 표기, 회차 경계)만 했다.
   - 필요하면 1~3화, 4~6화로 나눠 의상 HEX·소품·조명 연속을 검수한다.
3. **그림.**
   - `handoff/CHATGPT_PROJECT_INSTRUCTIONS.md`대로 ChatGPT 프로젝트를 만든다.
   - 인물 레퍼런스 → 소품 → 장소 → 컷 571장 순서로 진행한다.
4. **애니 압축(선택).** 같은 구도의 분할 칸을 한 샷으로 합치면 988샷을 약 800샷으로 줄일 수 있다(추정입니다).
5. **브랜치.** `g9-g11-storyboard`를 main에 합친다(사용자 승인 후).

## 4. 고친 뒤 다시 만드는 순서

```bash
cd five-doors/storyboard
python3 from_studio.py && python3 kit.py import --replace && python3 kit.py validate
python3 kit.py prompts --track all && python3 kit.py docx && python3 kit.py editor
cd ..
python3 tools/direction_scenes.py              # 연출 노트 2부
python3 tools/anim_tools.py check <회차>        # 애니 콘티 검사(merge, cues도 있음)
python3 tools/build_handoff.py                 # handoff/ 다시 만들기
```

콘티 검사기(형식·원작 대사 대조)는 `five-doors/tools/check_board.py <five-doors 경로> <회차> [--list]`다.

## 5. 꼭 지킬 사용자 선호와 원칙

- 한국어로 답한다. 사실에 근거하고, 확인 못 한 것은 "미확인", 추측은 "추측입니다"라고 밝힌다.
- 브레인스토밍 방식으로 단계마다 2~4개 안을 낸다. 사용자가 "진행", "끝까지"라고 하면 추천안으로 가고, 잠정으로 기록한다.
- **그림은 Claude가 그리지 않는다.** 사양·프롬프트·콘티만 만든다. 썸네일도 그리지 않는다.
- 수위
  - 낙동강보다 과감하게 쓴다: 몸 라인, 부분 노출, 감각적인 정사 장면.
  - 성기·유두·행위의 직접 묘사·체액은 쓰지 않는다.
  - 아이들은 관능 장면에 두지 않는다. 모든 인물은 성인이다.
- 실화 모티프다. 인물·지명·회사는 가공이고, 실제 브랜드 로고와 실제 화폐 도안은 쓰지 않는다.

## 6. 외부 자산 위치

- 시안 이미지는 Canva·Gamma 계정에 있다. 링크는 `five-doors/design/gen/prompts.md`와 `handoff/characters/_g7_generation_log.md`에 있다.
- 게시한 artifact(claude.ai): 「단톡방 그림체 보드」(G6), 「낙동강」 썸네일 보드와 웹툰 페이지.
