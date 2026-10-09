"""컷 하나의 이미지 프롬프트 조립 (표준 라이브러리만).

  python tools/prompt.py 1-11 --chars eunju,kwak --cut "extreme close-up of ..." --sound 동그리

[STYLE] design/style.json · [SCENE] design/scene_presets.json · [CHAR] design/style_guide.md 6절 고정 문구 + 그 씬 의상(design/outfits_en.json으로 영어화)
· [CUT] 직접 입력(콘티 컷 내용, 카메라는 style_guide 4절 표) · [SOUND] style_guide 2절 · [NEG] style.json
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LABEL = {"eunju": "은주", "dongmin": "동민", "manseok": "만석", "kwak": "곽 영감", "seonyoung": "선영",
         "choi": "최 계장", "taejun": "태준", "mija": "미자", "deoksu": "덕수", "sunrye": "순례 할머니"}


def char_locks():
    g = (ROOT / "design" / "style_guide.md").read_text(encoding="utf-8")
    locks = {}
    for cid, ko in LABEL.items():
        m = re.search(rf"^- {re.escape(ko)}: `([^`]+)`", g, re.M)
        if m:
            locks[cid] = m.group(1)
    return locks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scene", help="화-S#, 예: 1-11")
    ap.add_argument("--chars", default="", help="화면에 나오는 인물 id, 쉼표로")
    ap.add_argument("--cut", default="", help="컷 내용(영어): 카메라, 동작, 연기")
    ap.add_argument("--outfit", action="append", default=[], help="컷에서 의상이 다르면 id=영어 설명 (여러 번 가능). [CUT]의 의상 변화가 씬 의상보다 우선")
    ap.add_argument("--sound", default="", help="소리 색 이름(style.json sound_colors의 name 일부), 없으면 생략")
    a = ap.parse_args()

    style = json.loads((ROOT / "design" / "style.json").read_text(encoding="utf-8"))
    presets = {p["scene"]: p for p in json.loads((ROOT / "design" / "scene_presets.json").read_text(encoding="utf-8"))}
    p = presets[a.scene]
    locks = char_locks()
    outfits = {c["id"]: c.get("outfit", "") for c in p["characters"]}
    en_path = ROOT / "design" / "outfits_en.json"
    en = json.loads(en_path.read_text(encoding="utf-8")) if en_path.exists() else {}

    override = dict(o.split("=", 1) for o in a.outfit)
    lines = [f"[STYLE] {style['prompt_style']}", f"[SCENE] {p['prompt_scene']}"]
    for cid in [c for c in a.chars.split(",") if c]:
        lines.append(f"[CHAR] {locks.get(cid, cid)}; outfit in this scene: {override.get(cid) or en.get(outfits.get(cid, ''), outfits.get(cid, '(씬 프리셋에 없음 — 확인)') + ' [영어 대응 없음: design/outfits_en.json에 추가]')}")
    if a.cut:
        lines.append(f"[CUT] {a.cut}")
    if a.sound:
        sc = next((s for s in style["sound_colors"] if a.sound in s["name"]), None)
        if sc:
            lines.append(f"[SOUND] the surroundings are desaturated about 60%, only this sound glows as soft translucent "
                         f"{sc['hex']} light rings spreading into the air")
    lines.append(f"[NEG] {style['prompt_negative']}")
    print("\n".join(lines))
    print(f"\n# 참고(한국어): 빛 {p['light']} / 의상 {', '.join(f'{k}: {v}' for k, v in outfits.items())}")


if __name__ == "__main__":
    main()
