# 배경 시안 GPT 프롬프트 — 깡통 바이올린

1. 장소마다 ① 기준 배경을 먼저 만들어 `renders/sets/<set_id>.png`로 저장한다(변형은 `renders/sets/<set_id>__<시간>.png`).
2. 컷을 생성할 때 그 장소의 기준 배경(시간대가 맞으면 변형)을 참고 이미지로 함께 올리고, 컷 프롬프트에 '같은 배치 유지(same layout as the reference)'를 붙인다.
3. 배치·근거·카메라 자리는 `design/sets.md`, 기계용 원본은 `design/sets.json`. 이 문서는 `python tools/sets.py`로 만든다(직접 고치지 말 것).

### [junk_shop_in] 곽 영감 고물상 — 안 — 1-3, 1-9, 1-12, 1-13, 2-13, 2-28, 3-1

- 8절: 곽 영감 고물상 (안·앞) · 크기: 7×5 (안쪽 높이 처마 2.2m, 뒤 2.6m)
- 카메라 자리: front_wide: 마당에서 열린 전면 안쪽으로 와이드(북향). 작업대 오른쪽, 공방 문 뒤 왼쪽 / bench_reverse: 작업대 안쪽 끝(북)에서 열린 전면 쪽으로(남향). 작업대에 앉은 영감의 왼쪽 옆얼굴, 그 너머 문간이 밝게(역광), 문간에 선 사람 / east_wall_west: 동쪽 벽(선반) 쪽에서 서쪽을 보며 작업대 너머 영감 정면. 열린 전면은 화면 왼쪽(측광) / shelf_pov: 작업대 옆 서쪽에서 작업대 너머 동쪽 벽 선반으로(은주 시선) / exit_back: 안쪽에서 나가는 아이들 등 뒤(남향), 열린 전면 너머 마당

① 기준 배경 (`afternoon`) → `renders/sets/junk_shop_in.png`

```
old Kwak's junk shop at the island entrance: a corrugated-iron shed, sorted piles of scrap copper, brass and aluminum, a platform scale with a round dial, wooden apple crates by the door. Seen from the wide-open front looking in (facing north): a shed about 7 m wide and 5 m deep with a beaten-earth floor and a low corrugated-iron roof on wooden posts; the middle 4 m of the front is open, its two corrugated-iron sliding door leaves pushed aside behind short solid wall sections at both ends, a small four-pane window in the left wall section; along the right (east) wall a long scarred wooden workbench with a low stool on its left (west) side, so the worker sits facing the right wall with his back to the left; a plank shelf on the right wall above the workbench, a paper wall calendar at the back end of that shelf; the hanging scale, a round-dial spring scale with a hook, hangs from the front roof beam at the near end of the workbench; wooden apple crates stacked just inside the opening at the left jamb; on the left (west) side burlap sacks of scrap and sorted piles of scrap copper, brass and aluminum in wooden bins; in the back wall, left of center, a plank door to the small workshop, and through it the foot of the attic ladder; tiered scrap piles along the back wall to the right of that door. Lighting: 1987 spring afternoon, the interior in shade, low sunlight entering through the open front from behind the viewer on the left (southwest) and falling across the floor onto the right-wall shelf, dust in the light, key color #8A6A4A, cel shadows #4E3B2C. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`night`) → `renders/sets/junk_shop_in__night.png` — 같은 배치, 빛만 다름

```
old Kwak's junk shop at the island entrance: a corrugated-iron shed, sorted piles of scrap copper, brass and aluminum, a platform scale with a round dial, wooden apple crates by the door. Seen from the wide-open front looking in (facing north): a shed about 7 m wide and 5 m deep with a beaten-earth floor and a low corrugated-iron roof on wooden posts; the middle 4 m of the front is open, its two corrugated-iron sliding door leaves pushed aside behind short solid wall sections at both ends, a small four-pane window in the left wall section; along the right (east) wall a long scarred wooden workbench with a low stool on its left (west) side, so the worker sits facing the right wall with his back to the left; a plank shelf on the right wall above the workbench, a paper wall calendar at the back end of that shelf; the hanging scale, a round-dial spring scale with a hook, hangs from the front roof beam at the near end of the workbench; wooden apple crates stacked just inside the opening at the left jamb; on the left (west) side burlap sacks of scrap and sorted piles of scrap copper, brass and aluminum in wooden bins; in the back wall, left of center, a plank door to the small workshop, and through it the foot of the attic ladder; tiered scrap piles along the back wall to the right of that door. Lighting: night, the sliding doors closed, a single bare yellow incandescent bulb hanging above the workbench, a warm pool of light on the bench, the rest in navy darkness, key color #E8C46A, cel shadows #2A3352. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

③ 변형 (`midday_may`) → `renders/sets/junk_shop_in__midday_may.png` — 같은 배치, 빛만 다름

```
old Kwak's junk shop at the island entrance: a corrugated-iron shed, sorted piles of scrap copper, brass and aluminum, a platform scale with a round dial, wooden apple crates by the door. Seen from the wide-open front looking in (facing north): a shed about 7 m wide and 5 m deep with a beaten-earth floor and a low corrugated-iron roof on wooden posts; the middle 4 m of the front is open, its two corrugated-iron sliding door leaves pushed aside behind short solid wall sections at both ends, a small four-pane window in the left wall section; along the right (east) wall a long scarred wooden workbench with a low stool on its left (west) side, so the worker sits facing the right wall with his back to the left; a plank shelf on the right wall above the workbench, a paper wall calendar at the back end of that shelf; the hanging scale, a round-dial spring scale with a hook, hangs from the front roof beam at the near end of the workbench; wooden apple crates stacked just inside the opening at the left jamb; on the left (west) side burlap sacks of scrap and sorted piles of scrap copper, brass and aluminum in wooden bins; in the back wall, left of center, a plank door to the small workshop, and through it the foot of the attic ladder; tiered scrap piles along the back wall to the right of that door. Lighting: 1988 May midday, bright high sun from the front-left, glints on the scrap metal, the interior shade softer, key color #F4D9A0, cel shadows #7A5E44. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [junk_shop_front] 곽 영감 고물상 — 앞(외경) — 1-3, 1-8, 1-9, 1-10, 1-12, 1-13, 2-6, 2-28, 3-1

- 8절: 곽 영감 고물상 (안·앞) · 크기: 창고 7×5, 앞마당 약 20×14(섬 어귀 마당)
- 카메라 자리: yard_front: 마당(둑길 끝)에서 고물상 전면으로(북향) 외경 / from_tent: 천막 동쪽 옆자락 안에서 고물상 열린 전면을 비스듬히(북동향) — 작업대의 영감 등 / village_south: 마을 쪽(북)에서 고물상 지붕 너머 둑길 쪽(남향) — 아침 해가 지붕 왼쪽(동)에서

① 기준 배경 (`afternoon`) → `renders/sets/junk_shop_front.png`

```
old Kwak's junk shop at the island entrance: a corrugated-iron shed, sorted piles of scrap copper, brass and aluminum, a platform scale with a round dial, wooden apple crates by the door. Seen from the muddy yard in front, facing north: the low corrugated-iron shed about 7 m wide, its middle 4 m wide front open under the eave, short wall sections at both ends with a small four-pane window in the left section; tiered scrap piles stacked against the front wall sections on both sides of the opening; wooden apple crates at the left jamb; the round-dial hanging scale under the eave at the right end of the opening; inside on the right a workbench against the right (east) wall; behind the shed a lower plank workshop roof with a short stovepipe; on the far left edge of the frame, 3 m away and standing 2 m further forward, the side of grandma Sunrye's patched canvas tent with its side flap rolled up; far behind on the right the big flat-topped hill of trash; tire ruts and puddles in the foreground. Lighting: 1987 spring afternoon, low sunlight from the left (southwest) raking across the shed front, shade under the eave, hazy beige sky, key color #C9A66B, cel shadows #6E5640. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`night`) → `renders/sets/junk_shop_front__night.png` — 같은 배치, 빛만 다름

```
old Kwak's junk shop at the island entrance: a corrugated-iron shed, sorted piles of scrap copper, brass and aluminum, a platform scale with a round dial, wooden apple crates by the door. Seen from the muddy yard in front, facing north: the low corrugated-iron shed about 7 m wide, its middle 4 m wide front open under the eave, short wall sections at both ends with a small four-pane window in the left section; tiered scrap piles stacked against the front wall sections on both sides of the opening; wooden apple crates at the left jamb; the round-dial hanging scale under the eave at the right end of the opening; inside on the right a workbench against the right (east) wall; behind the shed a lower plank workshop roof with a short stovepipe; on the far left edge of the frame, 3 m away and standing 2 m further forward, the side of grandma Sunrye's patched canvas tent with its side flap rolled up; far behind on the right the big flat-topped hill of trash; tire ruts and puddles in the foreground. Lighting: deep night, the sliding doors closed, a thin strip of yellow incandescent light leaking from the small window and the door gap, faint yellow through gaps in the corrugated roof, everything else dark navy, stars over the hill, key color #E8C46A, cel shadows #2A3352. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [workshop] 공방(고물상 뒤) — 2-13, 2-14, 2-17, 2-22, 3-5, 3-6, 3-8, 3-9, 3-10, 3-11, 3-15, 3-18

- 8절: 공방 · 크기: 5×3.5 (천장 2.1m, 위는 다락)
- 카메라 자리: door_wide: 문(남)에서 안쪽으로 와이드(북향). 작업대 정면 안쪽, 창 왼쪽, 선반 오른쪽 / bench_reverse: 작업대 쪽에서 문 쪽으로(남향). 문가에 선 사람 역광, 문틈, 사다리 / kwak_back: 문 쪽에서 작업대에 앉은 사람의 등(북향, 가까이) / bench_top: 작업대 위 부감 / plank_gap: 서쪽 판자 틈에서 강 쪽으로(서향)

① 기준 배경 (`summer_afternoon`) → `renders/sets/workshop.png`

```
the small workshop behind old Kwak's junk shop: a wooden workbench, hand tools on the wall, wood shavings, instruments made from scrap hanging on nails, a ladder up to a small attic above the workshop. Seen from its doorway looking in (facing north): a cramped room about 5 m wide and 3.5 m deep with rough plank walls showing thin gaps of light, a low plank ceiling with a small square hatch to the attic, a raised plank floor one step above the doorway, wood shavings and sawdust on the floor; across the back wall a long wooden workbench with a shallow drawer, a rack of hand tools (saws, chisels, files, clamps, a coping saw) on the back wall above it, a single bare bulb on a cord over the bench; one small window in the left (west) wall, a bare nail in the wall beside it; plank shelves along the right (east) wall crowded with tin cans, can bodies, wooden spoons and instrument parts, scrap instruments hanging on nails above them; a square of bricks in the middle of the floor for a coal-briquette stove; to the right of the doorway a wooden ladder leaning up to the ceiling hatch; burlap scrap sacks in the near right corner. Lighting: 1988 early summer afternoon, slanted sunlight through the small window on the left (west), sawdust floating in the beams, warm shade, key color #D8B57A, cel shadows #6E5640. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`night`) → `renders/sets/workshop__night.png` — 같은 배치, 빛만 다름

