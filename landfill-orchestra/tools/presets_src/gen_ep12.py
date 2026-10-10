# -*- coding: utf-8 -*-
"""깡통 바이올린 1화 S#1~17, 2화 S#1~29 씬 프리셋 생성 -> design/_presets_ep12.json"""
import json, re, sys, io
from pathlib import Path

ROOT = __import__("pathlib").Path(__file__).resolve().parents[2]
OUT = ROOT / "design" / "_presets_ep12.json"

# ---------- 원문에서 뽑기 ----------
script = (ROOT / "story" / "script.md").read_text(encoding="utf-8")
ep_heads = {}
ep = None
for line in script.splitlines():
    if line.startswith("## 1화"): ep = 1
    elif line.startswith("## 2화"): ep = 2
    elif line.startswith("## 3화") or line.startswith("## 변경"): ep = None
    m = re.match(r"^S#(\d+)\. (.+) \((.+)\)$", line)
    if m and ep:
        ep_heads[f"{ep}-{m.group(1)}"] = (m.group(2), m.group(3))

guide = (ROOT / "design" / "style_guide.md").read_text(encoding="utf-8")
sec8 = guide.split("## 8.")[1]
LOC = {}
for line in sec8.splitlines():
    m = re.match(r"^\| (.+?) \| (.+?) \|$", line)
    if m and m.group(1) not in ("장소", "---"):
        LOC[m.group(1)] = m.group(2)

P = LOC["갈대섬 전경"]
SH = LOC["작은 산 (중턱·꼭대기)"]
BH = LOC["큰 산 아래 쇳더미"]
RD = LOC["둑길·섬 어귀"]
NB = LOC["섬 어귀 게시판"]
KIT = LOC["은주네 판잣집, 부엌 겸 방"]
ROOM = LOC["은주네 판잣집, 쪽방"]
KWAK = LOC["곽 영감 고물상 (안·앞)"]
WS = LOC["공방"]
TENT = LOC["국밥집 천막 (안·앞·뒤)"]
CH = LOC["강변교회 지하 공부방"]
PAWN = LOC["만복전당포"]
MKT = LOC["시장 골목"]
BUS = LOC["시내버스 안"]
HB = LOC["한빛문화회관 (앞·로비·복도·무대 옆·홀)"]
AUD = LOC["학교 강당"]

# 8절에 없는 장소: 새로 쓴 기준 문장 (보고 대상)
NEW = {k: LOC[k] for k in ("판잣집 동네 외경", "한빛문화회관 연습실", "뭍의 골목")}
NEW["국밥집 천막 뒤 쓰레기 더미"] = re.sub(r"^\(.*?\)\s*", "", LOC["국밥집 천막 뒤 쓰레기 더미"])
VIL = NEW["판잣집 동네 외경"]
PRAC = NEW["한빛문화회관 연습실"]
ALLEY = NEW["뭍의 골목"]
PILE = NEW["국밥집 천막 뒤 쓰레기 더미"]

def sc(loc, rest, key, shadow):
    return f"{loc}, {rest}, key color {key}, cel shadows {shadow}"

# 의상 라벨(characters.json outfits 그대로)
E1 = "큰 남색 점퍼·해진 바지·목장갑"
E2 = "흰 블라우스·감색 치마(학교)"
D1 = "물려받은 큰 운동복"
M1 = "낡은 야전상의·목수건·고무장화"
K1 = "톱밥 묻은 캔버스 앞치마·팔토시"
S1 = "구겨진 흰 셔츠·카디건·긴 플레어스커트"
C1 = "회색 양복·넥타이·서류 봉투"
T1 = "사립학교 교복(감색 재킷·넥타이)"
MJ = "빨간 트레이닝 상의"
DS = "늘어난 흰 러닝셔츠 위 체크 남방"
SR = "몸뻬 바지·꽃무늬 앞치마"

def ch(i, o, n=""):
    return {"id": i, "outfit": o, "note": n}

NECK = "소리굽쇠 목걸이 착용"
EXTRA = "보조 인물(characters.json 없음)"
CROWD_OUT = "어둡고 두꺼운 작업복, 머릿수건, 빨강·파랑 웃옷이 드문드문(research/notes 시각 고증 [A]14·18쪽 기준)"

S = []
def add(scene, date, sw, light, key, shadow, palette, chars, props, sound, mood, prompt, cont):
    loc, time = ep_heads[scene]
    S.append({"scene": scene, "location": loc, "time": time, "date": date,
              "season_weather": sw, "light": light, "key_hex": key, "shadow_hex": shadow,
              "palette": palette, "characters": chars, "props": props,
              "sound_color": sound, "mood": mood, "prompt_scene": prompt, "continuity": cont})

# ================= 1화 =================
add("1-1", "1987년 4월 초순(추정)", "봄, 안개, 쌀쌀함(고무장화 속 발가락이 시림)",
    "해 뜨기 전 회청색 확산광, 그림자 거의 없음. 끝 컷에서 화면 왼쪽(동쪽) 큰 산 너머로 첫 햇빛이 비침",
    "#5E7F99", "#34465E", ["#8FA3B5", "#C99A62", "#E3DED2", "#F2C98A"],
    [ch("eunju", E1, NECK + "(옷 속), 고무장화, 빈 자루. 듣는 때 고개 왼쪽으로"), ch("dongmin", D1, "빈 자루를 끌어안고 졺, 고무장화"),
     ch("extra:갈고리 아주머니", CROWD_OUT, EXTRA + ", 갈고리"), ch("extra:섬사람들", CROWD_OUT, EXTRA + ", 비탈 곳곳에 자루")],
    ["빈 자루", "갈고리", "비누 공장 트럭(문짝 흰 페인트 가공 공장명)", "철공소 트럭(큰 산 아래에서 짐칸 기울임)"],
    ["엔진 '쿨럭' #9DB7C9 — 은주 왼쪽 귀로 다가가는 컷(바람 빠지고 엔진만)", "쏟아지는 쇳소리가 낱낱으로 쪼개짐(깡·칭·짤랑·퉁·쨍) #9DB7C9 — 은주 옆얼굴 컷"],
    "신비·고요",
    sc(SH, "1987 early April, before dawn, thick fog, the big flat-topped hill and the embankment road below half-hidden in mist, cool blue-gray diffuse light with almost no shadows, at the end the first sunlight breaking over the big hill from the left (east)", "#5E7F99", "#34465E"),
    "작품 첫 씬. 동그리 아직 없음. 아이들은 반드시 목장갑·고무장화. 트럭 문짝 글씨는 이미지에 넣지 않음(no text)")

add("1-2", "1987년 4월 초순(추정), 1-1과 같은 날", "봄, 맑으나 먼지 낀 뿌연 베이지 하늘",
    "아침 낮은 해, 화면 왼쪽(동쪽)에서 비스듬히. 쇳더미에 짧은 금속 반사",
    "#C9A66B", "#6E5640", ["#E3D3B4", "#8C7A66", "#C0392F", "#B87333"],
    [ch("eunju", E1, NECK + "(옷 속), 허리춤에 짧은 쇠막대, 자루"), ch("dongmin", D1, "누나 등 뒤에서 혀를 내밂"),
     ch("mija", MJ, "목장갑, 코 반창고, 빨간 헝겊 깃발"), ch("deoksu", DS, "체크 남방 주머니에 누룽지"),
     ch("extra:미자네 패거리 아이 둘", "어두운 사복", EXTRA + ", 팔짱")],
    ["빨간 헝겊 깃발(막대)", "노란 칠한 쇳덩이(철)", "진흙 묻은 구리 파이프 토막", "짧은 쇠막대", "누룽지", "반쯤 빈 자루"],
    ["'깡'(노란 칠 쇳덩이) #9DB7C9 — 주변 소리 빠지고 그 소리만", "'통'(구리) #9DB7C9 — 둥글게 퍼졌다 길게 사그라지는 동심원, 은주 왼쪽 귀 클로즈업"],
    "활기",
    sc(BH, "1987 early April, morning, clear but dusty hazy beige sky, low morning sun from the left (east), short metallic glints on the scrap heap", "#C9A66B", "#6E5640"),
    "1-1에서 바로 이어짐(철공소 차가 쏟은 더미). 미자 빨간 상의가 무채색 바탕의 원색 점. 학교 가기 전 시간")

