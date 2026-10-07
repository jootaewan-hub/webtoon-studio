#!/usr/bin/env python3
"""「단톡방에 그 남자가 있다」 킷 입력 만들기.

프로젝트 원본(story/, storyboard/parts/, handoff/)에서 킷 입력을 다시 만든다.
원본을 고친 뒤에는 이 스크립트 → kit.py import --replace → kit.py prompts --track all 순서로 돌린다.

  cd five-doors/storyboard
  python3 build_kit_data.py
  python3 kit.py import --replace
  python3 kit.py validate
  python3 kit.py prompts --track all

만드는 것
  source/novel.md       ← ../story/novel.md (그대로 복사)
  source/storyboard.md  ← parts/ep1~ep6.md 합본(머리말 + 회차 순서)
  data/characters.json  ← ../handoff/characters/<id>.md 의 CHARACTER LOCK(영문, 한 글자도 바꾸지 않음)
  data/sets.json        ← ../handoff/sets.md 의 장소별 SET LOCK(영문, 한 글자도 바꾸지 않음)
  data/style.json, data/tracks.json ← ../handoff/style_lock.md 기준(트랙 1·2·3 문구 원문 그대로)
표준 라이브러리만 쓴다.
"""
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJ = HERE.parent
DATA, SRC = HERE / "data", HERE / "source"
DATA.mkdir(exist_ok=True); SRC.mkdir(exist_ok=True)


def code_block_after(text, heading_re):
    m = re.search(heading_re, text, re.M)
    if not m:
        return None
    b = re.search(r"```text\n(.+?)\n```", text[m.end():], re.S)
    return b.group(1).strip() if b else None


# 1. 원본 문서
(SRC / "novel.md").write_text((PROJ / "story/novel.md").read_text(encoding="utf-8"), encoding="utf-8")
parts = []
for n in range(1, 7):
    parts.append((HERE / f"parts/ep{n}.md").read_text(encoding="utf-8").strip())
head = ("# 단톡방에 그 남자가 있다 — 웹툰 콘티(G9)\n\n"
        "6화 본편과 표지. 컷 번호는 `회차-세자리`이고 표지는 `0-001`~`0-003`이다. 형식 규격은 `../SPEC.md`(storyboard/SPEC.md)에 있다.\n"
        "원작 대사·내레이션은 `story/novel.md` 원문 그대로이며, 순수한 동작·시각 묘사는 화면·연출 칸의 그림 지시로 옮겼다.\n")
(SRC / "storyboard.md").write_text(head + "\n\n" + "\n\n".join(parts) + "\n", encoding="utf-8")

# 2. 인물 (CHARACTER LOCK)
CHARS = [("dogyeom", "도겸", ["한도겸"]), ("yujin", "유진", ["서유진"]), ("miran", "미란", ["차미란"]),
         ("sera", "세라", ["오세라"]), ("harin", "하린", ["윤하린"]), ("hyesuk", "혜숙", ["정혜숙"]),
         ("sunok", "순옥", ["박순옥"])]
chars = []
for cid, name, aliases in CHARS:
    t = (PROJ / f"handoff/characters/{cid}.md").read_text(encoding="utf-8")
    lock = code_block_after(t, r"^## 2\. CHARACTER LOCK")
    if not lock:
        raise SystemExit(f"CHARACTER LOCK 없음: {cid}")
    chars.append({"id": cid, "name": name, "aliases": aliases, "look": lock,
                  "lock_file": f"handoff/characters/{cid}.md"})
(DATA / "characters.json").write_text(json.dumps(chars, ensure_ascii=False, indent=2), encoding="utf-8")

# 3. 장소 (SET LOCK)
sets_md = (PROJ / "handoff/sets.md").read_text(encoding="utf-8")
sets = {}
for m in re.finditer(r"^## (\d+|짧게 [ABC])\. (.+)$", sets_md, re.M):
    key, name = m.group(1), m.group(2).strip()
    sec_id = key if key.isdigit() else key[-1]
    lock = code_block_after(sets_md[m.start():], rf"^### {re.escape(sec_id)}-\d+\. SET LOCK")
    if lock:
        sets[key] = {"name": name, "lock": lock}
(DATA / "sets.json").write_text(json.dumps(sets, ensure_ascii=False, indent=2), encoding="utf-8")

