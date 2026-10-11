"""G12 인계 패키지 도구 (표준 라이브러리만).

  python3 tools/handoff.py manifest   → handoff/asset_manifest.csv (그릴 그림 전부: 인물 시트·소품·배경·컷, status=todo)
  python3 tools/handoff.py check      → 패키지에 넣을 정본 파일이 모두 있는지, 대장의 프롬프트 참조가 실제 제목과 맞는지
  python3 tools/handoff.py pack       → five-doors와 같은 방식으로 dist/landfill_handoff_<날짜>.zip

정본 파일은 복사하지 않는다. zip 안에서도 프로젝트와 같은 경로(landfill-orchestra/…)에 둔다.
작업용 조각(story/direction_parts, anim/parts), 검수 보고서(review), 킷 참고 출력(storyboard/outputs), 도구(tools)는 넣지 않는다.
"""
import csv
import datetime
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = ROOT.name
DIST = ROOT / "dist"

# zip에 넣을 정본(파일 또는 폴더)
INCLUDE = [
    "handoff",
    "decisions.md", "project.md",
    "source/original.md",
    "research/notes.md",
    "story/pitch.md", "story/bible.md", "story/synopsis.md", "story/beats.md", "story/continuity.md",
    "story/novel.md", "story/script.md", "story/script_format.md",
    "story/direction.md", "story/sfx_list.md", "story/era_terms_research.md",
    "design/style_guide.md", "design/style.json", "design/style_options.md", "design/style",
    "design/characters.json", "design/outfit_schedule.json", "design/outfits_en.json", "design/sheets",
    "design/scene_presets.md", "design/scene_presets.json",
    "design/props.md", "design/props.json", "design/sets.md", "design/sets.json",
    "design/colorscript.svg", "design/costume_research.md", "design/gen",
    "storyboard/README.md", "storyboard/SPEC.md",
    "storyboard/source/storyboard.md", "storyboard/source/storyboard.docx",
    "storyboard/source/cut_spec_ep1.jsonl", "storyboard/source/cut_spec_ep2.jsonl", "storyboard/source/cut_spec_ep3.jsonl",
    "storyboard/source/scene_index.md",
    "storyboard/out/cel", "storyboard/thumbs", "storyboard/tools/board.html", "storyboard/tools/editor_ready.html",
    "anim/storyboard_anim.md", "anim/sound_cues.md", "anim/cut_shots.md",
    "docx",
]
SKIP_DIRS = {"__pycache__", "node_modules", ".git"}


def files():
    out = []
    for p in INCLUDE:
        q = ROOT / p
        if q.is_dir():
            out += sorted(x for x in q.rglob("*") if x.is_file() and not SKIP_DIRS & set(x.parts) and not x.name.startswith("."))
        elif q.exists():
            out.append(q)
    return out


def headings(md, level):
    t = (ROOT / md).read_text(encoding="utf-8")
    return re.findall(rf"^{'#' * level} (.+)$", t, re.M)


