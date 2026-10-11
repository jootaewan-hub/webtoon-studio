# AGENTS.md — Codex 작업 지침 (「깡통 바이올린」 작화·레터링 파이프라인)

## 역할
Codex는 그림을 판단하지 않는다. 다음을 맡는다.
- 프롬프트 꺼내 주기(정본은 이미 조립돼 있다: `storyboard/out/cel/<컷>.md`)
- 파일 이름·폴더 정리, `handoff/asset_manifest.csv` 관리
- 검수 보조(README 5절 체크리스트, 아래 자동 점검)
- 레터링(말풍선·내레이션·효과음·게시판 글자)과 회차 조립

기준과 우선순위는 `handoff/README.md` 2절. 확정 결정은 `decisions.md`.

## 파일 이름
- 인물: `renders/characters/<id>_<sheet>.png` — id는 eunju, dongmin, manseok, kwak, seonyoung, choi, taejun, mija, deoksu, sunrye, bonggu, yeongran, gyeongho, gyeongmin, suni, seoki. sheet는 turnaround, expressions, outfits, 2003, flashback.
- 소품: `renders/props/<소품 id>.png` (id는 `design/gen/prop_prompts.md`의 `[대괄호]`, 예 `dongguri__s2_thrown`).
- 배경: `renders/sets/<장소 id>.png` (예 `junk_shop_in`).
- 컷: `storyboard/renders/cel/<컷 번호>.png` (예 `1-003.png`). 분할 컷을 칸마다 따로 만들면 `<컷>_a.png`, `_b.png`, `_c.png`(위에서 아래로)로 두고 조립 때 붙인다.
- 다시 만든 판은 덮어쓰지 말고 `_v2`를 붙인다. 확정본만 대장 `file` 이름으로 둔다.

## 대장 `handoff/asset_manifest.csv`
열: `file,kind,subject,variant,order,prompt_ref,tool,status,approved_by,notes`
- `order`: 1 인물 → 2 소품 A → 3 소품 B → 4 소품 C → 5 배경 → 6-1/6-2/6-3 화별 컷. 이 순서로 만든다.
- `status`: `todo` → `generated` → `approved` / `rejected`. 승인은 사람(`approved_by`)이 한다.
- `notes`에 "참고 이미지 필수"가 있는 컷 17개는 등장인물·소품·배경 기준 이미지를 모두 첨부해 생성한다.
- 대장을 다시 만들 때는 원본 저장소에서 `python3 tools/handoff.py manifest`(이미 채운 status·approved_by·notes는 file 기준으로 보존된다).

## 컷 생성 보조
- 컷 프롬프트는 `storyboard/out/cel/<컷>.md`를 그대로 쓴다. 문장을 고치지 않는다. 고칠 일이 생기면 원본 저장소에서 `storyboard/source/cut_spec_ep*.jsonl`을 고친 뒤 `python3 tools/cut_prompts.py build`로 다시 만든다.
- 첨부할 기준 이미지: 컷 프롬프트의 [CHAR] 인물 턴어라운드, [PROP] 소품, [SET] 배경. 소품은 상태 단계 id까지 맞춘다(예 동그리 `__s7_e_broken`).
- 콘티 칸의 크기(800×1000 등)를 지킨다. 결과 비율이 다르면 다시 만든다(자르지 않는다).

## 레터링 (웹툰)
글꼴은 Google Fonts(OFL). 기준은 `design/style_guide.md` 3절, `story/direction.md` 1부 4~6절, `story/sfx_list.md`.