```
the small workshop behind old Kwak's junk shop: a wooden workbench, hand tools on the wall, wood shavings, instruments made from scrap hanging on nails, a ladder up to a small attic above the workshop. Seen from its doorway looking in (facing north): a cramped room about 5 m wide and 3.5 m deep with rough plank walls showing thin gaps of light, a low plank ceiling with a small square hatch to the attic, a raised plank floor one step above the doorway, wood shavings and sawdust on the floor; across the back wall a long wooden workbench with a shallow drawer, a rack of hand tools (saws, chisels, files, clamps, a coping saw) on the back wall above it, a single bare bulb on a cord over the bench; one small window in the left (west) wall, a bare nail in the wall beside it; plank shelves along the right (east) wall crowded with tin cans, can bodies, wooden spoons and instrument parts, scrap instruments hanging on nails above them; a square of bricks in the middle of the floor for a coal-briquette stove; to the right of the doorway a wooden ladder leaning up to the ceiling hatch; burlap scrap sacks in the near right corner. Lighting: night, a single bare incandescent bulb over the workbench making a small pool of light, the rest in navy darkness, dust and sawdust floating in the light, key color #F2C14E, cel shadows #4A3626. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

③ 변형 (`winter_day`) → `renders/sets/workshop__winter_day.png` — 같은 배치, 빛만 다름

```
the small workshop behind old Kwak's junk shop: a wooden workbench, hand tools on the wall, wood shavings, instruments made from scrap hanging on nails, a ladder up to a small attic above the workshop. Seen from its doorway looking in (facing north): a cramped room about 5 m wide and 3.5 m deep with rough plank walls showing thin gaps of light, a low plank ceiling with a small square hatch to the attic, a raised plank floor one step above the doorway, wood shavings and sawdust on the floor; across the back wall a long wooden workbench with a shallow drawer, a rack of hand tools (saws, chisels, files, clamps, a coping saw) on the back wall above it, a single bare bulb on a cord over the bench; one small window in the left (west) wall, a bare nail in the wall beside it; plank shelves along the right (east) wall crowded with tin cans, can bodies, wooden spoons and instrument parts, scrap instruments hanging on nails above them; a square of bricks in the middle of the floor for a coal-briquette stove; to the right of the doorway a wooden ladder leaning up to the ceiling hatch; burlap scrap sacks in the near right corner. Lighting: 1987-88 winter daytime, cold pale daylight through the gaps between the planks, a coal-briquette stove on the brick square glowing orange in the middle, visible breath, key color #B8C6D0, cel shadows #3E4E66. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [soup_tent_in] 국밥집 천막 — 안 — 1-8, 1-14, 2-1, 2-2, 2-10, 2-15, 2-20, 2-21, 3-6

- 8절: 국밥집 천막 (안·앞·뒤) · 크기: 5×8 (가운데 높이 약 2.6m, 가장자리 1.8m)
- 카메라 자리: entrance_wide: 앞자락(남)에서 안쪽으로 와이드(북향). 국솥 정면 안쪽, 기둥 가운데, 걷힌 옆자락 오른쪽 / pot_reverse: 국솥 쪽에서 앞자락 쪽으로(남향). 문간에 선 사람, 빈 입구 / side_to_shop: 동쪽 평상 끝에서 걷힌 옆자락 너머 고물상으로(동향). 아이들 뒤통수 너머 영감의 등 / band_front: 서쪽 평상에서 가운데 바닥의 연주자들 정면(동향). 뒤로 동쪽 평상과 옆자락 / bench_end: 동쪽 평상 남쪽 끝(평상 끝) 가까이: 국밥 그릇·접힌 신문

① 기준 배경 (`afternoon`) → `renders/sets/soup_tent_in.png`

```
grandma Sunrye's rice-soup tent at the island entrance: a patched canvas tent, a huge iron soup pot on a coal fire, low wooden sitting platforms (pyeongsang) with long low tables on them, a ladle. Seen from the front entrance flap looking in (facing north): a long tent about 5 m wide and 8 m deep on a beaten-earth floor, patched beige and khaki canvas on a wooden pole frame, one tall wooden center pole halfway in with a bare bulb on a cord and a paper calendar nailed to it; at the far back the huge iron soup pot steaming on a brick coal fire with a small worktable and stacked bowls beside it, and to the right of the pot a rear flap that can be tied open; the benches are wide low wooden platforms (pyeongsang) with long low tables on them: two along the left (west) side and one long one along the right (east) side; the right side wall flap is rolled up, showing the corrugated-iron junk shop 3 m away; an open earth floor down the middle in front of the platforms. Lighting: 1987 afternoon, soft diffuse light through the canvas, steam from the pot blurring the back, the open right side brighter, key color #D9822B, cel shadows #6E5640. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`rain`) → `renders/sets/soup_tent_in__rain.png` — 같은 배치, 빛만 다름

```
grandma Sunrye's rice-soup tent at the island entrance: a patched canvas tent, a huge iron soup pot on a coal fire, low wooden sitting platforms (pyeongsang) with long low tables on them, a ladle. Seen from the front entrance flap looking in (facing north): a long tent about 5 m wide and 8 m deep on a beaten-earth floor, patched beige and khaki canvas on a wooden pole frame, one tall wooden center pole halfway in with a bare bulb on a cord and a paper calendar nailed to it; at the far back the huge iron soup pot steaming on a brick coal fire with a small worktable and stacked bowls beside it, and to the right of the pot a rear flap that can be tied open; the benches are wide low wooden platforms (pyeongsang) with long low tables on them: two along the left (west) side and one long one along the right (east) side; the right side wall flap is rolled up, showing the corrugated-iron junk shop 3 m away; an open earth floor down the middle in front of the platforms. Lighting: 1987 late November gray midday, rain drumming on the wet sagging canvas, dull diffuse light, weak shadows, the flaps lowered, key color #4A4F57, cel shadows #2E3850. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

③ 변형 (`winter_evening`) → `renders/sets/soup_tent_in__winter_evening.png` — 같은 배치, 빛만 다름

```
grandma Sunrye's rice-soup tent at the island entrance: a patched canvas tent, a huge iron soup pot on a coal fire, low wooden sitting platforms (pyeongsang) with long low tables on them, a ladle. Seen from the front entrance flap looking in (facing north): a long tent about 5 m wide and 8 m deep on a beaten-earth floor, patched beige and khaki canvas on a wooden pole frame, one tall wooden center pole halfway in with a bare bulb on a cord and a paper calendar nailed to it; at the far back the huge iron soup pot steaming on a brick coal fire with a small worktable and stacked bowls beside it, and to the right of the pot a rear flap that can be tied open; the benches are wide low wooden platforms (pyeongsang) with long low tables on them: two along the left (west) side and one long one along the right (east) side; the right side wall flap is rolled up, showing the corrugated-iron junk shop 3 m away; an open earth floor down the middle in front of the platforms. Lighting: 1988 January evening, a coal-briquette stove with a hissing kettle beside the center pole glowing orange, the bulb lit, white breath, the tent crowded, key color #9DB7C9, cel shadows #3E4E66. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [soup_tent_front] 국밥집 천막 — 앞 — 1-7, 1-9, 2-6, 2-10, 3-14

- 8절: 국밥집 천막 (안·앞·뒤) · 크기: 천막 5×8, 앞 마당 쪽 약 8×6
- 카메라 자리: yard_north: 마당에서 천막 앞으로 와이드(북향). 고물상은 오른쪽 / front_east: 천막 앞에서 동쪽 고물상 함석지붕을 올려다봄(동향). 해는 등 뒤 오른쪽 / low_mud: 진흙 위 구두에서 틸트 업(낮게)

① 기준 배경 (`autumn_afternoon`) → `renders/sets/soup_tent_front.png`

```
grandma Sunrye's rice-soup tent at the island entrance: a patched canvas tent, a huge iron soup pot on a coal fire, low wooden sitting platforms (pyeongsang) with long low tables on them, a ladle. Seen from the muddy yard in front, facing north: the front of the long patched beige and khaki canvas tent with its front flap tied half open and a wooden front pole at the entrance, steam drifting out from the dark interior where the soup pot sits at the far back; the tent's right (east) side flap rolled up; 3 m to the right and set 2 m further back, the corrugated-iron junk shop with its open front and tiered scrap piles; behind the tent, the low roofs of the shack village and the slope of the small trash hill on the left; puddles and tire ruts on the bare earth yard in the foreground. Lighting: 1987 autumn afternoon, clear cool light from the left (southwest), gray tones with a strip of clear sky above the corrugated roof, puddles reflecting the sky, key color #8C8F94, cel shadows #4A5060. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`july_noon`) → `renders/sets/soup_tent_front__july_noon.png` — 같은 배치, 빛만 다름