add("1-3", "1987년 4월 초순(추정), 같은 날", "봄, 맑음, 바람(함석지붕 덜컹)",
    "오후. 고물상 안은 그늘, 열린 문(둑길 쪽)에서 들어오는 측광. 선반의 바이올린 몸통만 먼지 없이 빛을 받음",
    "#8A6A4A", "#4E3B2C", ["#D8B98A", "#9AA0A6", "#B87333", "#2E3A5C"],
    [ch("eunju", E1, NECK + "(옷 속). 책가방 멤(하교길) — 점퍼 아래 학교 옷인지 대본 근거 없음"), ch("dongmin", D1, "책가방, 병뚜껑 한 주먹"),
     ch("kwak", K1, "귀에 연필, 돋보기안경 이마에. 오른손 약지·새끼 굽음")],
    ["구리 토막", "매다는 저울", "병뚜껑", "목 부러진 바이올린 나무 몸통(앞판에 금, 줄 없음, 먼지 없음 — 동그리 아님)", "부드러운 천", "지폐 한 장·동전(실제 화폐 도안 없이)", "작업대 아래 톱밥"],
    ["나무 몸통 '똑'과 그 안의 '오오' #9DB7C9 — 은주 왼쪽 귀로, 주변 소리 빠짐"],
    "호기심",
    sc(KWAK, "1987 early April, afternoon, windy, shaded interior under the corrugated roof, side light coming through the open door from the embankment road, the one wooden violin body on the shelf catching clean light", "#8A6A4A", "#4E3B2C"),
    "곽 영감 첫 등장. 선반의 부서진 몸통은 동그리와 다른 물건. 영감 표정 변화 없음")

add("1-4", "1987년 4월 초순(추정), 같은 날", "봄, 해 진 뒤",
    "외경: 남색 박명, 판잣집 창 몇 개에 노란 불. 안: 백열전구 하나와 석유곤로 불빛, 문틈 연탄 연기",
    "#3E4A6A", "#2A2F45", ["#E3B062", "#8C5A3C", "#5B6145", "#C9A66B"],
    [ch("eunju", E1, NECK + "(옷 속), 집 안이라 목장갑 없음"), ch("dongmin", D1, "숟가락으로 밥그릇 두드림"),
     ch("manseok", M1, "야전상의에 쇳가루. 목수건을 풀어 문고리에 검")],
    ["석유곤로·냄비", "밥상·김치찌개", "목수건(문고리)", "공구 자루", "리어카(소리만)"],
    ["문밖 긴 한숨 '후우―' #9DB7C9 — 은주 왼쪽 귀로, 찌개 소리 빠짐"],
    "쓸쓸함",
    sc(KIT, "1987 early April, evening after sunset, inside lit by a single bare bulb and the kerosene burner flame, thin coal-briquette smoke seeping through the door gap, navy dusk outside the tiny window; establishing exterior: " + VIL + ", navy twilight with a few yellow-lit windows", "#3E4A6A", "#2A2F45"),
    "만석 첫 등장. 판잣집은 두 칸(부엌 겸 방 / 합판 벽 너머 쪽방) — 두 칸을 한 화면에 두는 컷 있음")

add("1-5", "1987년 4월 초순(추정), 같은 날", "봄, 밤",
    "쪽방 백열전구 하나(위에서), 소리굽쇠에 반짝임. 불 끈 뒤 거의 어둠, 남색",
    "#24304F", "#1E2740", ["#F0C878", "#E9EEF5", "#B9A7D9", "#5A4A3E"],
    [ch("eunju", E1, NECK + " — 꺼내서 무릎에 쳐 귀에 댐. 이불 위, 점퍼 대신 실내복일 수 있음(근거 없음)"), ch("dongmin", D1, "이불을 둘둘 만 채"),
],
    ["엄마의 트랜지스터라디오(모서리 칠 벗겨짐, 손잡이 가죽 갈라짐)", "은색 소리굽쇠 목걸이", "동전(나사 풀기)", "이불", "합판 벽"],
    ["소리굽쇠 '웅―' #E9EEF5 — 주변 소리 모두 빠짐, 은주 눈 감음", "라디오 허밍 '음―' #B9A7D9 — 지지직 사이 아주 잠깐, 은주 숨 멈춘 정면 고정 컷"],
    "쓸쓸함",
    sc(ROOM, "1987 early April, night, a single bare bulb overhead giving a small warm pool of light, the silver tuning fork glinting, after the light is switched off almost total darkness tinted deep navy", "#24304F", "#1E2740"),
    "(E) 목소리: 만석(벽 너머 '자라'), 화면에 안 나옴. 엄마는 얼굴·모습 없음(내레이션·라디오·소리굽쇠로만). 벽 '톡톡' 복선(두 번). 동민은 처음 세 번 쳤다가 다시 두 번")

add("1-6", "1987년 4월 11일 토요일(추정)", "봄, 토요일 저녁(지하라 바깥 날씨 안 보임)",
    "지하 교실, 천장 백열등 세 개가 노랗게 흔들림(대본). 흔들리는 그림자",
    "#E8C46A", "#6E5640", ["#3F5A4A", "#8A3A3A", "#F4E7C8", "#C9A66B"],
    [ch("eunju", E1, NECK + "(옷 속)"), ch("dongmin", D1, "사탕을 볼에 묾"), ch("seonyoung", S1, "구두, 동그란 금속테 안경, 빈 바이올린 케이스"),
     ch("extra:섬 아이들 몇", "어두운 사복", EXTRA)],
    ["빈 바이올린 케이스(붉은 벨벳, 바이올린 모양 자국, 송진 가루)", "악보", "알록달록 사탕", "버스 토큰", "분필(끝 쪼개짐)", "받아쓰기 공책"],
    ["케이스 닫는 '텅' #9DB7C9 — 주변 소리 빠지고 그 소리만"],
    "웃음",
    sc(CH, "1987 mid-April, Saturday evening, underground with no daylight, the swinging bulbs giving warm yellow light and moving shadows", "#E8C46A", "#6E5640"),
    "선영 첫 등장(구두 차림, 다음 씬에서 장화로 바뀜). M: 선영 콧노래는 색 없음(2절 예외)")

add("1-7", "1987년 4월 18일 토요일(추정)", "봄, 비 갠 오후, 바퀴 자국마다 흙탕물",
    "비 갠 뒤 엷은 구름 사이 오후 빛, 화면 오른쪽(서쪽)에서. 물웅덩이 반사",
    "#C9A66B", "#6E5640", ["#DCD6C8", "#7A6A55", "#F2EFE8", "#B5546A"],
    [ch("seonyoung", S1, "흰 셔츠·긴 치마(대본), 구두 한 짝 진흙에 박힘, 빈 케이스를 가슴에"), ch("eunju", E1, NECK + "(옷 속), 둑 위에 앉음"),
     ch("dongmin", D1, "둑 위"), ch("deoksu", DS, "누룽지"), ch("sunrye", SR, "천막에서 나옴, 검정 고무장화를 내려놓음")],
    ["빈 바이올린 케이스", "선영 구두(진흙)", "검정 고무장화(큰 치수) — 이후 선영 고정 신발", "누룽지"],
    [], "코미디",
    sc(RD, "1987 mid-April, Saturday afternoon right after rain, muddy puddles in every tire rut reflecting the sky, soft afternoon light through thinning clouds from the right (west)", "#C9A66B", "#6E5640"),
    "이 씬 끝부터 선영은 순례 할머니의 검정 장화(한 치수 큼)")

add("1-8", "1987년 4월 18일 토요일(추정), 1-7 연속", "봄, 비 갠 오후",
    "천막 천을 거친 부드러운 확산광, 솥 김에 흐림. 천막 옆 고물상은 바깥 빛",
    "#C9A66B", "#6E5640", ["#D9C8A8", "#5A4A3E", "#C0392F", "#EDE6DA"],
    [ch("seonyoung", S1, "검정 고무장화(발목 헐렁), 안경"), ch("eunju", E1, NECK + "(옷 속)"), ch("dongmin", D1), ch("deoksu", DS, "맨 앞"),
     ch("mija", MJ, "천막 기둥에 기대 팔짱"), ch("sunrye", SR, "국자"), ch("kwak", K1, "고물상 작업대, 등 돌리고 사포질"),
     ch("extra:미자네 패거리 아이 둘", "어두운 사복", EXTRA)],
    ["빈 바이올린 케이스와 사탕", "국솥·국자", "평상", "사포"],
    ["사포질 '쓱, 쓱'이 끊긴 빈자리 #9DB7C9 — 은주 왼쪽 귀로, 웃음 낮아짐"],
    "코미디",
    sc(TENT, "1987 mid-April, Saturday afternoon after rain, soft diffused light through the canvas, steam from the soup pot, old Kwak's junk shop visible next to the tent in outdoor light", "#C9A66B", "#6E5640"),
    "1-7 연속. 선영 장화 착용. '은하악기' 처음 언급")

