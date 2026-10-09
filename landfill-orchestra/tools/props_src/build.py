import json, os, sys, importlib
sys.path.insert(0, os.path.dirname(__file__))
from common import prompt, ROOT, ERA_DEFAULT, sort_scenes

FIELDS = ["id", "name", "aliases", "tier", "era", "material", "size", "colors", "condition", "shape",
          "role", "scenes", "ref"]


def load_all():
    items = []
    for mod in ("data_a", "data_b", "data_c"):
        try:
            m = importlib.import_module(mod)
        except ModuleNotFoundError:
            continue
        items += getattr(m, mod[-1].upper())
    spec = {}
    for mod in ("spec_b", "spec_c"):
        try:
            spec.update(importlib.import_module(mod).SPEC)
        except ModuleNotFoundError:
            pass
    try:
        from research import RES
    except ModuleNotFoundError:
        RES = {}
    for p in items:
        sp = spec.get(p["id"])
        if sp:
            for k, v in sp.items():
                if k == "en":
                    p["_en"] = v
                elif k == "tier":
                    p["tier"] = v
                else:
                    p[k] = v
        if p["id"] in RES:
            p["research"] = RES[p["id"]]
            okr = [src for f, src, st in RES[p["id"]] if st in ("확인", "일부 확인")]
            if p["ref"].startswith("미확인") and okr:
                miss = any(st in ("미확인", "추측") for f, src, st in RES[p["id"]])
                p["ref"] = "; ".join(dict.fromkeys(okr)) + (" — 일부 미확인(props.md 고증 출처 표)" if miss else "")
    return items


def en_of(p, over=None):
    e = dict(p["_en"])
    e.setdefault("colors", p["colors"])
    e.setdefault("era", ERA_DEFAULT)
    if over:
        e.update(over)
    need = ("name", "shape", "material", "size", "condition")
    if not all(e.get(k) for k in need):
        return None
    return prompt(e["name"], e["shape"], e["material"], e["size"], e["condition"], e["colors"], e["era"])


def to_json(p):
    o = {k: p[k] for k in FIELDS}
    o["scenes"] = sort_scenes(p["scenes"])
    pe = en_of(p)
    if pe:
        o["prompt_en"] = pe
    if p["tier"] == "A":
        sts = []
        for s in p["_states"]:
            st = {"key": s["key"], "label": s["label"], "scenes": sort_scenes(s["scenes"]), "change": s["change"]}
            sp = en_of(p, s["_en"])
            if sp:
                st["prompt_en"] = sp
            sts.append(st)
        o["states"] = sts
    if p.get("offscreen"):
        o["offscreen"] = p["offscreen"]
    if p.get("notes"):
        o["notes"] = p["notes"]
    if p.get("research"):
        o["research"] = [{"fact": f, "source": s, "status": st} for f, s, st in p["research"]]
    return o


def main():
    items = load_all()
    order = {"A": 0, "B": 1, "C": 2}
    items.sort(key=lambda p: order[p["tier"]])
    out = [to_json(p) for p in items]
    path = os.path.join(ROOT, "design", "props.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    from collections import Counter
    print("saved", path, Counter(p["tier"] for p in out), "with prompt:", sum("prompt_en" in p for p in out))
    return items, out


if __name__ == "__main__":
    main()