```
grandma Sunrye's rice-soup tent at the island entrance: a patched canvas tent, a huge iron soup pot on a coal fire, low wooden sitting platforms (pyeongsang) with long low tables on them, a ladle. Seen from the muddy yard in front, facing north: the front of the long patched beige and khaki canvas tent with its front flap tied half open and a wooden front pole at the entrance, steam drifting out from the dark interior where the soup pot sits at the far back; the tent's right (east) side flap rolled up; 3 m to the right and set 2 m further back, the corrugated-iron junk shop with its open front and tiered scrap piles; behind the tent, the low roofs of the shack village and the slope of the small trash hill on the left; puddles and tire ruts on the bare earth yard in the foreground. Lighting: 1988 July midday, the sun almost overhead, very short shadows in front of the tent, bright dusty yard, key color #E3D6BE, cel shadows #6E5640. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [soup_tent_back] 국밥집 천막 — 뒤 쓰레기 더미 — 2-10, 2-11, 2-12, 2-14

- 8절: 국밥집 천막 뒤 쓰레기 더미 · 크기: 더미 약 4×3, 높이 2m
- 카메라 자리: path_south: 마을 흙길에서 천막 뒤와 더미(남향) / rear_flap: 천막 안 국솥 옆 뒷자락 너머 빗속의 더미(북향, 2-10) / far_window: 은주네 쪽방 창에서 본 먼 더미 위 불빛 둘(롱, 남동향)

① 기준 배경 (`overcast`) → `renders/sets/soup_tent_back.png`

```
grandma Sunrye's rice-soup tent at the island entrance: a patched canvas tent, a huge iron soup pot on a coal fire, low wooden sitting platforms (pyeongsang) with long low tables on them, a ladle, behind the tent, a mound of wet trash waiting for the collection yard: tangled plastic sheets, tin cans and broken wood. Seen from the dirt path on the village side, facing south: the back of the patched canvas tent with its rear flap, and right beside it on the left of the path a mound about 2 m high and 4 m wide of tangled wet plastic sheets, tin cans and broken wood; the narrow dirt path to the shack village runs past the mound toward the viewer; beyond the tent on the left, the corrugated-iron roof of the junk shop; the embankment road and reeds far behind. Lighting: overcast daytime, flat gray light, wet trash glistening dully, key color #9A8E7E, cel shadows #4E4438. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`night`) → `renders/sets/soup_tent_back__night.png` — 같은 배치, 빛만 다름

```
grandma Sunrye's rice-soup tent at the island entrance: a patched canvas tent, a huge iron soup pot on a coal fire, low wooden sitting platforms (pyeongsang) with long low tables on them, a ladle, behind the tent, a mound of wet trash waiting for the collection yard: tangled plastic sheets, tin cans and broken wood. Seen from the dirt path on the village side, facing south: the back of the patched canvas tent with its rear flap, and right beside it on the left of the path a mound about 2 m high and 4 m wide of tangled wet plastic sheets, tin cans and broken wood; the narrow dirt path to the shack village runs past the mound toward the viewer; beyond the tent on the left, the corrugated-iron roof of the junk shop; the embankment road and reeds far behind. Lighting: night, darkness, only two small flashlight beams, one sweeping over the mound and one held still at the children's feet, the river faintly heard, key color #2E3550, cel shadows #1E2538. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [shack_main] 은주네 판잣집 — 부엌 겸 방 — 1-4, 2-14, 2-24, 2-26, 3-2, 3-3

- 8절: 은주네 판잣집, 부엌 겸 방 · 크기: 3.0×3.0 (흙바닥 부엌 칸 0.9m + 방 2.1m), 천장 1.9m
- 카메라 자리: door_wide: 현관문 안에서 방 안쪽으로(북향). 작은 창·곤로 왼쪽, 합판 벽·쪽방 문 오른쪽 안 / table_front: 방 안쪽(북쪽)에서 밥상 정면, 뒤로 현관문(남향). 세 사람 밥상 정면 / section: 합판 벽을 가운데 두고 두 칸을 단면처럼 한 화면(남쪽 벽을 걷어낸 단면, 북향). 왼쪽 부엌 겸 방, 오른쪽 쪽방 / door_close: 현관문 안쪽 문고리·목수건·못의 손전등 가까이

① 기준 배경 (`evening`) → `renders/sets/shack_main.png`

```
inside a small 1980s shack: plywood and tar-paper walls, a low ceiling, a coal-briquette stove, a kerosene burner, a folding low table, a tiny window. Seen from just inside the front door looking in (facing north): a room about 3 m by 3 m under a low ceiling of boards; the first 0.9 m inside the door is a sunken strip of beaten earth running the width of the room, where rubber boots stand; in the middle of that strip a coal-briquette stove set into the riser of the raised floor, with a kettle on its lid; at the left (west) end of the strip, a kerosene burner on a low wooden stand right under the tiny window in the left wall; the rest of the room is a raised heated floor one step up; a single bare bulb hangs from the center of the ceiling over a folding low table; along the back wall folded quilts piled on a low wooden chest and clothes hanging on nails; the right (east) wall is a thin plywood partition with a small plank door at its far (back) end leading to the tiny side room; on the near right, beside the front door, a canvas tool sack leaning on the wall and a flashlight hanging on a nail by the door frame. Lighting: 1987 spring evening, a single bare incandescent bulb and the small flame of the kerosene burner, a thin wisp of briquette smoke at the door crack, navy dusk at the tiny window, key color #3E4A6A, cel shadows #2A2F45. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`night_bulb`) → `renders/sets/shack_main__night_bulb.png` — 같은 배치, 빛만 다름

```
inside a small 1980s shack: plywood and tar-paper walls, a low ceiling, a coal-briquette stove, a kerosene burner, a folding low table, a tiny window. Seen from just inside the front door looking in (facing north): a room about 3 m by 3 m under a low ceiling of boards; the first 0.9 m inside the door is a sunken strip of beaten earth running the width of the room, where rubber boots stand; in the middle of that strip a coal-briquette stove set into the riser of the raised floor, with a kettle on its lid; at the left (west) end of the strip, a kerosene burner on a low wooden stand right under the tiny window in the left wall; the rest of the room is a raised heated floor one step up; a single bare bulb hangs from the center of the ceiling over a folding low table; along the back wall folded quilts piled on a low wooden chest and clothes hanging on nails; the right (east) wall is a thin plywood partition with a small plank door at its far (back) end leading to the tiny side room; on the near right, beside the front door, a canvas tool sack leaning on the wall and a flashlight hanging on a nail by the door frame. Lighting: night, the burner off, one bare bulb at the center of the ceiling making a warm yellow pool over the low table, the corners in navy shade, key color #C89B6D, cel shadows #4A3A30. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

③ 변형 (`midnight`) → `renders/sets/shack_main__midnight.png` — 같은 배치, 빛만 다름

```
inside a small 1980s shack: plywood and tar-paper walls, a low ceiling, a coal-briquette stove, a kerosene burner, a folding low table, a tiny window. Seen from just inside the front door looking in (facing north): a room about 3 m by 3 m under a low ceiling of boards; the first 0.9 m inside the door is a sunken strip of beaten earth running the width of the room, where rubber boots stand; in the middle of that strip a coal-briquette stove set into the riser of the raised floor, with a kettle on its lid; at the left (west) end of the strip, a kerosene burner on a low wooden stand right under the tiny window in the left wall; the rest of the room is a raised heated floor one step up; a single bare bulb hangs from the center of the ceiling over a folding low table; along the back wall folded quilts piled on a low wooden chest and clothes hanging on nails; the right (east) wall is a thin plywood partition with a small plank door at its far (back) end leading to the tiny side room; on the near right, beside the front door, a canvas tool sack leaning on the wall and a flashlight hanging on a nail by the door frame. Lighting: after midnight, almost dark, only faint navy night light from the tiny window, key color #1A2238, cel shadows #232C4A. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [shack_side] 은주네 판잣집 — 쪽방 — 1-5, 1-10, 2-11, 2-25, 2-29, 3-3, 3-7, 3-19, 3-34

- 8절: 은주네 판잣집, 쪽방 · 크기: 1.5×3.0, 천장 1.9m
- 카메라 자리: top_down: 위에서 내려다보며: 이불 위 은주와 무릎, 머리맡 선반 / door_south: 쪽방 문에서 방 끝 작은 창 쪽으로(남향). 합판 벽 오른쪽, 선반 왼쪽 안 / window_from_mat: 이불에 누운 높이에서 작은 창(창틀 안 먼 불빛 둘) / wall_close: 합판 벽과 손가락 마디 극접사(톡톡) / section: 두 칸 단면(shack_main의 section과 같은 그림)

① 기준 배경 (`night_bulb`) → `renders/sets/shack_side.png`

```
Eunju's tiny side room in the shack: a thin wall shared with the next room, a sleeping mat, a shelf with an old broken transistor radio box. Seen from its small plank door at the back end of the room, looking along its length (facing south): a narrow room about 1.5 m wide and 3 m long under a low board ceiling; the right wall is the thin plywood partition shared with the next room, and a thin sleeping mat with a quilt lies along it with the pillow end at the far end; at the far end, in the end wall, one tiny window about 40 cm square; on the left wall near the far end, at shoulder height, a narrow plank shelf holding a small wooden box (the radio box); a single bare bulb hangs from the middle of the ceiling; bare plywood and tar-paper on the left outer wall; almost no other furniture. Lighting: night, one bare incandescent bulb from above, warm small light, glints on small metal things, the window black-navy, key color #24304F, cel shadows #1E2740. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`dark`) → `renders/sets/shack_side__dark.png` — 같은 배치, 빛만 다름

```
Eunju's tiny side room in the shack: a thin wall shared with the next room, a sleeping mat, a shelf with an old broken transistor radio box. Seen from its small plank door at the back end of the room, looking along its length (facing south): a narrow room about 1.5 m wide and 3 m long under a low board ceiling; the right wall is the thin plywood partition shared with the next room, and a thin sleeping mat with a quilt lies along it with the pillow end at the far end; at the far end, in the end wall, one tiny window about 40 cm square; on the left wall near the far end, at shoulder height, a narrow plank shelf holding a small wooden box (the radio box); a single bare bulb hangs from the middle of the ceiling; bare plywood and tar-paper on the left outer wall; almost no other furniture. Lighting: night with the light off, almost dark, a faint navy night glow through the tiny window, key color #24304F, cel shadows #1A2238. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [small_hill_top] 작은 산 꼭대기 — 1-11, 1-13, 2-1, 2-23, 2-27, 3-4, 3-6, 3-20, 3-21, 3-25

