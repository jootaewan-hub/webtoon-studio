# 캐릭터 시트 프롬프트 (ChatGPT·Codex용)

만든 도구: `python tools/char_prompts.py` (원본: `design/characters.json`, `design/style_guide.md` 6절, `design/outfits_en.json`).

사용법:
1. 인물마다 ① 턴어라운드를 먼저 만들고, 마음에 드는 결과를 `renders/characters/<id>_turnaround.png`로 저장한다.
2. ② 표정·③ 의상 시트는 ①의 이미지를 함께 올리고 "same character as the attached image"를 앞에 붙여 만든다(인물 일관성).
3. 콘티 컷을 만들 때도 해당 인물의 턴어라운드 이미지를 참고 이미지로 함께 올린다.

## 은주 (eunju) — A 들고양이 — 이마를 드러낸 잔머리

- 나이·키: 13세 · 140cm · 5.5등신
- 연기: 큰 표정 대신 귀와 손. 감동은 숨 멈춤으로. 마지막 무대에서 처음 활짝 웃는다. 목에 은색 소리굽쇠 목걸이

### ① 턴어라운드
```
character turnaround sheet, Eunju, 13-year-old Korean girl, 140cm, small and thin, sun-tanned skin, narrow small face, large long almond-shaped eyes, thick straight eyebrows, no bangs with the forehead visible, loose wisps of hair falling at both temples, faint freckles on nose and cheeks, long dark-brown hair tied low at the nape with a single rubber band, a small silver tuning-fork pendant on a thin chain, tilts her head slightly to the left when listening, wearing an oversized navy work jacket (hand-me-down), worn trousers with frayed knees, plain white knitted cotton work gloves with no rubber coating, rubber boots, front view, three-quarter view, side view, back view, standing neutral pose, full body, same scale in every view, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ② 표정 시트
```
same character as the attached image: Eunju, 13-year-old Korean girl, 140cm, small and thin, sun-tanned skin, narrow small face, large long almond-shaped eyes, thick straight eyebrows, no bangs with the forehead visible, loose wisps of hair falling at both temples, faint freckles on nose and cheeks, long dark-brown hair tied low at the nape with a single rubber band, a small silver tuning-fork pendant on a thin chain, tilts her head slightly to the left when listening. Expression sheet, head and shoulders, (1) neutral expressionless face, (2) listening intently, head tilted slightly to the left, eyes half-lowered, (3) surprised, eyes wide, (4) frightened, shoulders drawn in, (5) sad, holding back tears, (6) a faint smile, (7) a big open smile, consistent face in every panel, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ④ 15년 뒤(2003, 에필로그 3-34)
```
character turnaround sheet, Eunju at 29, an adult Korean woman violinist, slim, the same narrow face, long almond-shaped eyes and faint freckles, long dark-brown hair still tied low with a single rubber band, the same small silver tuning-fork pendant, wearing a simple deep-navy long concert dress, front view, three-quarter view, side view, back view, standing neutral pose, full body, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ③ 의상 시트

| # | 의상 | 등장 |
|---|---|---|
| 1 | 큰 남색 점퍼·해진 바지·목장갑 | 기본(일정표에 없는 씬) |
| 2 | 흰 블라우스·감색 치마(학교) | — |
| 3 | 빌린 흰 원피스(무대) | — |
| 4 | 남색 점퍼·회색 손뜨개 목도리·목장갑(겨울) | 2-14, 2-15, 2-16 |
| 5 | 남색 점퍼·회색 손뜨개 목도리·손끝 자른 목장갑(겨울) | 2-17 |
| 6 | 빛바랜 하늘색 반소매 셔츠·해진 바지(여름) | 3-6, 3-7, 3-8, 3-9, 3-10, 3-11, 3-12, 3-13, 3-14, 3-15, 3-33 |

```
same character as the attached image: Eunju, 13-year-old Korean girl, 140cm, small and thin, sun-tanned skin, narrow small face, large long almond-shaped eyes, thick straight eyebrows, no bangs with the forehead visible, loose wisps of hair falling at both temples, faint freckles on nose and cheeks, long dark-brown hair tied low at the nape with a single rubber band, a small silver tuning-fork pendant on a thin chain, tilts her head slightly to the left when listening. Outfit sheet, full body front view in each outfit: (1) an oversized navy work jacket (hand-me-down), worn trousers with frayed knees, plain white knitted cotton work gloves with no rubber coating, rubber boots; (2) her own plain everyday clothes, not a school uniform: a faded white cotton blouse and a plain navy skirt; (3) a borrowed plain white cotton dress, a little too big for her, long sleeves that keep sliding down to half cover the backs of her hands, hem well below the knee, no frills, no lace; (4) the oversized navy work jacket zipped to the chin, a gray hand-knitted scarf, plain white knitted cotton work gloves with no rubber coating, worn trousers, rubber boots; (5) the oversized navy work jacket zipped to the chin, a gray hand-knitted scarf, plain white knitted cotton work gloves with no rubber coating with the fingertips cut off, worn trousers, rubber boots; (6) a faded light-blue short-sleeved cotton shirt, worn trousers with frayed knees, worn canvas sneakers (rubber boots and plain white cotton work gloves only when working on the trash hill). Same face and body in every outfit, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

