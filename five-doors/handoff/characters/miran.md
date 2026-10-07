# 차미란 (Cha Mi-ran) — 캐릭터 프롬프트 팩

> 작화 기준: `story/bible.md` **0-2. 확정 외형(시안 B)** > 각 인물 3·4·5절 > 3-1 대비표. 충돌하면 0-2를 따른다. 성격·버릇·소설 속 사실은 바이블 그대로다. 등장인물은 모두 성인이며 가공 인물이다.

## 1. 한 줄 요약과 절대 고정값

**와인바 '미란'의 사장, 고개를 젖히고 웃는 팜파탈 돌싱맘. 버건디 랩 원피스와 와인잔이 기본 이미지다.**

- 나이 35세 · 키 165cm · 대표 색 버건디 `#7A1E2E` · 머리 `#4A2418`

**절대 고정값 체크리스트** (생성 결과를 받을 때마다 이 목록으로 검수한다)

- [ ] 키 165cm, 7.5등신 느낌(시리즈 기준 8등신보다 살짝 짧게)
- [ ] 다섯 중 **가장 뚜렷한 모래시계**: 크고 무게 있는 가슴, 잘록한 허리, 넓게 퍼지는 골반, 풍만한 허벅지
- [ ] 더 날카로운 계란형(시안 B), 광대가 살짝
- [ ] 평소 반쯤 감긴 나른한 눈 + 스모키 아이. 크게 웃을 때만 반달
- [ ] 짙고 굵은 아치 눈썹, 동그란 코
- [ ] 도톰한 입술 + 지워지지 않는 진한 붉은 립
- [ ] 피부 `#F2CDB0`(따뜻한 톤, 붉은 조명을 잘 받음)
- [ ] 옆가르마 볼륨 빈티지 웨이브, 가슴 아래 길이, 다크 와인브라운 `#4A2418`
- [ ] 입가 오른쪽 아래 작은 점
- [ ] 오른손 손등 바깥 가는 흉터(코르크 스크루)
- [ ] 와인색 손톱 `#5A1A26`, 가늘고 유연한 손목
- [ ] 얇은 골드 후프 귀걸이, 야외에선 머리 위 선글라스
- [ ] 대표 색 버건디 `#7A1E2E`

## 2. CHARACTER LOCK (164 words)

모든 프롬프트 맨 앞(공통 스타일 문구 바로 다음)에 **한 글자도 바꾸지 않고** 붙인다. 아래 3절의 코드블록에는 이미 들어 있다.

```text
Cha Mi-ran, fictional adult character, not resembling any real person. A 35-year-old Korean woman, wine bar owner, 165 cm, a slightly shorter 7.5-head figure. The most pronounced hourglass of the cast: large heavy bust, sharply cinched waist, wide flaring hips, full thighs, a back full of curves. Sharper oval face with soft cheekbones; heavy-lidded, half-closed sultry eyes with smoky eye makeup that curve into crescents only when she laughs out loud; thick bold arched brows; rounded nose; full lips in a long-lasting deep red lipstick. Warm skin (#F2CDB0) that glows under red light. Side-parted voluminous vintage waves, dark wine-brown (#4A2418), falling below the chest. Marks: a small beauty mark below the right corner of her mouth, a thin pale scar on the outer back of her right hand, wine-colored nails (#5A1A26), thin gold hoop earrings. Habits: swirls a wine glass with a loose flexible wrist, throws her head back to laugh, smiles back over her shoulder, sways her hips when she walks in heels.
```

## 3. 생성 프롬프트

각 코드블록 = 공통 스타일 문구 + CHARACTER LOCK + 작업 지시. **블록 전체를 그대로 복사해 붙인다.** 기준 이미지(5절)가 있으면 이미지를 첨부하고, 맨 앞에 5절의 '레퍼런스 문장'을 한 줄 더 붙인다.