- 8절: 작은 산 (중턱·꼭대기) · 크기: 꼭대기 평지 약 60×40 (높이는 1987년 미확인, 큰 산보다 낮게)
- 카메라 자리: top_south: 꼭대기 가운데에서 남쪽(판자·마을·둑길·뭍)으로 와이드 / slope_up: 남쪽 비탈 아래에서 꼭대기 가장자리로 올려다봄(북향). 오르는 사람 등 너머 아이들 얼굴 / board_close: 꼭대기 판자 위(동그리 자리) 가까이·극접사 / sky_low: 하늘을 등진 앙각(미자, 비닐)

① 기준 배경 (`noon`) → `renders/sets/small_hill_top.png`

```
on the small flat-topped hill of trash: terraced slope of compacted ochre soil mixed with scrap metal, broken boards, white plastic sheets and tin cans, a dump-truck ramp cut into the slope, the Han River and the 1980s city skyline far behind. Seen from the middle of the flat top looking south: a wide flat summit of compacted ochre and gray-brown soil studded with scrap and torn white plastic that flutters in the wind; near the south edge of the summit a single flat wooden board lying on the ground, the spot where the first sound was played; beyond the edge the terraced slope drops toward the shack village roofs at its foot, the narrow embankment road running south across reeds and water to the mainland, and the hazy 1980s city skyline far behind; on the left (east), past the dump-truck ramp that zigzags down the east slope, the bigger flat-topped trash hill, taller and wider; on the right (west) the open Han River. Lighting: 1988 early summer midday, strong overhead sun, short shadows, hazy beige sky, plastic sheets flapping in a strong breeze, key color #6FB3A8, cel shadows #5A4A3C. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`golden_sunset`) → `renders/sets/small_hill_top__golden_sunset.png` — 같은 배치, 빛만 다름

```
on the small flat-topped hill of trash: terraced slope of compacted ochre soil mixed with scrap metal, broken boards, white plastic sheets and tin cans, a dump-truck ramp cut into the slope, the Han River and the 1980s city skyline far behind. Seen from the middle of the flat top looking south: a wide flat summit of compacted ochre and gray-brown soil studded with scrap and torn white plastic that flutters in the wind; near the south edge of the summit a single flat wooden board lying on the ground, the spot where the first sound was played; beyond the edge the terraced slope drops toward the shack village roofs at its foot, the narrow embankment road running south across reeds and water to the mainland, and the hazy 1980s city skyline far behind; on the left (east), past the dump-truck ramp that zigzags down the east slope, the bigger flat-topped trash hill, taller and wider; on the right (west) the open Han River. Lighting: 1987 April evening, low sunset backlight from the right (west) across the river, long shadows, the whole trash hill glowing gold, key color #F2C14E, cel shadows #6E5640. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

③ 변형 (`dawn`) → `renders/sets/small_hill_top__dawn.png` — 같은 배치, 빛만 다름

```
on the small flat-topped hill of trash: terraced slope of compacted ochre soil mixed with scrap metal, broken boards, white plastic sheets and tin cans, a dump-truck ramp cut into the slope, the Han River and the 1980s city skyline far behind. Seen from the middle of the flat top looking south: a wide flat summit of compacted ochre and gray-brown soil studded with scrap and torn white plastic that flutters in the wind; near the south edge of the summit a single flat wooden board lying on the ground, the spot where the first sound was played; beyond the edge the terraced slope drops toward the shack village roofs at its foot, the narrow embankment road running south across reeds and water to the mainland, and the hazy 1980s city skyline far behind; on the left (east), past the dump-truck ramp that zigzags down the east slope, the bigger flat-topped trash hill, taller and wider; on the right (west) the open Han River. Lighting: before sunrise, blue-gray diffuse light, only the eastern horizon behind the big hill faintly bright, almost no shadows, two truck headlights far away on the embankment road, key color #5E7F99, cel shadows #34465E. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [small_hill_slope] 작은 산 중턱 — 1-1, 1-17, 2-1, 2-27

- 8절: 작은 산 (중턱·꼭대기) · 크기: 남쪽 비탈 중턱(층진 단 폭 약 5~8m)
- 카메라 자리: slope_down_se: 중턱 단에서 남동쪽 아래로 롱숏: 큰 산 아래 하역, 둑길 / slope_wide: 비탈 전체 와이드(사람들이 일어서는 비탈) / slope_from_below_night: 비탈 아래에서 올라가는 작은 불빛 하나(롱, 북향)

① 기준 배경 (`foggy_dawn`) → `renders/sets/small_hill_slope.png`

```
on the small flat-topped hill of trash: terraced slope of compacted ochre soil mixed with scrap metal, broken boards, white plastic sheets and tin cans, a dump-truck ramp cut into the slope, the Han River and the 1980s city skyline far behind. Seen from halfway up the south slope, on one of its wide terraces, looking southeast and down: the terraces step down like giant stairs of packed ochre and gray-brown trash; below, the low shack roofs of the village at the island entrance and the narrow embankment road running south through the reeds; on the left, at the foot of the bigger flat-topped hill, a dump truck tipping its load onto a heap; the ramp road climbing the slope beside the terraces. Lighting: 1987 early April before dawn, thick fog, the big hill and the embankment road half-hidden in mist, cool blue-gray diffuse light with almost no shadows, key color #5E7F99, cel shadows #34465E. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`first_sun`) → `renders/sets/small_hill_slope__first_sun.png` — 같은 배치, 빛만 다름

```
on the small flat-topped hill of trash: terraced slope of compacted ochre soil mixed with scrap metal, broken boards, white plastic sheets and tin cans, a dump-truck ramp cut into the slope, the Han River and the 1980s city skyline far behind. Seen from halfway up the south slope, on one of its wide terraces, looking southeast and down: the terraces step down like giant stairs of packed ochre and gray-brown trash; below, the low shack roofs of the village at the island entrance and the narrow embankment road running south through the reeds; on the left, at the foot of the bigger flat-topped hill, a dump truck tipping its load onto a heap; the ramp road climbing the slope beside the terraces. Lighting: the first sunlight breaking over the big hill from the left (east) through the thinning fog, key color #F2C98A, cel shadows #34465E. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [dyke_road] 둑길·섬 어귀 — 섬 쪽에서 뭍을 봄 — 1-1, 1-7, 1-16, 2-1, 2-5, 2-7, 2-14, 2-16, 3-32

- 8절: 둑길·섬 어귀 · 크기: 둑 위 길폭 약 5, 길이 약 400, 둑 높이 약 3
- 카메라 자리: island_end_south: 섬 쪽 끝에서 뭍 쪽으로(남향) 고정. 멀리 다가오는 사람 / bank_side: 둑 비탈에 줄지어 앉은 아이들 너머 둑길(옆에서, 동향 또는 서향) / middle_wide: 둑길 한가운데 작아지는 사람, 와이드(남향) / low_shoes: 진흙 바퀴 자국 위 구두·장화(낮게)

① 기준 배경 (`autumn_afternoon`) → `renders/sets/dyke_road.png`

```
the narrow earthen embankment road leading into the island, reeds on both sides, a cluster of shacks at the island entrance. Seen from the bare earth yard at the island end, looking south across the yard to the start of the road and on toward the mainland: on the near left a plywood notice board on two posts at the road's left shoulder; from there the narrow dirt road, about 5 m wide, runs straight away on top of a raised earth embankment about 3 m high, its surface rutted by truck tires with muddy water in the ruts; grassy earth banks slope down on both sides into tall reeds and shallow water; far away at the end of the road the low houses of the mainland and a hazy 1980s city skyline. Lighting: 1987 autumn afternoon, cool clear light from the right (west), long shadows of reeds across the road, key color #8C8F94, cel shadows #4A5060. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`morning`) → `renders/sets/dyke_road__morning.png` — 같은 배치, 빛만 다름

```
the narrow earthen embankment road leading into the island, reeds on both sides, a cluster of shacks at the island entrance. Seen from the bare earth yard at the island end, looking south across the yard to the start of the road and on toward the mainland: on the near left a plywood notice board on two posts at the road's left shoulder; from there the narrow dirt road, about 5 m wide, runs straight away on top of a raised earth embankment about 3 m high, its surface rutted by truck tires with muddy water in the ruts; grassy earth banks slope down on both sides into tall reeds and shallow water; far away at the end of the road the low houses of the mainland and a hazy 1980s city skyline. Lighting: early morning, low sun from the left (east), cool clear light, dew sparkling on the reeds, key color #8C8F94, cel shadows #4A5060. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

③ 변형 (`night`) → `renders/sets/dyke_road__night.png` — 같은 배치, 빛만 다름

```
the narrow earthen embankment road leading into the island, reeds on both sides, a cluster of shacks at the island entrance. Seen from the bare earth yard at the island end, looking south across the yard to the start of the road and on toward the mainland: on the near left a plywood notice board on two posts at the road's left shoulder; from there the narrow dirt road, about 5 m wide, runs straight away on top of a raised earth embankment about 3 m high, its surface rutted by truck tires with muddy water in the ruts; grassy earth banks slope down on both sides into tall reeds and shallow water; far away at the end of the road the low houses of the mainland and a hazy 1980s city skyline. Lighting: night, darkness, only low distant lights from the tent and shacks behind the viewer, cold navy blue, key color #5A6F88, cel shadows #263150. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [dyke_road_to_island] 둑길 — 뭍 쪽에서 섬을 봄(같은 구도 기준) — 3-30, 3-32

