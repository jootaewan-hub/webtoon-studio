# 소품 데이터 공통 도구
HEAD = "prop design sheet of "
TAIL_FIXED = ("front view, side view, and one close-up detail view, plain light background, "
              "clean uniform dark-brown 2px outlines, two-tone cel shading, semi-realistic, "
              "no text, no logos, no brand marks")
ERA_DEFAULT = "1987 Seoul"


def prompt(name, shape, material, size, condition, colors, era=ERA_DEFAULT):
    return (f"{HEAD}{name}, {shape}, {material}, {size}, {condition}, "
            f"colors {', '.join(colors)}, {TAIL_FIXED}, {era}")


def S(key, label, scenes, change, **en):
    """상태 단계. en: name/shape/material/size/condition/colors/era 덮어쓰기"""
    return {"key": key, "label": label, "scenes": scenes, "change": change, "_en": en}


def P(id, name, tier, scenes, *, aliases=(), era="1987~88 서울", material="", size="", colors=(),
      condition="", shape="", role="", ref="미확인", en=None, states=(), notes="", offscreen="",
      research=()):
    return dict(id=id, name=name, aliases=list(aliases), tier=tier, era=era, material=material,
                size=size, colors=list(colors), condition=condition, shape=shape, role=role,
                scenes=list(scenes), ref=ref, _en=en or {}, _states=list(states), notes=notes,
                offscreen=offscreen, research=list(research))


def R(*a):
    """'1-3', '2-5..2-9' 같은 표기를 씬 목록으로"""
    out = []
    for x in a:
        if ".." in x:
            s, e = x.split("..")
            ep, a1 = s.split("-")
            _, b1 = e.split("-")
            out += [f"{ep}-{i}" for i in range(int(a1), int(b1) + 1)]
        else:
            out.append(x)
    return out


import json as _json
ROOT = str(__import__("pathlib").Path(__file__).resolve().parents[2])
PRESETS = _json.load(open(ROOT + r"\design\scene_presets.json", encoding="utf-8"))
_ORDER = [s["scene"] for s in PRESETS]


def char_scenes(*ids, outfit=None, exclude=()):
    """scene_presets에서 인물이 나오는 씬(outfit 문자열이 주어지면 그 의상 라벨에 포함된 씬만)"""
    out = []
    for s in PRESETS:
        for c in s["characters"]:
            if c["id"] in ids and (outfit is None or outfit in c.get("outfit", "")):
                if s["scene"] not in exclude and s["scene"] not in out:
                    out.append(s["scene"])
    return out


def sort_scenes(sc):
    return sorted(set(sc), key=_ORDER.index)


def X(material, size, colors, condition, shape, role, en, ref="미확인", notes="", era=None, offscreen=None):
    """B·C 사양. en = (name, shape, material, size, condition[, era])"""
    d = dict(material=material, size=size, colors=list(colors), condition=condition or "특별한 낡음 없음(보통 사용감)", shape=shape, role=role, ref=ref)
    e = dict(zip(("name", "shape", "material", "size", "condition", "era"), en))
    d["en"] = e
    if notes: d["notes"] = notes
    if era: d["era"] = era
    if offscreen: d["offscreen"] = offscreen
    return d
