# 서유진 (Seo Yu-jin) — 캐릭터 프롬프트 팩

> 작화 기준: `story/bible.md` **0-2. 확정 외형(시안 B)** > 각 인물 3·4·5절 > 3-1 대비표. 충돌하면 0-2를 따른다. 성격·버릇·소설 속 사실은 바이블 그대로다. 등장인물은 모두 성인이며 가공 인물이다.

## 1. 한 줄 요약과 절대 고정값

**입은 웃어도 눈은 웃지 않는 전직 승무원 아내. 판을 짜는 사람이고, 결정할 때 진주 귀걸이를 뺀다.**

- 나이 33세 · 키 172cm · 대표 색 회색 `#9A9EA3` · 머리 `#3A2A22`

**절대 고정값 체크리스트** (생성 결과를 받을 때마다 이 목록으로 검수한다)

- [ ] 키 172cm, 다섯 여자 중 가장 크다. 등을 펴고 턱을 당긴 승무원 자세
- [ ] 체형(시안 B): 긴 키 위의 부드러운 모래시계 — 묵직한 가슴, 길고 잘록한 허리, 둥근 골반
- [ ] **아주 길고 곧은 다리**가 최대 실루엣 포인트
- [ ] 좁고 반듯한 어깨, 깊게 팬 쇄골
- [ ] 조금 둥근 계란형 얼굴
- [ ] 나른하게 처진 눈매 + 긴 속눈썹 — **입은 웃어도 눈은 웃지 않는다**
- [ ] 가늘고 길게 정돈한 아치 눈썹, 얇고 곧은 코
- [ ] 도톰한 입술, 뮤트 로즈레드
- [ ] 피부 `#F5D5BE`(희고 매끈)
- [ ] 옆으로 넘긴 부드러운 앞머리 + 턱~쇄골 길이 웨이브 단발, 흑갈색 `#3A2A22`
- [ ] 진주 스터드 귀걸이(6화만 긴 드롭). 오른쪽 귓불 피어싱 구멍 둘(하나만 씀)
- [ ] 왼쪽 쇄골 끝의 작은 점
- [ ] 길고 흰 손, 짧은 아몬드형 누드 베이지 손톱, 얇은 결혼반지
- [ ] 대표 색 회색 `#9A9EA3`

## 2. CHARACTER LOCK (160 words)

모든 프롬프트 맨 앞(공통 스타일 문구 바로 다음)에 **한 글자도 바꾸지 않고** 붙인다. 아래 3절의 코드블록에는 이미 들어 있다.

```text
Seo Yu-jin, fictional adult character, not resembling any real person. A 33-year-old Korean woman, former flight attendant, 172 cm, the tallest woman of the cast. Soft glamorous hourglass on a tall frame: full heavy bust, long slender cinched waist, rounded hips, and very long straight legs, her strongest silhouette point. Narrow straight shoulders with deep collarbones; ramrod-straight back, chin slightly tucked. Soft, slightly rounded oval face; languid down-turned eyes with long lashes that never smile even when her lips do; long thin groomed arched brows; slim straight nose; full lips in muted rose-red. Smooth fair skin (#F5D5BE). Wavy bob between chin and collarbone, dark espresso brown (#3A2A22), with soft side-swept bangs. Marks: small pearl stud earrings, two piercing holes in the right earlobe, a tiny mole at the tip of the left collarbone, long pale hands, short almond nude-beige nails, thin wedding band. Habit: polite closed-lip smile with cool unsmiling eyes; sits upright, knees together, legs slanted to one side.
```

## 3. 생성 프롬프트

각 코드블록 = 공통 스타일 문구 + CHARACTER LOCK + 작업 지시. **블록 전체를 그대로 복사해 붙인다.** 기준 이미지(5절)가 있으면 이미지를 첨부하고, 맨 앞에 5절의 '레퍼런스 문장'을 한 줄 더 붙인다.