- 8절: 둑길·섬 어귀 · 크기: 둑길 약 400 + 섬 원경
- 카메라 자리: mainland_north_fixed: 뭍 쪽 끝에서 섬 쪽으로(북향) 고정 와이드 — 3-30·3-31·3-32 '같은 구도' 기준

① 기준 배경 (`sunset`) → `renders/sets/dyke_road_to_island.png`

```
the narrow earthen embankment road leading into the island, reeds on both sides, a cluster of shacks at the island entrance. Fixed framing: seen from the mainland end of the embankment road looking north toward the island, the road running straight away from the viewer across the low reed flats to the island, the small flat-topped hill on the left (west) and the bigger flat-topped hill on the right (east), the Han River opening on the far left. At the far end of the road the low roofs of the shack cluster and a corrugated-iron shed; behind them the two terraced flat-topped trash hills with a dump-truck ramp and power transmission towers in front of them. Lighting: 1988 late July sunset, the low sun on the left (west) over the river, the sky grading from orange to violet, thin evening smoke rising above the shack roofs, the two hills in silhouette, key color #E8853A, cel shadows #4A3448. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`autumn_morning`) → `renders/sets/dyke_road_to_island__autumn_morning.png` — 같은 배치, 빛만 다름

```
the narrow earthen embankment road leading into the island, reeds on both sides, a cluster of shacks at the island entrance. Fixed framing: seen from the mainland end of the embankment road looking north toward the island, the road running straight away from the viewer across the low reed flats to the island, the small flat-topped hill on the left (west) and the bigger flat-topped hill on the right (east), the Han River opening on the far left. At the far end of the road the low roofs of the shack cluster and a corrugated-iron shed; behind them the two terraced flat-topped trash hills with a dump-truck ramp and power transmission towers in front of them. Lighting: 1988 autumn morning, clear autumn light, hazy beige sky, a line of trucks loaded with household goods leaving along the road, key color #C99A62, cel shadows #5A4A3C. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [notice_board] 섬 어귀 게시판 — 1-15, 1-16, 1-17, 2-15

- 8절: 섬 어귀 게시판 · 크기: 게시판 1.8×1.2 (기둥 높이 약 2)
- 카메라 자리: board_front: 마당에서 게시판 정면(남향). 오른쪽으로 둑길이 뭍까지 / over_shoulder: 은주 어깨 너머 게시판, 종이 두 장 나란히(남향) / thumbtack_close: 압정 머리·종이 귀퉁이 극접사 / road_north: 둑길에서 섬 쪽(북향): 걸어오는 은주, 그 뒤 고물상 함석지붕

① 기준 배경 (`morning`) → `renders/sets/notice_board.png`

```
a weathered plywood notice board on two posts at the island entrance, pinned papers. Seen from the bare earth yard on the island side looking south: the board, about 1.8 m wide and 1.2 m high on two wooden posts, stands at the left (east) shoulder of the end of the narrow embankment road, its face toward the viewer; the rutted road runs away to the mainland just to the right of the board; puddles and truck tire ruts in front of it, reeds behind it. Lighting: 1987 May early morning, low sun from the left (east), cool clear light, dew on the reeds, key color #8C8F94, cel shadows #4A5060. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`evening`) → `renders/sets/notice_board__evening.png` — 같은 배치, 빛만 다름

```
a weathered plywood notice board on two posts at the island entrance, pinned papers. Seen from the bare earth yard on the island side looking south: the board, about 1.8 m wide and 1.2 m high on two wooden posts, stands at the left (east) shoulder of the end of the narrow embankment road, its face toward the viewer; the rutted road runs away to the mainland just to the right of the board; puddles and truck tire ruts in front of it, reeds behind it. Lighting: 1987 May evening, low light from the right (west) raking across the board, a glint on a gold-bordered paper, key color #D8A657, cel shadows #5A4636. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [hanbit_hall] 한빛문화회관 홀 — 무대·객석 — 3-19, 3-20, 3-21, 3-23, 3-25, 3-26, 3-27

- 8절: 한빛문화회관 (앞·로비·복도·무대 옆·홀) · 크기: 홀 약 30×35, 무대 폭 약 16·깊이 10·높이 1.2
- 카메라 자리: house_back: 객석 뒤에서 무대 정면 와이드 / stage_to_house: 무대 위(은주 등 뒤 또는 은주 시점)에서 객석으로. 무대 옆은 화면 왼쪽 / floor_low: 무대 바닥 높이에서 객석 쪽으로 낮게 미끄러짐 / front_row_low: 맨 앞줄 오른쪽 끝자리, 로앵글(태준 기립) / back_corner: 맨 뒷줄 왼쪽 구석(최 계장) / center_seat: 객석 한가운데(만석) 가까이

① 기준 배경 (`show`) → `renders/sets/hanbit_hall.png`

```
the fictional Hanbit Cultural Center, a 1980s concert hall: concrete facade with wide stone steps and tall glass doors, a lobby with terrazzo floor, a backstage corridor, red velvet stage curtains, wooden stage, rows of dark gray-upholstered audience seats. View (only the hall interior is shown): seen from the back of the audience looking toward the stage: a large hall about 30 m wide and 35 m deep; across the front a raised wooden stage about 1.2 m high and 16 m wide, the red velvet curtains drawn open to both sides of the proscenium; at the right end of the stage, behind the curtain edge, a dark wing, and a short flight of steps going down from that wing to the right end of the front row; the audience seats on a gentle rake in three blocks separated by two aisles; a long plain judges' table set across the center block about seven rows back; exit doors at both back corners; rows of spotlights hanging from battens above the front of the stage. Lighting: 1988 midsummer, daytime show indoors, warm amber spotlights from above and front on the stage, the audience seats in deep navy darkness, warm reflections on the wooden stage floor, key color #D9B44A, cel shadows #2E2A44. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`solo_spot`) → `renders/sets/hanbit_hall__solo_spot.png` — 같은 배치, 빛만 다름

```
the fictional Hanbit Cultural Center, a 1980s concert hall: concrete facade with wide stone steps and tall glass doors, a lobby with terrazzo floor, a backstage corridor, red velvet stage curtains, wooden stage, rows of dark gray-upholstered audience seats. View (only the hall interior is shown): seen from the back of the audience looking toward the stage: a large hall about 30 m wide and 35 m deep; across the front a raised wooden stage about 1.2 m high and 16 m wide, the red velvet curtains drawn open to both sides of the proscenium; at the right end of the stage, behind the curtain edge, a dark wing, and a short flight of steps going down from that wing to the right end of the front row; the audience seats on a gentle rake in three blocks separated by two aisles; a long plain judges' table set across the center block about seven rows back; exit doors at both back corners; rows of spotlights hanging from battens above the front of the stage. Lighting: the house dark, the spotlight narrowed to a single warm circle at center stage, the rest of the stage in darkness, key color #D9B44A, cel shadows #2E2A44. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

③ 변형 (`award`) → `renders/sets/hanbit_hall__award.png` — 같은 배치, 빛만 다름

```
the fictional Hanbit Cultural Center, a 1980s concert hall: concrete facade with wide stone steps and tall glass doors, a lobby with terrazzo floor, a backstage corridor, red velvet stage curtains, wooden stage, rows of dark gray-upholstered audience seats. View (only the hall interior is shown): seen from the back of the audience looking toward the stage: a large hall about 30 m wide and 35 m deep; across the front a raised wooden stage about 1.2 m high and 16 m wide, the red velvet curtains drawn open to both sides of the proscenium; at the right end of the stage, behind the curtain edge, a dark wing, and a short flight of steps going down from that wing to the right end of the front row; the audience seats on a gentle rake in three blocks separated by two aisles; a long plain judges' table set across the center block about seven rows back; exit doors at both back corners; rows of spotlights hanging from battens above the front of the stage. Lighting: the whole stage evenly and brightly lit in warm light for the award ceremony, the audience in navy, key color #FFC93C, cel shadows #2E2A44. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [hanbit_wing] 한빛문화회관 무대 옆, 커튼 뒤 — 3-18, 3-21, 3-22, 3-24, 3-27

- 8절: 한빛문화회관 (앞·로비·복도·무대 옆·홀) · 크기: 약 4×6
- 카메라 자리: wing_to_stage: 무대 옆 안쪽에서 무대 쪽으로: 왼쪽 커튼 틈, 의자와 작업등 / curtain_gap_pov: 커튼 틈 시점: 무대 위 연주(은주 시점) / stage_to_wing: 무대 위에서 무대 옆 그늘로(은주 시점, 커튼 그늘의 영감) / steps_down: 무대 옆 계단에서 객석 어둠으로 내려감

① 기준 배경 (`show_warm`) → `renders/sets/hanbit_wing.png`

```
the fictional Hanbit Cultural Center, a 1980s concert hall: concrete facade with wide stone steps and tall glass doors, a lobby with terrazzo floor, a backstage corridor, red velvet stage curtains, wooden stage, rows of dark gray-upholstered audience seats. View (only this one space is shown): the dim stage wing on the right side of the stage (as seen from the audience), seen from deep inside the wing looking toward the stage: the heavy edge of the red velvet curtain on the left with a tall vertical gap of light from the stage, black masking flats and hanging ropes along the wall, a folding chair beside the curtain gap under a single bare incandescent work lamp clamped high on the wall, a short flight of steps at the near left going down toward the auditorium, a dark corner at the far right against the stage's back wall, the wooden stage floor continuing beyond the gap. Lighting: daytime show indoors, a single bare incandescent work lamp making a small yellow pool of light, a strip of the stage's warm amber spotlight leaking through the curtain gap, the rest in darkness, key color #E8C98A, cel shadows #3E3226. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`show_cold`) → `renders/sets/hanbit_wing__show_cold.png` — 같은 배치, 빛만 다름

