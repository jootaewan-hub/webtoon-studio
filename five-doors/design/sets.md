# 배경 설정서 — 「단톡방에 그 남자가 있다」

ChatGPT(이미지 생성)와 Codex가 **같은 장소를 매번 같은 구조·같은 빛으로** 그리게 하기 위한 배경 설정서와 프롬프트다. 이 파일에는 그림이 없다. 같은 내용이 `handoff/sets.md`와 `design/sets.md`에 있다.

## 0. 이 문서를 쓰는 법

- **기준 순서**: `story/novel.md` > `story/script.md`(변경 기록 포함) > `story/bible.md` > `story/SPEC.md`. 이 문서는 그 넷에 이미 나온 사실을 공간으로 옮기고 빈칸을 채운다. 소설·대본과 다르면 소설·대본을 따른다.
- **표기**
  - 문장(또는 표 칸) 끝 `*`: 이 문서에서 새로 정한 세부. 소설·대본에는 없다. 바꿔도 되지만 바꾸면 이 문서도 고친다.
  - `(N화 S#n)`: 대본 씬 번호. `(N화)`만 있으면 소설 근거다.
  - '추측입니다': 고증을 확인하지 못한 내용이다. 그림에는 써도 되지만 사실로 인용하지 않는다.
- **방위와 '시계방향'**
  - 모든 평면은 **북쪽이 위**다.
  - '들어가는 문 기준 시계방향' = 문을 등지고 방 안을 바라보고 섰을 때 **왼쪽 벽 → 정면 벽 → 오른쪽 벽 → 등 뒤(문 쪽 벽)** 순서로 적는다. 위에서 내려다본 평면도에서 시계방향과 같다.
  - 거리는 미터(m), 면적은 전용면적(㎡)과 공급면적 기준 평을 함께 적는다.
- **프롬프트 구조**: 모든 코드블록 = 공통 스타일 문구 + **SET LOCK**(장소별 고정 묘사, 80~120단어) + 컷 지시. **블록 전체를 그대로 복사**한다. SET LOCK은 한 글자도 바꾸지 않는다.
- **공통 금지**
  - 인물을 넣지 않는다. 배경에 사람이 생기면 다시 뽑는다.
  - 글자를 넣지 않는다. 간판, 'CLOSED' 팻말, 칠판 장부, '정기 점검 중', 모니터 기록, 층수 숫자는 모두 **빈 면으로 뽑고 식자 단계에서** 넣는다.
  - 실제 브랜드 로고를 넣지 않는다. BMW → 로고 없는 검정 대형 세단, 샤넬 가방 → 로고 없는 퀼팅 체인 백.
  - 배경 단계에서는 노출이 없다. 관능 장면의 수위 장치(가림 소품, 실루엣 광원, 컷을 넘길 사물)는 장소마다 따로 적었다.
  - 아이들(지호, 소이)이 나오는 장소(3801호 낮, 놀이터, 1204호 낮)의 배경 컷에 관능 소품을 두지 않는다.
- **화풍**: 본편은 G6 1안 '글로시 반실사'다(`design/style_options.md`). 코미디 컷(2안 셀)과 쇼츠 티저(3안 네온 누아르)는 **같은 SET LOCK**에 아래 꼬리 문장만 바꿔 단다*.
  - 코미디 컷: 프롬프트 끝에 `Flat cel-shaded variant: bold ink outlines, two-tone flat colors, simplified shapes.`*
  - 티저: 프롬프트 끝에 `Neon noir variant: large black areas, magenta and cyan rim light only, film grain, wet reflections.`*
- **비율**: 빈 배경 설정화는 가로 16:9. 카메라 자리 컷은 웹툰 세로 칸에 맞춰 세로 9:16을 기본으로 하고, 와이드 컷만 16:9로 적었다*.
- **인물 색 코드**(작품 전체 고정, bible 0절): 유진 회색 `#9A9EA3`, 미란 버건디 `#7A1E2E`, 세라 민트 `#7FD1BE`, 하린 하늘색 `#9CC7E8`, 혜숙 금색 `#C9A45C`. 배경에서는 각 여자의 공간에 그 색을 **소품 한두 개**로만 숨긴다. 벽 전체를 그 색으로 칠하지 않는다*.

### 공통 스타일 문구

```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.
```

### 장소 목록

| 번호 | 장소 | 주 등장 회차 | 관능 장면 |
|---|---|---|---|
| 1 | 101동 3801호 펜트하우스(거실 통창, 침실, 아일랜드 식탁, 현관) | 1·3·4·5·6화 | 있음(1화 유진의 밤) |
| 2 | 상가 1층 와인바 '미란'(홀, 카운터, 셀러, 칠판) | 2·3·4·5·6화 | 있음(2·5화 미란) |
| 3 | 더퍼스트 클럽 B1 필라테스룸·안내데스크 | 2·3·4·5화 | 있음(2화 세라) |
| 4 | 412동 502호 하린의 전세방 | 3·4·5·6화 | 있음(3화 하린) |
| 5 | 503동 2402호 혜숙의 거실·안방(+24층 엘리베이터 홀) | 1·2·3·4·5·6화 | 있음(1화 혜숙, 5화 절제) |
| 6 | 물결놀이터(바닥분수, 벤치, 호수공원) | 3·4화 | 없음(아이들) |
| 7 | 더퍼스트 클럽 사우나 세신실·열탕 | 1·2·5화 | 없음(노출 공간) |
| 8 | 지하 2층 주차장 B구역·동 연결통로·엘리베이터 홀 | 1·2·3·4·6화 | 없음 |
| 9 | 수원지방법원 형사법정 | 6화 | 없음 |
| 10 | 새솔신도시 '그랑블루 레이크' 모델하우스 | 6화(에필로그) | 없음 |
| 짧게 A | 304동 1204호 미란의 집 | 4·6화 | 없음 |
| 짧게 B | 207동 803호 세라의 집 | 5·6화 | 있음(5화 세라) |
| 짧게 C | 관리사무소 지하 방재실 | 5화 | 없음 |

단지 전체에서 각 장소가 어디 있는지는 맨 끝 **'단지 전체 배치'** 절에 있다.

---

## 1. 101동 3801호 펜트하우스 — 유진의 집

### 1-1. 공간 개요

- **위치**: 101동 38층, 최상층 펜트하우스. 전세이고 보증금은 유진의 친정 돈이다(SPEC, bible).
- **평형**: 공급 약 56평(전용 145㎡), 단층*.
- **창 방향**
  - 거실 통창은 **남향**이다. 호수는 남남동 아래로 내려다보인다*.
  - 안방은 세대의 **남동 모서리**에 있어 남쪽과 동쪽 두 면이 통창이다*.
  - 근거: 오후 두 시 반 가을볕이 비스듬히 든다(3화). 새벽 다섯 시 사십 분, 통창 너머 새벽이 푸르다(1화). 밤에 침실 통창으로 호수 위 가로등 불빛과 고속도로 불빛이 보인다(1화). 위 방향은 이 세 문장을 동시에 만족하도록 정했다*.
- **등장 근거**
  - 1화 S#2 침실(새벽 5:40), S#3 부엌과 식탁(아침 7:00), S#6~8 침실·통창·침대(밤 10:30~10:50)
  - 3화 S#8 현관·식탁(저녁 6:50), S#13 거실·현관·드레스룸(오후 2:30)
  - 4화 S#4 회상 통창(밤 10:30), S#6 거실(밤 11:10)
  - 5화 S#5 거실·아일랜드 식탁·소파(밤 9:30)
  - 6화 S#8 현관(저녁 7:13)

### 1-2. 평면 배치

**전체 구조**: 현관은 세대 북쪽 가운데에 있다*. 현관 → 유리 중문 → 남북으로 6m 복도 → 남쪽의 거실·주방이 한 공간으로 트여 있다*. 복도 동쪽에 지호 방과 공용 욕실, 복도 끝 남동쪽에 안방이 있다*. 바닥은 현관부터 안방까지 같은 흰 대리석이다(1화 "맨발로 대리석을 건넜다").

