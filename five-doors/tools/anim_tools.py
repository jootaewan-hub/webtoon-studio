#!/usr/bin/env python3
"""G11 애니메이션 콘티 도구.

  python3 anim_tools.py skeleton <회차>     # anim/parts/ep<N>_skeleton.md 생성(웹툰 컷별 대사·SFX·최소 길이)
  python3 anim_tools.py check <회차>        # anim/parts/ep<N>.md 검사(형식, 원 컷 누락, 대사 누락, 길이·프레임)
  python3 anim_tools.py merge               # anim/parts/ep0~6 → anim/storyboard_anim.md (총 길이 표 포함)
  python3 anim_tools.py cues                # anim/storyboard_anim.md → anim/sound_cues.md (타임코드 24fps)

입력: storyboard/data/cuts.json (kit.py import 결과). 표준 라이브러리만 쓴다.
"""
import json, re, sys
from collections import OrderedDict
from pathlib import Path

P = Path(__file__).resolve().parent.parent
ANIM = P / "anim"; PARTS = ANIM / "parts"
FPS = 24
COLS = ["샷", "원 컷", "길이", "카메라", "레이아웃·키포즈", "연기·립싱크", "SFX", "BGM·앰비언스", "대사·VO", "전환"]


def cuts():
    return json.loads((P / "storyboard/data/cuts.json").read_text(encoding="utf-8"))


def norm(s):
    s = s.replace("...", "…")
    return re.sub(r"[\s.,!?…~·\-—–'\"“”‘’()]", "", s)


def syll(t):
    return len(re.findall(r"[가-힣0-9A-Za-z]", t))


def min_sec(c):
    talk = [l for l in c["lines"] if l["type"] != "sfx" and l["text"] != "(무음)"]
    s = sum(syll(l["text"]) for l in talk) / 6.5 + 0.4 * len(talk)
    base = 2.0 if c["height"] >= 1200 else 1.5
    return round(max(base, s), 1)


def panels(screen):
    m = re.search(r"(가로|세로|위아래)\s*(\d)\s*(분할|단)", screen)
    return int(m.group(2)) if m else 1


