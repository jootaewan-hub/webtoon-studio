#!/usr/bin/env python3
"""효과음(SFX) 사전 도구 (G10).

  python3 sfx_tools.py extract [--dir <프로젝트>]            # storyboard/data/cuts.json → research/sfx_raw.json (표기별 컷·크기·글꼴)
  python3 sfx_tools.py apply <통일.json> [--dir <프로젝트>]   # 표기 통일을 웹툰 콘티(storyboard/parts)와 애니 콘티(anim/parts)에 반영

통일.json 형식: [{"cut": "3-078", "from": "지잉", "to": "징—", "why": "휴대폰 진동"},
                {"cut": "5-035", "spec": ["중간, 적색", "중간, 버건디"], "text": "하하하", "why": "웃음은 인물 색"}]
- from은 그 컷 대사 칸의 SFX 문자열과 글자 그대로 일치해야 한다. spec은 SFX 괄호(크기·색)만 바꾼다.
- 반영 뒤에는 kit.py import → direction_scenes.py → anim_tools.py merge·cues 를 다시 돌린다.
표준 라이브러리만 쓴다.
"""
import argparse, json, re
from collections import OrderedDict, Counter
from pathlib import Path


def extract(P):
    cuts = json.loads((P / "storyboard/data/cuts.json").read_text(encoding="utf-8"))
    sfx = OrderedDict()
    for c in cuts:
        font = ("코미디 고딕(Black Han Sans)" if ("[트랙2]" in c["screen"] or "Black Han Sans" in c["screen"])
                else ("붓(East Sea Dokdo)" if "East Sea Dokdo" in c["screen"] else "?"))
        for l in c["lines"]:
            if l["type"] != "sfx":
                continue
            spec = re.search(r"\((.*?)\)", l["speaker"]); spec = spec.group(1) if spec else ""
            txt = re.sub(r"\s+", " ", l["text"]).strip()
            key = re.sub(r"[.!…—\-~ ,]", "", txt)
            d = sfx.setdefault(key, {"text": txt, "cuts": [], "specs": Counter(), "fonts": Counter()})
            d["cuts"].append(c["id"]); d["specs"][spec] += 1; d["fonts"][font] += 1
    out = P / "research/sfx_raw.json"; out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps({k: {**v, "specs": dict(v["specs"]), "fonts": dict(v["fonts"])} for k, v in sfx.items()},
                              ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"효과음 표기 {len(sfx)}종 / 사용 {sum(len(d['cuts']) for d in sfx.values())}회 → {out}")


def apply(P, mapping):
    N = json.loads(Path(mapping).read_text(encoding="utf-8"))
    log = []
    for n in N:
        ep = n["cut"].split("-")[0]
        ep = "1" if ep == "0" else ep
        p = P / f"storyboard/parts/ep{ep}.md"
        L = p.read_text(encoding="utf-8").split("\n")
        for i, ln in enumerate(L):
            if not ln.startswith(f"| {n['cut']} |"):
                continue
            cells = ln.split("|"); lines = cells[5]
            if n.get("spec"):
                a, b = n["spec"]
                old = f"SFX({a}): {n.get('text', '')}"
                if old in lines:
                    lines = lines.replace(old, f"SFX({b}): {n.get('text', '')}", 1); log.append(f"콘티 {n['cut']} 크기·색")
                else:
                    log.append(f"!! 콘티 {n['cut']} '{old}' 없음")
            else:
                pat = re.compile(r"(SFX(?:\([^)]*\))?:\s*)" + re.escape(n["from"]) + r"(?=\s*(?:/|$))")
                lines, k = pat.subn(lambda m: m.group(1) + n["to"], lines, count=1)
                log.append(f"콘티 {n['cut']} {'수정' if k else '!! 못 찾음'}")
            cells[5] = lines; L[i] = "|".join(cells); break
        p.write_text("\n".join(L), encoding="utf-8")
        if n.get("spec"):
            continue
        ap = P / f"anim/parts/ep{ep}.md"
        if ap.exists():
            A = ap.read_text(encoding="utf-8").split("\n"); k = 0
            for i, ln in enumerate(A):
                if ln.startswith("|") and f"| {n['cut']}" in ln:
                    cells = ln.split("|")
                    if len(cells) >= 12 and n["from"] in cells[7]:
                        cells[7] = cells[7].replace(n["from"], n["to"]); A[i] = "|".join(cells); k += 1
            ap.write_text("\n".join(A), encoding="utf-8"); log.append(f"애니 {n['cut']} {k}행")
    print("\n".join(log))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["extract", "apply"]); ap.add_argument("mapping", nargs="?")
    ap.add_argument("--dir", default=str(Path(__file__).resolve().parent.parent))
    a = ap.parse_args(); P = Path(a.dir)
    extract(P) if a.cmd == "extract" else apply(P, a.mapping)


if __name__ == "__main__":
    main()
