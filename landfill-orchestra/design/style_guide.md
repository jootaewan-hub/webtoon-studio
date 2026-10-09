# 그림체 확정본 — 정밀 셀 반실사 「소리의 색」 (콘티 정합형)

G6 확정 2026-10-09. 기준: "ChatGPT·Codex가 콘티대로 정확히 그릴 수 있어야 한다"(사용자 지시). 그래서 우연에 맡기는 질감(수채 번짐·목탄)을 빼고, 모든 요소를 수치·HEX·영어 프롬프트 문구로 고정한다. 기계가 읽는 값은 `design/style.json`, 씬별 빛·색·의상은 `design/scene_presets.md`(대본 S# 80개). 맛보기 `design/style/style_final.svg`.

출처가 된 안: 2안의 깔끔한 선·셀(재현성) + 1안의 장면별 빛(감동·향수) + 3안의 '소리가 나면 색이 번진다'(작품 개념). 비교 문서는 `design/style_options.md`.

## 1. 그림 규칙 (모든 컷 공통)

| 항목 | 규칙 | 프롬프트 문구 |
|---|---|---|
| 선 | 균일한 진갈색 외곽선 2px(#2B2420), 내부선 1px. 굵기 변화·거친 질감 없음 | clean uniform dark-brown outlines, 2px, thin 1px inner lines, no sketchy texture |
| 채색 | 셀 2단(밝은 면 / 그림자 면). 하늘과 역광에만 부드러운 그러데이션 1층 | two-tone cel shading, soft gradient only in sky and backlight |
| 그림자 색 | 검정을 섞지 않는다. 씬 프리셋의 '그림자' HEX(따뜻한 갈색·남색 계열) | shadows tinted warm brown or navy, never gray-black |
| 질감 | 종이·수채·그레인·노이즈 없음 | no paper texture, no watercolor bleed, no film grain |
| 배경 | 1980년대 사진 고증 기반 반실사. 전경 1/3만 디테일, 원경은 색면 2~3단 | semi-realistic background based on 1980s Seoul references, detailed foreground, simplified flat-color distance |
| 비율 | 반실사. 은주 5.5등신·140cm, 동민 5등신·125cm, 덕수 5.5등신·155cm, 미자 6등신·158cm, 태준 6.5등신·165cm, 어른 6.5~7등신. 만석은 등이 약간 굽고, 곽 영감은 작지만 허리가 꼿꼿하다(바이블). 순례 할머니는 굽음 | semi-realistic proportions, children look their real age |
| 데포르메 | 대본에서 코미디로 지정한 컷만(2화 S#1 몽타주, 동민·미자 리액션). 2~3등신, 그 컷 안에서만 | (해당 컷에만) chibi comedic reaction, 2-3 heads tall |
| 표정·연기 | 콘티의 연기 메모를 얼굴·손으로 그대로. 은주는 '입꼬리만'이 기본. 열세 살 은주의 활짝 웃음은 3화 S#27이 처음이자 유일, 어른 은주는 에필로그 S#34에서 다시 활짝 웃는다 | 해당 컷의 연기 메모를 영어로 그대로 옮김 |
| 화면 비 | 웹툰 컷: 세로 800×1000 기본, 와이드 800×500, 세로 긴 컷 800×1600 | vertical webtoon panel, 4:5 (or 16:10 wide / 1:2 tall) |

## 2. 소리 색 규칙 (이 작품의 시각 장치)

대본에 `— 주변 소리 빠지고 그 소리만 남는다`, `— 은주 왼쪽 귀로` 같은 카메라 의도가 있는 컷, 그리고 음악(`M:`) 컷에만 쓴다. 그 밖의 컷에서는 쓰지 않는다(남발하면 장치가 죽는다).

- 배경과 인물 채도를 약 60% 낮춘다(색은 남기되 흐리게).
- 그 소리를 내는 물건에서 해당 색의 빛이 동심원·물결 띠로 퍼진다. 빛은 반투명, 가장자리 부드럽게.
- 효과음 글자도 같은 색.
- 프롬프트: `the surroundings are desaturated about 60%, only the sound from [물건] glows as soft translucent [색] light rings spreading into the air, the sound-effect lettering is the same [색]`

| 소리 | 색 | HEX |
|---|---|---|
| 동그리(깡통 바이올린) | 금빛 | #F5C04A |
| 뚱보(기름통 첼로) | 주황 | #E8944A |
| 꽥꽥이(배수관 트럼펫) | 청록 | #4FB3A9 |
| 뼈다귀 북(X선 필름 북) | 빨강 | #D9534A |
| 엄마의 소리굽쇠 '웅―' | 은빛 흰색 | #E9EEF5 |
| 엄마의 라디오 허밍 | 연보라 | #B9A7D9 |
| 은주가 가려 듣는 생활 소리(트럭·쇳소리·톱질 등). 대본 카메라 의도에 '귀로'·'그 소리만'이 있는 컷만 | 연청('은주의 귀' 색) | #9DB7C9 |
| '진짜 바이올린'(태준·다솜중의 비발디와 라 '팅', 3화 다락의 곽 영감 바이올린) | 차가운 청색 | #5B8DEF |
| 만석의 클라리넷(2화 전파사 라디오 관악기, 3화 S#3 극장 반주 회상). 에필로그 이중주는 규칙 밖(화면 전체가 이미 자연색) | 와인색 | #9C4A6B |
| 「섬의 하루」 '밤' 전원 합주 | 위 색이 모두 섞여 화면 전체 | — |

예외: 조롱·소음(예: 2화 S#19 객석 웃음)처럼 은주가 상처받는 소리에는 색을 주지 않는다. 화면 채도만 낮춰 '색이 빠지는' 쪽으로 쓴다. 선영의 콧노래 같은 가벼운 일상 음악도 색 없음.

3화 본선(S#19~S#27)은 이 규칙의 정점이다. '새벽'부터 악기가 하나씩 더해질 때마다 색이 하나씩 늘어, '밤'에서 화면이 처음으로 온전히 색으로 찬다.

## 3. 효과음·말풍선·폰트

| 용도 | 폰트(Google Fonts, OFL) | 규칙 |
|---|---|---|
| 대사 | Gowun Dodum | 둥근 흰 말풍선, 진갈색 2px 테두리 |
| 내레이션(어른 은주 `은주 (N)`) | Gowun Batang | 크림색 반투명 사각 박스(#FFF8EA, 85%), 테두리 없음 |
| 소리 효과음 | Nanum Pen Script(작은 소리), Gaegu Bold(큰 소리) | 손글씨. 소리 색 규칙 컷에서는 소리 색, 평소에는 진갈색 |
| 일상 소음(트럭·바람·웃음) | Gaegu Regular | 작게, 회갈색(#8A7A6A), 배경에 얹듯이 |
| 손글씨(쪽지·게시판·칠판) | Nanum Pen Script | 종이 위 글씨는 해당 종이 색 위에 |
| 공문·신문 글자 | Nanum Myeongjo | Insert 컷 안에서만 |

- 효과음은 이미지 생성에서 글자가 깨지기 쉽다. **이미지 프롬프트에는 글자를 넣지 않고(no text), 효과음·말풍선은 편집 단계에서 얹는다.** 킷의 편집기·식자 단계 몫이다.

## 4. 카메라 의도 → 프롬프트 문구 대응표

대본의 카메라 의도(`— …`)를 이 표대로 옮긴다.

| 대본 표기 | 프롬프트 |
|---|---|
| 와이드, 전체 | wide establishing shot |
| 고정 | static camera, eye level |
| 클로즈업 | close-up |
| 극접사 | extreme close-up |
| 투샷 | two-shot |
| ~시점 | point-of-view shot from [인물] |
| 비탈 아래에서 위로 | low angle looking up the slope |
| 내려다보며, 부감 | high angle looking down |
| 천천히 다가가며 | (웹툰: 같은 구도 2~3컷으로 점점 가깝게) slow push-in |
| 초점 밖 배경 | shallow depth of field, background out of focus |
| 무음, 정적 | quiet composition, empty negative space |
| Insert: 물건 | product-like insert shot of [물건], plain context |

## 5. 프롬프트 조립 틀 (컷 하나)

```
[STYLE]   clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions,
          soft gradient only in sky and backlight, no paper texture, no film grain, vertical webtoon panel 4:5
[SCENE]   (scene_presets.md의 해당 S# 줄: 장소, 연도·계절, 시간, 날씨, 광원과 방향, 대표 색 HEX, 그림자 HEX)
[CHAR]    (아래 6절 고정 문구 + 그 씬의 의상)
[CUT]     (콘티 컷 내용: 카메라 → 4절 표, 동작, 연기 메모를 영어로)
[SOUND]   (소리 색 규칙 컷이면 2절 문구)
[NEG]     no text, no letters, no speech bubbles, no brand logos, no real banknotes,
          no official Olympic mascot or emblem, fictional characters not resembling any real person,
          children drawn as ordinary kids, no injuries or blood
```

- 컷 안에서 의상이 씬 프리셋과 다르면(예: 1-11에서 목장갑을 벗고 켬) [CUT]의 의상 변화가 우선이다. `tools/prompt.py --outfit eunju="..."`로 덮어쓴다.

## 6. 인물 고정 문구 (영어, G7 확정 2026-10-09)

외형 원본은 `story/bible.md`, 기계용은 `design/characters.json`(고른 시안은 `design_choice`). 의상은 고정 문구에 넣지 않고 씬마다 `design/outfit_schedule.json` → 씬 프리셋 → `design/outfits_en.json`으로 붙인다(`tools/prompt.py`가 자동으로).

- 은주: `Eunju, 13-year-old Korean girl, 140cm, small and thin, sun-tanned skin, narrow small face, large long almond-shaped eyes, thick straight eyebrows, no bangs with the forehead visible, loose wisps of hair falling at both temples, faint freckles on nose and cheeks, long dark-brown hair tied low at the nape with a single rubber band, a small silver tuning-fork pendant on a thin chain, tilts her head slightly to the left when listening`
- 동민: `Dongmin, 9-year-old Korean boy, 125cm, round face, very short buzz cut, upper-left front tooth missing, big ears, adhesive bandage on the right knee`
- 만석: `Manseok, 41-year-old Korean man, 170cm, gaunt and slightly stooped, long gaunt face, hollow cheeks, stubble, always wears a worn olive work cap with a frayed brim over short hair streaked with gray, long fingers`
- 곽 영감: `old Kwak, 68-year-old Korean man, 160cm, short and solidly built with an upright posture (not stooped), square jaw, short white buzz cut, short thick white eyebrows, deep forehead wrinkles, thick forearms, reading glasses pushed up on his forehead, a pencil behind his ear, ring and little finger of the right hand permanently bent`
- 선영: `Seonyoung, 23-year-old Korean woman, 162cm, slim, round face, voluminous softly permed 1980s bob with fluffy bangs, large round thin gold-rim glasses`
- 최 계장: `Mr. Choi, 46-year-old Korean civil servant, 168cm, medium height with a slight belly, shiny pomaded 7:3 side part, thick black horn-rimmed glasses, a sheen of sweat on the forehead, a white handkerchief in hand`
- 태준: `Taejun, 14-year-old Korean boy, 165cm, tall and slim, long face, narrow long eyes, sharp 7:3 side part with the forehead visible, thin lips, pale skin, very straight posture`
- 미자: `Mija, 14-year-old Korean girl, 158cm, tall for her age, broad shoulders, choppy self-cut short bob with bangs sticking out in all directions, thick eyebrows, square jaw, an adhesive bandage across the nose`
- 덕수: `Deoksu, 12-year-old Korean boy, 155cm, big and chubby, round face, short crew cut, droopy gentle eyes, shirt buttons always done up one hole off`
- 순례 할머니: `grandma Sunrye, Korean woman in her 70s, 148cm, small and stooped, white hair in a low bun held with black hairpins, deep wrinkles, usually holding a ladle`
- 봉구: `Bonggu, 10-year-old Korean boy, buzz cut, wide face, mischievous eyes`
- 영란: `Yeongran, 11-year-old Korean girl, hair in two low pigtails, slim face, firm little mouth`
- 경호: `Gyeongho, 8-year-old Korean boy, identical twin of Gyeongmin, bowl haircut, round face (tell the twins apart only by shirt color)`
- 경민: `Gyeongmin, 8-year-old Korean boy, identical twin of Gyeongho, bowl haircut, round face (tell the twins apart only by shirt color)`
- 순이: `Suni, 9-year-old Korean girl, short bob with a red headband, round eyes`
- 석이: `Seoki, 7-year-old Korean boy, the smallest of all, buzz cut under a big cap, rosy cheeks`

### 단역 고정 문구 (characters.json 밖, 반복 등장)
- 갈고리 아주머니: `a middle-aged Korean woman scavenger with a head scarf, dark padded work clothes, holding a long iron hook`
- 미자 엄마: `Mija's mother, a sturdy Korean woman in her 40s with a loud voice, permed short hair, dark work clothes, a red cardigan`
- 집하장 아저씨: `a Korean man in his 50s at the scrap collection yard, towel on the head, rubber apron, work gloves`
- 전당포 주인: `an elderly Korean pawnbroker with a magnifying loupe pushed up on his forehead, a dark vest over a white shirt, sleeve garters`
- 과장(구청): `a Korean section chief in his 50s, thin, gray suit, reading glasses on a cord`
- 사회자: `a 1980s Korean contest MC in a light-gray suit and bow tie, holding a corded microphone`
- 엄마 한미숙(회상): `the mother, shown only as hands, back view or silhouette, never the face; a faded floral blouse`

## 7. 넘지 않는 선 (그림)

- 아동 인물은 어떤 컷에서도 꾸미거나 성적·선정적으로 보이게 그리지 않는다. 몸 라인 강조·노출 의상 없음.
- 쓰레기 산에서 아이들은 목장갑·장화를 쓴다. 유리·주삿바늘 같은 위험 폐기물을 맨손으로 만지는 그림 없음.
- 만석이 동그리를 던지는 컷은 물건만, 사람 쪽이 아니다. 팔이 다 올라가기 전에 은주 얼굴로 넘긴다(대본 2화 S#10).
- 엄마(한미숙)는 얼굴을 보이지 않는다(손·뒷모습·빛으로).
- 실존 브랜드 로고, 실제 화폐 도안, 올림픽 공식 마스코트·엠블럼 모양 없음. 가게 간판은 가공 이름.

## 7-1. 고증에서 온 화면 기준 (research/notes.md '시각 고증' 절)

- 1987~88년 쓰레기 산은 쌓는 중이다(1986~1992년 성토). 모양은 꼭대기가 평평한 탁자형, 비탈은 층이 지고 트럭길이 나 있다. 최종 높이(93·98m)보다 낮게 그린다(1987년 높이는 미확인).
- 낮 장면 기본 색조: 뿌연 베이지·회백 하늘, 황토·회갈색 땅, 흰 비닐 점, 사람들은 어둡고 두꺼운 옷에 빨강·파랑 웃옷이 드문드문. → 무채색 바탕에 원색 점 하나(은주 남색 점퍼, 미자 빨간 상의)가 눈에 띄는 구성.
- 원경에 가끔 가는 연기(쓰레기 산 자연 발화)를 둘 수 있다. 배경으로만, 아이들 곁에 불을 두지 않는다.
- **의도적 각색:** 실제 1987년 난지도 주민은 1984년 큰불 뒤 서울시가 지은 3~4평 조립식 주택에 살았다. 갈대섬은 가공의 섬이므로 판잣집 동네로 그린다.
- 국민학교는 자유복(일부 사립만 교복), 중학교 교복은 1986년 2학기부터 학교장 재량. 태준의 사립중 교복은 그대로 둔다.

## 8. 장소 기준 문장 (prompt [SCENE] 첫머리, 모든 씬에서 같은 문장 재사용)

장소 묘사가 컷마다 달라지면 GPT가 다른 장소로 그린다. 아래 문장을 그대로 쓰고, 뒤에 시대·시간·빛만 바꿔 붙인다. 배치 세부는 G8 `design/sets.md`에서 정한다.

| 장소 | 영어 기준 문장 |
|---|---|
| 갈대섬 전경 | a fictional landfill island on the Han River at the edge of Seoul, two flat-topped mesa-like hills of compacted trash still being built ('the big hill' and 'the small hill'), terraced ochre and gray-brown slopes with dump-truck ramps, specks of white plastic, power transmission towers in front, a single earthen embankment road linking it to the mainland, reeds along the water, hazy beige sky |
| 작은 산 (중턱·꼭대기) | on the small flat-topped hill of trash: terraced slope of compacted ochre soil mixed with scrap metal, broken boards, white plastic sheets and tin cans, a dump-truck ramp cut into the slope, the Han River and the 1980s city skyline far behind |
| 큰 산 아래 쇳더미 | at the foot of the big trash hill where dump trucks unload: a fresh heap of scrap iron and tin, tire ruts in the mud |
| 둑길·섬 어귀 | the narrow earthen embankment road leading into the island, reeds on both sides, a cluster of shacks at the island entrance |
| 섬 어귀 게시판 | a weathered plywood notice board on two posts at the island entrance, pinned papers |
| 은주네 판잣집, 부엌 겸 방 | inside a small 1980s shack: plywood and tar-paper walls, a low ceiling, a coal-briquette stove, a kerosene burner, a folding low table, a tiny window |
| 은주네 판잣집, 쪽방 | Eunju's tiny side room in the shack: a thin wall shared with the next room, a sleeping mat, a shelf with an old broken transistor radio box |
| 곽 영감 고물상 (안·앞) | old Kwak's junk shop at the island entrance: a corrugated-iron shed, sorted piles of scrap copper, brass and aluminum, a hanging scale, wooden apple crates by the door, a ladder to a small attic |
| 공방 | the small workshop behind old Kwak's junk shop: a wooden workbench, hand tools on the wall, wood shavings, instruments made from scrap hanging on nails |
| 국밥집 천막 (안·앞·뒤) | grandma Sunrye's rice-soup tent at the island entrance: a patched canvas tent, a huge iron soup pot on a coal fire, long low tables and benches, a ladle |
| 강변교회 지하 야학 | a 1980s church basement night-school classroom: a green chalkboard, mismatched desks, three bare incandescent bulbs hanging from the ceiling, a small high window |
| 만복전당포 | a narrow 1980s pawnshop: glass display cases with watches, gold rings and cameras, a yellowed fluorescent light, an abacus on the counter |
| 시장 골목 | a 1980s Seoul market alley: low shop fronts, an electronics repair shop with a radio, hand-painted fictional signs |
| 시내버스 안 | inside a 1980s Seoul city bus: worn seats, hanging straps, a token box by the driver |
| 한빛문화회관 (앞·로비·복도·무대 옆·홀) | the fictional Hanbit Cultural Center, a 1980s concert hall: concrete facade with wide steps, a lobby with terrazzo floor, a backstage corridor, red velvet stage curtains, wooden stage, rows of red audience seats |
| 학교 강당 | a 1980s school auditorium: a wooden stage with a raised platform, folding chairs, high windows |
| 구청 도시정비과 | a 1980s Seoul district office: steel desks, stacks of folders, a wall map of the district, a desk fan |
| 푸른 언덕 공원 (2003) | a green hilltop park built over the old landfill, grass and wildflowers, a walking path, a small outdoor stage, the Han River and a 2003 Seoul skyline |
| 판잣집 동네 외경 | the shack village at the island entrance: low shacks of plywood, tar paper and cement blocks with slate and roofing-felt roofs weighed down by plastic sheets and stones, narrow winding dirt alleys, thin stovepipes |
| 한빛문화회관 연습실 | the fictional Hanbit Cultural Center, its large rehearsal room: a polished wooden floor, rows of folding chairs grouped by school, white fluorescent ceiling lights, tall windows, a slogan-only Olympic campaign poster on the wall |
| 뭍의 골목 | a mainland back alley of 1980s Seoul outside the island: low brick and cement-block houses, gray walls, wooden utility poles, a narrow lane of cracked asphalt and dirt |
| 국밥집 천막 뒤 쓰레기 더미 | (국밥집 천막 문장 뒤에) behind the tent, a mound of wet trash waiting for the collection yard: tangled plastic sheets, tin cans and broken wood |
| 갈대섬 전경 (매립 끝난 뒤, 1990년대) | the same island after landfill closure: the two flat-topped hills covered with fresh soil, no trash visible, first green sprouts and grass on the terraced slopes, the embankment road, the Han River |
| 구청 복도 | a corridor of the same 1980s Seoul district office: terrazzo floor, a row of plain office doors, a potted plant by the wall, fluorescent tubes on the ceiling |
| 임대주택 골목 | a narrow alley between new low-rise public rental apartment blocks in late-1980s Seoul, rows of identical windows, a concrete alley entrance |
| 학교 교문 | a late-1980s Seoul elementary school front gate: an iron gate between concrete posts, a dirt schoolyard and a three-story school building behind |
| 회상: 1970년대 극장 쇼 무대 | a 1970s downtown Seoul theater show stage: a glittering tinsel curtain, footlights, a small band pit with music stands just behind and below the stage |
| 회상: 라디오 수리점 | a small 1970s Seoul radio repair shop: shelves crowded with transistor and vacuum-tube radios, a workbench with a soldering iron and small tools |
| 회상: 1950년대 판자촌 집 | a 1950s Seoul hillside shanty: a rusty corrugated tin roof, plywood and straw-mat walls, a dirt floor |