```
the fictional Hanbit Cultural Center, a 1980s concert hall: concrete facade with wide stone steps and tall glass doors, a lobby with terrazzo floor, a backstage corridor, red velvet stage curtains, wooden stage, rows of dark gray-upholstered audience seats. View (only this one space is shown): the dim stage wing on the right side of the stage (as seen from the audience), seen from deep inside the wing looking toward the stage: the heavy edge of the red velvet curtain on the left with a tall vertical gap of light from the stage, black masking flats and hanging ropes along the wall, a folding chair beside the curtain gap under a single bare incandescent work lamp clamped high on the wall, a short flight of steps at the near left going down toward the auditorium, a dark corner at the far right against the stage's back wall, the wooden stage floor continuing beyond the gap. Lighting: daytime show indoors, a single bare incandescent work lamp making a small yellow pool of light, a narrow blade of cold white stage light cutting in through the curtain gap like a knife, the rest in darkness, key color #E8C98A, cel shadows #3E3226. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [hanbit_corridor] 한빛문화회관 무대 뒤 복도 — 3-17

- 8절: 한빛문화회관 (앞·로비·복도·무대 옆·홀) · 크기: 폭 약 2, 길이 약 20
- 카메라 자리: mirror_front: 거울 속 정면 / follow_dark: 뒤를 따라 복도 끝 어둠 속으로

① 기준 배경 (`fluorescent`) → `renders/sets/hanbit_corridor.png`

```
the fictional Hanbit Cultural Center, a 1980s concert hall: concrete facade with wide stone steps and tall glass doors, a lobby with terrazzo floor, a backstage corridor, red velvet stage curtains, wooden stage, rows of dark gray-upholstered audience seats. View (only this one space is shown): the narrow backstage corridor, seen from one end looking down its length: painted concrete walls, plain dressing-room doors on the right, a wide wall mirror on the left wall near the viewer, fluorescent tubes on the ceiling, the far end of the corridor fading into darkness toward the stage wing. Lighting: white fluorescent tubes overhead, flat light, the far end dark, key color #EDEBE4, cel shadows #4E4A5E. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [hanbit_lobby] 한빛문화회관 로비 — 3-28

- 8절: 한빛문화회관 (앞·로비·복도·무대 옆·홀) · 크기: 약 25×12
- 카메라 자리: lobby_glass: 홀 문 쪽에서 유리문 쪽으로(역광) / two_shot_side: 사람들 사이 두 사람 옆모습 투숏

① 기준 배경 (`late_afternoon`) → `renders/sets/hanbit_lobby.png`

```
the fictional Hanbit Cultural Center, a 1980s concert hall: concrete facade with wide stone steps and tall glass doors, a lobby with terrazzo floor, a backstage corridor, red velvet stage curtains, wooden stage, rows of dark gray-upholstered audience seats. View (only this one space is shown): the lobby, seen from near the hall doors looking toward the entrance: a wide lobby with a polished terrazzo floor and square columns, a row of tall glass doors along the far wall with the bright plaza beyond, a broad staircase rising on the right. Lighting: late afternoon, low sunlight slanting in through the tall glass doors, long reflections on the terrazzo floor, key color #F0CF85, cel shadows #6A5038. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [hanbit_front] 한빛문화회관 앞·계단 — 3-16, 3-29

- 8절: 한빛문화회관 (앞·로비·복도·무대 옆·홀) · 크기: 계단 폭 약 30, 광장 약 60×40
- 카메라 자리: steps_up: 계단 아래에서 정면을 올려다봄 / steps_down: 계단 위에서 광장 쪽으로 내려다봄(긴 그림자, 역광) / plaza_wide: 광장의 전세 버스와 사람들, 노을 와이드

① 기준 배경 (`noon`) → `renders/sets/hanbit_front.png`

```
the fictional Hanbit Cultural Center, a 1980s concert hall: concrete facade with wide stone steps and tall glass doors, a lobby with terrazzo floor, a backstage corridor, red velvet stage curtains, wooden stage, rows of dark gray-upholstered audience seats. View (only this one space is shown): the front of the building, seen from the bottom of the steps looking up: a broad, plain 1980s concrete facade, wide pale stone steps rising across its whole front to a row of tall glass doors, a large paved plaza at the foot of the steps where a bus can pull in, a busy city avenue beyond the plaza. Lighting: 1988 midsummer noon, harsh overhead sun, the plaza glaring white, short shadows, a hazy white sky, key color #F5F5F2, cel shadows #5B5E78. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`sunset`) → `renders/sets/hanbit_front__sunset.png` — 같은 배치, 빛만 다름

```
the fictional Hanbit Cultural Center, a 1980s concert hall: concrete facade with wide stone steps and tall glass doors, a lobby with terrazzo floor, a backstage corridor, red velvet stage curtains, wooden stage, rows of dark gray-upholstered audience seats. View (only this one space is shown): the front of the building, seen from the bottom of the steps looking up: a broad, plain 1980s concrete facade, wide pale stone steps rising across its whole front to a row of tall glass doors, a large paved plaza at the foot of the steps where a bus can pull in, a busy city avenue beyond the plaza. Lighting: sunset, the low sun behind the plaza side, long shadows stretching up the steps, orange-gold backlight, key color #F7B955, cel shadows #6E4A3A. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [hanbit_rehearsal] 한빛문화회관 연습실 — 2-4

- 8절: 한빛문화회관 연습실 · 크기: 약 20×15
- 카메라 자리: room_wide: 뒷문 쪽에서 앞으로 와이드(창 왼쪽) / last_rows: 맨 뒷줄과 바로 앞줄 사이(은주·태준 교차)

① 기준 배경 (`day`) → `renders/sets/hanbit_rehearsal.png`

```
the fictional Hanbit Cultural Center, its large rehearsal room: a polished wooden floor, rows of folding chairs grouped by school, white fluorescent ceiling lights, tall windows, a slogan-only Olympic campaign poster on the wall. Seen from the back of the room by the entrance door looking toward the front: an open playing area at the front of the room; rows of folding chairs facing it, grouped by school with gaps between the groups; tall windows along the left wall letting in bands of sunlight; the poster on the right wall; the last row of chairs right in front of the viewer. Lighting: 1987 late October daytime, flat white fluorescent light plus bands of sunlight from the tall windows on the left, key color #3A5A8C, cel shadows #2C3A55. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [island_wide] 갈대섬 전경 — 1-1, 2-1, 2-28, 3-25

- 8절: 갈대섬 전경 · 크기: 섬 약 2km×1km(제안)
- 카메라 자리: high_north: 뭍 쪽 하늘에서 섬 전체를 북향으로 내려다보는 높은 와이드

① 기준 배경 (`afternoon`) → `renders/sets/island_wide.png`

```
a fictional landfill island on the Han River at the edge of Seoul, two flat-topped mesa-like hills of compacted trash still being built ('the big hill' and 'the small hill'), terraced ochre and gray-brown slopes with dump-truck ramps, specks of white plastic, power transmission towers in front, a single earthen embankment road linking it to the mainland, reeds along the water, hazy beige sky. High wide view from above the channel on the mainland side, looking north at the whole island: the embankment road runs up from the bottom of the frame to the island entrance at the south edge, where a small cluster of low shacks, a corrugated-iron shed and a canvas tent sit; behind them the small flat-topped hill on the left (west) and the bigger, taller one on the right (east), each with a dump-truck ramp zigzagging up its terraces; a row of power transmission towers in front of the hills; the Han River wrapping around the west side; reed beds along the shore. Lighting: 1987 October afternoon, cool clear light from the left (west), hazy beige sky, a thin wisp of smoke rising far off on the big hill, key color #C99A62, cel shadows #6E5640. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`night`) → `renders/sets/island_wide__night.png` — 같은 배치, 빛만 다름

```
a fictional landfill island on the Han River at the edge of Seoul, two flat-topped mesa-like hills of compacted trash still being built ('the big hill' and 'the small hill'), terraced ochre and gray-brown slopes with dump-truck ramps, specks of white plastic, power transmission towers in front, a single earthen embankment road linking it to the mainland, reeds along the water, hazy beige sky. High wide view from above the channel on the mainland side, looking north at the whole island: the embankment road runs up from the bottom of the frame to the island entrance at the south edge, where a small cluster of low shacks, a corrugated-iron shed and a canvas tent sit; behind them the small flat-topped hill on the left (west) and the bigger, taller one on the right (east), each with a dump-truck ramp zigzagging up its terraces; a row of power transmission towers in front of the hills; the Han River wrapping around the west side; reed beds along the shore. Lighting: deep night, the whole island dark navy, stars above the black hills, a single small yellow light at the island entrance, key color #1A2238, cel shadows #232C4A. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [scrap_heap] 큰 산 아래 쇳더미 — 1-1, 1-2, 3-6, 3-20

- 8절: 큰 산 아래 쇳더미 · 크기: 더미 높이 약 4, 둘레 약 10
- 카메라 자리: heap_up: 더미 아래에서 꼭대기(빨간 깃발)를 올려다봄(남향) / heap_pan: 은주 시점, 더미를 천천히 훑는 팬 / from_small_hill: 작은 산 중턱에서 내려다본 롱숏(small_hill_slope의 slope_down_se)

① 기준 배경 (`morning`) → `renders/sets/scrap_heap.png`

```
at the foot of the big trash hill where dump trucks unload: a fresh heap of scrap iron and tin, tire ruts in the mud. Seen from the mud at the foot of the heap, looking up and south: a heap about 4 m high of freshly dumped scrap iron, tin cans, bent pipes and sheet metal at the end of the truck road at the southwest foot of the big hill; deep tire ruts in the mud around it; mud-covered lumps scattered at its base; beyond the top of the heap the hazy beige sky, and on the right in the distance the smaller flat-topped trash hill. Lighting: early morning, low sun from the left (east) at a slant, short metallic glints on the scrap, hazy beige sky, key color #C9A66B, cel shadows #6E5640. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [shack_village] 판잣집 동네 외경 — 1-4, 1-10, 2-14, 3-25

- 8절: 판잣집 동네 외경 · 크기: 골목 폭 1~2
- 카메라 자리: alley_west: 골목 안에서 서쪽으로: 오른쪽에 은주네 집 현관 / roofs_to_entrance: 은주네 집 근처에서 지붕들 너머 남동쪽 섬 어귀(고물상 불빛 하나)

① 기준 배경 (`dusk`) → `renders/sets/shack_village.png`

```
the shack village at the island entrance: low shacks of plywood, tar paper and cement blocks with slate and roofing-felt roofs weighed down by plastic sheets and stones, narrow winding dirt alleys, thin stovepipes. Seen from inside a narrow dirt alley looking west: shacks pressed together on both sides of a 1.5 m wide alley; on the right, Eunju's family shack, a low plywood and tar-paper box about 4.5 m wide with a plank front door facing the alley, a tiny window, a thin tin stovepipe and a roof held down by plastic sheets and stones; the alley bends ahead toward the open sky, and above the roofs on the right rises the terraced slope of the small trash hill. Lighting: 1987 April evening after sunset, navy twilight, yellow light in a few small shack windows, thin briquette smoke from the stovepipes, key color #3E4A6A, cel shadows #2A2F45. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`night`) → `renders/sets/shack_village__night.png` — 같은 배치, 빛만 다름

