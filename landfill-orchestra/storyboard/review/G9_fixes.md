# G9 검수 반영 기록 — 「깡통 바이올린」

- 반영일: 2026-10-10
- 지시서: `storyboard/review/G9_review.md` 표 1~24번
- 고친 파일: `storyboard/source/storyboard.md`, `storyboard/source/cut_spec_ep1~3.jsonl`
  - 도구(`tools/cut_prompts.py`)와 `design/`·`scene_index.md`는 고치지 않았다.
- 대본 대사는 바꾸지 않았다. 353행 전체에서 대사 칸을 백업과 대조했다. 바뀐 칸은 다음 셋뿐이다.
  - 2-024: 이름표(20번)
  - 3-093: SFX 색 표기(6번)
  - 3-095: SFX 한 항목 삭제(15번)
- 컷 수와 번호는 그대로다(113·90·150, 합계 353).
- 표의 컷 번호 뒤 `*`는 지시서 목록 밖에서 같은 원칙으로 고친 컷이다. 이런 컷은 43개다.
- 3-057은 지시 7번("회상 칸이 있는 분할 컷은 cut_en에 flashback")과 일부러 다르게 했다. 그 이유는 표 7번 줄에 적었다.

## 1. 반영 표

| 번호 | 컷 | 한 일 |
|---|---|---|
| 1 | 2-078, 2-079, 2-080, 3-029 | 미자 outfit에 목장갑·고무장화를 넣었다(2-047 문구). 2-078 cut_en을 "Mija in work gloves and rubber boots"로 고쳤다. 3-029 cut_en을 "in rubber boots … in her gloved hand"로 고치고, 뒤의 아이들에 "white cotton work gloves and rubber boots"를 넣었다. 화면 칸에 목장갑·장화 차림을 적었다(3-029는 "목장갑 낀 손으로"). |
| 1 | 3-027 | 참고 컷. cut_en과 화면 칸 위 칸에 고무장화를 명시했다. 은주 outfit은 칸별로 지정했다(위 고물 더미: 목장갑·고무장화, 아래 공방: 맨손·운동화). |
| 1 | (2·3화 전체 점검) | 쓰레기 산 배경(small_hill_*, scrap_heap, soup_tent_back)에 아이가 나오는 컷을 모두 확인했다. 위 다섯 컷 말고는 빠진 곳이 없었다(2-047·2-048은 이미 덮어씀). |
| 2 | 2-084, 2-090, 3-001, 3-002, 3-003, 3-005*, 3-006, 3-007, 3-008, 3-009, 3-012, 3-014, 3-015, 3-017, 3-018 | `"pendant": false`를 넣었다. 범위는 2-083 ③(상자에 넣음) 다음 컷부터 3-019(다시 걸어 줌) 직전까지이고, 은주가 보이는 컷은 모두 넣었다. 3-005(맨손 손끝 극접사)는 지시서 목록에 없었다. 조립본의 은주 [CHAR]은 모두 "no necklace, bare neck"로 끝난다. |
| 2 | 2-084, 2-090 | char_text에서 ", a small silver tuning-fork pendant on a thin chain"을 지웠다. |
| 2 | 2-062 | `"pendant": "hidden"` |
| 2 | 2-063*, 2-065*, 2-066*, 2-069* | `"pendant": "hidden"`. 2-18·2-19 흰 블라우스 씬의 scene_index 소품이 `tuning_fork_necklace__s2_under_blouse`라서 2-062와 같은 상태로 맞췄다. |
| 3 | 2-003, 2-004, 2-005*, 2-009*, 2-010*, 2-035, 2-036*, 2-037, 2-038*, 2-040*, 2-041*, 2-042*, 2-043* | outfit: 천막 연주·연습. "…, rubber boots, bare hands (the white cotton gloves stuffed in the jacket pocket)". ep1 1-101·1-103 관행대로 천막에서는 장화를 둔다. 같은 연습·연주 자리의 컷은 손이 보이지 않아도 함께 맞췄다. |
| 3 | 2-070*, 2-073* | outfit: 천막에서 밥 먹는 손. 장갑은 주머니에 넣고 맨손이다(2-073은 숟가락 쥔 손 극접사). |
| 3 | 2-011, 2-012, 2-013, 2-014, 2-015, 2-017, 2-018, 2-019, 2-020, 2-022 | outfit: 연습실. "…, worn canvas sneakers, bare hands, no gloves, no boots" |
| 3 | 2-051* | outfit: 공방 연주(초겨울). 겨울 문구에서 장갑·장화를 뺐다(장갑은 주머니, 맨손, 운동화). |
| 3 | 2-053* | outfit: 장화를 빼고 운동화로 바꿨다(공방 실내). 손끝 자른 목장갑은 이 컷의 뜻이라 그대로 둔다. |
| 3 | 2-081, 2-082, 2-083, 3-007, 3-008, 3-009, 3-012, 3-014, 3-015, 3-017, 3-018, 3-019, 3-020 | outfit: 집 안. "an oversized navy work jacket (hand-me-down), worn trousers with frayed knees, socks, no gloves, no boots". 3-020은 집 안 연주라 이것으로 맨손이다. |
| 3 | 3-031* | outfit: 집 안(여름). 여름 문구에서 조건절(장화·장갑은 쓰레기 산 작업 때만)을 빼고 양말로 지정했다. |
| 3 | 3-028*, 3-030*, 3-032*, 3-040*, 3-041*, 3-042*, 3-043*, 3-045*, 3-046*, 3-048*, 3-063*, 3-064*, 3-065*, 3-066*, 3-067*, 3-068*, 3-069* | outfit: 공방(여름). "a faded light-blue short-sleeved cotton shirt, worn trousers with frayed knees, worn canvas sneakers, bare hands, no gloves, no boots". 여름 문구의 장갑·장화 조건절이 그림에 끼지 않게 했다. |
| 3 | 3-024*, 3-025* | outfit: 공방. 장화를 빼고 운동화로 바꿨다. 장갑은 남긴다(콘티 3-025 "목장갑 낀 손끝을 꼼지락거린다", 고물 작업 직후). |
| 3 | 3-036*, 3-037*, 3-038* | outfit: 공방에서 깡통 고르기. 장화를 빼고 운동화로 바꿨다. 장갑은 남긴다(콘티 3-036 "목장갑 낀 은주의 손이 깡통을 하나씩 두드린다", SPEC 7절 고물은 장갑). |
| 4 | 1-073 | `"colors": ["#E9EEF5", "#F5C04A"]` |
| 4 | 2-004 | `"colors": ["#F5C04A", "#4FB3A9"]` |
| 4 | 2-017 | `"colors": ["#F5C04A", "#E9EEF5"]` |
| 4 | 2-018 | `"colors": ["#5B8DEF", "#E9EEF5"]` |
| 4 | 3-022 | `"colors": ["#E9EEF5", "#9DB7C9"]` |
| 4 | 3-031 | `"colors": ["#B9A7D9", "#F5C04A"]` |
| 4 | 3-089 | `"colors": ["#F5C04A", "#E8944A"]`(2색) |
| 4 | 3-090 | `"colors": ["#D9534A", "#F5C04A", "#E8944A"]`(3색) |
| 4 | 3-092, 3-093 | `"colors": ["#4FB3A9", "#E8944A", "#F5C04A", "#D9534A"]`(4색) |
| 4 | 3-095 | `"colors": ["#E8944A", "#F5C04A", "#D9534A", "#4FB3A9"]`(누적 4색 유지) |
| 4 | 3-103 | `"colors": ["#E8944A", "#4FB3A9"]`(버팀 2색) |
| 4 | 3-107 | `"colors": ["#4FB3A9", "#E8944A"]` |
| 4 | 3-111 | `"colors": ["#E8944A", "#4FB3A9", "#D9534A"]`('밤' 시작, 금빛은 3-112부터) |
| 4 | 3-112*, 3-113, 3-114 | `"colors": ["#F5C04A", "#E8944A", "#4FB3A9", "#D9534A"]`('밤' 화면 전체). 3-112는 "모든 띠 위에 금빛"이라 지시서 목록 밖이어도 넣었다. |
| 4 | 3-042 | `"sound_style": "dots"`. colors는 넣지 않았다. 도구가 colors를 sound_style보다 먼저 보므로, colors가 있으면 dots 분기가 실행되지 않는다. 네 색 이름은 cut_en에 이미 있다. |
| 5 | 3-092 | cut_en 끝에 "…while the faint orange, gold and red bands from before still linger low across the stage, four colors now"를 붙였다. 화면 칸에도 "앞의 주황·금빛·빨강 띠가 무대 아래에 옅게 남아 있다"를 넣었다. |
| 6 | 3-093 | SFX "SFX(금빛 #F5C04A): 파다다닥" → "SFX: 파다다닥". sound는 꽥꽥이로 유지했다. 네 색은 화면 칸, cut_en, colors에 있다. |
| 7 | (확인) 3-010, 3-013, 3-058 | 회상만 있는 컷이다. cut_en이 "flashback"으로 시작하는지, 조립 [SCENE]이 회상 장소만인지 확인했다. |
| 7 | (확인) 3-3·3-12·3-21의 현재 시점 컷 | 조립 [SCENE]에 회상 장소가 붙지 않았다. 28컷 점검에서 문제 0건이다. |
| 7 | 3-057 | 아래 칸 회상의 장소는 섬의 천막 앞(set2)이다. 그런데 "flashback"이라는 낱말 때문에 [SCENE]에 1950년대 판자촌이 붙었다. 아래 칸을 "a brief memory insert from earlier on the island (not the 1950s)"로 바꿔 [SCENE] 사무실 + [SET-2] 천막으로 조립되게 했다. |
| 7 | 3-098* | 분할 컷이다(위: 무대 현재, 아래: 라디오 수리점 회상). set이 `fb_`라서 [SCENE]에 회상 장소만 붙었다. set=hanbit_hall, set2=fb_radio_shop으로 바꾸고 아래 칸을 "flashback, close on the workbench, …"로 시작하게 했다. 원래 spot `bench_close`는 회상 배경의 자리라 set에 둘 수 없어 지웠다. |
| 8 | 1-047 | set을 shack_main, spot을 section으로 했다. 아래 칸 좌우를 고쳤다: 동민은 왼쪽 부엌 겸 방, 은주는 오른쪽 쪽방. 샷 칸, 화면 칸, cut_en을 함께 고쳤다. 위 칸의 손 극접사는 그대로 둔다. |
| 8 | 2-084 | set을 shack_main, spot을 section으로 했다. 은주는 오른쪽 쪽방, 만석은 왼쪽 부엌 겸 방이다. 샷, 화면, cut_en을 함께 고쳤다. |
| 9 | 1-074 | 샷 칸: 곽 영감(우), 선영(중), 은주(좌). 화면 칸과 cut_en 위 칸: 선영이 애써 웃으며 사양하자 영감이 깡통을 받아 은주에게 내민다. |
| 10 | 3-018 | 샷 칸에 "은주(입가·위 가장자리)"를 더했다. |
| 10 | 3-019 | 가로 2분할로 바꿨다. 위: 만석의 긴 손가락이 사슬을 은주 목 뒤로 넘겨 점퍼 깃 위에 거는 손 극접사(얼굴은 위 가장자리). 아래: 기존 은빛 흰색 컷(말풍선 없음). 콘티의 샷·화면 칸과 cut_en을 함께 고쳤다. 크기 800×1600과 번호는 그대로다. 만석은 손만 나오므로 ep1 관행(손 컷은 chars를 비움)대로 chars에 넣지 않았다. |
| 11 | 3-149 | 아래 칸에 어른 동민이 함께 있다. 그래서 char_text는 어른 문구로 두었다. cut_en 가운데 칸은 "the same Dongmin as a nine-year-old boy, not the adult: round face, very short clipper buzz cut, upper-left front tooth missing, big ears, wrapped in a blanket …"으로 고쳤다. 아래 칸에는 "(the adult look applies to this frame only)"를 붙였다. |
| 12 | 3-073 | props `dongguri__s5_restored` → `dongguri__s6_worn_e` |
| 13 | 2-090 | 화면 칸: "귀에는 작은 창의 남색 달빛만 닿는다(소리 색 없음)". cut_en: "only faint navy moonlight from the small window falls on the ear, no glow, no light rings" |
| 14 | 3-054 | cut_en 포스터 구절을 "a plain wall poster with only unreadable blank lines suggesting a slogan, no emblem, no rings, no mascot"으로 바꿨다. |
| 15 | 3-095 | SFX 칸에서 "SFX(주황 #E8944A): (옅게 남은 띠)"를 지웠다. 화면 칸의 "무대의 네 색 띠는 옅게 남아 있다"는 그대로다. |
| 15 | 3-095 | SFX 색 표기를 빼자 sb_check에 "sound가 있는데 소리 색 표기가 없음" 주의가 생겼다. 그래서 화면 칸 첫머리에 "「섬의 하루」 '저녁' 음악의 첫머리."를 넣었다(scene_index 3-21 "[4. 저녁 시작]"이 근거). |
| 16 | 3-071, 3-053, 2-033, 3-138 | 손글씨·마커·날짜·명단 구절에 "with unreadable blank strokes suggesting text"를 붙였다. |
| 17 | 1-033, 2-028, 2-029, 2-075 | 지폐·동전 구절을 "plain fictional bills (and coins) with no real currency design"으로 통일했다. |
| 18 | 1-092 | 손뼈 구절을 "a clean, cartoonish white silhouette of a waving hand skeleton with five spread fingers …, no medical or injury look"로 바꿨다. |
| 19 | 3-103 | cut_en: "seen at a distance … the long skirt of her white dress, below the knee, swaying behind her as she runs". 화면 칸도 같은 뜻으로 고쳤다. |
| 20 | 2-024 | "최 계장(속삭임):" → "최 계장:". 속삭임은 화면 칸의 작은 점선 말풍선으로 보인다. |
| 21 | 1-067 | 샷 칸: 곽 영감(좌·그늘), 선영(우). cut_en의 좌우도 함께 바꿨다. |
| 22 | 1-083 | chars에 seonyoung을 더했다. |
| 23 | 3-134 | props `choi_handkerchief__s1_dry` → `choi_handkerchief__s2_damp` |
| 24 | 2-053 | 화면 칸 "겨울 공방" → "초겨울 공방", cut_en "early-winter workshop". 순서는 지시서대로 그대로 둔다. |

