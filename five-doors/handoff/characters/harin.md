# 윤하린 (Yoon Ha-rin) — 캐릭터 프롬프트 팩

> 작화 기준: `story/bible.md` **0-2. 확정 외형(시안 B)** > 각 인물 3·4·5절 > 3-1 대비표. 충돌하면 0-2를 따른다. 성격·버릇·소설 속 사실은 바이블 그대로다. 등장인물은 모두 성인이며 가공 인물이다.

## 1. 한 줄 요약과 절대 고정값

**얇은 금테 타원 안경의 로스쿨 2학년, 성숙한 지적 미인(25세 성인). 결심하면 손목의 머리끈으로 머리를 묶는다.**

- 나이 25세 · 키 163cm · 대표 색 하늘색 `#9CC7E8` · 머리 `#1C1F26`

**절대 고정값 체크리스트** (생성 결과를 받을 때마다 이 목록으로 검수한다)

- [ ] **25세 성인** — 얼굴과 비율이 성인으로 읽혀야 한다(교복·어린 비율 금지)
- [ ] 키 163cm, 7.5등신 느낌
- [ ] 마른 몸에 어울리지 않게 무게 있는 가슴(니트가 그 볼륨에서만 팽팽), 아주 가는 허리, 좁은 골반
- [ ] 좁고 뼈가 드러나는 어깨, 뾰족한 쇄골 끝, 가늘고 흰 긴 다리
- [ ] 갸름한 계란형(시안 B) + 동그란 볼은 유지
- [ ] 나른하게 반쯤 감긴 눈
- [ ] **얇은 금테 타원(OVAL) 메탈 안경**
- [ ] 옅은 자연 눈썹, 작은 코, 작고 도톰한 입술(생각할 때 아랫입술을 묾)
- [ ] 피부 `#F7DCC8`, 쉽게 붉어짐 — **귀가 먼저**
- [ ] 가슴 아래 길이 블랙 `#1C1F26` 생머리, 평소 **하프업**, 결심하면 전부 높이 묶음
- [ ] 손목의 **검정 머리끈**(늘), 콧등 안경 자국, 오른손 가운뎃손가락 펜 굳은살
- [ ] 짧고 아무것도 안 바른 손톱, 형광펜 잉크
- [ ] 앉아 있을 땐 살짝 굽은 등 → 머리를 묶으면 펴짐
- [ ] 대표 색 하늘색 `#9CC7E8`

## 2. CHARACTER LOCK (169 words)

모든 프롬프트 맨 앞(공통 스타일 문구 바로 다음)에 **한 글자도 바꾸지 않고** 붙인다. 아래 3절의 코드블록에는 이미 들어 있다.

```text
Yoon Ha-rin, fictional adult character, not resembling any real person. A 25-year-old Korean woman, second-year law school graduate student, clearly a grown adult with mature features. 163 cm, a slightly shorter 7.5-head figure. Slender frame with an unexpectedly full bust that pulls knitwear taut, a very thin waist, narrow hips, long pale slim legs, narrow bony shoulders with pointed collarbone tips. Slim oval face that keeps soft rounded cheeks; languid half-lidded eyes behind thin gold OVAL metal-frame glasses; light natural brows; small nose; small full lips she bites when thinking. Fair skin (#F7DCC8) that flushes easily, ears first. Long straight jet-black hair (#1C1F26) past the chest, usually worn half-up; tied into a high ponytail when she makes a decision. Marks: a black hair tie always on her right wrist, faint glasses marks on the nose bridge, a pen callus on the right middle finger, short bare nails. Habits: pushes up glasses that are already up; slightly hunched student posture that straightens when her hair is tied; bursts out laughing.
```

## 3. 생성 프롬프트

각 코드블록 = 공통 스타일 문구 + CHARACTER LOCK + 작업 지시. **블록 전체를 그대로 복사해 붙인다.** 기준 이미지(5절)가 있으면 이미지를 첨부하고, 맨 앞에 5절의 '레퍼런스 문장'을 한 줄 더 붙인다.

