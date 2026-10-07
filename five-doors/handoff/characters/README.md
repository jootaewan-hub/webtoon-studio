# 캐릭터 프롬프트 팩 — 「단톡방에 그 남자가 있다」

ChatGPT(이미지 생성)와 Codex가 일곱 인물을 **같은 얼굴로 반복해서** 그리게 하기 위한 프롬프트 모음이다. 이 폴더에는 그림이 없고, 프롬프트와 검수 기준만 있다.

- 작화 기준: `story/bible.md` **0-2. 확정 외형(시안 B)** > 인물별 3·4·5절 > 3-1 대비표. 충돌하면 0-2를 따른다.
- 등장인물은 모두 **가공의 성인**이다. 모든 LOCK에 `fictional adult character, not resembling any real person`이 들어 있다.
- 인물 파일: [dogyeom.md](dogyeom.md) · [yujin.md](yujin.md) · [miran.md](miran.md) · [sera.md](sera.md) · [harin.md](harin.md) · [hyesuk.md](hyesuk.md) · [sunok.md](sunok.md)

## 1. 7명 한눈 표

| 이름 | 나이 | 키 | 체형 키워드 | 대표 색 | 머리 HEX | 기준 이미지 |
|---|---|---|---|---|---|---|
| 한도겸 | 32 | 182cm | 넓은 어깨, 긴 팔다리의 마른 근육 | 없음(흰 셔츠 `#F4F4F2`) | `#1C1F26` 슬릭 백 + 앞머리 한 가닥 | **있음** 시안 B (Canva) |
| 서유진 | 33 | 172cm | 긴 다리의 부드러운 모래시계, 곧은 등 | 회색 `#9A9EA3` | `#3A2A22` 앞머리 웨이브 단발 | **있음** 시안 B (Canva) |
| 차미란 | 35 | 165cm | 가장 뚜렷한 모래시계 | 버건디 `#7A1E2E` | `#4A2418` 옆가르마 빈티지 웨이브 | **있음** 시안 B (Canva) |
| 오세라 | 28 | 168cm | 조각(복근, 비너스 보조개) + 둥근 볼륨 | 민트 `#7FD1BE` | `#1C1F26` 하이 포니테일 | 없음(시안 A는 체형·의상 참고만) |
| 윤하린 | 25 | 163cm | 마른 몸 + 볼륨, 좁은 어깨 | 하늘색 `#9CC7E8` | `#1C1F26` 긴 생머리 하프업 | 없음 |
| 정혜숙 | 42 | 166cm | 무게 있는 성숙 글래머, 느린 몸 | 금색 `#C9A45C` | `#2B1D16` 낮은 시뇽 | 없음 |
| 박순옥 | 61 | 155cm | 단단한 노동의 몸(관능 없음) | 분홍 세신복 `#E9A6B3` | `#8E8A86` 희끗한 단발 파마 | 없음 |

## 2. 프롬프트 구조

모든 코드블록은 세 덩어리로 되어 있고, **블록 전체를 그대로 복사**하면 된다.

```text
[공통 스타일 문구]
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

[CHARACTER LOCK — 인물별 120~180단어, 절대 수정 금지]

[작업 지시 — 턴어라운드 / 표정 / 의상 / 클로즈업 / 키 비주얼]
```

- '8-head proportions'는 작품 공통 기준이다. 미란·하린·혜숙(7.5등신), 순옥(6.5등신)은 LOCK에 따로 적어 두었고, **LOCK이 우선**이다.
- 의상·키 비주얼 지시에는 "옷은 바꾸되 얼굴·머리·체형·표식은 LOCK 그대로" 문장이 들어 있다. 법정 머리처럼 컷 지시가 따로 말하는 경우만 예외다.
- 권장 비율: 턴어라운드·표정·의상 시트는 가로 3:2, 클로즈업은 1:1, 키 비주얼은 세로 2:3.

## 3. 생성 순서

인물 하나씩, 아래 순서를 지킨다. 앞 단계 결과가 다음 단계의 레퍼런스가 된다.

1. **턴어라운드(3-a)**: 2~4번 뽑아 체크리스트를 가장 많이 통과한 1장을 기준 이미지로 정한다. 기준 이미지가 이미 있는 3명(도겸·유진·미란)은 그 이미지를 첨부하고 시작한다.
2. **표정 시트(3-b)**: 기준 이미지를 첨부하고 생성한다. 얼굴이 기준과 달라진 칸이 있으면 시트 전체를 다시 뽑는다.
3. **의상 시트(3-c)**: 시트를 나눠 둔 순서대로. 의상이 바뀌어도 얼굴·머리가 유지되는지 확인한다.
4. **클로즈업(3-d)**: 손의 표식(도겸 흉터, 미란 손등 흉터, 혜숙 진주 실 등)을 확정한다.
5. **키 비주얼(3-e)**: 마지막에. 여기까지 통과한 이미지 1~2장을 첨부한다.