## 동민 (dongmin) — 추천안(바이블 기준 세부 고정)

- 나이·키: 9세 · 125cm · 5등신
- 연기: 몸 전체로 말한다. 슬픈 장면에서 엉뚱한 한마디

### ① 턴어라운드
```
character turnaround sheet, Dongmin, 9-year-old Korean boy, 125cm, round face, very short uneven clipper buzz cut (same length all over, no fade), upper-left front tooth missing, big ears, adhesive bandage on the right knee, wearing an oversized hand-me-down loose green cotton-knit tracksuit with a single contrasting stripe down the sides, baggy at the knees, elastic cuffs, no logo, front view, three-quarter view, side view, back view, standing neutral pose, full body, same scale in every view, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ② 표정 시트
```
same character as the attached image: Dongmin, 9-year-old Korean boy, 125cm, round face, very short uneven clipper buzz cut (same length all over, no fade), upper-left front tooth missing, big ears, adhesive bandage on the right knee. Expression sheet, head and shoulders, (1) a big open smile, (2) surprised, eyes wide, (3) about to cry, trembling lips, (4) serious and determined, consistent face in every panel, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ④ 15년 뒤(2003, 에필로그 3-34)
```
character turnaround sheet, Dongmin at 25, an adult Korean man and percussionist, round face, short hair, big ears, a warm grin, holding drumsticks, wearing a plain black T-shirt and straight-leg jeans, front view, three-quarter view, side view, back view, standing neutral pose, full body, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ③ 의상 시트

| # | 의상 | 등장 |
|---|---|---|
| 1 | 물려받은 큰 운동복 | 기본(일정표에 없는 씬) |
| 2 | 물려받은 누빈 갈색 점퍼·털모자(겨울) | 2-14, 2-15, 2-16, 2-17 |
| 3 | 초록 반소매 체육복 티·반바지(여름) | 3-8, 3-9, 3-10, 3-11, 3-12, 3-13, 3-14, 3-15, 3-33 |
| 4 | 흰 반소매 남방·감색 반바지(제일 좋은 옷) | 2-18, 2-19 |
| 5 | 흰 반소매 남방·감색 반바지·빨간 손수건(본선) | 3-16, 3-17, 3-18, 3-19, 3-20, 3-21, 3-22, 3-23, 3-24, 3-25, 3-26, 3-27, 3-28, 3-29, 3-30 |

```
same character as the attached image: Dongmin, 9-year-old Korean boy, 125cm, round face, very short uneven clipper buzz cut (same length all over, no fade), upper-left front tooth missing, big ears, adhesive bandage on the right knee. Outfit sheet, full body front view in each outfit: (1) an oversized hand-me-down loose green cotton-knit tracksuit with a single contrasting stripe down the sides, baggy at the knees, elastic cuffs, no logo; (2) an oversized hand-me-down quilted brown jacket over the loose green tracksuit, a knitted wool hat; (3) a green short-sleeved cotton gym T-shirt and matching green shorts, worn canvas sneakers; (4) his best clothes: a white short-sleeved button shirt and navy shorts, white knee socks, sneakers; (5) his best clothes: a white short-sleeved button shirt and navy shorts, sneakers, a small red cloth neckerchief tied at the neck. Same face and body in every outfit, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

## 만석 (manseok) — B 지친 노동자 — 낡은 작업모

- 나이·키: 41세 · 170cm · 7등신
- 연기: 사랑을 말로 못 하는 아버지. 감정은 손과 등으로

### ① 턴어라운드
```
character turnaround sheet, Manseok, 41-year-old Korean man, 170cm, gaunt and slightly stooped, long gaunt face, hollow cheeks, stubble, always wears a worn plain olive cotton work cap with a short soft frayed brim (no logo, no emblem) over short hair streaked with gray, long fingers, wearing a worn, faded plain solid olive-drab 1980s Korean army field jacket (no camouflage pattern, no patches, no insignia, no name tape), a cotton towel around the neck, worn dark work trousers, rubber boots, front view, three-quarter view, side view, back view, standing neutral pose, full body, same scale in every view, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ② 표정 시트
```
same character as the attached image: Manseok, 41-year-old Korean man, 170cm, gaunt and slightly stooped, long gaunt face, hollow cheeks, stubble, always wears a worn plain olive cotton work cap with a short soft frayed brim (no logo, no emblem) over short hair streaked with gray, long fingers. Expression sheet, head and shoulders, (1) neutral expressionless face, (2) angry, frowning, (3) quietly sad, (4) tired sideways glance, (5) a faint smile, consistent face in every panel, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ④ 15년 뒤(2003, 에필로그 3-34)
```
character turnaround sheet, Manseok at 57, an older Korean man, white hair with no cap, gaunt face softened by age, long fingers, wearing a pressed white shirt and black trousers, no cap, white hair, front view, three-quarter view, side view, back view, standing neutral pose, full body, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ⑤ 회상(3-3)
```
character turnaround sheet, Manseok at about 30 in the 1970s, a young Korean clarinetist in a theater show band, slim, short neat hair, no cap, long fingers, wearing a 1970s Korean theater show band uniform: a white jacket with wide peaked lapels, a white shirt, a black bow tie, dark flared trousers, front view, three-quarter view, side view, back view, standing neutral pose, full body, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ③ 의상 시트

