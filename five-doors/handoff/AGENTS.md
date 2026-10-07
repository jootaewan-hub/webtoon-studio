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

## 컷 단계 (콘티가 추가된 뒤)
1. 콘티 표(`| 컷 | 크기 | 샷·앵글·인물 | 화면·연출 | 대사·내레이션·SFX |`)를 파싱한다.
2. 컷마다 위 규칙으로 프롬프트를 조립해 `prompts/ep<회차>.jsonl`로 낸다. 필드는 `cut`, `size`, `track`, `prompt`, `refs`(업로드할 레퍼런스 파일 목록)다.
3. 사람이나 ChatGPT가 이미지를 생성하면 `renders/`에 규칙대로 저장하고 매니페스트를 갱신한다.
4. 레터링
   - 대사는 Gowun Dodum, 내레이션은 Gowun Batang 박스에 얹는다.
   - 효과음은 본편이면 East Sea Dokdo, 코미디면 Black Han Sans, 손글씨는 Nanum Pen Script를 쓴다.
   - 말풍선 꼬리는 화자 입을 향하고, 한 컷에 말풍선은 2개를 넘기지 않는다.
5. 조립
   - 회차별 세로 스크롤 이미지: 폭 800px, 컷 사이 여백은 기본 40px, 장면 전환 120px, 반전 직전 240px.
   - 쇼츠용 9:16 컷 묶음.

## 금지
- 실제 브랜드 로고, 실제 화폐 도안의 정밀 재현, 실존 인물과 닮은 얼굴.
- 이미지 안의 글자(레터링 단계 제외).
- 성기·성행위 직접 묘사, 미성년으로 보이는 표현, 관능 컷에 아이를 넣는 것.
