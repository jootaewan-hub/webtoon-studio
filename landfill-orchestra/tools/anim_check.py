"""G11 애니메이션 콘티 점검·합치기·큐 시트 (표준 라이브러리만).

  python tools/anim_check.py check [anim/parts/ep1_a.md ...]   → 조각 점검(인자 없으면 anim/parts/*.md 전부)
  python tools/anim_check.py build                             → anim/storyboard_anim.md(합본+길이표), anim/sound_cues.md(타임코드 큐 시트)

조각 형식(장면마다):
  ### 1화 S#4 은주네 판잣집, 부엌 겸 방 (저녁) — 원 컷 1-034~1-039 — 대본 01:40
  BGM: …
  앰비언스: …
  | 샷 | 원 컷 | 길이 | 카메라 | 레이아웃·키포즈 | 연기·립싱크 | SFX | BGM·앰비언스 | 대사·VO | 전환 |
  |---|---|---|---|---|---|---|---|---|---|
  | 1-S04-01 | 1-034 | 6.0초 / 144f | … | … | … | … | … | — | 컷 |

점검: 장면 길이 합 = 대본 [예상 길이] ±15%, 대본 대사·내레이션이 그 장면 '대사·VO' 칸에 정확히 한 번,
샷 길이 ≥ 대사 음절/6.5 + 0.3초, 초·프레임(24fps) 일치, 샷 번호 형식·연속, 10칸,
원 컷이 그 장면(합친 장면은 받은 장면) 범위 안, 웹툰 353컷 전부 한 번 이상(전체 점검일 때).
원 컷 특수값: '—(무음 칸)', '—(대본 전용)'. 한 샷이 여러 컷이면 '1-034·1-035'.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTS = ROOT / "anim" / "parts"
sys.path.insert(0, str(ROOT / "tools"))
from sb_check import script_lines  # noqa: E402

FPS = 24
HEAD_RE = re.compile(r"^### (\d)화 S#(\d+) (.+?) — 원 컷 (.+?) — 대본 (\d\d):(\d\d)\s*$")
SHOT_RE = re.compile(r"^(\d)-S(\d\d)-(\d\d)$")
LEN_RE = re.compile(r"^(\d+(?:\.\d+)?)초 / (\d+)f$")
# G9에서 다른 장면에 합친 대본 장면 → 받은 장면(웹툰 컷 범위를 빌려 씀)
MERGED = {("1", 15): 16, ("2", 3): 4, ("2", 7): 6, ("2", 17): 14, ("3", 13): 12}
TOL = 0.15


def script_lengths():
    t = (ROOT / "story" / "script.md").read_text(encoding="utf-8")
    out, ep = {}, None
    for line in t.splitlines():
        m = re.match(r"^#{2,3} (\d)화", line)
        if m:
            ep = m.group(1)
        m = re.match(r"^S#(\d+)\.", line)
        if m:
            cur = int(m.group(1))
        m = re.match(r"^\[예상 길이 (\d\d):(\d\d)\]", line)
        if m and ep:
            out[(ep, cur)] = int(m.group(1)) * 60 + int(m.group(2))
    return out


def cut_ranges():
    cuts = json.loads((ROOT / "storyboard" / "data" / "cuts.json").read_text(encoding="utf-8"))
    rng = {}
    for c in cuts:
        ep = c["id"].split("-")[0]
        sn = int(re.match(r"S(\d+)", c["scene"]).group(1))
        rng.setdefault((ep, sn), []).append(c["id"])
    return rng, [c["id"] for c in cuts]


def norm(s):
    return re.sub(r"[\s\"“”'‘’]", "", s).replace("...", "…")


def syllables(s):
    return len(re.findall(r"[가-힣A-Za-z0-9]", s))


def parse(files):
    scenes = []
    for f in files:
        cur = None
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            m = HEAD_RE.match(line)
            if m:
                cur = {"file": f.name, "line": i, "ep": m.group(1), "sn": int(m.group(2)), "title": m.group(3),
                       "cuts": m.group(4), "budget": int(m.group(5)) * 60 + int(m.group(6)), "shots": [], "head": [line]}
                scenes.append(cur)
                continue
            if line.startswith("### "):
                cur = None
                scenes.append({"file": f.name, "line": i, "bad_head": line})
                continue
            if cur is None:
                continue
            if line.startswith("|") and not line.startswith("|---") and not line.startswith("| 샷 "):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                cur["shots"].append({"line": i, "cells": cells, "raw": line})
            elif not cur["shots"]:
                cur["head"].append(line)
    return scenes


def check(files, full):
    budgets = script_lengths()
    rng, all_cuts = cut_ranges()
    scenes = parse(files)
    errs, warns, used = [], [], set()
    totals = {}
    for sc in scenes:
        if "bad_head" in sc:
            errs.append(f"{sc['file']}:{sc['line']} 장면 머리 형식: {sc['bad_head'][:70]}")
            continue
        ep, sn, where = sc["ep"], sc["sn"], f"{sc['ep']}화 S#{sc['sn']}"
        if budgets.get((ep, sn)) != sc["budget"]:
            errs.append(f"{where}: 머리의 대본 길이 {sc['budget']}s ≠ 대본 {budgets.get((ep, sn))}s")
        own = set(rng.get((ep, sn), [])) | set(rng.get((ep, MERGED.get((ep, sn), -1)), []))
        host_of = [k[1] for k, v in MERGED.items() if k[0] == ep and v == sn]
        for h in host_of:
            own |= set(rng.get((ep, h), []))
        total, prev = 0.0, 0
        dlg_cells = []
        for sh in sc["shots"]:
            c, ln = sh["cells"], sh["line"]
            if len(c) != 10:
                errs.append(f"{sc['file']}:{ln} 칸 수 {len(c)} (10이어야 함)")
                continue
            m = SHOT_RE.match(c[0])
            if not m or m.group(1) != ep or int(m.group(2)) != sn:
                errs.append(f"{sc['file']}:{ln} 샷 번호 {c[0]} (기대 {ep}-S{sn:02d}-NN)")
            else:
                k = int(m.group(3))
                if k != prev + 1:
                    errs.append(f"{sc['file']}:{ln} 샷 번호 연속 아님: {c[0]}")
                prev = k
            lm = LEN_RE.match(c[2])
            if not lm:
                errs.append(f"{sc['file']}:{ln} 길이 형식 '{c[2]}' (예: 2.5초 / 60f)")
                secs = 0
            else:
                secs = float(lm.group(1))
                if int(lm.group(2)) != round(secs * FPS):
                    errs.append(f"{sc['file']}:{ln} {c[0]} 프레임 {lm.group(2)} ≠ {secs}×24={round(secs * FPS)}")
            total += secs
            if not c[1].startswith("—"):
                for cid in re.findall(r"\d-\d{3}", c[1]):
                    used.add(cid)
                    if cid not in own:
                        errs.append(f"{sc['file']}:{ln} {c[0]} 원 컷 {cid}가 이 장면 범위 밖")
            elif c[1] not in ("—(무음 칸)", "—(대본 전용)"):
                errs.append(f"{sc['file']}:{ln} 원 컷 특수값은 '—(무음 칸)' 또는 '—(대본 전용)'")
            dl = c[8]
            if dl not in ("—", ""):
                need = syllables(re.sub(r"[^:/]*?:", "", dl)) / 6.5 + 0.3
                if secs and secs + 1e-6 < need:
                    warns.append(f"{sc['file']}:{ln} {c[0]} {secs}초 < 대사 필요 {need:.1f}초")
            dlg_cells.append(norm(dl))
        sc["total"] = total
        b = sc["budget"]
        if b and abs(total - b) > b * TOL:
            errs.append(f"{where}: 길이 합 {total:.1f}s, 대본 {b}s의 ±15% 밖({b * (1 - TOL):.0f}~{b * (1 + TOL):.0f})")
        totals.setdefault(ep, [0, 0])
        totals[ep][0] += total
        totals[ep][1] += b
        joined = "".join(dlg_cells)
        lines = script_lines(int(ep), sn, sn)
        script_joined = "".join(norm(t) for _, _, t in lines)
        seen = set()
        for _, who, txt in lines:
            key = norm(txt)
            if key in seen:
                continue
            seen.add(key)
            want = script_joined.count(key)  # 대본에 같은 줄이 여러 번이거나 다른 줄 속에 들어 있는 경우까지
            n = joined.count(key)
            if n < want:
                errs.append(f"{where}: 대본 대사 누락({n}/{want}) — {who}: {txt[:30]}")
            elif n > want:
                errs.append(f"{where}: 대본 대사 {n}번(대본 {want}번) — {who}: {txt[:30]}")
    if full:
        miss = [c for c in all_cuts if c not in used]
        if miss:
            errs.append(f"쓰지 않은 웹툰 컷 {len(miss)}: {', '.join(miss[:20])}{' …' if len(miss) > 20 else ''}")
        have = {(s["ep"], s["sn"]) for s in scenes if "ep" in s}
        lack = sorted(k for k in budgets if k not in have)
        if lack:
            errs.append(f"빠진 대본 장면 {len(lack)}: " + ", ".join(f"{e}화 S#{n}" for e, n in lack))
    for w in warns:
        print("[주의]", w)
    for e in errs:
        print("[문제]", e)
    for ep in sorted(totals):
        a, b = totals[ep]
        print(f"{ep}화: 샷 길이 합 {a / 60:.1f}분 / 대본 {b / 60:.1f}분")
    n = sum(len(s.get("shots", [])) for s in scenes)
    print(f"장면 {sum(1 for s in scenes if 'ep' in s)} · 샷 {n} · 문제 {len(errs)} · 주의 {len(warns)}")
    return scenes, errs


def tc(sec):
    f = round(sec * FPS)
    return f"{f // (FPS * 3600):02d}:{f // (FPS * 60) % 60:02d}:{f // FPS % 60:02d}:{f % FPS:02d}"


def build():
    files = sorted(PARTS.glob("*.md"))
    scenes, errs = check(files, True)
    if errs:
        print("문제가 있어 합치지 않는다.")
        return 1
    scenes = sorted((s for s in scenes if "ep" in s), key=lambda s: (s["ep"], s["sn"]))
    head = ["# 애니메이션 콘티 — 깡통 바이올린 (G11)", "",
            "대본(`story/script.md`) 80씬을 샷으로 풀었다. 원 컷은 웹툰 콘티 번호다. 24fps. 형식·밀도는 `decisions.md` G11, 소리 규칙은 `story/direction.md` 1부 9절과 `story/sfx_list.md`.",
            "이 파일은 `python3 tools/anim_check.py build`가 `anim/parts/`를 합쳐 만든다. 고칠 때는 조각을 고친다.", "",
            "## 길이표", "", "| 화 | 장면 | 샷 | 길이 | 대본 |", "|---|---|---|---|---|"]
    body, cues = [], ["# 사운드 큐 시트 — 깡통 바이올린 (G11)", "",
                      "`anim/storyboard_anim.md`에서 기계로 뽑았다. 타임코드는 화마다 00:00:00:00에서 시작(24fps). SFX 표기는 `story/sfx_list.md`, 사운드 처리는 부록의 '애니/쇼츠 사운드 큐' 칸을 따른다.", ""]
    ep_t = {}
    cur_ep = None
    for s in scenes:
        if s["ep"] != cur_ep:
            cur_ep = s["ep"]
            body.append(f"\n## {cur_ep}화\n")
            cues += [f"\n## {cur_ep}화\n", "| TC 시작 | TC 끝 | 샷 | 원 컷 | SFX | BGM·앰비언스 | 대사·VO |", "|---|---|---|---|---|---|---|"]
            ep_t[cur_ep] = 0.0
        head.append(f"| {s['ep']} | S#{s['sn']} {s['title']} | {len(s['shots'])} | {s['total'] / 60:.0f}:{s['total'] % 60:04.1f} | {s['budget'] // 60:02d}:{s['budget'] % 60:02d} |")
        body.append("\n".join(s["head"]).rstrip() + "\n")
        body.append("| 샷 | 원 컷 | 길이 | 카메라 | 레이아웃·키포즈 | 연기·립싱크 | SFX | BGM·앰비언스 | 대사·VO | 전환 |")
        body.append("|---|---|---|---|---|---|---|---|---|---|")
        for sh in s["shots"]:
            body.append(sh["raw"])
            c = sh["cells"]
            secs = float(LEN_RE.match(c[2]).group(1))
            t0 = ep_t[s["ep"]]
            if c[6] not in ("—", "") or c[7] not in ("—", "", "유지"):
                cues.append(f"| {tc(t0)} | {tc(t0 + secs)} | {c[0]} | {c[1]} | {c[6]} | {c[7]} | {c[8] if len(c[8]) < 40 else c[8][:38] + '…'} |")
            ep_t[s["ep"]] = t0 + secs
        body.append("")
    tot = sum(ep_t.values())
    head.append(f"| 합계 | | {sum(len(s['shots']) for s in scenes)} | {tot / 60:.1f}분 | {sum(s['budget'] for s in scenes) / 60:.1f}분 |")
    (ROOT / "anim" / "storyboard_anim.md").write_text("\n".join(head + body) + "\n", encoding="utf-8")
    (ROOT / "anim" / "sound_cues.md").write_text("\n".join(cues) + "\n", encoding="utf-8")
    print(f"→ anim/storyboard_anim.md, anim/sound_cues.md (총 {tot / 60:.1f}분)")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "build":
        sys.exit(build())
    args = [Path(p) for p in sys.argv[2:]] or sorted(PARTS.glob("*.md"))
    _, e = check(args, not sys.argv[2:])
    sys.exit(1 if e else 0)
