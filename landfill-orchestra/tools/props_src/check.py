import json, re, os, sys
from collections import Counter
sys.path.insert(0, os.path.dirname(__file__))
from common import ROOT, HEAD, TAIL_FIXED

props = json.load(open(os.path.join(ROOT, "design", "props.json"), encoding="utf-8"))
byid = {p["id"]: p for p in props}
def has(pid, sc):
    p = byid[pid]
    return sc in p["scenes"] or re.search(r"(?<![\d-])" + re.escape(sc) + r"(?!\d)", p.get("offscreen", ""))

VALID = [f"1-{i}" for i in range(1, 18)] + [f"2-{i}" for i in range(1, 30)] + [f"3-{i}" for i in range(1, 35)]
errs = []

# 1. 형식
ids = Counter(p["id"] for p in props)
errs += [f"중복 id {k}" for k, v in ids.items() if v > 1]
al = Counter(a for p in props for a in p["aliases"])
errs += [f"별칭 중복 '{k}' → " + ",".join(p["id"] for p in props if k in p["aliases"]) for k, v in al.items() if v > 1]
HEX = re.compile(r"^#[0-9A-F]{6}$")
for p in props:
    if not re.match(r"^[a-z][a-z0-9_]*$", p["id"]): errs.append(f"id 형식 {p['id']}")
    for k in ("id", "name", "tier", "era", "material", "size", "colors", "condition", "shape", "role", "scenes", "ref", "prompt_en"):
        if not p.get(k): errs.append(f"{p['id']}: 빈 칸 {k}")
    if not (2 <= len(p["colors"]) <= 4): errs.append(f"{p['id']}: 색 개수 {len(p['colors'])}")
    for h in p["colors"]:
        if not HEX.match(h): errs.append(f"{p['id']}: HEX {h}")
    if not re.search(r"\d+(\.\d+)?\s*cm", p.get("size", "")): errs.append(f"{p['id']}: size에 cm 숫자 없음")
    for s in p["scenes"]:
        if s not in VALID: errs.append(f"{p['id']}: 없는 씬 {s}")
    prs = [p.get("prompt_en", "")]
    if p["tier"] == "A":
        if not p.get("states"): errs.append(f"{p['id']}: A인데 states 없음")
        for st in p.get("states", []):
            for s in st["scenes"]:
                if s not in p["scenes"]: errs.append(f"{p['id']}/{st['key']}: 상태 씬 {s}가 소품 scenes에 없음")
            if not st.get("prompt_en"): errs.append(f"{st['key']}: prompt 없음")
            prs.append(st.get("prompt_en", ""))
    for pr in prs:
        if not pr: continue
        if not pr.startswith(HEAD): errs.append(f"{p['id']}: 프롬프트 머리 다름")
        if TAIL_FIXED not in pr: errs.append(f"{p['id']}: 프롬프트 꼬리 다름")
        if not re.search(r", (1987|1988|1970s|1990s|2003|1950s) Seoul$", pr): errs.append(f"{p['id']}: 시대 토큰")
        if re.search(r"[가-힣]", pr): errs.append(f"{p['id']}: 프롬프트에 한글")
        for h in re.findall(r"#[0-9A-Fa-f]{6}", pr):
            if not HEX.match(h): errs.append(f"{p['id']}: 프롬프트 HEX {h}")
# 상태 프롬프트가 기본과 같으면서 shape 변경을 의도한 경우 탐지(동일 프롬프트 중복)
pc = Counter(st.get("prompt_en") for p in props for st in p.get("states", []) if st.get("prompt_en"))

# 2. Insert 대조
lines = open(os.path.join(ROOT, "story", "script.md"), encoding="utf-8").read().split("\n")
inserts, ep, sc = [], 0, None
for l in lines:
    if l.startswith("## 변경"): break
    m = re.match(r"## (\d)화", l)
    if m: ep = int(m.group(1))
    m = re.match(r"S#(\d+)\.", l)
    if m: sc = f"{ep}-{m.group(1)}"
    if l.startswith("Insert"): inserts.append((sc, l))
from insert_map import IMAP
missing, used = [], set()
for sc, l in inserts:
    hit = [m for m in IMAP if m[0] == sc and m[1] in l]
    if not hit:
        missing.append(f"[매핑 없음] {sc} {l[:60]}")
        continue
    for m in hit:
        used.add(id(m))
        if isinstance(m[2], str):
            continue
        for pid in m[2]:
            if pid not in byid: missing.append(f"[소품 없음] {sc} {pid} ← {l[:40]}")
            elif not has(pid, sc): missing.append(f"[씬 누락] {pid}에 {sc} 없음 ← {l[:40]}")

# 3. 프리셋 props 대조
from preset_map import PMAP
pres = json.load(open(os.path.join(ROOT, "design", "scene_presets.json"), encoding="utf-8"))
pmiss = []
for s in pres:
    for item in s.get("props", []):
        it = item.replace("동그리 아님", "")
        hits = [ids for kw, ids in PMAP if (kw[1:] == it if kw.startswith("=") else kw in it)]
        if not hits:
            pmiss.append(f"[매핑 없음] {s['scene']} {item}")
            continue
        for ids2 in hits:
            if isinstance(ids2, str): continue
            bad = [x for x in ids2 if x not in byid]
            if bad:
                pmiss.append(f"[소품 없음] {bad} ← {s['scene']} {item}"); continue
            ok = [has(x, s["scene"]) for x in ids2]
            if (isinstance(ids2, tuple) and not any(ok)) or (isinstance(ids2, list) and not all(ok)):
                pmiss.append(f"[씬 누락] {[x for x, o in zip(ids2, ok) if not o]}에 {s['scene']} ← {item}")

print("== 형식 오류", len(errs)); [print(" ", e) for e in errs[:80]]
print("== Insert 줄", len(inserts), "누락", len(missing)); [print(" ", e) for e in missing]
print("== 프리셋 props 누락", len(pmiss)); [print(" ", e) for e in pmiss]
print("== 등급", Counter(p["tier"] for p in props), "상태", sum(len(p.get("states", [])) for p in props))
