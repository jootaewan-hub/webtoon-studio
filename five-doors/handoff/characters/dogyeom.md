# 한도겸 (Han Do-gyeom) — 캐릭터 프롬프트 팩

> 작화 기준: `story/bible.md` **0-2. 확정 외형(시안 B)** > 각 인물 3·4·5절 > 3-1 대비표. 충돌하면 0-2를 따른다. 성격·버릇·소설 속 사실은 바이블 그대로다. 등장인물은 모두 성인이며 가공 인물이다.

## 1. 한 줄 요약과 절대 고정값

**다섯 여자의 캘린더 색을 굴리는 미남형 바람둥이 사기꾼. 흰 셔츠, 걷은 소매, 왼손의 시계와 초승달 흉터가 얼굴이다.**

- 나이 32세 · 키 182cm · 대표 색 없음(다섯 색의 주인) · 기본 흰 셔츠 `#F4F4F2` · 머리 `#1C1F26`

**절대 고정값 체크리스트** (생성 결과를 받을 때마다 이 목록으로 검수한다)

- [ ] 키 182cm, 넓고 곧은 어깨, 넓고 평평한 가슴, 어깨보다 확실히 좁은 허리, 길고 단단한 팔뚝·종아리(헬스 몸 아님)
- [ ] 갸름한 긴 얼굴 + 각진 턱선, 부드러운 미남형(시안 B)
- [ ] 짙은 일자 눈썹(어머니 순옥·아들 지호와 같은 집안 눈썹)
- [ ] 쌍꺼풀 없는 가로로 긴 눈, 눈을 오래 맞추는 따뜻한 시선, 눈 밑이 살짝 어둡다
- [ ] 높고 곧은 코, 얇은 입술, **왼쪽 입꼬리만** 올라가는 웃음
- [ ] 피부 `#E8C29E`
- [ ] 짧은 투블록 슬릭 백, 이마로 흘러내린 **머리 한 가닥**, 색 `#1C1F26`
- [ ] **왼손목** 금장 콤비 시계(로고 없음, 레플리카 느낌)
- [ ] **왼손 엄지·검지 사이** 1.5cm 연분홍 초승달 화상 흉터 — 시계 바로 아래, 늘 한 프레임
- [ ] 긴 손가락, 손등 핏줄, 짧고 깨끗한 손톱, 오른손 검지 핸들 굳은살
- [ ] 기본 의상: 흰 셔츠 `#F4F4F2` 단추 두 개 풂 + 소매 팔뚝까지 걷음 + 차콜 슬랙스 `#2B2F3A`
- [ ] 반지 없음. 휴대폰 두 대
- [ ] 자세: 등받이에 깊이 기대고 다리를 넓게 벌림. 거짓말할 때 귓불을 만진다

## 2. CHARACTER LOCK (166 words)

모든 프롬프트 맨 앞(공통 스타일 문구 바로 다음)에 **한 글자도 바꾸지 않고** 붙인다. 아래 3절의 코드블록에는 이미 들어 있다.

```text
Han Do-gyeom, fictional adult character, not resembling any real person. A 32-year-old Korean man, 182 cm, lean long-limbed build: broad straight shoulders, broad flat chest, waist clearly narrower than the shoulders, long hard forearms with visible veins and long calves; a night driver's body, not a gym body. Softly handsome long face with an angular jaw, thick straight dark eyebrows, warm long monolid eyes that hold eye contact, faint shadows under the eyes, a high straight nose, thin lips; when he smiles only the LEFT corner of the mouth lifts. Warm beige skin (#E8C29E). Short two-block undercut slicked back, jet black (#1C1F26), with one loose strand falling over the forehead. Signature, always together: a two-tone gold-and-steel wristwatch (no logo) on the LEFT wrist, and right below it a 1.5 cm pale-pink crescent burn scar on the web between the left thumb and index finger. Default look: white shirt (#F4F4F2), top two buttons open, sleeves rolled to the forearm. No rings. Relaxed, unhurried posture; leans back deep.
```

## 3. 생성 프롬프트

각 코드블록 = 공통 스타일 문구 + CHARACTER LOCK + 작업 지시. **블록 전체를 그대로 복사해 붙인다.** 기준 이미지(5절)가 있으면 이미지를 첨부하고, 맨 앞에 5절의 '레퍼런스 문장'을 한 줄 더 붙인다.

