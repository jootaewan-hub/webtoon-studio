def patch(fn, rep):
    s = open(fn, encoding='utf-8').read()
    for x, y in rep:
        assert x in s, (fn, x[:80])
        s = s.replace(x, y)
    open(fn, 'w', encoding='utf-8').write(s)


patch('data_a.py', [
('material="빨간 칠 몸체를 감싼 검은 가죽 커버, 앞면 스피커 자리의 은색 타공 금속판, 가죽 손잡이 끈, 옆면 다이얼 2(주파수·볼륨), 뒤판 일자 나사 4"',
 'material="빨간 칠 케이스(칠 아래 회색 바탕), 앞면 스피커 자리의 은색 타공 금속판, 갈색 가죽 손잡이 끈, 옆면 다이얼 2(주파수·볼륨), 뒤판 일자 나사 4"'),
('colors=["#A8322E", "#1E1C1A", "#C9CCCE", "#8C8C88"]', 'colors=["#A8322E", "#C9CCCE", "#5A3A24", "#8C8C88"]'),
('condition="빨간 칠 모서리가 벗겨져 회색 바탕이 드러남, 검은 가죽 커버와 손잡이 끈이 갈라짐, 눈금 창 플라스틱이 누렇게 바램"',
 'condition="빨간 칠 모서리가 벗겨져 회색 바탕이 드러남(대본 1-5), 가죽 손잡이 끈이 갈라짐, 눈금 창 플라스틱이 누렇게 바램"'),
('빨간 몸체를 검은 가죽 커버가 감싸고 앞면 왼쪽 2/3 스피커 자리만 은색 타공 금속판이 드러남.', '빨간 칠 몸체, 앞면 왼쪽 2/3는 은색 타공 금속판(스피커).'),
('(국립민속박물관 웹진: 빨간 본체·검은 가죽 커버·옆면 다이얼·은색 금속판). 안테나·뒤판 나사는 미확인"',
 '(국립민속박물관 웹진: 빨간 본체·옆면 다이얼·은색 금속판 반영. 같은 글의 \'검은 가죽 커버\'는 대본 1-5 \'모서리 칠이 벗겨지고 손잡이 가죽이 갈라져\'와 맞지 않아 넣지 않음). 안테나·뒤판 나사는 미확인"'),
('shape="a rounded rectangular red-bodied radio wrapped in a black leather cover, a perforated silver metal speaker plate showing on the left two thirds of the front,',
 'shape="a rounded rectangular box with a red painted body, a perforated silver metal speaker plate on the left two thirds of the front,'),
('material="red painted case, black leather cover, silver metal speaker plate, leather strap", size="15 by 9.5 by 4.5cm",\n          condition="red paint chipped off at the corners showing gray underneath, the black leather cover and strap cracked, the dial window yellowed"',
 'material="red painted case, silver metal speaker plate, brown leather strap", size="15 by 9.5 by 4.5cm",\n          condition="red paint chipped off at the corners showing gray underneath, the leather strap cracked, the dial window yellowed"'),
('condition="still broken but carefully wiped clean, red paint more faded, chipped corners, cracked black leather cover and strap", era="2003 Seoul"',
 'condition="still broken but carefully wiped clean, red paint more faded, chipped corners showing gray, cracked leather strap", era="2003 Seoul"'),
# 빨간 손수건 씬: 착용자 기준
('P("red_neckerchief", "빨간 손수건(본선 목 스카프)", "A",\n  R("3-16..3-30"),',
 'P("red_neckerchief", "빨간 손수건(본선 목 스카프)", "A",\n  NECK,'),
('S("red_neckerchief__s1_flat", "펼친 천(만든 그대로)", R("3-16"), "접기 전 삼각 천 — 콘티 참조용",',
 'S("red_neckerchief__s1_flat", "펼친 천(만든 그대로)", NECK[:1], "화면에 펼친 모습은 나오지 않음 — 맨 모습을 그리기 전 콘티 참고용 시트(씬 칸은 첫 착용 씬)",'),
('S("red_neckerchief__s2_tied", "목에 맨 모습", R("3-16..3-30"), "아이들 목에 매어 앞에서 한 번 묶음"),',
 'S("red_neckerchief__s2_tied", "목에 맨 모습", NECK, "아이들 목에 매어 앞에서 한 번 묶음"),'),
('from common import P, S, R\n', 'from common import P, S, R, char_scenes\nNECK = char_scenes("dongmin", "mija", "deoksu", "bonggu", "yeongran", "gyeongho", "gyeongmin", "suni", "seoki", outfit="빨간 손수건")\nNECK = sorted(set(NECK), key=lambda s: (int(s.split("-")[0]), int(s.split("-")[1])))\n'),
])