### 3-a. 턴어라운드 시트 (가로 3:2)

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Yoon Ha-rin, fictional adult character, not resembling any real person. A 25-year-old Korean woman, second-year law school graduate student, clearly a grown adult with mature features. 163 cm, a slightly shorter 7.5-head figure. Slender frame with an unexpectedly full bust that pulls knitwear taut, a very thin waist, narrow hips, long pale slim legs, narrow bony shoulders with pointed collarbone tips. Slim oval face that keeps soft rounded cheeks; languid half-lidded eyes behind thin gold OVAL metal-frame glasses; light natural brows; small nose; small full lips she bites when thinking. Fair skin (#F7DCC8) that flushes easily, ears first. Long straight jet-black hair (#1C1F26) past the chest, usually worn half-up; tied into a high ponytail when she makes a decision. Marks: a black hair tie always on her right wrist, faint glasses marks on the nose bridge, a pen callus on the right middle finger, short bare nails. Habits: pushes up glasses that are already up; slightly hunched student posture that straightens when her hair is tied; bursts out laughing.

Character turnaround model sheet of Yoon Ha-rin: four full-body views side by side at identical scale and height — front, three-quarter, side profile, back. Neutral standing pose, arms relaxed slightly away from the body, feet fully visible, no cropping. Same outfit in all four views: oatmeal sleeveless ribbed knit top (#DCCFB8), charcoal knit mini skirt (#3A3D44), white sneakers, thin gold oval glasses, black hair tie on the right wrist, hair half-up. Keep the glasses identical in all views (thin gold oval). Back view shows the half-up knot and long straight hair. Flat even studio lighting, plain neutral grey background (#BDBDBD). Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-b. 표정 시트 8종 (가로 3:2)

| # | 표정(바이블 연기 포인트) |
|---|---|
| 1 | 수줍은 미소 — 귀부터 빨개짐 |
| 2 | 당황해서 말이 빨라짐 — 이미 올라간 안경을 또 밀어 올림 |
| 3 | 울다가 웃음 — 눈물 맺힌 채 터지는 웃음 |
| 4 | 결심 — 손목의 머리끈으로 머리를 높이 묶는 순간 |
| 5 | 안경을 벗은 얼굴 — 초점 없이 가까운 곳만 보는 나른하고 어른스러운 시선 |
| 6 | 조문을 읽는 냉정 — 또박또박, 차가운 정면 시선 |
| 7 | 생각 — 아랫입술을 무는 버릇 |
| 8 | 터지는 웃음 — 웃고 나서야 웃을 일이 아님을 깨달음 |

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Yoon Ha-rin, fictional adult character, not resembling any real person. A 25-year-old Korean woman, second-year law school graduate student, clearly a grown adult with mature features. 163 cm, a slightly shorter 7.5-head figure. Slender frame with an unexpectedly full bust that pulls knitwear taut, a very thin waist, narrow hips, long pale slim legs, narrow bony shoulders with pointed collarbone tips. Slim oval face that keeps soft rounded cheeks; languid half-lidded eyes behind thin gold OVAL metal-frame glasses; light natural brows; small nose; small full lips she bites when thinking. Fair skin (#F7DCC8) that flushes easily, ears first. Long straight jet-black hair (#1C1F26) past the chest, usually worn half-up; tied into a high ponytail when she makes a decision. Marks: a black hair tie always on her right wrist, faint glasses marks on the nose bridge, a pen callus on the right middle finger, short bare nails. Habits: pushes up glasses that are already up; slightly hunched student posture that straightens when her hair is tied; bursts out laughing.

Expression sheet of Yoon Ha-rin: eight head-and-shoulders portraits in a 4x2 grid, the identical face, hairstyle, default outfit and lighting in every panel unless a panel says otherwise, slight three-quarter angle, plain neutral grey background (#BDBDBD). Panel 1: shy smile with her ears flushing red first, eyes lowered behind the glasses. Panel 2: flustered fast-talking: index finger pushing up glasses that are already up, mouth mid-word, brows raised. Panel 3: laughing and crying at once: tears on the lashes, a helpless burst of laughter. Panel 4: the decision: both hands gathering her hair into a high ponytail with the wrist hair tie, eyes hard and focused. Panel 5: glasses off: unfocused, languid, mature gaze at something very close, lips slightly parted. Panel 6: reciting a law article: cold steady front-facing stare, precise lips, glasses on. Panel 7: thinking: biting her lower lip, eyes up and to the side. Panel 8: a sudden burst of laughter, then catching herself, hand halfway to her mouth. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-c. 의상 시트 (가로 3:2)

바이블 4절의 회차별 대표 의상 전부. 한 장에 너무 많이 넣으면 얼굴이 무너지므로 시트를 나눴다. 침실·밤 의상은 실루엣과 재질 중심이다.

#### 의상 시트 1 — 3·4화

1. 3화(9/12 01:50): 오트밀 슬리브리스 골지 니트 `#DCCFB8` + 회색 트레이닝 반바지 `#8A8F98` + 안경
2. 3화(9/12 04:50): **그의 흰 셔츠 한 장** `#F4F4F2` — 단추 세 개만, 어깨선이 팔꿈치까지, 밑단 허벅지 중간, 맨다리
3. 3화(9/15): 필라테스 소그룹 운동복(라이트 그레이 탱크 + 검정 레깅스 제안)
4. 4화(9/21): 슬리브리스 니트 + 안경, 머리를 높이 묶음
5. 외출: 오버핏 셔츠 + 니트 미니스커트 + 백팩 + 운동화(백팩 끈을 두 손으로)

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Yoon Ha-rin, fictional adult character, not resembling any real person. A 25-year-old Korean woman, second-year law school graduate student, clearly a grown adult with mature features. 163 cm, a slightly shorter 7.5-head figure. Slender frame with an unexpectedly full bust that pulls knitwear taut, a very thin waist, narrow hips, long pale slim legs, narrow bony shoulders with pointed collarbone tips. Slim oval face that keeps soft rounded cheeks; languid half-lidded eyes behind thin gold OVAL metal-frame glasses; light natural brows; small nose; small full lips she bites when thinking. Fair skin (#F7DCC8) that flushes easily, ears first. Long straight jet-black hair (#1C1F26) past the chest, usually worn half-up; tied into a high ponytail when she makes a decision. Marks: a black hair tie always on her right wrist, faint glasses marks on the nose bridge, a pen callus on the right middle finger, short bare nails. Habits: pushes up glasses that are already up; slightly hunched student posture that straightens when her hair is tied; bursts out laughing.

Outfit sheet of Yoon Ha-rin: 5 full-body standing figures in a row, the same person with the identical face, hair, body and marks in every figure, front or three-quarter view, neutral pose, plain neutral grey background (#BDBDBD), exact outfit colors as given. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. Figure 1: Ep3 night: oatmeal sleeveless ribbed knit top (#DCCFB8) pulled taut over the bust, grey jersey track shorts (#8A8F98), gold oval glasses. Figure 2: Ep3 dawn: an oversized men's white dress shirt (#F4F4F2) worn as a dress, only three buttons fastened, the shoulder seam slipping to the elbow on one side, hem at mid-thigh, bare legs, barefoot. Figure 3: Ep3 pilates class: light grey loose tank top over a white sports bra, black leggings, hair half-up. Figure 4: Ep4: oatmeal sleeveless ribbed knit and charcoal knit mini skirt, glasses, hair tied up in a high ponytail. Figure 5: Outing: oversized pale blue striped shirt, charcoal knit mini skirt (#3A3D44), black backpack held by both straps, white sneakers. Tasteful fashion-lookbook presentation; skin shown only at the shoulders, back, arms and legs. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

#### 의상 시트 2 — 하늘색(5·6화)·법정

1. 5화(10/6): 하늘색 슬리브리스 니트 `#A9CBE6` + 차콜 니트 미니스커트 `#3A3D44`, 안경 벗지 않음
2. 6화: 하늘색 홀터넥 니트 미니 드레스 `#9EC8EA` — 목 뒤에서 묶음, 어깨·쇄골·팔 노출, 허벅지 위 기장. 안경 벗고 클러치에
3. 6화 법정: 회색 더플코트, 안경, 머리 묶음

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Yoon Ha-rin, fictional adult character, not resembling any real person. A 25-year-old Korean woman, second-year law school graduate student, clearly a grown adult with mature features. 163 cm, a slightly shorter 7.5-head figure. Slender frame with an unexpectedly full bust that pulls knitwear taut, a very thin waist, narrow hips, long pale slim legs, narrow bony shoulders with pointed collarbone tips. Slim oval face that keeps soft rounded cheeks; languid half-lidded eyes behind thin gold OVAL metal-frame glasses; light natural brows; small nose; small full lips she bites when thinking. Fair skin (#F7DCC8) that flushes easily, ears first. Long straight jet-black hair (#1C1F26) past the chest, usually worn half-up; tied into a high ponytail when she makes a decision. Marks: a black hair tie always on her right wrist, faint glasses marks on the nose bridge, a pen callus on the right middle finger, short bare nails. Habits: pushes up glasses that are already up; slightly hunched student posture that straightens when her hair is tied; bursts out laughing.

Outfit sheet of Yoon Ha-rin: 3 full-body standing figures in a row, the same person with the identical face, hair, body and marks in every figure, front or three-quarter view, neutral pose, plain neutral grey background (#BDBDBD), exact outfit colors as given. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. Figure 1: Ep5: sky-blue sleeveless ribbed knit (#A9CBE6), charcoal knit mini skirt (#3A3D44), glasses on. Figure 2: Ep6: sky-blue halter-neck knit mini dress (#9EC8EA) tied behind the neck, bare shoulders, collarbones and arms, hem at the upper thigh, small clutch with glasses folded inside, hair down, no glasses. Figure 3: Ep6 courtroom: mid-grey duffle coat with toggles, glasses on, hair tied up. Tasteful fashion-lookbook presentation; skin shown only at the shoulders, back, arms and legs. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-d. 손·소품 클로즈업 (정사각 1:1)

**안경 + 머리끈**

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Yoon Ha-rin, fictional adult character, not resembling any real person. A 25-year-old Korean woman, second-year law school graduate student, clearly a grown adult with mature features. 163 cm, a slightly shorter 7.5-head figure. Slender frame with an unexpectedly full bust that pulls knitwear taut, a very thin waist, narrow hips, long pale slim legs, narrow bony shoulders with pointed collarbone tips. Slim oval face that keeps soft rounded cheeks; languid half-lidded eyes behind thin gold OVAL metal-frame glasses; light natural brows; small nose; small full lips she bites when thinking. Fair skin (#F7DCC8) that flushes easily, ears first. Long straight jet-black hair (#1C1F26) past the chest, usually worn half-up; tied into a high ponytail when she makes a decision. Marks: a black hair tie always on her right wrist, faint glasses marks on the nose bridge, a pen callus on the right middle finger, short bare nails. Habits: pushes up glasses that are already up; slightly hunched student posture that straightens when her hair is tied; bursts out laughing.

Close-up of her face and right hand: the index finger pushing up thin gold OVAL metal glasses that are already at the top of her nose, a black hair tie around the right wrist, a pen callus on the middle finger, short bare nails with a faint yellow highlighter smudge, ears flushed pink. Warm desk lamp light. No text, no letters, no logo, no watermark.
```

**법전 위에 접힌 안경**

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Yoon Ha-rin, fictional adult character, not resembling any real person. A 25-year-old Korean woman, second-year law school graduate student, clearly a grown adult with mature features. 163 cm, a slightly shorter 7.5-head figure. Slender frame with an unexpectedly full bust that pulls knitwear taut, a very thin waist, narrow hips, long pale slim legs, narrow bony shoulders with pointed collarbone tips. Slim oval face that keeps soft rounded cheeks; languid half-lidded eyes behind thin gold OVAL metal-frame glasses; light natural brows; small nose; small full lips she bites when thinking. Fair skin (#F7DCC8) that flushes easily, ears first. Long straight jet-black hair (#1C1F26) past the chest, usually worn half-up; tied into a high ponytail when she makes a decision. Marks: a black hair tie always on her right wrist, faint glasses marks on the nose bridge, a pen callus on the right middle finger, short bare nails. Habits: pushes up glasses that are already up; slightly hunched student posture that straightens when her hair is tied; bursts out laughing.

Close-up of thin gold oval glasses folded on top of an open thick law book with a long yellow highlighter line across the page, a black hair tie and a capped highlighter beside it, a cold half-finished americano. Warm desk lamp cone in a dark room at 2 a.m. No text, no letters, no logo, no watermark.
```

### 3-e. 캐릭터 대표 키 비주얼 (세로 2:3)

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Yoon Ha-rin, fictional adult character, not resembling any real person. A 25-year-old Korean woman, second-year law school graduate student, clearly a grown adult with mature features. 163 cm, a slightly shorter 7.5-head figure. Slender frame with an unexpectedly full bust that pulls knitwear taut, a very thin waist, narrow hips, long pale slim legs, narrow bony shoulders with pointed collarbone tips. Slim oval face that keeps soft rounded cheeks; languid half-lidded eyes behind thin gold OVAL metal-frame glasses; light natural brows; small nose; small full lips she bites when thinking. Fair skin (#F7DCC8) that flushes easily, ears first. Long straight jet-black hair (#1C1F26) past the chest, usually worn half-up; tied into a high ponytail when she makes a decision. Marks: a black hair tie always on her right wrist, faint glasses marks on the nose bridge, a pen callus on the right middle finger, short bare nails. Habits: pushes up glasses that are already up; slightly hunched student posture that straightens when her hair is tied; bursts out laughing.

Key visual: a small studio apartment at 2 a.m. A single warm desk lamp throws a cone of light over a desk stacked with law books and highlighters; the window behind is cold blue. She sits on the desk chair with one knee pulled up, wearing an oversized men's white shirt as a dress, thin gold oval glasses, long black hair half-up, ears flushed, looking up from the book toward the viewer with a shy but steady gaze. Intimate, quiet, clearly an adult woman. Vertical webtoon cover composition. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. No text, no letters, no logo, no watermark.
```

## 4. 금지·주의

- **성인 명시가 최우선.** 25세 성인 얼굴·성인 비율(7.5등신). 교복, 책가방 아이 느낌, 지나치게 어린 얼굴은 즉시 폐기(정책 위험).
- 안경은 시안 B의 **금테 타원**. 바이블 3절·대비표의 '동그란 안경'은 시안 B로 대체됐다(3-1 대비표 '동그란 안경' 표기 주의).
- 머리는 평소 **하프업**, 결심 컷만 높이 묶음. 세라의 하이 포니테일과 겹치므로 묶은 컷에는 안경·흰 피부·니트로 구분한다.
- 하늘색 `#9CC7E8`/`#9EC8EA`와 세라의 민트는 형광등 아래서 같아 보인다(3화 설정). 작화에선 하린을 확실히 파랑 쪽으로.
- 얼굴은 유진보다 둥근 볼, 미란보다 옅은 화장(거의 맨얼굴). 붉은 립 금지.
- 셔츠 한 장 컷: 단추 세 개, 한쪽 어깨 흘러내림, 허벅지 중간. 그 이상 노출하지 않는다.
- 쇼츠·인스타: 셔츠 컷은 앉은 전신 실루엣이나 허리 위 크롭. 6화 홀터는 어깨·팔까지.
- 공통: 실존 인물·연예인 이름을 프롬프트에 넣지 않는다('누구 닮게' 금지). 텍스트·로고·워터마크가 들어간 결과는 버린다.

## 5. 기존 생성 이미지와 레퍼런스 업로드

- 기존 생성 이미지 **없음**(무료 한도 소진으로 미생성, `design/gen/prompts.md`). 3-a 턴어라운드가 첫 기준 이미지가 된다.

- 색·HEX 대조용 평면 시트: `design/sheets/harin.svg` (그림체 레퍼런스로는 쓰지 않는다).
- **레퍼런스로 업로드해 일관성 유지**
  1. 3-a 턴어라운드를 2~4번 뽑아, 체크리스트를 가장 많이 통과한 1장을 고른다.
  2. 그 이미지를 이후 모든 요청(표정·의상·클로즈업·키 비주얼)에 첨부하고, 아래 레퍼런스 문장을 맨 앞에 붙인다.
  3. 통과한 결과는 `design/gen/harin_turnaround_01.png`처럼 저장해 다음 작업의 기준으로 쓴다. 기준 이미지는 1~2장만 유지한다(많을수록 섞인다).

**레퍼런스 문장** (이미지를 첨부했을 때 블록 맨 앞에 붙임)

```text
Use the attached image as the identity reference for Yoon Ha-rin. Keep exactly the same face, hairstyle, hair color, skin tone, body proportions and signature marks; change only what the prompt below asks.
```