add("1-9", "1987년 4월 18일 토요일(추정), 1-8 연속", "봄, 비 갠 오후",
    "고물상 앞 오후 측광(서쪽, 화면 오른쪽), 함석지붕 아래 그늘",
    "#C9A66B", "#6E5640", ["#9AA0A6", "#8A6A4A", "#F2EFE8"],
    [ch("seonyoung", S1, "검정 고무장화"), ch("kwak", K1, "돋보기 이마에, 사포"), ch("eunju", E1, NECK + "(옷 속), 천막 쪽에서 봄")],
    ["사포", "나뭇조각", "천장 위 다락(시선만, 바이올린은 안 보임)"],
    ["느려진 사포 소리 #9DB7C9 — 은주 왼쪽 귀로"],
    "코미디",
    sc(KWAK, "1987 mid-April, Saturday afternoon after rain, side light from the right (west), deep shade under the corrugated-iron roof", "#C9A66B", "#6E5640"),
    "영감 시선이 다락으로 1초(다락의 바이올린 복선). 다락 속 물건은 그리지 않음")

add("1-10", "1987년 4월 18~21일 밤(추정)", "봄, 밤 사흘",
    "본 장면: 쪽방 어둠, 창으로 희미한 남색. 1: 고물상 함석지붕 틈으로 새는 노란 작업등. 2: 쪽방 같은 어둠. 3: 판잣집 지붕들 너머 고물상 불빛 하나",
    "#24304F", "#1E2740", ["#E8B04A", "#3A4A6B", "#5E7F99"],
    [ch("eunju", E1, NECK + "(옷 속), 이불 속에서 깸")],
    ["엄마의 라디오(머리맡)", "고물상 불빛(작업대 안쪽과 만드는 물건은 보이지 않음)"],
    ["톱질 '쓱싹'·망치 '똑' #9DB7C9 — 은주 왼쪽 귀로"],
    "호기심",
    "[main] " + sc(ROOM, "1987 late April, night, darkness tinted navy, faint blue night light from the small window", "#24304F", "#1E2740")
    + "; [1] " + KWAK + ", night, yellow work light leaking through gaps in the corrugated roof"
    + "; [2] " + ROOM + ", next night, same navy darkness"
    + "; [3] " + VIL + ", night, over the dark shack roofs a single yellow light from the junk shop",
    "몽타주 3밤. 작업대 안쪽·만드는 물건은 보여 주지 않음(1-11 공개를 위해)")

add("1-11", "1987년 4월 22일 무렵(추정, 1-9 뒤 나흘째)", "봄, 맑음, 강바람",
    "해 질 녘 역광, 화면 오른쪽(서쪽) 강 너머 낮은 해, 긴 그림자. 쓰레기 산 전체가 금빛",
    "#F2C14E", "#6E5640", ["#E8944A", "#C99A62", "#F5C04A", "#2E3A5C"],
    [ch("eunju", E1, NECK + " — 꺼내서 조율에 씀. 목장갑을 벗어 점퍼 주머니에"), ch("kwak", K1, "천으로 싼 꾸러미, 언덕을 올라옴"),
     ch("seonyoung", S1, "순례 할머니의 검정 장화, 안경"), ch("mija", MJ), ch("deoksu", DS, "누룽지(떨어뜨림)"), ch("dongmin", D1, "사탕"),
     ch("extra:미자네 패거리", "어두운 사복", EXTRA), ch("extra:비탈의 섬사람들·집하장 아저씨", CROWD_OUT, EXTRA)],
    ["동그리(처음 등장, 천에 싸여 옴: 큰 분유 깡통 몸통·상표 없음·녹슨 테두리, 나무 숟가락 목, 구부린 포크 줄받침, 진짜 바이올린 줄 4, 나무못)", "공장 시절 낡은 활", "싸 온 천", "누룽지", "사탕"],
    ["조율: 줄 소리 #F5C04A(옅게) + 소리굽쇠 '웅―' #E9EEF5 — 떨리다 하나로 포개지는 순간", "끼익 밑에 숨은 동그란 소리 하나 #F5C04A — 한 점", "동그리 첫 소리 #F5C04A — 두 번째 활부터 활을 내릴 때까지(바람·비닐·웃음·쇳소리가 한 겹씩 빠짐)"],
    "경이",
    sc(SH, "1987 late April, top of the small hill at sunset, clear with a light river wind, low golden backlight from the right (west) over the river, long shadows, the whole trash hill glowing gold", "#F2C14E", "#6E5640"),
    "1화 정서 정점. 곽 영감 첫 웃음은 입꼬리 한쪽 1초(이 안 보임). 은주는 입꼬리만. 처음 소리 낸 자리 = 2-23에서 동그리를 두는 '납작한 판자' 자리")

add("1-12", "1987년 4월 하순(추정, 1-11 다음 날부터 며칠)", "봄, 맑음",
    "오후, 고물상 안 그늘과 열린 문의 측광. 동민이 X선 필름을 해 쪽으로 드는 역광 컷. 바깥 와이드는 뿌연 베이지 하늘",
    "#E9853A", "#6E5640", ["#B0552E", "#D8B98A", "#4FB3A9", "#C0392F"],
    [ch("kwak", K1, "쇠톱·망치"), ch("eunju", E1, NECK + "(옷 속)"), ch("deoksu", DS, "누룽지"), ch("dongmin", D1),
     ch("mija", MJ, "문간에 팔짱"), ch("sunrye", SR, "국자 들고 천막에서 튀어나옴")],
    ["뚱보(반으로 가른 기름통 몸통·각목 목, 은주 키만 함)", "뼈다귀 북(페인트 통 + X선 필름, 손뼈 비침)", "나무 숟가락 북채 2", "꽥꽥이(구부린 배수관 + 깔때기, 철사·고무 조각 덧댐)", "비눗물 대야·빨랫줄의 X선 필름", "작업대 위 나사못", "까마귀 떼(큰 산 쪽, 미확인 고증 → 가공 연출)"],
    ["뚱보 '부우웅'(두 번째, 둥글어진 소리) #E8944A — 은주 왼쪽 귀로", "꽥꽥이 이음매 왼쪽 새는 바람 '쉬이' #4FB3A9 — 은주 왼쪽 귀로, 동민 웃음 빠짐"],
    "희망",
    sc(KWAK, "1987 late April, afternoon over several days, shaded interior with side light from the open door, backlit X-ray film held up toward the sun; exterior wide: hazy beige sky over the junk-shop roof, crows rising from the big hill", "#E9853A", "#6E5640"),
    "악기 셋 탄생·이름 붙임(뚱보·뼈다귀 북·꽥꽥이). X선 필름은 씻어 말린 것. 꽥꽥이 첫 큰 소리에 까마귀")

add("1-13", "1987년 4월 말~5월 초(대본 '4월 말', 달력이 5월로 넘어감)", "봄",
    "1: 아침, 고물상 함석지붕 위로 해 뜸(화면 왼쪽 동쪽). 2: 저녁, 작은 산 꼭대기 해 질 녘 역광(오른쪽 서쪽). 3: 고물상 안 벽, 낮 그늘",
    "#E9853A", "#6E5640", ["#F2C14E", "#9AA0A6", "#C99A62"],
    [ch("eunju", E1, NECK + "(옷 속), 2번 컷 혼자 동그리")],
    ["동그리", "고물상 벽 달력(4월→5월, 글자 없이)"],
    ["2: M: 아직 서툰 동그리 #F5C04A — 얇고 끊기는 빛 띠"],
    "희망",
    "[1] " + sc(KWAK, "1987 late April, morning, the sun rising over the corrugated-iron roof from the left (east)", "#E9853A", "#6E5640")
    + "; [2] " + SH + ", evening, low sunset backlight from the right (west)"
    + "; [3] " + KWAK + ", interior wall in daytime shade, a wall calendar turning a page",
    "몽타주. 달력 숫자·글자는 이미지에 넣지 않음")