| 요소 | 글꼴 | 모양 |
|---|---|---|
| 대사 | Gowun Dodum | 흰 둥근 풍선, 진갈색 #2B2420 2px 테두리. 한 컷 최대 3개·두 화자(1-012만 4개) |
| 화면 밖 목소리 `(E)` | Gowun Dodum | 둥근 풍선, 꼬리를 소리 나는 쪽 화면 가장자리 밖으로. 합판 벽 너머는 벽 쪽으로. 고함(2-042)은 들쭉날쭉 테두리 |
| 회상 위 지금의 목소리(3-013) | Gowun Dodum | 꼬리 없는 사각 풍선 |
| 전화·라디오·확성기 `(F)` | Gowun Dodum | 톱니 테두리 풍선 |
| 내레이션(어른 은주) | Gowun Batang | 크림색 반투명 사각 박스 #FFF8EA 85%, 테두리 없음, 컷 위쪽 가장자리. 2-090만 박스 없이 다음 무음 칸(#232C4A) 위에 크림색 글자 |
| 효과음 ① 소리 색 | 큰 소리 Gaegu Bold / 작은 소리 Nanum Pen Script | 그 소리 색 HEX + 흰 2px 번짐, 컷 폭 25~45%. 3-113~3-114 '밤'은 글자 없음 |
| 효과음 ② 소리 서명 | Nanum Pen Script | 진갈색, 15~25%, `story/sfx_list.md` 2절의 고정 모양(리어카 +8°·덜컹 반 글자 처짐, 국자 세 계단/두 계단, 벽·문 두 글자 나란히, 라디오는 몸통 위 지그재그, 소리굽쇠 긴 줄) |
| 효과음 ③ | 일상 소음 Gaegu Regular 회갈색 #8A7A6A / 그 밖 Nanum Pen·Gaegu Bold 진갈색 | 8~15%. 한 칸에 셋 이상이면 하나만(예외 2-009·2-015·2-040·3-147). 조롱 웃음(2-069·3-044·3-081)은 25% 색 없음 |
| 손글씨(게시판·칠판·쪽지) | Nanum Pen Script | 종이 색 위에 |
| 공문·신문 | Nanum Myeongjo | 인서트 컷 안에서만 |

- 콘티 SFX 중 괄호로만 된 것(`(동그리 선율)` 등)과 앞 괄호(`(멀리)`)는 글자로 얹지 않는다. 뒤 괄호(`와르르(웃음)`)는 뜻풀이라 괄호 안을 얹지 않는다.
- 소리 색 컷에는 그림에 이미 빛 띠가 있다. 글자는 그 띠를 따라 휘게 둔다. 말풍선과 겹치지 않는다.

## 회차 조립 (세로 스크롤)
- 폭 800px. 컷 사이 여백은 `story/direction.md` 1부 1절: 기본 40, 장면 전환 160(장소 색 10% 띠, 색이 바뀌면 두 색 그러데이션), 소리 색 컷 앞 240, 이어지는 소리 색 컷끼리 80, 장면 첫 컷이 소리 색이면 240 하나에 그러데이션. 컷마다 정확한 값은 `story/direction.md` 2부 장면별 '템포' 줄.
- 무음 칸(테두리 없는 빈 칸, 높이 600) 네 곳: 1-080과 1-081 사이(#6E5640 5%), 2-090 뒤(#232C4A, 내레이션), 3-126 뒤(#FFFFFF), 3-150 뒤(#3F5A6A 5%). 콘티 컷 번호가 없는 레이아웃 요소다.
- 결과: `storyboard/renders/episodes/ep<N>.png`(긴 원본)와 업로드용 조각 `ep<N>_<세 자리>.png`. 조각 높이는 플랫폼 규격을 따른다(규격 미확인 — 받기 전에는 1,280px 이하로 자르되 컷 중간을 피한다).
- 쇼츠(9:16)는 이 패키지 범위 밖이다. 필요하면 원본 저장소 킷의 shorts 트랙을 참고한다.

## 자동 점검 (조립 전)
- 대장의 `approved` 컷이 353개인지, 파일이 실제로 있는지.
- 컷 이미지 크기 비율이 콘티 칸과 같은지(±2%).
- 레터링 대사가 `storyboard/source/storyboard.md`의 대사 칸과 글자 하나까지 같은지(대본 대사 351줄은 콘티에 누락 0으로 검증됨).