## 2. 반영하지 않았거나 일부만 반영한 것

| 번호 | 내용 | 이유 |
|---|---|---|
| 2 | 장기 권고: 펜던트를 고정 문구에서 빼고 소품 키로만 붙이기 | 도구 쪽 일이고 이번 작업 범위(콘티·사양 세 파일) 밖이다. 지금 도구는 `pendant` 값으로 고정 문구를 바꿔 넣는다. 3-018의 [PROP] `tuning_fork_necklace__s3_in_box` 문구에 "tuning-fork pendant"가 있지만, 상자 속 목걸이를 그리는 정상 소품 문구다(은주 [CHAR]에는 없음). |
| 3 | outfit_schedule에 은주 실내 의상, 쓰레기 산 의상 변형 두기 | `design/` 데이터 쪽 일이라 범위 밖이다. 이번에는 컷별 outfit 덮어쓰기로 처리했다. 데이터에 변형을 두면 같은 문제가 다시 생기지 않는다(채택 권장). |
| 3 | 2-076(공방, 해 질 무렵) | 덮어쓰지 않았다. 은주가 동그리를 들고 공방을 나서는 순간이고, 바로 다음 컷 2-077 콘티에 "고무장화가 디딜 때마다"가 있다. 장화·장갑 차림을 그대로 이었다. |
| 3 | 운동화 | 연습실·공방의 신발은 "worn canvas sneakers"로 새로 정했다. 은주 여름 의상 문구에 이미 있는 신발이고, 3-9 콘티에 "문턱에서 신발을 턴다"가 있어 공방은 신을 신는 곳이다. ep1 공부방(1-049)은 신발을 정하지 않았다. 사용자가 바꿀 수 있다. |
| 3 | 3-024·3-025의 장갑과 신발 | 장갑은 콘티대로 남겼고, 장화는 SPEC 6·7절 "공방 실내에서는 장화를 뺀다"를 따라 운동화로 바꿨다. 반면 2-076은 다음 컷 2-077의 장화와 이어져야 해서 장화를 두었다. 두 경우가 엇갈려 보일 수 있다. |
| 3 | 2-053, 3-024, 3-025, 3-027, 3-036~3-038 | 장갑을 남긴 예외다. 근거: 손끝 자른 장갑이 이 컷의 뜻이다(2-053). 콘티에 목장갑이 명시되어 있다(3-025, 3-036). 고물 더미 작업 칸이 있다(3-027). |
| 3 | 2-13 고물상(2-048~2-050), 3-1 고물상(3-001~3-003), 천막 회의(2-054, 2-059) | 덮어쓰지 않았다. 작업장·모임 자리라 ep1 관행(1-025~1-033, 1-058·1-063 덮어쓰지 않음)을 따랐다. |
| 4 | 2-036(연청, 금빛이 물러남) | colors를 넣지 않았다. 금빛은 작아져 물러나고 연청만 다가오는 컷이다. "only … #9DB7C9"가 오히려 맞다. |
| 4 | 3-115, 3-116('밤'의 마지막 음) | colors를 넣지 않았다. 콘티와 cut_en이 모두 "금빛 동심원 하나"를 말하는 단색 컷이다(마지막 음이 혼자 떠오른다). |
| 7 | 도구 수정 | 이미 반영되어 있어 사양만 확인했다. |
| 11 | 회상 칸을 따로 떼어 별도 컷으로 두기 | 컷 수와 번호를 바꾸지 않는 조건이라 cut_en 가운데 칸 문장으로 해결했다. |
| 12 | scene_index 3-17 상태 키 고치기 | 지시대로 사양만 고쳤다. scene_index 3-17은 여전히 `dongguri__s5_restored`다. |
| 20 | 2-021 "(E)" | 지시서대로 그대로 둔다(화면 밖 처리라 해가 없음). |
| 24 | 장갑 자르기 순서 | 지시서대로 그대로 둔다(축소 후보 적용 범위 안). |