```
the shack village at the island entrance: low shacks of plywood, tar paper and cement blocks with slate and roofing-felt roofs weighed down by plastic sheets and stones, narrow winding dirt alleys, thin stovepipes. Seen from inside a narrow dirt alley looking west: shacks pressed together on both sides of a 1.5 m wide alley; on the right, Eunju's family shack, a low plywood and tar-paper box about 4.5 m wide with a plank front door facing the alley, a tiny window, a thin tin stovepipe and a roof held down by plastic sheets and stones; the alley bends ahead toward the open sky, and above the roofs on the right rises the terraced slope of the small trash hill. Lighting: night, the village dark navy, over the roofs toward the island entrance a single yellow light from the junk shop, key color #24304F, cel shadows #1E2740. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [pawnshop] 만복전당포 — 2-8, 3-10, 3-33

- 8절: 만복전당포 · 크기: 2.5×6
- 카메라 자리: door_in: 문 안에서 계산대 쪽으로(진열장 왼쪽) / counter_reverse: 계산대 뒤 주인 자리에서 문 쪽으로(문 종, 들어오는 사람) / counter_top: 계산대 위 부감(케이스 안, 전당표, 동전)

① 기준 배경 (`winter_morning`) → `renders/sets/pawnshop.png`

```
a narrow 1980s pawnshop: glass display cases with watches, gold rings and cameras, a yellowed fluorescent light, an abacus on the counter. Seen from just inside the front door looking in: a narrow shop about 2.5 m wide and 6 m deep; a long glass display case along the left wall; at the back a glass-fronted counter across the width with the abacus and a ledger on it and a stool behind it; behind the counter a doorway hung with a faded cloth curtain leading to a storeroom; plain shelves with a few pawned radios and small appliances on the right wall; a single yellowed fluorescent tube on the ceiling; a small brass bell on a bracket above the door. Lighting: 1987 mid-November frosty morning, inside a yellowed flickering fluorescent tube, cold pale light at the glass door behind the viewer, key color #B9A86A, cel shadows #5E5238. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`summer_day`) → `renders/sets/pawnshop__summer_day.png` — 같은 배치, 빛만 다름

```
a narrow 1980s pawnshop: glass display cases with watches, gold rings and cameras, a yellowed fluorescent light, an abacus on the counter. Seen from just inside the front door looking in: a narrow shop about 2.5 m wide and 6 m deep; a long glass display case along the left wall; at the back a glass-fronted counter across the width with the abacus and a ledger on it and a stool behind it; behind the counter a doorway hung with a faded cloth curtain leading to a storeroom; plain shelves with a few pawned radios and small appliances on the right wall; a single yellowed fluorescent tube on the ceiling; a small brass bell on a bracket above the door. Lighting: 1988 summer daytime, the same yellow fluorescent light, a strip of bright summer daylight across the floor from the opened door, key color #B9A86A, cel shadows #5A4A30. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [market_alley] 시장 골목 — 2-8, 2-9

- 8절: 시장 골목 · 크기: 골목 폭 약 3, 길이 약 40
- 카메라 자리: mouth_in: 골목 어귀에서 안쪽 끝 전당포 쪽으로 / sign_down: 전당포 간판에서 문 앞으로 내려옴 / radio_close: 전파사 진열대 라디오 스피커 극접사

① 기준 배경 (`frost_morning`) → `renders/sets/market_alley.png`

```
a 1980s Seoul market alley: low shop fronts, an electronics repair shop with a radio, hand-painted fictional signs. Seen from the mouth of the alley looking in: a narrow alley about 3 m wide lined with low one- and two-story shop fronts with blank hand-painted signboards and rolled-up awnings; on the near right, the electronics repair shop with radios on a display rack at its open front; the alley runs straight and ends at a narrow pawnshop front with an old signboard hanging crooked at one end; frost on the shaded ground; just outside the alley mouth on the main street, a two-wheeled handcart parked. Lighting: 1987 mid-November morning, cold low light, frost in the shaded alley, visible breath, key color #B9A86A, cel shadows #5E5238. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [school_auditorium] 학교 강당 — 2-18, 2-19, 3-10

- 8절: 학교 강당 · 크기: 약 18×30
- 카메라 자리: back_to_stage: 뒷문에서 무대 쪽 와이드 / wing_gap_to_house: 무대 옆 커튼 틈에서 객석을 훑어 문까지(은주 시점) / closed_door: 닫힌 뒷문 고정

① 기준 배경 (`day`) → `renders/sets/school_auditorium.png`

```
a 1980s school auditorium: a wooden stage with a raised platform, folding chairs, high windows. Seen from the back doors looking toward the stage: a long hall with a wooden floor; at the far end a raised wooden stage with a plain dark curtain at each side, the right side curtain hiding a narrow wing; rows of metal folding chairs facing the stage with a center aisle; high windows along both long walls near the ceiling; a pair of plain wooden double doors at the back behind the viewer. Lighting: 1988 April daytime, stage lights from above the front of the stage, the wing behind the curtain dim, the seats lit by daylight from the high windows, key color #7A6B5A, cel shadows #3E342A. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`evening`) → `renders/sets/school_auditorium__evening.png` — 같은 배치, 빛만 다름

```
a 1980s school auditorium: a wooden stage with a raised platform, folding chairs, high windows. Seen from the back doors looking toward the stage: a long hall with a wooden floor; at the far end a raised wooden stage with a plain dark curtain at each side, the right side curtain hiding a narrow wing; rows of metal folding chairs facing the stage with a center aisle; high windows along both long walls near the ceiling; a pair of plain wooden double doors at the back behind the viewer. Lighting: evening, stage lights and indoor lights on, the high windows dark blue, key color #7A6B5A, cel shadows #3E342A. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [night_school] 강변교회 지하 공부방 — 1-6

- 8절: 강변교회 지하 공부방 · 크기: 약 6×5, 천장 2.4
- 카메라 자리: bulb_down: 백열등에서 내려와 교실 전체로 / stairs_up: 계단 아래에서 올려다봄(사탕이 화면 쪽으로 쏟아짐) / across_room: 교실을 사이에 두고 칠판 앞 선영과 뒷줄 은주 투샷(옆에서)

① 기준 배경 (`evening`) → `renders/sets/night_school.png`

```
a 1980s church basement study room for neighborhood children: a green chalkboard, mismatched desks, three bare incandescent bulbs hanging from the ceiling, a small high window. Seen from the foot of the stairs at the back of the room looking toward the front: a steep narrow concrete staircase comes straight down from a street-level door into the back-right corner of the room; mismatched wooden desks and chairs in rows facing the green chalkboard on the front wall; the three bare bulbs hang in a line down the middle of the ceiling on long cords; the small high window near the ceiling on the left wall at ground level outside. Lighting: Saturday evening, the small high window dark blue, three bare bulbs glowing yellow and swaying slightly, swinging shadows on the walls, key color #E8C46A, cel shadows #6E5640. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [city_bus] 시내버스 안 — 2-3

- 8절: 시내버스 안 · 크기: 차내 길이 약 10, 폭 2.4
- 카메라 자리: aisle_back: 통로 따라 뒤로 미끄러지며(맨 뒷자리 아이들)

① 기준 배경 (`midday`) → `renders/sets/city_bus.png`

```
inside a 1980s Seoul city bus: worn seats, hanging straps, a token box by the driver. Seen from the front near the driver's seat looking back along the aisle: worn two-seat rows on both sides facing forward, an empty long bench seat across the very back, hanging straps on metal rails along both sides of the aisle, windows along both sides, a rear exit door on one side, the token box fixed beside the driver's seat at the front door. Lighting: 1987 late October midday, bright side light through the bus windows, swaying window-frame shadows across the seats, key color #A8B3BF, cel shadows #4A5A70. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [district_office] 구청 도시정비과 사무실 — 3-12

- 8절: 구청 도시정비과 · 크기: 약 10×8
- 카메라 자리: light_down: 형광등에서 내려와 책상 줄로 / chief_desk: 과장 책상 앞에 선 최 계장(옆에서)

① 기준 배경 (`day`) → `renders/sets/district_office.png`

```
a 1980s Seoul district office: steel desks, stacks of folders, a wall map of the district, a desk fan. Seen from the entrance door looking in: gray steel desks pushed together in two facing rows down the middle of the room, stacks of folders and file trays on them, a desk fan on the desk at the head of the near row; at the far end by the windows a larger section chief's desk facing the room; the large district map on the left wall; a slogan-only Olympic campaign poster on the right wall; fluorescent tubes on the ceiling; dim windows behind the chief's desk. Lighting: 1988 early July daytime, white fluorescent light from above onto the rows of desks, weak window light, key color #E6E8EA, cel shadows #5E6A78. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [district_corridor] 구청 복도 — 3-13

- 8절: 구청 복도 · 크기: 폭 약 2.5
- 카메라 자리: plant_close: 화분 접사, 위에서 물방울

① 기준 배경 (`day`) → `renders/sets/district_corridor.png`

```
a corridor of the same 1980s Seoul district office: terrazzo floor, a row of plain office doors, a potted plant by the wall, fluorescent tubes on the ceiling. Seen along the corridor: the potted plant in the near foreground against the right wall, the row of plain doors on the left, a window at the far end glowing white. Lighting: daytime, fluorescent tubes overhead, white light from the window at the far end, key color #E6E8EA, cel shadows #5E6A78. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [park_2003_view] 푸른 언덕 공원(2003) — 같은 구도 — 3-31, 3-32

