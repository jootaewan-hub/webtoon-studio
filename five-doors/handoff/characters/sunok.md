# 박순옥 (Park Sun-ok) — 캐릭터 프롬프트 팩

> 작화 기준: `story/bible.md` **0-2. 확정 외형(시안 B)** > 각 인물 3·4·5절 > 3-1 대비표. 충돌하면 0-2를 따른다. 성격·버릇·소설 속 사실은 바이블 그대로다. 등장인물은 모두 성인이며 가공 인물이다.

## 1. 한 줄 요약과 절대 고정값

**40년 경력의 세신사, 그 남자의 어머니. 말이 없고, 수건을 네 모서리 맞춰 접는다. 아들과 같은 짙은 일자 눈썹.**

- 나이 61세 · 키 155cm · 대표 색 분홍(세신복) `#E9A6B3` · 머리 `#8E8A86`

**절대 고정값 체크리스트** (생성 결과를 받을 때마다 이 목록으로 검수한다)

- [ ] 61세, 키 155cm, 6.5등신 — 캐스트 중 가장 작고 다부짐
- [ ] 넓은 어깨, 두꺼운 팔뚝, 굵은 종아리, 약간 굽은 허리
- [ ] 둥근 얼굴, 볕과 김에 그을린 붉은 볼
- [ ] **짙은 일자 눈썹**(도겸·지호와 같은 눈썹 — 6화 법정의 열쇠)
- [ ] 작고 처진 눈, 넓은 코, 늘 다문 얇은 입술
- [ ] 피부 `#E3B48E`, 늘 김에 젖은 붉은 기, 노동과 나이의 주름
- [ ] 희끗한 단발 파마 `#8E8A86`, 일할 때 망사 헤어캡
- [ ] **두껍고 단단한 따뜻한 손**, 굵은 손마디, 이태리타월 굳은살
- [ ] 아주 짧고 물에 불어 하얀 손톱, 오른쪽 손목 파스
- [ ] 근무복: **분홍** 세신복 `#E9A6B3`(빨강 아님), 고무 슬리퍼
- [ ] 시선은 늘 아래(수건·등·손)
- [ ] 관능 요소 없음. 존엄하게

## 2. CHARACTER LOCK (160 words)

모든 프롬프트 맨 앞(공통 스타일 문구 바로 다음)에 **한 글자도 바꾸지 않고** 붙인다. 아래 3절의 코드블록에는 이미 들어 있다.

```text
Park Sun-ok, fictional adult character, not resembling any real person. A 61-year-old Korean woman, a bathhouse body-scrub attendant for forty years, 155 cm, a compact 6.5-head build, shorter and sturdier than the rest of the cast. Solid working body: broad shoulders, thick forearms, thick calves, a slightly stooped back, plain unglamorous figure. Round face with cheeks flushed by steam and sun; THICK STRAIGHT dark eyebrows, the same family brows as her son; small droopy eyes; a wide nose; thin lips always pressed shut. Weathered warm skin (#E3B48E) with a reddish steam flush, lined by age and labor. Short graying permed bob (#8E8A86), under a mesh hair cap at work. Signature: thick, firm, warm hands with big knuckles, scrub-mitt calluses on the palms, very short water-softened nails, a pain-relief patch on the right wrist. Habits: silent, eyes lowered to towels, backs and hands; folds a towel in half and in half again with all four corners matching. Never sensual, always dignified.
```

## 3. 생성 프롬프트

각 코드블록 = 공통 스타일 문구 + CHARACTER LOCK + 작업 지시. **블록 전체를 그대로 복사해 붙인다.** 기준 이미지(5절)가 있으면 이미지를 첨부하고, 맨 앞에 5절의 '레퍼런스 문장'을 한 줄 더 붙인다.