add("1-14", "1987년 5월 2일 토요일(대본 '5월 첫 토요일', 날짜는 요일 계산)", "늦봄, 맑음",
    "오후, 천막 천을 거친 확산광. 금빛 테두리 종이가 천막 그늘 속에서 반짝",
    "#E9853A", "#6E5640", ["#D9C8A8", "#E8C46A", "#C0392F", "#5D7DA8"],
    [ch("eunju", E1, NECK + "(옷 속), 동그리"), ch("deoksu", DS, "뚱보"), ch("mija", MJ, "꽥꽥이"), ch("dongmin", D1, "뼈다귀 북"),
     ch("seonyoung", S1, "검정 장화, 지휘봉을 두 손으로"), ch("kwak", K1), ch("sunrye", SR, "국자"), ch("extra:국밥 먹는 아저씨들", CROWD_OUT, EXTRA)],
    ["악기 넷(동그리·뚱보·꽥꽥이·뼈다귀 북)", "지휘봉(숟가락 자루를 매끈하게 깎은 막대)", "전국 청소년 합주제 공고(금빛 테두리 종이)", "국솥"],
    [], "희망",
    sc(TENT, "1987 early May, Saturday afternoon, clear, soft diffused light through the canvas, a gold-bordered paper glinting in the tent's shade", "#E9853A", "#6E5640"),
    "첫 합주는 엉망 — 동그리 소리를 은주 귀가 못 찾음, 그래서 소리 색 넣지 않음. 지휘봉 첫 등장")

add("1-15", "1987년 5월 2일 토요일(계산), 1-14 같은 날", "늦봄, 맑음",
    "저녁, 해 질 무렵 낮은 빛이 화면 오른쪽(서쪽)에서, 금빛 테두리 종이에 반사",
    "#D8A657", "#5A4636", ["#E8C46A", "#8C7A66", "#C9A66B"],
    [ch("seonyoung", S1, "검정 장화"), ch("dongmin", D1, "압정 통")],
    ["금빛 테두리 공고", "압정 4개", "나무 게시판"],
    [], "기대와 불안",
    sc(NB, "1987 early May, evening, low warm sunset light from the right (west) glinting on a gold-bordered paper", "#D8A657", "#5A4636"),
    "게시판에 공고 한 장(금빛)만. 다음 씬에서 회색 갱지가 옆에 붙음")

add("1-16", "1987-05-03(일, 추정)", "늦봄, 선선한 아침, 갈대에 이슬",
    "이른 아침 낮은 해 화면 왼쪽(동쪽), 차갑고 맑은 빛, 이슬 반짝임",
    "#8C8F94", "#4A5060", ["#7A7C80", "#C9B98A", "#E6E3DA", "#A9B4A0"],
    [ch("choi", C1, "얼굴 화면에 넣지 않음 — 소매·손·반들반들한 구두·누런 서류 봉투·손수건만")],
    ["누런 서류 봉투", "회색 갱지 공문(빨간 도장)", "압정(진흙에 떨어졌다 닦임)", "손수건"],
    [], "기대와 불안",
    sc(RD + "; " + NB, "1987 early May, cool early morning, dew on the reeds, low clear sunlight from the left (east)", "#8C8F94", "#4A5060"),
    "최 계장 첫 등장, 얼굴 없음(이 씬 끝까지). 금빛 공고 바로 옆에 회색 공문. 이튿날이 일요일 — 구청이 일요일 아침에 붙인 셈. 문제되면 1-14를 금요일로")

add("1-17", "1987년 5월 3일(계산), 1-16 조금 뒤", "늦봄, 아침, 강바람",
    "아침 빛 화면 왼쪽(동쪽), 둑길 바퀴 자국 그늘. 두 종이가 같은 빛에 함께 떨림",
    "#8C8F94", "#4A5060", ["#E8C46A", "#B23A30", "#CFCBC2", "#2E3A5C"],
    [ch("eunju", E1, NECK + "(옷 속), 빈손인데 손가락이 활 쥐는 모양")],
    ["금빛 테두리 공고(왼쪽)", "회색 갱지 공문·빨간 도장(오른쪽)", "Insert: 작은 산 비탈에서 고물 고르는 목장갑 손"],
    ["사락(금빛 공고)과 바스락(회색 공문) 둘 다 #9DB7C9, 같은 세기로 번갈아·겹쳐서 — 어느 쪽도 키우지 않음"],
    "기대와 불안",
    sc(NB, "1987 early May, morning, river wind, the embankment road with tire ruts from the dawn trucks and the junk shop's corrugated roof ahead, morning light from the left (east)", "#8C8F94", "#4A5060")
    + "; insert: " + SH + ", daylight",
    "1화 끝 훅. 공문 글자는 Insert에서 식자로(이미지 no text). 은주 기운 고개가 돌아오지 않음")

# ================= 2화 =================
add("2-1", "1987년 9월~10월 주말들", "가을, 9월은 아직 따뜻, 10월은 서늘한 강바람·파리 떼 줄어듦",
    "본 장면·3·4·6·7·9: 천막 천 확산광, 오후. 1: 토요일 아침 둑길, 왼쪽(동쪽) 낮은 해. 2: 뭍 골목, 해가 아직 높은 낮. 5: 섬 어귀 오후. 8: 10월 오후, 서늘하고 맑은 빛. 10·11: 쓰레기 산 낮",
    "#D9822B", "#6E5640", ["#C9A66B", "#B5546A", "#3F7A55", "#E8C46A"],
    [ch("dongmin", D1, "뼈다귀 북·북채"), ch("seonyoung", S1, "검정 장화(한 치수 큼), 지휘봉, 빈 케이스"), ch("eunju", E1, NECK + "(옷 속), 동그리, 왼손 손끝 굳은살"),
     ch("mija", MJ, "꽥꽥이"), ch("deoksu", DS, "뚱보, 누룽지"), ch("manseok", M1, "2번 컷 리어카"), ch("kwak", K1, "5번 피아노"), ch("sunrye", SR, "국자·행주"),
     ch("extra:섬 아저씨들", CROWD_OUT, EXTRA)],
    ["뼈다귀 북", "지휘봉", "뚱보(줄 끊김 — 줄은 덕수 반대쪽으로 튐)", "부서진 피아노와 굵은 쇠줄", "리어카", "국솥(지휘봉 퐁당)", "천막 기둥 달력(9월, 글자 없이)", "쇠막대·깡통"],
    ["은주 귀로: 꽥꽥이 소리 밑에 깔린 가는 동그리 소리 #F5C04A — 꽥꽥이 #4FB3A9는 채도 낮춰 위에 덮이게"],
    "코미디",
    "[main] " + sc(TENT, "1987 autumn weekends, afternoon, soft light through the canvas", "#D9822B", "#6E5640")
    + "; [1] " + RD + ", Saturday morning, low sun from the left (east)"
    + "; [2] " + ALLEY + ", early afternoon with the sun still high"
    + "; [5] " + RD + ", afternoon"
    + "; [8] " + P + ", October afternoon, cool clear light, river wind lifting the tent flaps"
    + "; [10][11] " + SH + ", daytime",
    "몽타주(9~10월). 데포르메 허용(코미디 몽타주). 줄은 사람을 맞히지 않음. 덕수 넘어지는 컷 2회 같은 구도")

add("2-2", "1987년 10월 10일 토요일(대본 '10월 둘째 토요일', 날짜는 요일 계산)", "가을, 바람",
    "늦은 오후, 천막 기둥에 매단 전구 하나가 흔들리며 따뜻한 빛, 천막 밖 남은 낮빛",
    "#E0A050", "#6E5640", ["#F0C878", "#C0392F", "#5D7DA8", "#3F7A55"],
    [ch("eunju", E1, NECK + "(옷 속), 동그리"), ch("dongmin", D1, "뼈다귀 북"), ch("deoksu", DS, "뚱보"), ch("mija", MJ, "꽥꽥이"), ch("seonyoung", S1, "검정 장화, 지휘봉, 안경을 벗었다 씀")],
    ["악기 넷", "지휘봉", "흔들리는 전구"],
    [], "희망",
    sc(TENT, "1987 mid-October, late afternoon, windy, a single bare bulb hanging from the tent pole swaying and giving warm light, remaining daylight outside the tent", "#E0A050", "#6E5640"),
    "처음으로 네 소리가 한 점에 모임. 소리 색 규칙 근거(귀로·M:) 없어 비움 — 판단 메모 참고")