### 3-a. 턴어라운드 시트 (가로 3:2)

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Han Do-gyeom, fictional adult character, not resembling any real person. A 32-year-old Korean man, 182 cm, lean long-limbed build: broad straight shoulders, broad flat chest, waist clearly narrower than the shoulders, long hard forearms with visible veins and long calves; a night driver's body, not a gym body. Softly handsome long face with an angular jaw, thick straight dark eyebrows, warm long monolid eyes that hold eye contact, faint shadows under the eyes, a high straight nose, thin lips; when he smiles only the LEFT corner of the mouth lifts. Warm beige skin (#E8C29E). Short two-block undercut slicked back, jet black (#1C1F26), with one loose strand falling over the forehead. Signature, always together: a two-tone gold-and-steel wristwatch (no logo) on the LEFT wrist, and right below it a 1.5 cm pale-pink crescent burn scar on the web between the left thumb and index finger. Default look: white shirt (#F4F4F2), top two buttons open, sleeves rolled to the forearm. No rings. Relaxed, unhurried posture; leans back deep.

Character turnaround model sheet of Han Do-gyeom: four full-body views side by side at identical scale and height — front, three-quarter, side profile, back. Neutral standing pose, arms relaxed slightly away from the body, feet fully visible, no cropping. Same outfit in all four views: white shirt (#F4F4F2) with two top buttons open and sleeves rolled to mid-forearm, charcoal slim slacks (#2B2F3A), brown leather loafers, two-tone watch on the left wrist; the crescent scar on the left hand visible in the front and three-quarter views. In the side and back views keep the single forehead strand and the neat slicked-back nape. Arms slightly away from the body so both hands read. Flat even studio lighting, plain neutral grey background (#BDBDBD). Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-b. 표정 시트 8종 (가로 3:2)

| # | 표정(바이블 연기 포인트) |
|---|---|
| 1 | 유혹 — 눈을 오래 맞추며 왼쪽 입꼬리만 올린 반미소 |
| 2 | 혼자일 때의 빈 얼굴 — 표정이 꺼진 거울 앞 얼굴 |
| 3 | 거짓말 — 왼손 끝으로 귓불을 만지며 쉬운 미소, 시선이 반 박자 비켜 감 |
| 4 | 이기고 있다고 믿는 휘파람 — 입술을 오므린 여유 |
| 5 | 드문 진짜 웃음 — 위를 올려다보는 환한 웃음(아이는 프레임 밖, 그리지 않음) |
| 6 | 반 초 멈칫 — 올라가던 웃음이 중간에 멈춘 얼굴 |
| 7 | 동선 패닉 — 식은땀, 흘러내린 앞머리 여러 가닥, 숨참 |
| 8 | 법정 — 깃 없는 연한 수용복, 시선을 떨군 공허, 끝내 돌아보지 않음 |

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Han Do-gyeom, fictional adult character, not resembling any real person. A 32-year-old Korean man, 182 cm, lean long-limbed build: broad straight shoulders, broad flat chest, waist clearly narrower than the shoulders, long hard forearms with visible veins and long calves; a night driver's body, not a gym body. Softly handsome long face with an angular jaw, thick straight dark eyebrows, warm long monolid eyes that hold eye contact, faint shadows under the eyes, a high straight nose, thin lips; when he smiles only the LEFT corner of the mouth lifts. Warm beige skin (#E8C29E). Short two-block undercut slicked back, jet black (#1C1F26), with one loose strand falling over the forehead. Signature, always together: a two-tone gold-and-steel wristwatch (no logo) on the LEFT wrist, and right below it a 1.5 cm pale-pink crescent burn scar on the web between the left thumb and index finger. Default look: white shirt (#F4F4F2), top two buttons open, sleeves rolled to the forearm. No rings. Relaxed, unhurried posture; leans back deep.

Expression sheet of Han Do-gyeom: eight head-and-shoulders portraits in a 4x2 grid, the identical face, hairstyle, default outfit and lighting in every panel unless a panel says otherwise, slight three-quarter angle, plain neutral grey background (#BDBDBD). Panel 1: seductive half smile: long warm eye contact, only the left corner of the mouth lifted. Panel 2: the empty face when alone: every expression switched off, flat eyes, mouth neutral, as if looking into a mirror. Panel 3: lying: fingertips of the left hand touching his left earlobe, easy smile, eyes drifting slightly off target. Panel 4: smug and winning: lips pursed in a soft whistle, eyebrows relaxed, eyes amused. Panel 5: a rare genuine open smile while looking upward, eyes crinkling (nobody else in frame). Panel 6: a smile frozen halfway: the left corner stopped mid-rise, eyes suddenly alert. Panel 7: panic: cold sweat on the temples, several strands fallen loose from the slick hair, lips parted, breathing hard. Panel 8: courtroom: pale collarless detention uniform (#BFC8C2), hollow eyes cast down, refusing to look back. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-c. 의상 시트 (가로 3:2)

바이블 4절의 회차별 대표 의상 전부. 한 장에 너무 많이 넣으면 얼굴이 무너지므로 시트를 나눴다. 침실·밤 의상은 실루엣과 재질 중심이다.

#### 의상 시트 1 — 평상·작업(1~3화)

1. 1화 기본: 흰 셔츠(단추 두 개) `#F4F4F2` + 차콜 슬랙스 `#2B2F3A` + 갈색 로퍼
2. 1화 새벽: 셔츠 위 형광 연두 대리운전 조끼 `#C8E62E`
3. 2화: 같은 셔츠, 깃에 붉은 립스틱 번짐
4. 3화: 트렁크의 똑같은 흰 셔츠 다섯 벌(옷걸이 소품)
5. 실내복(아내 앞): 회색 반팔 티 + 트레이닝 팬츠 `#8C9096`

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Han Do-gyeom, fictional adult character, not resembling any real person. A 32-year-old Korean man, 182 cm, lean long-limbed build: broad straight shoulders, broad flat chest, waist clearly narrower than the shoulders, long hard forearms with visible veins and long calves; a night driver's body, not a gym body. Softly handsome long face with an angular jaw, thick straight dark eyebrows, warm long monolid eyes that hold eye contact, faint shadows under the eyes, a high straight nose, thin lips; when he smiles only the LEFT corner of the mouth lifts. Warm beige skin (#E8C29E). Short two-block undercut slicked back, jet black (#1C1F26), with one loose strand falling over the forehead. Signature, always together: a two-tone gold-and-steel wristwatch (no logo) on the LEFT wrist, and right below it a 1.5 cm pale-pink crescent burn scar on the web between the left thumb and index finger. Default look: white shirt (#F4F4F2), top two buttons open, sleeves rolled to the forearm. No rings. Relaxed, unhurried posture; leans back deep.

Outfit sheet of Han Do-gyeom: 5 full-body standing figures in a row, the same person with the identical face, hair, body and marks in every figure, front or three-quarter view, neutral pose, plain neutral grey background (#BDBDBD), exact outfit colors as given. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. Figure 1: Ep1 default: white shirt (#F4F4F2) two buttons open, sleeves rolled, charcoal slacks (#2B2F3A), brown leather loafers, watch. Figure 2: Ep1 dawn: the same shirt and slacks with a neon lime-green mesh safety vest (#C8E62E) over it, a folded electric kick scooter beside him. Figure 3: Ep2: the same white shirt with a smudge of deep red lipstick on the collar. Figure 4: Ep3: standing beside an open car trunk where five identical white shirts hang on a rail, buttoning a fresh one. Figure 5: Home wear: plain grey short-sleeve T-shirt and grey track pants (#8C9096), barefoot. Tasteful menswear lookbook presentation. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

#### 의상 시트 2 — 밤·외출·결말(3~6화)

1. 3화 하린 방: 셔츠를 두고 네이비 언컨 재킷 `#1F2C46`만 걸침(맨가슴, 시계만)
2. 5화 10/6 밤: 머리칼에 빗방울, 백화점 쇼핑백
3. 6화: 흰 셔츠 + 네이비 재킷(양쪽 주머니가 향수병 무게로 처짐), 땀 젖은 등판
4. 6화 법정: 깃 없는 연한 수용복 `#BFC8C2`, 머리가 자라 이마를 덮음
5. 6화 에필로그(35세): 3년 묵은 흰 셔츠, 어깨가 헐렁, 왼손목에 하얀 시계 자국, 볼이 꺼짐

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Han Do-gyeom, fictional adult character, not resembling any real person. A 32-year-old Korean man, 182 cm, lean long-limbed build: broad straight shoulders, broad flat chest, waist clearly narrower than the shoulders, long hard forearms with visible veins and long calves; a night driver's body, not a gym body. Softly handsome long face with an angular jaw, thick straight dark eyebrows, warm long monolid eyes that hold eye contact, faint shadows under the eyes, a high straight nose, thin lips; when he smiles only the LEFT corner of the mouth lifts. Warm beige skin (#E8C29E). Short two-block undercut slicked back, jet black (#1C1F26), with one loose strand falling over the forehead. Signature, always together: a two-tone gold-and-steel wristwatch (no logo) on the LEFT wrist, and right below it a 1.5 cm pale-pink crescent burn scar on the web between the left thumb and index finger. Default look: white shirt (#F4F4F2), top two buttons open, sleeves rolled to the forearm. No rings. Relaxed, unhurried posture; leans back deep.

Outfit sheet of Han Do-gyeom: 5 full-body standing figures in a row, the same person with the identical face, hair, body and marks in every figure, front or three-quarter view, neutral pose, plain neutral grey background (#BDBDBD), exact outfit colors as given. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. Figure 1: Ep3: navy unstructured jacket (#1F2C46) worn open over a bare chest, slacks, watch only. Figure 2: Ep5 night: white shirt and navy jacket, raindrops in his hair, a plain paper department-store shopping bag in hand. Figure 3: Ep6: white shirt and navy jacket (#1F2C46) with both side pockets sagging from small bottles, shirt back damp with sweat. Figure 4: Ep6 courtroom: pale grey-green collarless detention uniform (#BFC8C2), hair grown out and covering the forehead, no watch. Figure 5: Epilogue, age 35: the same old white shirt now loose at the shoulders, a pale watch tan line on the bare left wrist, slightly hollow cheeks. Tasteful menswear lookbook presentation. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-d. 손·소품 클로즈업 (정사각 1:1)

**왼손 시계 + 초승달 흉터**

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Han Do-gyeom, fictional adult character, not resembling any real person. A 32-year-old Korean man, 182 cm, lean long-limbed build: broad straight shoulders, broad flat chest, waist clearly narrower than the shoulders, long hard forearms with visible veins and long calves; a night driver's body, not a gym body. Softly handsome long face with an angular jaw, thick straight dark eyebrows, warm long monolid eyes that hold eye contact, faint shadows under the eyes, a high straight nose, thin lips; when he smiles only the LEFT corner of the mouth lifts. Warm beige skin (#E8C29E). Short two-block undercut slicked back, jet black (#1C1F26), with one loose strand falling over the forehead. Signature, always together: a two-tone gold-and-steel wristwatch (no logo) on the LEFT wrist, and right below it a 1.5 cm pale-pink crescent burn scar on the web between the left thumb and index finger. Default look: white shirt (#F4F4F2), top two buttons open, sleeves rolled to the forearm. No rings. Relaxed, unhurried posture; leans back deep.

Close-up of his LEFT hand and forearm: sleeve rolled to the elbow, veined forearm, two-tone gold-and-steel watch on the wrist, and directly below it a 1.5 cm pale-pink crescent burn scar on the web between thumb and index finger. Long fingers, short clean nails. Hand resting on a black leather steering wheel at night, warm dashboard glow, shallow depth of field. No text, no letters, no logo, no watermark.
```

**트렁크 공구함의 향수 다섯 병**

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Han Do-gyeom, fictional adult character, not resembling any real person. A 32-year-old Korean man, 182 cm, lean long-limbed build: broad straight shoulders, broad flat chest, waist clearly narrower than the shoulders, long hard forearms with visible veins and long calves; a night driver's body, not a gym body. Softly handsome long face with an angular jaw, thick straight dark eyebrows, warm long monolid eyes that hold eye contact, faint shadows under the eyes, a high straight nose, thin lips; when he smiles only the LEFT corner of the mouth lifts. Warm beige skin (#E8C29E). Short two-block undercut slicked back, jet black (#1C1F26), with one loose strand falling over the forehead. Signature, always together: a two-tone gold-and-steel wristwatch (no logo) on the LEFT wrist, and right below it a 1.5 cm pale-pink crescent burn scar on the web between the left thumb and index finger. Default look: white shirt (#F4F4F2), top two buttons open, sleeves rolled to the forearm. No rings. Relaxed, unhurried posture; leans back deep.

Close-up inside a car trunk toolbox: five small unbranded perfume bottles lying where wrenches should be, caps colored grey (#9A9EA3), burgundy (#7A1E2E), mint (#7FD1BE), sky blue (#9CC7E8) and gold (#C9A45C). His left hand with the watch and crescent scar reaches in to pick the mint one. Dim underground garage light. No text, no letters, no logo, no watermark.
```

### 3-e. 캐릭터 대표 키 비주얼 (세로 2:3)

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Han Do-gyeom, fictional adult character, not resembling any real person. A 32-year-old Korean man, 182 cm, lean long-limbed build: broad straight shoulders, broad flat chest, waist clearly narrower than the shoulders, long hard forearms with visible veins and long calves; a night driver's body, not a gym body. Softly handsome long face with an angular jaw, thick straight dark eyebrows, warm long monolid eyes that hold eye contact, faint shadows under the eyes, a high straight nose, thin lips; when he smiles only the LEFT corner of the mouth lifts. Warm beige skin (#E8C29E). Short two-block undercut slicked back, jet black (#1C1F26), with one loose strand falling over the forehead. Signature, always together: a two-tone gold-and-steel wristwatch (no logo) on the LEFT wrist, and right below it a 1.5 cm pale-pink crescent burn scar on the web between the left thumb and index finger. Default look: white shirt (#F4F4F2), top two buttons open, sleeves rolled to the forearm. No rings. Relaxed, unhurried posture; leans back deep.

Key visual: underground parking level B2 of a luxury apartment complex at night. He leans against a black luxury sedan, white shirt with rolled sleeves, one hand in his pocket, the left hand holding a glowing smartphone that lights his face from below, a second phone in his shirt pocket, a neon lime-green vest rolled up on the car roof. Cool fluorescent ceiling light, wet reflective concrete, warm rim light on his shoulder, the single strand on his forehead, left-corner half smile. Vertical webtoon cover composition, waist-up to knees. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. No text, no letters, no logo, no watermark.
```

## 4. 금지·주의

- 시계·흉터는 **왼손**. 좌우 반전된 결과물은 버린다(이미지 생성기가 자주 뒤집는다 — '왼손'을 프롬프트에 대문자로 둔 이유).
- 웃음은 **왼쪽 입꼬리만**. 양쪽 다 올라가면 다른 사람이 된다.
- 시안 A(졸린 눈 사기꾼, 앞머리 없음)와 섞지 않는다. 기준은 시안 B: 이마의 머리 한 가닥, 부드러운 미남형, 걷은 소매.
- 헬스 근육·식스팩 금지. 마른 근육과 긴 팔다리.
- 롤렉스 등 실제 브랜드 로고·이름을 넣지 않는다(정책·저작권). '로고 없는 금장 콤비 시계'로만.
- 눈썹은 짙은 **일자** — 순옥과 같은 눈썹이어야 6화 법정 컷이 성립한다.
- 아이(지호)와 함께 그릴 때는 관능 톤 의상(맨가슴 재킷 등)을 절대 쓰지 않는다.
- 쇼츠·인스타: 맨가슴 재킷 컷은 실루엣·역광으로만. 썸네일에는 흰 셔츠 기본 룩을 쓴다.
- 공통: 실존 인물·연예인 이름을 프롬프트에 넣지 않는다('누구 닮게' 금지). 텍스트·로고·워터마크가 들어간 결과는 버린다.

## 5. 기존 생성 이미지와 레퍼런스 업로드

| 구분 | 링크 |
|---|---|
| 시안 B(기준) | https://www.canva.com/M/MAHXUMP9VSc |
| 시안 A(참고 금지 — 폐기안) | https://www.canva.com/M/MAHXUFEL4Qw |

- 색·HEX 대조용 평면 시트: `design/sheets/dogyeom.svg` (그림체 레퍼런스로는 쓰지 않는다).
- **레퍼런스로 업로드해 일관성 유지**
  1. 위 '기준' 링크를 열어 이미지를 PNG로 내려받는다(Canva는 공유 화면 → 다운로드).
  2. ChatGPT 새 대화에 그 이미지를 첨부하고, 아래 레퍼런스 문장 + 3-a 턴어라운드 블록을 붙인다.
  3. 통과한 결과는 `design/gen/dogyeom_turnaround_01.png`처럼 저장해 다음 작업의 기준으로 쓴다. 기준 이미지는 1~2장만 유지한다(많을수록 섞인다).
  4. '참고 금지'로 표시한 시안 A 이미지는 첨부하지 않는다.

**레퍼런스 문장** (이미지를 첨부했을 때 블록 맨 앞에 붙임)

```text
Use the attached image as the identity reference for Han Do-gyeom. Keep exactly the same face, hairstyle, hair color, skin tone, body proportions and signature marks; change only what the prompt below asks.
```
