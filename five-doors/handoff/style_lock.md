# 스타일 고정 규칙 (STYLE LOCK) — 「단톡방에 그 남자가 있다」

G6에서 **하이브리드**로 확정했다. 모든 이미지는 아래 세 트랙 중 하나로 그린다. 트랙을 섞지 않는다(한 컷 = 한 트랙).

## 트랙 1 — 본편 기본: 글로시 반실사 (전체 컷의 약 85%)

```text
Korean adult webtoon, semi-realistic glossy digital painting, soft airbrush gradient shading, gentle rim light, fine thin warm-brown lineart, 8-head proportions, cinematic lighting, detailed fabric rendering (silk sheen, velvet depth, knit texture), smooth luminous skin, clean background painting with soft bokeh, vertical webtoon panel composition, no text, no watermark, no logos.
```

- **선**: 가는 따뜻한 갈색 선(#5A3328 계열). 형태는 선보다 면과 빛으로 만든다.
- **피부**: 3~4단 그러데이션. 쇄골, 어깨, 허리선, 허벅지 위에 하이라이트를 준다.
- **의상**: 재질이 보이게 그린다.
  - 실크는 물처럼 흐르는 하이라이트, 벨벳은 깊은 그늘, 니트는 몸에 당겨지는 결.
  - 몸 라인(가슴의 굴곡, 잘록한 허리, 골반과 허벅지)이 옷 위로 드러나게 그린다.
- **빛**: 장면마다 광원은 하나로 정한다(배경 설정서의 시간대 조명을 따른다). 역광 림라이트로 실루엣을 강조한다.

## 트랙 2 — 코미디 리액션: 하이콘트라스트 셀 (약 10%)

```text
Korean webtoon comedic reaction panel, bold black ink outlines 3-4px, flat two-tone cel shading, high-saturation flat colors, simple speed lines or focus lines, slightly exaggerated expression (chibi-lite deformation allowed only for the face and hands), same character design and outfit colors as the main style, plain flat color background, no text.
```

- **쓰는 곳**
  - 도겸이 귓불을 만지는 순간, 엘리베이터 패닉(6화), 부녀회 임원들의 "어머."
  - 같은 멘트 "너한테만"이 다섯 번 반복될 때의 리액션, 세신실의 씁쓸한 웃음.
- 등신은 유지하고 얼굴과 손만 과장한다. 의상 색은 본편과 같다.

## 트랙 3 — 쇼츠·인스타 티저: 네온 누아르 실루엣 (홍보용)

```text
Neon noir silhouette illustration, figure rendered as a near-black silhouette with magenta (#FF3D9A) rim light on one side and cyan (#3DE0FF) on the other, rain-streaked glass, blurred city neon bokeh, deep indigo background (#07081A to #2A1F4A), subtle film grain, elegant curves of the silhouette, no visible skin detail, no text.
```

- 노출 장면은 실루엣과 림라이트로만 처리한다. 인스타와 틱톡의 비팔로워 추천에서 성적 암시 콘텐츠를 빼는 정책에 대응하기 위해서다.

## 작품 팔레트

| 용도 | 색 |
|---|---|
| 밤 남색 / 보라 그림자 | `#1A1E3A` / `#3B2F55` |
| 피부 기준 | `#F3CDB6` (인물별 피부 HEX는 캐릭터 LOCK 우선) |
| 금빛 보케 | `#F2C26B` |
| 인물 대표 색(캘린더 색) | 유진 회색 `#9A9EA3` · 미란 버건디 `#7A1E2E` · 세라 민트 `#7FD1BE` · 하린 하늘색 `#9CC7E8` · 혜숙 금색 `#C9A45C` |
| 코미디 트랙 | 잉크 `#14161C`, 핫핑크 `#E2457A`, 레몬 `#F6D84A`, 크림 `#FFF4E0` |

**대표 색 규칙**: 다섯 여자가 한 컷에 함께 나오면 각자의 대표 색이 옷, 소품, 조명 중 한 곳에는 반드시 들어가게 한다. 독자는 색으로 인물을 구분한다.

## 레터링 (그림에 글자를 넣지 않는다)

이미지에는 글자를 넣지 않는다(`no text`). 말풍선, 효과음, 내레이션은 나중에 Codex가 얹는다.

| 용도 | 폰트(Google Fonts) |
|---|---|
| 대사 | Gowun Dodum |
| 내레이션 박스 | Gowun Batang |
| 효과음, 본편 | East Sea Dokdo |
| 효과음, 코미디 | Black Han Sans |
| 손글씨, 문자 메시지 | Nanum Pen Script |

- 폰트 라이선스는 SIL OFL 계열로 알고 있으나, 배포 전에 폰트마다 확인한다.

## 수위 규칙 (모든 트랙)

- **허용**
  - 몸에 붙는 의상과 깊은 V넥, 슬릿, 크롭.
  - 속옷과 슬립, 드러난 등·어깨·쇄골·허벅지.
  - 시트로 가린 나신, 실루엣, 맞닿은 손과 입술, 땀과 숨.
- **그리지 않는 것**: 성기, 성행위의 직접 묘사, 체액, 미성년으로 보이는 표현.
  - 하린(25)은 동안이라도 성인 체형과 성숙한 표정으로 그린다.
- **아이들**: 지호(5)와 소이(7)는 관능 장면과 같은 컷이나 같은 공간에 두지 않는다.
- **이미지 생성기 정책**: ChatGPT 이미지 생성은 노출 수위가 높은 요청을 거절한다. 거절되면 다음 순서로 바꾼다.
  1. 가림 소품(시트, 커튼, 와인잔, 셔츠 자락)을 넣는다.
  2. 실루엣으로 바꾼다.
  3. 손·입술·사물 인서트로 바꾼다.

## 일관성 규칙

1. 모든 인물 프롬프트는 `characters/<id>.md`의 **CHARACTER LOCK**을 그대로 붙인다.
2. 모든 배경 프롬프트는 `sets.md`의 **SET LOCK**을 그대로 붙인다.
3. 소품이 클로즈업될 때는 `props.md`의 **PROP LOCK**을 붙인다.
4. 확정된 레퍼런스 이미지(`refs/`)를 매번 함께 업로드한다.
5. 실제 브랜드 로고는 그리지 않는다. 롤렉스나 샤넬 등은 '로고 없는 고급 시계', '퀼팅 체인 백'으로 쓴다.
