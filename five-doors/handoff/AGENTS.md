# AGENTS.md — Codex 작업 지침 (「단톡방에 그 남자가 있다」 작화 파이프라인)

## 역할
Codex는 그림 자체를 판단하지 않는다. 다음 일을 맡는다.
- 프롬프트 조립
- 파일 정리와 이름 규칙 적용
- 매니페스트 관리
- 일관성 검수 보조
- 레터링(말풍선, 효과음, 내레이션)
- 회차 조립

기준 문서와 우선순위는 `README.md` 2절을 따른다.

## 파일 이름 규칙
- 인물 레퍼런스: `refs/characters/<id>_<sheet>_v<N>.png`
  - id: dogyeom, yujin, miran, sera, harin, hyesuk, sunok
  - sheet: turnaround, expressions, outfits-a, outfits-b, hand, keyvisual
- 소품: `refs/props/P<번호>_<이름>_v<N>.png` (예: `P2_shoppingbag_v1.png`)
- 배경: `refs/sets/S<번호 두 자리>_<이름>_<시간대>_v<N>.png` (예: `S02_winebar_closing_v1.png`)
- 컷(콘티 이후): `renders/ep<회차>/<컷번호>_v<N>.png` (예: `renders/ep1/1-014_v2.png`). 컷 번호는 콘티 표의 '컷' 열을 그대로 쓴다.
- 확정본은 매니페스트의 `status`를 `approved`로 바꾼다. 파일 이름의 버전은 유지한다.

## 매니페스트 `asset_manifest.csv`
열: `file,kind,subject,variant,track,prompt_ref,tool,status,approved_by,notes`
- status 값: `todo` → `generated` → `approved` / `rejected`
- `prompt_ref`: 사용한 프롬프트의 위치(예: `characters/yujin.md#턴어라운드`)
- 새 이미지를 저장하면 한 줄을 추가한다. 같은 subject와 variant 안에서 approved는 하나만 둔다.

## 프롬프트 조립 규칙
최종 프롬프트는 아래 순서로 이어 붙인다.
1. `style_lock.md`의 트랙 문구(트랙 1·2·3 중 하나)
2. 등장인물마다 `characters/<id>.md`의 CHARACTER LOCK. 여러 명이면 인물마다 문단을 나눈다.
3. 장소의 `sets.md` SET LOCK과 장면 시각의 조명 줄(장소 '시간대별 조명'에서 해당 회차·시각)
4. 소품 클로즈업이면 `props.md`의 PROP LOCK
5. 컷 지시(콘티의 샷·앵글·화면)
6. 끝맺음: `no text, no watermark, no logos, fictional adult characters`

- LOCK 문장은 한 글자도 바꾸지 않는다.
- 인물 사이 구분이 필요하면 `characters/README.md`의 다인 컷 규칙을 덧붙인다.

## 검수 보조
- 이미지마다 `README.md` 5절 체크리스트를 `notes` 열에 기록한다. 예: `ok:face,hair; miss:scar`
- 다섯 여자가 함께 나오는 컷은 대표 색(회색·버건디·민트·하늘색·금색)이 각각 보이는지 확인한다.
- 수위 규칙 위반이 의심되면 `rejected`로 두고 이유를 남긴다. 직접 고치거나 피해 가는 프롬프트를 만들지 않는다. 가림 장치 대안만 제안한다.

## 컷 단계 (콘티·프롬프트 완료 — 2026-10-07)
1. 컷 프롬프트는 이미 조립되어 있다: `prompts/ep<회차>.jsonl`(1화 파일에 표지 0-001~0-003 포함).
   - 한 줄이 컷 하나다. 필드는 다음과 같다.
     - `cut`, `size`(예 `800x1200`), `track`(1·2·3), `chapter`, `scene`, `flags`(`intimate`·`child_present`·`violence`)
     - `characters`(id), `sets`(S01~S10·SA·SB·SC), `props`(P1~P10)
     - `prompt`(그대로 생성기에 넣는 문자열), `safety`(금지·수위 규칙)
     - `refs`(첨부할 확정 레퍼런스 경로 패턴), `lettering`(레터링 줄)
   - 사람이 읽는 같은 내용이 `prompts/ep<회차>_prompts.md`에 있다.
   - LOCK이나 콘티를 고쳤으면 원본 저장소에서 다시 만든다. `five-doors/storyboard`에서 `build_kit_data.py` → `kit.py import --replace`를 돌리고, 이어서 `five-doors/tools/build_handoff.py`를 돌린다. 직접 고치지 않는다.
2. `refs` 패턴에 맞는 `approved` 레퍼런스를 매니페스트에서 찾아 생성 요청에 첨부한다. 없으면 그 컷은 `todo`로 둔다.
3. 생성 결과는 `renders/ep<회차>/<컷번호>_v<N>.png`로 저장하고, 매니페스트 해당 줄(`kind=cut`)의 status를 갱신한다.
4. 레터링: `storyboard/cuts.json`의 `lines`를 쓴다. 줄 종류(`type`)는 dialogue·narration·thought·whisper·sfx·caption이다.
   - 대사는 Gowun Dodum, 내레이션은 Gowun Batang 박스에 넣는다.
   - 효과음은 본편이면 East Sea Dokdo, [트랙2] 컷이면 Black Han Sans, 손글씨는 Nanum Pen Script다.
   - 크기·색은 SFX 괄호값을 따른다(`story/sfx_list.md`, `story/direction.md` 5절).
   - 화자 표기에 따라 말풍선이 정해진다.
     - `(전화)`: 톱니 풍선
     - `(V.O.)`: 점선 풍선
     - `문자(…)`: 가상 UI 말풍선
     - `다섯:`: 풍선 하나에 꼬리 다섯, 꼬리 끝에 대표 색 점
   - 말풍선 위치는 콘티 화면 칸의 지시(좌상·우하 등)를 따르고, 한 컷에 대사 풍선은 2개까지만 둔다.
5. 조립
   - 회차별 세로 스크롤 이미지: 폭 800px. 컷 사이 여백은 기본 40px, 장면 전환 120px, 반전 직전·충격 직후 240px, 회차 끝 360px.
   - 쇼츠용 9:16 컷 묶음은 원본 저장소 킷 `five-doors/storyboard/outputs/shorts`의 대본과 `shorts_ffmpeg/` 스크립트를 쓴다.
6. 애니·모션코믹: `anim/storyboard_anim.md`(샷 번호 `<회차>S<씬>-<번호>`, 24fps)와 `anim/sound_cues.md`(타임코드)를 기준으로 한다.

## 금지
- 실제 브랜드 로고, 실제 화폐 도안의 정밀 재현, 실존 인물과 닮은 얼굴.
- 이미지 안의 글자(레터링 단계 제외).
- 성기·성행위 직접 묘사, 미성년으로 보이는 표현, 관능 컷에 아이를 넣는 것.