def skeleton(ep):
    PARTS.mkdir(parents=True, exist_ok=True)
    cs = [c for c in cuts() if c["id"].startswith(f"{ep}-") or (ep == 1 and c["id"].startswith("0-"))]
    out = [f"# {ep}화 애니 콘티 뼈대 (자동 생성 — 이 파일은 참고용, 결과는 ep{ep}.md에 쓴다)", "",
           "컷마다: 원 컷 / 분할 칸 수 / 최소 길이(대사 기준, 한국어 초당 6.5음절 + 대사마다 숨 0.4초) / 대사·VO 원문 / SFX 원문 / 화면 첫 문장", ""]
    scene = None
    for c in cs:
        if c["scene"] != scene:
            scene = c["scene"]; out += ["", f"### {c['chapter']} / {scene}", ""]
        talk = " / ".join(f"{l['speaker']}: {l['text']}" if l["speaker"] else l["text"]
                          for l in c["lines"] if l["type"] != "sfx")
        sfx = " / ".join(f"{l['speaker']}: {l['text']}" for l in c["lines"] if l["type"] == "sfx")
        out.append(f"- {c['id']} | {c['shot']} | {c['height']}px | 분할 {panels(c['screen'])} | 최소 {min_sec(c)}초 | "
                   f"대사·VO: {talk or '—'} | SFX: {sfx or '—'} | 화면: {c['summary']}")
    (PARTS / f"ep{ep}_skeleton.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"ep{ep}: {len(cs)}컷 뼈대 → {PARTS / f'ep{ep}_skeleton.md'}")


def parse_anim(text):
    rows, scenes, cur = [], [], None
    for i, ln in enumerate(text.splitlines(), 1):
        if ln.startswith("### "):
            cur = {"title": ln[4:].strip(), "rows": [], "bgm": "", "amb": "", "line": i}; scenes.append(cur); continue
        if cur is not None and ln.startswith("BGM:"):
            cur["bgm"] = ln[4:].strip(); continue
        if cur is not None and ln.startswith("앰비언스:"):
            cur["amb"] = ln[5:].strip(); continue
        if not ln.startswith("|") or ln.startswith("|---") or ln.startswith("| 샷"):
            continue
        cells = [x.strip() for x in ln.strip().strip("|").split("|")]
        r = {"line": i, "cells": cells}
        rows.append(r)
        if cur is not None:
            cur["rows"].append(r)
    return rows, scenes


def dur_of(cell):
    m = re.match(r"^(\d+(?:\.\d+)?)초\s*/\s*(\d+)f$", cell)
    return (float(m.group(1)), int(m.group(2))) if m else (None, None)


def check(ep):
    f = PARTS / f"ep{ep}.md"
    text = f.read_text(encoding="utf-8")
    rows, scenes = parse_anim(text)
    cs = [c for c in cuts() if c["id"].startswith(f"{ep}-") or (ep == 1 and c["id"].startswith("0-"))]
    probs = []
    ids_seen = set(); vo_all = ""; total = 0.0
    for r in rows:
        c = r["cells"]
        if len(c) != 10:
            probs.append(f"L{r['line']} 열 수 {len(c)} (10이어야 함)"); continue
        if not re.match(r"^\dS\d{2}-\d{2}$", c[0]):
            probs.append(f"L{r['line']} 샷 번호 형식 오류: {c[0]}")
        for cid in re.findall(r"\d-\d{3}", c[1]):
            ids_seen.add(cid)
        sec, fr = dur_of(c[2])
        if sec is None:
            probs.append(f"L{r['line']} 길이 형식 오류: {c[2]} (예: 2.5초 / 60f)")
        else:
            total += sec
            if fr != round(sec * FPS):
                probs.append(f"L{r['line']} {c[0]} 프레임 불일치 {sec}초≠{fr}f")
        vo_all += " " + c[8]
    for s in scenes:
        if not s["bgm"]:
            probs.append(f"L{s['line']} 장면 머리에 BGM: 줄 없음")
        if not s["amb"]:
            probs.append(f"L{s['line']} 장면 머리에 앰비언스: 줄 없음")
    miss_cut = [c["id"] for c in cs if c["id"] not in ids_seen]
    vn = norm(vo_all)
    miss_line = []
    for c in cs:
        for l in c["lines"]:
            if l["type"] == "sfx" or l["text"] == "(무음)":
                continue
            if norm(l["text"]) and norm(l["text"]) not in vn:
                miss_line.append(f"{c['id']} {l['speaker']}: {l['text'][:40]}")
    rep = {"ep": ep, "샷": len(rows), "장면": len(scenes), "총 길이(초)": round(total, 1),
           "총 길이": f"{int(total // 60)}:{int(total % 60):02d}", "형식 문제": len(probs),
           "원 컷 누락": len(miss_cut), "대사 누락": len(miss_line)}
    print(json.dumps(rep, ensure_ascii=False))
    for p in probs[:40]:
        print("  형식:", p)
    if miss_cut:
        print("  원 컷 누락:", ", ".join(miss_cut))
    for m in miss_line[:60]:
        print("  대사 누락:", m)


def tc(sec):
    fr = int(round(sec * FPS)); h, rem = divmod(fr, 3600 * FPS); m, rem = divmod(rem, 60 * FPS); s, f = divmod(rem, FPS)
    return f"{h:02d}:{m:02d}:{s:02d}:{f:02d}"


def merge():
    head = ["# 애니메이션 콘티 (G11) — 「단톡방에 그 남자가 있다」", "",
            "기준: 웹툰 콘티 `storyboard/source/storyboard.md`, 연출 원칙 `story/direction.md`(8절 BGM 큐 M1~M7, 앰비언스), 효과음 표기 `story/sfx_list.md`.",
            "밀도: 혼합안(잠정) — 웹툰 컷 1개 = 기본 1샷(모션코믹 수준), 분할 컷은 칸마다 1샷, 반전·훅·코미디 박자 컷은 2~3샷. 24fps.",
            "샷 번호: `<회차>S<씬 두자리>-<두자리>` (예: 2S05-03). 표지는 0S00.", "", "## 회차별 길이", "",
            "| 회차 | 샷 | 장면 | 길이 |", "|---|---|---|---|"]
    body = []; grand = 0.0
    for ep in range(1, 7):
        f = PARTS / f"ep{ep}.md"
        if not f.exists():
            continue
        t = f.read_text(encoding="utf-8")
        rows, scenes = parse_anim(t)
        sec = sum(dur_of(r["cells"][2])[0] or 0 for r in rows if len(r["cells"]) == 10)
        grand += sec
        head.append(f"| {ep}화 | {len(rows)} | {len(scenes)} | {int(sec // 60)}:{int(sec % 60):02d} |")
        body.append(t.strip())
    head.append(f"| 합계 | | | {int(grand // 3600)}:{int(grand % 3600 // 60):02d}:{int(grand % 60):02d} |")
    (ANIM / "storyboard_anim.md").write_text("\n".join(head) + "\n\n" + "\n\n".join(body) + "\n", encoding="utf-8")
    print(f"합본 → anim/storyboard_anim.md (총 {grand/60:.1f}분)")


def cues():
    t = (ANIM / "storyboard_anim.md").read_text(encoding="utf-8")
    out = ["# 사운드 큐 시트 (G11) — 「단톡방에 그 남자가 있다」", "",
           "`anim/storyboard_anim.md`에서 자동 생성(`five-doors/tools/anim_tools.py cues`). 타임코드는 회차마다 00:00:00:00에서 시작, 24fps(HH:MM:SS:FF).",
           "종류: SFX(효과음·폴리) / BGM(음악 큐, direction.md 8절 M1~M7) / AMB(앰비언스) / VO(대사·내레이션 첫 줄).", ""]
    ep = None; clock = 0.0
    cur_scene = None
    for ln in t.splitlines():
        m = re.match(r"^## (\d)화", ln)
        if m:
            ep = m.group(1); clock = 0.0
            out += ["", f"## {ln[3:].strip()}", "", "| 타임코드 | 샷 | 종류(SFX/BGM/AMB/VO) | 내용 | 메모 |", "|---|---|---|---|---|"]
            continue
        if ln.startswith("### "):
            cur_scene = ln[4:].strip(); continue
        if ln.startswith("BGM:") and ep:
            out.append(f"| {tc(clock)} | — | BGM | {ln[4:].strip()} | 장면 시작: {cur_scene[:40] if cur_scene else ''} |"); continue
        if ln.startswith("앰비언스:") and ep:
            out.append(f"| {tc(clock)} | — | AMB | {ln[5:].strip()} | |"); continue
        if not ln.startswith("|") or ln.startswith("|---") or ln.startswith("| 샷") or not ep:
            continue
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        if len(c) != 10:
            continue
        sec = dur_of(c[2])[0] or 0
        if c[6] and c[6] not in ("—", "-", "없음"):
            out.append(f"| {tc(clock)} | {c[0]} | SFX | {c[6]} | 원 컷 {c[1]} |")
        if c[7] and c[7] not in ("—", "-", "유지", "이어서"):
            out.append(f"| {tc(clock)} | {c[0]} | BGM/AMB | {c[7]} | |")
        if c[8] and c[8] not in ("—", "-"):
            first = c[8].split(" / ")[0]
            out.append(f"| {tc(clock)} | {c[0]} | VO | {first[:60]}{'…' if len(first) > 60 or ' / ' in c[8] else ''} | |")
        clock += sec
    (ANIM / "sound_cues.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"큐 시트 → anim/sound_cues.md ({sum(1 for x in out if x.startswith('| 0'))}행)")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "skeleton":
        skeleton(int(sys.argv[2]))
    elif cmd == "check":
        check(int(sys.argv[2]))
    elif cmd == "merge":
        merge()
    elif cmd == "cues":
        cues()