add("2-3", "1987년 10월 말", "가을, 맑음",
    "한낮, 버스 창으로 들어오는 밝은 측광, 흔들리는 창틀 그림자",
    "#A8B3BF", "#4A5A70", ["#E2DCCD", "#5B6E5A", "#C0392F", "#2E3A5C"],
    [ch("seonyoung", S1, "토큰을 셈, 무릎에 안내문"), ch("eunju", E1, NECK + "(옷 속)"), ch("dongmin", D1), ch("deoksu", DS), ch("mija", MJ, "승객을 노려봄"),
     ch("extra:승객들", "1980년대 사복", EXTRA)],
    ["버스 토큰", "안내문(글자는 식자)", "고물 자루에 싼 악기 넷"],
    [], "모욕",
    sc(BUS, "1987 late October, midday, clear, bright side light through the bus windows, swaying window-frame shadows", "#A8B3BF", "#4A5A70"),
    "섬 밖으로 첫 외출. 악기는 자루에 싸여 안 보임")

add("2-4", "1987년 10월 말, 2-3 이어서", "가을, 맑음, 실내는 따뜻(재킷 벗은 아이들)",
    "흰 형광등(윙―)의 평평한 빛 + 창으로 드는 햇볕 띠",
    "#3A5A8C", "#2C3A55", ["#E8EEF2", "#B08A5A", "#1F2A4A", "#F2C14E"],
    [ch("eunju", E1, NECK + " — 꺼내 조율 후 도로 옷 속에"), ch("dongmin", D1, "점퍼 자락을 당김"), ch("deoksu", DS), ch("mija", MJ), ch("seonyoung", S1, "검정 장화일지 구두일지 근거 없음, 안경 흘러내림"),
     ch("taejun", T1, "고급 바이올린 케이스, 헝겊으로 송진 닦음. 이름은 끝에야 불림"), ch("extra:다솜중 단원·다른 학교 아이들·진행 간사", "교복(감색 재킷 등)", EXTRA)],
    ["동그리·뚱보·꽥꽥이·뼈다귀 북(자루에서 꺼냄)", "태준 바이올린과 고급 케이스", "헝겊", "소리굽쇠", "올림픽 포스터(표어만, 마스코트·엠블럼 없음, 글자는 식자)", "안내문 부채질"],
    ["M: 비발디 '여름' 3악장 #5B8DEF — 은주 귀로, 한 덩어리 합주가 줄 하나하나의 빛 띠로 갈라짐", "소리굽쇠 '웅―' #E9EEF5 — 조율", "동그리 두 줄 울림 #F5C04A — 태준 쪽에서, 웃음 가라앉고 두 줄 울림만", "태준의 라 '팅' #5B8DEF — 은주 귀로, 소리굽쇠 '웅―' #E9EEF5 잔향과 겹쳐 아주 가늘게 어긋나 일렁임"],
    "모욕",
    sc(PRAC, "1987 late October, daytime, flat white fluorescent light humming overhead plus a band of sunlight through the tall windows, warm indoors", "#3A5A8C", "#2C3A55"),
    "태준 첫 등장(교복). 은주→태준 반말. 섬 악기 엉망 연주 때 동그리 자리만 소리가 빔(색 없음). 형광등 차가운 청")

add("2-5", "1987년 11월 초", "늦가을, 맑음, 둑길 진흙",
    "오후, 차가운 맑은 빛 화면 오른쪽(서쪽)",
    "#8C8F94", "#4A5060", ["#7A7C80", "#C9B98A", "#B8AE9A", "#D5D2C8"],
    [ch("choi", C1, "두꺼운 뿔테, 얼굴 처음 보임. 누런 서류 봉투")],
    ["누런 서류 봉투('갈대섬 가구 조사표' 종이 삐져나옴, 글자는 식자)", "진흙 묻은 구두"],
    [], "여운",
    sc(RD, "1987 early November, afternoon, hazy beige sky, cold, crisp light from the right (west), sticky mud on the road", "#8C8F94", "#4A5060"),
    "(E) 목소리: 과장(화면에 안 나옴). 최 계장 얼굴 첫 노출(1-16은 손·소매만)")

add("2-6", "1987년 11월 초, 2-5 이어서", "늦가을, 맑음, 구름 한 점 없음",
    "오후 맑은 빛 화면 오른쪽(서쪽). 회색 톤 속에 함석지붕 위 맑은 하늘 한 줄",
    "#8C8F94", "#4A5060", ["#A9C3D9", "#F2E2B0", "#7A7C80", "#E8944A"],
    [ch("choi", C1, "손수건, 땀 한 줄기"), ch("deoksu", DS, "Insert: 천막 안, 눈 감고 뚱보")],
    ["손수건", "진흙 위 고인 물(잔물결)", "뚱보"],
    ["뚱보 '부우우우웅―' #E8944A — 진흙 물웅덩이 잔물결에서 구두·발목·무릎으로, 바람 소리 빠짐"],
    "여운",
    sc(TENT, "1987 early November, afternoon, outside the front of the tent, clear cloudless cold sky, light from the right (west), the junk shop's corrugated roof next door under clean blue sky", "#8C8F94", "#4A5060"),
    "(E) 목소리: 선영(천막 안). 덕수 첼로에 최 계장이 멈춤(3화 보고서 복선). 최 계장은 천막 안을 보지 못함")

add("2-7", "1987년 11월 초, 2-6 이어서", "늦가을, 맑음",
    "오후 기우는 빛 화면 오른쪽(서쪽), 둑길 위 긴 그림자",
    "#8C8F94", "#4A5060", ["#7A7C80", "#A9B4A0", "#C9B98A"],
    [ch("choi", C1, "수첩·볼펜, 손수건(말라 있음)")],
    ["수첩('특이 사항 없음', 글자는 식자)", "볼펜", "손수건"],
    [], "여운",
    sc(RD, "1987 early November, late afternoon, hazy beige sky, cold, slanting light from the right (west), long shadow on the embankment road", "#8C8F94", "#4A5060"),
    "보고에 '특이 사항 없음'. 손수건이 말라 있음(땀이 안 남)")

add("2-8", "1987년 11월 중순", "늦가을, 서리 내린 아침",
    "바깥: 서리 낀 아침 차가운 빛. 안: 누렇게 깜빡이는 형광등(치익)",
    "#B9A86A", "#5E5238", ["#D8CC8A", "#E8E6E1", "#8A3A3A", "#5B6145"],
    [ch("seonyoung", S1, "빈 케이스, 전당표·지폐. 서리 아침 — G7 의상 추가 필요: 겉옷(외투) 제안(대본 근거 없음)"),
     ch("manseok", M1, "고무장화(진흙 말라붙음)부터 위로, 얼굴은 마지막. 안주머니에 바랜 전당표"),
     ch("extra:전당포 주인", "어두운 조끼·돋보기(근거 없음, 제안)", EXTRA + ", 주판")],
    ["만복전당포 간판('복' 자 반쯤 떨어져 매달림, 글자는 식자)", "문 위의 종", "빈 바이올린 케이스(붉은 벨벳·악보·사탕 봉지)", "선영 전당표", "만석 전당표(접힌 자리 하얗게 닳음, 물건 이름 칸 지워짐)", "도장", "주판", "실제 화폐 도안 없는 지폐"],
    [], "씁쓸함",
    sc(PAWN, "1987 mid-November, frosty morning, inside a yellowed flickering fluorescent light, cold pale morning light at the door; exterior: " + MKT + ", white frost at the end of the alley", "#B9A86A", "#5E5238"),
    "같은 전당포 복선. 두 사람은 서로 모름. 빈 케이스 '텅' — 소리 색 근거 없음")

add("2-9", "1987년 11월 중순, 2-8 이어서", "늦가을, 서리 낀 아침",
    "아침 차가운 빛, 골목 그늘에 서리, 입김",
    "#B9A86A", "#5E5238", ["#E8E6E1", "#8AA0B0", "#5B6145", "#F2EFE8"],
    [ch("seonyoung", S1, "케이스를 안고, 부딪힌 팔을 만짐. G7 의상 추가 필요: 겉옷 제안(근거 없음)"), ch("manseok", M1, "리어카")],
    ["전파사 진열대 라디오", "리어카(왼쪽 바퀴 반 박자 늦음)"],
    ["M: 전파사 라디오 노래의 관악기 #9C4A6B(만석의 클라리넷 색) — 라디오 스피커 극접사에서 뻗어 나오고, 만석이 멀어질수록 작아짐"],
    "씁쓸함",
    sc(MKT, "1987 mid-November, frosty morning, cold low light, white frost in the shaded corners of the alley", "#B9A86A", "#5E5238"),
    "선영은 만석의 긴 손가락을 기억. 만석은 관악기 소리를 피함(극장 악단 클라리넷 복선)")

