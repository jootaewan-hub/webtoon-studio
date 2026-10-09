def patch(fn, rep):
    s = open(fn, encoding='utf-8').read()
    for x, y in rep:
        assert x in s, (fn, x[:80])
        s = s.replace(x, y)
    open(fn, 'w', encoding='utf-8').write(s)


patch('data_a.py', [
# 라디오
('material="칠한 금속·플라스틱 케이스, 은색 타공 스피커망, 가죽 손잡이 끈, 뒤판 일자 나사 4"',
 'material="빨간 칠 몸체를 감싼 검은 가죽 커버, 앞면 스피커 자리의 은색 타공 금속판, 가죽 손잡이 끈, 옆면 다이얼 2(주파수·볼륨), 뒤판 일자 나사 4"'),
('colors=["#E3D8BE", "#9A9C98", "#5A3A24", "#C9CCCE"]', 'colors=["#A8322E", "#1E1C1A", "#C9CCCE", "#8C8C88"]'),
('condition="모서리 칠이 벗겨져 회색 바탕이 드러남, 가죽 손잡이 끈이 갈라짐, 다이얼 창 플라스틱이 누렇게 바램"',
 'condition="빨간 칠 모서리가 벗겨져 회색 바탕이 드러남, 검은 가죽 커버와 손잡이 끈이 갈라짐, 눈금 창 플라스틱이 누렇게 바램"'),
('shape="가로로 긴 직사각 상자, 모서리 둥글림. 앞면 왼쪽 2/3는 은색 타공 스피커망, 오른쪽에 둥근 주파수 다이얼과 눈금 창(눈금선만, 숫자·글자 없음). 윗면에 가죽 손잡이 끈과 접힌 은색 안테나. 뒤판은 일자 나사 4개로 고정(동전으로 푼다)"',
 'shape="가로로 긴 직사각 상자, 모서리 둥글림. 빨간 몸체를 검은 가죽 커버가 감싸고 앞면 왼쪽 2/3 스피커 자리만 은색 타공 금속판이 드러남. 오른쪽 옆면에 둥근 다이얼 2개(주파수·볼륨), 앞면 오른쪽 위에 작은 눈금 창(눈금선만, 숫자·글자 없음). 윗면에 가죽 손잡이 끈과 접힌 은색 안테나(안테나는 미확인). 뒤판은 일자 나사 4개(동전으로 푼다)"'),
('ref="미확인(고증 검색 결과로 갱신)",\n  en=dict(name="an old pocket transistor radio"',
 'ref="https://webzine.nfm.go.kr/2017/03/28/%EB%9D%BC%EB%94%94%EC%98%A4-%EC%A0%84%EC%84%B1%EC%8B%9C%EB%8C%80/ (국립민속박물관 웹진: 빨간 본체·검은 가죽 커버·옆면 다이얼·은색 금속판). 안테나·뒤판 나사는 미확인",\n  en=dict(name="an old pocket transistor radio"'),
('shape="a rounded rectangular box, a perforated silver speaker grille on the left two thirds of the front, a round tuning dial and a small dial window with tick marks only on the right, "\n                "a leather carrying strap on top, a folded silver telescopic antenna, four slotted screws on the back panel"',
 'shape="a rounded rectangular red-bodied radio wrapped in a black leather cover, a perforated silver metal speaker plate showing on the left two thirds of the front, two round dials (tuning and volume) on the right side edge, a small dial window with tick marks only, "\n                "a leather carrying strap on top, a folded silver telescopic antenna, four slotted screws on the back panel"'),
('material="painted case, silver metal grille, leather strap", size="15 by 9.5 by 4.5cm",\n          condition="paint chipped off at the corners showing gray underneath, the leather strap cracked, the dial window yellowed"',
 'material="red painted case, black leather cover, silver metal speaker plate, leather strap", size="15 by 9.5 by 4.5cm",\n          condition="red paint chipped off at the corners showing gray underneath, the black leather cover and strap cracked, the dial window yellowed"'),
('condition="still broken but carefully wiped clean, paint more faded, chipped corners, cracked leather strap", era="2003 Seoul"',
 'condition="still broken but carefully wiped clean, red paint more faded, chipped corners, cracked black leather cover and strap", era="2003 Seoul"'),
# 신문
('size="대판 한 면 39×55cm(한 번 접어 39×27.5cm), 단신 기사는 손바닥만 함(8×10cm)"', 'size="대판 한 면 39×54cm(한 번 접어 39×27cm), 단신 기사는 손바닥만 함(8×10cm)"'),
('shape="여러 단으로 나뉜 신문 지면, 맨 아래 구석에 작은 네모 기사(굵은 제목 줄 + 본문 몇 줄). 글자는 그리지 않고 회색 줄로"',
 'shape="1987년식 세로쓰기 지면: 위아래로 흐르는 좁은 세로 글줄이 여러 단, 맨 아래 구석에 작은 네모 기사(굵은 세로 제목 줄 + 세로 본문 몇 줄). 글자는 그리지 않고 회색 줄로"'),
('ref="미확인(고증 검색 결과로 갱신)",\n  en=dict(name="a folded daily newspaper page',
 'ref="https://www.seoul.co.kr/news/1996/10/01/19961001003001 (1987~88 일간지 세로쓰기), https://www.journalist.or.kr/m/m_article.html?no=48168 (대판 39×54cm, 검색 요약). 사회면 단 수·종이 색은 미확인",\n  en=dict(name="a folded daily newspaper page'),
('shape="a broadsheet page divided into many narrow columns of gray text lines and a few blocks, a small boxed brief article in the bottom corner with a bold headline bar, all lettering rendered as illegible gray lines"',
 'shape="a 1980s Korean broadsheet page laid out in vertical writing: many narrow blocks of short vertical gray text lines running top to bottom, a small boxed brief article in the bottom corner with a bold vertical headline bar, all lettering rendered as illegible gray lines"'),
('size="39 by 55cm page, the brief about 8 by 10cm"', 'size="39 by 54cm page, the brief about 8 by 10cm"'),
('shape="the newspaper folded so the small corner article faces up, lettering as illegible gray lines"', 'shape="the newspaper folded so the small corner article faces up, vertical gray text lines, no readable letters"'),
('shape="an extreme close-up of a small newspaper brief, a bold blank headline bar over a few gray text lines"', 'shape="an extreme close-up of a small newspaper brief in vertical layout, a bold blank vertical headline bar beside a few vertical gray text lines"'),
# 정리 예정 알림
('size="B4(25.7×36.4cm)",\n  colors=["#C9C6BC", "#2B2B2B", "#C0302A"]', 'size="19×26cm(1980년대 공문 용지, B5급)",\n  colors=["#C9C6BC", "#2B2B2B", "#C0302A"]'),
('shape="세로 종이, 위에 제목 줄, 본문 여러 줄(글자 대신 선), 아래에 기관 이름 자리와 빨간 네모 도장 하나"',
 'shape="세로 종이, 가로쓰기: 위에 제목 줄, 본문 가로줄 여러 개(글자 대신 선), 아래 발신 기관 자리 끝 글자에 빨간 네모 관인이 걸쳐 찍힘(1986.12 이후 양식, 성명 없음)"'),
('ref="미확인(공문 양식 고증 결과로 갱신)",\n  en=dict(name="a gray official notice sheet with a red seal", shape="a portrait sheet of thin gray paper with a blank title line and rows of illegible typed text marks, a red square official seal stamp near the bottom",\n          material="thin gray newsprint paper, red seal ink", size="B4, 25.7 by 36.4cm"',
 'ref="https://theme.archives.go.kr/next/officialDocument/docSketch02.do?page=2 (국가기록원: 가로쓰기, 19×26cm 안팎 용지, 관인 위치). 관인 크기는 미확인",\n  en=dict(name="a gray official notice sheet with a red seal", shape="a portrait sheet of thin gray paper written horizontally: a blank title line and rows of illegible horizontal typed text marks, a red square official seal stamped over the last character of the issuing office name near the bottom",\n          material="thin gray newsprint paper, red seal ink", size="19 by 26cm"'),
])