### 3-a. 턴어라운드 시트 (가로 3:2)

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Park Sun-ok, fictional adult character, not resembling any real person. A 61-year-old Korean woman, a bathhouse body-scrub attendant for forty years, 155 cm, a compact 6.5-head build, shorter and sturdier than the rest of the cast. Solid working body: broad shoulders, thick forearms, thick calves, a slightly stooped back, plain unglamorous figure. Round face with cheeks flushed by steam and sun; THICK STRAIGHT dark eyebrows, the same family brows as her son; small droopy eyes; a wide nose; thin lips always pressed shut. Weathered warm skin (#E3B48E) with a reddish steam flush, lined by age and labor. Short graying permed bob (#8E8A86), under a mesh hair cap at work. Signature: thick, firm, warm hands with big knuckles, scrub-mitt calluses on the palms, very short water-softened nails, a pain-relief patch on the right wrist. Habits: silent, eyes lowered to towels, backs and hands; folds a towel in half and in half again with all four corners matching. Never sensual, always dignified.

Character turnaround model sheet of Park Sun-ok: four full-body views side by side at identical scale and height — front, three-quarter, side profile, back. Neutral standing pose, arms relaxed slightly away from the body, feet fully visible, no cropping. Same outfit in all four views: pink short-sleeve scrub attendant top and matching shorts set (#E9A6B3), pink rubber slippers, mesh hair cap, a green scrub mitt on the right hand. Keep the slightly stooped back in the side view and the thick calves and forearms in every view. Plain and realistic, no glamour. Flat even studio lighting, plain neutral grey background (#BDBDBD). Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-b. 표정 시트 8종 (가로 3:2)

| # | 표정(바이블 연기 포인트) |
|---|---|
| 1 | 말 없는 무표정 — 다문 입, 아래를 보는 눈 |
| 2 | 코로 새는 짧은 바람 — 웃음을 감춤('때가 많이 나와서') |
| 3 | 두 박자 멈춤 — 등을 밀던 손이 멈춘 순간 |
| 4 | 숨긴 슬픔 — 수건을 접으며 |
| 5 | 알아봄 — 사진 속 흉터를 본 정지 |
| 6 | 조용한 결의 — 아무 말도 하지 않기로 한 얼굴 |
| 7 | 법정 — 며느리의 눈을 정면으로 받음(끄덕이지도 숙이지도 않음) |
| 8 | 12시간 노동 끝의 피로 — 김 속의 이마와 희끗한 머리 |

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Park Sun-ok, fictional adult character, not resembling any real person. A 61-year-old Korean woman, a bathhouse body-scrub attendant for forty years, 155 cm, a compact 6.5-head build, shorter and sturdier than the rest of the cast. Solid working body: broad shoulders, thick forearms, thick calves, a slightly stooped back, plain unglamorous figure. Round face with cheeks flushed by steam and sun; THICK STRAIGHT dark eyebrows, the same family brows as her son; small droopy eyes; a wide nose; thin lips always pressed shut. Weathered warm skin (#E3B48E) with a reddish steam flush, lined by age and labor. Short graying permed bob (#8E8A86), under a mesh hair cap at work. Signature: thick, firm, warm hands with big knuckles, scrub-mitt calluses on the palms, very short water-softened nails, a pain-relief patch on the right wrist. Habits: silent, eyes lowered to towels, backs and hands; folds a towel in half and in half again with all four corners matching. Never sensual, always dignified.

Expression sheet of Park Sun-ok: eight head-and-shoulders portraits in a 4x2 grid, the identical face, hairstyle, default outfit and lighting in every panel unless a panel says otherwise, slight three-quarter angle, plain neutral grey background (#BDBDBD). Panel 1: silent neutral: lips pressed shut, eyes lowered. Panel 2: a short breath through the nose, the ghost of a dry laugh she hides immediately. Panel 3: a two-beat freeze: hands stopped mid-scrub, eyes fixed downward, breath held. Panel 4: hidden sorrow while folding a towel, eyes glistening but dry, jaw firm. Panel 5: recognition: utterly still, staring at a small phone screen held by someone else. Panel 6: quiet resolve: the decision to say nothing, lips set, eyes calm. Panel 7: courtroom: meeting a younger woman's eyes head-on, not nodding, not bowing, perfectly still. Panel 8: end of a twelve-hour shift: tired eyes half-closed, steam haze over the face, damp graying hair. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-c. 의상 시트 (가로 3:2)

바이블 4절의 회차별 대표 의상 전부. 한 장에 너무 많이 넣으면 얼굴이 무너지므로 시트를 나눴다. 침실·밤 의상은 실루엣과 재질 중심이다.

#### 의상 시트 — 근무·외출·회상

1. 1·2·5화 근무복: 분홍 세신복(반팔 상의+반바지) `#E9A6B3` + 고무 슬리퍼 + 망사 헤어캡 + 이태리타월 + 수건 카트
2. 외출·6화 법정: 회색 패딩 점퍼 `#6E6F73` + 검정 바지 + 천 가방, 무릎 위 손수건
3. 2화 회상(2001, 36세): 늘어난 면 티 + 몸빼 바지 `#C9B79C` — 같은 눈썹, 더 짙은 머리, 덜 굽은 등

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Park Sun-ok, fictional adult character, not resembling any real person. A 61-year-old Korean woman, a bathhouse body-scrub attendant for forty years, 155 cm, a compact 6.5-head build, shorter and sturdier than the rest of the cast. Solid working body: broad shoulders, thick forearms, thick calves, a slightly stooped back, plain unglamorous figure. Round face with cheeks flushed by steam and sun; THICK STRAIGHT dark eyebrows, the same family brows as her son; small droopy eyes; a wide nose; thin lips always pressed shut. Weathered warm skin (#E3B48E) with a reddish steam flush, lined by age and labor. Short graying permed bob (#8E8A86), under a mesh hair cap at work. Signature: thick, firm, warm hands with big knuckles, scrub-mitt calluses on the palms, very short water-softened nails, a pain-relief patch on the right wrist. Habits: silent, eyes lowered to towels, backs and hands; folds a towel in half and in half again with all four corners matching. Never sensual, always dignified.

Outfit sheet of Park Sun-ok: 3 full-body standing figures in a row, the same person with the identical face, hair, body and marks in every figure, front or three-quarter view, neutral pose, plain neutral grey background (#BDBDBD), exact outfit colors as given. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. Figure 1: Work, Ep1-2-5: pink short-sleeve top and shorts set (#E9A6B3), pink rubber slippers, mesh hair cap, green scrub mitt, pushing a towel cart stacked with folded white towels. Figure 2: Outing / Ep6 courtroom: grey padded jumper (#6E6F73), plain black trousers, canvas tote bag, a folded white handkerchief in her hands. Figure 3: Ep2 flashback, year 2001, the same woman at age 36: stretched-out faded cotton T-shirt and loose patterned work trousers (#C9B79C), darker hair with no gray, less stooped, same thick straight brows and same hands. Plain, realistic presentation. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-d. 손·소품 클로즈업 (정사각 1:1)

**수건을 접는 손**

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Park Sun-ok, fictional adult character, not resembling any real person. A 61-year-old Korean woman, a bathhouse body-scrub attendant for forty years, 155 cm, a compact 6.5-head build, shorter and sturdier than the rest of the cast. Solid working body: broad shoulders, thick forearms, thick calves, a slightly stooped back, plain unglamorous figure. Round face with cheeks flushed by steam and sun; THICK STRAIGHT dark eyebrows, the same family brows as her son; small droopy eyes; a wide nose; thin lips always pressed shut. Weathered warm skin (#E3B48E) with a reddish steam flush, lined by age and labor. Short graying permed bob (#8E8A86), under a mesh hair cap at work. Signature: thick, firm, warm hands with big knuckles, scrub-mitt calluses on the palms, very short water-softened nails, a pain-relief patch on the right wrist. Habits: silent, eyes lowered to towels, backs and hands; folds a towel in half and in half again with all four corners matching. Never sensual, always dignified.

Close-up of her thick, firm hands with big knuckles folding a white towel in half and then in half again, all four corners matching exactly; scrub-mitt calluses on the palms, very short water-softened nails, a beige pain-relief patch on the right wrist. Steamy fluorescent bathhouse light. No text, no letters, no logo, no watermark.
```

**이태리타월과 바가지**

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Park Sun-ok, fictional adult character, not resembling any real person. A 61-year-old Korean woman, a bathhouse body-scrub attendant for forty years, 155 cm, a compact 6.5-head build, shorter and sturdier than the rest of the cast. Solid working body: broad shoulders, thick forearms, thick calves, a slightly stooped back, plain unglamorous figure. Round face with cheeks flushed by steam and sun; THICK STRAIGHT dark eyebrows, the same family brows as her son; small droopy eyes; a wide nose; thin lips always pressed shut. Weathered warm skin (#E3B48E) with a reddish steam flush, lined by age and labor. Short graying permed bob (#8E8A86), under a mesh hair cap at work. Signature: thick, firm, warm hands with big knuckles, scrub-mitt calluses on the palms, very short water-softened nails, a pain-relief patch on the right wrist. Habits: silent, eyes lowered to towels, backs and hands; folds a towel in half and in half again with all four corners matching. Never sensual, always dignified.

Close-up of her right hand wearing a green body-scrub mitt, resting on a wet vinyl scrub table beside a plastic water scoop; thick knuckles, a beige pain-relief patch on the wrist, the pink sleeve edge of her uniform. A towel cart edge in the background, steam, fluorescent light, wet tile walls. Only her hand and forearm in frame. No text, no letters, no logo, no watermark.
```

### 3-e. 캐릭터 대표 키 비주얼 (세로 2:3)

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Park Sun-ok, fictional adult character, not resembling any real person. A 61-year-old Korean woman, a bathhouse body-scrub attendant for forty years, 155 cm, a compact 6.5-head build, shorter and sturdier than the rest of the cast. Solid working body: broad shoulders, thick forearms, thick calves, a slightly stooped back, plain unglamorous figure. Round face with cheeks flushed by steam and sun; THICK STRAIGHT dark eyebrows, the same family brows as her son; small droopy eyes; a wide nose; thin lips always pressed shut. Weathered warm skin (#E3B48E) with a reddish steam flush, lined by age and labor. Short graying permed bob (#8E8A86), under a mesh hair cap at work. Signature: thick, firm, warm hands with big knuckles, scrub-mitt calluses on the palms, very short water-softened nails, a pain-relief patch on the right wrist. Habits: silent, eyes lowered to towels, backs and hands; folds a towel in half and in half again with all four corners matching. Never sensual, always dignified.

Key visual: a steamy bathhouse scrub room lit by flat fluorescent tubes. Wet tiles, a vinyl scrub table, a towel cart. She stands in her pink scrub attendant set and mesh cap, folding a white towel with exact corners, eyes lowered, steam veiling the air; quiet, dignified, lonely. Muted pink, white and pale teal palette. No other people in frame. Vertical webtoon cover composition. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. No text, no letters, no logo, no watermark.
```

## 4. 금지·주의

- 세신복은 **분홍** `#E9A6B3`. 빨강·자주로 나오면 버린다(바이블 3-3 체크리스트).
- **관능 톤 금지.** 글래머·피부 광택·화보 조명을 쓰지 않는다. 세신실 장면은 김·형광등·타일로 감각만.
- 공통 스타일 문구의 'adult webtoon'과 '8-head'는 작품 스타일 기준이다. 순옥은 LOCK의 6.5등신이 우선이다.
- 눈썹은 도겸과 **같은** 짙은 일자. 이 연결이 6화의 핵심 장치다. 가늘게 그리면 안 된다.
- 다섯 여자를 함께 그리는 세신실 컷은 순옥의 손과 등·수건 위주. 여자 쪽은 등과 수건, 김으로만 처리.
- 회상(36세)은 같은 얼굴 구조로 나이만 내린다. 다른 사람처럼 예뻐지면 안 된다.
- 6화 에필로그에는 등장하지 않는다.
- 쇼츠·인스타: 수위 문제 없음. 대신 김에 얼굴이 가리는 연출을 기본으로.
- 공통: 실존 인물·연예인 이름을 프롬프트에 넣지 않는다('누구 닮게' 금지). 텍스트·로고·워터마크가 들어간 결과는 버린다.

## 5. 기존 생성 이미지와 레퍼런스 업로드

- 기존 생성 이미지 **없음**(무료 한도 소진으로 미생성, `design/gen/prompts.md`). 3-a 턴어라운드가 첫 기준 이미지가 된다.

- 색·HEX 대조용 평면 시트: `design/sheets/sunok.svg` (그림체 레퍼런스로는 쓰지 않는다).
- **레퍼런스로 업로드해 일관성 유지**
  1. 3-a 턴어라운드를 2~4번 뽑아, 체크리스트를 가장 많이 통과한 1장을 고른다.
  2. 그 이미지를 이후 모든 요청(표정·의상·클로즈업·키 비주얼)에 첨부하고, 아래 레퍼런스 문장을 맨 앞에 붙인다.
  3. 통과한 결과는 `design/gen/sunok_turnaround_01.png`처럼 저장해 다음 작업의 기준으로 쓴다. 기준 이미지는 1~2장만 유지한다(많을수록 섞인다).

**레퍼런스 문장** (이미지를 첨부했을 때 블록 맨 앞에 붙임)

```text
Use the attached image as the identity reference for Park Sun-ok. Keep exactly the same face, hairstyle, hair color, skin tone, body proportions and signature marks; change only what the prompt below asks.
```