| # | 의상 | 등장 |
|---|---|---|
| 1 | 낡은 야전상의·목수건·고무장화 | 기본(일정표에 없는 씬) |
| 2 | 낡은 야전상의·다린 셔츠·운동화(본선) | 3-16, 3-19, 3-21, 3-23, 3-25, 3-26, 3-29 |

```
same character as the attached image: Manseok, 41-year-old Korean man, 170cm, gaunt and slightly stooped, long gaunt face, hollow cheeks, stubble, always wears a worn plain olive cotton work cap with a short soft frayed brim (no logo, no emblem) over short hair streaked with gray, long fingers. Outfit sheet, full body front view in each outfit: (1) a worn, faded plain solid olive-drab 1980s Korean army field jacket (no camouflage pattern, no patches, no insignia, no name tape), a cotton towel around the neck, worn dark work trousers, rubber boots; (2) the same worn plain solid olive-drab field jacket (no camouflage pattern, no patches, no insignia), collar pulled closed, over a pressed collared shirt, dark trousers, worn canvas sneakers instead of rubber boots, no towel. Same face and body in every outfit, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

## 곽 영감 (kwak) — A 각진 장인 — 꼿꼿한 허리

- 나이·키: 68세 · 160cm · 6.5등신
- 연기: 표정 변화 거의 없음. 감정은 작업하는 손의 속도로. 웃음은 두 번뿐

### ① 턴어라운드
```
character turnaround sheet, old Kwak, 68-year-old Korean man, 160cm, short and solidly built with an upright posture (not stooped), square jaw, short white buzz cut, short thick white eyebrows, deep forehead wrinkles, thick forearms, reading glasses pushed up on his forehead, a pencil behind his ear, ring and little finger of the right hand permanently bent, wearing a canvas work apron dusted with sawdust over a faded gray long-sleeved work shirt and dark work trousers, cloth arm sleeves, front view, three-quarter view, side view, back view, standing neutral pose, full body, same scale in every view, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ② 표정 시트
```
same character as the attached image: old Kwak, 68-year-old Korean man, 160cm, short and solidly built with an upright posture (not stooped), square jaw, short white buzz cut, short thick white eyebrows, deep forehead wrinkles, thick forearms, reading glasses pushed up on his forehead, a pencil behind his ear, ring and little finger of the right hand permanently bent. Expression sheet, head and shoulders, (1) neutral expressionless face, (2) sideways glance, (3) serious and determined, (4) a faint smile, (5) a big open smile, consistent face in every panel, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ④ 15년 뒤(2003, 에필로그 3-34)
```
character turnaround sheet, old Kwak at 84, still healthy and upright, short white buzz cut, deeper wrinkles, a pencil behind his ear, wearing a clean brown cardigan over a shirt, front view, three-quarter view, side view, back view, standing neutral pose, full body, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ③ 의상 시트

| # | 의상 | 등장 |
|---|---|---|
| 1 | 톱밥 묻은 캔버스 앞치마·팔토시 | 기본(일정표에 없는 씬) |
| 2 | 앞치마 위 회색 털조끼·털모자(겨울) | 2-14, 2-15, 2-16, 2-17 |
| 3 | 앞치마·반소매 작업 셔츠(여름) | 3-9, 3-15 |
| 4 | 다린 흰 반소매 셔츠·회색 바지(본선) | 3-18, 3-22, 3-24, 3-27 |

```
same character as the attached image: old Kwak, 68-year-old Korean man, 160cm, short and solidly built with an upright posture (not stooped), square jaw, short white buzz cut, short thick white eyebrows, deep forehead wrinkles, thick forearms, reading glasses pushed up on his forehead, a pencil behind his ear, ring and little finger of the right hand permanently bent. Outfit sheet, full body front view in each outfit: (1) a canvas work apron dusted with sawdust over a faded gray long-sleeved work shirt and dark work trousers, cloth arm sleeves; (2) a gray knitted vest over the canvas work apron, a knitted wool hat; (3) a canvas work apron dusted with sawdust over a faded short-sleeved work shirt, dark work trousers, cloth arm sleeves; (4) his going-out clothes: a pressed white short-sleeved shirt buttoned to the top, gray trousers, reading glasses on his nose. Same face and body in every outfit, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

## 선영 (seonyoung) — B 1980년대 파마 단발 — 큰 금테

- 나이·키: 23세 · 162cm · 7등신
- 연기: 아이들보다 더 허둥대지만 결정적일 때 단단하다

### ① 턴어라운드
```
character turnaround sheet, Seonyoung, 23-year-old Korean woman, 162cm, slim, round face, voluminous softly permed 1980s bob with fluffy bangs, large round thin gold-rim glasses, wearing a wrinkled white shirt, a cardigan, a long flared skirt, front view, three-quarter view, side view, back view, standing neutral pose, full body, same scale in every view, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ② 표정 시트
```
same character as the attached image: Seonyoung, 23-year-old Korean woman, 162cm, slim, round face, voluminous softly permed 1980s bob with fluffy bangs, large round thin gold-rim glasses. Expression sheet, head and shoulders, (1) flustered and startled, (2) nervous, cold sweat, (3) a faint smile, (4) serious and determined, (5) about to cry, trembling lips, consistent face in every panel, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ④ 15년 뒤(2003, 에필로그 3-34)
```
character turnaround sheet, Seonyoung at 38, a Korean music teacher, shoulder-length softly permed hair, the same large round gold-rim glasses, wearing a neat navy skirt suit, front view, three-quarter view, side view, back view, standing neutral pose, full body, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ③ 의상 시트