patch('spec_b.py', [
('"흰 육각 몸통·검은 캡 볼펜",\n  "길이 14cm", ["#F2F0EA", "#1E1E1E"],\n  "몸통 끝을 씹은 자국",\n  "육각 몸통에 검은 캡과 꼭지",',
 '"흰 육각 몸통 노크식 볼펜(캡 없음)",\n  "길이 14cm(미확인)", ["#F2F0EA", "#1E1E1E", "#A7ACB0"],\n  "몸통 끝을 씹은 자국",\n  "흰 육각 플라스틱 몸통, 위에 검은 노크 버튼, 아래 금속 팁. 캡 없음",'),
('("a plain ballpoint pen", "a white hexagonal barrel with a black cap and tip", "plastic", "14cm long", "chewed end")',
 '("a plain click ballpoint pen", "a white hexagonal plastic barrel with a black click button on top and a metal tip, no cap", "plastic, metal tip", "14cm long", "chewed end")'),
('"지폐 약 15×7cm, 동전 지름 2~2.5cm", ["#8FA06A", "#C7CBC9", "#B07A4A"]',
 '"천 원권 15.1×7.6cm, 동전 10원 지름 2.29cm(황동)·50원 2.16cm·100원 2.4cm(백동)", ["#9A86B0", "#C9A24A", "#C7CBC9"]'),
('"paper, metal", "note about 15 by 7cm, coins 2 to 2.5cm", "crumpled note, worn coins"',
 '"purplish paper note, brass and silvery cupronickel coins", "note 15.1 by 7.6cm, coins 2.16 to 2.4cm", "crumpled note, worn coins"'),
('"버스 토큰(금속 주화 모양) — 크기·재질은 고증 결과로 확정",\n  "지름 약 2cm", ["#C9A24A", "#8A7A50"],\n  "손때로 반질",\n  "가운데 구멍이 있거나 없는 작은 원판(고증 결과로 확정), 무늬 없음",',
 '"황동 버스 토큰(일반용)",\n  "지름 1.8cm, 가운데 둥근 구멍", ["#C9A24A", "#8A7A50"],\n  "손때로 반질",\n  "가운데 둥근 구멍이 뚫린 누런 황동 원판, 무늬 없음",'),
('("a city bus token", "a small plain metal disc token", "brass-colored metal", "about 2cm across", "worn shiny by handling")',
 '("a brass city bus token", "a small plain brass disc with a round hole in the center", "brass", "1.8cm across", "worn shiny by handling")'),
('"올림픽 표어 포스터(종이 인쇄, 표어만)",', '"올림픽 표어 포스터(종이 인쇄, 표어만 — 식자 문구 예: \'선진국 시민답게, 올림픽 주인답게\')",'),
('"기워 덧댄 캔버스 천막(나무 기둥) — 색은 고증 결과로 확정",\n  "폭 6m·깊이 4m·높이 2.5m, 기둥 지름 10cm", ["#C8A574", "#8A6A45", "#C7843A", "#5A4A3A"],',
 '"바랜 캔버스 천막에 파랑·흰 줄무늬 방수포 조각을 덧댐, 나무 기둥",\n  "폭 600cm·깊이 400cm·높이 250cm, 기둥 지름 10cm", ["#C8A574", "#8A6A45", "#3E6E9E", "#E8E2D6"],'),
('"rain stains, patches of different colors"),\n  notes="천막 색(카키 캔버스 vs 주황 비닐)은 고증 결과로 확정"',
 '"rain stains, patches of blue-and-white striped tarpaulin sewn on"),\n  notes="주황 비닐 천막은 1987 근거 없음(고증) — 바랜 캔버스와 줄무늬 방수포"'),
('("a patched canvas tent eating place", "a rectangular canvas tent on wooden poles with the front flap rolled up, mismatched patches sewn on, a bulb hanging from a pole"',
 '("a patched canvas tent eating place", "a rectangular faded canvas tent on wooden poles with the front flap rolled up, patches of blue-and-white striped tarpaulin sewn on, a bulb hanging from a pole"'),
('"밥그릇 지름 11cm·높이 7cm, 국그릇 지름 14cm, 숟가락 20cm, 젓가락 21cm"', '"밥그릇 안지름 10.5cm·높이 6cm(1976 서울시 규격), 국그릇 지름 14cm, 숟가락 20cm, 젓가락 21cm"'),
('"rice bowl 11cm across, spoon 20cm"', '"rice bowl 10.5cm across and 6cm tall, spoon 20cm"'),
('"백열전구(맑은 유리), 소켓, 전깃줄",', '"60W 백열전구(맑은 유리), 소켓, 전깃줄",'),
('("a bare incandescent light bulb hanging on a cord"', '("a bare 60W incandescent light bulb hanging on a cord"'),
('"목화솜 이불(홑청 씌움)",\n  "150×200cm, 두께 6cm", ["#C9636A", "#F1E6D2", "#7A8A5A"],\n  "빨아 바랜 홑청, 솜이 뭉친 자리",\n  "꽃무늬(분홍 바탕 큰 꽃) 이불. 은주·동민이 둘둘 말아 기어 다님",',
 '"두툼한 밍크담요(큰 꽃무늬)",\n  "150×200cm, 두께 1.5cm", ["#C9636A", "#F1E6D2", "#7A3E4A"],\n  "보풀, 빨아 바램",\n  "자줏빛 바탕에 큰 장미 무늬가 화려한 털 담요. 은주·동민이 둘둘 말아 기어 다님",'),
('("a padded cotton quilt", "a thick quilt with a pink cover printed with large flowers", "cotton cover, cotton batting", "150 by 200cm, 6cm thick", "faded from washing, lumpy batting")',
 '("a thick plush Korean mink blanket", "a heavy plush blanket with a bold large rose pattern on a deep pink ground", "acrylic plush", "150 by 200cm", "pilled and faded from washing, not modern microfiber")'),
('  notes="무늬·색은 고증 결과로 조정"),\n"plywood_wall"', '  notes="1970~80년대 밍크담요 유행(고증 일부 확인). 대본 \'이불\'을 밍크담요로 그림 — 목화솜 이불도 가능"),\n"plywood_wall"'),
('"짐칸 길이 180cm·폭 90cm, 손잡이 포함 전체 길이 260cm, 바퀴 지름 60cm"', '"전체 길이 약 200cm·폭 약 150cm(바퀴 바깥)·짐칸 높이 50cm, 26인치(66cm) 자전거형 바퀴"'),
('"bed 180 by 90cm, wheels 60cm"', '"about 200cm long and 150cm wide, 26-inch (66cm) bicycle-type wheels"'),
('notes="크기·색은 고증 결과로 확정"),\n"blanket"', 'notes="크기는 현재 기준(고증 일부 확인), 색은 미확인"),\n"blanket"'),
('"원통형 손전등(건전지 2개) — 재질·색은 고증 결과로 확정",', '"원통형 백열 손전등(D형 건전지 2개)",'),
('"a tube body with a wider head, a slide switch on the side and a hanging loop at the tail", "metal or plastic", "20cm long", "chipped finish, dull reflector"',
 '"a tube body for two D-cell batteries with a wider head, an incandescent bulb behind a dull reflector giving a warm yellow beam, a slide switch on the side and a hanging loop at the tail", "metal or plastic", "20cm long", "chipped finish, dull reflector"'),
('"원통형 기름통 위에 둥근 화구와 받침살 셋, 앞에 심지 올리는 작은 손잡이, 화구 창으로 파란 불꽃",',
 '"바닥의 원통형 기름통(주입구 뚜껑), 위에 둥근 화구와 받침살 셋, 앞에 심지 올리는 작은 손잡이, 화구 창으로 파란 불꽃",'),
('"a cylindrical fuel tank with a round burner on top,', '"a cylindrical fuel tank at the base with a filler cap, a round burner on top,'),
('notes="색·모양은 고증 결과로 확정"),', 'notes="구조는 고증 일부 확인, 크기·색은 미확인"),'),
('notes="재질(PP 마대 vs 황마 자루)은 고증 결과로 확정"),', 'notes="PP 마대는 1970년대부터 국내 생산(고증 일부 확인)"),'),
('notes="저울 형식(걸이 용수철 저울 vs 대저울)은 고증 결과로 확정"),', 'notes="저울 종류(대저울·앉은뱅이·용수철)는 고증 확인, 고물상이 어느 것을 썼는지는 미확인 — 대본 \'바늘\'에 맞춰 용수철 눈금 저울"),'),
('"낡은 관광(전세) 버스 — 외형은 고증 결과로 확정",', '"낡은 관광(전세) 버스(리어엔진 각진 차체)",'),
('("an old 1980s Korean chartered coach bus", "a flat-fronted large bus', '("an old 1980s Korean chartered coach bus", "a boxy rear-engine coach with a flat front'),
('"국밥(뚝배기) — 그릇 형태는 고증 결과로",', '"국밥(흑갈색 뚝배기)",'),
])

