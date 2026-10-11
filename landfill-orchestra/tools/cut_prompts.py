"""G9 컷 이미지 프롬프트 조립 — 콘티(storyboard/data/cuts.json) + 컷 사양(storyboard/source/cut_spec_ep*.jsonl).

  python tools/cut_prompts.py check          # 사양 점검만(빠진 컷, 모르는 id, 소리 색 남용 경고)
  python tools/cut_prompts.py build          # storyboard/out/cel/<컷>.md, _cel_ALL_ep<n>.md, cel_prompts.jsonl

한 컷 = [STYLE] style.json · [SCENE] scene_presets.json · [SET] sets.json 배치 문장·카메라 자리 · [CHAR] style_guide 6절 고정 문구
+ 그 씬 의상(outfits_en.json) · [PROPS] props.json(상태 키) · [CUT] 사양의 영어 컷 문장 · [SOUND] style_guide 2절 · [NEG] style.json.
tools/prompt.py와 같은 재료를 쓰고, 콘티 컷마다 한 번에 만든다. 표준 라이브러리만.

컷 사양 한 줄(JSON):
  {"id": "1-003", "scene": "1-1", "chars": ["eunju", "dongmin"], "extras": ["갈고리 아주머니"],
   "set": "small_hill_slope", "spot": "카메라 자리 id(선택)", "props": ["dongguri__s1_first"],
   "sound": "은주의 귀" 또는 null, "desaturate": true(기본, false면 채도 유지), "outfit": {"eunju": "영어 의상(씬 의상과 다를 때만)"},
   "char_text": {"manseok": "회상 등에서 고정 문구 대신 쓸 영어 외형(선택)"}, "set2": "가로 분할 컷 다른 칸 배경 id(선택)",
   "pendant": true|false|"hidden" (은주 소리굽쇠 목걸이, 기본 true), "colors": ["#E8944A", "#F5C04A"] (여러 소리 색, 선택),
   "sound_style": "dots" (번지지 않는 작은 점, 선택),
   "cut_en": "medium shot, eye level: ... (카메라 → 동작 → 표정·손 → 빛)"}
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SB = ROOT / "storyboard"
OUT = SB / "out" / "cel"
CLOSE = ("ECU", "CU", "INS", "TXT")
PENDANT = "a small silver tuning-fork pendant on a thin chain"


def jload(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def locks():
    g = (ROOT / "design" / "style_guide.md").read_text(encoding="utf-8")
    sec = g.split("## 6.", 1)[1].split("## 7.", 1)[0]
    return {m.group(1).strip(): m.group(2) for m in re.finditer(r"^- ([^:`]+): `([^`]+)`", sec, re.M)}


LABEL = {"eunju": "은주", "dongmin": "동민", "manseok": "만석", "kwak": "곽 영감", "seonyoung": "선영",
         "choi": "최 계장", "taejun": "태준", "mija": "미자", "deoksu": "덕수", "sunrye": "순례 할머니",
         "bonggu": "봉구", "yeongran": "영란", "gyeongho": "경호", "gyeongmin": "경민", "suni": "순이", "seoki": "석이"}


def load_all():
    style = jload(ROOT / "design" / "style.json")
    presets = {p["scene"]: p for p in jload(ROOT / "design" / "scene_presets.json")}
    sets = {s["id"]: s for s in jload(ROOT / "design" / "sets.json")}
    props, states = {}, {}
    for p in jload(ROOT / "design" / "props.json"):
        props[p["id"]] = p
        for s in p.get("states") or []:
            states[s["key"]] = (p, s)
    en = jload(ROOT / "design" / "outfits_en.json")
    cuts = jload(SB / "data" / "cuts.json") if (SB / "data" / "cuts.json").exists() else []
    spec = {}
    for f in sorted((SB / "source").glob("cut_spec_ep*.jsonl")):
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if line.strip():
                try:
                    d = json.loads(line)
                except json.JSONDecodeError as e:
                    raise SystemExit(f"{f.name}:{n} JSON 오류: {e}")
                spec[d["id"]] = d
    return style, presets, sets, props, states, en, cuts, spec


def prop_text(key, props, states, short=False):
    """소품 시트 프롬프트에서 시트 꼬리(앞·옆 보기, 배경, 그림체)를 떼고 컷 안 묘사로 쓴다."""
    if key in states:
        p, s = states[key]
        src = s.get("prompt_en") or p["prompt_en"]
    elif key in props:
        p, src = props[key], props[key]["prompt_en"]
    else:
        return None
    t = re.sub(r"^prop design sheet of\s+", "", src)
    t = re.split(r",\s*(?:front view|colors #|plain light background)", t)[0]
    t = re.sub(r",\s*an old real violin bow shown beside it", "", t)
    limit = 200 if short else (None if p.get("tier") == "A" else 420)  # 소품이 많은 합주 컷은 짧게, 세부는 참고 이미지로
    if limit and len(t) > limit:
        t = t[:limit].rsplit(",", 1)[0]
    return f"{t} (match the reference image renders/props/{key}.png)"


def shot_of(cut):
    m = re.match(r"\s*(ECU|CU|BS|MS|FS|LS|ELS|INS|TXT)\b", cut.get("shot", ""))
    return m.group(1) if m else ""


def aspect(cut):
    w, h = cut.get("width", 800), cut.get("height", 1000)
    return f"panel {w}x{h} ({'tall' if h > w * 1.4 else 'vertical' if h >= w else 'wide'})"


def assemble(cut, sp, style, presets, sets, props, states, en, lk):
    warn = []
    p = presets.get(sp.get("scene", ""))
    if not p:
        return None, [f"씬 프리셋 없음: {sp.get('scene')}"]
    outfits = {}
    for c in p["characters"]:  # 같은 인물이 두 번 있으면(3-34 어른·회상 동민) 앞의 것이 기본, 다른 쪽은 사양 outfit으로
        outfits.setdefault(c["id"], c.get("outfit", ""))
    scene_txt = p["prompt_scene"]
    if "; [flashback] " in scene_txt:  # 회상 장소가 같은 씬 프리셋에 들어 있는 씬(3-3·3-12·3-21)
        now, fb = scene_txt.split("; [flashback] ", 1)
        ce = sp.get("cut_en", "").lower()
        if (sp.get("set") or "").startswith("fb_") or ce.startswith("flashback"):
            scene_txt = fb
        elif (sp.get("set2") or "").startswith("fb_") or "flashback" in ce:
            scene_txt = f"{now}; [flashback frame only] {fb}"
        else:
            scene_txt = now
    L = [f"[STYLE] {style['prompt_style']}, {aspect(cut)}", f"[SCENE] {scene_txt}"]
    st = sets.get(sp.get("set") or "")
    if sp.get("set") and not st:
        warn.append(f"배경 id 없음: {sp['set']}")
    if st:
        spot = next((c for c in st.get("camera_spots", []) if c["id"] == sp.get("spot")), None)
        if sp.get("spot") and not spot:
            warn.append(f"카메라 자리 없음: {st['id']}/{sp['spot']}")
        body = "" if shot_of(cut) in CLOSE else st["layout_text_en"].rstrip(". ") + ". "
        lead = body.split(". ", 1)[0]
        if lead and lead in p["prompt_scene"]:  # 장소 기준 문장은 [SCENE]에 이미 있다
            body = body.split(". ", 1)[1] if ". " in body else ""
        cam = f"Camera position: {spot['en']}. " if spot else ""
        L.append(f"[SET] {body}{cam}(keep the layout consistent with the reference image renders/sets/{st['id']}.png)")
    st2 = sets.get(sp.get("set2") or "")
    if sp.get("set2") and not st2:
        warn.append(f"둘째 칸 배경 id 없음: {sp['set2']}")
    if st2:  # 가로 분할 컷의 다른 칸 배경
        L.append(f"[SET-2] for the other frame of the split panel: {st2['layout_text_en'][:600].rsplit(',', 1)[0]} "
                 f"(keep consistent with the reference image renders/sets/{st2['id']}.png)")
    for cid in sp.get("chars", []):
        if cid not in LABEL:
            warn.append(f"인물 id 없음: {cid}")
            continue
        o = (sp.get("outfit") or {}).get(cid)
        if not o:
            ko = outfits.get(cid, "")
            o = en.get(ko) or ""
            if not o:
                warn.append(f"{cid}: 씬 {p['scene']} 의상 영어 대응 없음({ko or '프리셋에 인물 없음'}) — outfit으로 지정")
        base = (sp.get("char_text") or {}).get(cid) or lk.get(LABEL[cid], cid)  # 회상 등 나이·모습이 다를 때 고정 문구를 통째로 바꾼다
        if cid == "eunju":  # 소리굽쇠 목걸이: 2화 S#25 상자에 넣음 → 3화 S#3 만석이 다시 걸어 줌. 사양 pendant로 정한다
            base = base.replace(PENDANT + ", ", "").replace(PENDANT, "")
            pd = sp.get("pendant", True)
            base += ", " + (PENDANT if pd is True else "a thin chain at her collar, the pendant hidden under her clothes"
                            if pd == "hidden" else "no necklace, bare neck")
        L.append(f"[CHAR] {base}; outfit in this scene: {o or '(see scene preset)'}")
    for x in sp.get("extras", []):
        L.append(f"[CHAR] {lk.get(x, x)}")
    for k in sp.get("props", []):
        t = prop_text(k, props, states, short=len(sp.get("props", [])) > 3)
        if not t:
            warn.append(f"소품 키 없음: {k}")
            continue
        L.append(f"[PROP] {t}")
    if not sp.get("cut_en"):
        warn.append("cut_en 비어 있음")
    L.append(f"[CUT] {sp.get('cut_en', '')}")
    if sp.get("colors"):  # 여러 소리 색이 함께인 컷(3화 본선 누적, '밤')
        desat = "the surroundings are desaturated about 60%, " if sp.get("desaturate", True) else "the scene keeps its full color, "
        L.append(f"[SOUND] {desat}the colored light bands described in [CUT] glow as soft translucent bands of "
                 f"{', '.join(sp['colors'][:-1])} and {sp['colors'][-1]} spreading into the air" if len(sp["colors"]) > 1 else
                 f"[SOUND] {desat}soft translucent {sp['colors'][0]} light rings spreading into the air")
    elif sp.get("sound"):
        sc = next((s for s in style["sound_colors"] if sp["sound"] in s["name"]), None)
        if not sc:
            warn.append(f"소리 색 이름 없음: {sp['sound']}")
        else:
            desat = "the surroundings are desaturated about 60%, only " if sp.get("desaturate", True) else "the scene keeps its full natural color, "
            if sp.get("sound_style") == "dots":  # 리허설처럼 화면으로 번지지 않는 소리
                L.append(f"[SOUND] the scene keeps its full color, tiny soft dots of {sc['hex']} light hug each instrument, not spreading")
            else:
                L.append(f"[SOUND] {desat}this sound glows as soft translucent {sc['hex']} light rings spreading into the air")
            if not p.get("sound_color"):
                warn.append(f"씬 {p['scene']} 프리셋에 소리 색 순간이 없는데 소리 색을 씀 — 대본 근거 확인")
    L.append(f"[NEG] {style['prompt_negative']}")
    return "\n".join(L), warn


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    style, presets, sets, props, states, en, cuts, spec = load_all()
    lk = locks()
    if not cuts:
        raise SystemExit("storyboard/data/cuts.json이 비어 있다. 먼저 storyboard에서 python kit.py import")
    ids = [c["id"] for c in cuts]
    missing = [i for i in ids if i not in spec]
    extra = [i for i in spec if i not in set(ids)]
    problems, built = [], []
    for c in cuts:
        sp = spec.get(c["id"])
        if not sp:
            continue
        txt, warn = assemble(c, sp, style, presets, sets, props, states, en, lk)
        problems += [f"{c['id']}: {w}" for w in warn]
        if txt:
            built.append((c, sp, txt))
    sound_n = sum(1 for _, sp, _ in built if sp.get("sound"))
    print(f"콘티 {len(ids)}컷 · 사양 {len(spec)}줄 · 사양 없는 컷 {len(missing)} · 콘티에 없는 사양 {len(extra)} · 소리 색 컷 {sound_n}")
    for i in missing[:30]:
        print(f"  [사양 없음] {i}")
    for i in extra[:30]:
        print(f"  [콘티에 없음] {i}")
    for w in problems[:80]:
        print(f"  [주의] {w}")
    if cmd != "build":
        return
    OUT.mkdir(parents=True, exist_ok=True)
    by_ep, rows = {}, []
    for c, sp, txt in built:
        letter = "\n".join(f"  - [{l['type']}] {l['speaker']}: {l['text']}" if l["speaker"] else f"  - [{l['type']}] {l['text']}"
                           for l in c.get("lines", [])) or "  - (없음)"
        md = (f"## {c['id']} — {c.get('scene', '')}\n- 크기 {c.get('width')}×{c.get('height')} · {c.get('shot', '')}\n"
              f"- 화면(한국어): {c.get('screen', '')}\n\n```\n{txt}\n```\n\n**레터링(후공정, 이미지에 넣지 않음)**\n{letter}\n")
        (OUT / f"{c['id']}.md").write_text(md, encoding="utf-8")
        by_ep.setdefault(c["id"].split("-")[0], []).append(md)
        rows.append({"id": c["id"], "scene": sp.get("scene"), "size": [c.get("width"), c.get("height")], "prompt": txt,
                     "lettering": c.get("lines", []), "ref_images": ([f"renders/sets/{sp['set']}.png"] if sp.get("set") else [])
                     + ([f"renders/sets/{sp['set2']}.png"] if sp.get("set2") else [])
                     + [f"renders/props/{k}.png" for k in sp.get("props", [])]
                     + [f"renders/characters/{x}.png" for x in sp.get("chars", [])]})
    for ep, mds in by_ep.items():
        head = (f"# {ep}화 컷 이미지 프롬프트 — 정밀 셀 반실사 「소리의 색」\n\n"
                "한 컷씩 붙여 넣는다. 참고 이미지(renders/characters·props·sets)를 함께 올리면 일관성이 오른다. "
                f"결과는 storyboard/renders/cel/<컷번호>.png로 저장한다. 말풍선·효과음은 이미지에 넣지 않는다.\n\n")
        (OUT / f"_cel_ALL_ep{ep}.md").write_text(head + "\n".join(mds), encoding="utf-8")
    with (OUT / "cel_prompts.jsonl").open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"→ {OUT} ({len(rows)}컷)")


if __name__ == "__main__":
    main()