| # | 의상 | 등장 |
|---|---|---|
| 1 | 구겨진 흰 셔츠·카디건·긴 플레어스커트 | 기본(일정표에 없는 씬) |
| 2 | 검은 연주복(무대) | — |
| 3 | 베이지 더플코트·목도리(늦가을~겨울) | 2-8, 2-9, 2-14, 2-15, 2-16, 2-17 |
| 4 | 구겨진 흰 반소매 블라우스·긴 플레어스커트(여름) | 3-8, 3-10 |

```
same character as the attached image: Seonyoung, 23-year-old Korean woman, 162cm, slim, round face, voluminous softly permed 1980s bob with fluffy bangs, large round thin gold-rim glasses. Outfit sheet, full body front view in each outfit: (1) a wrinkled white shirt, a cardigan, a long flared skirt; (2) a plain black concert outfit; (3) a beige duffle coat and a scarf over a long skirt; (4) a wrinkled white short-sleeved blouse and a long flared skirt, no cardigan. Same face and body in every outfit, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

## 최 계장 (choi) — 추천안(바이블 기준 세부 고정)

- 나이·키: 46세 · 168cm · 6.5등신
- 연기: 웃기지 않으려는데 웃긴 사람. 진지할수록 땀을 닦는다

### ① 턴어라운드
```
character turnaround sheet, Mr. Choi, 46-year-old Korean civil servant, 168cm, medium height with a slight belly, shiny pomaded 7:3 side part, thick black horn-rimmed glasses, a sheen of sweat on the forehead, a white handkerchief in hand, wearing a gray suit and tie, carrying a manila document envelope, front view, three-quarter view, side view, back view, standing neutral pose, full body, same scale in every view, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ② 표정 시트
```
same character as the attached image: Mr. Choi, 46-year-old Korean civil servant, 168cm, medium height with a slight belly, shiny pomaded 7:3 side part, thick black horn-rimmed glasses, a sheen of sweat on the forehead, a white handkerchief in hand. Expression sheet, head and shoulders, (1) neutral expressionless face, (2) nervous, cold sweat, (3) flustered, (4) serious and determined, (5) about to cry, trembling lips, consistent face in every panel, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ④ 15년 뒤(2003, 에필로그 3-34)
```
character turnaround sheet, Mr. Choi at 62, a retired Korean civil servant, thinning gray pomaded hair, thick horn-rimmed glasses, a handkerchief in hand, wearing a gray suit without a tie, front view, three-quarter view, side view, back view, standing neutral pose, full body, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ③ 의상 시트

| # | 의상 | 등장 |
|---|---|---|
| 1 | 회색 양복·넥타이·서류 봉투 | 기본(일정표에 없는 씬) |
| 2 | 회색 양복 위 감색 오버코트(겨울) | 2-14, 2-15, 2-16, 2-17 |
| 3 | 흰 반소매 와이셔츠·넥타이, 양복 상의는 의자에(여름) | 3-12, 3-13, 3-14 |

```
same character as the attached image: Mr. Choi, 46-year-old Korean civil servant, 168cm, medium height with a slight belly, shiny pomaded 7:3 side part, thick black horn-rimmed glasses, a sheen of sweat on the forehead, a white handkerchief in hand. Outfit sheet, full body front view in each outfit: (1) a gray suit and tie, carrying a manila document envelope; (2) a navy wool overcoat over the gray suit; (3) a white short-sleeved dress shirt with a tie, gray suit trousers, the gray suit jacket hung on the chair back or carried over his arm. Same face and body in every outfit, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

## 태준 (taejun) — A 차가운 우등생 — 가는 눈

- 나이·키: 14세 · 165cm · 6.5등신
- 연기: 완벽한 자세 속 긴장. 무너질 때 손끝이 먼저 떨린다

### ① 턴어라운드
```
character turnaround sheet, Taejun, 14-year-old Korean boy, 165cm, tall and slim, long face, narrow long eyes, sharp 7:3 side part with the forehead visible, thin lips, pale skin, very straight posture, wearing a late-1980s Korean private middle-school uniform: a navy wool blazer with a small school badge, a white shirt, a plain dark tie, matching dark trousers in a loose straight cut; not a black high-collar uniform, not a sailor uniform, front view, three-quarter view, side view, back view, standing neutral pose, full body, same scale in every view, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ② 표정 시트
```
same character as the attached image: Taejun, 14-year-old Korean boy, 165cm, tall and slim, long face, narrow long eyes, sharp 7:3 side part with the forehead visible, thin lips, pale skin, very straight posture. Expression sheet, head and shoulders, (1) cold and composed, (2) a slight sneer, (3) surprised, eyes wide, (4) nervous, cold sweat, (5) a faint smile, consistent face in every panel, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ④ 15년 뒤(2003, 에필로그 3-34)
```
character turnaround sheet, Taejun at 29, an adult Korean man violinist, tall and slim, neat side part, a calmer face, wearing a black concert suit, front view, three-quarter view, side view, back view, standing neutral pose, full body, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ③ 의상 시트