# 4. 스타일·트랙 (style_lock.md 원문 문구)
sl = (PROJ / "handoff/style_lock.md").read_text(encoding="utf-8")
T1 = code_block_after(sl, r"^## 트랙 1")
T2 = code_block_after(sl, r"^## 트랙 2")
T3 = code_block_after(sl, r"^## 트랙 3")
style = {
    "era": "2026년 9~10월, 한국 경기도 호수 신도시의 2024년 준공 신축 대단지 '레이크시티 더퍼스트'(가상, 15개 동 3,012세대)와 단지 상가·커뮤니티. "
           "에필로그는 2027년 2월 수원지방법원 형사법정, 2029년 10월 교도소 정문과 새솔신도시 모델하우스(가상). 스마트폰·메신저·스마트워치가 있는 현재.",
    "palette_hint": "밤 남색 #1A1E3A / 보라 그림자 #3B2F55, 피부 기준 #F3CDB6(인물별 피부는 CHARACTER LOCK 우선), 금빛 보케 #F2C26B. "
                    "인물 대표 색(캘린더 색): 유진 회색 #9A9EA3, 미란 버건디 #7A1E2E, 세라 민트 #7FD1BE, 하린 하늘색 #9CC7E8, 혜숙 금색 #C9A45C — "
                    "다섯 여자가 한 컷에 나오면 각자의 대표 색이 옷·소품·조명 중 한 곳에 반드시 들어간다. 장면마다 광원은 하나(연출 메모의 조명 줄을 따른다).",
    "fonts": {"dialogue": "Gowun Dodum", "narration": "Gowun Batang", "sfx_main": "East Sea Dokdo",
              "sfx_comedy": "Black Han Sans", "handwriting": "Nanum Pen Script"},
    "bubbles": "대사=흰 둥근 풍선, 외침=각진 풍선, 생각=점선 풍선, 속삭임=얇은 점선+작은 글씨, 전화 너머=톱니 테두리, "
               "문자·메신저=가상 UI 말풍선(Nanum Pen Script 아님, 시스템 고딕 느낌), 내레이션=사각 박스(Gowun Batang)",
    "tone": "블랙코미디 + 19세 관능 드라마. 한 남자가 한 단지 안에서 다섯 여자를 '관리'하다가 다섯 여자에게 역관리당한다. 웃음은 상황의 아이러니에서 나온다.",
}
(DATA / "style.json").write_text(json.dumps(style, ensure_ascii=False, indent=2), encoding="utf-8")

tracks = {
    "tracks": {
        "webtoon_adult": {
            "title": "본편 웹툰 이미지 — 성인(19세)",
            "brief": "본편 컷 이미지 프롬프트. 기본은 트랙 1(글로시 반실사)이고, 콘티 화면 칸이 [트랙2]로 시작하는 컷은 자동으로 트랙 2(코미디 셀) 문구가 붙는다. "
                     "각 컷에 장면 연출 메모(장소·조명·의상 HEX), 해당 장소의 SET LOCK, 등장인물의 CHARACTER LOCK이 붙어 있다. "
                     "확정 레퍼런스 이미지(handoff/refs/)를 함께 올리고 생성한다. 수위 상한은 콘티와 같다.",
            "style": T1, "style_track2": T2, "style_track3": T3,
        },
        "shorts": {
            "title": "쇼츠 (9:16 세로 영상) — 티저 수위",
            "brief": "화당 1~2편, 편당 60초 안팎. 관능 컷은 쓰지 않거나 트랙 3(네온 누아르 실루엣)으로 바꿔 쓴다(인스타·틱톡 추천 정책 대응). "
                     "첫 2초에 훅(가장 강한 대사나 반전 컷). 내레이션은 VO, 대사는 자막. 세분화 콘티를 그대로 쓰면 60초를 넘으므로 하이라이트 컷만 고른다.",
            "style": T3,
        },
        "anim": {
            "title": "애니메이션 샷 리스트",
            "brief": "24fps 기준 컷별 샷 리스트(길이·카메라·레이어·립싱크). 세부 연출(키포즈·카메라 무빙·SFX·BGM 큐)은 ../anim/storyboard_anim.md(G11)를 우선한다.",
        },
    },
    "global_negative": [
        "모든 얼굴은 창작된 성인 — 실존 인물·유명인과 닮게 만들지 않는다(실화 모티프 작품)",
        "실제 브랜드 로고·엠블럼, 실제 화폐 도안, 법원·경찰·교도소 휘장 금지(로고 없는 시계, 퀼팅 체인 백, 도안 없는 소품용 지폐)",
        "이미지 안에 말풍선·글자·간판 문구를 넣지 않는다(레터링은 후공정)",
        "미성년으로 보이는 표현 금지 — 하린(25)은 성인 체형·성숙한 표정",
        "아이(지호 5세, 소이 7세)는 관능 장면과 같은 컷·공간에 두지 않는다",
    ],
    "intimate_rule": [
        "허용: 몸 라인이 드러나는 의상, 속옷·슬립, 옷이 벗겨지는 과정, 드러난 등·어깨·쇄골·허리·허벅지, 시트로 가린 나신, 역광 실루엣, 손과 입술, 땀과 숨",
        "금지: 성기, 유두 노출, 삽입·성행위의 직접 묘사, 체액",
        "생성기가 거절하면 가림 소품(시트·커튼·와인잔·셔츠 자락) → 실루엣 → 손·입술·사물 인서트 순서로 바꾼다",
    ],
    "violence_rule": ["폭력 없음. 체포는 비폭력(신분증·수갑·손목)", "상처·출혈 묘사 금지"],
    "self_harm_rule": ["자해·투신 묘사 금지"],
    "child_rule": [
        "아이(지호·소이)가 있는 장면: 관능 요소 없음. 어른의 몸 라인 강조·노출 연출을 하지 않고 평상시 차림으로 그린다",
        "아이와 어른의 신체 접촉은 일상 동작(안기, 목말, 손잡기)만",
    ],
}
(DATA / "tracks.json").write_text(json.dumps(tracks, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"source: novel.md, storyboard.md / 인물 {len(chars)}명 / 장소 SET LOCK {len(sets)}곳({', '.join(sets)})")
