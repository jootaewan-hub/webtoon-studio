# 산출물 목록

`python studio.py init <이름>`이 아래 구조와 템플릿을 만든다.

```
<프로젝트>/
  project.md            접수 결과(원문, 각색 수준, 등급, 분량, 범위, 기본값)
  decisions.md          결정 로그(게이트별 확정·잠정)
  source/original.md    받은 원문 그대로
  research/notes.md     고증 노트(출처 포함)
  story/
    pitch.md            로그라인·기획 의도·결말 방향 (G1)
    bible.md            캐릭터 바이블 (G2)
    synopsis.md         시놉시스·회차 구성 (G3)
    beats.md / beats.json  비트 시트 (G3)
    novel.md            소설 (G4)
    script.md           대본 (G5)
    direction.md        연출 노트 (G10)
    sfx_list.md         효과음·사운드 큐 사전 (G10)
  design/
    style_options.md    그림체 3안 (G6)
    style.json          확정 스타일 (G6)
    characters.json     인물 외형 고정값·시안 (G2·G7)
    sheets/*.svg        턴어라운드·표정 시트, 시안 비교 (G7)
    props.json, props/*.svg, props_sheet.svg  소품 삽화 (G8)
    sets.md             배경 설정 (G8)
    colorscript.svg     컬러 스크립트
    board.html          디자인 보드 (artifact로 게시)
  storyboard/           webtoon-adaptation-kit 킷(콘티·썸네일·프롬프트·쇼츠·애니 트랙) (G9)
  anim/
    parts/ep<N>.md, ep<N>_skeleton.md  회차별 애니 콘티와 뼈대 (G11)
    storyboard_anim.md  애니메이션급 세부 콘티 합본 (G11)
    sound_cues.md       사운드 큐 시트 (G11)
  handoff/              작화 인계 패키지 (G12, 아래)
  docx/                 studio.py docx 결과(Word 사본)
  tools/                studio.py, md2docx.js, check_board.py, sfx_tools.py, direction_scenes.py, anim_tools.py, build_handoff.py (init이 복사)
```

## 형식
- 원본은 Markdown. `python tools/studio.py docx`로 내용이 채워진 md의 Word 사본을 `docx/`에 만든다(애니 콘티·큐 시트·결정 로그·고증은 가로 방향).
- 사용자가 Claude Docs나 Google Docs를 원하면 그쪽에 만들고, 같은 내용을 Markdown으로도 남긴다(킷이 Markdown을 읽기 때문).
- 디자인 보드와 콘티 보드는 artifact로 게시한다. 게이트마다 같은 주소로 갱신한다.
- 끝에 `python studio.py pack`으로 zip.

## 보고 형식 (매 게이트 끝, 그리고 마지막)
- 확정한 것(decisions.md 기준)과 잠정인 것
- 만든 파일
- 다음에 고를 것
- 확인하지 못한 사실, 기본값으로 정한 것

## G12 작화 인계 패키지 (`handoff/`)

ChatGPT·Codex·사람 작가가 이 폴더 하나로 작품 전체를 그릴 수 있게 만든다. `python3 tools/build_handoff.py`가 아래 자동 생성분을 만든다. README·지침 문서는 Claude가 작품에 맞게 쓴다.

```
handoff/
  README.md                        작업 순서, 기준 우선순위, 도구 경로, 검수 체크리스트, 미확인 사항
  CHATGPT_PROJECT_INSTRUCTIONS.md  ChatGPT 프로젝트 '지침' 문구(임의 변경 금지·변경 보고 포함) + 올릴 파일 우선순위
  AGENTS.md                        Codex 지침(파일 이름, 매니페스트, 프롬프트 조립, 레터링, 회차 조립)
  IMAGE_TOOLS.md                   도구 경로 A·B, 거절·변경 대응, 도구 현황(확인 날짜·출처)  ← references/image_tools.md
  style_lock.md / characters/<id>.md / props.md / sets.md   LOCK 원본
  prompts/ep<N>_prompts.md         컷별 '그대로 복사' 프롬프트 + 수위 + 레퍼런스 + 도구 경로 + 레터링   (자동)
  prompts/ep<N>.jsonl              같은 내용 기계용: cut,size,track,route,flags,characters,sets,props,prompt,safety,refs,lettering (자동)
  storyboard/ (storyboard.md·docx, cuts.json, chapter_notes.json, SPEC.md)   (자동 복사)
  story/ (novel, script, bible, pitch, beats, direction, sfx_list)           (자동 복사)
  anim/ (storyboard_anim.md, sound_cues.md)                                   (자동 복사)
  decisions.md                                                                 (자동 복사)
  asset_manifest.csv               레퍼런스(인물×시트, 소품, 장소) + 컷 전부, status=todo, tool=경로별   (자동)
  refs/, renders/                  사람·Codex가 채움
```

- **컷 프롬프트 조립 순서**: 트랙 문구(`[트랙2]` 컷은 코미디 문구) → 화면에 나오는 인물의 CHARACTER LOCK(앵글 칸의 POV 대상은 제외, 오버숄더의 어깨 주인은 포함) → 장소 SET LOCK → 소품 클로즈업이면 PROP LOCK → 장면 연출 메모(조명·의상) → 컷 지시(말풍선·효과음·식자 문장은 뺀다) → 금지 문구.
- **도구 경로**: `storyboard/data/flags.json`의 `route_b_keywords`(노출·탈의 단서)로 B를 판정한다. 소품 판정 키워드는 `storyboard/data/props.json`이다.
- **zip**: 인계 폴더를 zip으로 묶어 사용자에게 보내고, 저장소에는 넣지 않는다(`.gitignore`의 `dist/`·`*.zip`).