| # | 의상 | 등장 |
|---|---|---|
| 1 | 사립학교 교복(감색 재킷·넥타이) | 기본(일정표에 없는 씬) |
| 2 | 검은 연주복 | — |

```
same character as the attached image: Taejun, 14-year-old Korean boy, 165cm, tall and slim, long face, narrow long eyes, sharp 7:3 side part with the forehead visible, thin lips, pale skin, very straight posture. Outfit sheet, full body front view in each outfit: (1) a late-1980s Korean private middle-school uniform: a navy wool blazer with a small school badge, a white shirt, a plain dark tie, matching dark trousers in a loose straight cut; not a black high-collar uniform, not a sailor uniform; (2) a plain black concert suit. Same face and body in every outfit, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

## 미자 (mija) — A 선머슴 — 뻗친 숏단발

- 나이·키: 14세 · 158cm · 6등신
- 연기: 큰소리와 몸짓. 때리는 장면은 없다

### ① 턴어라운드
```
character turnaround sheet, Mija, 14-year-old Korean girl, 158cm, tall for her age, broad shoulders, choppy self-cut short bob with bangs sticking out in all directions, thick eyebrows, square jaw, an adhesive bandage across the nose, wearing a loose-fitting red cotton-knit tracksuit top with a single contrasting stripe down each sleeve, zip front, no logo, dark trousers, front view, three-quarter view, side view, back view, standing neutral pose, full body, same scale in every view, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ② 표정 시트
```
same character as the attached image: Mija, 14-year-old Korean girl, 158cm, tall for her age, broad shoulders, choppy self-cut short bob with bangs sticking out in all directions, thick eyebrows, square jaw, an adhesive bandage across the nose. Expression sheet, head and shoulders, (1) angry, frowning, (2) a slight sneer, (3) a big open smile, (4) about to cry, trembling lips, (5) serious and determined, consistent face in every panel, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ④ 15년 뒤(2003, 에필로그 3-34)
```
character turnaround sheet, Mija at 30, a Korean PE teacher, tall and broad-shouldered, short practical haircut with unruly bangs, wearing a slim-fit 2003-style navy tracksuit with side stripes, no logo, a whistle around the neck, an attendance book under the arm, front view, three-quarter view, side view, back view, standing neutral pose, full body, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ③ 의상 시트

| # | 의상 | 등장 |
|---|---|---|
| 1 | 빨간 트레이닝 상의 | 기본(일정표에 없는 씬) |
| 2 | 빨간 누빔 점퍼(겨울) | 2-14, 2-15, 2-16, 2-17 |
| 3 | 빨간 반소매 티(여름) | 3-8, 3-9, 3-10, 3-11, 3-12, 3-13, 3-14, 3-15, 3-33 |
| 4 | 새것 같은 빨간 트레이닝 위아래(제일 좋은 옷) | 2-18, 2-19 |
| 5 | 새것 같은 빨간 트레이닝 위아래·빨간 손수건(본선) | 3-16, 3-17, 3-18, 3-19, 3-20, 3-21, 3-22, 3-23, 3-24, 3-25, 3-26, 3-27, 3-28, 3-29, 3-30 |

```
same character as the attached image: Mija, 14-year-old Korean girl, 158cm, tall for her age, broad shoulders, choppy self-cut short bob with bangs sticking out in all directions, thick eyebrows, square jaw, an adhesive bandage across the nose. Outfit sheet, full body front view in each outfit: (1) a loose-fitting red cotton-knit tracksuit top with a single contrasting stripe down each sleeve, zip front, no logo, dark trousers; (2) a red quilted jacket, dark trousers; (3) a red short-sleeved T-shirt, dark trousers; (4) her best clothes: a brand-new-looking loose-fitting red cotton-knit tracksuit, top and bottom, a single contrasting stripe down the sleeves and legs, no logo; (5) her best clothes: a brand-new-looking loose-fitting red cotton-knit tracksuit, top and bottom, a single contrasting stripe down the sleeves and legs, no logo, a small red cloth neckerchief tied at the neck. Same face and body in every outfit, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

## 덕수 (deoksu) — 추천안(바이블 기준 세부 고정)

- 나이·키: 12세 · 155cm · 5.5등신
- 연기: 느리고 따뜻하다. 첼로 소리가 그의 목소리

### ① 턴어라운드
```
character turnaround sheet, Deoksu, 12-year-old Korean boy, 155cm, big and chubby, round face, short crew cut (no fade), droopy gentle eyes, shirt buttons always done up one hole off, wearing a blue plaid shirt over a stretched, slightly yellowed thin white cotton-knit sleeveless undershirt (a Korean 'running shirt', not an athletic tank top), front view, three-quarter view, side view, back view, standing neutral pose, full body, same scale in every view, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ② 표정 시트
```
same character as the attached image: Deoksu, 12-year-old Korean boy, 155cm, big and chubby, round face, short crew cut (no fade), droopy gentle eyes, shirt buttons always done up one hole off. Expression sheet, head and shoulders, (1) neutral expressionless face, (2) a faint smile, (3) surprised, eyes wide, (4) about to cry, trembling lips, consistent face in every panel, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ④ 15년 뒤(2003, 에필로그 3-34)
```
character turnaround sheet, Deoksu at 28, a big round-faced Korean man who runs the rice-soup restaurant, short crew cut, gentle eyes, wearing a flower-pattern apron over work clothes, front view, three-quarter view, side view, back view, standing neutral pose, full body, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ③ 의상 시트