- 8절: 푸른 언덕 공원 (2003) · 크기: 둑길 자리 산책로 + 두 언덕 원경
- 카메라 자리: mainland_north_fixed: dyke_road_to_island와 같은 자리·같은 구도(북향)

① 기준 배경 (`spring_noon`) → `renders/sets/park_2003_view.png`

```
a green hilltop park built over the old landfill, grass and wildflowers, a walking path, a small outdoor stage, the Han River and a 2003 Seoul skyline. Fixed framing: seen from the mainland end of the embankment road looking north toward the island, the wide walking path running straight away from the viewer across the low reed flats to the island, the small flat-topped hill on the left (west) and the bigger flat-topped hill on the right (east), the Han River opening on the far left. Both hills are entirely green with low grass on their terraced slopes, a zigzag stairway climbing the right hill, no shacks and no trash anywhere. Lighting: 2003 spring midday, clear bright blue sky for the first time with no haze, everything in natural colors, soft spring sunlight from above and slightly left, key color #7FB77E, cel shadows #3F5A6A. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [park_2003_stage] 푸른 언덕 공원 꼭대기, 작은 무대(2003) — 3-34

- 8절: 푸른 언덕 공원 (2003) · 크기: 무대 약 6×4, 객석 의자 약 60석
- 카메라 자리: audience_back: 객석 뒤에서 무대와 하늘을 넓게(남향) / stage_to_audience: 무대에서 객석으로(은주 시점, 맨 앞줄부터 팬, 북향) / down_slope: 언덕 비탈을 따라 강 쪽으로 내려감(풀밭과 흙)

① 기준 배경 (`spring_noon`) → `renders/sets/park_2003_stage.png`

```
a green hilltop park built over the old landfill, grass and wildflowers, a walking path, a small outdoor stage, the Han River and a 2003 Seoul skyline. View: the flat top of the smaller green hill, seen from behind the audience looking south: rows of folding chairs on the grass facing a small low wooden stage at the south edge of the summit; a banner on a frame beside the stage; behind the stage the hillside drops away so the open sky is wide, and far below the glittering river and the 2003 Seoul skyline; a walking path curving across the summit. Lighting: 2003 spring midday, wide clear blue sky, the sun high and behind the stage, no dark shadows on the stage, the river sparkling below, natural colors, key color #7FB77E, cel shadows #3F5A6A. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [island_after] 갈대섬 전경(매립 끝난 뒤, 1990년대) — 3-32

- 8절: 갈대섬 전경 (매립 끝난 뒤, 1990년대) · 크기: 섬 원경
- 카메라 자리: mainland_north_fixed: dyke_road_to_island와 같은 자리·같은 구도(북향)

① 기준 배경 (`overcast`) → `renders/sets/island_after.png`

```
the same island after landfill closure: the two flat-topped hills covered with fresh soil, no trash visible, first green sprouts and grass on the terraced slopes, the embankment road, the Han River. Fixed framing: seen from the mainland end of the embankment road looking north toward the island, the road running straight away from the viewer across the low reed flats to the island, the small flat-topped hill on the left (west) and the bigger flat-topped hill on the right (east), the Han River opening on the far left. The ground where the shacks stood at the end of the road is bare and empty. Lighting: early 1990s overcast daytime, flat gray light, fresh brown soil, no people, key color #8C8F94, cel shadows #4A4258. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

② 변형 (`greening`) → `renders/sets/island_after__greening.png` — 같은 배치, 빛만 다름

```
the same island after landfill closure: the two flat-topped hills covered with fresh soil, no trash visible, first green sprouts and grass on the terraced slopes, the embankment road, the Han River. Fixed framing: seen from the mainland end of the embankment road looking north toward the island, the road running straight away from the viewer across the low reed flats to the island, the small flat-topped hill on the left (west) and the bigger flat-topped hill on the right (east), the Han River opening on the far left. The ground where the shacks stood at the end of the road is bare and empty. Lighting: 1990s, soft daylight, green spreading over the soil, the same framing, key color #A8C88A, cel shadows #3F5A6A. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [temp_alley] 임시 거처 골목 (1988) — 3-32

- 8절: 임시 거처 골목 (1988) · 크기: 골목 폭 약 6
- 카메라 자리: entrance_in: 골목 입구에서 안으로(입구에 서류 든 최 계장)

① 기준 배경 (`autumn_day`) → `renders/sets/temp_alley.png`

```
a narrow dirt alley between rows of identical single-story prefabricated temporary houses in 1988 Seoul, thin panel walls, small windows, a shared water tap at the alley entrance; seen from the alley entrance looking in, the water tap on the right, laundry lines across the alley. Lighting: 1988 autumn daytime, soft autumn light, key color #D8C8A8, cel shadows #4A4A6E. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [rental_alley] 임대주택 골목 — 3-32

- 8절: 임대주택 골목 · 크기: 골목 폭 약 6
- 카메라 자리: entrance_in: 골목 입구에서 안으로(입구에 서류 든 최 계장)

① 기준 배경 (`autumn_day`) → `renders/sets/rental_alley.png`

```
a narrow alley between new low-rise public rental apartment blocks in 1990 Seoul, rows of identical windows, a concrete alley entrance. Seen from the alley entrance looking in: two plain five-story walk-up blocks facing each other across a narrow concrete lane, rows of identical windows on both facades, a parked moving truck stacked with household goods halfway down the lane. Lighting: 1990 autumn daytime, soft autumn light, key color #D8C8A8, cel shadows #4A4A6E. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [school_gate] 학교 교문 — 3-32

- 8절: 학교 교문 · 크기: 교문 폭 약 6
- 카메라 자리: street_in: 길에서 교문 안으로 뛰어 들어가는 아이들

① 기준 배경 (`autumn_morning`) → `renders/sets/school_gate.png`

```
a late-1980s Seoul elementary school front gate: an iron gate between concrete posts, a dirt schoolyard and a three-story school building behind. Seen from the street outside: the iron gate standing open between two square concrete posts, the wide dirt schoolyard beyond, the long three-story school building across the back of the yard. Lighting: 1988 autumn morning, bright morning sunlight, long shadows across the dirt yard, key color #E8D6A0, cel shadows #4A4A6E. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [mainland_alley] 뭍의 골목 — 2-1

- 8절: 뭍의 골목 · 크기: 골목 폭 약 3
- 카메라 자리: lane_along: 골목을 따라 리어카를 끄는 만석

① 기준 배경 (`afternoon`) → `renders/sets/mainland_alley.png`

```
a mainland back alley of 1980s Seoul outside the island: low brick and cement-block houses, gray walls, wooden utility poles, a narrow lane of cracked asphalt and dirt. Seen along the lane: gray block walls and low houses on both sides, wooden utility poles with sagging wires, the lane narrowing into the distance. Lighting: 1987 autumn early afternoon, the sun still high, short shadows at the wall bases, key color #D9822B, cel shadows #6E5640. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [fb_theater] 회상: 1970년대 극장 쇼 무대 — 3-3

- 8절: 회상: 1970년대 극장 쇼 무대 · 크기: 무대 폭 약 12
- 카메라 자리: front_to_band: 무대 앞에서 뒤쪽 악단석으로 천천히

① 기준 배경 (`sepia_night`) → `renders/sets/fb_theater.png`

```
a 1970s downtown Seoul theater show stage: a glittering tinsel curtain, footlights, a small band seated with music stands on a lower riser just behind the singer's platform. Seen from the front of the stage moving back toward the band: the singer's place at the front center of a raised stage edged with footlights, the glittering tinsel curtain hanging behind it, and the small band seated with music stands on a lower level just behind the singer's platform. Lighting: 1970s night, sepia-toned flashback, a strong stage spotlight glaring from the stage toward the band so that faces dissolve into the glare, reflections sparkling on the tinsel curtain, key color #A8865E, cel shadows #4A3A30. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [fb_radio_shop] 회상: 1970년대 라디오 수리점 — 3-21

- 8절: 회상: 라디오 수리점 · 크기: 약 3×4
- 카메라 자리: bench_close: 작업대 위 손가락과 소리굽쇠(얼굴 없이)

① 기준 배경 (`sepia_day`) → `renders/sets/fb_radio_shop.png`

```
a small 1970s Seoul radio repair shop: shelves crowded with transistor and vacuum-tube radios, a workbench with a soldering iron and small tools. Seen from the doorway: shelves of radios covering the back and side walls, the workbench under them in front with a soldering iron and small tools, a stool at the bench. Lighting: 1970s daytime, sepia-toned translucent flashback, soft blurry light, key color #C8A878, cel shadows #4A3A30. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```

### [fb_shanty_1950s] 회상: 1950년대 판자촌 집 — 3-12

- 8절: 회상: 1950년대 판자촌 집 · 크기: 한 칸 약 2.5×2.5
- 카메라 자리: bare_feet: 지붕 아래 쪼그린 작은 아이의 맨발

① 기준 배경 (`rain`) → `renders/sets/fb_shanty_1950s.png`

```
a 1950s Seoul hillside shanty: a rusty corrugated tin roof, plywood and straw-mat walls, a dirt floor. Seen from inside, low: a cramped single room under the rusty corrugated tin roof, plywood and straw-mat walls patched together, a bare dirt floor, rain dripping through a seam of the roof. Lighting: faded-color flashback, gray rainy light, rain drumming on the tin roof, key color #9A9A90, cel shadows #4A4A48. Style: clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic proportions, soft gradient only in sky and backlight, no paper texture, no film grain, wide background establishing art, no people. no text, no letters, no speech bubbles, no brand logos, no real banknotes, no official Olympic mascot or emblem, fictional characters not resembling any real person, children drawn as ordinary kids, no injuries or blood
```
