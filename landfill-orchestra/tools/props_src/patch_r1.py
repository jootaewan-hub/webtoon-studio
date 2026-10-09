a = open('data_a.py', encoding='utf-8').read()
rep = [
('colors=["#9FC7B0", "#7A4E2A", "#E3EEF0", "#8FB8D8"]', 'colors=["#E3EEF0", "#BFD8E0", "#7A4E2A", "#8FB8D8"]'),
('material="빈 유리병 6개(투명·연녹색·갈색 섞임, 상표 라벨 없음), 물, 두드리는 쇠 숟가락 2"', 'material="빈 유리병 6개(투명·연하늘색·갈색 섞임, 초록 병 없음 — 초록 소주병은 1994년부터, 상표 라벨 없음), 물, 두드리는 쇠 숟가락 2"'),
('material="clear, pale green and brown glass, water"', 'material="clear, pale blue and brown glass, no green bottles, water"'),
('ref="미확인",\n  en=dict(name="a bottle xylophone"', 'ref="https://www.insight.co.kr/news/473379 (초록 소주병 1994년부터, 검색 요약). 병 크기는 미확인",\n  en=dict(name="a bottle xylophone"'),
('"the cut rim of the drum exposed all around, an old worn cello bow shown beside it"', '"one raised rolling hoop ring around the middle of the drum body, the cut rim of the drum exposed all around, an old worn cello bow shown beside it"'),
('원판 앞면 가운데쯤 나무토막 줄받침,', '몸통 가운데 둘레에 드럼통 굴림 테(볼록한 띠) 한 줄. 원판 앞면 가운데쯤 나무토막 줄받침,'),
('size="높이 140cm(은주 키와 같음, 1-12). 몸통 지름 57cm·깊이 44cm, 각목 목 5×5cm 굵기·몸통 위로 83cm"', 'size="높이 140cm(은주 키와 같음, 1-12). 몸통 지름 58cm·깊이 44cm(200L 드럼 높이 약 88cm의 반), 각목 목 5×5cm 굵기·몸통 위로 82cm"'),
('size="140cm tall overall, drum body 57cm diameter and 44cm deep, beam 5cm square"', 'size="140cm tall overall, drum body 58cm diameter and 44cm deep, beam 5cm square"'),
("ref=\"형태 참고만(카테우라 콘트라베이스 '금속 통·볼트·재활용 나무': research/notes.md Commons 링크). 드럼통을 가로로 자르는 방식·원판을 앞판으로 쓰는 구조는 디자인 판단(미확인)\"",
 'ref="https://en.wikipedia.org/wiki/Recycled_Orchestra_of_Cateura (카테우라 첼로=오일 드럼), https://www.pachmas.com/info/products/metal_drums/01thcyl/216.htm (드럼 치수, 검색 요약). 가로로 잘라 원판을 앞판으로 쓰는 구조는 디자인 판단(미확인)"'),
('size="통 지름 30cm·높이 36cm, 철사 손잡이. 필름은 통 위를 덮고 옆으로 5cm 내려옴"', 'size="통 위 지름 30cm·아래 지름 28cm·높이 34cm, 철사 손잡이. 필름 한 장 35×43cm를 덮어 옆으로 5cm 내려옴"'),
('size="30cm diameter, 36cm tall"', 'size="30cm across the top tapering to 28cm at the bottom, 34cm tall, film sheet 35 by 43cm"'),
('shape="a round steel paint can with a wire bail handle,', 'shape="a round steel paint pail slightly tapered toward the bottom with a wire bail handle,'),
('ref="고정 방식: 카테우라 X선 필름 북을 포장 테이프로 감음 — research/notes.md https://www.michiganpublic.org/2016-09-14/from-trash-to-triumph-the-recycled-orchestra. 페인트 통 크기는 미확인"',
 'ref="https://en.wikipedia.org/wiki/Recycled_Orchestra_of_Cateura (X선 필름+포장 테이프), https://mms.mckesson.com/product/381330 (필름 35×43cm, 검색 요약). 한국 18L 페인트 통 치수는 미확인(해외 5갤런 통 기준)"'),
('size="소리굽쇠 길이 8cm(손잡이 3cm, 가지 2개 각 5cm·폭 0.5cm), 사슬 길이 60cm·굵기 1mm"', 'size="소리굽쇠 길이 10cm(손잡이 3.5cm, 가지 2개 각 6.5cm, 둥근 막대 굵기 0.36cm), 사슬 길이 60cm·굵기 0.1cm"'),
('size="fork 8cm long, chain 60cm"', 'size="fork 10cm long with 0.36cm round tines, chain 60cm"'),
('shape="a U-shaped tuning fork with two straight tines and a short stem', 'shape="a U-shaped tuning fork of round steel rod with two straight tines and a short stem'),
('ref="미확인(소형 소리굽쇠 치수는 추측)"', 'ref="https://www.stretta-music.dk/tuning-fork-km-168-nr-457627.html (A440 소리굽쇠 약 10.5cm, 검색 요약). 목걸이 고리·사슬은 디자인 판단"'),
('조립 길이 66cm, 관 지름 약 3cm', '조립 길이 66cm(마우스피스 포함, 배럴~벨 60cm), 관 지름 약 3cm'),
('ref="미확인",\n  en=dict(name="a B-flat clarinet"', 'ref="https://emuseum.nmmusd.org/objects/17821/clarinet-bflat (미국 국립음악박물관, 검색 요약). 1970년대 한국 쇼단·케이스는 미확인",\n  en=dict(name="a B-flat clarinet"'),
('ref="미확인(일반 바이올린 치수)"', 'ref="https://fiddlerman.com/what-size-violin-should-i-get/ (4/4 치수, 검색 요약)"'),
("ref=\"미확인\",\n  en=dict(name=\"a conductor's baton", "ref=\"https://en.wikipedia.org/wiki/Baton_(conducting) (지휘봉 30~41cm, 검색 요약)\",\n  en=dict(name=\"a conductor's baton"),
('material="양은(알루미늄) 냄비 뚜껑 2개, 꼭지는 검은 베이클라이트 손잡이"', 'material="양은(노란 아노다이징 알루미늄) 냄비 뚜껑 2개, 꼭지는 검은 수지 손잡이(꼭지 재질은 미확인)"'),
('ref="미확인",\n  en=dict(name="a pair of pot-lid cymbals"', 'ref="https://sayhikorean.com/?p=12522 (양은=노란 알루미늄, 검색 요약). 뚜껑 지름은 미확인",\n  en=dict(name="a pair of pot-lid cymbals"'),
('size="펼치면 약 60cm, 지름 6cm 원으로 동그랗게 감김, 굵기 0.26mm"', 'size="펼치면 약 60cm, 지름 6cm 원으로 동그랗게 감김, 굵기 0.026cm(0.26mm)"'),
('ref="미확인",\n  en=dict(name="a new violin E string', 'ref="https://collection.tamuseum.org.nz/objects/19117/paper-pocket-for-violin-string (예비 줄 포장, 검색 요약)",\n  en=dict(name="a new violin E string'),
('ref="형태 참고만(카테우라 실물: research/notes.md https://commons.wikimedia.org/wiki/File:Instruments_made_from_recycled_metal_(14350937984).jpg). 깡통을 눕히는 방향·숟가락 머리 줄감개·꼬리 철사는 디자인 판단(미확인)"',
 'ref="형태 참고만: https://en.wikipedia.org/wiki/Recycled_Orchestra_of_Cateura (깡통·숟가락·포크), https://commons.wikimedia.org/wiki/File:Instruments_made_from_recycled_metal_(14350937984).jpg. 한국 분유통 치수·깡통 방향·숟가락 머리 줄감개·꼬리 철사는 디자인 판단(미확인)"'),
('ref="형태 참고만(카테우라 트럼펫=빗물관: research/notes.md https://www.thomannmusic.com/blog/inspire/landfill-melodies). 배수관 재질·S자 형태·테이프는 디자인 판단(미확인)"',
 'ref="형태 참고만: https://en.wikipedia.org/wiki/Recycled_Orchestra_of_Cateura (배수관 금관), https://www.thomannmusic.com/blog/inspire/landfill-melodies. 한국 배수관 재질·S자 형태·테이프는 디자인 판단(미확인)"'),
]
for x, y in rep:
    assert x in a, x[:70]
    a = a.replace(x, y)
open('data_a.py', 'w', encoding='utf-8').write(a)

r = open('research.py', encoding='utf-8').read()
if 'research_r1' not in r:
    r += "\nfrom research_r1 import R1, A1\nfor _k, _v in R1.items():\n    RES.setdefault(_k, []).extend(_v)\nANACHRONISM += A1\n"
    open('research.py', 'w', encoding='utf-8').write(r)
print("patched")