add("2-10", "1987년 11월 25일 수요일(추정, '11월 말' + 대본 '수요일')", "늦가을, 비",
    "회색 한낮, 빗줄기, 젖은 천막 천을 거친 탁한 확산광. 그림자 약함",
    "#4A4F57", "#2E3850", ["#8C939C", "#D9C8A8", "#5B6145", "#F5C04A"],
    [ch("eunju", E1, NECK + "(옷 속), 큰 남색 점퍼(대본 명시), 동그리"), ch("deoksu", DS, "뚱보"), ch("dongmin", D1, "뼈다귀 북, 북채를 등 뒤로 감춤, 울음"), ch("mija", MJ, "꽥꽥이를 무릎에"),
     ch("manseok", M1, "비에 젖음, 목수건 끝 빗물"), ch("sunrye", SR, "국자, 아무 말 없음")],
    ["동그리(던져짐 — 물건만, 사람 쪽 아님)", "지휘봉(평상 위, 선영 자리 빔)", "리어카", "천막 뒤 쓰레기 더미"],
    ["M: 동그리 「도라지 타령」 #F5C04A — 빗소리 위, 바퀴 소리가 멎을 때 끊김", "멀리 리어카 바퀴 '끼익, 덜컹' #9DB7C9 — 은주 왼쪽 귀로", "포크 줄받침 꺾이는 '딱' #F5C04A — 동그리 금빛이 꺼져 가는 작은 한 점, 은주 왼쪽 귀 극접사, 빗소리 빠짐"],
    "상처",
    sc(TENT, "1987 late November, rainy gray midday, dull diffused light through the wet sagging canvas, heavy rain streaks; " + PILE + " in the rain, nobody near it", "#4A4F57", "#2E3850"),
    "던지는 컷: 팔이 다 올라가기 전에 은주 얼굴로 CUT, 던지는 손 안 보임(7절). 이후 동그리 행방: 천막 뒤 더미 → 2-12 수색 → 2-13 수리")

add("2-11", "1987년 11월 25일(추정), 2-10 같은 날 밤", "늦가을, 비 그친 밤",
    "쪽방 어둠, 작은 창 밖 멀리 손전등 불빛 둘(하나는 움직이고 하나는 멈춤)",
    "#2E3550", "#1E2538", ["#E8D27A", "#4A4F57", "#3A4A6B"],
    [ch("eunju", E1, NECK + "(옷 속), 이불 속")],
    ["나무 상자(머리맡 선반, 안에 엄마 라디오)", "창밖 손전등 불빛 둘"],
    ["멀리 헤집는 소리·깡통 짤그랑 #9DB7C9 — 은주 왼쪽 귀로"],
    "상처",
    sc(ROOM, "1987 late November, night after the rain, darkness tinted navy, through the small window two distant flashlight beams over the trash pile, one moving and one still", "#2E3550", "#1E2538"),
    "(E) 목소리·소리: 동민 훌쩍임·톡톡(벽 너머), 만석 뒤척임, 미자·덕수(멀리) — 모두 화면에 안 나옴. 벽 '톡톡' 두 번 → 동민도 두 번(정상). 은주는 일어나지 않음")

add("2-12", "1987년 11월 25일(추정), 2-11 같은 시각", "늦가을, 비 그친 밤, 젖은 더미",
    "어둠, 손전등 불빛 둘(덕수 것은 움직이고 어른 것은 아이들 발치를 꼼짝 않고 비춤)",
    "#2E3550", "#1E2538", ["#E8D27A", "#4A4F57", "#C0392F", "#5D7DA8"],
    [ch("mija", MJ, "고무장화·목장갑, 막대기"), ch("deoksu", DS, "고무장화·목장갑, 손전등"),
     ch("kwak", K1, "얼굴 화면 밖 — 고무장화와 손전등 쥔 손만. 화면상 정체 숨김(2-13 진흙 장화로 암시)")],
    ["손전등 둘", "막대기", "젖은 비닐·깡통 더미"],
    [], "상처",
    sc(TENT, "1987 late November, night after rain, " + PILE + ", darkness lit only by two flashlight beams, distant river sound", "#2E3550", "#1E2538"),
    "어른은 장화·손만. 아이들 목장갑·장화 필수(위험 폐기물 맨손 금지)")

add("2-13", "1987년 11월 26일(추정), 이튿날 오후", "늦가을, 갬",
    "오후, 고물상 안 그늘, 문간 측광. 작업대 위 닦인 동그리에 반짝임",
    "#B08A5E", "#4E3B2C", ["#D8B98A", "#F5C04A", "#7A6A55", "#C0392F"],
    [ch("mija", MJ, "장화·목장갑 진흙투성이, 고물 자루에 기대 졺"), ch("deoksu", DS, "같은 진흙, 졺"), ch("eunju", E1, NECK + "(옷 속), 문간"), ch("kwak", K1, "장화에 진흙 말라붙음")],
    ["동그리(진흙 닦임, 줄받침 자리에 새 포크, 전보다 조금 더 반짝)", "싼 천", "고물 자루", "판자로 막은 작은 공방(뒤쪽)"],
    [], "온기",
    sc(KWAK, "1987 late November, afternoon after the rain, shaded interior with side light from the doorway, a cleaned tin-can violin catching a soft gleam on the workbench", "#B08A5E", "#4E3B2C"),
    "동그리 수리 완료(포크만 갈았음). 이제부터 공방에서만 연습 — 아버지는 동그리가 없어진 줄 앎")

add("2-14", "1987년 늦가을~초겨울(대본)", "늦가을에서 초겨울로, 쌀쌀함",
    "1·2: 공방 판자 틈 빛, 실내 그늘. 3: 해 질 녘 둑길, 오른쪽(서쪽) 낮은 해. 4: 판잣집 실내 백열전구. 5: 천막 뒤, 흐린 낮",
    "#9A8E7E", "#4E4438", ["#D8B98A", "#E3B062", "#5B6145", "#F5C04A"],
    [ch("eunju", E1, NECK + "(옷 속). G7 의상 추가 필요: 초겨울 겉옷(목도리 등) 제안, 근거 없음"), ch("seonyoung", S1, "지휘봉. 초겨울 겉옷 제안(근거 없음)"), ch("dongmin", D1, "입을 꾹 다묾"),
     ch("manseok", M1, "리어카"), ch("deoksu", DS), ch("mija", MJ)],
    ["동그리(공방 선반, 천을 덮고 누움)", "지휘봉", "리어카"],
    [], "온기",
    "[1][2] " + sc(WS, "1987 late autumn into early winter, daylight through gaps in the plank walls, shaded interior", "#9A8E7E", "#4E4438")
    + "; [3] " + RD + ", sunset, low light from the right (west); " + VIL
    + "; [4] " + KIT + ", evening, a single bare bulb"
    + "; [5] " + TENT + ", " + PILE + ", overcast daytime",
    "몽타주. 공방 첫 등장. 은주는 공방에서만 활을 듦. 동민은 아빠에게 말하지 않음. 만석은 더미를 스쳐 보지만 묻지 않음")