def manifest():
    rows = []
    # 인물: ## 이름 (id) 아래 ### ①… 시트
    t = (ROOT / "design/gen/character_prompts.md").read_text(encoding="utf-8")
    cur = None
    for line in t.splitlines():
        m = re.match(r"^## (.+?) \(([a-z_]+)\)", line)
        if m:
            cur = (m.group(1), m.group(2))
            continue
        m = re.match(r"^### (.+)$", line)
        if m and cur:
            title = m.group(1).strip()
            var = {"①": "turnaround", "②": "expressions", "③": "outfits", "④": "2003", "⑤": "flashback"}.get(title[0], re.sub(r"\W+", "_", title)[:20])
            rows.append({"file": f"renders/characters/{cur[1]}_{var}.png", "kind": "character", "subject": cur[1], "variant": var,
                         "order": "1", "prompt_ref": f"design/gen/character_prompts.md#{cur[0]} > {title}"})
    # 소품: ## A 핵심 / B 반복 / C 디테일 아래 ### [id]
    grp = None
    for line in (ROOT / "design/gen/prop_prompts.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## ([ABC]) ", line)
        if m:
            grp = m.group(1)
        m = re.match(r"^### \[([^\]]+)\]", line)
        if m:
            rows.append({"file": f"renders/props/{m.group(1)}.png", "kind": "prop", "subject": m.group(1), "variant": grp or "",
                         "order": {"A": "2", "B": "3", "C": "4"}.get(grp, "4"), "prompt_ref": f"design/gen/prop_prompts.md#[{m.group(1)}]"})
    for line in (ROOT / "design/gen/set_prompts.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^### \[([^\]]+)\]", line)
        if m:
            rows.append({"file": f"renders/sets/{m.group(1)}.png", "kind": "set", "subject": m.group(1), "variant": "",
                         "order": "5", "prompt_ref": f"design/gen/set_prompts.md#[{m.group(1)}]"})
    big = set()
    for l in (ROOT / "storyboard/out/cel/cel_prompts.jsonl").read_text(encoding="utf-8").splitlines():
        x = json.loads(l)
        if len(x["prompt"]) > 6000:
            big.add(x["id"])
        rows.append({"file": f"storyboard/renders/cel/{x['id']}.png", "kind": "cel", "subject": x["id"], "variant": f"{x['size'][0]}x{x['size'][1]}",
                     "order": f"6-{x['id'][0]}", "prompt_ref": f"storyboard/out/cel/{x['id']}.md",
                     "notes": "참고 이미지 필수(프롬프트 6천 자 이상 합주 컷)" if len(x["prompt"]) > 6000 else ""})
    out = ROOT / "handoff" / "asset_manifest.csv"
    out.parent.mkdir(exist_ok=True)
    cols = ["file", "kind", "subject", "variant", "order", "prompt_ref", "tool", "status", "approved_by", "notes"]
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({**{c: "" for c in cols}, "tool": "ChatGPT", "status": "todo", **r})
    kinds = {}
    for r in rows:
        kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
    print(f"→ {out} ({len(rows)}줄: {kinds}, 참고 이미지 필수 컷 {len(big)})")


def check():
    probs = []
    for p in INCLUDE:
        if not (ROOT / p).exists():
            probs.append(f"없는 정본: {p}")
    man = ROOT / "handoff" / "asset_manifest.csv"
    if man.exists():
        for r in csv.DictReader(man.open(encoding="utf-8-sig")):
            ref = r["prompt_ref"]
            path = ref.split("#")[0]
            if not (ROOT / path).exists():
                probs.append(f"대장 참조 파일 없음: {ref}")
    else:
        probs.append("handoff/asset_manifest.csv 없음(manifest 먼저)")
    for md in (ROOT / "handoff").glob("*.md"):
        for ref in re.findall(r"`((?:story|design|storyboard|anim|docx|research|source)/[^`*<>|]+?)`", md.read_text(encoding="utf-8")):
            ref = ref.split("#")[0].split(" ")[0].rstrip("/")
            if not any(ch in ref for ch in "*{<") and not (ROOT / ref).exists() and not ref.startswith(("storyboard/renders", "renders")):
                probs.append(f"{md.name}: 없는 경로 `{ref}`")
    fs = files()
    size = sum(f.stat().st_size for f in fs)
    for p in probs:
        print("[문제]", p)
    print(f"정본 {len(fs)}개 · {size / 1e6:.1f}MB · 문제 {len(probs)}")
    return 1 if probs else 0


def pack():
    if check():
        print("문제가 있어 묶지 않는다.")
        return 1
    DIST.mkdir(exist_ok=True)
    out = DIST / f"landfill_handoff_{datetime.date.today():%Y-%m-%d}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files():
            z.write(f, f"{NAME}/{f.relative_to(ROOT)}")
    print(f"→ {out} ({out.stat().st_size / 1e6:.1f}MB)")
    return 0


if __name__ == "__main__":
    sys.exit({"manifest": manifest, "check": check, "pack": pack}[sys.argv[1] if len(sys.argv) > 1 else "check"]() or 0)
