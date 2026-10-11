"""G9 작가용 씬 색인: 씬마다 인물·의상·배경(카메라 자리)·소품(상태 키)·소리 색 순간을 한 곳에.

  python tools/scene_index.py   →  storyboard/source/scene_index.md
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def jl(p):
    return json.loads((ROOT / p).read_text(encoding="utf-8"))


presets, sets, props = jl("design/scene_presets.json"), jl("design/sets.json"), jl("design/props.json")
out = ["# 씬 색인 (G9 콘티·컷 사양 작성용, tools/scene_index.py로 생성)", "",
       "컷 사양(cut_spec)의 `scene`·`set`·`spot`·`props`·`sound`는 아래 id를 그대로 쓴다. 소품은 상태 키가 있으면 그 씬에 맞는 상태 키를 쓴다.", ""]
for p in presets:
    sc = p["scene"]
    out.append(f"## {sc} {p['location']} ({p['time']})")
    out.append(f"- 빛: {p['light']}")
    out.append("- 인물·의상: " + "; ".join(f"{c['id']}={c.get('outfit','')}" for c in p["characters"]))
    for s in sets:
        if sc in s["scenes"]:
            spots = [f"`{c['id']}`({c['ko']})" for c in s.get("camera_spots", []) if sc in c.get("scenes", [])]
            other = [f"`{c['id']}`" for c in s.get("camera_spots", []) if sc not in c.get("scenes", [])]
            out.append(f"- 배경 `{s['id']}` {s['name']} — 이 씬 카메라 자리: {', '.join(spots) or '없음'}" + (f" / 그 밖: {', '.join(other)}" if other else ""))
    ps = []
    for pr in props:
        st = [x for x in (pr.get("states") or []) if sc in x.get("scenes", [])]
        if st:
            ps += [f"`{x['key']}`({pr['name']}·{x['label']})" for x in st]
        elif sc in pr.get("scenes", []):
            ps.append(f"`{pr['id']}`({pr['name']})")
    out.append(f"- 소품: {', '.join(ps) or '없음'}")
    if p.get("sound_color"):
        out.append(f"- 소리 색 순간(이 컷들에만): {' / '.join(p['sound_color'])}")
    out.append("")
(ROOT / "storyboard" / "source" / "scene_index.md").write_text("\n".join(out), encoding="utf-8")
print("scene_index.md", len(presets), "씬")
