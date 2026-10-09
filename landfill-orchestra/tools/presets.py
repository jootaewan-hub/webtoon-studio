"""씬 프리셋 합치기·점검 (표준 라이브러리만).

  python tools/presets.py   # design/_presets_ep12.json + _presets_ep3.json → design/scene_presets.json, scene_presets.md

점검: 대본 S# 전부 있는지, 씬 머리(장소·시간)가 대본과 같은지, HEX 형식, 필수 칸.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQ = ["scene", "location", "time", "date", "season_weather", "light", "key_hex", "shadow_hex",
       "characters", "sound_color", "prompt_scene"]
HEX = re.compile(r"^#[0-9A-Fa-f]{6}$")


def script_scenes():
    s = (ROOT / "story" / "script.md").read_text(encoding="utf-8")
    out = {}
    for ch in re.split(r"^## (?=\d화)", s, flags=re.M)[1:]:
        ep = ch[0]
        for m in re.finditer(r"^S#(\d+)\. (.+?) \((.+)\)\s*$", ch.split("\n## 변경 기록")[0], re.M):
            out[f"{ep}-{m.group(1)}"] = (m.group(2).strip(), m.group(3).strip())
    return out


def main():
    items = []
    for name in ("_presets_ep12.json", "_presets_ep3.json"):
        items += json.loads((ROOT / "design" / name).read_text(encoding="utf-8"))
    want = script_scenes()
    problems = []
    got = {}
    for it in items:
        sc = it.get("scene")
        got[sc] = it
        for k in REQ:
            if k not in it or it[k] in ("", None):
                problems.append(f"{sc}: '{k}' 없음")
        for k in ("key_hex", "shadow_hex"):
            if k in it and not HEX.match(str(it[k])):
                problems.append(f"{sc}: {k} 형식 {it[k]}")
        if sc in want:
            loc, tm = want[sc]
            if it.get("location") != loc or it.get("time") != tm:
                problems.append(f"{sc}: 씬 머리 불일치 — 대본 '{loc} ({tm})' / 프리셋 '{it.get('location')} ({it.get('time')})'")
    for sc in want:
        if sc not in got:
            problems.append(f"{sc}: 프리셋 없음")
    for sc in got:
        if sc not in want:
            problems.append(f"{sc}: 대본에 없는 씬")

    def key(sc):
        e, n = sc.split("-")
        return int(e), int(n)
    items = [got[sc] for sc in sorted(got, key=key)]
    (ROOT / "design" / "scene_presets.json").write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")

    md = ["# 씬 프리셋 — 「깡통 바이올린」", "",
          "대본 S#마다 이미지 프롬프트 [SCENE] 칸에 붙일 빛·색·의상. 규칙은 `design/style_guide.md`, 기계용 원본은 `design/scene_presets.json`(이 문서는 거기서 만든다: `python tools/presets.py`).", ""]
    ep = None
    for it in items:
        e = it["scene"].split("-")[0]
        if e != ep:
            ep = e
            md += [f"## {e}화", ""]
        chars = "; ".join(f"{c.get('id')}: {c.get('outfit', '')}" + (f" ({c['note']})" if c.get("note") else "") for c in it.get("characters", []))
        md += [f"### {it['scene']} {it['location']} ({it['time']})", "",
               f"- 때: {it['date']} · {it['season_weather']}",
               f"- 빛: {it['light']}",
               f"- 색: 주조 {it['key_hex']} · 그림자 {it['shadow_hex']} · 보조 {' '.join(it.get('palette', []))}",
               f"- 인물·의상: {chars or '없음'}",
               f"- 소품: {', '.join(it.get('props', [])) or '—'}",
               f"- 소리 색: {' / '.join(it['sound_color']) or '없음'}",
               f"- 분위기: {it.get('mood', '')}",
               f"- 연속성: {it.get('continuity', '')}",
               "", "```", it["prompt_scene"], "```", ""]
    (ROOT / "design" / "scene_presets.md").write_text("\n".join(md), encoding="utf-8")
    print(f"씬 {len(items)}개 / 대본 {len(want)}개")
    print("\n".join(problems) if problems else "문제 없음")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