add("2-15", "1988년 1월", "한겨울, 추위, 입김",
    "Insert(게시판): 흐린 겨울 낮. 천막 안: 저녁, 연탄난로 불빛과 천막 전구, 입김이 하얗게",
    "#A9B1B6", "#3E4E66", ["#E06A3A", "#F2EFE8", "#7A7C80", "#C0392F"],
    [ch("choi", C1, "G7 의상 추가 필요: 두꺼운 외투(대본·소설 근거). 이마에 땀, 손수건 축축"),
     ch("eunju", E1, NECK + "(옷 속). 겨울 겉옷 제안(근거 없음)"), ch("dongmin", D1, "G7 의상 추가 필요: 겨울 겉옷 제안(근거 없음)"),
     ch("manseok", M1, "천막 입구 팔짱, 중간에 사라짐. 야전상의 그대로(겨울 내피는 제안만)"),
     ch("mija", MJ, "빨간 트레이닝 상의 소매를 꽉 쥠(대본 명시). 위에 겨울 겉옷 제안(근거 없음, 빨강 보이게)"),
     ch("deoksu", DS, "앞쪽 평상. 겨울 겉옷 제안(근거 없음)"), ch("sunrye", SR, "겨울 겉옷 제안(근거 없음)"),
     ch("extra:미자 엄마·섬 아저씨·갈고리 아주머니·섬사람들", CROWD_OUT + ", 겨울", EXTRA)],
    ["게시판 새 공문(빨간 도장 둘, 글자는 식자)", "연탄난로·주전자", "서류", "손수건"],
    [], "불안",
    sc(TENT, "1988 January, deep winter, cold evening, warm orange glow of a coal-briquette stove with a hissing kettle and a bare bulb, white breath in the air", "#A9B1B6", "#3E4E66")
    + "; insert: " + NB + ", overcast winter daylight, a new paper's corner lifting in the wind",
    "섬 정리 정식 통보 '8월 말까지'. 최 계장 눈이 덕수에게 잠깐(2-6 복선). 미자네 이사 이야기")

add("2-16", "1988년 1월, 2-15 같은 날 밤", "한겨울, 밤, 추위",
    "밤, 어둠. 천막·판잣집 쪽 먼 불빛이 낮게, 차가운 남청",
    "#5A6F88", "#263150", ["#9DB7C9", "#2E3A5C", "#C0392F"],
    [ch("mija", MJ, "겨울 겉옷 제안(근거 없음)"), ch("eunju", E1, NECK + "(옷 속)"), ch("dongmin", D1, "누나 손을 잡아당김. 겨울 겉옷 제안(근거 없음)")],
    ["굴러다니는 깡통(걷어참)"],
    [], "불안",
    sc(RD, "1988 January, winter night, cold blue darkness, faint distant lights of the tent and shacks low on the horizon", "#5A6F88", "#263150"),
    "'섬을 정리하면 우리도 정리돼?' 미자 '예선(4월)까지는 안 가'")

add("2-17", "1988년 1~3월 중(추정, 대본 '겨울')", "한겨울, 추위, 입김",
    "판자 틈으로 드는 차가운 겨울 낮빛 + 가운데 연탄 화덕의 주황 불빛",
    "#B8C6D0", "#3E4E66", ["#E06A3A", "#D8B98A", "#F5C04A", "#2E3A5C"],
    [ch("kwak", K1, "가위. 겨울 겉옷 제안(근거 없음)"), ch("eunju", E1, NECK + "(옷 속), 손가락 끝을 자른 목장갑(이 씬부터)")],
    ["연탄 화덕", "손끝 자른 목장갑", "가위", "동그리와 활"],
    ["M: 동그리 가락 #F5C04A — 판자 틈으로 새어 나가 바람 따라 강 쪽으로 흐르는 빛 띠"],
    "불안",
    sc(WS, "1988 winter, daytime, cold pale light through gaps in the plank walls, a coal-briquette brazier in the middle with warm orange glow, white breath", "#B8C6D0", "#3E4E66"),
    "은주 장갑은 이 씬부터 손끝 잘림. 공방에서만 연습")

add("2-18", "1988년 4월 셋째 주(대본)", "봄, 실내",
    "강당 무대 조명(정면 위), 무대 옆 커튼 뒤는 어둑, 객석은 높은 창의 낮빛",
    "#7A6B5A", "#3E342A", ["#F1EEE6", "#C9B48A", "#8C7E6E", "#F5C04A"],
    [ch("eunju", E2, "빛바랜 흰 블라우스·감색 치마(대본). 목에 가는 사슬만 보이고 소리굽쇠는 블라우스 안"),
     ch("deoksu", DS, "'제일 좋은 옷' — 체크 남방 단추를 목까지 잠금(대본)"), ch("dongmin", D1, "G7 의상 추가 필요: '제일 좋은 옷'(대본, 구체 없음). 침으로 까까머리 쓸어 넘김"),
     ch("mija", MJ, "G7 의상 추가 필요: '제일 좋은 옷'(대본, 구체 없음) — 빨간 상의 유지 제안. 꽥꽥이"),
     ch("seonyoung", S1, "지휘봉. 본선 검은 연주복은 3화, 예선은 기본 의상(판단)"),
     ch("taejun", T1, "객석 셋째 줄, 감색 재킷 교복(예선 객석 교복), 웃지 않음·팔짱 안 낌"),
     ch("extra:객석(교복·학부모)·사회자", "교복과 1980년대 외출복", EXTRA)],
    ["악기 넷", "지휘봉", "커튼", "객석 문(야전상의 없음)"],
    ["M: 동그리 「도라지 타령」 #F5C04A — 은주 정면, 웃음소리가 한 겹씩 빠짐, 객석이 잠시 조용"],
    "수치",
    sc(AUD, "1988 April, daytime, stage lit from the front and above, dim backstage behind the side curtain, the audience hall in daylight from the high windows", "#7A6B5A", "#3E342A"),
    "예선. 아버지 안 옴. 태준은 교복으로 객석에서 지켜봄. 은주 학교 옷, 소리굽쇠는 블라우스 안")

add("2-19", "1988년 4월 셋째 주(대본), 2-18 같은 날 저녁", "봄, 저녁",
    "저녁, 강당 무대 조명과 실내등, 창밖은 어두워짐. 은주 귀로 웃음이 갈라지는 컷: 화면 채도만 낮춤(색이 빠지는 쪽), 소리 색 없음",
    "#7A6B5A", "#3E342A", ["#E0C890", "#5A4E40", "#F1EEE6"],
    [ch("eunju", E2, "사슬만 보이고 소리굽쇠는 블라우스 안"), ch("seonyoung", S1, "펄쩍 뛰어 안경 떨어짐"), ch("mija", MJ, "주먹"), ch("dongmin", D1, "덕수 배에 매달림"), ch("deoksu", DS),
     ch("extra:사회자·객석", "-", EXTRA)],
    ["사회자 종이", "선영 안경(바닥)", "닫힌 강당 문"],
    [],
    "수치 — 화면 채도만 낮춤(색이 빠지는 쪽)",
    sc(AUD, "1988 April, evening, warm stage lights and indoor lamps, the high windows turning dark", "#7A6B5A", "#3E342A"),
    "본선 진출 발표. 문은 닫혀 있음(아버지 없음). 객석 웃음은 조롱 소리라 색 없음(2절 예외)")

add("2-20", "1988년 4월(예선 이튿날)", "봄, 아침",
    "아침, 천막 천 확산광, 국밥 김",
    "#7A6B5A", "#4E4236", ["#E8E2D2", "#EDE6DA", "#B5546A", "#C9A66B"],
    [ch("eunju", E1, NECK + "(옷 속), 평상 끝 숟가락 — 의상 근거 없음, 기본 의상(판단)"), ch("sunrye", SR, "신문을 낚아채 기사가 위로 오게 접음"),
     ch("extra:집하장 아저씨·갈고리 아주머니·섬 아저씨·섬사람들", CROWD_OUT, EXTRA)],
    ["「한강신보」 사회면(세로쓰기·국한문 혼용 지면, 구석 단신 '쓰레기 밴드', 글자는 식자)", "국그릇·숟가락", "평상"],
    ["숟가락이 국그릇에 닿는 '딸그락' #9DB7C9 — 주변 소리 빠지고 그 소리만 크게"],
    "수치",
    sc(TENT, "1988 April, morning, soft diffused light through the canvas, steam rising from bowls of rice soup", "#7A6B5A", "#4E4236"),
    "신문 단신. 할머니가 접어 평상 끝에 둔 신문 → 2-21 만석이 읽음")

add("2-21", "1988년 4월(예선 이튿날), 2-20 같은 날 점심", "봄, 낮",
    "한낮, 천막 천 확산광. 손대지 않은 국밥 김이 가늘어짐",
    "#7A6B5A", "#4E4236", ["#E8E2D2", "#EDE6DA", "#5B6145"],
    [ch("manseok", M1, "신문을 오래 읽음, 긴 손가락"), ch("sunrye", SR, "국밥 한 그릇")],
    ["접힌 신문('하모(14) 양', '깡통 바이올린' — 글자는 식자)", "국밥", "국밥값", "리어카(소리)"],
    [], "수치",
    sc(TENT, "1988 April, midday, soft diffused light through the canvas, thin steam fading from an untouched bowl of soup", "#7A6B5A", "#4E4236"),
    "만석이 딸이 계속했다는 걸 앎. 신문을 반듯이 펴 제자리에 둠")