| # | 의상 | 등장 |
|---|---|---|
| 1 | 늘어난 흰 러닝셔츠 위 체크 남방 | 기본(일정표에 없는 씬) |
| 2 | 체크 남방 위 회색 털스웨터(겨울) | 2-14, 2-15, 2-16, 2-17 |
| 3 | 흰 러닝셔츠·반바지(여름) | 3-8, 3-9, 3-10, 3-11, 3-12, 3-13, 3-14, 3-15, 3-33 |
| 4 | 단추를 목까지 잠근 체크 남방·빨간 손수건(본선) | 3-16, 3-17, 3-18, 3-19, 3-20, 3-21, 3-22, 3-23, 3-24, 3-25, 3-26, 3-27, 3-28, 3-29, 3-30 |

```
same character as the attached image: Deoksu, 12-year-old Korean boy, 155cm, big and chubby, round face, short crew cut (no fade), droopy gentle eyes, shirt buttons always done up one hole off. Outfit sheet, full body front view in each outfit: (1) a blue plaid shirt over a stretched, slightly yellowed thin white cotton-knit sleeveless undershirt (a Korean 'running shirt', not an athletic tank top); (2) a gray wool sweater over the plaid shirt; (3) a stretched, slightly yellowed thin white cotton-knit sleeveless undershirt (a Korean 'running shirt', not an athletic tank top) and shorts; (4) the blue plaid shirt buttoned all the way up to the neck, dark trousers, a small red cloth neckerchief tied at the neck. Same face and body in every outfit, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

## 순례 할머니 (sunrye) — 추천안(바이블 기준 세부 고정)

- 나이·키: 70대 · 148cm · 6등신
- 연기: 섬의 목소리. 툭 던지는 한마디로 장면을 정리한다

### ① 턴어라운드
```
character turnaround sheet, grandma Sunrye, Korean woman in her 70s, 148cm, small and stooped, white hair pulled back into a low traditional bun (jjok) at the nape, fixed with a single plain binyeo hairpin, deep wrinkles, usually holding a ladle, wearing baggy elastic-waist Korean work trousers (momppe) in a small floral print, wide in the leg and gathered at the ankles, and a flower-pattern apron, front view, three-quarter view, side view, back view, standing neutral pose, full body, same scale in every view, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ② 표정 시트
```
same character as the attached image: grandma Sunrye, Korean woman in her 70s, 148cm, small and stooped, white hair pulled back into a low traditional bun (jjok) at the nape, fixed with a single plain binyeo hairpin, deep wrinkles, usually holding a ladle. Expression sheet, head and shoulders, (1) a faint smile, (2) a big open smile, (3) serious and determined, consistent face in every panel, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ④ 15년 뒤(2003, 에필로그 3-34)
```
character turnaround sheet, grandma Sunrye in her 90s, even more stooped, white hair in a low bun held with a single plain binyeo hairpin, cheerful, wearing a purple going-out blouse and a long plain dark skirt, front view, three-quarter view, side view, back view, standing neutral pose, full body, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ③ 의상 시트

| # | 의상 | 등장 |
|---|---|---|
| 1 | 몸뻬 바지·꽃무늬 앞치마 | 기본(일정표에 없는 씬) |
| 2 | 솜 누빈 조끼·털목도리(겨울) | 2-14, 2-15, 2-16, 2-17 |
| 3 | 외출용 자주색 블라우스·긴 치마, 접은 앞치마를 손에(본선) | 3-16, 3-17, 3-18, 3-19, 3-20, 3-21, 3-22, 3-23, 3-24, 3-25, 3-26, 3-27, 3-28, 3-29, 3-30 |