추천 인물 순서: 도겸 → 유진 → 미란(기준 이미지 있음) → 세라 → 하린 → 혜숙 → 순옥. 순옥은 도겸의 눈썹과 비교해야 하므로 도겸보다 뒤에 둔다.

## 4. ChatGPT에서 일관성 유지하는 법

- **첫 결과를 레퍼런스로 다시 업로드한다.** 통과한 턴어라운드를 저장하고, 이후 요청마다 첨부한 뒤 각 파일 5절의 '레퍼런스 문장'을 맨 앞에 붙인다.
- **같은 대화를 유지한다.** 한 인물의 시트는 한 대화 안에서 끝낸다. 결과가 흔들리기 시작하면(대략 10장 이상 생성) 새 대화를 열고 기준 이미지와 LOCK으로 다시 시작한다.
- **시드 대신 LOCK 문단을 고정한다.** ChatGPT에서는 시드를 지정하는 방식에 기대지 않는다. 고정할 것은 LOCK 문단이다. 단어 하나도 바꾸지 말고, 수정 요청은 LOCK 바깥에 짧게 덧붙인다(예: "Same character. Only fix: the scar must be on the LEFT hand.").
- **한 번에 한 인물만.** 한 대화에 두 인물을 섞지 않는다. 다인 컷은 각 인물의 기준 이미지가 확정된 뒤에 따로 한다(6절).
- **부분 수정은 짧게.** 마음에 드는 결과에서 한 가지만 틀리면 다시 생성하지 말고 "Keep everything, change only …"로 고친다.
- **검수는 체크리스트로.** 각 파일 1절의 체크리스트와 4절의 '자주 틀리는 점'을 보고 통과/폐기를 정한다. 좌우 반전(도겸의 왼손 시계·흉터), 머리 색, 하린 안경 모양이 가장 자주 틀린다.
- **저장 규칙**: `design/gen/{id}_{종류}_{번호}.png` (예: `design/gen/sera_turnaround_01.png`, `design/gen/sera_expr_01.png`). 기준 이미지는 인물당 1~2장만 둔다.

## 5. Codex로 생성할 때

- 프롬프트는 각 파일의 코드블록을 **문자열 그대로** 쓴다. 코드에서 LOCK을 조합하거나 요약하지 않는다.
- 레퍼런스 이미지 입력을 받는 생성·편집 방식을 쓸 수 있으면 4절과 같이 기준 이미지를 함께 넘긴다.
- 출력은 4절의 저장 규칙대로 저장하고, 결과마다 해당 인물 체크리스트로 사람이 검수한다.
- 구체적인 API 이름·파라미터(크기, 품질 옵션 등)는 사용하는 도구의 최신 문서를 확인한다. 이 팩은 특정 API를 전제하지 않는다.

## 6. 같은 컷에 여러 인물이 나올 때 — 구분 규칙

**원칙**: 한 장에 2명까지는 직접 생성하고, 3명 이상(4화 카운터, 6화 드레스 라인업, 법정 방청석)은 인물별로 따로 생성해 합성하는 쪽이 안전하다.

### 구분 3요소

| 인물 | ① 대표 색 | ② 머리 | ③ 실루엣 |
|---|---|---|---|
| 서유진 | 회색·은회색 실크 | 흑갈색 **앞머리 웨이브 단발** | 가장 큰 키, 긴 다리, 곧은 등 |
| 차미란 | 버건디 벨벳·저지 | 와인브라운 **옆가르마 긴 웨이브** | 가장 뚜렷한 모래시계 |
| 오세라 | 민트 기능성 원단 | 블랙 **하이 포니테일** | 구릿빛, 복근, 등 보조개 |
| 윤하린 | 하늘색 니트 | 블랙 **긴 생머리 하프업**(결심 컷은 묶음) + **금테 타원 안경** | 가장 작은 키, 좁은 어깨 |
| 정혜숙 | 금색 시퀸·와인 저지 | 다크초콜릿 **낮은 시뇽** | 무게 있는 곡선, 진주 |
| 한도겸 | 흰 셔츠 | 블랙 슬릭 백 + 앞머리 한 가닥 | 182cm, 넓은 어깨 |
| 박순옥 | 분홍 세신복 | 희끗한 단발 파마/망사 캡 | 155cm, 다부진 몸, 굽은 등 |

- **헷갈리는 쌍**
  - 세라 vs 하린: 둘 다 블랙 `#1C1F26`. 세라=구릿빛+하이 포니테일+민트, 하린=흰 피부+안경+하늘색. 하린이 머리를 묶는 컷에서는 안경을 반드시 그린다.
  - 민트 vs 하늘색: 3화 설정상 형광등 아래서 같아 보이지만, 작화에서는 세라=초록 기, 하린=파랑 기로 확실히 벌린다.
  - 미란(버건디 `#7A1E2E`·`#5E1324`) vs 혜숙 5화(와인색 `#6B2236`): 미란=붉은 립+긴 웨이브, 혜숙=진주+시뇽.
  - 유진(회색) vs 세라 4화(회색 브라톱): 재질로 구분(실크·니트 vs 기능성).
  - 도겸 vs 순옥: **같은 짙은 일자 눈썹**이어야 한다. 다르게 그리면 6화 법정 장치가 깨진다.