### 3-a. 턴어라운드 시트 (가로 3:2)

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Cha Mi-ran, fictional adult character, not resembling any real person. A 35-year-old Korean woman, wine bar owner, 165 cm, a slightly shorter 7.5-head figure. The most pronounced hourglass of the cast: large heavy bust, sharply cinched waist, wide flaring hips, full thighs, a back full of curves. Sharper oval face with soft cheekbones; heavy-lidded, half-closed sultry eyes with smoky eye makeup that curve into crescents only when she laughs out loud; thick bold arched brows; rounded nose; full lips in a long-lasting deep red lipstick. Warm skin (#F2CDB0) that glows under red light. Side-parted voluminous vintage waves, dark wine-brown (#4A2418), falling below the chest. Marks: a small beauty mark below the right corner of her mouth, a thin pale scar on the outer back of her right hand, wine-colored nails (#5A1A26), thin gold hoop earrings. Habits: swirls a wine glass with a loose flexible wrist, throws her head back to laugh, smiles back over her shoulder, sways her hips when she walks in heels.

Character turnaround model sheet of Cha Mi-ran: four full-body views side by side at identical scale and height — front, three-quarter, side profile, back. Neutral standing pose, arms relaxed slightly away from the body, feet fully visible, no cropping. Same outfit in all four views: burgundy jersey wrap dress (#741C2C) crossing under the bust, tied tight at the waist, flowing over the hips and parting at the front of the thighs, knee length; black heels, thin gold hoops. The side view must show the full hourglass curve; the back view shows the long vintage waves spilling down the back. Flat even studio lighting, plain neutral grey background (#BDBDBD). Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-b. 표정 시트 8종 (가로 3:2)

| # | 표정(바이블 연기 포인트) |
|---|---|
| 1 | 고개를 젖히고 터지는 웃음 — 반달 눈, 머리가 등 뒤로 쏟아짐 |
| 2 | 어깨 너머로 돌아보는 나른한 미소 |
| 3 | 생각 — 잔 돌리던 손목이 멈춘 순간, 눈이 가늘어짐 |
| 4 | 실패하는 웃음 — 잠금화면을 본 순간 무너지는 웃음 |
| 5 | 분노 — 웃음이 끊기고 목소리가 갈라지며 벌떡 일어남 |
| 6 | 거짓말 — 더 크게, 과장된 웃음('자기야'를 한 번 더) |
| 7 | 코르크를 뽑기 전 — 알 것 같은 비스듬한 미소('남자 거짓말은 와인이랑 같아') |
| 8 | 호스트의 여유 — 잔을 들어 올린 느긋한 승리('자기 차 간다') |

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Cha Mi-ran, fictional adult character, not resembling any real person. A 35-year-old Korean woman, wine bar owner, 165 cm, a slightly shorter 7.5-head figure. The most pronounced hourglass of the cast: large heavy bust, sharply cinched waist, wide flaring hips, full thighs, a back full of curves. Sharper oval face with soft cheekbones; heavy-lidded, half-closed sultry eyes with smoky eye makeup that curve into crescents only when she laughs out loud; thick bold arched brows; rounded nose; full lips in a long-lasting deep red lipstick. Warm skin (#F2CDB0) that glows under red light. Side-parted voluminous vintage waves, dark wine-brown (#4A2418), falling below the chest. Marks: a small beauty mark below the right corner of her mouth, a thin pale scar on the outer back of her right hand, wine-colored nails (#5A1A26), thin gold hoop earrings. Habits: swirls a wine glass with a loose flexible wrist, throws her head back to laugh, smiles back over her shoulder, sways her hips when she walks in heels.

Expression sheet of Cha Mi-ran: eight head-and-shoulders portraits in a 4x2 grid, the identical face, hairstyle, default outfit and lighting in every panel unless a panel says otherwise, slight three-quarter angle, plain neutral grey background (#BDBDBD). Panel 1: head thrown back in a big open laugh, eyes curved into crescents, waves spilling behind her shoulders. Panel 2: a languid half-lidded smile looking back over her bare shoulder. Panel 3: thinking: the wine glass she was swirling stops, eyes narrow, red lips pressed. Panel 4: a failed smile: the grin collapsing as she stares at something on a phone screen. Panel 5: anger: laughter cut off, brows drawn, mouth open mid-crack of the voice, rising to her feet. Panel 6: lying: a too-big, too-bright laugh, eyes not quite matching. Panel 7: a sly knowing sideways smile, holding up a waiter's corkscrew. Panel 8: the hostess in control: amused relaxed smirk, glass raised slightly, chin up. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-c. 의상 시트 (가로 3:2)

바이블 4절의 회차별 대표 의상 전부. 한 장에 너무 많이 넣으면 얼굴이 무너지므로 시트를 나눴다. 침실·밤 의상은 실루엣과 재질 중심이다.

#### 의상 시트 1 — 가게·놀이터·일상

1. 2화(9/4): 검은 오프숄더 블라우스 `#151214` + 버건디 슬릿 롱스커트 `#6E1A2A`(허벅지 중간 슬릿) + 꽉 묶은 검정 앞치마 + 하이힐 + 붉은 립
2. 3·4화(9/19~22): 흰 오프숄더 블라우스 `#F5F1EA` + 검정 슬릿 롱스커트 `#1A1718` + 머리 위 선글라스
3. 실내복: 오버사이즈 실크 셔츠 원피스 `#E8D8D0`, 맨발
4. 2화 9/9 세신실: 흰 목욕 수건, 방수팩 휴대폰
5. 6화 법정: 검정 롱코트

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Cha Mi-ran, fictional adult character, not resembling any real person. A 35-year-old Korean woman, wine bar owner, 165 cm, a slightly shorter 7.5-head figure. The most pronounced hourglass of the cast: large heavy bust, sharply cinched waist, wide flaring hips, full thighs, a back full of curves. Sharper oval face with soft cheekbones; heavy-lidded, half-closed sultry eyes with smoky eye makeup that curve into crescents only when she laughs out loud; thick bold arched brows; rounded nose; full lips in a long-lasting deep red lipstick. Warm skin (#F2CDB0) that glows under red light. Side-parted voluminous vintage waves, dark wine-brown (#4A2418), falling below the chest. Marks: a small beauty mark below the right corner of her mouth, a thin pale scar on the outer back of her right hand, wine-colored nails (#5A1A26), thin gold hoop earrings. Habits: swirls a wine glass with a loose flexible wrist, throws her head back to laugh, smiles back over her shoulder, sways her hips when she walks in heels.

Outfit sheet of Cha Mi-ran: 5 full-body standing figures in a row, the same person with the identical face, hair, body and marks in every figure, front or three-quarter view, neutral pose, plain neutral grey background (#BDBDBD), exact outfit colors as given. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. Figure 1: Ep2: black off-shoulder blouse (#151214) resting just on the curve of the bust, burgundy long skirt (#6E1A2A) with a slit to mid-thigh, black bistro apron tied tight at the waist, black heels, red lips. Figure 2: Ep3-4: white off-shoulder blouse (#F5F1EA), black long slit skirt (#1A1718), sunglasses pushed up on her head, gold hoops. Figure 3: Home: oversized blush-beige silk shirt dress (#E8D8D0), barefoot. Figure 4: Ep2 bathhouse: wrapped in a large white bath towel from chest to mid-thigh, phone in a clear waterproof pouch. Figure 5: Ep6 courtroom: black long coat, hair down, minimal makeup but still red lips. Tasteful fashion-lookbook presentation; skin shown only at the shoulders, back, arms and legs. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

#### 의상 시트 2 — 버건디(5·6화). 실루엣과 재질 중심

1. 5화(9/26): 버건디 저지 랩 원피스 `#741C2C` — 가슴 아래에서 엇갈려 허리를 조이고, 허벅지 앞에서 갈라짐
2. 6화: 버건디 벨벳 슬립 드레스 `#5E1324` — 깊은 V 앞섶(명치), 허리를 감아 골반에서 부풂, 허벅지 위 슬릿

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Cha Mi-ran, fictional adult character, not resembling any real person. A 35-year-old Korean woman, wine bar owner, 165 cm, a slightly shorter 7.5-head figure. The most pronounced hourglass of the cast: large heavy bust, sharply cinched waist, wide flaring hips, full thighs, a back full of curves. Sharper oval face with soft cheekbones; heavy-lidded, half-closed sultry eyes with smoky eye makeup that curve into crescents only when she laughs out loud; thick bold arched brows; rounded nose; full lips in a long-lasting deep red lipstick. Warm skin (#F2CDB0) that glows under red light. Side-parted voluminous vintage waves, dark wine-brown (#4A2418), falling below the chest. Marks: a small beauty mark below the right corner of her mouth, a thin pale scar on the outer back of her right hand, wine-colored nails (#5A1A26), thin gold hoop earrings. Habits: swirls a wine glass with a loose flexible wrist, throws her head back to laugh, smiles back over her shoulder, sways her hips when she walks in heels.

Outfit sheet of Cha Mi-ran: 2 full-body standing figures in a row, the same person with the identical face, hair, body and marks in every figure, front or three-quarter view, neutral pose, plain neutral grey background (#BDBDBD), exact outfit colors as given. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. Figure 1: Ep5: burgundy jersey wrap dress (#741C2C), crossing under the bust, tied at the waist, clinging to the hips, parting at the front of the thighs. Figure 2: Ep6: burgundy velvet slip dress (#5E1324), deep V neckline, wrapped waist, fuller over the hips, high slit to the upper thigh, gold hoops, black heels. Tasteful fashion-lookbook presentation; skin shown only at the shoulders, back, arms and legs. Clean model sheet. No text, no letters, no labels, no logo, no watermark.
```

### 3-d. 손·소품 클로즈업 (정사각 1:1)

**잔을 돌리는 손목**

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Cha Mi-ran, fictional adult character, not resembling any real person. A 35-year-old Korean woman, wine bar owner, 165 cm, a slightly shorter 7.5-head figure. The most pronounced hourglass of the cast: large heavy bust, sharply cinched waist, wide flaring hips, full thighs, a back full of curves. Sharper oval face with soft cheekbones; heavy-lidded, half-closed sultry eyes with smoky eye makeup that curve into crescents only when she laughs out loud; thick bold arched brows; rounded nose; full lips in a long-lasting deep red lipstick. Warm skin (#F2CDB0) that glows under red light. Side-parted voluminous vintage waves, dark wine-brown (#4A2418), falling below the chest. Marks: a small beauty mark below the right corner of her mouth, a thin pale scar on the outer back of her right hand, wine-colored nails (#5A1A26), thin gold hoop earrings. Habits: swirls a wine glass with a loose flexible wrist, throws her head back to laugh, smiles back over her shoulder, sways her hips when she walks in heels.

Close-up of her right hand swirling a glass of red wine by the stem with a loose flexible wrist: wine-colored nails (#5A1A26), a thin pale scar on the outer back of the hand, a red lipstick print on the glass rim, a thin gold hoop and a lock of wine-brown wave in the background. Red pendant light, dark wood bar counter. No text, no letters, no logo, no watermark.
```

**코르크를 뽑는 손**

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Cha Mi-ran, fictional adult character, not resembling any real person. A 35-year-old Korean woman, wine bar owner, 165 cm, a slightly shorter 7.5-head figure. The most pronounced hourglass of the cast: large heavy bust, sharply cinched waist, wide flaring hips, full thighs, a back full of curves. Sharper oval face with soft cheekbones; heavy-lidded, half-closed sultry eyes with smoky eye makeup that curve into crescents only when she laughs out loud; thick bold arched brows; rounded nose; full lips in a long-lasting deep red lipstick. Warm skin (#F2CDB0) that glows under red light. Side-parted voluminous vintage waves, dark wine-brown (#4A2418), falling below the chest. Marks: a small beauty mark below the right corner of her mouth, a thin pale scar on the outer back of her right hand, wine-colored nails (#5A1A26), thin gold hoop earrings. Habits: swirls a wine glass with a loose flexible wrist, throws her head back to laugh, smiles back over her shoulder, sways her hips when she walks in heels.

Close-up of her hands pulling a cork with a waiter's corkscrew from a wine bottle, the cork half out, wine-colored nails, the scar on the right hand, deep red lips blurred in the background. Warm red bar lighting. No text, no letters, no logo, no watermark.
```

### 3-e. 캐릭터 대표 키 비주얼 (세로 2:3)

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Cha Mi-ran, fictional adult character, not resembling any real person. A 35-year-old Korean woman, wine bar owner, 165 cm, a slightly shorter 7.5-head figure. The most pronounced hourglass of the cast: large heavy bust, sharply cinched waist, wide flaring hips, full thighs, a back full of curves. Sharper oval face with soft cheekbones; heavy-lidded, half-closed sultry eyes with smoky eye makeup that curve into crescents only when she laughs out loud; thick bold arched brows; rounded nose; full lips in a long-lasting deep red lipstick. Warm skin (#F2CDB0) that glows under red light. Side-parted voluminous vintage waves, dark wine-brown (#4A2418), falling below the chest. Marks: a small beauty mark below the right corner of her mouth, a thin pale scar on the outer back of her right hand, wine-colored nails (#5A1A26), thin gold hoop earrings. Habits: swirls a wine glass with a loose flexible wrist, throws her head back to laugh, smiles back over her shoulder, sways her hips when she walks in heels.

Key visual: a small wine bar after closing time. Red glass pendant lamps glow low over a dark wood counter; racks of hanging wine glasses glint behind her. She perches on the edge of the counter in a burgundy jersey wrap dress (#741C2C), one leg crossed so the wrap parts at the thigh, a glass of red wine swirling in her hand, head tilted back mid-laugh, vintage waves falling behind her. Deep red and amber light, soft shadows, velvet atmosphere. Vertical webtoon cover composition. The outfit described here replaces the default look; face, hair, body proportions and marks stay exactly as described above unless a figure or panel states otherwise. No text, no letters, no logo, no watermark.
```

## 4. 금지·주의

- 평소 눈은 **반쯤 감긴 나른한 눈**. 반달은 크게 웃을 때만. 늘 반달이면 시안 A(따뜻한 육감형)로 돌아간다.
- 머리는 **옆가르마 빈티지 웨이브 + 와인브라운**. 검정으로 나오면 하린·세라와 섞인다.
- 가장 모래시계인 사람은 미란이다. 유진이나 혜숙이 미란보다 볼륨이 커 보이면 그쪽 프롬프트를 다시 본다.
- 버건디(미란) vs 와인색(혜숙 5화 `#6B2236`): 미란은 붉은 기, 혜숙은 보랏빛. 같은 컷엔 미란=벨벳/저지+붉은 립, 혜숙=진주+올림머리로 구분.
- 붉은 립은 9시간이 지나도 그대로다. 번지는 곳은 도겸의 셔츠 깃뿐.
- 앞치마는 '라인을 강조하는' 장치다. 헐렁한 앞치마로 그리지 않는다.
- 쇼츠·인스타: 6화 벨벳 V넥은 측면·역광 실루엣이나 어깨 위 크롭. 슬릿 컷은 다리 라인까지.
- 공통: 실존 인물·연예인 이름을 프롬프트에 넣지 않는다('누구 닮게' 금지). 텍스트·로고·워터마크가 들어간 결과는 버린다.

## 5. 기존 생성 이미지와 레퍼런스 업로드

| 구분 | 링크 |
|---|---|
| 시안 B(기준) | https://www.canva.com/M/MAHXUMzjuqY |
| 시안 A(참고 금지 — 폐기안) | https://www.canva.com/M/MAHXUM5_Vjw |

- 색·HEX 대조용 평면 시트: `design/sheets/miran.svg` (그림체 레퍼런스로는 쓰지 않는다).
- **레퍼런스로 업로드해 일관성 유지**
  1. 위 '기준' 링크를 열어 이미지를 PNG로 내려받는다(Canva는 공유 화면 → 다운로드).
  2. ChatGPT 새 대화에 그 이미지를 첨부하고, 아래 레퍼런스 문장 + 3-a 턴어라운드 블록을 붙인다.
  3. 통과한 결과는 `design/gen/miran_turnaround_01.png`처럼 저장해 다음 작업의 기준으로 쓴다. 기준 이미지는 1~2장만 유지한다(많을수록 섞인다).
  4. '참고 금지'로 표시한 시안 A 이미지는 첨부하지 않는다.

**레퍼런스 문장** (이미지를 첨부했을 때 블록 맨 앞에 붙임)

```text
Use the attached image as the identity reference for Cha Mi-ran. Keep exactly the same face, hairstyle, hair color, skin tone, body proportions and signature marks; change only what the prompt below asks.
```