```
same character as the attached image: grandma Sunrye, Korean woman in her 70s, 148cm, small and stooped, white hair pulled back into a low traditional bun (jjok) at the nape, fixed with a single plain binyeo hairpin, deep wrinkles, usually holding a ladle. Outfit sheet, full body front view in each outfit: (1) baggy elastic-waist Korean work trousers (momppe) in a small floral print, wide in the leg and gathered at the ankles, and a flower-pattern apron; (2) a cotton-padded quilted vest and a wool scarf over baggy elastic-waist Korean work trousers (momppe) in a small floral print, wide in the leg and gathered at the ankles; (3) her going-out clothes: a purple blouse and a long plain dark skirt, holding her folded flower-pattern apron in one hand. Same face and body in every outfit, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

## 봉구 (bonggu) — 섬 아이 단순 디자인(사용자 선택)

- 나이·키: 10세(추정) · 132cm · 5등신
- 연기: 3화 섬 아이. 악기: 깡통 바이올린 2호. 이름과 옷 색으로 구분

### ① 턴어라운드
```
character turnaround sheet, Bonggu, 10-year-old Korean boy, very short uneven clipper buzz cut (no fade), wide face, mischievous eyes, wearing a yellow cotton-knit sleeveless undershirt-style top (a Korean 'running shirt', not an athletic tank top) and shorts, front view, three-quarter view, side view, back view, standing neutral pose, full body, same scale in every view, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ② 표정 시트
```
same character as the attached image: Bonggu, 10-year-old Korean boy, very short uneven clipper buzz cut (no fade), wide face, mischievous eyes. Expression sheet, head and shoulders, (1) a big open smile, (2) surprised, eyes wide, (3) serious and determined, consistent face in every panel, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ③ 의상 시트

| # | 의상 | 등장 |
|---|---|---|
| 1 | 노란 러닝셔츠·반바지 | 기본(일정표에 없는 씬) |
| 2 | 노란 반소매 남방·반바지·빨간 손수건(본선) | — |

```
same character as the attached image: Bonggu, 10-year-old Korean boy, very short uneven clipper buzz cut (no fade), wide face, mischievous eyes. Outfit sheet, full body front view in each outfit: (1) a yellow cotton-knit sleeveless undershirt-style top (a Korean 'running shirt', not an athletic tank top) and shorts; (2) his best clothes: a yellow short-sleeved button shirt and shorts, sneakers, a small red cloth neckerchief tied at the neck. Same face and body in every outfit, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

## 영란 (yeongran) — 섬 아이 단순 디자인(사용자 선택)

- 나이·키: 11세(추정) · 138cm · 5등신
- 연기: 3화 섬 아이. 악기: 깡통 바이올린 3호. 이름과 옷 색으로 구분

### ① 턴어라운드
```
character turnaround sheet, Yeongran, 11-year-old Korean girl, hair in two low pigtails, slim face, firm little mouth, wearing a pink short-sleeved blouse and a navy skirt, front view, three-quarter view, side view, back view, standing neutral pose, full body, same scale in every view, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ② 표정 시트
```
same character as the attached image: Yeongran, 11-year-old Korean girl, hair in two low pigtails, slim face, firm little mouth. Expression sheet, head and shoulders, (1) a big open smile, (2) surprised, eyes wide, (3) serious and determined, consistent face in every panel, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ③ 의상 시트

| # | 의상 | 등장 |
|---|---|---|
| 1 | 분홍 반소매 블라우스·감색 치마 | 기본(일정표에 없는 씬) |
| 2 | 분홍 반소매 블라우스·감색 치마·빨간 손수건(본선) | — |

```
same character as the attached image: Yeongran, 11-year-old Korean girl, hair in two low pigtails, slim face, firm little mouth. Outfit sheet, full body front view in each outfit: (1) a pink short-sleeved blouse and a navy skirt; (2) a pink short-sleeved blouse and a navy skirt, a small red cloth neckerchief tied at the neck. Same face and body in every outfit, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

## 경호 (gyeongho) — 섬 아이 단순 디자인(사용자 선택)

- 나이·키: 8세(추정) · 122cm · 4.5등신
- 연기: 3화 섬 아이. 악기: 냄비 뚜껑 심벌. 이름과 옷 색으로 구분

### ① 턴어라운드
```
character turnaround sheet, Gyeongho, 8-year-old Korean boy, identical twin of Gyeongmin, bowl haircut, round face (tell the twins apart only by shirt color), wearing a blue T-shirt and shorts, front view, three-quarter view, side view, back view, standing neutral pose, full body, same scale in every view, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ② 표정 시트
```
same character as the attached image: Gyeongho, 8-year-old Korean boy, identical twin of Gyeongmin, bowl haircut, round face (tell the twins apart only by shirt color). Expression sheet, head and shoulders, (1) a big open smile, (2) surprised, eyes wide, (3) serious and determined, consistent face in every panel, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ③ 의상 시트

| # | 의상 | 등장 |
|---|---|---|
| 1 | 파란 티·반바지 | 기본(일정표에 없는 씬) |
| 2 | 파란 티·반바지·빨간 손수건(본선) | — |

```
same character as the attached image: Gyeongho, 8-year-old Korean boy, identical twin of Gyeongmin, bowl haircut, round face (tell the twins apart only by shirt color). Outfit sheet, full body front view in each outfit: (1) a blue T-shirt and shorts; (2) a blue T-shirt and shorts, a small red cloth neckerchief tied at the neck. Same face and body in every outfit, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