- **라인업 순서**(바이블 3-1): 6화 카운터는 버건디 → 금색 → 민트 → 하늘색 → 은회색. 법정 방청석은 유진을 가운데 둘째 줄에 두고 미란·세라·하린·혜숙이 차례로 앉는다.

### 2인 컷 템플릿

두 인물의 기준 이미지를 모두 첨부하고, LOCK 전체 대신 아래 그룹 태그를 쓴 뒤 컷 지시를 붙인다. 얼굴이 흔들리면 두 사람의 LOCK 전체를 `LEFT:` / `RIGHT:`로 나눠 붙인다.

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions.

Two fictional adult characters, not resembling any real persons, matching the two attached reference images.
LEFT: [그룹 태그 A]
RIGHT: [그룹 태그 B]
Keep each one's face, hair color, hairstyle and body exactly as in their reference image; do not blend their features.

[장면 지시]. No text, no letters, no logo, no watermark.
```

### 그룹 태그(다인 컷용 요약)

```text
Do-gyeom: tall man, slicked-back black hair with one forehead strand, white shirt with rolled sleeves, watch and crescent scar on the LEFT hand, left-corner half smile
Yu-jin: tallest woman, wavy espresso-brown bob with side bangs, cool unsmiling eyes, pearl studs, grey/silver silk, very long legs
Mi-ran: most curvy hourglass, side-parted voluminous wine-brown vintage waves, smoky half-lidded eyes, deep red lips, burgundy jersey or velvet, wine glass
Se-ra: tan bronze skin, black HIGH ponytail with baby hairs, heart-shaped freckled face, athletic abs, mint sportswear or mint cutout dress, smartwatch
Ha-rin: thin gold oval glasses, long straight black hair half-up (or high tie when decided), fair skin and flushed ears, slim with narrow shoulders, sky-blue knit
Hye-suk: oldest woman, low dark-chocolate chignon with falling strands, winged eyeliner, pearl necklace, red nails, gold or wine jersey, hand covering her smile
Sun-ok: short stocky older woman, graying permed bob or mesh cap, thick straight dark brows, pink scrub uniform, thick hands, eyes lowered
```

## 7. 공통 수위·안전 원칙

- 노출은 **어깨·등·팔·다리**까지. 속옷·슬립·셔츠 한 장 컷은 패션 화보 수준에서 멈추고, 실루엣과 재질(실크의 흐름, 니트의 당김, 벨벳의 그늘)로 표현한다.
- 실존 인물·연예인 이름, 실제 브랜드 로고(롤렉스·샤넬 등)를 넣지 않는다. 짝퉁 설정은 '로고 없는' 물건으로만 그린다.
- 하린(25)은 성인임을 얼굴·비율에서 분명히 한다. 어려 보이는 결과는 바로 폐기한다.
- 아이(지호, 소이)는 관능 톤의 인물 이미지·의상과 한 장에 두지 않는다.
- 순옥과 세신실 장면에는 관능 톤을 섞지 않는다.
- **쇼츠·인스타용**: 침실·드레스 컷은 역광 실루엣, 뒷모습, 허리 위 크롭을 기본으로 한다. 썸네일은 각 인물의 평상복 턴어라운드나 키 비주얼을 쓴다.

## 8. 바이블 3·4절과 달라진 점(시안 B 반영)

| 인물 | 바이블 3절·대비표 | 이 팩(0-2 시안 B) |
|---|---|---|
| 한도겸 | 졸린 눈, 투블록 슬릭 | 부드러운 미남형, 이마의 머리 한 가닥, 소매 걷음 |
| 서유진 | 긴 S, 차가운 눈매, 얇은 입술 | 모래시계 쪽, 나른하게 처진 눈매, 도톰한 뮤트 로즈레드, 앞머리 |
| 차미란 | 큰 반달 눈, 둥근 계란형 | 날카로운 계란형, 스모키, 평소 반쯤 감긴 눈, 옆가르마 빈티지 웨이브 |
| 오세라 | V라인, 아몬드 눈 | 하트형, 동그란 눈, 주근깨, 잔머리, 민트 집업 |
| 윤하린 | 둥근 얼굴, **동그란** 안경, 평소 풂 | 갸름한 계란형(볼은 둥글게), **금테 타원** 안경, 평소 하프업 |
| 정혜숙 | 갸름한 얼굴, 프렌치 트위스트 | 둥글고 부드러운 얼굴, 웃음 주름, 낮은 시뇽 |
| 박순옥 | — | 변경 없음(단일안) |

- 순옥 회상(2001) 몸빼 색은 바이블 4절 `#C9B79C`를 따랐다. `design/characters.json`은 이 의상의 바지 색을 `#5B4A6B`로 적고 있어 서로 다르다. 확정이 필요하다.
