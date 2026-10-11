"""G9 콘티 조각 점검 (표준 라이브러리만).

  python tools/sb_check.py storyboard/parts/ep1.md --ep 1 --scenes 1-17 [--spec storyboard/source/cut_spec_ep1.jsonl]

- 대본(story/script.md) 해당 씬의 대사·내레이션이 콘티 대사 칸에 글자 그대로 있는지(연기 메모 괄호는 뺀다)
- 5열 표 형식, 컷 번호 연속, 칸 안 '|' 금지, 장면 소제목의 S# 범위
- 컷당 말풍선 수(대사·생각·속삭임·내레이션) 3개 초과 경고
- 컷 사양(jsonl): 콘티 컷과 1:1, scene이 장면 S#와 맞는지, 소리 색은 씬 프리셋에 소리 색 순간이 있는 씬에만
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ID_RE = re.compile(r"^(\d+)-(\d{3})$")


def script_lines(ep, lo, hi):
    t = (ROOT / "story" / "script.md").read_text(encoding="utf-8")
    parts = re.split(r"\n(?=## )", t)
    body = next(p for p in parts if re.match(rf"## {ep}화", p))
    out = []
    for sc in re.split(r"\n(?=S#\d+\.)", body)[1:]:
        n = int(re.match(r"S#(\d+)", sc).group(1))
        if not lo <= n <= hi:
            continue
        for l in sc.splitlines():
            m = re.match(r"^([^\s#|`\-][^\t]{0,14})\t(.*)$", l)
            if not m:
                continue
            txt = m.group(2).strip()
            txt = re.sub(r"^(\([^)]*\)\s*)+", "", txt).strip()
            if txt:
                out.append((n, m.group(1).strip(), txt))
    return out


def norm(s):
    return re.sub(r"\s+", "", s).replace("...", "…")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("md")
    ap.add_argument("--ep", type=int, required=True)
    ap.add_argument("--scenes", required=True, help="예: 1-17")
    ap.add_argument("--spec")
    a = ap.parse_args()
    lo, hi = map(int, a.scenes.split("-"))
    md = Path(a.md).read_text(encoding="utf-8")
    errs, warns = [], []
    cuts, scene_of, cur = [], {}, None
    in_ep = not re.search(r"^### \d+화", md, re.M)  # 화 제목이 없는 조각(ep3b)은 전부 대상
    for i, line in enumerate(md.splitlines(), 1):
        s = line.strip()
        if s.startswith("### "):
            in_ep = bool(re.match(rf"### {a.ep}화", s))
            continue
        if s.startswith("## "):
            in_ep = False if s.startswith("## 작업 메모") else in_ep
            continue
        if not in_ep:
            continue
        if s.startswith("#### "):
            m = re.search(r"S(\d+)", s)
            cur = int(m.group(1)) if m else None
            if cur is None:
                errs.append(f"{i}: 장면 소제목에 S# 없음: {s}")
            elif not lo <= cur <= hi:
                errs.append(f"{i}: 범위 밖 S#{cur}")
            continue
        if not s.startswith("|") or s.startswith("|---") or s.startswith("| 컷"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) != 5:
            errs.append(f"{i}: 칸 수 {len(cells)} (5여야 함, 칸 안 '|' 금지)")
            continue
        if not ID_RE.match(cells[0]):
            errs.append(f"{i}: 컷 번호 형식 {cells[0]}")
            continue
        if not re.match(r"^800×\d+$", cells[1]):
            warns.append(f"{cells[0]}: 크기 형식 {cells[1]}")
        cuts.append(cells)
        scene_of[cells[0]] = cur
    ids = [c[0] for c in cuts]
    for x, y in zip(ids, ids[1:]):
        if int(y.split("-")[1]) != int(x.split("-")[1]) + 1:
            errs.append(f"번호 불연속: {x} → {y}")
    alltext = norm(" ".join(c[4] for c in cuts))
    miss = [(n, sp, t) for n, sp, t in script_lines(a.ep, lo, hi) if norm(t) not in alltext]
    for n, sp, t in miss:
        errs.append(f"대사 누락/변형 S#{n} {sp}: {t}")
    for c in cuts:
        bubbles = [p for p in re.split(r"\s+/\s+", c[4]) if p and not re.match(r"^(SFX|제목|자막|손글씨|고지문|간판|TXT)", p) and p != "(무음)"]
        if len(bubbles) > 3:
            warns.append(f"{c[0]}: 말풍선 {len(bubbles)}개(3 초과 — 규격 예외인지 확인)")
    n_lines = len(script_lines(a.ep, lo, hi))
    print(f"컷 {len(cuts)} · 대본 대사 {n_lines}줄 · 누락 {len(miss)}")
    if a.spec:
        presets = {p["scene"]: p for p in json.loads((ROOT / "design" / "scene_presets.json").read_text(encoding="utf-8"))}
        spec = {}
        for k, l in enumerate(Path(a.spec).read_text(encoding="utf-8").splitlines(), 1):
            if not l.strip():
                continue
            try:
                d = json.loads(l)
            except json.JSONDecodeError as e:
                errs.append(f"사양 {k}행 JSON 오류: {e}")
                continue
            spec[d.get("id")] = d
        for cid in ids:
            d = spec.get(cid)
            if not d:
                errs.append(f"사양 없음: {cid}")
                continue
            want = f"{a.ep}-{scene_of.get(cid)}"
            if d.get("scene") != want:
                errs.append(f"{cid}: 사양 scene {d.get('scene')} ≠ 장면 {want}")
            if not d.get("cut_en"):
                errs.append(f"{cid}: cut_en 없음")
            if d.get("sound") and not presets.get(d.get("scene"), {}).get("sound_color"):
                warns.append(f"{cid}: 소리 색 순간이 없는 씬에서 sound 사용")
            c = next(x for x in cuts if x[0] == cid)
            if d.get("sound") and "SFX(" not in c[4] and "M:" not in c[3] and "음악" not in c[3]:
                warns.append(f"{cid}: sound가 있는데 콘티에 소리 색 SFX·음악 표기가 없음")
        for cid in spec:
            if cid not in ids:
                errs.append(f"사양만 있고 콘티에 없는 컷: {cid}")
    for e in errs:
        print("[오류]", e)
    for w in warns:
        print("[주의]", w)
    print("통과" if not errs else f"오류 {len(errs)}건")


if __name__ == "__main__":
    main()