patch('spec_c.py', [
('"원통형 연탄난로 위 노란 양은 주전자, 연통"', '"원통형 연탄난로(22공탄 2장 들어감) 위 노란 양은 주전자, 위로 올라가는 양철 연통"'),
('("a coal-briquette heater with an aluminum kettle", "a cylindrical briquette stove with a stovepipe and a yellowish aluminum kettle steaming on top"',
 '("a coal-briquette heater with an aluminum kettle", "a cylindrical briquette stove with a tin stovepipe rising from it and a yellowish aluminum kettle steaming on top"'),
('"원통 화덕 속 구멍 뚫린 연탄"', '"원통 화덕 속 22공탄(지름 15.8cm·높이 15.2cm)"'),
('"a round brazier holding a perforated coal briquette glowing faintly"', '"a round brazier holding a cylindrical coal briquette with 22 holes (15.8cm across, 15.2cm tall) glowing faintly"'),
('"운전석 옆 토큰함, 손잡이 줄, 좁은 좌석"', '"운전석 옆 요금통(앞문 승차, 안내양 없음), 손잡이 줄, 좁은 좌석. 외부 도색 보라·하늘색(미확인)"'),
('"rows of worn seats, hanging straps, a fare token box beside the driver\'s seat"', '"rows of worn seats, hanging straps, a fare box beside the driver\'s seat at the front door, no bus conductor"'),
('"길이 470cm", ["#3E6E5A", "#E8E2D6", "#5A5E62"]', '"길이 452cm(1톤 캡오버 트럭)", ["#3E6E5A", "#E8E2D6", "#5A5E62"]'),
('"steel", "470cm long", "faded paint")', '"steel", "452cm long", "faded paint")'),
('"길이 470cm", ["#3E6E5A", "#8A6A45", "#E8E2D6"]', '"길이 452cm(1톤 캡오버 트럭)", ["#3E6E5A", "#8A6A45", "#E8E2D6"]'),
('"steel", "470cm long each"', '"steel", "452cm long each"'),
('"녹색 칠판(나무 틀)"', '"녹색 칠판(철판에 도료)"'),
('"painted board, wood", "180 by 90cm", "smudged")', '"painted steel board, wooden frame", "180 by 90cm", "smudged")'),
('"큰 숫자 칸(글자 대신 칸만), 위에 단순한 풍경 그림"', '"위에 한복 입은 여인 사진(누구도 닮지 않은 얼굴), 아래 날짜 칸(글자 대신 칸만)"'),
('"a wall calendar with a simple landscape picture on top and a blank grid of day boxes, no readable numbers"', '"a wall calendar with a photo of a woman in hanbok on top (generic face, not a real person) and a blank grid of day boxes, no readable numbers"'),
('"B5 18.2×25.7cm", ["#E8E2D0", "#2B2B2B"]', '"19×26cm", ["#E8E2D0", "#2B2B2B"]'),
('"a ruled form sheet with blank boxes and illegible text marks", "paper", "18.2 by 25.7cm"', '"a ruled form sheet written horizontally with blank boxes and illegible text marks", "paper", "19 by 26cm"'),
('"정식 통보 공문(빨간 도장 둘)", "B4 25.7×36.4cm"', '"정식 통보 공문(빨간 도장 둘, 가로쓰기)", "19×26cm"'),
('"a portrait notice sheet with a blank title line, illegible typed lines and two red square seals", "paper", "25.7 by 36.4cm"', '"a portrait notice sheet written horizontally with a blank title line, illegible typed lines and two red square seals", "paper", "19 by 26cm"'),
('"이주 공문(1988년 7월)", "B4 25.7×36.4cm"', '"이주 공문(1988년 7월, 가로쓰기)", "19×26cm"'),
('"a portrait notice sheet with illegible typed lines and a red square seal", "paper", "25.7 by 36.4cm"', '"a portrait notice sheet written horizontally with illegible typed lines and a red square seal", "paper", "19 by 26cm"'),
('"보고서 표지·본문(식자)", "B4 25.7×36.4cm"', '"보고서 표지·본문(식자, 가로쓰기)", "19×26cm"'),
('"paper", "25.7 by 36.4cm", "one blurred spot")', '"paper", "19 by 26cm", "one blurred spot")'),
])

r = open('research.py', encoding='utf-8').read()
if 'research_r2' not in r:
    r += ("\nfrom research_r2 import R2, G2\nfrom research_r3 import R3, G3, A3\n"
          "for _d in (R2, R3):\n    for _k, _v in _d.items():\n        RES.setdefault(_k, []).extend(_v)\n"
          "ANACHRONISM += A3\nGUARD = G2 + G3\n")
    open('research.py', 'w', encoding='utf-8').write(r)
print('ok')
