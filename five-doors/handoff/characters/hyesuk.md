# 정혜숙 (Jeong Hye-suk) — 캐릭터 프롬프트 팩

> 작화 기준: `story/bible.md` **0-2. 확정 외형(시안 B)** > 각 인물 3·4·5절 > 3-1 대비표. 충돌하면 0-2를 따른다. 성격·버릇·소설 속 사실은 바이블 그대로다. 등장인물은 모두 성인이며 가공 인물이다.

## 1. 한 줄 요약과 절대 고정값

**부녀회장이자 의사 사모님. 따뜻한 성숙 글래머, 낮은 시뇽, 날개형 아이라인, 44알 진주. 웃을 때 손으로 입을 가린다.**

- 나이 42세 · 키 166cm · 대표 색 금색 `#C9A45C` · 머리 `#2B1D16`

**절대 고정값 체크리스트** (생성 결과를 받을 때마다 이 목록으로 검수한다)

- [ ] **42세 성인 여성**, 키 166cm, 7.5등신 느낌
- [ ] 무게 있는 성숙 모래시계: 풍만한 가슴, 부드럽게 꺼지는 허리, 넓고 둥근 엉덩이
- [ ] 매끈한 종아리 + 얇은 스타킹, 긴 목덜미
- [ ] 무게중심이 낮고 걸음이 느린 '서두르지 않는 몸'
- [ ] 더 둥글고 부드러운 얼굴(시안 B), 아직 탄탄한 턱선, 눈가 웃음 주름
- [ ] 가늘고 긴 눈 + **우아하게 꺾은 날개형 아이라인**
- [ ] 가늘고 높게 그린 아치 눈썹, 오뚝한 코
- [ ] 도톰한 와인 레드 입술
- [ ] 피부 `#F0CDB4`(관리한 피부, 목·손등에서 나이가 먼저)
- [ ] **낮게 틀어 올린 시뇽 + 흘러내린 몇 가닥**, 다크 초콜릿 `#2B1D16`
- [ ] **진주 목걸이 44알** — 4화부터 새 하얀 실(알 사이 실이 눈에 띔), 6화는 세 줄
- [ ] 진주 귀걸이, **빨간 손톱**, 왼쪽 약지 결혼반지 자국(반지 없음), 오른쪽 귀 뒤 작은 점
- [ ] 대표 색 금색 `#C9A45C`

## 2. CHARACTER LOCK (168 words)

모든 프롬프트 맨 앞(공통 스타일 문구 바로 다음)에 **한 글자도 바꾸지 않고** 붙인다. 아래 3절의 코드블록에는 이미 들어 있다.

```text
Jeong Hye-suk, fictional adult character, not resembling any real person. A 42-year-old Korean woman, elegant wealthy housewife and residents' association president, 166 cm, a slightly shorter 7.5-head figure. Warm mature hourglass with weight: full heavy bust, softly cinched waist, wide round hips, smooth calves in sheer stockings, a long graceful neck; a slow, low-centered, unhurried body. Soft rounded face with a still-firm jawline and fine smile lines at the eyes; long narrow eyes with elegant winged eyeliner; high thin painted arched brows; straight nose; plump wine-red lips. Well-kept skin (#F0CDB4). Dark chocolate hair (#2B1D16) in a loose low chignon at the nape with a few strands falling. Signature: a single strand of 44 pearls restrung on a visibly new bright-white silk thread, pearl stud earrings, glossy red nails, a faint pale mark on the bare left ring finger. Habits: covers her mouth with her hand when she smiles, fingers drift up to the pearls, looks down with her chin raised, perches on the edges of beds and tables.
```

## 3. 생성 프롬프트

각 코드블록 = 공통 스타일 문구 + CHARACTER LOCK + 작업 지시. **블록 전체를 그대로 복사해 붙인다.** 기준 이미지(5절)가 있으면 이미지를 첨부하고, 맨 앞에 5절의 '레퍼런스 문장'을 한 줄 더 붙인다.

