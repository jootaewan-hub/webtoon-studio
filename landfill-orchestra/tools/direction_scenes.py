"""G10 연출 노트 2부(장면별 포인트) 뼈대: 콘티에서 사실 칸을 뽑는다 (표준 라이브러리만).

  python tools/direction_scenes.py skeleton   → story/direction_parts/ep1~3.md (판단 칸은 '…'로 비워 둠)
  python tools/direction_scenes.py merge      → story/direction.md 2부를 ep1~3.md로 채움
  python tools/direction_scenes.py check      → 2부 점검(빈 칸, 장면 범위 밖 컷 번호, 무음 칸 위치, 사실 줄 변경)
  python tools/direction_scenes.py sfx        → story/sfx_list.md 부록(전수 목록)을 다시 만들고 표기를 점검

사실 칸: 컷 범위·컷 수·높이 흐름, 소리 색 컷(색), 효과음(위계 ①②③), 무음 컷, 대사·내레이션 수, 씬 프리셋 빛·대표 색.
판단 칸(작가가 채움): 목표 감정, 템포, 앵글, 조명·색, 효과음 연출, 무음·여백, 12세·아동 보호(해당할 때만).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTS = ROOT / "story" / "direction_parts"
# ② 소리 서명(sfx_list.md 2절): 글자 모양이 정확히 맞을 때만. 소리 색이 붙으면 ①이 우선한다.
SIGN = [
    ("리어카", re.compile(r"끼익,? ?덜컹")),
    ("국자", re.compile(r"^(탕, 탕, 탕|탕탕)$")),
    ("문", re.compile(r"^똑\. 똑\.$")),
    ("벽", re.compile(r"^톡톡(\. 톡\.)?$")),
    ("라디오", re.compile(r"지지?직")),
    ("소리굽쇠", re.compile(r"^웅―(\. 라\.)?$")),
]


# G9 콘티에서 '축소 후보 적용'으로 다른 장면에 합친 대본 장면(대본 S# → 콘티 장면)
MERGED = {
    "1": ["S#15 섬 어귀 게시판(저녁) → S#16 안(1-106~1-107 압정)"],
    "2": ["S#3 시내버스 → S#4 머리(2-011 위 칸 안내문)", "S#7 둑길 한가운데 → S#6 끝(2-027 아래 칸 수첩)",
          "S#17 공방(겨울) → S#14 몽타주 안(2-053)"],
    "3": ["S#13 구청 복도 → S#12 안(화분 '똑, 똑' 대신 3-054 땀방울 '똑')"],
}


def bare(text):
    """앞의 출처 괄호 '(멀리) ' 를 뗀 소리 글자."""
    return re.sub(r"^\([^)]*\)\s*", "", text).strip()


def tier(l):
    if re.search(r"#[0-9A-Fa-f]{6}", l["speaker"]):
        return "①"
    if any(rx.search(bare(l["text"])) for _, rx in SIGN):
        return "②"
    return "③"


def skeleton():
    cuts = json.loads((ROOT / "storyboard" / "data" / "cuts.json").read_text(encoding="utf-8"))
    presets = {p["scene"]: p for p in json.loads((ROOT / "design" / "scene_presets.json").read_text(encoding="utf-8"))}
    groups = []
    for c in cuts:
        ep = c["id"].split("-")[0]
        key = (ep, c.get("scene", ""))
        if not groups or groups[-1][0] != key:
            groups.append((key, []))
        groups[-1][1].append(c)
    PARTS.mkdir(parents=True, exist_ok=True)
    out = {}
    for (ep, scene), cs in groups:
        m = re.match(r"S(\d+)\s+(.*)", scene)
        sn, title = (m.group(1), m.group(2)) if m else ("?", scene)
        p = presets.get(f"{ep}-{sn}", {})
        hs = " ".join(str(c["height"]) for c in cs)
        sc = []
        for c in cs:
            labels = " ".join(l["speaker"] for l in c["lines"] if l["type"] == "sfx")
            names = re.findall(r"\(([^)#]*?)\s*#", labels)
            if names:
                sc.append(f"{c['id']}({','.join(dict.fromkeys(names))})")
        sfx = {"①": [], "②": [], "③": []}
        for c in cs:
            for l in c["lines"]:
                if l["type"] == "sfx":
                    sfx[tier(l)].append(f"{l['text']}({c['id']})")
        silent = [c["id"] for c in cs if not c["lines"] or any(l["text"] == "(무음)" for l in c["lines"])]
        talk = sum(1 for c in cs for l in c["lines"] if l["type"] in ("dialogue", "thought", "whisper") and l["text"] != "(무음)")
        nar = sum(1 for c in cs for l in c["lines"] if l["type"] == "narration")
        block = [f"### {ep}화 S#{sn} {title} — {cs[0]['id']}~{cs[-1]['id']} ({len(cs)}컷)",
                 f"- 사실: 높이 {hs} · 대사 {talk}·내레이션 {nar} · 무음 {', '.join(silent) or '없음'}",
                 f"- 사실: 빛 {p.get('light', '(프리셋 없음)')} · 대표 색 {p.get('key_hex', '')}/그림자 {p.get('shadow_hex', '')}",
                 f"- 사실: 소리 색 {', '.join(sc) or '없음'}",
                 f"- 사실: 효과음 ① {' '.join(sfx['①']) or '-'} / ② {' '.join(sfx['②']) or '-'} / ③ {' '.join(sfx['③']) or '-'}",
                 "- 목표 감정: …", "- 템포: …", "- 앵글: …", "- 조명·색: …", "- 효과음 연출: …", "- 무음·여백: …", ""]
        out.setdefault(ep, []).append("\n".join(block))
    for ep, blocks in out.items():
        f = PARTS / f"ep{ep}.md"
        if f.exists():
            print(f"이미 있음, 건너뜀: {f}")
            continue
        merged = "".join(f"- 합친 장면: {m}\n" for m in MERGED.get(ep, []))
        f.write_text(f"## {ep}화\n\n{merged}\n" + "\n".join(blocks), encoding="utf-8")
        print(f"→ {f} ({len(blocks)}장면)")


def merge():
    d = ROOT / "story" / "direction.md"
    t = d.read_text(encoding="utf-8")
    head = t.split("## 2부. 장면별 포인트", 1)[0]
    body = "\n".join((PARTS / f"ep{e}.md").read_text(encoding="utf-8").strip() + "\n" for e in (1, 2, 3))
    if "콘티 수정 제안" in body:
        print("주의: '콘티 수정 제안' 절이 2부에 들어간다. 반영·기각 후 지우거나 review/로 옮길 것")
    left = len(re.findall(r"^- [^:\n]+: …$", body, re.M))
    d.write_text(head + "## 2부. 장면별 포인트\n\n각 장면의 '사실' 줄은 콘티(`storyboard/source/storyboard.md`)에서 기계로 뽑았다. 나머지 줄은 연출 판단이다.\n\n" + body,
                 encoding="utf-8")
    print(f"→ {d} (빈 판단 칸 '…' {left}개)")


def sfx():
    """효과음 전수 목록(부록)과 표기 점검. 부록은 sfx_list.md의 표시 줄 아래를 통째로 바꾼다."""
    cuts = json.loads((ROOT / "storyboard" / "data" / "cuts.json").read_text(encoding="utf-8"))
    rows, probs = {}, []
    for c in cuts:
        for l in c["lines"]:
            if l["type"] != "sfx":
                continue
            t, sp = l["text"], l["speaker"]
            label = sp.replace("SFX", "").strip() or "-"
            k = (tier(l), t, label)
            rows.setdefault(k, []).append(c["id"])
            outside = re.sub(r"\([^)]*\)", "", t)
            if "—" in outside or "-" in outside.replace("따닥-쿵", "").replace("쿠웅-따악", ""):
                probs.append(f"{c['id']} '{t}': 소리 글자의 긴소리는 ―(U+2015)")
            if "..." in t:
                probs.append(f"{c['id']} '{t}': 말줄임은 …")
            if "(" in t and not (t.startswith("(") or t.endswith(")")):
                probs.append(f"{c['id']} '{t}': 괄호는 맨 앞(출처) 또는 맨 끝(뜻풀이)")
            if "덜컹" in t and "끼익" in t and not re.search(r"끼익,? ?덜컹", t):
                probs.append(f"{c['id']} '{t}': 리어카 서명은 '끼익, 덜컹'")
    out = ["", "| 위계 | 소리 글자 | 표시 | 컷 수 | 컷 |", "|---|---|---|---|---|"]
    for (tr, t, label), ids in sorted(rows.items(), key=lambda kv: (kv[0][0], kv[1][0])):
        out.append(f"| {tr} | {t} | {label} | {len(ids)} | {', '.join(dict.fromkeys(ids))} |")
    n = {tr: sum(len(v) for k, v in rows.items() if k[0] == tr) for tr in "①②③"}
    f = ROOT / "story" / "sfx_list.md"
    mark = "<!-- 부록: tools/direction_scenes.py sfx 가 만든다. 아래는 손으로 고치지 않는다. -->"
    t = f.read_text(encoding="utf-8")
    head = t.split(mark, 1)[0].rstrip() + "\n\n" + mark + "\n"
    summary = f"\n콘티 효과음 {sum(n.values())}개(종류 {len(rows)}): ① {n['①']} · ② {n['②']} · ③ {n['③']}. 표기 문제 {len(probs)}건.\n"
    f.write_text(head + summary + "\n".join(out) + "\n", encoding="utf-8")
    print(f"→ {f} 부록 갱신. ① {n['①']} ② {n['②']} ③ {n['③']}, 종류 {len(rows)}")
    for p in probs:
        print("[표기]", p)
    print(f"표기 문제 {len(probs)}건")
    return 1 if probs else 0


ALLOWED_BLANK = {("1", "11"), ("2", "29"), ("3", "27"), ("3", "34")}  # 1부 1절 무음 칸 네 곳


def check():
    cuts = json.loads((ROOT / "storyboard" / "data" / "cuts.json").read_text(encoding="utf-8"))
    ids = {c["id"] for c in cuts}
    files = sorted(PARTS.glob("ep*.md"))
    probs, n = [], 0
    for f in files:
        for blk in re.split(r"^(?=### )", f.read_text(encoding="utf-8"), flags=re.M):
            m = re.match(r"### (\d)화 S#(\d+) .*?— (\d-\d{3})~(\d-\d{3})", blk)
            if not m:
                continue
            n += 1
            ep, sn, a, b = m.groups()
            where = f"{ep}화 S#{sn}"
            for line in blk.splitlines()[1:]:
                if line.startswith("## "):
                    break  # 파일 끝 '콘티 수정 제안' 절은 범위 점검에서 뺀다
                if re.match(r"^- [^:]+: …$", line):
                    probs.append(f"{where}: 빈 칸 — {line}")
                if line.startswith("- 사실:"):
                    continue
                for cid in re.findall(r"\b\d-\d{3}\b", line):
                    if cid not in ids:
                        probs.append(f"{where}: 없는 컷 {cid}")
                    elif not (a <= cid <= b):
                        probs.append(f"{where}: 범위({a}~{b}) 밖 컷 {cid}")
                placed = re.search(r"무음 칸[^.]{0,20}?(둔다|두어|넣|쓴다|하나로|하나를)", line)
                denied = re.search(r"무음 칸[^.]{0,12}?(없|아님|않)", line)
                if placed and not denied and (ep, sn) not in ALLOWED_BLANK:
                    probs.append(f"{where}: 무음 칸은 1부 네 곳만 — {line[:60]}")
    for p_ in probs:
        print("[점검]", p_)
    print(f"장면 {n} · 문제 {len(probs)}건")
    return 1 if probs else 0


if __name__ == "__main__":
    {"skeleton": skeleton, "merge": merge, "sfx": sfx, "check": check}[sys.argv[1] if len(sys.argv) > 1 else "skeleton"]()
