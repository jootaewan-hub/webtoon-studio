# G6 그림체 3안 (2026-10-09)

> **최종 결정은 `design/style_guide.md`(정밀 셀 반실사 「소리의 색」, 콘티 정합형).** 사용자 지시 "구체적인 콘티를 최대한 반영한 안으로, 그래야 GPT가 정확하게 그려낼 수 있으니"에 따라 아래 '추천'(1안 기본)과 다르게, 2안의 선·셀을 바탕으로 1안의 장면별 빛과 3안의 소리 색 규칙을 섞어 확정했다. 이 문서는 비교 기록이다. 확정안 맛보기 `design/style/style_final.svg`.

같은 장면(1화 S#11 '첫 소리': 해 질 녘 작은 산 꼭대기, 은주가 동그리를 처음 켜는 순간)을 세 화풍으로 그린 맛보기: `design/style/style_a.svg`, `style_b.svg`, `style_c.svg`(생성기 `design/style/gen.py`, 한눈에 보기 `design/style/preview.html`). 맛보기는 선·채색·명암·효과음 처리를 비교하는 도식 러프다. 실제 작화는 아래 '이미지 프롬프트'로 ChatGPT·Codex에서 만든다.

판단 기준(G0~G5 확정 사항):
- 12세 이상, 감동·밝음·희망. 1987~88년 서울 변두리 쓰레기 섬의 가난을 정직하게, 그러나 무겁지 않게.
- 소리가 주인공인 작품이다. 은주가 소리를 가려 듣는 순간을 그림으로 보여 줄 방법(효과음 레터링, 소리의 시각화)이 그림체 안에 있어야 한다.
- 웹툰 3화(회당 60~80컷)와 애니(G11) 둘 다 쓴다. 애니로 옮기기 쉬운지도 본다.
- 아동 인물이 주인공이다. 비율·표정은 나이대로 보이게 하고, 꾸밈은 하지 않는다.

## 1안 — 수채 반실사 「금빛 먼지」
- 선: 가는 갈색 연필 선(1px 안팎). 선은 형태를 잡는 정도이고 면과 빛이 주인공
- 채색: 수채 번짐 + 브러시 반실사. 종이 질감을 깔고, 가장자리가 살짝 번진다
- 명암: 부드러운 그러데이션 + 역광 림라이트(노을·먼지 낀 빛)
- 배경: 사진 기반 단순화. 쓰레기 산은 색 덩어리로 뭉개고, 가까운 고물만 형태를 준다
- 비율: 아이 5.5~6등신, 어른 6.5~7등신. 데포르메는 거의 쓰지 않음(코미디는 표정과 타이밍으로)
- 효과음·소리: 붓·연필 손글씨 효과음, 크기 작게. 소리는 부드러운 빛의 동심원·먼지 입자로
- 팔레트: #7C8FB0 새벽·저녁 하늘 / #F2C14E 금빛(첫 소리·기립) / #C99A62 흙빛 쓰레기 산 / #6E5640 그늘 갈색 / #3C4A6E 은주 점퍼 남색 / #E7B790 피부 / #FFF1C9 빛
- 폰트: 대사 Gowun Dodum / 내레이션 Gowun Batang / 효과음 Nanum Pen Script(큰 소리는 Gaegu Bold) / 손글씨 Nanum Pen Script
- 맞는 이유: 감동·향수·희망 톤에 가장 가깝다. 비트 시트의 컬러 스크립트(신비 청회색 → 첫 소리 금빛 → 절망 남색 → 기립 금빛)를 빛으로 그대로 살릴 수 있다. 1980년대 사진의 흐린 색감과도 맞는다
- 약점·비용: 수채 번짐은 컷마다 일관성을 지키기 어렵고 이미지 생성에서 들쭉날쭉하다. 쇼츠 썸네일에서 대비가 약하다. 애니로 옮길 때 배경 미술 비용이 크다
- 맛보기: `design/style/style_a.svg`

## 2안 — 셀 팝 「깡통 팝」
- 선: 굵은 잉크 외곽선(3~4px), 둥근 끝
- 채색: 셀 2단(밝은 면/그림자 면), 고채도. 악기마다 대표 색(동그리 은색, 뚱보 빨강, 꽥꽥이 파랑, 뼈다귀 북 초록)
- 명암: 딱 떨어지는 그림자 한 단. 빛 효과는 최소
- 배경: 평면 도형으로 단순화. 쓰레기 더미는 색 조각의 리듬으로
- 비율: 아이 4.5~5등신, 어른 6등신. 리액션 컷에서 2~3등신 데포르메 허용
- 효과음·소리: 굵은 고딕 효과음 + 흰 외곽선, 효과선 많음. 소리를 그래픽(방사선·글자 크기)으로 크게 보여 준다
- 팔레트: #1B1A1F 잉크 / #FF8A4C 노을 주황 / #FFC861 금빛 / #9C6B4E 쓰레기 산 / #2F55A4 은주 점퍼 / #5EC6C9 강 / #E2574C 포인트 빨강
- 폰트: 대사 Jua / 내레이션 Gowun Dodum / 효과음 Black Han Sans / 손글씨 Gaegu
- 맞는 이유: 12세 독자에게 가장 친숙하고, 동민·미자·덕수의 코미디(2화 엉망진창 몽타주)가 가장 산다. 셀 채색은 애니 제작 파이프라인과 바로 이어지고, 이미지 생성에서도 인물 일관성을 지키기 쉽다. 쇼츠 썸네일에서 가장 잘 읽힌다
- 약점·비용: 1980년대 가난의 질감과 향수가 가벼워진다. 2화의 상처(던져진 바이올린, 소리굽쇠를 빼다)와 3화 클라이맥스의 숨 멈춤이 만화적으로 보일 수 있다
- 맛보기: `design/style/style_b.svg`

## 3안 — 잿빛 섬, 소리만 색 「소리의 색」
- 선: 목탄·연필 질감의 거친 선(1.5~2px), 흔들림 있음
- 채색: 섬과 일상은 회갈색 모노톤. **은주가 소리를 가려 듣는 순간과 음악이 날 때만 그 소리 주변에 색이 번진다**(소리마다 색: 동그리 금빛, 뚱보 주황, 꽥꽥이 청록, 뼈다귀 북 빨강)
- 명암: 모노톤 부분은 중간 대비 + 필름 그레인. 색이 번지는 부분은 빛처럼 밝게
- 배경: 거친 질감의 단순화. 판화 같은 면 분할
- 비율: 아이 5.5~6등신, 어른 7등신. 데포르메 거의 없음
- 효과음·소리: 소리 효과음만 색을 갖는다(붓 손글씨). 일상 소음은 회색 작은 글씨
- 팔레트: #3E3B38 잿빛 / #6E6A65 회갈색 / #A8A39B 흐린 하늘 / #E8E4DC 종이 흰색 / #F5C04A 동그리 금빛 / #E8944A 뚱보 주황 / #4FB3A9 꽥꽥이 청록
- 폰트: 대사 Noto Sans KR / 내레이션 Nanum Myeongjo / 효과음 East Sea Dokdo / 손글씨 Nanum Pen Script
- 맞는 이유: '소리가 주인공'이라는 작품의 개념을 그림 규칙 하나로 보여 준다. 1화 회색 섬 → 3화 본선에서 온 화면이 색으로 가득 차는 흐름이 곧 이야기의 성장 곡선이 된다. 에필로그(공원이 된 언덕)는 처음으로 '소리 없이도' 색이 있는 화면
- 약점·비용: 감동·밝음·희망 톤에 비해 1~2화가 어둡고 무겁게 보일 수 있다(12세 독자에게 진입 장벽). 색을 쓰는 규칙을 3화 내내 지키는 연출 관리가 필요하다. 모노톤 컷이 많아 썸네일에서 손해
- 맛보기: `design/style/style_c.svg`

## 추천
**1안을 기본으로, 3안의 '소리가 나면 색이 번진다' 규칙을 연출 장치로만 섞는 하이브리드.**
- 평소 화면은 1안의 따뜻한 수채 반실사(밝음·희망 톤 유지).
- 은주가 소리를 가려 듣는 순간(대본의 `— 주변 소리 빠지고 그 소리만 남는다`)에는 주변 채도를 낮추고 그 소리만 색과 빛으로 남긴다. 3안의 장점을 '특별한 순간'에만 쓰므로 어둡지 않다.
- 2안의 데포르메는 코미디 컷(2화 몽타주, 동민 리액션)에만 2~3컷 단위로 허용.
- 약점 보완: 수채 일관성은 G7에서 인물 시트를 먼저 고정하고, 이미지 프롬프트에 팔레트 HEX와 선 굵기를 매번 넣어 관리한다.

## 이미지 프롬프트 (ChatGPT·Codex용, 안별 같은 장면)

공통 장면: `1987, a fictional landfill island on the edge of Seoul at sunset. A 13-year-old Korean girl (small and thin, tanned skin, long hair tied low with one rubber band, oversized navy jacket, worn trousers, rubber boots) stands on top of a hill of trash and plays, for the first time, a violin made from a large rusted powdered-milk can with a wooden-spoon neck and a bent-fork bridge. Eyes nearly closed, holding her breath. Golden dust in the air, the Han River behind. Fictional character, not resembling any real person. No brand logos, no text.`

- 1안: `+ soft watercolor and brush semi-realistic style, thin brown pencil lines, warm golden backlight rim light, paper texture, gentle gradients, muted nostalgic 1980s colors, palette #7C8FB0 #F2C14E #C99A62 #6E5640 #3C4A6E #E7B790, vertical webtoon panel`
- 2안: `+ bold clean ink outlines 3-4px, two-tone cel shading, saturated flat colors, simplified geometric background, comic speed lines radiating from the instrument, palette #1B1A1F #FF8A4C #FFC861 #9C6B4E #2F55A4 #5EC6C9, vertical webtoon panel`
- 3안: `+ charcoal and pencil textured lines, the whole scene in desaturated gray-brown monotone with film grain, only the sound coming from the can violin glows in warm gold color spreading into the air, palette #3E3B38 #6E6A65 #A8A39B #E8E4DC with accent #F5C04A, vertical webtoon panel`

폰트는 모두 Google Fonts(SIL Open Font License) 배포본이라 상업 사용이 가능한 것으로 안다. 최종 배포 전에 각 폰트 라이선스 파일을 다시 확인한다(미확인).