### 3-a. 턴어라운드 시트 (가로 3:2)

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Seo Yu-jin, fictional adult character, not resembling any real person. A 33-year-old Korean woman, former flight attendant, 172 cm, the tallest woman of the cast. Soft glamorous hourglass on a tall frame: full heavy bust, long slender cinched waist, rounded hips, and very long straight legs, her strongest silhouette point. Narrow straight shoulders with deep collarbones; ramrod-straight back, chin slightly tucked. Soft, slightly rounded oval face; languid down-turned eyes with long lashes that never smile even when her lips do; long thin groomed arched brows; slim straight nose; full lips in muted rose-red. Smooth fair skin (#F5D5BE). Wavy bob between chin and collarbone, dark espresso brown (#3A2A22), with soft side-swept bangs. Marks: small pearl stud earrings, two piercing holes in the right earlobe, a tiny mole at the tip of the left collarbone, long pale hands, short almond nude-beige nails, thin wedding band. Habit: polite closed-lip smile with cool unsmiling eyes; sits upright, knees together, legs slanted to one side.

Character turnaround model sheet of Seo Yu-jin: four full-body views side by side at identical scale and height — front, three-quarter, side profile, back. Neutral standing pose, arms relaxed slightly away from the body, feet fully visible, no cropping. Same outfit in all four views: light grey cropped knit (#BFC1C4) ending just above the waist, cream ivory high-waisted wide-leg trousers (#EAE3D6) rising above the navel, pointed nude flats, small pearl stud earrings. The back view must show the long straight spine and the wavy bob ends; the side view shows the long legs and tucked chin. Flat even studio lighting, plain neutral grey background (#BDBDBD). Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-b. 표정 시트 8종 (가로 3:2)

| # | 표정(바이블 연기 포인트) |
|---|---|
| 1 | 눈이 웃지 않는 미소 — 입꼬리만 아주 조금, 눈은 서늘 |
| 2 | 화날수록 공손 — 완벽하게 침착한 얼굴, 흔들림 없는 시선 |
| 3 | 결심 — 왼쪽 진주 귀걸이를 빼는 순간, 시선을 내리깐 단호함 |
| 4 | 등을 돌린 채 눈을 뜨고 있음 — 어둠 속에서 깨어 있는 옆얼굴 |
| 5 | 관찰 — 반 초 만에 상대를 읽는 차가운 시선 |
| 6 | 처음으로 눈까지 웃는 웃음(4화 엔딩) |
| 7 | 귓가 속삭임 — 입술을 귀에 댈 거리, 옅은 미소('너한테만 하는 얘긴데요') |
| 8 | 법정 — 검정 울 코트, 시어머니와 처음 눈이 마주친 정지 |

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Seo Yu-jin, fictional adult character, not resembling any real person. A 33-year-old Korean woman, former flight attendant, 172 cm, the tallest woman of the cast. Soft glamorous hourglass on a tall frame: full heavy bust, long slender cinched waist, rounded hips, and very long straight legs, her strongest silhouette point. Narrow straight shoulders with deep collarbones; ramrod-straight back, chin slightly tucked. Soft, slightly rounded oval face; languid down-turned eyes with long lashes that never smile even when her lips do; long thin groomed arched brows; slim straight nose; full lips in muted rose-red. Smooth fair skin (#F5D5BE). Wavy bob between chin and collarbone, dark espresso brown (#3A2A22), with soft side-swept bangs. Marks: small pearl stud earrings, two piercing holes in the right earlobe, a tiny mole at the tip of the left collarbone, long pale hands, short almond nude-beige nails, thin wedding band. Habit: polite closed-lip smile with cool unsmiling eyes; sits upright, knees together, legs slanted to one side.

Expression sheet of Seo Yu-jin: eight head-and-shoulders portraits in a 4x2 grid, the identical face, hairstyle, default outfit and lighting in every panel unless a panel says otherwise, slight three-quarter angle, plain neutral grey background (#BDBDBD). Panel 1: the signature smile: lips curve very slightly, eyes stay cool and unsmiling. Panel 2: anger as courtesy: perfectly composed polite face, steady unblinking gaze, not a single tremor. Panel 3: the decision: fingertips removing the pearl stud from her LEFT ear, eyes lowered, jaw set. Panel 4: awake in the dark: lying on her side with her back turned, eyes wide open, cheek on a pillow, moonlit. Panel 5: appraising: cool narrowed eyes reading a person in half a second, head tilted a few degrees. Panel 6: the first true smile that reaches her eyes, warm and surprised at herself. Panel 7: whispering into someone's ear at very close range, faint knowing smile, eyes sideways. Panel 8: courtroom: black wool coat, utterly still, meeting an older woman's eyes for the first time, restrained emotion. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-c. 의상 시트 (가로 3:2)

바이블 4절의 회차별 대표 의상 전부. 한 장에 너무 많이 넣으면 얼굴이 무너지므로 시트를 나눴다. 침실·밤 의상은 실루엣과 재질 중심이다.

#### 의상 시트 1 — 낮·외출·법정

1. 3·4화(9/19): 라이트 그레이 크롭 니트 `#BFC1C4` + 크림 아이보리 하이웨이스트 와이드 슬랙스 `#EAE3D6` + 진주 스터드
2. 4화(9/20~22): 같은 톤 니트 셋업, 9/22 밤엔 귀걸이를 뺀 맨 귓불
3. 외출: 몸에 붙는 니트 원피스 + 트렌치(회색 계열, 놀이터에도 귀걸이)
4. 실내복: 리넨 셔츠 + 같은 톤 팬츠(오트밀)
5. 5화 10/5 세신실: 가슴부터 허벅지까지 감은 흰 목욕 수건, 김
6. 6화 법정: 검정 울 코트 `#1E1E21`, 결혼반지 없음

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Seo Yu-jin, fictional adult character, not resembling any real person. A 33-year-old Korean woman, former flight attendant, 172 cm, the tallest woman of the cast. Soft glamorous hourglass on a tall frame: full heavy bust, long slender cinched waist, rounded hips, and very long straight legs, her strongest silhouette point. Narrow straight shoulders with deep collarbones; ramrod-straight back, chin slightly tucked. Soft, slightly rounded oval face; languid down-turned eyes with long lashes that never smile even when her lips do; long thin groomed arched brows; slim straight nose; full lips in muted rose-red. Smooth fair skin (#F5D5BE). Wavy bob between chin and collarbone, dark espresso brown (#3A2A22), with soft side-swept bangs. Marks: small pearl stud earrings, two piercing holes in the right earlobe, a tiny mole at the tip of the left collarbone, long pale hands, short almond nude-beige nails, thin wedding band. Habit: polite closed-lip smile with cool unsmiling eyes; sits upright, knees together, legs slanted to one side.

Outfit sheet of Seo Yu-jin: 6 full-body standing figures in a row, the same person with the identical face, hair, body and marks in every figure, front or three-quarter view, neutral pose, plain neutral grey background (#BDBDBD), exact outfit colors as given. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. Figure 1: Ep3-4: light grey cropped knit (#BFC1C4) + cream ivory high-waisted wide-leg trousers (#EAE3D6), pearl studs. Figure 2: Ep4: matching grey-and-ivory knit set (fitted knit top and knit wide trousers), bare earlobes. Figure 3: Outing: body-skimming grey knit midi dress (#9A9EA3) under an open beige trench coat, pearl studs. Figure 4: Home: oatmeal linen shirt with matching linen trousers, barefoot. Figure 5: Ep5 bathhouse: wrapped in a large white bath towel from chest to mid-thigh, damp hair, light steam. Figure 6: Ep6 courtroom: black wool coat (#1E1E21) buttoned, no wedding ring, pearl studs. Tasteful fashion-lookbook presentation; skin shown only at the shoulders, back, arms and legs. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

#### 의상 시트 2 — 실크(밤·5·6화). 실루엣과 재질 중심

1. 1화 새벽: 샴페인색 실크 슬립 `#E9D8B4` — 등선을 따라 흐르다 골반에서 한 번 접힘
2. 1화 밤: 검은 실크 슬립 `#141416` — 가는 끈 두 줄, 허리에서 조이고 허벅지 중간 기장, 진주 스터드
3. 5화 9/25: 회색 실크 슬립 드레스 `#A7A9AC` — 허리에서 조였다가 골반에서 퍼짐
4. 6화: 은회색 실크 드레스 `#C9CCD1` — 가는 끈 두 줄, 등은 허리선까지 파임, 양옆 높은 트임, 긴 진주 드롭

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Seo Yu-jin, fictional adult character, not resembling any real person. A 33-year-old Korean woman, former flight attendant, 172 cm, the tallest woman of the cast. Soft glamorous hourglass on a tall frame: full heavy bust, long slender cinched waist, rounded hips, and very long straight legs, her strongest silhouette point. Narrow straight shoulders with deep collarbones; ramrod-straight back, chin slightly tucked. Soft, slightly rounded oval face; languid down-turned eyes with long lashes that never smile even when her lips do; long thin groomed arched brows; slim straight nose; full lips in muted rose-red. Smooth fair skin (#F5D5BE). Wavy bob between chin and collarbone, dark espresso brown (#3A2A22), with soft side-swept bangs. Marks: small pearl stud earrings, two piercing holes in the right earlobe, a tiny mole at the tip of the left collarbone, long pale hands, short almond nude-beige nails, thin wedding band. Habit: polite closed-lip smile with cool unsmiling eyes; sits upright, knees together, legs slanted to one side.

Outfit sheet of Seo Yu-jin: 4 full-body standing figures in a row, the same person with the identical face, hair, body and marks in every figure, front or three-quarter view, neutral pose, plain neutral grey background (#BDBDBD), exact outfit colors as given. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. Figure 1: Ep1 dawn: champagne silk slip dress (#E9D8B4), thin straps, the fabric flowing down the back and folding once at the hips, knee length. Figure 2: Ep1 night: black silk slip dress (#141416), two thin double straps, softly cinched at the waist, skimming the hips, ending mid-thigh, pearl studs. Figure 3: Ep5: grey silk slip dress (#A7A9AC), cowl over the bust, cinched at the waist and flaring from the hips, knee length. Figure 4: Ep6: silver-grey silk evening gown (#C9CCD1), thin double straps, back open down to the waistline, high slits on both sides showing the long legs, long pearl drop earrings, strappy heels. Tasteful fashion-lookbook presentation; skin shown only at the shoulders, back, arms and legs. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-d. 손·소품 클로즈업 (정사각 1:1)

**진주 귀걸이를 빼는 손**

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Seo Yu-jin, fictional adult character, not resembling any real person. A 33-year-old Korean woman, former flight attendant, 172 cm, the tallest woman of the cast. Soft glamorous hourglass on a tall frame: full heavy bust, long slender cinched waist, rounded hips, and very long straight legs, her strongest silhouette point. Narrow straight shoulders with deep collarbones; ramrod-straight back, chin slightly tucked. Soft, slightly rounded oval face; languid down-turned eyes with long lashes that never smile even when her lips do; long thin groomed arched brows; slim straight nose; full lips in muted rose-red. Smooth fair skin (#F5D5BE). Wavy bob between chin and collarbone, dark espresso brown (#3A2A22), with soft side-swept bangs. Marks: small pearl stud earrings, two piercing holes in the right earlobe, a tiny mole at the tip of the left collarbone, long pale hands, short almond nude-beige nails, thin wedding band. Habit: polite closed-lip smile with cool unsmiling eyes; sits upright, knees together, legs slanted to one side.

Close-up of her face in three-quarter profile and her cold slender fingers removing a small pearl stud from her LEFT earlobe, short almond nude-beige nails, thin wedding band, the wavy espresso-brown bob tucked behind the ear. Cool window light, shallow depth of field, unsmiling eyes. No text, no letters, no logo, no watermark.
```

**날짜를 짚어 내려가는 손끝**

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Seo Yu-jin, fictional adult character, not resembling any real person. A 33-year-old Korean woman, former flight attendant, 172 cm, the tallest woman of the cast. Soft glamorous hourglass on a tall frame: full heavy bust, long slender cinched waist, rounded hips, and very long straight legs, her strongest silhouette point. Narrow straight shoulders with deep collarbones; ramrod-straight back, chin slightly tucked. Soft, slightly rounded oval face; languid down-turned eyes with long lashes that never smile even when her lips do; long thin groomed arched brows; slim straight nose; full lips in muted rose-red. Smooth fair skin (#F5D5BE). Wavy bob between chin and collarbone, dark espresso brown (#3A2A22), with soft side-swept bangs. Marks: small pearl stud earrings, two piercing holes in the right earlobe, a tiny mole at the tip of the left collarbone, long pale hands, short almond nude-beige nails, thin wedding band. Habit: polite closed-lip smile with cool unsmiling eyes; sits upright, knees together, legs slanted to one side.

Close-up of her long pale index finger tracing down a printed weekly schedule table whose cells are tinted grey, burgundy, mint, sky blue and gold, the way a flight attendant checks a passenger list. Thin wedding band. Kitchen island marble surface, morning light. No text, no letters, no logo, no watermark.
```

### 3-e. 캐릭터 대표 키 비주얼 (세로 2:3)

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Seo Yu-jin, fictional adult character, not resembling any real person. A 33-year-old Korean woman, former flight attendant, 172 cm, the tallest woman of the cast. Soft glamorous hourglass on a tall frame: full heavy bust, long slender cinched waist, rounded hips, and very long straight legs, her strongest silhouette point. Narrow straight shoulders with deep collarbones; ramrod-straight back, chin slightly tucked. Soft, slightly rounded oval face; languid down-turned eyes with long lashes that never smile even when her lips do; long thin groomed arched brows; slim straight nose; full lips in muted rose-red. Smooth fair skin (#F5D5BE). Wavy bob between chin and collarbone, dark espresso brown (#3A2A22), with soft side-swept bangs. Marks: small pearl stud earrings, two piercing holes in the right earlobe, a tiny mole at the tip of the left collarbone, long pale hands, short almond nude-beige nails, thin wedding band. Habit: polite closed-lip smile with cool unsmiling eyes; sits upright, knees together, legs slanted to one side.

Key visual: a penthouse living room at night with a floor-to-ceiling window over a lake-city skyline. She stands at the glass in a black silk slip dress (#141416), seen in three-quarter back view, the long straight back and legs forming the silhouette; her reflection in the dark glass shows the face with a faint smile and unsmiling eyes. Cool blue night light from the city, warm amber interior rim light along her shoulder, pearl stud glinting. Quiet, controlled, elegant. Vertical webtoon cover composition. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. No text, no letters, no logo, no watermark.
```

## 4. 금지·주의

- **눈이 웃지 않는다.** 결과물에서 눈이 반달이 되면 미란처럼 보인다. 4화 엔딩 외에는 무조건 다시 뽑는다.
- 대비표의 '긴 S'는 시안 B에서 모래시계 쪽으로 옮겼다. 그래도 **가장 모래시계는 미란**이다. 유진은 키와 다리 길이, 곧은 등으로 구분한다.
- 머리는 **앞머리 있는 웨이브 단발**. 시안 A의 슬릭 단발, 혹은 어깨 아래로 내려가는 길이는 오답.
- 귀걸이를 빼는 순서: 1·4화 왼쪽→오른쪽, 6화 오른쪽→왼쪽. 컷 지시에 맞춰 프롬프트의 LEFT/RIGHT를 바꾼다.
- 회색 계열 의상이 많아 세라의 4화 회색 브라톱과 겹칠 수 있다 — 유진은 실크·니트, 세라는 기능성 원단.
- 슬립 컷: 노출은 어깨·등·다리까지. 가슴 쪽은 원단이 덮는 실루엣으로만 쓴다.
- 쇼츠·인스타: 6화 등 파인 드레스는 뒷모습 실루엣·역광으로. 슬립 컷은 창에 비친 실루엣이나 허리 위 크롭.
- 공통: 실존 인물·연예인 이름을 프롬프트에 넣지 않는다('누구 닮게' 금지). 텍스트·로고·워터마크가 들어간 결과는 버린다.

## 5. 기존 생성 이미지와 레퍼런스 업로드

| 구분 | 링크 |
|---|---|
| 시안 B(기준) | https://www.canva.com/M/MAHXUMErVuU |
| 시안 A(참고 금지 — 폐기안) | https://www.canva.com/M/MAHXUKxaRCE |
| 로컬 썸네일(저해상도, 확인용) | design/gen/yujin_B.jpg |

- 색·HEX 대조용 평면 시트: `design/sheets/yujin.svg` (그림체 레퍼런스로는 쓰지 않는다).
- **레퍼런스로 업로드해 일관성 유지**
  1. 위 '기준' 링크를 열어 이미지를 PNG로 내려받는다(Canva는 공유 화면 → 다운로드).
  2. ChatGPT 새 대화에 그 이미지를 첨부하고, 아래 레퍼런스 문장 + 3-a 턴어라운드 블록을 붙인다.
  3. 통과한 결과는 `design/gen/yujin_turnaround_01.png`처럼 저장해 다음 작업의 기준으로 쓴다. 기준 이미지는 1~2장만 유지한다(많을수록 섞인다).
  4. '참고 금지'로 표시한 시안 A 이미지는 첨부하지 않는다.

**레퍼런스 문장** (이미지를 첨부했을 때 블록 맨 앞에 붙임)

```text
Use the attached image as the identity reference for Seo Yu-jin. Keep exactly the same face, hairstyle, hair color, skin tone, body proportions and signature marks; change only what the prompt below asks.
```