## 경민 (gyeongmin) — 섬 아이 단순 디자인(사용자 선택)

- 나이·키: 8세(추정) · 122cm · 4.5등신
- 연기: 3화 섬 아이. 악기: 냄비 뚜껑 심벌. 이름과 옷 색으로 구분

### ① 턴어라운드
```
character turnaround sheet, Gyeongmin, 8-year-old Korean boy, identical twin of Gyeongho, bowl haircut, round face (tell the twins apart only by shirt color), wearing an orange T-shirt and shorts, front view, three-quarter view, side view, back view, standing neutral pose, full body, same scale in every view, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ② 표정 시트
```
same character as the attached image: Gyeongmin, 8-year-old Korean boy, identical twin of Gyeongho, bowl haircut, round face (tell the twins apart only by shirt color). Expression sheet, head and shoulders, (1) a big open smile, (2) surprised, eyes wide, (3) serious and determined, consistent face in every panel, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ③ 의상 시트

| # | 의상 | 등장 |
|---|---|---|
| 1 | 주황 티·반바지 | 기본(일정표에 없는 씬) |
| 2 | 주황 티·반바지·빨간 손수건(본선) | — |

```
same character as the attached image: Gyeongmin, 8-year-old Korean boy, identical twin of Gyeongho, bowl haircut, round face (tell the twins apart only by shirt color). Outfit sheet, full body front view in each outfit: (1) an orange T-shirt and shorts; (2) an orange T-shirt and shorts, a small red cloth neckerchief tied at the neck. Same face and body in every outfit, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

## 순이 (suni) — 섬 아이 단순 디자인(사용자 선택)

- 나이·키: 9세(추정) · 126cm · 5등신
- 연기: 3화 섬 아이. 악기: 병 실로폰. 이름과 옷 색으로 구분

### ① 턴어라운드
```
character turnaround sheet, Suni, 9-year-old Korean girl, short bob with a red headband, round eyes, wearing a flower-pattern dress, front view, three-quarter view, side view, back view, standing neutral pose, full body, same scale in every view, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ② 표정 시트
```
same character as the attached image: Suni, 9-year-old Korean girl, short bob with a red headband, round eyes. Expression sheet, head and shoulders, (1) a big open smile, (2) surprised, eyes wide, (3) serious and determined, consistent face in every panel, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ③ 의상 시트

| # | 의상 | 등장 |
|---|---|---|
| 1 | 꽃무늬 원피스 | 기본(일정표에 없는 씬) |
| 2 | 꽃무늬 원피스·빨간 손수건(본선) | — |

```
same character as the attached image: Suni, 9-year-old Korean girl, short bob with a red headband, round eyes. Outfit sheet, full body front view in each outfit: (1) a flower-pattern dress; (2) a flower-pattern dress, a small red cloth neckerchief tied at the neck. Same face and body in every outfit, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

## 석이 (seoki) — 섬 아이 단순 디자인(사용자 선택)

- 나이·키: 7세(추정) · 115cm · 4.5등신
- 연기: 3화 섬 아이. 악기: 병 실로폰. 이름과 옷 색으로 구분

### ① 턴어라운드
```
character turnaround sheet, Seoki, 7-year-old Korean boy, the smallest of all, very short clipper buzz cut (no fade) under a too-big plain cotton cap with a soft brim and no logo, rosy cheeks, wearing an oversized hand-me-down short-sleeved T-shirt that covers both shoulders, the sleeves hanging past his elbows and the hem down to his thighs, a too-big plain cotton cap with a soft brim and no logo, front view, three-quarter view, side view, back view, standing neutral pose, full body, same scale in every view, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ② 표정 시트
```
same character as the attached image: Seoki, 7-year-old Korean boy, the smallest of all, very short clipper buzz cut (no fade) under a too-big plain cotton cap with a soft brim and no logo, rosy cheeks. Expression sheet, head and shoulders, (1) a big open smile, (2) surprised, eyes wide, (3) serious and determined, consistent face in every panel, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### ③ 의상 시트

| # | 의상 | 등장 |
|---|---|---|
| 1 | 물려받은 큰 반소매 티(소매가 팔꿈치 아래로)·큰 모자 | 기본(일정표에 없는 씬) |
| 2 | 물려받은 큰 반소매 티(소매가 팔꿈치 아래로)·큰 모자·빨간 손수건(본선) | — |

```
same character as the attached image: Seoki, 7-year-old Korean boy, the smallest of all, very short clipper buzz cut (no fade) under a too-big plain cotton cap with a soft brim and no logo, rosy cheeks. Outfit sheet, full body front view in each outfit: (1) an oversized hand-me-down short-sleeved T-shirt that covers both shoulders, the sleeves hanging past his elbows and the hem down to his thighs, a too-big plain cotton cap with a soft brim and no logo; (2) an oversized hand-me-down short-sleeved T-shirt that covers both shoulders, the sleeves hanging past his elbows and the hem down to his thighs, a too-big plain cotton cap with a soft brim and no logo, a small red cloth neckerchief tied at the neck. Same face and body in every outfit, plain light background, clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```