## 3. 점검 결과

```
컷 113 · 대본 대사 139줄 · 누락 0 / [주의] 1-012: 말풍선 4개(기존 예외) / 통과
컷 90 · 대본 대사 93줄 · 누락 0 / 통과
컷 150 · 대본 대사 119줄 · 누락 0 / 통과
컷 353개 / 문제 0건
수위 태그: {'violence': 9}
콘티 353컷 · 사양 353줄 · 사양 없는 컷 0 · 콘티에 없는 사양 0 · 소리 색 컷 71   (주의 0)
→ storyboard/out/cel (353컷)
```

조립본(`storyboard/out/cel/`)을 python으로 따로 검사했다.

- (a) `pendant: false` 15컷:
  - 은주 [CHAR]에 "tuning-fork pendant"가 남은 컷은 0이다. 15컷 모두 "no necklace, bare neck"로 끝난다.
  - 파일 전체를 단순 grep하면 1건(3-018)이 나온다. 상자 속 목걸이 소품 `tuning_fork_necklace__s3_in_box`의 [PROP] 문구(design/)라 정상이다.
- (b) 실내 컷(집 안·연습실·공방·공부방)과 연주 컷 은주의 outfit:
  - 'rubber boots'(실내)나 'work gloves'(실내·연주)가 남은 컷은 0이다. "no work gloves" 같은 부정형과 "장갑은 주머니에" 문구는 세지 않았다.
  - 위 표의 장갑 예외 7컷(2-053, 3-024, 3-025, 3-027, 3-036~3-038)과 2-076은 따로 세었다.
  - 단순 grep으로는 ep1 실내 문구도 걸린다. "no work gloves, no rubber boots", "work gloves tucked into the jacket pocket"처럼 모두 부정형이다.
- (c) colors가 있는 17컷: [SOUND]에 'only this sound'가 있는 컷은 0이다. HEX는 모두 style_guide 2절의 9색 안에 있다. 3-042의 [SOUND]는 "tiny soft dots … hug each instrument, not spreading"이다.
- 회상 씬 3-3·3-12·3-21의 28컷:
  - 현재 시점 컷에 회상 장소가 붙은 경우는 0이다.
  - 회상 단독 컷은 모두 cut_en이 "flashback"으로 시작하고, [SCENE]이 회상 장소다.
  - 회상 칸이 있는 분할 컷(3-098)은 [SCENE]에 "[flashback frame only]"가 있다.