### 3-a. 턴어라운드 시트 (가로 3:2)

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Jeong Hye-suk, fictional adult character, not resembling any real person. A 42-year-old Korean woman, elegant wealthy housewife and residents' association president, 166 cm, a slightly shorter 7.5-head figure. Warm mature hourglass with weight: full heavy bust, softly cinched waist, wide round hips, smooth calves in sheer stockings, a long graceful neck; a slow, low-centered, unhurried body. Soft rounded face with a still-firm jawline and fine smile lines at the eyes; long narrow eyes with elegant winged eyeliner; high thin painted arched brows; straight nose; plump wine-red lips. Well-kept skin (#F0CDB4). Dark chocolate hair (#2B1D16) in a loose low chignon at the nape with a few strands falling. Signature: a single strand of 44 pearls restrung on a visibly new bright-white silk thread, pearl stud earrings, glossy red nails, a faint pale mark on the bare left ring finger. Habits: covers her mouth with her hand when she smiles, fingers drift up to the pearls, looks down with her chin raised, perches on the edges of beds and tables.

Character turnaround model sheet of Jeong Hye-suk: four full-body views side by side at identical scale and height — front, three-quarter, side profile, back. Neutral standing pose, arms relaxed slightly away from the body, feet fully visible, no cropping. Same outfit in all four views: wine-colored jersey dress (#6B2236) clinging unbroken from bust to waist to hips, knee length, sheer nude stockings, low-heeled pumps, the 44-pearl strand on new white thread, pearl studs, red nails. Back view shows the low chignon at the nape with a few falling strands and the long neck. Side view shows the mature hourglass and slow, slightly back-weighted stance. Flat even studio lighting, plain neutral grey background (#BDBDBD). Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-b. 표정 시트 8종 (가로 3:2)

| # | 표정(바이블 연기 포인트) |
|---|---|
| 1 | 손으로 입을 가린 우아한 웃음 |
| 2 | 턱을 든 지시 — '얘, 그건 그렇게 하는 거 아니야' |
| 3 | 바닥까지 낮아진 분노 — 웃음기 없는 차가운 얼굴 |
| 4 | 불안 — 손가락이 진주 목걸이로 올라감 |
| 5 | 거짓말 — 오히려 밝고 큰 목소리의 사교적 웃음 |
| 6 | 굳는 얼굴 — 사진을 본 순간 표정이 멈춤 |
| 7 | 외로운 오후 — 창밖을 보는 고요한 옆얼굴 |
| 8 | 무장한 우아함 — 진주 세 줄, '근데 이제 그 남자도 알아' |

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Jeong Hye-suk, fictional adult character, not resembling any real person. A 42-year-old Korean woman, elegant wealthy housewife and residents' association president, 166 cm, a slightly shorter 7.5-head figure. Warm mature hourglass with weight: full heavy bust, softly cinched waist, wide round hips, smooth calves in sheer stockings, a long graceful neck; a slow, low-centered, unhurried body. Soft rounded face with a still-firm jawline and fine smile lines at the eyes; long narrow eyes with elegant winged eyeliner; high thin painted arched brows; straight nose; plump wine-red lips. Well-kept skin (#F0CDB4). Dark chocolate hair (#2B1D16) in a loose low chignon at the nape with a few strands falling. Signature: a single strand of 44 pearls restrung on a visibly new bright-white silk thread, pearl stud earrings, glossy red nails, a faint pale mark on the bare left ring finger. Habits: covers her mouth with her hand when she smiles, fingers drift up to the pearls, looks down with her chin raised, perches on the edges of beds and tables.

Expression sheet of Jeong Hye-suk: eight head-and-shoulders portraits in a 4x2 grid, the identical face, hairstyle, default outfit and lighting in every panel unless a panel says otherwise, slight three-quarter angle, plain neutral grey background (#BDBDBD). Panel 1: a gracious smile hidden behind her hand, red nails, eyes crinkling with smile lines. Panel 2: commanding: chin raised, looking down along her nose, a cool patient half smile. Panel 3: icy low-voiced anger: no smile at all, eyes heavy-lidded and cold, lips firm. Panel 4: uneasy: fingertips rising to touch the pearl necklace, eyes looking away. Panel 5: lying: an unusually bright, loud sociable smile, eyebrows lifted, one hand clenched around something small. Panel 6: frozen: her face going still and pale as she stares at a photo, smile drained away. Panel 7: a lonely gaze out of a window in golden afternoon light, profile, lips softly closed. Panel 8: armored elegance: triple pearl strands, a knowing small smile, chin up, eyes steady. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-c. 의상 시트 (가로 3:2)

바이블 4절의 회차별 대표 의상 전부. 한 장에 너무 많이 넣으면 얼굴이 무너지므로 시트를 나눴다. 침실·밤 의상은 실루엣과 재질 중심이다.

#### 의상 시트 1 — 1~4화·실내

1. 1화(9/2): 아이보리 실크 블라우스 `#EFE6D2`(진주 단추, 하나 더 풂) + 검정 펜슬스커트 `#17171A` + 얇은 스타킹 + 진주 한 줄(오래된 실)
2. 2화(9/2 16:41): 네이비 저지 원피스 `#1F2A44`, 목에 아무것도 없음, 새로 바른 립
3. 3화(9/15): 블라우스 계열, 진주 귀걸이를 만짐
4. 4화(9/20): 네이비 저지 원피스 + 새 실로 다시 꿴 진주 한 줄
5. 실내복: 캐시미어 가디건 + 실크 팬츠

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Jeong Hye-suk, fictional adult character, not resembling any real person. A 42-year-old Korean woman, elegant wealthy housewife and residents' association president, 166 cm, a slightly shorter 7.5-head figure. Warm mature hourglass with weight: full heavy bust, softly cinched waist, wide round hips, smooth calves in sheer stockings, a long graceful neck; a slow, low-centered, unhurried body. Soft rounded face with a still-firm jawline and fine smile lines at the eyes; long narrow eyes with elegant winged eyeliner; high thin painted arched brows; straight nose; plump wine-red lips. Well-kept skin (#F0CDB4). Dark chocolate hair (#2B1D16) in a loose low chignon at the nape with a few strands falling. Signature: a single strand of 44 pearls restrung on a visibly new bright-white silk thread, pearl stud earrings, glossy red nails, a faint pale mark on the bare left ring finger. Habits: covers her mouth with her hand when she smiles, fingers drift up to the pearls, looks down with her chin raised, perches on the edges of beds and tables.

Outfit sheet of Jeong Hye-suk: 5 full-body standing figures in a row, the same person with the identical face, hair, body and marks in every figure, front or three-quarter view, neutral pose, plain neutral grey background (#BDBDBD), exact outfit colors as given. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. Figure 1: Ep1: ivory silk blouse (#EFE6D2) with pearl buttons, one more button undone than usual, the silk shimmering over the bust; black pencil skirt (#17171A) hugging the hips; sheer stockings; one strand of pearls on an old yellowed thread. Figure 2: Ep2: navy jersey dress (#1F2A44) clinging from bust to hips, bare neck with no necklace, freshly applied wine-red lipstick. Figure 3: Ep3: champagne silk blouse and black pencil skirt, fingers touching a pearl earring. Figure 4: Ep4: navy jersey dress (#1F2A44) with the 44-pearl strand restrung on bright-white new thread. Figure 5: Home: camel cashmere cardigan over an ivory silk camisole top, ivory silk wide trousers, slippers. Tasteful fashion-lookbook presentation; skin shown only at the shoulders, back, arms and legs. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

#### 의상 시트 2 — 5·6화·법정·침실. 실루엣과 재질 중심

1. 1화 침실: 피부색 레이스 + 얇은 스타킹 — 패션 화보 수준(누드톤 레이스 슬립)
2. 5화(10/1): 와인색 저지 원피스 `#6B2236` + 새 실의 진주 44알
3. 5화(10/5): 열탕 가장자리, 머리에 수건
4. 6화: 금색 시퀸 오프숄더 원피스 `#CFA950` — 가슴 굴곡을 따라 빛의 비늘, 허리를 바짝, 무릎 아래까지 좁게. 진주 세 줄
5. 6화 법정: 검정 캐시미어 코트

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Jeong Hye-suk, fictional adult character, not resembling any real person. A 42-year-old Korean woman, elegant wealthy housewife and residents' association president, 166 cm, a slightly shorter 7.5-head figure. Warm mature hourglass with weight: full heavy bust, softly cinched waist, wide round hips, smooth calves in sheer stockings, a long graceful neck; a slow, low-centered, unhurried body. Soft rounded face with a still-firm jawline and fine smile lines at the eyes; long narrow eyes with elegant winged eyeliner; high thin painted arched brows; straight nose; plump wine-red lips. Well-kept skin (#F0CDB4). Dark chocolate hair (#2B1D16) in a loose low chignon at the nape with a few strands falling. Signature: a single strand of 44 pearls restrung on a visibly new bright-white silk thread, pearl stud earrings, glossy red nails, a faint pale mark on the bare left ring finger. Habits: covers her mouth with her hand when she smiles, fingers drift up to the pearls, looks down with her chin raised, perches on the edges of beds and tables.

Outfit sheet of Jeong Hye-suk: 5 full-body standing figures in a row, the same person with the identical face, hair, body and marks in every figure, front or three-quarter view, neutral pose, plain neutral grey background (#BDBDBD), exact outfit colors as given. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. Figure 1: Ep1 private: nude-tone lace slip dress with thin straps, knee length, sheer stockings, pearl strand; fashion editorial, elegant and covered. Figure 2: Ep5: wine-colored jersey dress (#6B2236) folding in at the waist, the 44 pearls on new white thread, red nails, fountain pen in hand. Figure 3: Ep5 bathhouse: sitting at the edge of a hot pool wrapped in a white bath towel, a folded towel on her head, steam. Figure 4: Ep6: gold sequin off-shoulder dress (#CFA950), the sequins rising like scales of light over the bust, tightly cinched waist, molded over the hips, narrow to below the knee; three strands of pearls. Figure 5: Ep6 courtroom: black cashmere coat, single pearl strand, chignon. Tasteful fashion-lookbook presentation; skin shown only at the shoulders, back, arms and legs. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-d. 손·소품 클로즈업 (정사각 1:1)

**44알 진주 + 새 하얀 실**

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Jeong Hye-suk, fictional adult character, not resembling any real person. A 42-year-old Korean woman, elegant wealthy housewife and residents' association president, 166 cm, a slightly shorter 7.5-head figure. Warm mature hourglass with weight: full heavy bust, softly cinched waist, wide round hips, smooth calves in sheer stockings, a long graceful neck; a slow, low-centered, unhurried body. Soft rounded face with a still-firm jawline and fine smile lines at the eyes; long narrow eyes with elegant winged eyeliner; high thin painted arched brows; straight nose; plump wine-red lips. Well-kept skin (#F0CDB4). Dark chocolate hair (#2B1D16) in a loose low chignon at the nape with a few strands falling. Signature: a single strand of 44 pearls restrung on a visibly new bright-white silk thread, pearl stud earrings, glossy red nails, a faint pale mark on the bare left ring finger. Habits: covers her mouth with her hand when she smiles, fingers drift up to the pearls, looks down with her chin raised, perches on the edges of beds and tables.

Close-up of her collarbone and neck: a single strand of 44 pearls restrung on a visibly bright-white new silk thread, the thread showing clearly between each pearl; red-nailed fingertips lifting one pearl; a few strands from the low chignon falling on the long neck. Golden afternoon light. No text, no letters, no logo, no watermark.
```

**손바닥 위의 마흔네 번째 진주**

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Jeong Hye-suk, fictional adult character, not resembling any real person. A 42-year-old Korean woman, elegant wealthy housewife and residents' association president, 166 cm, a slightly shorter 7.5-head figure. Warm mature hourglass with weight: full heavy bust, softly cinched waist, wide round hips, smooth calves in sheer stockings, a long graceful neck; a slow, low-centered, unhurried body. Soft rounded face with a still-firm jawline and fine smile lines at the eyes; long narrow eyes with elegant winged eyeliner; high thin painted arched brows; straight nose; plump wine-red lips. Well-kept skin (#F0CDB4). Dark chocolate hair (#2B1D16) in a loose low chignon at the nape with a few strands falling. Signature: a single strand of 44 pearls restrung on a visibly new bright-white silk thread, pearl stud earrings, glossy red nails, a faint pale mark on the bare left ring finger. Habits: covers her mouth with her hand when she smiles, fingers drift up to the pearls, looks down with her chin raised, perches on the edges of beds and tables.

Close-up of her open palm with glossy red nails holding one single loose pearl, a white marble floor and a few scattered pearls blurred below, a pale mark on the bare left ring finger. Warm golden light shaft. No text, no letters, no logo, no watermark.
```

### 3-e. 캐릭터 대표 키 비주얼 (세로 2:3)

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Jeong Hye-suk, fictional adult character, not resembling any real person. A 42-year-old Korean woman, elegant wealthy housewife and residents' association president, 166 cm, a slightly shorter 7.5-head figure. Warm mature hourglass with weight: full heavy bust, softly cinched waist, wide round hips, smooth calves in sheer stockings, a long graceful neck; a slow, low-centered, unhurried body. Soft rounded face with a still-firm jawline and fine smile lines at the eyes; long narrow eyes with elegant winged eyeliner; high thin painted arched brows; straight nose; plump wine-red lips. Well-kept skin (#F0CDB4). Dark chocolate hair (#2B1D16) in a loose low chignon at the nape with a few strands falling. Signature: a single strand of 44 pearls restrung on a visibly new bright-white silk thread, pearl stud earrings, glossy red nails, a faint pale mark on the bare left ring finger. Habits: covers her mouth with her hand when she smiles, fingers drift up to the pearls, looks down with her chin raised, perches on the edges of beds and tables.

Key visual: a luxury apartment living room in the afternoon. The curtains are open only one hand's width, letting a single shaft of golden light fall across a marble floor, a white sofa and lilies on a console. She perches on the edge of a glass coffee table in a wine-colored jersey dress (#6B2236), legs crossed in sheer stockings, chin raised, one red-nailed hand covering her smile, the 44-pearl strand glowing in the light, low chignon with a few loose strands. Warm gold and cream palette. Vertical webtoon cover composition. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. No text, no letters, no logo, no watermark.
```

## 4. 금지·주의

- **성숙함이 매력이다.** 20대처럼 젊게 그리지 않는다. 웃음 주름, 목·손등의 나이 질감을 남기되 아이라인으로 우아하게.
- 머리는 시안 B의 **낮은 시뇽 + 흘러내린 몇 가닥**. 시안 A의 프렌치 트위스트(높고 단단한 올림)는 폐기안. 머리를 푸는 컷은 거의 없다.
- 진주 연속성: 1화 오래된 실 한 줄 → 2화 16:41 이후 목에 없음 → 4화부터 **새 하얀 실 44알** → 6화 세 줄.
- 와인색 `#6B2236`(혜숙 5화)과 미란의 버건디는 비슷하다. 같은 컷엔 혜숙=진주·시뇽·손으로 가린 미소로 구분.
- 부녀회 임원 셋(50대)과 겹치지 않게: 혜숙만 날개형 아이라인·빨간 손톱·글래머 실루엣.
- 침실 의상은 '누드톤 레이스 슬립 + 스타킹' 패션 화보 수준에서 멈춘다.
- 쇼츠·인스타: 6화 시퀸은 그대로 써도 되는 대표 이미지. 침실 컷은 빛줄기 속 실루엣·등과 어깨만.
- 공통: 실존 인물·연예인 이름을 프롬프트에 넣지 않는다('누구 닮게' 금지). 텍스트·로고·워터마크가 들어간 결과는 버린다.

## 5. 기존 생성 이미지와 레퍼런스 업로드

- 기존 생성 이미지 **없음**(무료 한도 소진으로 미생성, `design/gen/prompts.md`). 3-a 턴어라운드가 첫 기준 이미지가 된다.

- 색·HEX 대조용 평면 시트: `design/sheets/hyesuk.svg` (그림체 레퍼런스로는 쓰지 않는다).
- **레퍼런스로 업로드해 일관성 유지**
  1. 3-a 턴어라운드를 2~4번 뽑아, 체크리스트를 가장 많이 통과한 1장을 고른다.
  2. 그 이미지를 이후 모든 요청(표정·의상·클로즈업·키 비주얼)에 첨부하고, 아래 레퍼런스 문장을 맨 앞에 붙인다.
  3. 통과한 결과는 `design/gen/hyesuk_turnaround_01.png`처럼 저장해 다음 작업의 기준으로 쓴다. 기준 이미지는 1~2장만 유지한다(많을수록 섞인다).

**레퍼런스 문장** (이미지를 첨부했을 때 블록 맨 앞에 붙임)

```text
Use the attached image as the identity reference for Jeong Hye-suk. Keep exactly the same face, hairstyle, hair color, skin tone, body proportions and signature marks; change only what the prompt below asks.
```
