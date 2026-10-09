"""배경 시안 점검·GPT 프롬프트 생성 (표준 라이브러리만).

  python tools/sets.py           # 점검 후 design/sets.json → design/gen/set_prompts.md
  python tools/sets.py --check   # 점검만

점검: sets.json 필수 칸, 8절 장소 이름·영어 기준 문장(글자 그대로 첫머리), 8절 모든 행이 쓰였는지,
scene_presets.json 80씬이 모두 어느 장소에 배정됐는지, 장소마다 씬이 하나 이상인지,
프리셋 prompt_scene 속 8절 문장으로 자동 추정한 배정과의 차이(경고), '같은 구도' 문장 일치.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQ = ["id", "name", "section8", "scenes", "size_m", "layout_text_en", "base_time",
       "light_by_time", "variants", "camera_spots", "fixed_props"]
FRAME = ("Fixed framing: seen from the mainland end of the embankment road looking north toward the island, "
         "the {way} running straight away from the viewer across the low reed flats to the island, "
         "the small flat-topped hill on the left (west) and the bigger flat-topped hill on the right (east), "
         "the Han River opening on the far left.")
FRAME_SETS = {"dyke_road_to_island": "road", "island_after": "road", "park_2003_view": "wide walking path"}


def section8():
    """style_guide.md 8절 표 → {장소 이름: 영어 기준 문장}. '(… 문장 뒤에)'는 앞 문장을 이어 붙인다."""
    s = (ROOT / "design" / "style_guide.md").read_text(encoding="utf-8")
    body = s.split("## 8.", 1)[1]
    rows = {}
    for line in body.splitlines():
        m = re.match(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$", line)
        if not m or m.group(1) in ("장소", "---") or set(m.group(1)) <= set("-"):
            continue
        rows[m.group(1)] = m.group(2)
    for k, v in list(rows.items()):
        m = re.match(r"^\((.+?) 문장 뒤에\)\s*(.+)$", v)
        if m:
            base = next(n for n in rows if n.startswith(m.group(1)))
            rows[k] = rows[base] + ", " + m.group(2)
    return rows


def style_bits():
    st = json.loads((ROOT / "design" / "style.json").read_text(encoding="utf-8"))
    style = re.sub(r",\s*vertical webtoon panel", "", st["prompt_style"])
    return style + ", wide background establishing art, no people", st["prompt_negative"]


def check(sets, rows, presets):
    errs, warns = [], []
    ids = [x.get("id") for x in sets]
    if len(ids) != len(set(ids)):
        errs.append("id 중복")
    for x in sets:
        for k in REQ:
            if k not in x:
                errs.append(f"{x.get('id')}: '{k}' 없음")
        if not re.fullmatch(r"[a-z0-9_]+", x.get("id", "")):
            errs.append(f"{x.get('id')}: id는 영문 소문자·숫자·_ 만")
        if x.get("section8") not in rows:
            errs.append(f"{x['id']}: section8 '{x.get('section8')}'가 8절 표에 없음")
        elif not x["layout_text_en"].startswith(rows[x["section8"]]):
            errs.append(f"{x['id']}: layout_text_en이 8절 문장으로 시작하지 않음")
        lt = x.get("light_by_time", {})
        if x.get("base_time") not in lt:
            errs.append(f"{x['id']}: base_time '{x.get('base_time')}'이 light_by_time에 없음")
        for v in x.get("variants", []):
            if v not in lt:
                errs.append(f"{x['id']}: 변형 '{v}'이 light_by_time에 없음")
        for t, txt in lt.items():
            for h in re.findall(r"#[0-9A-Fa-f]+", txt):
                if not re.fullmatch(r"#[0-9A-Fa-f]{6}", h):
                    errs.append(f"{x['id']}.{t}: HEX 형식 {h}")
        if not x.get("scenes"):
            errs.append(f"{x['id']}: 씬 없음")
        for c in x.get("camera_spots", []):
            for sc in c.get("scenes", []):
                if sc not in x["scenes"] and sc not in {s for y in sets for s in y["scenes"]}:
                    warns.append(f"{x['id']}.{c['id']}: 카메라 씬 {sc}가 어느 장소에도 없음")
        if x["id"] in FRAME_SETS and FRAME.format(way=FRAME_SETS[x["id"]]) not in x["layout_text_en"]:
            errs.append(f"{x['id']}: '같은 구도' 문장이 다름")
    used = {x["section8"] for x in sets}
    for r in rows:
        if r not in used:
            errs.append(f"8절 '{r}'에 해당하는 장소 없음")
    all_sc = [p["scene"] for p in presets]
    assigned = {}
    for x in sets:
        for sc in x["scenes"]:
            if sc not in all_sc:
                errs.append(f"{x['id']}: 씬 {sc}가 scene_presets.json에 없음")
            assigned.setdefault(sc, []).append(x["id"])
    missing = [sc for sc in all_sc if sc not in assigned]
    if missing:
        errs.append("장소가 배정되지 않은 씬: " + ", ".join(missing))
    # 프리셋 prompt_scene에 들어 있는 8절 문장으로 자동 추정한 배정과 비교
    by_row = {}
    for x in sets:
        by_row.setdefault(x["section8"], set()).update(x["scenes"])
    keys = {}
    for r, sent in rows.items():
        base = next((o for o, s2 in rows.items() if o != r and sent.startswith(s2)), None)
        keys[r] = (sent[len(rows[base]):].strip(", ") if base else sent).split(":")[0]
    for p in presets:
        hit = {r for r, k in keys.items() if k in p["prompt_scene"]}
        hit -= {o for r in hit for o in rows if o != r and rows[r].startswith(rows[o])}
        for r in hit:
            if p["scene"] not in by_row.get(r, set()):
                warns.append(f"{p['scene']}: 프리셋 문장에 8절 '{r}'가 있으나 그 장소의 scenes에 없음")
    return errs, warns, assigned, all_sc


def build(sets, assigned):
    style, neg = style_bits()
    out = ["# 배경 시안 GPT 프롬프트 — 깡통 바이올린",
           "",
           "1. 장소마다 ① 기준 배경을 먼저 만들어 `renders/sets/<set_id>.png`로 저장한다(변형은 `renders/sets/<set_id>__<시간>.png`).",
           "2. 컷을 생성할 때 그 장소의 기준 배경(시간대가 맞으면 변형)을 참고 이미지로 함께 올리고, 컷 프롬프트에 '같은 배치 유지(same layout as the reference)'를 붙인다.",
           "3. 배치·근거·카메라 자리는 `design/sets.md`, 기계용 원본은 `design/sets.json`. 이 문서는 `python tools/sets.py`로 만든다(직접 고치지 말 것).",
           ""]
    for x in sets:
        out += [f"### [{x['id']}] {x['name']} — {', '.join(x['scenes'])}", ""]
        cams = " / ".join(f"{c['id']}: {c['ko']}" for c in x["camera_spots"])
        out += [f"- 8절: {x['section8']} · 크기: {x['size_m']}", f"- 카메라 자리: {cams}", ""]
        out += [f"① 기준 배경 (`{x['base_time']}`) → `renders/sets/{x['id']}.png`", "", "```",
                f"{x['layout_text_en']}. Lighting: {x['light_by_time'][x['base_time']]}. "
                f"Style: {style}. {neg}", "```", ""]
        for i, v in enumerate(x["variants"]):
            out += [f"{'②③④'[i]} 변형 (`{v}`) → `renders/sets/{x['id']}__{v}.png` — 같은 배치, 빛만 다름", "", "```",
                    f"{x['layout_text_en']}. Lighting: {x['light_by_time'][v]}. Style: {style}. {neg}", "```", ""]
    (ROOT / "design" / "gen").mkdir(exist_ok=True)
    (ROOT / "design" / "gen" / "set_prompts.md").write_text("\n".join(out), encoding="utf-8")


def main():
    sets = json.loads((ROOT / "design" / "sets.json").read_text(encoding="utf-8"))
    presets = json.loads((ROOT / "design" / "scene_presets.json").read_text(encoding="utf-8"))
    rows = section8()
    errs, warns, assigned, all_sc = check(sets, rows, presets)
    print(f"장소 {len(sets)}개, 8절 행 {len(rows)}개, 씬 {len(all_sc)}개 중 배정 {len([s for s in all_sc if s in assigned])}개")
    for w in warns:
        print("경고:", w)
    for e in errs:
        print("오류:", e)
    if errs:
        sys.exit(1)
    if "--check" not in sys.argv:
        build(sets, assigned)
        print("→ design/gen/set_prompts.md")


if __name__ == "__main__":
    main()