add("2-22", "1988년 4월(예선 이튿날), 같은 날 해 질 무렵", "봄, 저녁",
    "해 질 무렵, 판자 틈으로 낮고 붉은 빛(서쪽), 영감 등은 역광 실루엣에 가까움",
    "#9C7650", "#4E3B2C", ["#D8B98A", "#C98A4B", "#F5C04A"],
    [ch("kwak", K1, "등 돌리고 사포질"), ch("eunju", E1, NECK + "(옷 속), 선반에서 동그리를 내림")],
    ["동그리(공방 선반 → 은주가 가져감)", "사포"],
    [], "절망",
    sc(WS, "1988 April, near sunset, low reddish light slanting through gaps in the plank walls from the west, the workbench almost in silhouette against the light", "#9C7650", "#4E3B2C"),
    "동그리 공방 보관 → 작은 산으로")

add("2-23", "1988년 4월(예선 이튿날), 같은 날 해 질 녘", "봄, 흐림, 저녁 바람(비닐 펄럭)",
    "해 질 녘이지만 강 너머 하늘이 흙탕물 색으로 탁하게 저묾 — 1-11 같은 금빛 없음. 확산광, 그림자 흐림",
    "#8C7A62", "#4A3F35", ["#A8916E", "#6E6250", "#C0392F", "#D8D0C0"],
    [ch("eunju", E1, NECK + "(옷 속), 고무장화"), ch("mija", MJ, "빨간 상의가 저녁 바람에 부풂")],
    ["동그리(납작한 판자 위에 눕힘, 나무못을 풀어 줄 넷이 늘어짐)", "납작한 판자(1-11 처음 소리 낸 자리)", "펄럭이는 비닐"],
    [], "절망",
    sc(SH, "1988 April, dusk, overcast, the sky beyond the river fading to a muddy brownish color with no gold at all, flat diffused light with soft weak shadows, evening wind making the plastic sheets flutter", "#8C7A62", "#4A3F35"),
    "1-11과 같은 자리·같은 구도, 색만 대비(금빛 없음). 줄 푼 뒤 침묵 3초 — 소리 색 없음. 동그리는 판자 위에 남음")

add("2-24", "1988년 4월(예선 이튿날), 같은 날 저녁", "봄, 저녁",
    "판잣집 실내 백열전구 하나, 어둑하고 무거운 톤",
    "#4A4E5E", "#2A2E3E", ["#D9A85A", "#5B6145", "#3F7A55"],
    [ch("eunju", E1, NECK + "(아직 착용, 옷 속)"), ch("dongmin", D1), ch("manseok", M1, "집 안 — 목수건은 문고리에 걸었을 수 있음(근거 없음)")],
    ["작은 밥상", "숟가락·젓가락"],
    [], "절망",
    sc(KIT, "1988 April, evening, a single dim bare bulb, heavy subdued tones", "#4A4E5E", "#2A2E3E"),
    "은주가 아버지 말투로 '밥이나 먹어'. 만석이 은주를 봄")

add("2-25", "1988년 4월(예선 이튿날), 같은 날 밤", "봄, 밤",
    "쪽방 백열전구 → 불 끈 뒤 깊은 남색 어둠",
    "#1A2238", "#232C4A", ["#F0C878", "#E9EEF5", "#5A4A3E"],
    [ch("eunju", E1, "소리굽쇠 목걸이를 빼서 라디오 상자에 넣음(이 씬부터 미착용). 사슬이 고무줄에 걸려 머리가 풀려 흘러내림(이후 풀린 머리)"),
     ch("manseok", M1, "벽 너머 어둠 속 눈 뜸")],
    ["나무 상자와 엄마의 라디오(뒤판 열지 않음)", "은색 소리굽쇠 목걸이(상자 안 라디오 옆으로, 사슬이 엉키며 쌓임)", "머리 묶던 고무줄", "합판 벽"],
    [], "절망",
    sc(ROOM, "1988 April, night, a bare bulb, then after the light is switched off deep navy darkness", "#1A2238", "#232C4A"),
    "(E) 동민 톡톡·'근데 누나'(벽 너머, 화면에 안 나옴). 소리굽쇠 → 라디오 상자(3화 S#3에서 만석이 다시 걸어 줌). 은주가 벽에 답하지 않음(톡톡 복선 끊김)")

add("2-26", "1988년 4월, 예선 이튿날 자정 지나(날짜 넘어감)", "봄, 깊은 밤",
    "거의 어둠, 창의 희미한 남색 밤빛만",
    "#1A2238", "#232C4A", ["#3A4A6B", "#5B6145"],
    [ch("manseok", M1, "손전등을 내리고 고무장화를 신음"), ch("dongmin", D1, "아빠 팔을 베고 잠, 실내복일 수 있음(근거 없음)")],
    ["손전등(문 옆 못)", "고무장화", "쪽방 문고리"],
    [], "절망",
    sc(KIT, "1988 April, past midnight, near-total darkness with only faint navy night light from the tiny window", "#1A2238", "#232C4A"),
    "만석이 쪽방 문고리에 손만 올렸다 내림")

add("2-27", "1988년 4월, 같은 밤(자정 지나)", "봄, 맑은 밤, 별 몇 개, 밤이슬",
    "손전등 원 하나가 유일한 광원(따뜻한 노랑), 나머지는 남색 어둠. 큰 산 검은 등성이 위 별",
    "#1A2238", "#232C4A", ["#F2D27A", "#3A4A6B", "#C99A62"],
    [ch("manseok", M1, "손전등. 야전상의 단추를 풀고 깡통을 품에")],
    ["동그리(판자 위, 밤이슬, 나무 숟가락 목이 젖어 거뭇, 줄 넷 늘어짐)", "손전등", "깨진 화분·찢어진 비닐·고무신 한 짝(손전등 원 안)"],
    [], "온기",
    sc(SH, "1988 April, deep night, clear with a few stars above the black ridge of the big hill, night dew, the only light a small warm flashlight circle, everything else navy darkness", "#1A2238", "#232C4A"),
    "동그리: 작은 산 → 만석 품. '투웅' — 2-23 마지막 줄과 같은 소리(소리 색 없음)")

add("2-28", "1988년 4월, 같은 밤(자정 지나)", "봄, 깊은 밤",
    "어둠 속 고물상 문틈·창으로 번지는 노란 백열등 한 줄기, 영감은 그 빛을 등짐. 높은 와이드에서 섬 전체에 불 켜진 곳은 거기 하나",
    "#E8C46A", "#2A3352", ["#1A2238", "#F2D27A", "#5B6145"],
    [ch("manseok", M1, "품에서 동그리를 두 손으로 내밂, 긴 손가락"), ch("kwak", K1, "돋보기 이마에, 자다 깬 얼굴 아님. 잠옷 차림 근거 없음 — 기본 의상(판단)")],
    ["동그리", "빈 사과 상자(발끝으로 밀어 놓음)"],
    [], "온기",
    sc(KWAK, "1988 April, deep night, darkness all around, a warm yellow bulb light spilling through the door gap and window, the doorway backlit; high wide: " + P + ", at night, the only lit spot on the whole island", "#E8C46A", "#2A3352"),
    "동그리: 만석 → 곽 영감(3화 S#1에서 다시 손본 동그리를 은주 앞에). 문 두드림 '똑. 똑.' 두 번 = 벽 '톡톡' 박자")

add("2-29", "1988년 4월, 같은 밤(같은 시각)", "봄, 깊은 밤",
    "거의 어둠, 남색. 은주 귀에만 아주 희미한 빛",
    "#1A2238", "#232C4A", ["#3A4A6B", "#E9EEF5"],
    [ch("eunju", E1, "소리굽쇠 미착용(2-25에서 뺌). 머리는 풀린 채(2-25). 깊이 잠듦, 이불이 귀까지")],
    ["이불"],
    [], "온기",
    sc(ROOM, "1988 April, deep night, near-total darkness tinted navy, a faint glow on the edge of the blanket", "#1A2238", "#232C4A"),
    "멀리 '똑. 똑.'에 귀가 움직이지 않음 — 소리 색 넣지 않음(듣지 못한 소리). 2화 끝")

# ---------- 저장 ----------
OUT.write_text(json.dumps(S, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", len(S))