**현관** (현관문을 등지고 남쪽을 볼 때, 시계방향)
1. 왼쪽(동) 벽: 천장까지 닿는 흰 무광 신발장*. 가운데 니치 선반에 화이트머스크 리드 디퓨저가 있다(디퓨저 냄새는 1화, 위치는*).
2. 정면: 슬림 프레임 유리 중문 3연동*. 중문 너머 복도 끝으로 거실 통창의 빛이 보인다*.
3. 오른쪽(서) 벽: 전신 거울과 벤치형 수납*.
4. 등 뒤: 현관문. 문 위 천장에 센서 다운라이트*(6화 S#8 조명).

**복도**: 동쪽 벽에 지호 방 문(가습기, 4화), 공용 욕실 문(샤워 소리, 4화 S#6)*. 서쪽 벽에 팬트리 문*. 복도가 거실로 열리는 모서리 기둥에 거실 조명 스위치가 있다(4화 S#6 "거실 조명 스위치로 가던 손", 위치는*).

**거실·주방** (복도 끝에 서서 남쪽을 볼 때, 시계방향)
1. 왼쪽(동) 벽: 안방과 맞닿은 벽이다*. 벽걸이 TV와 낮은 화이트 오크 거실장*.
2. 정면(남): 바닥부터 천장까지 통창. 폭 약 9m, 높이 2.6m, 가는 검정 세로 멀리언으로 다섯 칸*. 하부에 높이 10cm 대리석 창턱*. 창 앞 동쪽 끝에 공기청정기 한 대(소리는 1화, 위치는*).
3. 가운데: 회색 패브릭 3인 소파가 등받이를 서쪽 주방 쪽으로, 정면을 동쪽 TV 쪽으로 둔다*. 통창은 소파의 오른편이다*. 소파 앞에 낮은 원형 대리석 테이블*.
4. 오른쪽(서): 주방. 소파 등 뒤로 길이 2.4m 아일랜드 식탁(흰 세라믹 상판)이 남북으로 놓이고, 거실 쪽 면에 의자 넷*. 아일랜드 위에 둥근 펜던트 두 개*. 서쪽 벽은 'ㄱ'자 주방 가구와 인덕션, 북서쪽 끝에 빌트인 냉장고(냉장고 모터 소리는 1화, 위치는*).
5. 등 뒤(북): 복도 입구, 팬트리*.

**안방** (문은 안방의 북서쪽 모서리. 문을 등지고 남동쪽을 볼 때, 시계방향)
1. 왼쪽(북) 벽: 드레스룸 슬라이딩 도어와 안방 욕실 문*. 드레스룸 안에 전신 거울이 있다(3화 S#13 "드레스룸 거울 앞").
2. 정면 왼쪽(동): 통창 폭 4m*. 너머로 신도시 아파트 숲과 상가 거리의 야경*.
3. 정면(남): 통창 폭 4.5m*. 너머로 호수, 건너편 호숫가 산책로 가로등, 수평선 쪽으로 동서로 흐르는 고속도로 불빛(1화 "고속도로의 불빛", 배치는*). 남동 모서리는 기둥 없이 유리끼리 만난다*. 두 통창 아래 높이 10cm 대리석 창턱(1화 진주 귀걸이를 놓는 '창틀').
4. 오른쪽(서) 벽: 거실과 맞닿은 벽. 헤드보드를 이 벽에 붙인 킹 침대가 동쪽 통창을 향한다*. 양옆에 협탁과 낮은 스탠드*. 남쪽 통창 앞에서 침대 발치까지 다섯 걸음이다(1화 "침대까지는 다섯 걸음", 거리 환산은 약 3m*).
5. 크기: 약 5m × 4.5m*. 커튼은 천장 매입형 블라인드 박스에 말려 올라가 있어 통창 앞에 천이 없다*.

### 1-3. 시간대별 조명

| 회차·씬 | 시각 | 광원 | 색온도 | 방향 | 메모 |
|---|---|---|---|---|---|
| 1화 S#2 | 새벽 5:40 | 통창 밖 블루아워. 실내등 꺼짐 | 약 9000K | 동·남 통창에서 수평으로 | 호수가 회색 비단처럼(1화). 대리석에 푸른 반사* |
| 1화 S#3 | 아침 7:00 | 남동 저각 햇빛 + 아일랜드 펜던트 | 5200K / 3000K | 남동→북서 | 탄 버터 연기에 빛줄기가 생긴다* |
| 3화 S#13 | 오후 2:30 | 가을볕 | 4800K | 남남서에서 비스듬히. 대리석 위 긴 사다리꼴 | 호수 위 오리배 두 척(3화) |
| 1화 S#6~8, 4화 S#4 | 밤 10:30 | **실내등 0**. 통창 야경이 유일한 광원 | 보케 2700~4000K 혼합, 공기는 7000K 푸른 기 | 창에서 안쪽으로. 인물은 역광 실루엣 | 호수 위 가로등 불빛이 길게 흔들린다(1화) |
| 4화 S#6 | 밤 11:10 | 실내등 0. 바깥 불빛이 거실 바닥에 얇게 | 3500K 전후 | 남쪽 통창 | 식탁 위 마시지 않은 와인 한 잔(4화) |
| 5화 S#5 | 밤 9:30 | 아일랜드 펜던트 하나 + 통창 너머 호수공원 산책로 가로등 점선(5화) | 2700K | 위에서 아래, 창은 점선 보케 | 회색 실크가 펜던트 빛을 받는다* |
| 3화 S#8, 6화 S#8 | 저녁 6:50 / 7:13 | 현관 센서 다운라이트 | 3000K | 바로 위에서 아래 | 문이 열린 틈으로 엘리베이터 홀 빛* |

**대표 색**: `#1A1E3A` 밤 남색 · `#5B7598` 블루아워 · `#E9E6E1` 흰 대리석 · `#F2C26B` 금빛 보케 · `#9A9EA3` 유진 회색

### 1-4. 소리·냄새

- **소리**: 공기청정기가 숨 쉬듯 도는 소리(1화 S#2). 냉장고 모터(1화 S#6·8). 버터 타는 소리, 문을 들이받는 쾅(1화 S#3). 식기세척기 마지막 헹굼(3화 S#13). 지호 방 가습기 쌕쌕, 도어락, 샤워기 물소리(4화 S#6). 바지 주머니 진동 '징—'(1화 S#8).
- **냄새**: 현관의 화이트머스크 디퓨저와 그것에 섞이는 회색 병 머스크(1화). 샤워 직후의 습기와 재스민 바디오일(1화 밤). 섬유유연제와 남편 향수(3화). 탄 버터(1화).

### 1-5. 반복 소품과 위치

| 소품 | 위치 | 근거 |
|---|---|---|
| 진주 귀걸이 두 알 | 안방 남쪽 통창 대리석 창턱 | 1화 S#6 |
| 유진 휴대폰(잠금화면 가족사진) | 아일랜드 식탁 위 | 1화 S#3 |
| 유치원 가방과 이름표 | 아일랜드 식탁 위 의자 쪽 | 1화 S#3 |
| 마시지 않은 와인 한 잔 | 아일랜드 식탁 위 | 4화 S#6 |
| 그의 메인폰 | 아일랜드 식탁 위 | 4화 S#6 |
| 과일 바구니(녹음 중인 휴대폰을 숨김) | 아일랜드 식탁 거실 쪽 끝 | 5화 S#5, 끝 위치는* |
| 화이트머스크 디퓨저 | 현관 신발장 니치 | 1화, 위치는* |
| 공기청정기 | 거실 통창 앞 동쪽 끝 | 1화, 위치는* |
| 손바닥 자국 두 개, 동그란 김 자국 | 안방 남쪽 통창 유리 | 1화 S#8 |

### 1-6. 카메라 자리

| 자리 | 높이·방향 | 핵심 장면 |
|---|---|---|
| C1 안방 문가 | 눈높이 160cm, 남동쪽 모서리 통창을 대각선으로 | 1화 S#6 창가 대화, S#7 돌려 세우는 순간, 4화 S#4 회상 |
| C2 안방 남쪽 창턱 | 창턱 높이 30cm 로우 앵글, 유리에 바짝 붙여 야경 쪽 | 1화 S#6 창턱의 귀걸이 Insert, S#7 유리 위 김, S#8 F.I. 손바닥 자국 |
| C3 거실 남서쪽 모서리 | 허리 높이 110cm, 북동쪽으로. 아일랜드·소파·복도·현관 중문까지 깊이 | 1화 S#3 아침 식탁, 4화 S#6 밤 귀가, 5화 S#5 소파 |
| C4 현관 중문 앞 | 눈높이, 현관문 쪽. 열린 문 너머 엘리베이터 홀 | 3화 S#13 셔츠 깃 털기, 6화 S#8 "십 분 뒤에 다시 와요" |

### 1-7. 수위 장치 (1화 S#6~8, 4화 S#4 회상, 5화 S#5)

1. **역광 실루엣**: 실내등을 모두 끄고 통창 야경 하나로만 비춘다. 몸은 림라이트 윤곽으로만 보인다(대본 S#7 "실루엣").
2. **멀리언과 모서리 기둥선**: 통창의 검정 세로 창살과 남동 모서리 유리 이음선이 몸의 일부를 자르는 자리에 오도록 카메라를 놓는다*.
3. **유리 위 김과 손바닥 자국**: 행위 대신 유리를 보여 주고 컷을 넘긴다(S#7 Insert, S#8 F.I.).
4. **바닥에 고인 검은 실크, 시트에 파묻힌 시계**: 컷을 넘길 사물(S#7, S#8).
5. **야경 아웃포커스**: 절정은 화면 전체를 흐린 보케로 대신한다(S#8).
6. 5화 S#5: 아일랜드 위 **과일 바구니**를 전경에 크게 걸어 몸을 가리고, 동시에 녹음기라는 정보를 준다*.

### 1-8. SET LOCK (111 words)

```text
Penthouse unit 3801 on the 38th, top floor of a new 2024-built Korean high-rise apartment tower in a Gyeonggi new town. Polished white marble floor throughout, warm white walls, minimal luxury interior. The living room's south wall is one floor-to-ceiling glass wall about 9 m wide, five panes with slim black mullions and a low marble sill, overlooking a wide calm lake far below with a lit lakeside promenade and a distant highway on the horizon. Grey fabric sofa, white ceramic kitchen island with two round pendant lamps. Master bedroom in the southeast corner with frameless corner glass on two sides, a king bed against the inner wall facing the glass.
```

### 1-9. 프롬프트

**E1 빈 배경 — 밤 10:30 안방 야경** (1화 S#6~8)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Penthouse unit 3801 on the 38th, top floor of a new 2024-built Korean high-rise apartment tower in a Gyeonggi new town. Polished white marble floor throughout, warm white walls, minimal luxury interior. The living room's south wall is one floor-to-ceiling glass wall about 9 m wide, five panes with slim black mullions and a low marble sill, overlooking a wide calm lake far below with a lit lakeside promenade and a distant highway on the horizon. Grey fabric sofa, white ceramic kitchen island with two round pendant lamps. Master bedroom in the southeast corner with frameless corner glass on two sides, a king bed against the inner wall facing the glass.

Establishing view of the empty master bedroom at 10:30 pm. All interior lights are off; the only light is the city night view through the corner glass: warm gold and white bokeh, long streetlight reflections trembling on the black lake, a thin stream of highway lights on the horizon. Cool blue ambient light on the marble floor and the white bedding, the bed neatly made. Quiet, cold, expectant mood. Wide 16:9 composition. No logos, no watermark.
```

**E2 빈 배경 — 오후 2:30 거실 가을볕** (3화 S#13)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Penthouse unit 3801 on the 38th, top floor of a new 2024-built Korean high-rise apartment tower in a Gyeonggi new town. Polished white marble floor throughout, warm white walls, minimal luxury interior. The living room's south wall is one floor-to-ceiling glass wall about 9 m wide, five panes with slim black mullions and a low marble sill, overlooking a wide calm lake far below with a lit lakeside promenade and a distant highway on the horizon. Grey fabric sofa, white ceramic kitchen island with two round pendant lamps. Master bedroom in the southeast corner with frameless corner glass on two sides, a king bed against the inner wall facing the glass.

Establishing view of the empty living room and kitchen at 2:30 pm in late September. Slanting autumn sunlight from the south-southwest lays a long bright trapezoid across the white marble floor; fine dust floats in the light. Two tiny swan pedal boats drift on the lake far below. The kitchen island on the right, the hallway toward the front door at the back center. Calm, polished, slightly too perfect. Wide 16:9 composition. No logos, no watermark.
```

**C1 안방 문가 → 모서리 통창** (1화 S#6~7)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Penthouse unit 3801 on the 38th, top floor of a new 2024-built Korean high-rise apartment tower in a Gyeonggi new town. Polished white marble floor throughout, warm white walls, minimal luxury interior. The living room's south wall is one floor-to-ceiling glass wall about 9 m wide, five panes with slim black mullions and a low marble sill, overlooking a wide calm lake far below with a lit lakeside promenade and a distant highway on the horizon. Grey fabric sofa, white ceramic kitchen island with two round pendant lamps. Master bedroom in the southeast corner with frameless corner glass on two sides, a king bed against the inner wall facing the glass.

Camera at the bedroom doorway in the northwest corner, eye level, looking diagonally toward the southeast corner where the two glass walls meet. Night, interior lights off, the room lit only by the night view; the glass corner is a bright frame of bokeh, the king bed a dark shape on the right. Deep perspective so a figure standing at the glass would read as a silhouette. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C2 남쪽 창턱 로우 앵글** (1화 S#6 Insert, S#8 F.I.)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Penthouse unit 3801 on the 38th, top floor of a new 2024-built Korean high-rise apartment tower in a Gyeonggi new town. Polished white marble floor throughout, warm white walls, minimal luxury interior. The living room's south wall is one floor-to-ceiling glass wall about 9 m wide, five panes with slim black mullions and a low marble sill, overlooking a wide calm lake far below with a lit lakeside promenade and a distant highway on the horizon. Grey fabric sofa, white ceramic kitchen island with two round pendant lamps. Master bedroom in the southeast corner with frameless corner glass on two sides, a king bed against the inner wall facing the glass.

Extreme low angle at the marble window sill of the south glass wall in the master bedroom, camera almost touching the glass. Two small white pearl earrings lie on the sill in sharp focus. On the glass, two faint palm prints and a small round patch of breath fog slowly fading. Beyond, the lake and city lights blur into soft gold bokeh. Night, no interior lights. Vertical 9:16 webtoon panel, macro detail. No logos, no watermark.
```

**C3 거실 남서쪽 모서리 → 아일랜드·현관** (1화 S#3, 4화 S#6, 5화 S#5)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Penthouse unit 3801 on the 38th, top floor of a new 2024-built Korean high-rise apartment tower in a Gyeonggi new town. Polished white marble floor throughout, warm white walls, minimal luxury interior. The living room's south wall is one floor-to-ceiling glass wall about 9 m wide, five panes with slim black mullions and a low marble sill, overlooking a wide calm lake far below with a lit lakeside promenade and a distant highway on the horizon. Grey fabric sofa, white ceramic kitchen island with two round pendant lamps. Master bedroom in the southeast corner with frameless corner glass on two sides, a king bed against the inner wall facing the glass.

Camera in the southwest corner of the living room at waist height, looking northeast: the white kitchen island in the foreground with a fruit basket and a child's yellow kindergarten bag on it, the grey sofa beyond, and the long hallway leading to the glass entry door in the far background. Morning at 7 am, low southeast sun through the glass wall cutting warm beams through a faint haze of cooking smoke, the two pendants softly lit. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C4 현관 중문 앞 → 열린 현관문** (3화 S#13, 6화 S#8)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Penthouse unit 3801 on the 38th, top floor of a new 2024-built Korean high-rise apartment tower in a Gyeonggi new town. Polished white marble floor throughout, warm white walls, minimal luxury interior. The living room's south wall is one floor-to-ceiling glass wall about 9 m wide, five panes with slim black mullions and a low marble sill, overlooking a wide calm lake far below with a lit lakeside promenade and a distant highway on the horizon. Grey fabric sofa, white ceramic kitchen island with two round pendant lamps. Master bedroom in the southeast corner with frameless corner glass on two sides, a king bed against the inner wall facing the glass.

The entry hall seen from just inside the glass middle door, eye level, facing the open front door. Tall matte white shoe cabinet on the left with a small reed diffuser in a niche, full-length mirror on the right, white marble floor. Through the half-open front door, a bright elevator lobby with grey stone walls. Evening around 7 pm, a single warm sensor downlight above the doorway. Vertical 9:16 webtoon panel. No logos, no watermark.
```

### 1-10. 고증 메모

- 2024년 무렵 입주한 수도권 신축 대단지는 지하주차장이 각 동 엘리베이터와 바로 이어진다. 그래서 그가 1층 로비를 거치지 않고 B2에서 38층으로 바로 올라간다(1화).
- 최상층 '펜트하우스(PH)' 타입은 일반 평형보다 넓고 창이 크다. 테라스가 딸린 경우가 많지만, 소설에 테라스가 나오지 않으므로 그리지 않는다. 추측입니다: 테라스 유무와 면적은 단지마다 다르다.
- 현관 중문, 팬트리, 드레스룸, 빌트인 냉장고는 2020년대 신축의 흔한 사양이다. 추측입니다: 상당수는 유상 옵션이다.
- 소설의 '대리석 바닥'은 그대로 그린다. 추측입니다: 실제 신축 고급 평형에는 대형 포셀린 타일을 대리석처럼 쓰는 경우가 많다. 작화에서는 둘을 구분하지 않아도 된다.
- 커튼을 천장 매입 박스에 숨기는 마감은 신축에서 흔하다. 추측입니다.

---

## 2. 와인바 '미란' — 퍼스트 애비뉴 1층

### 2-1. 공간 개요

- **위치**: 단지 상가 '퍼스트 애비뉴' 1층. 빨간 간판이다(3화). 상가는 단지 동쪽 대로변에 있다(맨 끝 '단지 전체 배치')*.
- **크기**: 전용 약 83㎡(25평), 전면 폭 7m × 깊이 12m*. 층고 3.6m*.
- **창 방향**: 전면 통유리는 남동향*. 오전 열 시에 블라인드 틈으로 햇빛이 카운터 위에 흰 줄을 긋는다(5화). 그 문장에 맞춘 방향이다*.
- **문 두 개**
  - 정문: 전면 원목 문. 문에 종이 달려 있고 'CLOSED' 팻말을 건다(4·6화).
  - 뒷문: 안쪽 벽 스틸 문. 상가 내부 서비스 복도로 이어지고(2화 "뒷문이 열렸다"), 그 복도 끝 계단이 지하 2층 '상가 쪽 통로'와 이어진다(6화 동선은 bible 3-2, 계단 구조는*).
  - 6화에는 뒷문을 안에서 잠가 두었다. 그래서 그가 상가 공용 홀을 돌아 정문 종을 울리며 들어온다*.
- **등장 근거**
  - 2화 S#3~6(새벽 1:20~2:20)
  - 3화 S#9(저녁 7:30, 오픈 30분 전)
  - 4화 S#3 회상, S#16~18(밤 11:00~11:40)
  - 5화 S#1(오전 10:00), S#3 몽타주(카운터의 미란), S#6~7(새벽 1:10)
  - 6화 S#10~12(저녁 7:22~7:41)

### 2-2. 평면 배치

**정문** (정문을 등지고 북서쪽 안쪽을 볼 때, 시계방향). 정문은 전면의 가운데에서 조금 왼쪽에 있다*.
1. 왼쪽 앞 구석: 2인용 둥근 대리석 테이블 하나. 6화 형사 둘이 탄산수를 두고 앉는 '구석 테이블'이다(6화, 위치는*).
2. 왼쪽 벽 가운데: 버건디 벨벳 3인 소파(팔걸이가 있는 체스터필드형)와 낮은 원목 테이블(2화 S#6 "벨벳 소파", 형태는*). 소파 위 벽에 와인 라벨 액자 셋*.
3. 왼쪽 벽 안쪽: 키 큰 유리문 와인 셀러 두 대. 컴프레서 소리가 난다(4·5·6화). 셀러 옆 바닥에 오크 와인 상자 서너 개가 쌓여 있다(5화 "빈 와인 상자", 개수는*).
4. 안쪽 벽: 왼쪽에 화장실 문*, 오른쪽 끝(카운터 안쪽)에 스틸 뒷문*.
5. 오른쪽 벽: 길이 6m의 일자 원목 바 카운터가 벽에서 1.2m 떨어져 평행하게 놓인다*.
   - 손님 쪽에 바 스툴 여섯 개(5화 "스툴 하나가 넘어가는", 개수는*).
   - 카운터 안쪽 벽에 백바 선반, 그 가운데에 가로 1.8m 칠판 메뉴판(4화 "카운터 뒤 칠판 메뉴판", 크기는*).
   - 카운터 하부 안쪽 끝, 뒷문 가까이에 식기세척기(2·5화, 위치는*). 백바 위쪽 모서리에 블루투스 스피커(2화 재즈, 위치는*).
   - 카운터 위 천장: 잔을 거꾸로 거는 스템웨어 랙(2화)과 붉은 유리 갓 펜던트 **다섯 개**. 4화에는 다섯 개를 다 켜고, 2·5화 마감 후에는 가운데 세 개만 켠다(소설의 '세 개'와 '다섯 개'를 함께 만족하는 설정*).
   - 카운터 끝, 정문 쪽 상판 위에 리모델링 견적서(2화).
6. 등 뒤(전면): 통유리 두 칸과 원목 루버 블라인드(4화 끝까지 내림, 5화 반쯤, 재질은*). 처마 위 빨간 간판(3화).

**바닥**: 짙은 버건디와 흑갈색 헥사곤 타일(5화 "스툴 다리가 타일을 긁었다", 무늬는*).

### 2-3. 시간대별 조명

| 회차·씬 | 시각 | 광원 | 색온도 | 방향 | 메모 |
|---|---|---|---|---|---|
| 2화 S#3~6 | 새벽 1:20~2:20 | 간판 꺼짐. 펜던트 가운데 세 개만 붉게 + 셀러 안 LED | 붉은 유리 갓 빛(약 1800K 상당), 셀러 4000K | 위에서 아래로 좁은 원뿔. 원뿔 밖은 어둠 | 식기세척기 표시등 초록 점* |
| 3화 S#9 | 저녁 7:30 | 펜던트 다섯 + 백바 간접등 | 2700K | 위에서, 백바는 아래에서 위로 | 오픈 30분 전. 블라인드 반, 바깥 저녁 푸른빛* |
| 4화 S#16~18 | 밤 11:00 | 블라인드 끝까지. 펜던트 다섯 개 | 붉은 빛 | 카운터 위 일렬 | 칠판은 펜던트 끝 하나의 빛만 받는다* |
| 5화 S#1 | 오전 10:00 | 실내등 꺼짐. 블라인드 틈 햇빛 | 5500K | 남동 전면에서 카운터 쪽으로 흰 줄 여러 개 | 카운터 위 A4 다섯 장과 형광펜(5화) |
| 5화 S#6~7 | 새벽 1:10 | 펜던트 가운데 세 개 + 셀러 LED | 붉은 빛 / 4000K | 위에서 | 펜던트 하나가 출렁인다(5화 S#7) |
| 6화 S#10~12 | 저녁 7:22~7:41 | 펜던트 다섯 + 케이크 초 다섯 개 | 붉은 빛 + 촛불 1900K | 위에서 + 카운터 가운데 아래에서 | 재즈 꺼짐. 블라인드 끝까지* |

**대표 색**: `#7A1E2E` 버건디 · `#B3262E` 붉은 펜던트 빛 · `#3B2416` 흑갈 원목 · `#B8893B` 놋쇠 · `#2F3A33` 칠판

### 2-4. 소리·냄새

- **소리**: 식기세척기 웅웅, 사이클 끝 '삐, 삐, 삐'(2화). 볼륨을 반쯤 줄인 재즈 트럼펫(2화). 랙의 잔이 '쨍, 쨍' 울리다 '쨍그랑'(2화). 코르크 '퐁'(2·4화). 셀러 컴프레서(4·5·6화). 셀러 안 병들이 짤랑(5화). 스툴 다리가 타일을 긁는 소리(5화). 문 종(6화). 커터칼 '사각'(6화). 의자 끄는 소리(6화).
- **냄새**: 엎질러진 말벡, 레몬 세정제, 젖은 코르크(2화). 오크와 코르크, 방금 딴 레드 와인(4화). 어젯밤 흘린 카베르네와 락스(5화 오전). 오크통과 식은 치즈(5화 새벽). 촛농과 디캔터 속 보르도(6화). 6화에는 그가 다섯 향을 한꺼번에 묻혀 들어온다.

### 2-5. 반복 소품과 위치

| 소품 | 위치 | 근거 |
|---|---|---|
| 리모델링 견적서(3,200만 원) | 카운터 정문 쪽 끝 | 2화 |
| 거꾸로 걸린 잔 | 카운터 위 랙 | 2화 |
| 와인 오프너, 잔 두 개 | 카운터 가운데 | 2·4화 |
| 코스터 다섯 장 | 카운터 위 일렬 | 4화 S#16 |
| 칠판 장부(분필) | 카운터 뒤 칠판 | 4화 S#17 |
| 작은 진주 귀걸이 두 알 | 카운터 위 | 4화 S#18, 6화 S#11 |
| A4 다섯 장, 형광펜 다섯 자루 | 카운터 위 | 5화 S#1 |
| 빈 와인 상자 속 휴대폰 | 셀러 옆, 보르도 병들 사이 | 5화 S#6 |
| 케이크와 초 다섯 개, 디캔터 | 카운터 한가운데 | 6화 S#10 |
| 소품용 돈다발 부채꼴, 열린 쇼핑백 | 카운터, 띠지가 문 쪽을 본다 | 6화 S#10 |
| 탄산수 두 잔 | 구석 테이블 | 6화 S#10 |
| 향수병 다섯 개, 휴대폰 두 대 | 카운터 위 일렬 | 6화 S#12 |

### 2-6. 카메라 자리

| 자리 | 높이·방향 | 핵심 장면 |
|---|---|---|
| C1 정문 안쪽 | 눈높이, 북서쪽 안으로. 카운터가 오른쪽, 소파·셀러가 왼쪽으로 깊어진다 | 6화 S#11 문간에서 본 라인업, 4화 S#16 와이드 |
| C2 카운터 안쪽(바텐더 자리) | 눈높이, 칠판을 등지고 손님 쪽 | 4화 S#16 코스터 다섯 장과 다섯 얼굴, 2화 S#4 |
| C3 카운터 뒷문 쪽 끝 | 상판 높이 로우 앵글, 상판을 따라 정문 쪽으로 | 2화 S#5 잔 울림 Insert, 5화 S#7 잔이 밀려가다 멈춤 |
| C4 벨벳 소파 옆 | 앉은 눈높이, 카운터 너머 칠판 쪽 | 4화 S#17 칠판 장부, 2화 S#6 잠든 그 |

### 2-7. 수위 장치 (2화 S#5, 4화 S#3 회상, 5화 S#7)

1. **랙의 거꾸로 걸린 잔**: 전경에 흐리게 걸어 상반신을 가린다. 동시에 잔 울림이 리듬을 대신한다(2화 S#5).
2. **붉은 펜던트의 좁은 빛 원뿔**: 빛 안은 어깨·쇄골·등만, 원뿔 밖은 완전한 어둠(대본 S#5 "실루엣 위주").
3. **카운터 상판 높이**: C2·C3에서 상판이 하반신을 자른다*.
4. **컷을 넘길 사물**: 바닥에 떨어진 앞치마, 깨진 잔(2화), 넘어진 스툴, 카운터 끝까지 밀려간 잔, 출렁이는 펜던트(5화).
5. **셀러 유리문 반사**: 5화 S#7은 셀러 유리에 비친 흐린 붉은 형체로 처리한다*.

### 2-8. SET LOCK (110 words)

```text
Small Korean wine bar called Miran on the ground floor of a new apartment complex shopping street, about 7 m wide and 12 m deep. A dark walnut bar counter 6 m long runs along the right wall with six bar stools, an overhead rack of upside-down wine glasses, and five red glass pendant lamps in a row above it. Behind the counter, a back-bar shelf with a blank chalkboard menu. Along the left wall: a small round marble corner table near the front, a burgundy velvet Chesterfield sofa, and two tall glass-door wine cellars at the back. Dark burgundy hexagon floor tiles, wooden louver blinds on the front glass.
```

### 2-9. 프롬프트

**E1 빈 배경 — 새벽 1:20 마감 후 붉은 조명** (2화 S#3)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Small Korean wine bar called Miran on the ground floor of a new apartment complex shopping street, about 7 m wide and 12 m deep. A dark walnut bar counter 6 m long runs along the right wall with six bar stools, an overhead rack of upside-down wine glasses, and five red glass pendant lamps in a row above it. Behind the counter, a back-bar shelf with a blank chalkboard menu. Along the left wall: a small round marble corner table near the front, a burgundy velvet Chesterfield sofa, and two tall glass-door wine cellars at the back. Dark burgundy hexagon floor tiles, wooden louver blinds on the front glass.

Establishing view of the closed, empty bar at 1:20 am. Sign off, blinds down, only the middle three red pendants glowing over the counter, casting narrow red cones on the wood; everything outside the cones falls into deep shadow. Cool white light inside the wine cellars, a tiny green indicator light under the counter. Clean glasses hang upside down in the rack, a corkscrew and two wine glasses on the counter. Intimate, late, hushed. Wide 16:9 composition. No logos, no watermark.
```

**E2 빈 배경 — 오전 10:00 블라인드 틈 햇빛** (5화 S#1)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Small Korean wine bar called Miran on the ground floor of a new apartment complex shopping street, about 7 m wide and 12 m deep. A dark walnut bar counter 6 m long runs along the right wall with six bar stools, an overhead rack of upside-down wine glasses, and five red glass pendant lamps in a row above it. Behind the counter, a back-bar shelf with a blank chalkboard menu. Along the left wall: a small round marble corner table near the front, a burgundy velvet Chesterfield sofa, and two tall glass-door wine cellars at the back. Dark burgundy hexagon floor tiles, wooden louver blinds on the front glass.

Establishing view of the empty bar at 10 am. All interior lights off; the louver blinds are half down and morning sun from the southeast slips through the slats, drawing several sharp white stripes across the counter and the hexagon tiles. On the counter, five sheets of white paper laid side by side and five highlighter pens. Dust in the light, stools pushed in. Fresh, sober, plotting mood. Wide 16:9 composition. No logos, no watermark.
```

**C1 정문 안쪽 → 카운터 라인** (6화 S#11, 4화 S#16)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Small Korean wine bar called Miran on the ground floor of a new apartment complex shopping street, about 7 m wide and 12 m deep. A dark walnut bar counter 6 m long runs along the right wall with six bar stools, an overhead rack of upside-down wine glasses, and five red glass pendant lamps in a row above it. Behind the counter, a back-bar shelf with a blank chalkboard menu. Along the left wall: a small round marble corner table near the front, a burgundy velvet Chesterfield sofa, and two tall glass-door wine cellars at the back. Dark burgundy hexagon floor tiles, wooden louver blinds on the front glass.

Camera just inside the front door at eye level, looking deep into the bar: the long counter on the right receding toward the back door, the velvet sofa and glowing wine cellars on the left, the round corner table with two glasses of sparkling water in the left foreground. Evening, all five red pendants on; on the counter a birthday cake with five lit candles, a decanter, and a fan of banded cash bundles. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C2 카운터 안쪽 → 손님 쪽** (4화 S#16, 2화 S#4)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Small Korean wine bar called Miran on the ground floor of a new apartment complex shopping street, about 7 m wide and 12 m deep. A dark walnut bar counter 6 m long runs along the right wall with six bar stools, an overhead rack of upside-down wine glasses, and five red glass pendant lamps in a row above it. Behind the counter, a back-bar shelf with a blank chalkboard menu. Along the left wall: a small round marble corner table near the front, a burgundy velvet Chesterfield sofa, and two tall glass-door wine cellars at the back. Dark burgundy hexagon floor tiles, wooden louver blinds on the front glass.

Camera behind the counter at the bartender's position, eye level, the blank chalkboard behind the camera, looking out over the counter toward the stools, the sofa and the front glass. Five face-down round coasters and five ballpoint pens lie in a row on the counter top, an uncorked bottle of red wine beside them. Night, blinds fully down, five red pendants. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C3 카운터 끝 상판 로우 앵글** (2화 S#5, 5화 S#7)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Small Korean wine bar called Miran on the ground floor of a new apartment complex shopping street, about 7 m wide and 12 m deep. A dark walnut bar counter 6 m long runs along the right wall with six bar stools, an overhead rack of upside-down wine glasses, and five red glass pendant lamps in a row above it. Behind the counter, a back-bar shelf with a blank chalkboard menu. Along the left wall: a small round marble corner table near the front, a burgundy velvet Chesterfield sofa, and two tall glass-door wine cellars at the back. Dark burgundy hexagon floor tiles, wooden louver blinds on the front glass.

Extreme low angle from the back end of the bar counter, lens resting on the walnut top, looking along the whole length of the counter toward the front door. The upside-down glasses in the overhead rack fill the top of the frame, catching red pendant light; one glass sits at the very edge of the counter about to fall. Deep shadow beyond the red cones, a knocked-over bar stool lying on the tiles. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C4 벨벳 소파 옆 → 칠판** (4화 S#17, 2화 S#6)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Small Korean wine bar called Miran on the ground floor of a new apartment complex shopping street, about 7 m wide and 12 m deep. A dark walnut bar counter 6 m long runs along the right wall with six bar stools, an overhead rack of upside-down wine glasses, and five red glass pendant lamps in a row above it. Behind the counter, a back-bar shelf with a blank chalkboard menu. Along the left wall: a small round marble corner table near the front, a burgundy velvet Chesterfield sofa, and two tall glass-door wine cellars at the back. Dark burgundy hexagon floor tiles, wooden louver blinds on the front glass.

Camera beside the burgundy velvet sofa at seated eye level, looking across the bar counter to the back-bar chalkboard. The chalkboard is wiped half clean with smeared chalk dust and a broken piece of chalk on its ledge; the board surface itself is left blank. Red pendant light falls on the counter, the chalkboard lit only at one edge. Late night, blinds down. Vertical 9:16 webtoon panel. No logos, no watermark.
```

### 2-10. 고증 메모

- 2020년대 신축 대단지는 단지 바깥 도로변에 1~2층짜리 '스트리트형' 단지 내 상가를 두는 경우가 많다. 와인바가 1층 도로변에 간판을 내건 설정과 맞는다.
- 상가 주차장과 단지 지하주차장이 통로로 이어지는 단지도 있다. 그러나 보안 때문에 세대카드로 출입을 통제하는 경우가 많다. 작중 '상가 쪽 통로'(6화)는 이 구조를 썼다. 추측입니다: 실제로 연결하는 단지가 얼마나 흔한지는 확인하지 못했다.
- 새벽 1시 넘어 마감하는 바는 일반음식점·주점 영업으로 가능하다. 상가 관리규약으로 심야영업을 제한하는 경우도 있다. 추측입니다.
- 벽돌 대신 헥사곤 타일, 루버 블라인드, 붉은 유리 갓 펜던트는 2020년대 국내 소형 와인바의 흔한 인테리어 어휘다. 추측입니다.

---

## 3. 더퍼스트 클럽 지하 1층 — 필라테스룸·안내데스크

### 3-1. 공간 개요

- **위치**: 커뮤니티센터 '더퍼스트 클럽' 지하 1층. 같은 층에 사우나, 필라테스룸, 골프연습장, 키즈카페가 있다(SPEC).
- **필라테스룸 크기**: 약 20평(66㎡), 8m × 8.5m*. 층고 3m*. 지하라 창이 없다.
- **이웃 공간**: 필라테스룸 동쪽 벽은 여탕과 맞닿아 있다. 그래서 수증기 냄새가 새어 든다(3·4화 "옆 사우나", 벽 위치는*).
- **B2 연결**: 클럽 B1 복도 끝에 지하 2층 연결통로로 내려가는 계단 문이 있다. 문에 세대카드 리더가 있고, 태그하면 'B2 연결통로 출입'으로 기록된다(2·4화 기록, 계단 위치는*).
- **등장 근거**
  - 2화 S#7~10 필라테스룸(밤 10:10~10:58)
  - 3화 S#11 필라테스룸(밤 9:00), S#12 여자 탈의실 → 복도(밤 9:50)
  - 4화 S#10~12 필라테스룸(밤 9:30~9:45), S#11 회상
  - 5화 S#2 안내데스크(오전 7:02)

### 3-2. 평면 배치

**B1 전체** (엘리베이터·계단 홀에서 북쪽 게이트를 볼 때, 시계방향)*
1. 왼쪽: 유리벽 너머 골프연습장. 스크린 타석 다섯 개와 그물(5화 "유리벽 너머 골프연습장", 타석 수는*).
2. 정면: 스피드 게이트 세 레인(카드를 먹을 때 '삑', 5화, 레인 수는*). 게이트 오른쪽 안쪽에 안내데스크*.
3. 게이트를 지나면 남북으로 곧은 중앙 복도*.
   - 복도 왼쪽(서): 키즈카페, 여자 탈의실(피트니스·GX 공용)*.
   - 복도 오른쪽(동): 남탕 입구, 여탕 입구*. 여탕 입구 앞 복도가 1화 S#5⑤의 '사우나 입구 앞 복도'다.
   - 복도 끝(북): 필라테스룸 유리문*. 3화 S#12에서 탈의실을 나온 하린이 걸어가는 화면 깊숙이 이 유리문이 보인다.
   - 필라테스룸 유리문 오른쪽: B2 연결통로 계단 문(세대카드 리더)*.

**필라테스룸** (복도에서 들어오는 유리문은 남쪽 벽 오른쪽 끝. 문을 등지고 북쪽을 볼 때, 시계방향)
1. 왼쪽(서) 벽: **벽 전체가 거울**(3화). 폭 1.2m × 높이 2.4m 거울 여섯 장*. 2·4화의 "거울 벽이 두 사람을 여섯 번 비췄다"는 이 여섯 장이다. 거울 아래 바닥 경계에 간접 LED 라인(2화 "거울 벽 아래 깔린 간접조명").
2. 정면(북) 벽: 낮은 수납장 위에 소도구(링, 볼, 폼롤러)*. 선반 위 블루투스 스피커(3화, 위치는*). 벽 위쪽에 환기구 그릴 두 개(2화 "환기구에서 서늘한 바람", 개수는*).
3. 오른쪽(동) 벽: 여탕과 맞닿은 벽. 문 가까운 남동 모서리에 강사 데스크(모니터, 태블릿)(2화 S#7 데스크, 4화 S#10 태블릿, 위치는*). 데스크 옆에 스탠드 옷걸이(2화 S#8 체인 백이 걸린 옷걸이, 형태는*).
4. 등 뒤(남): 유리문과 유리 칸막이. 복도가 들여다보인다*.
5. 바닥: 리포머 **여섯 대**가 남북으로 한 줄(2화). 한 대 한 대는 동서로 길게 누워 풋바가 거울(서쪽) 쪽을 향한다*. 북쪽 끝이 3화의 '맨 끝 리포머'다*. 리포머 사이 간격 0.8m*.
6. 리포머: 오크 프레임, 차콜 캐리지, 빨간 스프링(2화 "빨간 스프링 두 개", 프레임 색은*).
7. 천장: 매입 다운라이트 두 줄과 남·북 벽 쪽 코브 간접등*. 바닥은 연한 오크 강마루, 리포머 아래 검정 고무 매트*.

**안내데스크** (5화 S#2): 게이트 오른쪽 L자 화이트 데스크*. 모니터 두 대, 하나가 게이트 출입 기록이다(5화). 데스크 뒤 벽에 클럽 이름 자리의 무광 금속판(글자 없음)*. 데스크 맞은편이 골프연습장 유리벽이다*.

### 3-3. 시간대별 조명

| 회차·씬 | 시각 | 광원 | 색온도 | 방향 | 메모 |
|---|---|---|---|---|---|
| 2화 S#7~10 | 밤 10:10~10:58 | 천장 꺼짐. 거울 아래 간접 LED만 | 4000K | 바닥에서 낮게, 거울에 반사되어 두 배 | 데스크 모니터의 푸른빛*, 문 위 비상구 유도등 초록* |
| 3화 S#11 | 밤 9:00 | 천장 다운라이트 절반 | 4000K | 위에서 | 거울에 리포머 줄이 반복된다 |
| 4화 S#10~12 | 밤 9:30 | 불 하나(거울 쪽 다운라이트 한 줄)* | 4000K | 위에서 한 줄 | 일요일, 클럽은 일찍 닫았다(4화) |
| 5화 S#2 | 오전 7:02 | 안내데스크 전체 조명 + 골프 스크린 | 5000K, 스크린은 초록·하늘 | 위에서 + 유리벽 너머 옆에서 | 첫 공이 그물을 때린다(5화) |

**대표 색**: `#EEF3F2` 차가운 흰 벽 · `#9FB3B8` 거울 슬레이트 · `#C8A77E` 오크 · `#2B2F33` 차콜 캐리지 · `#C8323A` 빨간 스프링

### 3-4. 소리·냄새

- **소리**: 환기구 바람(2화). 스프링 '철컥'(2·3·4화). 캐리지 '끼익, 탁'과 스토퍼 '탁'(2화). 블루투스 스피커의 물소리 음악(3화). 유리문 열리는 소리(3화 S#12). 게이트 '삑', 골프공이 그물을 때리는 소리(5화).
- **냄새**: 고무 매트, 유칼립투스 소독 스프레이, 마지막 수업 회원들의 땀(2화). 옆 사우나에서 새어 든 수증기(3·4화). 고무 매트와 소독약(5화). 2화에는 그보다 민트 향이 먼저 들어온다.

### 3-5. 반복 소품과 위치

| 소품 | 위치 | 근거 |
|---|---|---|
| 빨간 스프링 두 개 | 리포머 캐리지 아래 | 2화 S#9 |
| 소독 스프레이와 마른 수건 | 리포머 레일 위 | 2화 S#7, 수건은* |
| 출입 기록 모니터 | 강사 데스크 | 2화 S#7·10 |
| 태블릿 | 강사 데스크 | 4화 S#10 |
| 로고 없는 퀼팅 체인 백 | 데스크 옆 옷걸이 | 2화 S#8 |
| 요가 매트(스트레칭) | 거울 앞 바닥 | 2화 S#10, 4화 S#10 |
| 게이트 출입 기록 모니터 | 안내데스크 | 5화 S#2 |

### 3-6. 카메라 자리

| 자리 | 높이·방향 | 핵심 장면 |
|---|---|---|
| C1 남동 모서리(데스크 옆) | 눈높이, 북서쪽으로. 리포머 줄과 거울 여섯 장을 대각선으로 | 2화 S#9 와이드 "여섯 개", S#10 무표정 여섯, 3화 S#11 |
| C2 거울 앞 바닥 | 바닥 높이 로우 앵글, 리포머 레일을 따라 동쪽 | 2화 S#9 캐리지·스프링·스토퍼 Insert, 4화 S#11 회상 |
| C3 강사 데스크 뒤 | 앉은 눈높이, 모니터 너머 유리문과 복도 | 2화 S#7·10 출입 기록, 4화 S#10 유리문을 여는 두 사람, 3화 S#12 복도 끝 유리문 |
| C4 안내데스크 | 눈높이, 데스크 안쪽에서 게이트와 골프 유리벽 | 5화 S#2 |

### 3-7. 수위 장치 (2화 S#9, 4화 S#11 회상)

1. **거울 여섯 장의 이음매**: 몸이 거울과 거울 사이 세로 이음선에 걸리게 구도를 잡는다*.
2. **간접조명 하나**: 빛은 바닥에서 낮게만 온다. 측면 실루엣으로 굴곡만 남긴다(대본 S#9 "측면 실루엣").
3. **리포머 구조물 전경**: 풋바, 스프링, 캐리지 받침대를 화면 앞에 크게 걸어 가린다*.
4. **컷을 넘길 사물**: 레일 위를 미끄러지는 캐리지, 늘어난 스프링, 스토퍼 '탁'(2화).
5. **걸린 체인 백·수건**: 옷걸이의 가방과 수건을 전경에 둔다*.

### 3-8. SET LOCK (107 words)

```text
Basement pilates studio in the community center of a new Korean apartment complex, about 8 by 8.5 meters, no windows. The left wall is a full mirror wall of six tall panels with a thin LED light strip along the floor beneath it. Six oak-frame pilates reformers with charcoal carriages and red springs stand in one row, foot bars toward the mirror. Light oak flooring with black rubber mats, recessed ceiling downlights, two ventilation grilles high on the back wall. A glass door and glass partition on the near wall, a small instructor desk with a monitor and a coat stand in the corner by the door.
```

### 3-9. 프롬프트

**E1 빈 배경 — 밤 10:10 마감 후 간접조명** (2화 S#7)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Basement pilates studio in the community center of a new Korean apartment complex, about 8 by 8.5 meters, no windows. The left wall is a full mirror wall of six tall panels with a thin LED light strip along the floor beneath it. Six oak-frame pilates reformers with charcoal carriages and red springs stand in one row, foot bars toward the mirror. Light oak flooring with black rubber mats, recessed ceiling downlights, two ventilation grilles high on the back wall. A glass door and glass partition on the near wall, a small instructor desk with a monitor and a coat stand in the corner by the door.

Establishing view of the empty studio after closing at 10:10 pm. Ceiling lights off; only the LED strip under the mirror wall washes the floor in a low cool white glow, doubled by the reflections, the six reformers casting long soft shadows. The desk monitor glows faint blue in the near corner, a small green exit sign above the glass door. A spray bottle and a folded towel on the nearest reformer rail. Cool, silent, intimate emptiness. Wide 16:9 composition. No logos, no watermark.
```

**E2 빈 배경 — 밤 9:00 수업 중 조명** (3화 S#11)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Basement pilates studio in the community center of a new Korean apartment complex, about 8 by 8.5 meters, no windows. The left wall is a full mirror wall of six tall panels with a thin LED light strip along the floor beneath it. Six oak-frame pilates reformers with charcoal carriages and red springs stand in one row, foot bars toward the mirror. Light oak flooring with black rubber mats, recessed ceiling downlights, two ventilation grilles high on the back wall. A glass door and glass partition on the near wall, a small instructor desk with a monitor and a coat stand in the corner by the door.

Establishing view of the same studio at 9 pm during an evening class, but with no people: ceiling downlights at half brightness, even cool light, the mirror wall repeating the row of six reformers into a long rhythm. Small props neatly stacked on the low back shelf, a speaker on the shelf. Clean, disciplined, airy for a basement. Wide 16:9 composition. No logos, no watermark.
```

**C1 남동 모서리 → 거울 벽 대각선** (2화 S#9~10)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Basement pilates studio in the community center of a new Korean apartment complex, about 8 by 8.5 meters, no windows. The left wall is a full mirror wall of six tall panels with a thin LED light strip along the floor beneath it. Six oak-frame pilates reformers with charcoal carriages and red springs stand in one row, foot bars toward the mirror. Light oak flooring with black rubber mats, recessed ceiling downlights, two ventilation grilles high on the back wall. A glass door and glass partition on the near wall, a small instructor desk with a monitor and a coat stand in the corner by the door.

Camera in the southeast corner beside the instructor desk, eye level, looking diagonally northwest across the row of reformers to the mirror wall. The six mirror panels reflect the reformers again and again, each panel separated by a thin vertical seam. Night, only the low LED strip under the mirror lit, the carriages dark and glossy. Wide 16:9 composition. No logos, no watermark.
```

**C2 거울 앞 바닥 로우 앵글** (2화 S#9 Insert)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Basement pilates studio in the community center of a new Korean apartment complex, about 8 by 8.5 meters, no windows. The left wall is a full mirror wall of six tall panels with a thin LED light strip along the floor beneath it. Six oak-frame pilates reformers with charcoal carriages and red springs stand in one row, foot bars toward the mirror. Light oak flooring with black rubber mats, recessed ceiling downlights, two ventilation grilles high on the back wall. A glass door and glass partition on the near wall, a small instructor desk with a monitor and a coat stand in the corner by the door.

Floor-level low angle at the foot of one reformer near the mirror, looking along its metal rails toward the carriage. Two red springs hooked under the carriage, stretched; the padded foot bar huge and blurred in the foreground; the rubber stopper at the end of the rail in sharp focus. Low LED glow from the floor strip, the mirror behind doubling the rails. Vertical 9:16 webtoon panel, mechanical close-up. No logos, no watermark.
```

**C3 강사 데스크 뒤 → 유리문** (2화 S#7·10, 4화 S#10, 3화 S#12)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Basement pilates studio in the community center of a new Korean apartment complex, about 8 by 8.5 meters, no windows. The left wall is a full mirror wall of six tall panels with a thin LED light strip along the floor beneath it. Six oak-frame pilates reformers with charcoal carriages and red springs stand in one row, foot bars toward the mirror. Light oak flooring with black rubber mats, recessed ceiling downlights, two ventilation grilles high on the back wall. A glass door and glass partition on the near wall, a small instructor desk with a monitor and a coat stand in the corner by the door.

Camera behind the instructor desk at seated eye level, the monitor's blank glowing screen in the blurred foreground, a coat stand with a quilted chain shoulder bag without logos at the edge of frame. Through the glass door, the long bright corridor of the community center basement stretches away, its far end lit. Studio side dark, corridor side bright. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C4 안내데스크 → 게이트·골프 유리벽** (5화 S#2)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Basement pilates studio in the community center of a new Korean apartment complex, about 8 by 8.5 meters, no windows. The left wall is a full mirror wall of six tall panels with a thin LED light strip along the floor beneath it. Six oak-frame pilates reformers with charcoal carriages and red springs stand in one row, foot bars toward the mirror. Light oak flooring with black rubber mats, recessed ceiling downlights, two ventilation grilles high on the back wall. A glass door and glass partition on the near wall, a small instructor desk with a monitor and a coat stand in the corner by the door.

Different area on the same basement floor: the community center reception at 7 am. A white L-shaped reception desk with two monitors turned toward the camera side, three glass speed gates for card entry, and across from the desk a glass wall into an indoor golf practice room with five screen bays and green turf glowing. Bright even 5000K light, a plain brushed-metal plaque on the wall behind the desk. Vertical 9:16 webtoon panel. No logos, no watermark.
```

### 3-10. 고증 메모

- 2020년대 수도권 신축 대단지 커뮤니티센터는 피트니스, GX·필라테스룸, 실내 골프연습장, 사우나, 키즈카페, 독서실을 갖춘 경우가 많다. 입주민은 세대카드나 앱으로 게이트를 통과한다.
- 커뮤니티 운영은 위탁업체가 맡고 강사는 위탁업체 소속이나 프리랜서인 경우가 많다(bible 세라 1. 기본과 같다). 추측입니다: 강사가 출입 기록 화면까지 볼 수 있는지는 단지마다 다르다. 작중 설정으로 둔다.
- 필라테스룸을 지하에 두는 단지는 흔하다. 거울 벽과 리포머 6~10대가 일반적인 규모다. 추측입니다.
- 커뮤니티센터가 지하주차장과 바로 이어져 우천 시 지상으로 나가지 않는 동선은 신축 대단지의 흔한 홍보 포인트다.

---

## 4. 412동 502호 — 하린의 전세방

### 4-1. 공간 개요

- **위치**: 412동 5층, 전세(SPEC). 412동은 단지 남서쪽, 호수공원 서쪽 잔디 광장과 맞닿은 동이다(맨 끝 '단지 전체 배치')*.
- **평형**: 전용 39㎡(공급 약 17평) 1.5룸*. 현관 겸 주방, 방 하나, 작은 알파룸(옷·세탁), 욕실*.
- **창 방향**: 방 창은 남향*. 창밖 아래가 호수공원 잔디 광장이다(3화 "창밖 호수공원에서는 스프링클러", 방향은*). 저층이라 새벽 배달 오토바이와 청소차 후진음이 올라온다(3화).
- **5층 복도**: 계단식 코어. 엘리베이터 두 대와 비상계단 문, 한 층 네 세대*. 502호는 엘리베이터에서 나와 왼쪽 두 번째 문*. 복도에 센서등이 켜졌다 꺼진다(4화).
- **등장 근거**
  - 3화 S#1~3(새벽 1:50~2:20), S#4(새벽 4:50), S#5(새벽 5:30 → 오전 9:00)
  - 4화 S#13~15(밤 8:00~8:10), S#14 회상
  - 5화 S#3 몽타주(책상 스탠드 아래), S#12·14(밤 9:00~9:21), S#13 5층 복도와 계단
  - 6화 S#7 현관(저녁 7:05)

### 4-2. 평면 배치

**현관** (현관문을 등지고 남쪽을 볼 때, 시계방향)
1. 왼쪽(동): 낮은 신발장과 그 위 거울*. 이어서 욕실 문*.
2. 정면: 1m 짧은 통로 끝에 방 문(미닫이, 늘 열어 둔다)*.
3. 오른쪽(서): 일자 주방(싱크, 2구 인덕션), 그 끝에 소형 냉장고(3화 냉장고 모터, 위치는*). 냉장고 옆 알파룸 미닫이(옷 행거, 세탁기는 알파룸 안)*.
4. 등 뒤: 현관문과 도어락(3화 "삐, 삐, 삐, 삐" 네 자리).

**방** (방 문을 등지고 남쪽 창을 볼 때, 시계방향). 크기 3.0m × 3.6m*.
1. 왼쪽(동) 벽: 문 쪽부터 3단 책장(법전, 형사소송법 문제집, 바인더)*. 책장 끝 창가에 폭 1.2m 책상이 창을 왼쪽 옆에 두고 벽을 향해 놓인다*. 책상 위 스탠드 하나(3화), 노트북, 형광펜 컵, 법전*. 책상 아래 선반에 작은 프린터(5화 "프린터에서 막 나온 종이", 위치는*). 의자는 바퀴 달린 회전의자(3화 "의자를 밀고", "의자를 돌렸다", 형태는*).
2. 정면(남): 폭 2.1m 이중 미닫이창*. 얇은 흰 롤 블라인드를 대개 반쯤 올려 둔다*. 창밖 아래로 호수공원 잔디 광장과 가로등 몇 개, 멀리 호수 수면 한 조각*.
3. 오른쪽(서) 벽: 싱글 침대, 머리는 북쪽(문 쪽)*. 침대 위 벽에 코르크 보드(스터디 일정표)*. 책상과 침대 사이 바닥 폭 약 1.4m*(3화 "책상이 삐걱거리다가 침대가 삐걱거렸다" — 두 걸음 거리).
4. 등 뒤(북): 방 문 옆에 작은 협탁과 스탠드 옷걸이*. 3화 이후 의자 등받이에 그의 흰 셔츠가 걸려 있을 때가 있다*.
5. 바닥: 밝은 나뭇결 장판(LVT)*. 벽지: 아이보리 실크 벽지*.

### 4-3. 시간대별 조명

| 회차·씬 | 시각 | 광원 | 색온도 | 방향 | 메모 |
|---|---|---|---|---|---|
| 3화 S#1~3 | 새벽 1:50~2:20 | 책상 스탠드 하나 | 2700K | 책상 왼쪽 위에서 방 오른쪽으로 퍼짐. 서쪽 벽에 큰 그림자(3화 S#3) | 창은 남색, 공원 가로등 점 몇 개 |
| 3화 S#4 | 새벽 4:50 | 스탠드 + 창의 새벽빛 | 2700K / 창 6500K 약하게 | 창에서 수평 | 하늘이 남색에서 잿빛으로 묽어진다(3화) |
| 3화 S#5 | 오전 9:00 | 창 자연광, 스탠드 아직 켜짐* | 5500K | 남쪽 창에서 | 법전의 '사기와 공갈의 죄' 페이지 |
| 4화 S#13~15 | 밤 8:00 | 스탠드 + 현관 센서등 | 2700K / 3000K | 현관에서 방 쪽으로 | 센서등이 켜졌다 꺼진다(4화) |
| 5화 S#12~14 | 밤 9:00 | 스탠드의 노란 원 + 비 오는 창 | 2700K / 창 푸른 회색 | 위에서 원형으로 | 첫 가을비가 창을 비스듬히 긋는다(5화) |
| 6화 S#7 | 저녁 7:05 | 5층 복도 센서 다운라이트 | 4000K | 위에서 | 현관 안쪽은 어둡다* |

**대표 색**: `#F2C14E` 스탠드 노랑 · `#20263D` 새벽 남색 · `#F3EEDF` 법전 종이 · `#9CC7E8` 하린 하늘색 · `#7D8794` 빗줄기 회색

### 4-4. 소리·냄새

- **소리**: 냉장고 모터의 웅웅과 멈춤(3화). 창밖 스프링클러가 돌다 멈춤(3화). 도어락 네 음(3화). 형광펜 '쭉—', 법전 페이지 '후루룩', 버클 '딱'(3화). 책상과 싱글 침대의 삐걱(3화). 배달 오토바이, 청소차 후진 '삑, 삑'(3화). 어느 집 세탁기 탈수가 바닥을 울림(4화). 빗소리(5화). 계단으로 멀어지는 휘파람(5화 S#13).
- **냄새**: 식은 아메리카노와 형광펜 잉크(3화). 땀과 그의 비누 같은 향(3화). 식은 커피(4화). 프린터 토너와 식은 믹스커피(5화).

### 4-5. 반복 소품과 위치

| 소품 | 위치 | 근거 |
|---|---|---|
| 법전(형법 각칙 제39장 펼침) | 책상, 밀려난 자리 | 3화 S#5, 4화 S#13 |
| 안경(접힌 채) | 법전 위 | 3화 S#4 |
| 형광펜 여러 자루, 식은 아메리카노 | 책상 | 3화 S#1 |
| 노트북(상환 일정표 → 녹음 앱) | 책상 가운데 | 3화 S#4, 5화 S#12 |
| 그의 흰 셔츠 | 의자 등받이* / 하린이 입음 | 3화 |
| 머리끈 | 하린 손목, 책상 위* | 4화 S#15 |
| 한국장학재단 상환 안내문 | 책상 | 5화 S#12 |
| 테이프로 봉한 백화점 쇼핑백 | 책상 위 법전 옆, 스탠드 아래 | 5화 S#12·14 |
| 형사소송법 문제집 | 책상 | 5화 S#12 |

### 4-6. 카메라 자리

| 자리 | 높이·방향 | 핵심 장면 |
|---|---|---|
| C1 방 문가(북동) | 눈높이, 남쪽. 책상·스탠드 왼쪽, 침대 오른쪽, 창 정면 | 3화 S#1, 4화 S#15, 5화 S#12 |
| C2 책상 상판 | 상판 높이 클로즈, 스탠드 아래 법전·안경·쇼핑백 | 3화 S#4·5 Insert, 5화 S#14 사진 구도 |
| C3 침대 머리맡 위 | 부감 45°, 침대와 서쪽 벽 | 3화 S#3 벽 위 두 그림자 Insert, S#4 침대의 그 |
| C4 5층 복도 | 눈높이, 엘리베이터 쪽에서 502호 문과 비상계단 문 | 4화 S#13, 5화 S#13, 6화 S#7 |

### 4-7. 수위 장치 (3화 S#2~3, 4화 S#14 회상)

1. **스탠드 하나의 빛 원**: 빛은 책상 위만 밝고 방 대부분은 어둡다. 침대는 빛 원 바깥이다(3화).
2. **벽 위의 큰 그림자**: 행위는 서쪽 벽에 비친 두 그림자로만 보여 준다(대본 3화 S#3 Insert).
3. **안경을 벗은 POV 흐림**: 한 뼘 안쪽만 또렷하고 나머지는 흐린다(3화 S#2). 배경 레이어를 그대로 블러해 쓴다*.
4. **책상 위 사물 전경**: 법전, 스탠드 갓, 형광펜 컵을 화면 앞에 크게 걸어 가린다*.
5. **컷을 넘길 사물**: 데구루루 구르는 형광펜, 법전 모서리에 부딪힌 버클, 멈춘 냉장고(3화).

### 4-8. SET LOCK (106 words)

```text
A small rented room in unit 502 on the 5th floor of a new 2024-built Korean apartment building, a law student's room about 3 by 3.6 meters. On the left wall, a bookshelf crammed with thick law code books and a simple desk beside the window with one desk lamp, a laptop, highlighter pens in a cup and a swivel chair. Ahead, a sliding double window with a half-raised white roller blind, looking down on a lakeside park lawn with a few streetlights. On the right wall, a narrow single bed with plain light bedding. Ivory wallpaper, light wood-look vinyl floor, tidy but cramped student life.
```

### 4-9. 프롬프트

**E1 빈 배경 — 새벽 1:50 스탠드 하나** (3화 S#1)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A small rented room in unit 502 on the 5th floor of a new 2024-built Korean apartment building, a law student's room about 3 by 3.6 meters. On the left wall, a bookshelf crammed with thick law code books and a simple desk beside the window with one desk lamp, a laptop, highlighter pens in a cup and a swivel chair. Ahead, a sliding double window with a half-raised white roller blind, looking down on a lakeside park lawn with a few streetlights. On the right wall, a narrow single bed with plain light bedding. Ivory wallpaper, light wood-look vinyl floor, tidy but cramped student life.

Establishing view of the empty room at 1:50 am. The only light is the desk lamp: a warm yellow pool over an open law book whose thin pages glow translucent, a cold cup of americano and highlighters beside it. The rest of the room sinks into dim brown shade, the bed in soft darkness. Through the window, navy night and a few small park lamps; a sprinkler mist faintly visible on the lawn below. Lonely, studious, waiting. Wide 16:9 composition. No logos, no watermark.
```

**E2 빈 배경 — 밤 9:00 첫 가을비** (5화 S#12)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A small rented room in unit 502 on the 5th floor of a new 2024-built Korean apartment building, a law student's room about 3 by 3.6 meters. On the left wall, a bookshelf crammed with thick law code books and a simple desk beside the window with one desk lamp, a laptop, highlighter pens in a cup and a swivel chair. Ahead, a sliding double window with a half-raised white roller blind, looking down on a lakeside park lawn with a few streetlights. On the right wall, a narrow single bed with plain light bedding. Ivory wallpaper, light wood-look vinyl floor, tidy but cramped student life.

Establishing view of the same room at 9 pm on a rainy October night. Rain streaks slant across the window glass, blue-grey outside. The desk lamp makes a clean yellow circle over the law code and a criminal procedure workbook; a laptop shows a blank screen with a faint waveform glow. On the desk, beside the law book, a department store paper shopping bag sealed shut with many layers of shiny clear tape. Tense, quiet, decisive. Wide 16:9 composition. No logos, no watermark.
```

**C1 방 문가 → 창** (3화 S#1, 4화 S#15, 5화 S#12)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A small rented room in unit 502 on the 5th floor of a new 2024-built Korean apartment building, a law student's room about 3 by 3.6 meters. On the left wall, a bookshelf crammed with thick law code books and a simple desk beside the window with one desk lamp, a laptop, highlighter pens in a cup and a swivel chair. Ahead, a sliding double window with a half-raised white roller blind, looking down on a lakeside park lawn with a few streetlights. On the right wall, a narrow single bed with plain light bedding. Ivory wallpaper, light wood-look vinyl floor, tidy but cramped student life.

Camera at the room doorway at eye level, looking south: the desk and lamp on the left by the window, the single bed along the right wall, the window straight ahead with the blind half raised. Deep night, lamp light only, the bed edge just catching a rim of warm light. The whole cramped room readable in one frame. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C2 책상 상판 클로즈** (3화 S#4·5, 5화 S#14)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A small rented room in unit 502 on the 5th floor of a new 2024-built Korean apartment building, a law student's room about 3 by 3.6 meters. On the left wall, a bookshelf crammed with thick law code books and a simple desk beside the window with one desk lamp, a laptop, highlighter pens in a cup and a swivel chair. Ahead, a sliding double window with a half-raised white roller blind, looking down on a lakeside park lawn with a few streetlights. On the right wall, a narrow single bed with plain light bedding. Ivory wallpaper, light wood-look vinyl floor, tidy but cramped student life.

Close view at desk-top height under the lamp: a thick law code book lying open where it was pushed aside, its page edges fanned; a pair of thin gold oval glasses folded neatly on top of it; a highlighter rolled to the desk edge. Warm lamp light from upper left, everything beyond the desk dissolving into darkness. Vertical 9:16 webtoon panel, still-life detail. No logos, no watermark.
```

**C3 침대 머리맡 부감** (3화 S#3·4)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A small rented room in unit 502 on the 5th floor of a new 2024-built Korean apartment building, a law student's room about 3 by 3.6 meters. On the left wall, a bookshelf crammed with thick law code books and a simple desk beside the window with one desk lamp, a laptop, highlighter pens in a cup and a swivel chair. Ahead, a sliding double window with a half-raised white roller blind, looking down on a lakeside park lawn with a few streetlights. On the right wall, a narrow single bed with plain light bedding. Ivory wallpaper, light wood-look vinyl floor, tidy but cramped student life.

High angle from above the head of the narrow single bed, looking down at rumpled light bedding and the west wall beside it. The desk lamp across the room throws a large soft-edged shadow shape onto the ivory wallpaper. Window at the edge of frame turning from navy to grey toward dawn. Intimate, hushed, small. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C4 5층 복도** (4화 S#13, 5화 S#13, 6화 S#7)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A small rented room in unit 502 on the 5th floor of a new 2024-built Korean apartment building, a law student's room about 3 by 3.6 meters. On the left wall, a bookshelf crammed with thick law code books and a simple desk beside the window with one desk lamp, a laptop, highlighter pens in a cup and a swivel chair. Ahead, a sliding double window with a half-raised white roller blind, looking down on a lakeside park lawn with a few streetlights. On the right wall, a narrow single bed with plain light bedding. Ivory wallpaper, light wood-look vinyl floor, tidy but cramped student life.

Different area: the 5th-floor elevator lobby outside unit 502, a short apartment corridor with grey stone-look tiles, two stainless elevator doors on one side, a plain apartment front door with a digital keypad lock, and a heavy grey emergency stair door at the end. A single sensor downlight is on above the door, the rest of the corridor dim. Vertical 9:16 webtoon panel. No logos, no watermark.
```

### 4-10. 고증 메모

- 2020년대 수도권 신축 대단지에는 전용 39㎡·49㎡ 같은 소형 평형이 일부 동에 섞여 있는 경우가 있다. 추측입니다: 412동을 소형 위주 동으로 둔 것은 작중 설정이다.
- 소형 평형의 '알파룸'(옷방·세탁 공간)은 신축 평면에서 흔한 이름이다. 추측입니다.
- 도어락 비밀번호 네 자리는 그녀의 생일(1129)이다(bible). 화면에 숫자를 쓰지 않는다.
- 2020년대 신축은 대부분 계단식(코어당 2~4세대)이다. 복도식이 아니므로 5층 복도는 '엘리베이터 홀' 크기로 그린다.
- 청년 버팀목 전세대출로 소형 전세를 얻는 설정은 bible과 같다.

---

## 5. 503동 2402호 — 혜숙의 거실·안방 (+24층 엘리베이터 홀)

### 5-1. 공간 개요

- **위치**: 503동 24층, 자가(SPEC). 503동은 단지 북쪽 줄의 가운데 동이다(맨 끝 '단지 전체 배치')*.
- **평형**: 공급 약 45평(전용 114㎡), 4베이 판상형*. 층당 두 세대(2401호와 2402호)*. 그래서 24층에는 서는 사람이 거의 없다(1화 문장의 이유*). 옆집 2401호와 벽 하나를 사이에 둔다("옆집이 귀가 밝아", 1화).
- **창 방향**: 남향 거실(bible). 오후 두 시에 커튼 한 뼘 틈으로 금빛 빛줄기 한 줄(1화), 오전 열 시에 흰 소파 위로 칼 같은 빛(4화), 오후 세 시에 긴 사다리꼴(5화).
- **등장 근거**
  - 1화 S#9 현관·거실(오후 2:00), S#10~12 안방(오후 2:10~4:25), S#13 현관(4:38), S#14 24층 엘리베이터 홀(4:40)
  - 2화 S#1 24층 엘리베이터 홀(4:41), S#2 엘리베이터 안
  - 3화 S#6 몽타주(저녁 6:00)
  - 4화 S#7·9 거실(오전 10:00~10:15), S#8 회상 안방
  - 5화 S#8 거실(오후 3:00)
  - 6화 S#5 현관(저녁 6:49). 6화 S#4 503동 지하 엘리베이터 홀은 8번 장소.

### 5-2. 평면 배치

**현관** (현관문을 등지고 남쪽을 볼 때, 시계방향). 현관은 세대 북쪽 가운데*.
1. 왼쪽(동): 천장까지 짙은 월넛 신발장(1화 "신발장 안에 넣고 문을 닫았다", 재질은*).
2. 정면: 현관 홀 정면 벽에 짙은 월넛 콘솔(폭 1.4m)*. 콘솔 위 왼쪽에 백합 꽃꽂이, 오른쪽에 가운 차림 남편 액자(1화 S#9, 좌우는*). 콘솔 위 벽에 둥근 금테 거울*. 콘솔을 지나 왼쪽(동)으로 꺾으면 안방 복도, 오른쪽(서)으로 꺾으면 거실이다*.
3. 오른쪽(서): 주방과 다이닝으로 바로 이어지는 개구부*.
4. 등 뒤: 현관문. 벨은 누르지 않는다(1화).

**거실** (콘솔 오른쪽으로 돌아 거실에 들어서서 남쪽을 볼 때, 시계방향)
1. 왼쪽(동) 벽: 베이지 대리석 아트월과 벽걸이 TV*. TV 위에 둥근 벽시계(1화 S#9 "벽시계 초침", 위치는*).
2. 정면(남): 폭 5m 창(발코니 확장형)*. 차콜 암막 커튼과 흰 쉬어 커튼 두 겹*. 1화에는 암막이 한 뼘만 열려 있다. 4화에는 반쯤 → 끝까지. 5화에는 반만.
3. 오른쪽(서) 벽: 흰 가죽 3인 소파가 벽에 붙어 동쪽 TV를 본다(흰 소파는 bible, 방향은*). 소파 앞 직사각 유리 테이블(5화 "맞은편 유리 테이블에 걸터앉았다", 크기 1.2m×0.6m*). 소파 옆 사이드보드 위 오디오(4화 클래식 FM, 위치는*).
4. 등 뒤(북서): 다이닝 6인 원목 식탁(2화 "떡은 식탁에 놓고")과 주방, 핸드드립 세트(4화, 위치는*).

**안방** (현관 홀 동쪽 복도 끝, 문을 등지고 남쪽을 볼 때, 시계방향)
1. 왼쪽(동) 벽: 화장대와 낮은 서랍장*.
2. 정면(남): 폭 3m 창, 차콜 암막 커튼(1화 "안방 커튼도 한 뼘만", 색은*).
3. 오른쪽(서) 벽: 드레스룸 문*.
4. 등 뒤(북) 벽: 헤드보드를 북쪽 벽에 붙인 퀸 침대. 발치가 창을 향한다*. 그래서 커튼 틈 빛이 침대 머리맡 벽을 비스듬히 가른다(1화). 침대 프레임은 가는 금속 다리 위에 떠 있다(1화 "침대 다리에 부딪혀 멈췄다", 형태는*). 침대 위 벽에 작은 벽시계(1화 S#12 "벽시계 4시 25분", 위치는*).
5. 바닥: 대리석(1화 진주가 대리석으로 떨어진다). 크기 약 4.5m × 4.2m*.

**24층 엘리베이터 홀**
- 엘리베이터 두 대가 나란히, 문 위에 붉은 층수 숫자(1화)*. 숫자는 식자로 넣는다.
- 홀 바닥은 대리석(2화 진주가 대리석 위에서 한 번 튄다). 벽은 회색 석재 타일*.
- 천장 센서등이 '지잉' 하며 켜진다(1화).
- 엘리베이터에서 나와 오른쪽이 2402호, 왼쪽이 2401호*. 2402호 문까지 4m*.
- 라벤더 방향제 냄새(1화). 방향제는 엘리베이터 안에 있다*.

### 5-3. 시간대별 조명

| 회차·씬 | 시각 | 광원 | 색온도 | 방향 | 메모 |
|---|---|---|---|---|---|
| 1화 S#9~10 | 오후 2:00 | 실내등 꺼짐. 암막 커튼 한 뼘 틈 | 5200K, 금빛으로 | 남→북. 대리석 위 금빛 칼날 한 줄. 안방에서는 머리맡 벽을 비스듬히 | 빛 속을 도는 먼지(1화) |
| 1화 S#11~12 | 오후 4:00~4:25 | 같은 틈, 해가 낮아짐 | 4000K, 더 노랗게 | 빛줄기가 벽에서 내려와 침대 위·어깨로 | 1화 S#11 |
| 1화 S#14, 2화 S#1 | 오후 4:40 | 홀 센서 다운라이트 | 3500K | 위에서 | 엘리베이터 문 안의 밝은 빛이 홀로 쏟아진다* |
| 4화 S#7 → S#9 | 오전 10:00 → 10:15 | 반쯤 걷힌 커튼 → 끝까지 걷음 | 5500K | 남동에서. 흰 소파 위 칼 같은 한 줄 → 거실 전체 | 커튼을 걷는 순간이 장면의 전환점(4화) |
| 5화 S#8 | 오후 3:00 | 반만 걷은 커튼 | 4800K | 남서에서. 대리석 위 긴 사다리꼴 | 진주가 쇄골 위에서 차갑게 구른다(5화) |
| 6화 S#5 | 저녁 6:49 | 현관 다운라이트 + 홀 센서등 | 3000K | 위에서 | 금색 시퀸이 빛을 받는 자리* |

**대표 색**: `#E8B85A` 금빛 칼날 · `#EDEAE4` 흰 대리석 · `#F5F3EE` 흰 소파 · `#3A3536` 차콜 암막 · `#C9A45C` 혜숙 금색

### 5-4. 소리·냄새

- **소리**: 벽시계 초침, 멀리 조경팀 예초기, 늦매미 한 마리(1화). 스커트 지퍼 '지이이익'(1화). 진주가 대리석에 '타다닥', 구르며 '또르르'(1화). 센서등 '지잉', 엘리베이터 '띵'(1화). 클래식 FM 첼로, 핸드드립 물 떨어지는 소리(4화). 조경수 가지치기 전기톱(5화).
- **냄새**: 콘솔 위 백합 꽃가루(1·4·5화). 금색 병의 달큰한 앰버·바닐라(bible). 엘리베이터 홀의 라벤더 방향제(1화). 떡 상자의 참기름(2화). 핸드드립 원두(4화).

### 5-5. 반복 소품과 위치

| 소품 | 위치 | 근거 |
|---|---|---|
| 백합 꽃꽂이 | 현관 홀 콘솔 왼쪽 | 1·4·5화 |
| 가운 차림 남편 액자 | 콘솔 오른쪽. 1화에는 엎어진다 | 1화 S#9 |
| 진주 목걸이(44알) | 혜숙 목. 1화 안방 바닥에 흩어진 알들 | 1·2·4·5화 |
| 한우 보자기 상자 | 현관 | 1화 S#13 |
| 분양권 서류 | 거실 유리 테이블 | 3화 S#6 |
| 만년필 한 자루, 확인서 한 장 | 거실 유리 테이블 | 5화 S#8 |
| 클리어파일 | 거실 유리 테이블 → 6화 와인바 | 5·6화 |
| 벽시계 | 거실 TV 위, 안방 침대 위 | 1화 |
| 오디오(클래식 FM) | 거실 소파 옆 사이드보드 | 4화, 위치는* |

### 5-6. 카메라 자리

| 자리 | 높이·방향 | 핵심 장면 |
|---|---|---|
| C1 현관 홀 | 눈높이, 콘솔 너머 거실 남쪽 창의 빛 | 1화 S#9 액자를 엎는 손, 4화 S#7 |
| C2 안방 문가 | 눈높이, 남쪽 창의 틈과 침대 머리맡 벽 | 1화 S#10~11. 같은 자리에서 부감으로 바꾸면 1화 S#12 진주 줍기 |
| C3 거실 TV 앞 | 낮은 앉은 눈높이, 서쪽 흰 소파와 유리 테이블, 오른쪽에 창 | 5화 S#8 확인서, 4화 S#9 커튼을 걷는 혜숙 |
| C4 24층 엘리베이터 홀 | 눈높이, 2402호 문 앞에서 엘리베이터 문 쪽 | 1화 S#14 "어머.", 2화 S#1 진주가 구른다 |

### 5-7. 수위 장치 (1화 S#10, 4화 S#8 회상, 5화 S#8)

1. **커튼 틈 빛줄기 하나**: 방은 어둡고 빛줄기에 걸린 부위만 보인다. 등과 척추 골, 맨어깨를 빛이 금색으로 칠한다(1화 S#10).
2. **커튼 자락 전경**: 차콜 암막의 주름을 화면 앞에 크게 걸어 몸을 반쯤 가린다*.
3. **컷을 넘길 사물**: 대리석 위로 흩어지는 진주알, 침대 다리에 부딪혀 멈춘 마지막 한 알, 벽시계(1화).
4. 5화 S#8 **유리 테이블 위 만년필과 종이**: 전경에 두고 키스는 흐린 뒤 배경으로 보낸다*.
5. **엎어진 액자**: 장면 시작의 신호. 액자 뒷면이 '지금부터 보지 않는다'는 표시다*.

### 5-8. SET LOCK (108 words)

```text
Unit 2402 on the 24th floor of a new 2024-built Korean apartment tower, a wealthy middle-aged woman's home of about 114 square meters. Polished white marble floor, cream walls, a south-facing living room window about 5 m wide with charcoal blackout curtains over sheer white curtains. A white leather sofa against the right wall faces a beige marble feature wall with a TV and a round wall clock, a rectangular glass coffee table between them. The entry hall has a dark walnut console with a white lily arrangement and a framed photo. Master bedroom: a queen bed on thin metal legs, headboard against the wall, facing the window.
```

### 5-9. 프롬프트

**E1 빈 배경 — 오후 2:00 커튼 한 뼘** (1화 S#9)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Unit 2402 on the 24th floor of a new 2024-built Korean apartment tower, a wealthy middle-aged woman's home of about 114 square meters. Polished white marble floor, cream walls, a south-facing living room window about 5 m wide with charcoal blackout curtains over sheer white curtains. A white leather sofa against the right wall faces a beige marble feature wall with a TV and a round wall clock, a rectangular glass coffee table between them. The entry hall has a dark walnut console with a white lily arrangement and a framed photo. Master bedroom: a queen bed on thin metal legs, headboard against the wall, facing the window.

Establishing view of the dim living room at 2 pm. The blackout curtains are open only a hand's width; through the gap one blade of golden September sunlight lies across the white marble floor, dust motes turning slowly inside it. Everything else in soft brown shade: the white sofa, the glass table, the clock on the marble wall. Hushed, forbidden afternoon. Wide 16:9 composition. No logos, no watermark.
```

**E2 빈 배경 — 오전 10:00 커튼을 끝까지 걷은 뒤** (4화 S#9)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Unit 2402 on the 24th floor of a new 2024-built Korean apartment tower, a wealthy middle-aged woman's home of about 114 square meters. Polished white marble floor, cream walls, a south-facing living room window about 5 m wide with charcoal blackout curtains over sheer white curtains. A white leather sofa against the right wall faces a beige marble feature wall with a TV and a round wall clock, a rectangular glass coffee table between them. The entry hall has a dark walnut console with a white lily arrangement and a framed photo. Master bedroom: a queen bed on thin metal legs, headboard against the wall, facing the window.

Establishing view of the same living room at 10:15 am with the curtains thrown fully open: bright clean south-east morning light floods the whole room, the white sofa and marble floor almost glowing, the lily arrangement visible in the entry hall at the back, a pour-over coffee set on the dining sideboard. Clear, exposed, decisive mood. Wide 16:9 composition. No logos, no watermark.
```

**C1 현관 홀 → 콘솔과 거실의 빛** (1화 S#9, 4화 S#7)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Unit 2402 on the 24th floor of a new 2024-built Korean apartment tower, a wealthy middle-aged woman's home of about 114 square meters. Polished white marble floor, cream walls, a south-facing living room window about 5 m wide with charcoal blackout curtains over sheer white curtains. A white leather sofa against the right wall faces a beige marble feature wall with a TV and a round wall clock, a rectangular glass coffee table between them. The entry hall has a dark walnut console with a white lily arrangement and a framed photo. Master bedroom: a queen bed on thin metal legs, headboard against the wall, facing the window.

Camera in the entry hall at eye level just inside the front door, facing the dark walnut console: white lilies on the left, a small framed photo lying face down on the right, a round gold-rimmed mirror above. To the right, the opening into the dim living room where a thin blade of golden sunlight cuts the marble floor. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C2 안방 문가 → 커튼 틈과 머리맡 벽** (1화 S#10~12)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Unit 2402 on the 24th floor of a new 2024-built Korean apartment tower, a wealthy middle-aged woman's home of about 114 square meters. Polished white marble floor, cream walls, a south-facing living room window about 5 m wide with charcoal blackout curtains over sheer white curtains. A white leather sofa against the right wall faces a beige marble feature wall with a TV and a round wall clock, a rectangular glass coffee table between them. The entry hall has a dark walnut console with a white lily arrangement and a framed photo. Master bedroom: a queen bed on thin metal legs, headboard against the wall, facing the window.

Camera at the master bedroom doorway, eye level, looking at the bed and the window. The charcoal curtain is open a hand's width and a diagonal beam of warm afternoon light slices across the wall above the headboard. Rumpled ivory bedding, a pencil skirt draped at the foot of the bed, and several loose white pearls scattered on the marble floor near the thin metal bed legs. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C3 거실 TV 앞 → 흰 소파와 유리 테이블** (5화 S#8, 4화 S#9)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Unit 2402 on the 24th floor of a new 2024-built Korean apartment tower, a wealthy middle-aged woman's home of about 114 square meters. Polished white marble floor, cream walls, a south-facing living room window about 5 m wide with charcoal blackout curtains over sheer white curtains. A white leather sofa against the right wall faces a beige marble feature wall with a TV and a round wall clock, a rectangular glass coffee table between them. The entry hall has a dark walnut console with a white lily arrangement and a framed photo. Master bedroom: a queen bed on thin metal legs, headboard against the wall, facing the window.

Camera low at seated height in front of the marble TV wall, looking west at the white leather sofa and the rectangular glass coffee table. On the glass, a fountain pen and a single sheet of paper with a blank signature line. Curtains half open at the left of frame, autumn afternoon light at 3 pm laying a long trapezoid on the marble. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C4 24층 엘리베이터 홀** (1화 S#14, 2화 S#1)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Unit 2402 on the 24th floor of a new 2024-built Korean apartment tower, a wealthy middle-aged woman's home of about 114 square meters. Polished white marble floor, cream walls, a south-facing living room window about 5 m wide with charcoal blackout curtains over sheer white curtains. A white leather sofa against the right wall faces a beige marble feature wall with a TV and a round wall clock, a rectangular glass coffee table between them. The entry hall has a dark walnut console with a white lily arrangement and a framed photo. Master bedroom: a queen bed on thin metal legs, headboard against the wall, facing the window.

Different area: the 24th-floor elevator lobby outside unit 2402. Two stainless elevator doors side by side with a small blank red floor indicator above each, grey stone tile walls, a polished marble floor, one sensor downlight just switched on. One elevator door stands open, bright light spilling out onto the floor. A single white pearl rests on the marble near the door. Vertical 9:16 webtoon panel. No logos, no watermark.
```

### 5-10. 고증 메모

- 2020년대 신축 대단지의 중대형 평형은 '4베이 판상형 남향'을 앞세우는 경우가 많다. 거실과 안방이 같은 남쪽 면에 나란히 놓인다.
- 발코니 확장은 신축 분양에서 거의 기본처럼 선택된다. 그래서 거실 창이 넓고 바로 실내와 맞닿는다. 추측입니다: 확장 비율은 단지마다 다르다.
- 층당 두 세대 코어에서는 한 층에 서는 사람이 적다. 1화 '24층은 서는 사람이 거의 없다'를 이 구조로 설명한다*.
- 엘리베이터 홀에 천장 센서등과 방향제를 두는 관리 방식은 흔하다. 추측입니다: 방향제 비치는 관리사무소 재량이다.
- 부녀회는 법정 단체인 입주자대표회의와 별개인 자생 단체다. 부녀회장이 관리사무소·경비실과 친하다는 설정은 흔한 현실을 쓴 것이다. 추측입니다: 실제 영향력은 단지마다 크게 다르다.

---

## 6. 물결놀이터와 호수공원

### 6-1. 공간 개요

- **위치**: 단지 중앙광장 남쪽. 열다섯 개 동이 놀이터를 빙 둘러싸고 서 있다(3화 S#16 부감). 놀이터 북쪽에 커뮤니티센터가 있다*. 남동쪽 수변 게이트 너머가 호수신도시 중앙 호수공원이다(호수는 3화 "호수 쪽에서 비린 물 냄새", 게이트는*).
- **크기**: 놀이터 영역 약 45m × 35m*. 원형 바닥분수 지름 약 14m*.
- **호수공원**: 공공 호수공원이다. 호수 둘레에 산책로와 가로등(5화 "호수공원 산책로 가로등"), 건너편 기슭에 오리배 선착장(3화 "오리배 두 척", 선착장 위치는*).
- **등장 근거**
  - 3화 S#14 놀이터(오후 3:40), S#15 벤치(3:55), S#16 벤치·하늘(4:00)
  - 4화 S#1 놀이터(오후 4:02)
  - 3화 S#6 몽타주: 열다섯 개 동의 그림자가 호수 위로(저녁 6:00)
  - 1화 S#4 단지 정문 셔틀버스 정류장은 동쪽 정문(맨 끝 '단지 전체 배치')*

### 6-2. 평면 배치

(101동 쪽 남동 진입로에 서서 북서쪽 놀이터를 볼 때, 시계방향)
1. 왼쪽(남서): 키 큰 느티나무 줄과 잔디 둔덕*. 둔덕 너머로 4xx 동들*.
2. 정면 왼쪽(서): 조합놀이대. 미끄럼틀 두 개, 그물 오르기, 지붕 있는 작은 탑*. 그 아래에 모래 놀이 구역(3화 "모래 위로 미끄럼틀 그림자")*. 모래 구역 둘레는 낮은 화강석 경계석*.
3. 정면(북서~북): 원형 바닥분수 광장. 연회색 화강석 바닥에 노즐이 동심원 두 줄, 바깥 가장자리에 배수 그레이팅*. 분수는 정해진 박자로 솟았다 꺼진다(3화). 분수 너머 북쪽으로 커뮤니티센터 '더퍼스트 클럽'의 낮은 유리 건물*.
4. 오른쪽(북동~동): 분수를 바라보는 원목 벤치 다섯 개가 반원으로 놓인다*. 벤치 뒤에 그늘 퍼걸러*. 벤치 사이에 가로등 기둥 하나, 그 중간 높이에 원통형 방송 스피커(3화 S#16 "놀이터 가로등 기둥의 스피커", 형태는*). 유진과 미란은 이 반원의 남쪽 두 벤치에 앉는다*.
5. 등 뒤(남동): 수변 게이트와 산책로, 그 너머 호수*.
6. 바닥 재질: 놀이대 아래는 탄성 포장, 분수는 화강석, 동선은 연한 투수 블록*.

### 6-3. 시간대별 조명

| 회차·씬 | 시각 | 광원 | 색온도 | 방향 | 메모 |
|---|---|---|---|---|---|
| 3화 S#14~16, 4화 S#1 | 오후 3:40~4:02(9/19) | 해 | 4500K | 남서쪽, 고도 약 35°*. 미끄럼틀 그림자가 북동으로 길다 | 분수 물방울이 역광으로 반짝. S#16 부감에서 동 유리창이 한꺼번에 반짝인다 |
| 3화 S#6 | 저녁 6:00(9/15) | 지는 해 | 3200K | 서쪽 낮은 각도. 동 그림자가 호수 위로 길게 눕는다 | 유리창이 차례로 주황색으로 물든다(3화) |

**대표 색**: `#CFE8F0` 물보라 · `#D9C7A1` 모래 · `#6F8E9C` 호수 · `#7C9A5E` 느티나무 · `#F0B865` 유리창 반사 주황

### 6-4. 소리·냄새

- **소리**: 바닥분수가 솟고 꺼지는 소리, 아이들 비명(3·4화). 관리사무소 안내방송 차임 '딩동댕동'과 방송(가로등 스피커, 3화 S#16). 두 휴대폰의 신호음이 반 박자씩 어긋남(3화). 4:19 차량 알림음(4화). 하원 버스 문, 치킨집 환풍기(3화 S#6, 단지 전체).
- **냄새**: 호수 쪽 비린 물 냄새, 벤치마다 선크림과 귤껍질(3·4화).

### 6-5. 반복 소품과 위치

| 소품 | 위치 | 근거 |
|---|---|---|
| 방송 스피커 | 벤치 사이 가로등 기둥 | 3화 S#16 |
| 벤치 | 분수 동쪽 반원 | 3화 S#14 |
| 바닥분수 노즐 | 분수 광장 | 3화 |
| 미끄럼틀 그림자 | 모래 위 | 3화 |
| 수건, 선글라스 | 벤치 위(장면 소품) | 4화 S#1 |

### 6-6. 카메라 자리

| 자리 | 높이·방향 | 핵심 장면 |
|---|---|---|
| C1 퍼걸러 아래 벤치 뒤 | 앉은 눈높이, 서쪽. 벤치 등받이 너머 분수와 놀이대 | 3화 S#14~15 벤치 대화 |
| C2 분수 광장 한가운데 | 바닥 로우 앵글, 솟는 물줄기 너머 동쪽 벤치 | 3화 S#15 "바닥분수가 솟았다. 꺼졌다." |
| C3 가로등 아래 | 올려다보기. 스피커와 하늘, 둘러싼 동들의 꼭대기 | 3화 S#16 스피커 Insert |
| C4 상공 부감 | 높이 약 80m, 남동쪽에서 북서쪽으로. 놀이터와 15개 동, 화면 아래 호수 | 3화 S#16 부감 |

### 6-7. 수위 장치

- 관능 장면이 없다. 아이들이 있는 장소다.
- 미란의 의상 Insert(3화 S#14 오프숄더, 슬릿)는 아이가 프레임에 들어오지 않게 벤치 쪽으로 잘라 쓴다*.
- 아이 둘은 이 장소 밖의 관능 장면과 같은 컷에 넣지 않는다(SPEC 4절).

### 6-8. SET LOCK (99 words)

```text
The central playground called Mulgyeol, meaning ripple, in a new 2024-built Korean mega apartment complex, surrounded on all sides by fifteen tall residential towers. A circular light-grey granite splash pad about 14 m wide with two rings of ground fountain nozzles. On the left, a colorful play structure with two slides above a sand pit edged with granite. On the right, a half-circle of wooden benches under a pergola and one tall lamppost with a cylindrical announcement speaker. Zelkova trees and lawn mounds around it; beyond a gate to the southeast, a wide calm lake with a lakeside promenade.
```

### 6-9. 프롬프트

**E1 빈 배경 — 오후 3:40 9월 오후** (3화 S#14)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The central playground called Mulgyeol, meaning ripple, in a new 2024-built Korean mega apartment complex, surrounded on all sides by fifteen tall residential towers. A circular light-grey granite splash pad about 14 m wide with two rings of ground fountain nozzles. On the left, a colorful play structure with two slides above a sand pit edged with granite. On the right, a half-circle of wooden benches under a pergola and one tall lamppost with a cylindrical announcement speaker. Zelkova trees and lawn mounds around it; beyond a gate to the southeast, a wide calm lake with a lakeside promenade.

Establishing view of the empty playground at 3:40 pm in mid-September. Warm afternoon sun from the southwest, the slide's long shadow lying across the sand, fountain jets frozen mid-rise and sparkling against the light, the apartment towers' glass windows glinting all around. Benches empty, a towel left on one. Bright, ordinary, safe weekend mood just before a shock. Wide 16:9 composition. No logos, no watermark.
```

**E2 빈 배경 — 저녁 6:00 호수 위 그림자** (3화 S#6)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The central playground called Mulgyeol, meaning ripple, in a new 2024-built Korean mega apartment complex, surrounded on all sides by fifteen tall residential towers. A circular light-grey granite splash pad about 14 m wide with two rings of ground fountain nozzles. On the left, a colorful play structure with two slides above a sand pit edged with granite. On the right, a half-circle of wooden benches under a pergola and one tall lamppost with a cylindrical announcement speaker. Zelkova trees and lawn mounds around it; beyond a gate to the southeast, a wide calm lake with a lakeside promenade.

Establishing view from the playground toward the southeast lake at 6 pm in September, sun low in the west. The towers cast very long dark shadows stretching east across the lawn and onto the lake surface; their windows turn orange one after another. The splash pad is off and still wet, reflecting the sky. Golden, melancholy, the whole complex watching. Wide 16:9 composition. No logos, no watermark.
```

**C1 퍼걸러 아래 벤치 뒤** (3화 S#14~15)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The central playground called Mulgyeol, meaning ripple, in a new 2024-built Korean mega apartment complex, surrounded on all sides by fifteen tall residential towers. A circular light-grey granite splash pad about 14 m wide with two rings of ground fountain nozzles. On the left, a colorful play structure with two slides above a sand pit edged with granite. On the right, a half-circle of wooden benches under a pergola and one tall lamppost with a cylindrical announcement speaker. Zelkova trees and lawn mounds around it; beyond a gate to the southeast, a wide calm lake with a lakeside promenade.

Camera under the pergola behind the half-circle of wooden benches, seated eye level, looking west over two empty bench backs toward the splash pad and the colorful play structure. Dappled pergola shade in the foreground, bright afternoon sun beyond, fountain spray glittering. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C2 분수 광장 로우 앵글** (3화 S#15)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The central playground called Mulgyeol, meaning ripple, in a new 2024-built Korean mega apartment complex, surrounded on all sides by fifteen tall residential towers. A circular light-grey granite splash pad about 14 m wide with two rings of ground fountain nozzles. On the left, a colorful play structure with two slides above a sand pit edged with granite. On the right, a half-circle of wooden benches under a pergola and one tall lamppost with a cylindrical announcement speaker. Zelkova trees and lawn mounds around it; beyond a gate to the southeast, a wide calm lake with a lakeside promenade.

Ground-level low angle in the middle of the granite splash pad, wet stone and nozzles in sharp foreground focus, a column of fountain water bursting upward and catching the afternoon backlight, the row of wooden benches blurred behind the water to the east. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C3 가로등 스피커 올려다보기** (3화 S#16)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The central playground called Mulgyeol, meaning ripple, in a new 2024-built Korean mega apartment complex, surrounded on all sides by fifteen tall residential towers. A circular light-grey granite splash pad about 14 m wide with two rings of ground fountain nozzles. On the left, a colorful play structure with two slides above a sand pit edged with granite. On the right, a half-circle of wooden benches under a pergola and one tall lamppost with a cylindrical announcement speaker. Zelkova trees and lawn mounds around it; beyond a gate to the southeast, a wide calm lake with a lakeside promenade.

Worm's-eye view straight up the tall lamppost beside the benches: the cylindrical announcement speaker mounted halfway up in sharp detail, the lamp head above, and around the edges of the frame the tops of tall apartment towers converging against a pale autumn sky. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C4 상공 부감** (3화 S#16)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The central playground called Mulgyeol, meaning ripple, in a new 2024-built Korean mega apartment complex, surrounded on all sides by fifteen tall residential towers. A circular light-grey granite splash pad about 14 m wide with two rings of ground fountain nozzles. On the left, a colorful play structure with two slides above a sand pit edged with granite. On the right, a half-circle of wooden benches under a pergola and one tall lamppost with a cylindrical announcement speaker. Zelkova trees and lawn mounds around it; beyond a gate to the southeast, a wide calm lake with a lakeside promenade.

High aerial view from about 80 meters above the southeast, looking northwest: the small round splash pad and playground at the center, fifteen tall apartment towers standing in a ring around it, a low glass community building just north of the playground, and the edge of the wide lake along the bottom of the frame. Late afternoon sun makes thousands of windows flash at once. Wide 16:9 composition. No logos, no watermark.
```

### 6-10. 고증 메모

- 2020년대 신축 대단지는 지상에 차가 다니지 않는 '공원형 단지'가 많다. 중앙광장, 바닥분수(물놀이 시설), 테마 놀이터는 분양 홍보의 단골 항목이다.
- 단지 방송은 관리사무소에서 옥외 스피커와 세대 월패드로 함께 내보낸다. 그래서 3화의 안내방송이 놀이터 하늘과 다른 장소의 수화기 속에서 동시에 들린다. 추측입니다: 옥외 스피커를 가로등 기둥에 다는지 별도 기둥에 다는지는 단지마다 다르다.
- 최근 신축 놀이터는 모래 대신 탄성 포장만 쓰는 경우가 많다. 소설에 '모래'가 있으므로 모래 놀이 구역을 따로 둔다*. 추측입니다: 모래 놀이터 비율은 확인하지 못했다.
- 9월 중순 경기 남부의 오후 4시 해 고도는 약 35°, 일몰은 오후 6시 40분대다. 추측입니다: 정확한 값은 천문 계산으로 다시 확인할 것.

---

## 7. 더퍼스트 클럽 사우나 — 여탕 세신실·열탕

### 7-1. 공간 개요

- **위치**: 커뮤니티센터 지하 1층 여탕. 중앙 복도 동쪽에 입구가 있고, 욕장 북쪽 끝은 필라테스룸 동쪽 벽과 맞닿는다*.
- **크기**: 욕장 약 30평(100㎡)*. 세신 코너는 욕장 북동쪽 구석이고 열탕과 바로 붙어 있다*. 그래서 5화에 열탕 가장자리의 혜숙과 세신대 위의 유진이 말을 주고받는다.
- **창**: 없다. 천장 형광등이 수증기에 번져 흐린 달처럼 뜬다(2화).
- **등장 근거**
  - 2화 S#11 세신실(오전 11:00), S#12 세신실 입구(11:38), S#13·15 세신실(11:40~11:42)
  - 5화 S#11 세신실(오전 11:00, 10월 5일)
  - 1화 S#5⑤ 사우나 입구 앞 복도(오후 3:00)
  - 참고: 2화 S#14 회상 '동네 목욕탕 보일러실'(2001년 겨울)은 다른 장소다. 이 SET LOCK을 쓰지 않는다.

### 7-2. 평면 배치

**여탕 입구와 탈의실**: 복도 쪽 입구 → 신발장 → 탈의실(옷장 줄, 파우더대, 체중계)* → 유리 미닫이 → 욕장*. 2화의 체인 백은 탈의실 옷장 앞에 걸려 있었다(2화).

**욕장** (유리 미닫이를 등지고 북쪽을 볼 때, 시계방향)
1. 왼쪽(서) 벽: 좌식 샤워대 열 개가 한 줄. 각 칸마다 거울과 수전*.
2. 정면 왼쪽(북서): 냉탕과 온탕*.
3. 정면 오른쪽(북동): 열탕, 2m × 3m*. 타일 테두리가 걸터앉을 수 있는 턱이다(5화 "열탕 가장자리에… 앉아", 턱 높이 45cm*). 순환 펌프 토출구가 탕 안 벽에 있다(2화 "순환 펌프", 위치는*).
4. 오른쪽(동) 벽 북쪽 끝: **세신 코너**. 열탕 바로 오른쪽*.
   - 세신대 두 대. 인조가죽 매트 침대에 투명 비닐을 덮는다(2화 "새 비닐을 펼쳤다")*.
   - 벽 선반: 대야와 바가지, 쑥 비누, 이태리타월, 방수팩에 든 손님 휴대폰을 올리는 작은 선반(2화 "세신대 옆 선반")*.
   - 수전 두 개와 짧은 샤워 호스*. 바닥 배수구*.
   - 욕장 쪽으로 반투명 유리 칸막이가 허리 위까지 반쯤 가린다*.
5. 오른쪽(동) 벽 남쪽: 서서 쓰는 샤워 부스 넷, 나무 문 건식 사우나실*.
6. 천장: 둥근 방습 커버 등(2화 '형광등', 모양은*). 바닥과 벽은 연한 아쿠아 화이트 타일*.

**사우나 입구 앞 복도**(1화 S#5⑤): 클럽 B1 중앙 복도 동쪽. 여탕 입구 유리문 틈으로 김이 새어 나온다(1화). 수건을 가득 실은 카트가 지나간다(1화).

### 7-3. 시간대별 조명

작중 시간이 오전 11시 하나뿐이라 **김의 농도**로 두 상태를 나눈다*.

| 회차·씬 | 시각 | 광원 | 색온도 | 방향 | 김 | 메모 |
|---|---|---|---|---|---|---|
| 2화 S#11 | 오전 11:00 | 천장 둥근 등 | 5000K, 김에 확산 | 위에서, 헤일로 | 짙음 | "김으로 하얗게 차 있었다"(2화) |
| 2화 S#13 | 오전 11:40 | 같음 | 5000K | 위에서 | 새 비닐을 갈자 크게 일어남 | 바가지 물로 김이 '확'(2화) |
| 2화 S#15 | 오전 11:42 | 같음 | 5000K | 위에서 | 천천히 내려앉아 투명해짐 | 펌프 소리만 남는다(2화) |
| 5화 S#11 | 오전 11:00(10/5) | 같음 + 열탕 물빛 반사 | 5000K | 위에서, 물에서 반사 | 중간 | 세신사의 얼굴은 김에 가려 이마만(5화) |
| 1화 S#5⑤ | 오후 3:00 | 복도 다운라이트 | 4000K | 위에서 | 입구 틈으로 새는 김 | 복도는 건조하고 밝다* |

**대표 색**: `#F1F3F2` 김 · `#D6E3E1` 아쿠아 화이트 타일 · `#8FC2C0` 열탕 물 · `#8E9696` 젖은 석재 · `#E9A6B3` 분홍 세신복(순옥, 색 기준)

### 7-4. 소리·냄새

- **소리**: 탕의 순환 펌프가 쉬지 않고 물을 뱉는 소리(2화). 바가지가 타일에 부딪히는 소리(2화). 바가지로 물을 붓는 '촤아'(2화). 탕으로 떨어지는 물, 대야끼리 부딪는 소리(5화). 복도의 카트 바퀴 '덜컹, 덜컹'(1화).
- **냄새**: 쑥 비누, 락스, 젖은 이태리타월(2화). 쑥 비누와 뜨거운 타일(5화). 복도에서는 쑥과 락스가 한꺼번에 밀려 나온다(1화).

### 7-5. 반복 소품과 위치

| 소품 | 위치 | 근거 |
|---|---|---|
| 투명 비닐 | 세신대 위 | 2화 |
| 바가지, 대야 | 세신 코너 선반과 바닥 | 2·5화 |
| 이태리타월 | 선반, 순옥의 손 | 2·5화 |
| 쑥 비누 | 선반 | 2·5화 |
| 방수팩에 든 휴대폰 | 세신대 옆 선반 | 2화 S#13 |
| 반으로, 다시 반으로 접은 수건 | 세신대 위 | 5화 S#11 |
| 수건 카트 | B1 복도 | 1화 S#5⑤ |

### 7-6. 카메라 자리

| 자리 | 높이·방향 | 핵심 장면 |
|---|---|---|
| C1 열탕 턱 | 앉은 눈높이, 동쪽 세신 코너 쪽. 김 너머 세신대 | 2화 S#11 와이드, 5화 S#11 혜숙의 자리에서 |
| C2 세신대 머리 쪽 | 세신대 높이 로우 앵글, 상판을 따라 | 2화 S#13 방수팩 휴대폰 Insert, S#15 멈춘 타월 |
| C3 세신 코너 위 | 부감. 바가지·대야·접힌 수건 | 5화 S#11 수건 Insert, 2화 S#11 새 비닐 |
| C4 여탕 입구 앞 B1 복도 | 눈높이, 복도를 따라. 입구에서 새는 김과 카트 | 1화 S#5⑤, 2화 S#12 입구 |

### 7-7. 노출 관리 장치 (관능 장면 없음, 나체 공간)

bible은 이 장소에 관능 톤을 섞지 말라고 한다. 대신 노출을 다룬다.
1. **김**: 화면 앞쪽에 두꺼운 수증기 층을 둔다. 인물은 등과 어깨까지만 김 밖에 있다*.
2. **반투명 유리 칸막이**: 세신 코너를 욕장 쪽에서 볼 때 허리 아래를 가린다*.
3. **세신대 자세와 수건**: 엎드린 등만 보여 주고 허리 아래는 수건으로 덮는다*.
4. **컷을 넘길 사물**: 바가지 물을 붓는 순간의 김 폭발(2화 S#13), 멈춘 이태리타월(2화 S#15), 접힌 수건의 네 모서리(5화).

### 7-8. SET LOCK (106 words)

```text
The scrub corner of a women's bathhouse in the basement sauna of a new Korean apartment complex community center. Wet pale aqua-white tiles on walls and floor, thick white steam hanging everywhere, round ceiling lights glowing like blurred moons through the steam, no windows. Two scrub tables covered with clear plastic sheets, plastic basins and dippers stacked on a wall shelf, a bar of mugwort soap, folded white towels. Right beside the scrub corner, a hot bath with a tiled rim to sit on and water circulating from a spout; a row of low seated shower stations along the far wall, a frosted glass half partition.
```

### 7-9. 프롬프트

**E1 빈 배경 — 김이 짙은 오전 11시** (2화 S#11)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The scrub corner of a women's bathhouse in the basement sauna of a new Korean apartment complex community center. Wet pale aqua-white tiles on walls and floor, thick white steam hanging everywhere, round ceiling lights glowing like blurred moons through the steam, no windows. Two scrub tables covered with clear plastic sheets, plastic basins and dippers stacked on a wall shelf, a bar of mugwort soap, folded white towels. Right beside the scrub corner, a hot bath with a tiled rim to sit on and water circulating from a spout; a row of low seated shower stations along the far wall, a frosted glass half partition.

Establishing view of the empty scrub corner at 11 am, steam so thick that the far shower stations fade to white. Round ceiling lights bloom into soft halos. A fresh clear plastic sheet spread over one scrub table, water beading on it, a dipper resting on the tile. Hot, humid, quiet, everyday working space, no sensual mood. Wide 16:9 composition. No logos, no watermark.
```

**E2 빈 배경 — 김이 내려앉은 뒤** (2화 S#15)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The scrub corner of a women's bathhouse in the basement sauna of a new Korean apartment complex community center. Wet pale aqua-white tiles on walls and floor, thick white steam hanging everywhere, round ceiling lights glowing like blurred moons through the steam, no windows. Two scrub tables covered with clear plastic sheets, plastic basins and dippers stacked on a wall shelf, a bar of mugwort soap, folded white towels. Right beside the scrub corner, a hot bath with a tiled rim to sit on and water circulating from a spout; a row of low seated shower stations along the far wall, a frosted glass half partition.

Establishing view of the same scrub corner minutes later, the steam slowly settling low so the room turns clearer and colder in tone: wet tiles shining, the hot bath surface rippling from the circulation spout, the basins and dippers on the shelf sharp and still. Stillness after something has stopped. Wide 16:9 composition. No logos, no watermark.
```

**C1 열탕 턱 → 세신 코너** (2화 S#11, 5화 S#11)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The scrub corner of a women's bathhouse in the basement sauna of a new Korean apartment complex community center. Wet pale aqua-white tiles on walls and floor, thick white steam hanging everywhere, round ceiling lights glowing like blurred moons through the steam, no windows. Two scrub tables covered with clear plastic sheets, plastic basins and dippers stacked on a wall shelf, a bar of mugwort soap, folded white towels. Right beside the scrub corner, a hot bath with a tiled rim to sit on and water circulating from a spout; a row of low seated shower stations along the far wall, a frosted glass half partition.

Camera at seated height on the tiled rim of the hot bath, the water surface steaming in the near foreground, looking east into the scrub corner: two plastic-covered scrub tables half hidden behind drifting steam and the frosted glass half partition, a shelf of basins on the wall. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C2 세신대 머리 쪽 로우 앵글** (2화 S#13·15)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The scrub corner of a women's bathhouse in the basement sauna of a new Korean apartment complex community center. Wet pale aqua-white tiles on walls and floor, thick white steam hanging everywhere, round ceiling lights glowing like blurred moons through the steam, no windows. Two scrub tables covered with clear plastic sheets, plastic basins and dippers stacked on a wall shelf, a bar of mugwort soap, folded white towels. Right beside the scrub corner, a hot bath with a tiled rim to sit on and water circulating from a spout; a row of low seated shower stations along the far wall, a frosted glass half partition.

Low angle at the head end of a scrub table, lens level with the plastic sheet: water droplets on the plastic in sharp focus, a rolled green scrub mitt lying still on the sheet, and on the small shelf beside it a smartphone inside a clear waterproof pouch, screen dark. Steam softening the background. Vertical 9:16 webtoon panel, detail shot. No logos, no watermark.
```

**C3 세신 코너 부감** (5화 S#11)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The scrub corner of a women's bathhouse in the basement sauna of a new Korean apartment complex community center. Wet pale aqua-white tiles on walls and floor, thick white steam hanging everywhere, round ceiling lights glowing like blurred moons through the steam, no windows. Two scrub tables covered with clear plastic sheets, plastic basins and dippers stacked on a wall shelf, a bar of mugwort soap, folded white towels. Right beside the scrub corner, a hot bath with a tiled rim to sit on and water circulating from a spout; a row of low seated shower stations along the far wall, a frosted glass half partition.

Top-down view over the scrub corner: two scrub tables side by side, a white towel folded in half and in half again lying neatly on one with its four corners exactly aligned, plastic basins and a dipper on the wet tile floor, a drain grate, thin steam drifting across. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C4 여탕 입구 앞 B1 복도** (1화 S#5⑤, 2화 S#12)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The scrub corner of a women's bathhouse in the basement sauna of a new Korean apartment complex community center. Wet pale aqua-white tiles on walls and floor, thick white steam hanging everywhere, round ceiling lights glowing like blurred moons through the steam, no windows. Two scrub tables covered with clear plastic sheets, plastic basins and dippers stacked on a wall shelf, a bar of mugwort soap, folded white towels. Right beside the scrub corner, a hot bath with a tiled rim to sit on and water circulating from a spout; a row of low seated shower stations along the far wall, a frosted glass half partition.

Different area: the dry, brightly lit basement corridor of the community center outside the women's sauna entrance. A frosted glass entrance door slightly open with steam curling out, a laundry cart stacked high with folded white towels standing by the wall, long corridor perspective toward a glass door at the far end. Vertical 9:16 webtoon panel. No logos, no watermark.
```

### 7-10. 고증 메모

- 신축 대단지 커뮤니티 사우나는 대중목욕탕보다 작고, 세신(때밀이)은 입점 업자나 위탁업체가 운영하는 경우가 있다. 추측입니다: 커뮤니티 사우나에 세신 코너가 있는 단지가 얼마나 흔한지는 확인하지 못했다. 작중 설정으로 둔다.
- 세신대에 비닐을 깔고 손님마다 가는 것, 쑥 비누, 이태리타월, 분홍·빨강 세신복은 한국 목욕탕의 일반적인 풍경이다(세신복은 **분홍**, bible 3-3).
- 신축 사우나의 천장 조명은 방습형 LED가 일반적이다. 소설의 '형광등'은 둥근 방습 커버 등으로 그려 두 표현을 함께 만족시킨다*.
- 격주 화요일 세신(유진), 사십 년 세신 경력(순옥)은 bible과 같다.

---

## 8. 지하 2층 주차장 B구역·동 연결통로·엘리베이터 홀

### 8-1. 공간 개요

- **위치**: 단지 전체 아래로 이어진 통합 지하주차장의 지하 2층. 열다섯 개 동의 지하가 통로로 이어져 있다(1화).
- **B구역**: 단지 남쪽 가운데, 101동 엘리베이터 홀과 중앙광장 아래 사이*. 101동 엘리베이터 홀과 동 연결통로 입구가 B구역 북쪽 끝에 붙어 있다*. 출구 경사로는 B구역 남쪽 끝에서 위로 굽어 오른다*.
- **규격**: 기둥 간격 8.1m, 천장고(보 아래) 2.3m*. 구역 표지색은 B구역 = 주황*.
- **그의 자리**: B구역 동쪽 벽 쪽 칸. 앞을 벽에 대고 세워 트렁크가 통로를 본다(트렁크 장면이 많아서*).
- **바닥 도색**: 9/19 오후 5시부터 B구역 바닥 도색 작업(3화 안내방송). 그래서 **9/20 이후 컷의 B구역 바닥은 새 녹색 에폭시로 반들거리고**, 9/19 이전 컷은 타이어 자국이 남은 바랜 바닥이다*.
- **등장 근거**
  - 1화 S#1 B구역(새벽 5:10), S#5① 운전석(오전 9:10), S#5③ 연결통로·엘리베이터 홀 몽타주
  - 2화 S#2 503동 엘리베이터 안(B2로 내려감)
  - 3화 S#7 B구역 트렁크(저녁 6:40), S#10 B구역·BMW 안(밤 8:20~8:40)
  - 4화 S#1·6 B구역 도색으로 차를 뺌(대사)
  - 6화 S#1~2 B구역 운전석·트렁크(저녁 6:30~6:36), S#4 연결통로와 503동 지하 엘리베이터 홀(6:44~6:47), S#9 101동 아래 연결통로(7:20), S#13 B구역 견인(8:10)

### 8-2. 평면 배치

**B구역** (북쪽 끝 101동 엘리베이터 홀 유리문을 등지고 남쪽 출구 경사로를 볼 때, 시계방향)
1. 왼쪽(동): 벽을 따라 주차칸 한 줄*. 그 가운데쯤, 기둥 사이 칸에 로고 없는 검정 대형 세단(검정 BMW 7시리즈, 238노 7171)*. 그 위 천장에 제트팬 하나(1화 "천장 어딘가에서 환풍기", 위치는*).
2. 정면(남): 출구 경사로가 위로 굽어 오른다*. 경사로 입구 위에 높이 제한바*. 6화 견인차가 이 경사로로 올라간다(6화 "출구 경사로").
3. 오른쪽(서): 통로 건너편 주차칸 줄*. 기둥마다 허리 높이에 주황 띠, 그 위 흰 구역 표지판(글자는 식자)*. 소화전함 하나*.
4. 등 뒤(북): 101동 엘리베이터 홀 유리 자동문(가운데)과 동 연결통로 입구(오른쪽, 서쪽)*.
5. 천장 조명: 형광등처럼 보이는 직관형 등기구 두 줄. 새벽과 늦은 저녁에는 한 줄 건너 하나씩 꺼져 '반만' 켜진다(1·3화)*.
6. 바닥: 녹색 에폭시, 흰 주차선, 주황 구역선. 젖은 듯 번들거린다(1화)*.

**동 연결통로** (101동 쪽 입구에서 통로 안을 볼 때)
- 폭 3m, 높이 2.4m의 긴 흰 통로*. 허리 높이에 동 번호별 색띠*. 천장에 형광등형 등기구 한 줄*.
- 101동 아래 구간에서 등 하나가 깜빡인다(6화 S#9).
- 분기 두 개: 지상으로 오르는 '출구 쪽 계단'과 상가로 이어지는 '상가 쪽 통로'(6화)*. 분기 지점 벽에 방향 표지판(글자는 식자)*.
- 바닥은 연회색 에폭시, 발소리가 울린다*.

**엘리베이터 홀** (동마다 같은 규격, 101동·503동 B2 홀)
- 유리 자동문 → 폭 2.5m × 깊이 5m 홀*. 엘리베이터 두세 대, 벽은 흰 대형 타일, 바닥은 회색 포셀린*. 천장 돔 CCTV 하나*.
- 304동: 3호기 엘리베이터 천장 CCTV에 '고장' 스티커(1화 S#5③, 7월부터 고장).
- 207동: 화물용 엘리베이터. 벽에 보호용 담요가 덮여 있다(1화 S#5③). 6화에는 '정기 점검 중' 팻말(6화 S#6).
- 412동: 엘리베이터를 B2에서 타지 않고 비상계단으로 2층까지 걸어 오른 뒤 탄다(1화). 비상계단 문은 홀 옆 철문*.
- 503동: B2에서 24층 직행(1화). 6화 S#4 부녀회 임원 셋이 이 홀의 엘리베이터 안에 서 있다.

### 8-3. 시간대별 조명

| 회차·씬 | 시각 | 광원 | 색온도 | 방향 | 메모 |
|---|---|---|---|---|---|
| 1화 S#1 | 새벽 5:10 | 천장 직관등 반만 + 열린 트렁크 실내등 | 4500K, 약간 녹색 기 / 트렁크 3000K | 위에서 띄엄띄엄, 바닥에 길게 번진 반사 | 바닥이 젖어 번들거린다(1화) |
| 1화 S#5① | 오전 9:10 | 천장 직관등 전부 | 4500K | 위에서. 앞유리에 길쭉하게 번진다(1화) | 출근 차 타이어가 경사로를 긁는다 |
| 3화 S#7·10 | 저녁 6:40, 밤 8:20 | 반만 켜짐 | 4500K | 위에서 | 하늘색과 민트가 같은 색으로 보이는 빛(3화). 색이 죽은 빛으로 그린다* |
| 6화 S#1~2 | 저녁 6:30 | 전부 켜짐 + 퇴근 차 헤드라이트 | 4500K / 헤드라이트 5500K | 경사로 쪽에서 기둥을 하나씩 훑는다(6화) | 배기가스 연무* |
| 6화 S#9 | 저녁 7:20 | 연결통로 등 한 줄, 하나 깜빡 | 4500K | 위에서 | 통로 끝은 어둡다* |
| 6화 S#13 | 저녁 8:10 | 천장 직관등 + 견인차 노란 경광등 회전 | 4500K / 노랑 | 경광등이 기둥을 돌아가며 핥는다(6화) | 경찰차 붉은·푸른 등이 경사로 위에서 비친다* |

**대표 색**: `#DDE8E0` 직관등 빛 · `#8A8C88` 콘크리트 · `#4F6B5A` 녹색 에폭시 · `#E58A2E` B구역 주황 · `#F5B700` 경광등 노랑

### 8-4. 소리·냄새

- **소리**: 환풍기의 낮은 웅웅(1·6화). 타이어가 경사로를 긁는 소리(1화). 트렁크 닫히는 '쿵'(1화). 휴대폰 진동(6화). 유압 장치 '끼익'(6화). 엘리베이터 '띵'. 통로를 뛰는 발소리와 주머니 속 병이 짤랑대는 소리(6화 S#4).
- **냄새**: 젖은 콘크리트와 타이어 고무(1화). 배기가스와 젖은 콘크리트 위에 얇게 뜬 향수(6화). 기름(6화). 9/20 이후에는 새 도료 냄새가 며칠 남는다*.

### 8-5. 반복 소품과 위치

| 소품 | 위치 | 근거 |
|---|---|---|
| 공구함(향수 다섯 병, 뚜껑 회색·버건디·민트·하늘색·금색) | 트렁크 안 | 1·3·6화 |
| 셔츠 다섯 벌 | 트렁크 안 옷걸이 | 3화 S#7 |
| 접이식 전동킥보드, 형광 연두 대리운전 조끼 | 트렁크 안 | 1화 S#1 |
| 포장도 안 뜯은 명품 상자 다섯 개 | 트렁크 안 | 6화 S#2 |
| 투명 테이프 한 롤, 접힌 쇼핑백 네 장, 띠지 두른 돈다발 한 묶음 | 공구함 안 | 6화 S#13 |
| '고장' 스티커 | 304동 3호기 천장 CCTV | 1화 S#5③ |
| 보호용 담요 | 207동 화물용 엘리베이터 벽 | 1화 S#5③ |
| 견인차, 리스사 클립보드 | B구역 통로 | 6화 S#13 |

### 8-6. 카메라 자리

| 자리 | 높이·방향 | 핵심 장면 |
|---|---|---|
| C1 트렁크 안쪽 | 트렁크 바닥 높이, 밖을 향해. 공구함과 천장 직관등 | 1화 S#1, 3화 S#7·10, 6화 S#2·13 |
| C2 B구역 통로 가운데 | 눈높이, 남쪽 경사로 쪽. 기둥 줄 원근 | 6화 S#1 헤드라이트, S#13 견인 |
| C3 동 연결통로 | 눈높이, 소실점 정면. 깜빡이는 등과 분기 | 6화 S#9, S#4 질주 |
| C4 지하 엘리베이터 홀 | 눈높이, 엘리베이터 문 정면 | 6화 S#4 503동 "어머니가 몇 분이세요?", 1화 S#5③ |

### 8-7. 수위 장치

관능 장면이 없다. 해당 없음.

### 8-8. SET LOCK (94 words)

```text
Underground parking level B2, zone B, of a new 2024-built Korean mega apartment complex. A low concrete ceiling with exposed ducts and jet fans, two long rows of linear tube lights, square concrete columns wrapped with orange zone bands at waist height, a glossy green epoxy floor with white parking lines, slightly wet and reflective. An exit ramp curving upward at the far end. Behind, a glass automatic door into a bright elevator lobby and the mouth of a long white underground corridor that links the fifteen apartment buildings. Cool, humming, damp and empty.
```

### 8-9. 프롬프트

**E1 빈 배경 — 새벽 5:10 반만 켜진 등** (1화 S#1)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Underground parking level B2, zone B, of a new 2024-built Korean mega apartment complex. A low concrete ceiling with exposed ducts and jet fans, two long rows of linear tube lights, square concrete columns wrapped with orange zone bands at waist height, a glossy green epoxy floor with white parking lines, slightly wet and reflective. An exit ramp curving upward at the far end. Behind, a glass automatic door into a bright elevator lobby and the mouth of a long white underground corridor that links the fifteen apartment buildings. Cool, humming, damp and empty.

Establishing view of zone B at 5:10 am. Only every other tube light is on, leaving the space in stripes of light and dark; the wet green floor mirrors the lights in long smears. A black full-size luxury sedan without any visible logos is parked nose-in against the wall on the left, its trunk lid open, a small warm trunk light glowing. No other cars nearby. Lonely, secretive dawn. Wide 16:9 composition. No logos, no watermark.
```

**E2 빈 배경 — 저녁 6:30 퇴근 헤드라이트** (6화 S#1)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Underground parking level B2, zone B, of a new 2024-built Korean mega apartment complex. A low concrete ceiling with exposed ducts and jet fans, two long rows of linear tube lights, square concrete columns wrapped with orange zone bands at waist height, a glossy green epoxy floor with white parking lines, slightly wet and reflective. An exit ramp curving upward at the far end. Behind, a glass automatic door into a bright elevator lobby and the mouth of a long white underground corridor that links the fifteen apartment buildings. Cool, humming, damp and empty.

Establishing view of zone B at 6:30 pm on a Friday. All tube lights on, cars filling most spaces, headlights from cars coming down the curved ramp sweeping across the columns one by one, a faint haze of exhaust in the beams. The black logo-free sedan parked against the left wall. Busy, rushed, ticking-clock mood. Wide 16:9 composition. No logos, no watermark.
```

**C1 트렁크 안쪽 → 밖** (1화 S#1, 3화 S#7·10, 6화 S#2)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Underground parking level B2, zone B, of a new 2024-built Korean mega apartment complex. A low concrete ceiling with exposed ducts and jet fans, two long rows of linear tube lights, square concrete columns wrapped with orange zone bands at waist height, a glossy green epoxy floor with white parking lines, slightly wet and reflective. An exit ramp curving upward at the far end. Behind, a glass automatic door into a bright elevator lobby and the mouth of a long white underground corridor that links the fifteen apartment buildings. Cool, humming, damp and empty.

Camera placed inside the open trunk of the black sedan at trunk-floor level, looking out. In the foreground an opened black tool case lined with foam: instead of wrenches, five small perfume bottles lie side by side with caps in grey, burgundy, mint, sky blue and gold. A folded fluorescent yellow-green vest and a folding electric scooter at the side, five white shirts on hangers above. Beyond the trunk lid, the half-lit parking ceiling. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C2 B구역 통로 → 출구 경사로** (6화 S#1·13)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Underground parking level B2, zone B, of a new 2024-built Korean mega apartment complex. A low concrete ceiling with exposed ducts and jet fans, two long rows of linear tube lights, square concrete columns wrapped with orange zone bands at waist height, a glossy green epoxy floor with white parking lines, slightly wet and reflective. An exit ramp curving upward at the far end. Behind, a glass automatic door into a bright elevator lobby and the mouth of a long white underground corridor that links the fifteen apartment buildings. Cool, humming, damp and empty.

Camera in the middle of the zone B driving aisle at eye level, looking south down the receding rows of orange-banded columns toward the curving exit ramp. At night, a yellow tow truck's rotating amber beacon light sweeps across the columns and ceiling, glinting on the fresh glossy green floor paint; faint red and blue police light reflecting from the top of the ramp. Wide 16:9 composition. No logos, no watermark.
```

**C3 동 연결통로** (6화 S#9·S#4)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Underground parking level B2, zone B, of a new 2024-built Korean mega apartment complex. A low concrete ceiling with exposed ducts and jet fans, two long rows of linear tube lights, square concrete columns wrapped with orange zone bands at waist height, a glossy green epoxy floor with white parking lines, slightly wet and reflective. An exit ramp curving upward at the far end. Behind, a glass automatic door into a bright elevator lobby and the mouth of a long white underground corridor that links the fifteen apartment buildings. Cool, humming, damp and empty.

Camera inside the long white underground corridor linking the buildings, eye level, one-point perspective. A single line of tube lights along the ceiling, one of them flickering dimly. Color bands at waist height along the walls. Ahead the corridor splits: a stairway leading up to the left and a corridor toward the shopping street to the right, with a blank direction sign at the junction. Echoing, cold, decision point. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C4 지하 엘리베이터 홀** (6화 S#4, 1화 S#5③)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Underground parking level B2, zone B, of a new 2024-built Korean mega apartment complex. A low concrete ceiling with exposed ducts and jet fans, two long rows of linear tube lights, square concrete columns wrapped with orange zone bands at waist height, a glossy green epoxy floor with white parking lines, slightly wet and reflective. An exit ramp curving upward at the far end. Behind, a glass automatic door into a bright elevator lobby and the mouth of a long white underground corridor that links the fifteen apartment buildings. Cool, humming, damp and empty.

Camera in a basement elevator lobby facing two stainless steel elevator doors, one of them sliding open with bright cabin light spilling out onto the grey porcelain floor. White large-format wall tiles, a dome security camera on the ceiling, a glass automatic door reflected faintly at the side. Vertical 9:16 webtoon panel. No logos, no watermark.
```

### 8-10. 고증 메모

- 2020년대 수도권 신축 대단지는 지상에 차가 없고, 지하주차장이 단지 전체를 하나로 잇는다. 각 동 엘리베이터가 지하 주차층까지 내려온다. 그가 '지상으로 다니지 않는' 규칙(1화)은 이 구조 덕분이다.
- 신축 지하주차장 조명은 대부분 LED이고 센서·시간대별 절전 운영을 한다. 소설의 '형광등이 반만 켜져 있었다'는 형광등처럼 생긴 직관형 LED의 절전 운영으로 그린다*. 추측입니다: 절전 패턴(한 줄 건너 하나)은 단지마다 다르다.
- 지하주차장을 구역(A·B·C…)과 색으로 나누는 표지 체계는 흔하다. B = 주황은 이 작품에서 정한 것이다*.
- 바닥 도색(에폭시) 작업 공지를 단지 방송으로 하는 것은 흔한 관리 업무다(3화).
- 세대카드로 동 출입문과 연결통로 문을 여는 방식은 신축의 일반 사양이다. 그가 101동 3801호 카드 한 장으로 클럽 게이트와 B2 연결통로를 지나는 이유다(bible 3-2).
- 차량 번호판 '238노 7171'은 가공 번호다. 작화에서 번호판은 흐리게 처리하고 숫자는 식자로 넣는다*.

---

## 9. 수원지방법원 형사법정

### 9-1. 공간 개요

- **시점**: 2027년 2월 18일(목) 오전 10시, 1심 선고(6화 S#14, bible 연표).
- **법정**: 판사 한 명이 앉는 형사 단독 법정으로 그린다(소설과 대본 모두 '판사' 한 사람)*. 크기 약 15m × 12m, 천장고 4.5m*.
- **창**: 한쪽 측벽 높은 곳에 창이 있다(6화 "높은 창으로 들어온 빛"). 창 아래 벽에 라디에이터(6화).
- **법봉 없음**(SPEC, 6화). 법대 위에 법봉이나 받침을 절대 그리지 않는다.
- **등장 근거**: 6화 S#14 단 한 씬.

### 9-2. 평면 배치

(방청석 맨 뒤 출입문을 등지고 앞쪽 법대를 볼 때, 시계방향)
1. 왼쪽 측벽: 높은 창 네 개, 바닥에서 2.8m 위부터 천장 근처까지*. 창 아래 벽에 라디에이터 패널*. 겨울빛이 이 창들로 비스듬히 들어온다.
2. 정면 왼쪽: 검사석. 긴 책상과 마이크*. 추측입니다: 방청석에서 보아 검사석이 왼쪽인지 오른쪽인지는 법정마다 확인하지 못했다. 이 작품에서는 왼쪽으로 고정한다*.
3. 정면 가운데: 바닥보다 세 단 높은 목재 법대. 가운데 판사석 의자 하나*. 법대 위에는 서류철과 작은 모니터만 있다*. 법대 바로 앞 낮은 단에 참여관·실무관석*. 그 앞 가운데에 증인석*.
4. 정면 오른쪽: 피고인·변호인석*. 그 뒤 벽에 피고인 출입문(구속 피고인 대기실로 이어지는 문, 교도관이 데려가는 문)*.
5. 오른쪽 측벽: 목재 패널 벽과 벽시계*.
6. 방청석: 법정 앞부분과 낮은 나무 난간으로 나뉜다*. 긴 나무 의자 여섯 줄이 가운데 통로를 사이에 두고 좌우로 놓인다*.
   - 둘째 줄: 유진을 가운데 두고 미란, 세라, 하린, 혜숙(6화, bible 3-1 라인업).
   - 맨 뒷줄: 순옥(6화). 판결 뒤 의자 위에 접힌 손수건 하나.
7. 등 뒤: 방청석 출입문 두 개*.

### 9-3. 시간대별 조명

작중 시각은 오전 10시 하나뿐이다. 두 번째 상태는 같은 시각의 '폐정 뒤'로 둔다*.

| 상태 | 시각 | 광원 | 색온도 | 방향 | 메모 |
|---|---|---|---|---|---|
| 선고 중(6화 S#14) | 오전 10:00 | 높은 창의 겨울빛 + 천장 매입 LED 패널 | 창 6500K, 희고 얇게 / 천장 4500K | 왼쪽 측벽 높은 곳에서 비스듬히 아래로. 바닥과 방청석에 창 모양 빛 | "희고 얇았다"(6화) |
| 폐정 뒤* | 오전 10:20 | 천장 패널 절반 꺼짐, 창빛만 남음* | 6500K | 같음 | 맨 뒷줄 의자의 손수건만 빛 안에 있다* |

**대표 색**: `#EDEFF2` 겨울빛 · `#8B6A4A` 목재 패널 · `#D9D2C5` 베이지 벽 · `#4A3B30` 방청석 나무 · `#5C6168` 회색 코트 톤

### 9-4. 소리·냄새

- **소리**: 라디에이터가 '똑딱똑딱' 식어 가는 소리(6화). 판결문 낭독(6화). 등 뒤 바스락거리다 멈추는 소리(6화). 다음 사건 번호를 부르는 법정 경위(6화).
- **냄새**: 젖은 모직 코트와 바닥 왁스(6화).

### 9-5. 반복 소품과 위치

| 소품 | 위치 | 근거 |
|---|---|---|
| 판결문, 서류철 | 법대 위 | 6화 |
| 피고인석 의자 | 정면 오른쪽 | 6화 |
| 반듯하게 접힌 손수건 하나 | 방청석 맨 뒷줄 의자 위 | 6화 S#14 |
| 법봉 | **없음** | SPEC, 6화 |

### 9-6. 카메라 자리

| 자리 | 높이·방향 | 핵심 장면 |
|---|---|---|
| C1 방청석 맨 뒷줄 | 앉은 눈높이, 법대 정면 | 6화 S#14 시작, 판결문 낭독 |
| C2 법대 옆 | 높은 앵글, 방청석을 내려다봄 | 둘째 줄 다섯 명과 맨 뒷줄, 유진이 돌아보는 순간 |
| C3 맨 뒷줄 의자 | 의자 높이 클로즈 | S#14 마지막 Insert, 접힌 손수건 |
| C4 피고인석 옆 | 낮은 앵글, 피고인 출입문 쪽 | 교도관이 그를 데려가는 문, 깃 없는 수용복 |

### 9-7. 수위 장치

관능 장면이 없다. 해당 없음.

### 9-8. SET LOCK (110 words)

```text
A criminal courtroom of the Suwon District Court in South Korea, modern and austere. A raised wooden judge's bench at the front with a single judge's chair, papers and a small monitor on it, absolutely no gavel. A clerk's desk just below the bench and a witness stand in the center. The prosecutor's table on the left, the defendant and defense table on the right with a plain side door for detainees. A low wooden railing separates six rows of long wooden public benches with a center aisle. Warm brown wood paneling, beige walls, tall high windows on the left wall letting in thin white winter light, radiators beneath them.
```

### 9-9. 프롬프트

**E1 빈 배경 — 오전 10:00 선고 직전** (6화 S#14)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A criminal courtroom of the Suwon District Court in South Korea, modern and austere. A raised wooden judge's bench at the front with a single judge's chair, papers and a small monitor on it, absolutely no gavel. A clerk's desk just below the bench and a witness stand in the center. The prosecutor's table on the left, the defendant and defense table on the right with a plain side door for detainees. A low wooden railing separates six rows of long wooden public benches with a center aisle. Warm brown wood paneling, beige walls, tall high windows on the left wall letting in thin white winter light, radiators beneath them.

Establishing view of the empty courtroom at 10 am in February, seen from the back of the public gallery. Pale white winter light falls diagonally from the high left windows across the benches and floor in long window shapes; ceiling panels add a flat cool light. The judge's bench waits empty and formal. Quiet, cold, final. Wide 16:9 composition. No logos, no emblems, no watermark.
```

**E2 빈 배경 — 폐정 뒤, 창빛만** (6화 S#14 끝)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A criminal courtroom of the Suwon District Court in South Korea, modern and austere. A raised wooden judge's bench at the front with a single judge's chair, papers and a small monitor on it, absolutely no gavel. A clerk's desk just below the bench and a witness stand in the center. The prosecutor's table on the left, the defendant and defense table on the right with a plain side door for detainees. A low wooden railing separates six rows of long wooden public benches with a center aisle. Warm brown wood paneling, beige walls, tall high windows on the left wall letting in thin white winter light, radiators beneath them.

Establishing view of the same courtroom just after the session, half the ceiling lights off so the room is mostly lit by the thin winter light from the high windows. Empty benches, an empty defendant's chair, dust floating in the light beams. Hollow, still, aftermath. Wide 16:9 composition. No logos, no emblems, no watermark.
```

**C1 방청석 맨 뒷줄 → 법대** (6화 S#14)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A criminal courtroom of the Suwon District Court in South Korea, modern and austere. A raised wooden judge's bench at the front with a single judge's chair, papers and a small monitor on it, absolutely no gavel. A clerk's desk just below the bench and a witness stand in the center. The prosecutor's table on the left, the defendant and defense table on the right with a plain side door for detainees. A low wooden railing separates six rows of long wooden public benches with a center aisle. Warm brown wood paneling, beige walls, tall high windows on the left wall letting in thin white winter light, radiators beneath them.

Camera at seated eye level in the last row of the public gallery, the backs of the wooden benches leading the eye down the center aisle to the raised judge's bench far ahead. Winter light slanting in from the high windows on the left. Vertical 9:16 webtoon panel. No logos, no emblems, no watermark.
```

**C2 법대 옆 → 방청석 부감** (6화 S#14)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A criminal courtroom of the Suwon District Court in South Korea, modern and austere. A raised wooden judge's bench at the front with a single judge's chair, papers and a small monitor on it, absolutely no gavel. A clerk's desk just below the bench and a witness stand in the center. The prosecutor's table on the left, the defendant and defense table on the right with a plain side door for detainees. A low wooden railing separates six rows of long wooden public benches with a center aisle. Warm brown wood paneling, beige walls, tall high windows on the left wall letting in thin white winter light, radiators beneath them.

High angle from beside the judge's bench looking down over the low wooden railing at the six rows of public benches, the second row and the last row clearly readable, a band of pale window light lying across the middle rows. Vertical 9:16 webtoon panel. No logos, no emblems, no watermark.
```

**C3 맨 뒷줄 의자 위 손수건** (6화 S#14 마지막)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A criminal courtroom of the Suwon District Court in South Korea, modern and austere. A raised wooden judge's bench at the front with a single judge's chair, papers and a small monitor on it, absolutely no gavel. A clerk's desk just below the bench and a witness stand in the center. The prosecutor's table on the left, the defendant and defense table on the right with a plain side door for detainees. A low wooden railing separates six rows of long wooden public benches with a center aisle. Warm brown wood paneling, beige walls, tall high windows on the left wall letting in thin white winter light, radiators beneath them.

Close view at bench height of the empty last row: on the worn wooden seat lies one plain cotton handkerchief folded in half and in half again, its four corners exactly aligned, touched by a single strip of thin winter light. The rest of the row empty and shadowed. Vertical 9:16 webtoon panel, still-life detail. No logos, no emblems, no watermark.
```

**C4 피고인석 옆 → 피고인 출입문** (6화 S#14)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A criminal courtroom of the Suwon District Court in South Korea, modern and austere. A raised wooden judge's bench at the front with a single judge's chair, papers and a small monitor on it, absolutely no gavel. A clerk's desk just below the bench and a witness stand in the center. The prosecutor's table on the left, the defendant and defense table on the right with a plain side door for detainees. A low wooden railing separates six rows of long wooden public benches with a center aisle. Warm brown wood paneling, beige walls, tall high windows on the left wall letting in thin white winter light, radiators beneath them.

Low angle beside the defendant's table looking at the plain wooden side door for detainees in the right wall, the door slightly ajar onto a dim corridor, an empty chair pushed back from the table. Flat ceiling light, cooler and dimmer than the gallery side. Vertical 9:16 webtoon panel. No logos, no emblems, no watermark.
```

### 9-10. 고증 메모

- 한국 법정은 법봉을 쓰지 않는다. 판결은 판사가 판결문을 낭독해 선고한다(SPEC). 추측입니다: 법봉을 쓰지 않게 된 정확한 시점은 확인하지 못했다.
- 형법 제347조 사기는 법정형에 하한이 없어 원칙적으로 지방법원 단독판사 사건이다. 특정경제범죄법(이득액 5억 원 이상)이 적용되면 합의부로 간다. 작중 피해액 4억 1,870만 원은 다섯 명 합계이고, 피해자별로는 5억 원에 못 미친다. 그래서 단독 법정(판사 1인)으로 그린다. 추측입니다: 실제 사건 배당은 검사의 기소 죄명과 법원 사무분담에 따라 달라질 수 있다.
- 형사소송법 개정(2007년 무렵) 뒤로 피고인은 변호인과 나란히 앉고, 검사석과 마주 보는 배치가 일반적이다. 추측입니다: 정확한 시행 시점과 좌우 배치는 확인하지 못했다.
- 미결수용자는 재판에 나갈 때 사복을 입을 수 있다(형의 집행 및 수용자의 처우에 관한 법률). 작중 그는 수용복 차림이다(6화). 그가 사복을 마련하지 못한 것으로 읽는다*.
- 수원지방법원은 2019년 수원 광교의 새 청사로 옮겼다. 추측입니다: 새 청사 형사법정의 창 구조는 확인하지 못했다. 소설의 '높은 창'을 따른다.
- 법정 정면 벽의 법원 상징이나 글자는 그리지 않는다(실제 기관 표장 사용을 피한다)*.

---

## 10. 새솔신도시 '그랑블루 레이크' 모델하우스 — 에필로그

### 10-1. 공간 개요

- **시점**: 2029년 10월 16일(화) 오후 3시(6화 S#16).
- **위치**: 다른 신도시 '새솔신도시'의 견본주택(6화). 1층 로비와 그 뒤 견본 세대*.
- **로비 크기**: 약 30m × 20m, 천장고 7m*. 정면 유리 파사드는 남서향*.
- **핵심**: 로비 한가운데 유리 상자 안 단지 모형. 손톱만 한 나무, 성냥갑 같은 동 **열여섯 개**, 파란 아크릴 호수(6화). 모형의 동 배치는 레이크시티 더퍼스트처럼 호수 옆에서 중앙 광장을 빙 둘러싼 고리 모양이다. 그가 3년 전 살던 단지의 거울상이다*.
- **등장 근거**: 6화 S#16 로비, 화장실 거울. (6화 S#15 교도소 정문은 이 문서 범위 밖이다.)

### 10-2. 평면 배치

(정문 유리문을 등지고 안쪽을 볼 때, 시계방향)
1. 왼쪽: 흰 대리석 접수·안내데스크, 금색 몰딩*. 그 뒤 벽에 대형 LED 스크린(단지 투시도 영상)*.
2. 정면 가운데: 샹들리에 바로 아래, 허리 높이 받침 위 유리 상자 단지 모형(약 3m × 2m)*. 모형 오른쪽 옆에 세움 안내판 하나(6화 S#16 "피트니스 / 필라테스룸 / 골프연습장 / 사우나", 글자는 식자).
3. 정면 안쪽: 견본 세대 입구 두 개(타입 표지판, 글자는 식자)*. 왼쪽 안쪽 복도 끝에 화장실(6화 "화장실 거울 앞")*.
4. 오른쪽: 상담석 여덟 테이블. 흰 테이블, 회색 의자, 테이블마다 유선 전화(6화 "상담석 전화벨")*. 상담석 뒤 벽에 분양 일정 패널(글자 없음)*.
5. 등 뒤: 높이 7m 유리 파사드와 회전문이 아닌 양개 유리문*.

**화장실**: 흰 세면대 두 개, 벽 전체 거울, 거울 위 간접등*. 그가 3년 묵은 셔츠의 단추 두 개를 푸는 곳이다(6화).

### 10-3. 시간대별 조명

작중 시각은 오후 3시 하나뿐이다. 두 번째는 보조로 '폐관 직전 저녁'을 둔다*.

| 상태 | 시각 | 광원 | 색온도 | 방향 | 메모 |
|---|---|---|---|---|---|
| 6화 S#16 | 오후 3:00 | 그림자 없는 하얀 LED(천장 라인·다운라이트) + 샹들리에 + 유리 파사드의 오후 볕 | LED 5000K / 샹들리에 2700K / 볕 4500K | 위에서 고르게, 파사드 쪽에서 비스듬히 | "그림자 하나 없이 밝았다"(6화). 모형 상자 안 조명이 아크릴 호수를 푸르게 띄운다* |
| 보조: 폐관 직전* | 저녁 6:30 | 실내 LED만, 바깥은 어둠 | 5000K | 위에서 | 유리 파사드에 로비가 거울처럼 비친다* |

**대표 색**: `#F7F7F5` 흰 LED · `#D4B483` 샴페인 골드 · `#3E8EDB` 아크릴 호수 · `#CDB28A` 밝은 오크 · `#B7BDC4` 은회색

### 10-4. 소리·냄새

- **소리**: 피아노 배경음악, 띄엄띄엄 울리는 상담석 전화벨(6화).
- **냄새**: 새 벽지 풀 냄새와 드립커피(6화).

### 10-5. 반복 소품과 위치

| 소품 | 위치 | 근거 |
|---|---|---|
| 단지 모형(동 열여섯 개, 파란 아크릴 호수) | 로비 한가운데 유리 상자 | 6화 S#16 |
| 커뮤니티 시설 안내판 | 모형 오른쪽 옆 | 6화 S#16 |
| 상담 직원의 서류철 | 상담석 → 모형 앞 | 6화 S#16 |
| 화장실 거울 | 로비 안쪽 복도 끝 | 6화 S#16 |

### 10-6. 카메라 자리

| 자리 | 높이·방향 | 핵심 장면 |
|---|---|---|
| C1 정문 안쪽 | 눈높이, 로비 전체 와이드 | 6화 S#16 그가 로비로 들어섬 |
| C2 단지 모형 위 | 부감, 유리 상자 안 | 동 열여섯 개와 파란 호수 Insert |
| C3 모형 옆 안내판 | 눈높이 클로즈, 뒤로 흐린 상담석 | '사우나'에서 시선이 떨어지는 Insert |
| C4 화장실 거울 | 세면대 앞 정면 | 단추 두 개를 푸는 장면(거울에 비칠 자리만 비워 둔다) |

### 10-7. 수위 장치

관능 장면이 없다. 해당 없음.

### 10-8. SET LOCK (104 words)

```text
The sales model house lobby for a new lakeside apartment complex called Grand Bleu Lake in another Korean new town, bright and shadowless. White marble floor, white walls with champagne-gold trim, a crystal chandelier over the center. Under it, a large glass display case holding a detailed architectural scale model: sixteen white apartment towers in a ring around a central plaza, tiny trees, and a blue acrylic lake. A freestanding facility sign beside the model, a white marble reception desk on the left, rows of white consultation tables with grey chairs and desk phones on the right, a tall glass facade at the entrance.
```

### 10-9. 프롬프트

**E1 빈 배경 — 오후 3:00 그림자 없는 로비** (6화 S#16)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The sales model house lobby for a new lakeside apartment complex called Grand Bleu Lake in another Korean new town, bright and shadowless. White marble floor, white walls with champagne-gold trim, a crystal chandelier over the center. Under it, a large glass display case holding a detailed architectural scale model: sixteen white apartment towers in a ring around a central plaza, tiny trees, and a blue acrylic lake. A freestanding facility sign beside the model, a white marble reception desk on the left, rows of white consultation tables with grey chairs and desk phones on the right, a tall glass facade at the entrance.

Establishing view of the empty lobby at 3 pm. Shadowless white LED light everywhere, the chandelier sparkling warm above the model, afternoon sun slanting in through the glass facade at the back. The blue acrylic lake glows inside the display case. Polished, cheerful, endlessly repeating, a little hollow. Wide 16:9 composition. No logos, no watermark.
```

**E2 빈 배경 — 폐관 직전 저녁(보조)**
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The sales model house lobby for a new lakeside apartment complex called Grand Bleu Lake in another Korean new town, bright and shadowless. White marble floor, white walls with champagne-gold trim, a crystal chandelier over the center. Under it, a large glass display case holding a detailed architectural scale model: sixteen white apartment towers in a ring around a central plaza, tiny trees, and a blue acrylic lake. A freestanding facility sign beside the model, a white marble reception desk on the left, rows of white consultation tables with grey chairs and desk phones on the right, a tall glass facade at the entrance.

Establishing view of the same empty lobby at 6:30 pm near closing. Outside the glass facade it is dark, and the glass reflects the bright white interior like a mirror, doubling the chandelier and the model case. Consultation tables cleared, chairs pushed in. Too bright inside, nothing outside. Wide 16:9 composition. No logos, no watermark.
```

**C1 정문 안쪽 와이드** (6화 S#16)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The sales model house lobby for a new lakeside apartment complex called Grand Bleu Lake in another Korean new town, bright and shadowless. White marble floor, white walls with champagne-gold trim, a crystal chandelier over the center. Under it, a large glass display case holding a detailed architectural scale model: sixteen white apartment towers in a ring around a central plaza, tiny trees, and a blue acrylic lake. A freestanding facility sign beside the model, a white marble reception desk on the left, rows of white consultation tables with grey chairs and desk phones on the right, a tall glass facade at the entrance.

Camera just inside the glass entrance doors at eye level, looking straight across the lobby: the reception desk on the left, the glass model case under the chandelier in the center, the consultation tables on the right, and two blank sample-unit entrance portals at the back. Even white light, soft reflections on the marble floor. Wide 16:9 composition. No logos, no watermark.
```

**C2 단지 모형 부감** (6화 S#16 Insert)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The sales model house lobby for a new lakeside apartment complex called Grand Bleu Lake in another Korean new town, bright and shadowless. White marble floor, white walls with champagne-gold trim, a crystal chandelier over the center. Under it, a large glass display case holding a detailed architectural scale model: sixteen white apartment towers in a ring around a central plaza, tiny trees, and a blue acrylic lake. A freestanding facility sign beside the model, a white marble reception desk on the left, rows of white consultation tables with grey chairs and desk phones on the right, a tall glass facade at the entrance.

Top-down close view into the glass display case: the architectural scale model of sixteen small white towers standing in a ring around a tiny central plaza with a round fountain, fingernail-sized trees, and a shiny blue acrylic lake along one side lit from within. Faint reflections of the chandelier on the glass lid. Vertical 9:16 webtoon panel, miniature detail. No logos, no watermark.
```

**C3 모형 옆 안내판** (6화 S#16 Insert)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The sales model house lobby for a new lakeside apartment complex called Grand Bleu Lake in another Korean new town, bright and shadowless. White marble floor, white walls with champagne-gold trim, a crystal chandelier over the center. Under it, a large glass display case holding a detailed architectural scale model: sixteen white apartment towers in a ring around a central plaza, tiny trees, and a blue acrylic lake. A freestanding facility sign beside the model, a white marble reception desk on the left, rows of white consultation tables with grey chairs and desk phones on the right, a tall glass facade at the entrance.

Eye-level close view of a freestanding white and gold facility sign beside the model case, its panel showing four simple line icons for a fitness gym, a pilates room, a golf range and a sauna, with blank spaces where text will go. Behind it, the consultation area softly out of focus. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C4 화장실 거울** (6화 S#16)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The sales model house lobby for a new lakeside apartment complex called Grand Bleu Lake in another Korean new town, bright and shadowless. White marble floor, white walls with champagne-gold trim, a crystal chandelier over the center. Under it, a large glass display case holding a detailed architectural scale model: sixteen white apartment towers in a ring around a central plaza, tiny trees, and a blue acrylic lake. A freestanding facility sign beside the model, a white marble reception desk on the left, rows of white consultation tables with grey chairs and desk phones on the right, a tall glass facade at the entrance.

Different area in the same model house: a clean white restroom seen straight on from the sink, a wide wall mirror with a soft light strip above it, two white basins and a marble counter, the mirror reflecting an empty pale tiled wall behind the camera. Neutral, clinical, bright. Vertical 9:16 webtoon panel. No logos, no watermark.
```

### 10-10. 고증 메모

- 신규 분양 단지는 공급 지역 가까이에 견본주택(모델하우스)을 짓고, 로비 한가운데 단지 모형, 커뮤니티 시설 안내, 상담석, 타입별 견본 세대를 두는 구성이 일반적이다.
- 모형 속 커뮤니티 시설 네 가지(피트니스, 필라테스룸, 골프연습장, 사우나)가 레이크시티 더퍼스트와 같다. 2020년대 신축의 표준 구성이라 자연스럽고, 작품에서는 반복의 신호다.
- 견본주택 실내를 그림자 없이 밝게 하는 조명, 피아노 배경음악, 드립커피 대접은 흔한 연출이다. 추측입니다.

---

## 짧게 A. 304동 1204호 — 미란의 집

### A-1. 공간 개요

- **위치**: 304동 12층(SPEC). 304동은 단지 동쪽 줄에 있고 거실이 단지 안쪽(서쪽)을 본다*.
- **평형**: 공급 약 34평(전용 84㎡) 3베이*. 미란, 소이, 미란의 어머니가 함께 지낸다(bible).
- **창 방향**: 거실 서향. 오후 다섯 시 반, 서쪽 창으로 든 해 때문에 거실이 온통 와인색이다(4화).
- **엘리베이터**: 3호기. 천장 CCTV가 7월부터 고장이다(1화). 6화에는 12층까지 한 번도 서지 않는다.
- **등장 근거**: 4화 S#2·4·5 거실·식탁(오후 5:30~5:50), 6화 S#3 현관(저녁 6:41), 1화 S#5③ 3호기.

### A-2. 평면 배치

**현관**은 세대 동쪽, 복도 쪽에 있다*. (현관문을 등지고 서쪽을 볼 때, 시계방향)
1. 왼쪽(남): 짧은 복도를 따라 방 두 개(소이 방, 미란과 어머니의 방)와 욕실 문*.
2. 정면(서): 거실. 서쪽 창 폭 4.2m*. 창 바깥에 확장하지 않은 좁은 베란다가 남아 있다(4화 "베란다로 나가 전화를 받았다", 폭 1.2m*). 창에는 버건디 쉬어 커튼*. 거실 남쪽 벽에 소파, 북쪽 벽에 TV*. 소파 옆 바닥에 소이의 장난감 바구니*.
3. 오른쪽(북): 주방과 원목 4인 식탁(4화 "식탁 위에 휴대폰 두 대")*. 식탁 옆 벽에 작은 와인 랙*. 냉장고는 주방 안쪽 끝(4화 냉장고 모터, 위치는*).
4. 등 뒤: 현관. 신발장 위에 무화과 리드 디퓨저(4·6화 무화과 디퓨저, 위치는*).

### A-3. 조명·색

| 회차·씬 | 시각 | 광원 | 색온도 | 방향 | 메모 |
|---|---|---|---|---|---|
| 4화 S#2·4 | 오후 5:30~5:40 | 서쪽 창의 낮은 해 + 버건디 쉬어 커튼 | 2500K, 커튼을 지나 붉게 | 서→동, 수평에 가깝게. 식탁과 벽에 긴 창 그림자 | 거실이 와인색(4화). 커튼 색이 그 이유다* |
| 6화 S#3 | 저녁 6:41 | 현관 다운라이트 + 12층 홀 센서등 | 3000K / 4000K | 위에서 | 벨벳 드레스가 빛을 먹는다* |

**대표 색**: `#8C2F3A` 노을 와인빛 · `#E9A06A` 낮은 해 · `#6B4A3A` 원목 식탁 · `#F2E6DA` 크림 벽

### A-4. 소리·냄새·소품

- **소리**: 반 박자씩 늦게 웅웅거리는 냉장고 모터(4화). 코르크 '퐁'(4화). 휴대폰 진동과 어머니의 전화(4화 S#5).
- **냄새**: 무화과 디퓨저와 코르크(4·6화).
- **소품**: 식탁 위 휴대폰 두 대와 같은 9월 캘린더, 와인 잔 두 개, 오프너(4화). 현관 디퓨저(4·6화). 장난감 바구니*.
- **아이**: 4화 장면 동안 아이들은 키즈카페에 있다(4화). 배경 컷에 장난감은 둬도 된다. 관능 장면은 이 장소에 없다(4화 회상 컷은 2번 와인바 배경을 쓴다).

### A-5. 카메라 자리

| 자리 | 높이·방향 | 핵심 장면 |
|---|---|---|
| C1 현관 안쪽 | 눈높이, 서쪽 거실 창까지 | 4화 S#2 와이드 |
| C2 식탁 옆 | 앉은 눈높이, 식탁 위 휴대폰 두 대와 그 너머 창 | 4화 S#2·4 캘린더 대조 |
| C3 3호기 엘리베이터 안 | 눈높이, 거울 벽과 천장 | 1화 S#5③ CCTV 스티커, 6화 S#3 거울 앞 버건디 병 |

### A-6. SET LOCK (96 words)

```text
Unit 1204 on the 12th floor of a new 2024-built Korean apartment tower, a single mother's three-bay home of about 84 square meters. The living room faces west through a 4.2 m window with sheer burgundy curtains and a narrow unextended balcony beyond. A sofa on the left wall, a TV on the right, a basket of a seven-year-old girl's toys on the floor. To the right of the entry, an open kitchen with a solid wood four-seat dining table and a small wine rack on the wall. Light wood floor, cream walls, lived-in and warm.
```

### A-7. 프롬프트

**E1 빈 배경 — 오후 5:30 와인색 거실** (4화 S#2)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Unit 1204 on the 12th floor of a new 2024-built Korean apartment tower, a single mother's three-bay home of about 84 square meters. The living room faces west through a 4.2 m window with sheer burgundy curtains and a narrow unextended balcony beyond. A sofa on the left wall, a TV on the right, a basket of a seven-year-old girl's toys on the floor. To the right of the entry, an open kitchen with a solid wood four-seat dining table and a small wine rack on the wall. Light wood floor, cream walls, lived-in and warm.

Establishing view of the empty living and dining area at 5:30 pm. The low western sun pours through the burgundy sheer curtains and turns the whole room wine-red, long window shadows stretching across the floor and up the wall. On the wooden table, two smartphones lying side by side, an uncorked bottle and two red wine glasses. Warm, private, confessional. Wide 16:9 composition. No logos, no watermark.
```

**E2 빈 배경 — 저녁 6:41 현관** (6화 S#3)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Unit 1204 on the 12th floor of a new 2024-built Korean apartment tower, a single mother's three-bay home of about 84 square meters. The living room faces west through a 4.2 m window with sheer burgundy curtains and a narrow unextended balcony beyond. A sofa on the left wall, a TV on the right, a basket of a seven-year-old girl's toys on the floor. To the right of the entry, an open kitchen with a solid wood four-seat dining table and a small wine rack on the wall. Light wood floor, cream walls, lived-in and warm.

Establishing view of the entry hall from just inside the front door at 6:41 pm: a warm downlight over the doorway, a fig-scented reed diffuser on the shoe cabinet, the living room beyond dim and blue after sunset. The front door open onto a bright 12th-floor elevator lobby. Wide 16:9 composition. No logos, no watermark.
```

**C1 현관 안쪽 → 서쪽 창** (4화 S#2)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Unit 1204 on the 12th floor of a new 2024-built Korean apartment tower, a single mother's three-bay home of about 84 square meters. The living room faces west through a 4.2 m window with sheer burgundy curtains and a narrow unextended balcony beyond. A sofa on the left wall, a TV on the right, a basket of a seven-year-old girl's toys on the floor. To the right of the entry, an open kitchen with a solid wood four-seat dining table and a small wine rack on the wall. Light wood floor, cream walls, lived-in and warm.

Camera inside the entry at eye level looking straight west through the living room to the curtained window glowing deep red with sunset; the dining table on the right in silhouette, toys in a basket by the sofa. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C2 식탁 위 휴대폰 두 대** (4화 S#2·4)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Unit 1204 on the 12th floor of a new 2024-built Korean apartment tower, a single mother's three-bay home of about 84 square meters. The living room faces west through a 4.2 m window with sheer burgundy curtains and a narrow unextended balcony beyond. A sofa on the left wall, a TV on the right, a basket of a seven-year-old girl's toys on the floor. To the right of the entry, an open kitchen with a solid wood four-seat dining table and a small wine rack on the wall. Light wood floor, cream walls, lived-in and warm.

Close view at seated height across the wooden dining table: two smartphones lying side by side with their screens glowing blank, two wine glasses with a little red wine, a corkscrew and a cork, and behind them the wine-red window light. Vertical 9:16 webtoon panel, still-life detail. No logos, no watermark.
```

**C3 304동 3호기 엘리베이터 안** (1화 S#5③, 6화 S#3)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

Unit 1204 on the 12th floor of a new 2024-built Korean apartment tower, a single mother's three-bay home of about 84 square meters. The living room faces west through a 4.2 m window with sheer burgundy curtains and a narrow unextended balcony beyond. A sofa on the left wall, a TV on the right, a basket of a seven-year-old girl's toys on the floor. To the right of the entry, an open kitchen with a solid wood four-seat dining table and a small wine rack on the wall. Light wood floor, cream walls, lived-in and warm.

Different area: the inside of elevator car number 3 in the same building, a stainless and mirror-paneled cabin, a small dome security camera in the ceiling corner covered by a plain paper sticker, a blank floor button panel, cool even ceiling light. Vertical 9:16 webtoon panel. No logos, no watermark.
```

### A-8. 고증 메모

- 전용 84㎡(이른바 '국민평형')는 신축 대단지의 주력 평형이다. 3베이 판상형이 흔하다.
- 발코니를 대부분 확장하고 일부만 남기는 선택도 흔하다. 추측입니다.
- 엘리베이터 내부 CCTV 고장이 몇 달 방치되는 설정은 작중 사실(1화)이다. 실제로는 관리 소홀로 지적될 일이다. 추측입니다.

---

## 짧게 B. 207동 803호 — 세라의 집

### B-1. 공간 개요

- **위치**: 207동 8층, 소형 월세(bible). 207동은 단지 서쪽 줄의 소형 평형 동이다*.
- **평형**: 전용 26㎡ 원룸*. "열 걸음이면 끝나는 방"(5화).
- **거울이 없다.** "거울 하나 없는 방에서 그녀는 자기 몸이 지금 어떤 각도인지 정확히 알았다"(5화). 방 안에 거울을 그리지 않는다. 욕실 거울도 문 안쪽이라 보이지 않는다*.
- **엘리베이터**: 화물용을 탄다(1화). 벽에 보호용 담요. 6화에는 '정기 점검 중' 팻말이 걸려 계단으로 8층까지 오른다.
- **등장 근거**: 5화 S#9~10(밤 11:00), 6화 S#6 엘리베이터 앞 → 계단 → 803호 현관(저녁 6:57), 1화 S#5③.

### B-2. 평면 배치

(현관문을 등지고 남쪽 창을 볼 때, 시계방향). 방 크기 약 3.2m × 5m*.
1. 왼쪽(동): 욕실 문, 이어서 미니 주방(2구 인덕션, 소형 냉장고)*.
2. 정면(남): 창, 그 바깥에 세탁기를 둔 작은 베란다(5화 "베란다에서는 세탁기가 탈수를")*.
3. 오른쪽(서) 벽: 더블 침대가 벽에 붙고, 머리맡 선반에 간접등(5화 "침대 머리맡 간접등")*. 침대 옆 협탁에 근육 연고*.
4. 가운데 바닥: 요가 매트 한 장(5화). 매트 옆에 폼롤러와 작은 케틀벨*.
5. 등 뒤(북): 현관 옆 스탠드 행거(운동복, 민트 집업)*.

### B-3. 조명·색

| 회차·씬 | 시각 | 광원 | 색온도 | 방향 | 메모 |
|---|---|---|---|---|---|
| 5화 S#9~10 | 밤 11:00 | 천장등 꺼짐. 머리맡 간접등 하나 | 2400K 주황 | 서쪽 벽 위에서 방 쪽으로 낮게. 벽이 주황으로 물든다(5화) | 창밖은 어두운 단지 불빛* |
| 6화 S#6 | 저녁 6:57 | 계단실 등 + 8층 복도 센서등 | 4500K | 위에서 | 계단참마다 숨이 끊긴다(6화) |

**대표 색**: `#E8873A` 간접등 주황 · `#2E2A33` 어두운 방 · `#7FD1BE` 세라 민트(행거의 집업) · `#BFC6C4` 흰 세탁기

### B-4. 소리·냄새·소품

- **소리**: 베란다 세탁기 탈수 '덜컹덜컹'. 정점에서 바닥을 울리고, 멈추면 방이 넓어진 것처럼 조용하다(5화).
- **냄새**: 유칼립투스 근육 연고와 섬유유연제(5화).
- **소품**: 요가 매트(5화), 스마트워치(인물 소품), 폼롤러·케틀벨*, 근육 연고*, 민트 집업*.

### B-5. 카메라 자리

| 자리 | 높이·방향 | 핵심 장면 |
|---|---|---|
| C1 현관 안쪽 | 눈높이, 방 전체 | 5화 S#9 "열 걸음이면 끝나는 방" |
| C2 매트 높이 | 바닥 로우 앵글, 머리맡 간접등 쪽 | 5화 S#10 |
| C3 207동 화물용 엘리베이터 앞과 계단 | 눈높이 | 6화 S#6 '정기 점검 중', 1화 S#5③ 담요 벽 |

### B-6. 수위 장치 (5화 S#10)

1. **간접등 하나**: 주황 빛이 낮고 좁다. 몸은 측면 실루엣과 땀의 하이라이트만 남는다*.
2. **침대 모서리와 매트 끝 전경**: 로우 앵글에서 매트 끝과 폼롤러를 크게 걸어 가린다*.
3. **컷을 넘길 사물**: 정점으로 치닫는 세탁기 탈수, 멈춘 세탁기, 스마트워치 화면 '52:08 / 168'(5화).
4. **거울 금지**: 이 방에서는 반사로 몸을 보여 주지 않는다(5화).

### B-7. SET LOCK (103 words)

```text
A tiny rented studio, unit 803 on the 8th floor of a small-unit building in a new 2024-built Korean apartment complex, about 3.2 by 5 meters, ten steps from wall to wall. A double bed against the right wall with a small warm indirect lamp on the headboard shelf, a single yoga mat on the floor in the middle with a foam roller and a small kettlebell, a mini kitchen and bathroom door on the left, a window ahead onto a tiny balcony holding a washing machine. A clothes rack by the door with athletic wear. Absolutely no mirrors anywhere in the room.
```

### B-8. 프롬프트

**E1 빈 배경 — 밤 11:00 주황 간접등** (5화 S#9)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A tiny rented studio, unit 803 on the 8th floor of a small-unit building in a new 2024-built Korean apartment complex, about 3.2 by 5 meters, ten steps from wall to wall. A double bed against the right wall with a small warm indirect lamp on the headboard shelf, a single yoga mat on the floor in the middle with a foam roller and a small kettlebell, a mini kitchen and bathroom door on the left, a window ahead onto a tiny balcony holding a washing machine. A clothes rack by the door with athletic wear. Absolutely no mirrors anywhere in the room.

Establishing view of the empty studio at 11 pm. The ceiling light is off; only the indirect lamp at the bed head glows low and orange, washing the right wall and the yoga mat in warm light while the corners sink into dark plum shadow. Through the window, the washing machine on the balcony and distant apartment lights. Small, close, warm. Wide 16:9 composition. No logos, no watermark.
```

**E2 빈 배경 — 낮의 같은 방(보조)***
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A tiny rented studio, unit 803 on the 8th floor of a small-unit building in a new 2024-built Korean apartment complex, about 3.2 by 5 meters, ten steps from wall to wall. A double bed against the right wall with a small warm indirect lamp on the headboard shelf, a single yoga mat on the floor in the middle with a foam roller and a small kettlebell, a mini kitchen and bathroom door on the left, a window ahead onto a tiny balcony holding a washing machine. A clothes rack by the door with athletic wear. Absolutely no mirrors anywhere in the room.

Establishing view of the same studio on a bright afternoon: daylight from the balcony window, the yoga mat rolled out, a mint zip-up jacket hanging on the rack, a tube of muscle balm on the bedside table. Neat, sporty, cramped but cheerful. Wide 16:9 composition. No logos, no watermark.
```

**C1 현관 안쪽 → 방 전체** (5화 S#9)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A tiny rented studio, unit 803 on the 8th floor of a small-unit building in a new 2024-built Korean apartment complex, about 3.2 by 5 meters, ten steps from wall to wall. A double bed against the right wall with a small warm indirect lamp on the headboard shelf, a single yoga mat on the floor in the middle with a foam roller and a small kettlebell, a mini kitchen and bathroom door on the left, a window ahead onto a tiny balcony holding a washing machine. A clothes rack by the door with athletic wear. Absolutely no mirrors anywhere in the room.

Camera just inside the front door at eye level, the whole studio visible at once: mini kitchen on the left, yoga mat in the center, bed with the glowing orange lamp on the right, balcony window ahead. Night. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C2 매트 높이 로우 앵글** (5화 S#10)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A tiny rented studio, unit 803 on the 8th floor of a small-unit building in a new 2024-built Korean apartment complex, about 3.2 by 5 meters, ten steps from wall to wall. A double bed against the right wall with a small warm indirect lamp on the headboard shelf, a single yoga mat on the floor in the middle with a foam roller and a small kettlebell, a mini kitchen and bathroom door on the left, a window ahead onto a tiny balcony holding a washing machine. A clothes rack by the door with athletic wear. Absolutely no mirrors anywhere in the room.

Floor-level low angle at the edge of the yoga mat, a foam roller big and blurred in the foreground, the mat's texture in focus, looking toward the bed head where the orange indirect lamp glows; the balcony washing machine faintly visible through the window glass. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C3 화물용 엘리베이터 앞과 계단** (6화 S#6)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

A tiny rented studio, unit 803 on the 8th floor of a small-unit building in a new 2024-built Korean apartment complex, about 3.2 by 5 meters, ten steps from wall to wall. A double bed against the right wall with a small warm indirect lamp on the headboard shelf, a single yoga mat on the floor in the middle with a foam roller and a small kettlebell, a mini kitchen and bathroom door on the left, a window ahead onto a tiny balcony holding a washing machine. A clothes rack by the door with athletic wear. Absolutely no mirrors anywhere in the room.

Different area: the ground-floor service elevator of the same building, its inner walls hung with grey protective padding blankets visible through the half-open door, a blank sign board on a stand in front of it, and beside it the door to a concrete stairwell with a handrail climbing upward under cool stair lights. Vertical 9:16 webtoon panel. No logos, no watermark.
```

### B-9. 고증 메모

- 신축 대단지에 원룸·소형 평형이 섞인 동이 있는 경우가 있다. 추측입니다: 207동을 소형 동으로 둔 것은 작중 설정이다.
- 아파트 화물용(인승 겸용) 엘리베이터 벽에 이사·택배용 보호 패드를 걸어 두는 것은 흔하다.
- 원룸 베란다에 세탁기를 두는 배치는 흔하다. 탈수 진동이 바닥을 울리는 것도 그렇다.

---

## 짧게 C. 관리사무소 지하 방재실

### C-1. 공간 개요

- **위치**: 관리사무소 건물 지하 1층*. 관리사무소는 커뮤니티센터 서쪽에 붙어 있다*. 관리사무소는 추석에 닫았지만 지하 방재실은 24시간 돌아간다(5화).
- **크기**: 약 40㎡, 창 없음*.
- **등장 근거**: 5화 S#4(오전 9:00, 9월 25일 추석 당일).

### C-2. 평면 배치

(출입문을 등지고 안쪽을 볼 때, 시계방향)
1. 왼쪽: 복합기와 서류 캐비닛(5화 "복합기가 종이를 뱉는 소리", 위치는*).
2. 정면: CCTV 모니터 벽(대형 모니터 여섯 대, 각각 16분할)*. 그 아래 화재 수신반(표시등 패널)*.
3. 오른쪽: 당직 책상 두 개. 한 책상에 차량 출입 관제 모니터(5화 '238노 7171 출차 21:52 / 입차 04:17', 글자는 식자)*. 책상 위 전기포트와 믹스커피 상자*.
4. 등 뒤: 출입문 옆 간이 소파와 사물함*.

### C-3. 조명·색

| 회차·씬 | 시각 | 광원 | 색온도 | 방향 | 메모 |
|---|---|---|---|---|---|
| 5화 S#4 | 오전 9:00 | 천장 형광(직관 LED) + 모니터 벽 | 5000K / 모니터 푸른빛 | 위에서 + 정면 벽에서 | 창이 없어 아침인지 알 수 없다* |
| 보조: 심야* | 새벽 3:00 | 천장등 절반 + 모니터 벽 | 모니터 푸른빛 위주 | 정면에서 | 당직 근무의 밤* |

**대표 색**: `#3E6FA8` 모니터 푸른빛 · `#E6E8E4` 형광 흰빛 · `#7A7F84` 회색 캐비닛 · `#D9A441` 송편 상자 노랑

### C-4. 소리·냄새·소품

- **소리**: 복합기가 종이를 뱉는 소리, 당직 반장의 주차 민원 수다(5화).
- **냄새**: 믹스커피(5화 "믹스커피를 저었다")*. 송편의 참기름*.
- **소품**: 송편 상자(5화), 종이컵 믹스커피(5화), 차량 출입 기록 출력물(5화).

### C-5. 카메라 자리

| 자리 | 높이·방향 | 핵심 장면 |
|---|---|---|
| C1 문가 | 눈높이, 모니터 벽 정면 | 5화 S#4 와이드 |
| C2 당직 책상 | 앉은 눈높이 클로즈, 송편 상자·종이컵·관제 모니터 | 5화 S#4 Insert |

### C-6. SET LOCK (95 words)

```text
The basement security and disaster control room of a new Korean apartment complex management office, about 40 square meters with no windows. A wall of six large monitors showing grids of blank CCTV views above a fire alarm control panel with small indicator lights. On the right, two duty desks with office chairs, one desk holding a parking gate monitor, an electric kettle and a box of instant coffee sticks. On the left, a multifunction printer and grey filing cabinets. A small couch by the door. Flat white ceiling light mixed with blue monitor glow.
```

### C-7. 프롬프트

**E1 빈 배경 — 오전 9:00 추석 당직** (5화 S#4)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The basement security and disaster control room of a new Korean apartment complex management office, about 40 square meters with no windows. A wall of six large monitors showing grids of blank CCTV views above a fire alarm control panel with small indicator lights. On the right, two duty desks with office chairs, one desk holding a parking gate monitor, an electric kettle and a box of instant coffee sticks. On the left, a multifunction printer and grey filing cabinets. A small couch by the door. Flat white ceiling light mixed with blue monitor glow.

Establishing view of the empty control room at 9 am on a holiday morning. Flat white ceiling light and the cool blue glow of the monitor wall; a box of rice cakes with a pine-needle pattern lid and a paper cup of instant coffee on the duty desk, a fresh printout curling out of the printer. Mundane, quiet, quietly important. Wide 16:9 composition. No logos, no watermark.
```

**E2 빈 배경 — 심야(보조)***
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The basement security and disaster control room of a new Korean apartment complex management office, about 40 square meters with no windows. A wall of six large monitors showing grids of blank CCTV views above a fire alarm control panel with small indicator lights. On the right, two duty desks with office chairs, one desk holding a parking gate monitor, an electric kettle and a box of instant coffee sticks. On the left, a multifunction printer and grey filing cabinets. A small couch by the door. Flat white ceiling light mixed with blue monitor glow.

Establishing view of the same control room at 3 am, half the ceiling lights off, the room lit mostly by the blue monitor wall, an empty office chair turned slightly toward the screens. Watchful, sleepless. Wide 16:9 composition. No logos, no watermark.
```

**C1 문가 → 모니터 벽** (5화 S#4)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The basement security and disaster control room of a new Korean apartment complex management office, about 40 square meters with no windows. A wall of six large monitors showing grids of blank CCTV views above a fire alarm control panel with small indicator lights. On the right, two duty desks with office chairs, one desk holding a parking gate monitor, an electric kettle and a box of instant coffee sticks. On the left, a multifunction printer and grey filing cabinets. A small couch by the door. Flat white ceiling light mixed with blue monitor glow.

Camera at the doorway at eye level facing the monitor wall straight on, the duty desks on the right with an office chair pulled out, the fire alarm panel's small lights below the screens. Vertical 9:16 webtoon panel. No logos, no watermark.
```

**C2 당직 책상 클로즈** (5화 S#4 Insert)
```text
Korean adult webtoon background art, semi-realistic glossy digital painting, soft gradient lighting, clean perspective, no people, no text.

The basement security and disaster control room of a new Korean apartment complex management office, about 40 square meters with no windows. A wall of six large monitors showing grids of blank CCTV views above a fire alarm control panel with small indicator lights. On the right, two duty desks with office chairs, one desk holding a parking gate monitor, an electric kettle and a box of instant coffee sticks. On the left, a multifunction printer and grey filing cabinets. A small couch by the door. Flat white ceiling light mixed with blue monitor glow.

Close view at seated desk height: a paper cup of instant coffee with a stirring stick, an open box of half-moon rice cakes, and behind them the parking gate monitor glowing with a blank list window. Vertical 9:16 webtoon panel, still-life detail. No logos, no watermark.
```

### C-8. 고증 메모

- 2020년대 대단지 관리사무소는 지하나 1층에 방재실(종합방재실)을 두고 CCTV, 화재 수신반, 주차 관제, 엘리베이터 감시를 한곳에서 본다. 24시간 교대 근무가 일반적이다.
- 차량 출입 기록과 CCTV는 개인정보다. 관리사무소가 제3자에게 함부로 보여 주면 개인정보보호법 문제가 생긴다. 4화의 "개인정보라 소장도 함부로 못 보여 줘", 5화의 '주차 민원 조사' 핑계, bible의 '개인정보 소지' 메모와 같다.

---

## 연속성 체크리스트 (자주 틀리는 것)

- 법정에 **법봉 없음**(SPEC, 6화). 법원 상징·글자도 그리지 않는다*.
- 207동 803호에는 **거울이 없다**(5화). 필라테스룸은 반대로 **거울 여섯 장**이다(2화).
- 와인바 펜던트는 **다섯 개**다. 마감 후(2·5화)에는 가운데 세 개만 켜고, 4·6화에는 다섯 개를 다 켠다*.
- B2 B구역 바닥은 **9/19 오후 도색** 전후로 다르다. 9/20 이후는 새 녹색 에폭시*.
- 3801호 통창 앞에는 **커튼 천이 보이지 않는다**(천장 매입 박스)*. 2402호는 반대로 **차콜 암막 커튼**이 핵심이다.
- 2402호 거실은 **남향**, 1204호 거실은 **서향**, 3801호 거실은 **남향** + 안방 남동 모서리 통창*.
- 503동 24층은 **두 세대**뿐이다(2401·2402)*.
- 순옥의 세신복은 **분홍**이다(bible 3-3). 세신실 배경에 붉은 소품을 많이 두지 않는다*.
- 놀이터·1204호 낮·3801호 낮 배경에는 관능 소품을 두지 않는다(SPEC 4절).
- 간판, 팻말, 칠판 장부, 층수, 번호판, 모니터 기록은 모두 **빈 면**으로 뽑고 식자로 넣는다.

---

## 단지 전체 배치 — 레이크시티 더퍼스트

경기도 가상 신도시 '호수신도시'의 신축 대단지. 2024년 입주, 15개 동, 3,012세대(SPEC). 아래 배치는 소설·대본의 빛 방향과 동선(bible 3-2)을 함께 만족하도록 정했다. 북쪽이 위다.

### 땅의 모양

- 동서 약 650m, 남북 약 450m의 모서리가 둥근 직사각형*.
- **남동쪽**이 호수신도시 중앙 호수공원(공공)과 맞닿는다*. 호수는 둘레 약 3km*, 둘레에 산책로와 가로등이 있다(5화). 호수 건너편 남쪽 기슭에 오리배 선착장(3화 오리배, 위치는*), 그 너머 수평선 쪽에 동서로 흐르는 고속도로가 있다(1화 고속도로 불빛, 위치는*).
- 단지 안 지상에는 차가 다니지 않는다. 모든 차는 지하로 들어간다(1화 "열다섯 개 동은 지하 2층 주차장에서 통로로 이어져", 지상 구조는*).

### 가운데: 중앙광장

- 단지 한가운데에 중앙광장이 있다*.
- 광장 **북쪽**: 커뮤니티센터 '더퍼스트 클럽'. 지상 1층의 낮은 유리 건물과 지하 1층(사우나·필라테스룸·골프연습장·키즈카페). 지상층에 커뮤니티 독서실*.
- 클럽 **서쪽**에 붙어 관리사무소. 그 지하에 방재실*.
- 광장 **남쪽**: 물결놀이터(바닥분수, 조합놀이대, 모래, 벤치)(3화).
- 놀이터 **남동쪽** 끝에 수변 게이트. 호수공원 산책로로 바로 나간다*.

### 둘레: 열다섯 개 동 (다섯 구역 × 세 동)

동 번호의 백 단위가 구역을 뜻한다*. 열다섯 개 동이 중앙광장과 놀이터를 고리처럼 둘러싼다(3화 S#16 부감).

| 구역 | 방위 | 동 | 층수·형태 | 이 작품에서 |
|---|---|---|---|---|
| 1구역 | 남동, 호수 바로 앞('앞동 라인', 3화) | 101·102·103동 | 38층 탑상형* | **101동**은 가장 남동쪽 모서리, 호수에 가장 가깝다*. 38층 3801호 펜트하우스(유진) |
| 3구역 | 동, 상가 쪽 | 304·305·306동 | 25층 판상형, 거실이 단지 안쪽(서쪽)을 본다* | **304동** 12층 1204호(미란). 3호기 CCTV 고장 |
| 5구역 | 북, 클럽 뒤 | 501·502·503동 | 29층 판상형, 남향, 층당 2세대* | **503동**은 가운데 동*. 24층 2402호(혜숙) |
| 2구역 | 서 | 205·206·207동 | 20층, 소형 평형 위주* | **207동** 8층 803호(세라). 화물용 엘리베이터 |
| 4구역 | 남서, 호수공원 서쪽 잔디 광장 앞 | 410·411·412동 | 20층, 소형·중형 혼합, 남향* | **412동** 5층 502호(하린). 창밖이 호수공원 잔디 광장 |

### 바깥: 상가와 문

- **상가 '퍼스트 애비뉴'**: 단지 **동쪽** 대로변, 3구역 동들과 1구역 사이 바깥쪽에 지상 2층 스트리트형으로 늘어선다*. 1층 남쪽 끝 모서리 칸이 **와인바 '미란'**이다. 전면이 남동쪽 호수공원 보행로를 본다*. 상가 1층 북쪽에 무인택배함(1화), 치킨집(3화)이 있다(위치는*).
- **정문**: 동쪽 대로, 상가 북쪽 끝 옆*. 유치원 셔틀버스 정류장이 정문 앞에 있다(1화 S#4).
- **후문**: 서쪽, 2구역 옆*.
- **수변 게이트**: 남동쪽, 놀이터와 1구역 사이*.

### 지하: 주차장과 연결통로

- 지하 1·2층 통합 주차장이 열다섯 개 동, 커뮤니티센터, 관리사무소 아래를 하나로 잇는다*.
- **지하 2층 B구역**: 남쪽 가운데. 101동 엘리베이터 홀과 중앙광장 남쪽 아래 사이*. 그의 차 자리.
- **동 연결통로**: 각 동 엘리베이터 홀을 고리 모양 통로가 잇는다*. 101동 아래 구간에서 '출구 쪽 계단'과 '상가 쪽 통로'가 갈라진다(6화, 위치는*). 상가 쪽 통로는 동쪽으로 가서 상가 지하 계단으로 올라간다*.
- **클럽 연결 계단**: 지하 2층 연결통로에서 클럽 지하 1층 복도 끝(필라테스룸 옆)으로 올라가는 계단. 세대카드 리더(2·4화 'B2 연결통로 출입' 기록)*.

### 6화 동선 확인 (bible 3-2와 대조)

B구역(남쪽 가운데) → 304동(동) 18:41 → 지하 통로 → 503동(북) 18:47 지하 홀·18:49 → 207동(서) 18:57 → 412동(남서) 19:05 → 101동(남동) 19:13 → 101동 아래 연결통로 19:20 → 상가 쪽 통로(동) → 와인바 19:30.
단지를 **반시계방향으로 한 바퀴** 돈 뒤 출발점 바로 옆 상가로 들어간다. 지도로 보면 그가 단지를 한 바퀴 '관리'하고 제자리로 돌아오는 모양이다*.

### 빛 방향 확인

- 3화 S#6 저녁 6시: 서쪽의 낮은 해 → 2·4·1구역 동들의 그림자가 동쪽으로 길게 늘어져 남동쪽 호수 위에 눕는다.
- 4화 S#2 오후 5시 반: 304동(동쪽 줄) 서향 거실에 지는 해가 정면으로 든다.
- 1화 S#9, 4화 S#7, 5화 S#8: 503동(북쪽 줄) 남향 거실로 오전 남동·오후 남서의 해가 든다.
- 3화 S#13 오후 2시 반: 101동 남향 거실에 남남서의 볕이 비스듬히 든다. 1화 S#2 새벽: 101동 안방 동·남 통창이 먼저 푸르다.
- 5화 S#1 오전 10시: 와인바 남동 전면 블라인드 틈으로 햇빛이 든다.

### 개략도*

```text
                              N
        ┌───────────────────────────────────────────────┐
        │   [501] [502] [503]          (5구역, 남향)     │
        │                                               │
        │  [205]        [관리사무소][더퍼스트 클럽]   [304]│  ║ 퍼
 후문 ◀ │  [206]             (B1 사우나·필라테스)     [305]│  ║ 스
        │  [207]          ┌───────────┐               [306]│  ║ 트
        │ (2구역)          │ 중앙광장   │            (3구역)│  ║
        │                 │ 물결놀이터 │                   │  ║ 애비뉴
        │  [410] [411]    └───────────┘   [103] [102]     │  ║ ▶ 정문
        │  [412] (4구역)                   [101] (1구역)  │  ║ [와인바 '미란']
        └──────────────── 잔디 광장 ─────── 수변 게이트 ───┘
                    ~~~~~~~~ 호수신도시 중앙 호수공원 ~~~~~~~~
                         (건너편 기슭 오리배 선착장)
                    ═══════════ 고속도로(수평선) ═══════════
```

- 지하 2층 B구역은 놀이터 남쪽과 101동 사이 아래에 있다*.