patch('spec_b.py', [
('"두툼한 밍크담요(큰 꽃무늬)",\n  "150×200cm, 두께 1.5cm", ["#C9636A", "#F1E6D2", "#7A3E4A"],\n  "보풀, 빨아 바램",\n  "자줏빛 바탕에 큰 장미 무늬가 화려한 털 담요. 은주·동민이 둘둘 말아 기어 다님",',
 '"목화솜 이불(홑청 씌움)",\n  "150×200cm, 두께 6cm", ["#C9636A", "#F1E6D2", "#7A8A5A"],\n  "빨아 바랜 홑청, 솜이 뭉친 자리",\n  "분홍 바탕 큰 꽃무늬 홑청 이불. 은주·동민이 둘둘 말아 기어 다님",'),
('("a thick plush Korean mink blanket", "a heavy plush blanket with a bold large rose pattern on a deep pink ground", "acrylic plush", "150 by 200cm", "pilled and faded from washing, not modern microfiber")',
 '("a padded cotton quilt", "a thick quilt with a pink cover printed with large flowers", "cotton cover, cotton batting", "150 by 200cm, 6cm thick", "faded from washing, lumpy batting")'),
('notes="1970~80년대 밍크담요 유행(고증 일부 확인). 대본 \'이불\'을 밍크담요로 그림 — 목화솜 이불도 가능"),',
 'notes="대본대로 이불(목화솜). 1970~80년대 밍크담요 유행 자료(홍보성 매체, 검색 요약)가 있어 밍크담요로 바꿔도 됨 — 선택지(props.md 디자인 판단)"),'),
])

patch('research_r2.py', [
('"https://theweekly.co.kr/ (신앙촌 관련 매체, 홍보성, 검색 요약)"',
 '"https://theweekly.co.kr/%EB%82%B4%EA%B0%80-%EB%BD%91%EC%9D%80-%EC%8B%A0%EC%95%99%EC%B4%8C-%EC%A0%9C%ED%92%88-%EB%B2%A0%EC%8A%A4%ED%8A%B8-10-%EC%8B%A0%EC%95%99%EC%B4%8C-%EB%B0%8D%ED%81%AC%EB%8B%B4%EC%9A%94/ (신앙촌 관련 매체, 홍보성, 검색 요약)"'),
])

patch('judgments.py', [
('"\'기본 시트와 같음\' 상태',
 '"이불(B): 대본 \'이불\'대로 목화솜 꽃무늬 이불로 그림. 1970~80년대 밍크담요 유행 자료(홍보성)가 있어 밍크담요로 바꾸는 선택지를 남김",\n"엄마의 라디오: 고증의 빨간 본체·옆면 다이얼·은색 금속판은 반영, 같은 회고의 \'검은 가죽 커버\'는 대본 1-5(모서리 칠 벗겨짐·손잡이 가죽)와 충돌해 뺌",\n"\'prompt_en에는 확인된 사실만\'의 적용: 대본·연속성 문서에 적힌 사실 + 웹 고증으로 확인된 시대 사실(치수·재질·색) + 디자인 판단(props.md에 표시)으로 프롬프트를 썼다. 확인 못 한 시대 세부(예: 1980년대 한국 분유통 치수, 드럼통 칠 색)는 수치로 고정하되 ref·고증 표에 \'미확인/추측\'으로 표시했다",\n"\'기본 시트와 같음\' 상태'),
])
print("fixed")
