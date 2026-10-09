"""캐릭터 시트용 이미지 프롬프트 (ChatGPT·Codex) 만들기 (표준 라이브러리만).

  python tools/char_prompts.py  → design/gen/character_prompts.md

인물마다 ① 턴어라운드 ② 표정 시트 ③ 의상 시트. 외형은 style_guide.md 6절 고정 문구,
의상은 characters.json outfits → outfits_en.json, 그림체·금지는 style.json.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from prompt import LABEL, char_locks  # noqa: E402

EXPR = {
    "무표정": "neutral expressionless face", "귀 기울임": "listening intently, head tilted slightly to the left, eyes half-lowered",
    "놀람": "surprised, eyes wide", "겁·공포": "frightened, shoulders drawn in", "슬픔·울먹": "sad, holding back tears",
    "울먹": "about to cry, trembling lips", "미소": "a faint smile", "활짝 웃음": "a big open smile",
    "단호·진지": "serious and determined", "분노": "angry, frowning", "슬픔": "quietly sad", "곁눈·나른": "tired sideways glance",
    "곁눈": "sideways glance", "당황·놀람": "flustered and startled", "식은땀·초조": "nervous, cold sweat",
    "당황": "flustered", "냉정": "cold and composed", "비웃": "a slight sneer",
}


# 15년 뒤(2003, 에필로그 3-34)와 회상 모습. 바이블·continuity 에필로그 기준, 나이는 1987년 기준 +16.
LATER = {
    "eunju": ("2003", "Eunju at 29, an adult Korean woman violinist, slim, the same narrow face, long almond-shaped eyes and faint freckles, long dark-brown hair still tied low with a single rubber band, the same small silver tuning-fork pendant"),
    "dongmin": ("2003", "Dongmin at 25, an adult Korean man and percussionist, round face, short hair, big ears, a warm grin, holding drumsticks"),
    "manseok": ("2003", "Manseok at 57, an older Korean man, white hair with no cap, gaunt face softened by age, long fingers"),
    "kwak": ("2003", "old Kwak at 84, still healthy and upright, short white buzz cut, deeper wrinkles, a pencil behind his ear"),
    "seonyoung": ("2003", "Seonyoung at 38, a Korean music teacher, shoulder-length softly permed hair, the same large round gold-rim glasses"),
    "choi": ("2003", "Mr. Choi at 62, a retired Korean civil servant, thinning gray pomaded hair, thick horn-rimmed glasses, a handkerchief in hand"),
    "taejun": ("2003", "Taejun at 29, an adult Korean man violinist, tall and slim, neat side part, a calmer face"),
    "mija": ("2003", "Mija at 30, a Korean PE teacher, tall and broad-shouldered, short practical haircut with unruly bangs"),
    "deoksu": ("2003", "Deoksu at 28, a big round-faced Korean man who runs the rice-soup restaurant, short crew cut, gentle eyes"),
    "sunrye": ("2003", "grandma Sunrye in her 90s, even more stooped, white hair in a low bun, cheerful"),
}
YOUNG = {"manseok": ("회상", "Manseok at about 30 in the 1970s, a young Korean clarinetist in a theater show band, slim, short neat hair, no cap, long fingers")}


def main():
    style = json.loads((ROOT / "design" / "style.json").read_text(encoding="utf-8"))
    chars = json.loads((ROOT / "design" / "characters.json").read_text(encoding="utf-8"))
    en = json.loads((ROOT / "design" / "outfits_en.json").read_text(encoding="utf-8"))
    locks = char_locks()
    st, neg = style["prompt_style"].replace(", vertical webtoon panel", ""), style["prompt_negative"]
    out = ["# 캐릭터 시트 프롬프트 (ChatGPT·Codex용)", "",
           "만든 도구: `python tools/char_prompts.py` (원본: `design/characters.json`, `design/style_guide.md` 6절, `design/outfits_en.json`).",
           "",
           "사용법:",
           "1. 인물마다 ① 턴어라운드를 먼저 만들고, 마음에 드는 결과를 `renders/characters/<id>_turnaround.png`로 저장한다.",
           "2. ② 표정·③ 의상 시트는 ①의 이미지를 함께 올리고 \"same character as the attached image\"를 앞에 붙여 만든다(인물 일관성).",
           "3. 콘티 컷을 만들 때도 해당 인물의 턴어라운드 이미지를 참고 이미지로 함께 올린다.",
           ""]
    for c in chars:
        cid = c["id"]
        lock = locks.get(cid, c.get("face", ""))
        name = LABEL.get(cid, c.get("name"))
        outs_all = c.get("outfits", [])
        outs = [o for o in outs_all if "2003" not in o["label"] and "회상" not in o["label"]]
        base = en.get(outs[0]["label"], outs[0]["label"]) if outs else ""
        exprs = [EXPR.get(e, e) for e in c.get("expressions", [])]
        out += [f"## {name} ({cid}) — {c.get('design_choice', '')}", "",
                f"- 나이·키: {c.get('age')} · {c.get('height')} · {c.get('head_ratio')}등신",
                f"- 연기: {c.get('acting', '')}", "",
                "### ① 턴어라운드", "```",
                f"character turnaround sheet, {lock}, wearing {base}, front view, three-quarter view, side view, back view, "
                f"standing neutral pose, full body, same scale in every view, plain light background, {st}, {neg}", "```", "",
                "### ② 표정 시트", "```",
                f"same character as the attached image: {lock}. Expression sheet, head and shoulders, "
                + ", ".join(f"({i + 1}) {e}" for i, e in enumerate(exprs))
                + f", consistent face in every panel, plain light background, {st}, {neg}", "```", ""]
        for tag, table in (("④ 15년 뒤(2003, 에필로그 3-34)", LATER), ("⑤ 회상(3-3)", YOUNG)):
            if cid in table:
                key, desc = table[cid]
                o = next((x for x in outs_all if key in x["label"]), None)
                wear = en.get(o["label"], o["label"]) if o else ""
                out += [f"### {tag}", "```",
                        f"character turnaround sheet, {desc}, wearing {wear}, front view, three-quarter view, side view, "
                        f"back view, standing neutral pose, full body, plain light background, {st}, {neg}", "```", ""]
        if len(outs) > 1:
            listing = "; ".join(f"({i + 1}) {en.get(o['label'], o['label'])}" for i, o in enumerate(outs))
            out += ["### ③ 의상 시트", "",
                    "| # | 의상 | 등장 |", "|---|---|---|"]
            sch = json.loads((ROOT / "design" / "outfit_schedule.json").read_text(encoding="utf-8"))
            for i, o in enumerate(outs):
                scenes = [s for s, m in sch.items() if not s.startswith("_") and m.get(cid) == o["label"]]
                out.append(f"| {i + 1} | {o['label']} | {', '.join(scenes) if scenes else '기본(일정표에 없는 씬)' if i == 0 else '—'} |")
            out += ["", "```",
                    f"same character as the attached image: {lock}. Outfit sheet, full body front view in each outfit: {listing}. "
                    f"Same face and body in every outfit, plain light background, {st}, {neg}", "```", ""]
    p = ROOT / "design" / "gen" / "character_prompts.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n".join(out), encoding="utf-8")
    print(f"{len(chars)}명 → {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
