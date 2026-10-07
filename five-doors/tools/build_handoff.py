#!/usr/bin/env python3
"""G12 최종 인계 패키지(handoff/) 만들기.

  python3 five-doors/tools/build_handoff.py

입력
  storyboard/data/cuts.json, chapter_notes.json, characters.json, sets.json, tracks.json   (kit.py import·build_kit_data.py 결과)
  handoff/props.md (PROP LOCK), story/*, anim/*, decisions.md
출력 (handoff/ 아래)
  prompts/ep<N>.jsonl         Codex용. 컷마다 {cut, size, track, scene, flags, prompt, refs, lettering}
  prompts/ep<N>_prompts.md    ChatGPT·사람용. 컷마다 '그대로 복사하는 프롬프트' 블록 + 레터링
  storyboard/                 콘티 합본 md·docx, cuts.json, chapter_notes.json
  story/                      소설·대본·바이블·기획·비트 + 연출 노트(G10)·효과음 사전(G10)
  anim/                       애니 콘티(G11)·사운드 큐 시트(G11)
  decisions.md                결정 로그 사본
  asset_manifest.csv          레퍼런스·컷 이미지 대장(todo 상태로 전부 나열)
프롬프트 조립 순서는 handoff/AGENTS.md '프롬프트 조립 규칙'과 같다. LOCK 문장은 원문 그대로 넣는다.
표준 라이브러리만 쓴다.
"""
import csv, json, re, shutil
from pathlib import Path

P = Path(__file__).resolve().parent.parent
H = P / "handoff"
D = P / "storyboard/data"
load = lambda n: json.loads((D / n).read_text(encoding="utf-8"))
cuts, notes, chars, sets, tracks = (load("cuts.json"), load("chapter_notes.json"), load("characters.json"),
                                    load("sets.json"), load("tracks.json"))
T = tracks["tracks"]["webtoon_adult"]
STYLE = {"1": T["style"], "2": T["style_track2"], "3": T["style_track3"]}
SET_CODE = {k: (f"S{int(k):02d}" if k.isdigit() else "S" + k[-1]) for k in sets}

# PROP LOCK (props.md의 '- **PROP LOCK**: `…`' 줄)
props_md = (H / "props.md").read_text(encoding="utf-8")
PROPS = {}
for m in re.finditer(r"^## (P\d+)\. (.+?)$", props_md, re.M):
    sec = props_md[m.end():]
    nxt = re.search(r"^## ", sec, re.M)
    sec = sec[: nxt.start()] if nxt else sec
    lk = re.search(r"\*\*PROP LOCK\*\*: `([^`]+)`", sec)
    if lk:
        PROPS[m.group(1)] = {"name": m.group(2).strip(), "lock": lk.group(1)}
PROP_KW = [("P2", r"쇼핑백|돈다발|지폐"), ("P1", r"향수"), ("P6", r"귀걸이"), ("P4", r"진주"),
           ("P7", r"체인 백|퀼팅"), ("P8", r"공유 시트|당번표"), ("P9", r"안경|법전|머리끈"),
           ("P10", r"이태리타월|손수건"), ("P5", r"세컨폰|메인폰|휴대폰|멀티프로필"), ("P3", r"시계|흉터")]

# 이미지 프롬프트에서 빼는 레터링 지시(말풍선·효과음·식자는 후공정)
LETTER_RE = re.compile(r"말풍선|효과음|내레이션 박스|내레이션은|식자|East Sea Dokdo|Black Han Sans|Gowun|Nanum|자막")
NAME_RE = re.compile(r"(도겸|유진|미란|세라|하린|혜숙|순옥)")


def image_screen(screen):
    s = screen.replace("[트랙2]", "").replace("[트랙3]", "").strip()
    out = []
    for sent in re.split(r"(?<=[.다])\s+", s):
        if not LETTER_RE.search(sent):
            out.append(sent); continue
        keep = [cl for cl in re.split(r",\s*", sent) if not LETTER_RE.search(cl)]
        if keep:
            t = ", ".join(keep).strip()
            out.append(t if t.endswith(".") else t + ".")
    txt = " ".join(out).strip()
    POS = r"(좌상|우상|좌하|우하|중상|중하|좌|우|상단|하단|가운데|위|아래)"
    txt = re.sub(rf"(?:^|\s){POS}(?:,\s*{POS})*\.(?=\s|$)", "", txt)  # 말풍선 위치만 남은 조각 제거
    return re.sub(r"\s{2,}", " ", txt).strip()


def track_of(c):
    return "2" if "[트랙2]" in c["screen"] else ("3" if "[트랙3]" in c["screen"] else "1")


def present(c):
    names = []
    seg = c.get("shot", "").split("·", 2)
    who_part = seg[2] if len(seg) == 3 else c.get("shot", "")  # 앵글 칸의 POV(누구)·오버숄더(누구 너머)는 화면 밖일 수 있어 인물 칸만 본다
    if "오버숄더" in (seg[1] if len(seg) == 3 else ""):
        who_part += " " + seg[1]  # 오버숄더의 어깨 주인은 화면에 걸린다
    for n in NAME_RE.findall(who_part):
        if n not in names:
            names.append(n)
    return [ch for ch in chars if ch["name"] in names]


def set_keys(memo):
    ks = []
    for k in re.findall(r"장소\s*(\d+|짧게 [ABC])", memo):
        if k in sets and k not in ks:
            ks.append(k)
    return ks[:2]


def props_for(c):
    if not re.match(r"\s*(INS|ECU|CU)\b", c.get("shot", "")):
        return []
    found = [p for p, kw in PROP_KW if re.search(kw, c["screen"])]
    return found[:2]


def safety(c):
    r = list(tracks["global_negative"])
    if "intimate" in c["flags"]:
        r += tracks["intimate_rule"]
    if "child_present" in c["flags"]:
        r += tracks["child_rule"]
    if "violence" in c["flags"]:
        r += tracks["violence_rule"]
    return r


def build(c):
    memo = notes.get(f"{c['chapter']} / {c['scene']}", "")
    tr = track_of(c)
    who = present(c)
    sk = set_keys(memo)
    pk = props_for(c)
    parts = [STYLE[tr]]
    for ch in who:
        parts.append(ch["look"])
    for k in sk:
        parts.append(sets[k]["lock"])
    for p in pk:
        parts.append("PROP LOCK: " + PROPS[p]["lock"])
    parts.append(f"장면(조명·의상 고정값): {memo}")
    parts.append(f"컷 {c['id']} — 세로 웹툰 컷 {c['width']}×{c['height']}px. 샷: {c['shot']}. 화면: {image_screen(c['screen'])}")
    parts.append("no text, no speech bubbles, no sound-effect lettering, no watermark, no logos, fictional adult characters only.")
    prompt = "\n\n".join(parts)
    refs = [f"refs/characters/{ch['id']}_turnaround_v*.png (approved)" for ch in who]
    refs += [f"refs/sets/{SET_CODE[k]}_*_v*.png (approved, 장면 시간대)" for k in sk]
    refs += [f"refs/props/{p}_*_v*.png (approved)" for p in pk]
    return {"cut": c["id"], "size": f"{c['width']}x{c['height']}", "track": int(tr),
            "chapter": c["chapter"], "scene": c["scene"], "flags": c["flags"],
            "characters": [ch["id"] for ch in who], "sets": [SET_CODE[k] for k in sk], "props": pk,
            "prompt": prompt, "safety": safety(c), "refs": refs, "lettering": c["lines"]}


(H / "prompts").mkdir(parents=True, exist_ok=True)
by_ep = {}
for c in cuts:
    ep = "1" if c["id"].startswith("0-") else c["id"].split("-")[0]
    by_ep.setdefault(ep, []).append(build(c))
for ep, items in by_ep.items():
    with open(H / f"prompts/ep{ep}.jsonl", "w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")
    md = [f"# {ep}화 컷별 이미지 프롬프트 — 「단톡방에 그 남자가 있다」", "",
          "컷마다 '프롬프트' 상자 안을 **그대로** 복사해 ChatGPT 이미지 생성에 붙인다. 상자 아래 '레퍼런스'의 확정 이미지를 함께 첨부한다.",
          "상자는 `style_lock.md` 트랙 문구 → CHARACTER LOCK → SET LOCK → (소품 클로즈업이면) PROP LOCK → 장면 조명·의상 → 컷 지시 → 금지 문구 순서로 조립했다(AGENTS.md).",
          "말풍선·효과음·내레이션은 그림에 넣지 않는다. 아래 '레터링'은 Codex가 나중에 얹는다.", ""]
    scene = None
    for it in items:
        if it["scene"] != scene:
            scene = it["scene"]; md += ["", f"## {it['chapter']} / {scene}", ""]
        tag = {1: "트랙 1 본편", 2: "트랙 2 코미디 셀", 3: "트랙 3 티저"}[it["track"]]
        flg = ", ".join(it["flags"]) or "없음"
        md += [f"### {it['cut']} ({it['size'].replace('x', '×')}, {tag}, 태그: {flg})", "", "```text", it["prompt"], "```", "",
               "- 수위·금지: " + " / ".join(it["safety"]),
               "- 레퍼런스: " + ("; ".join(it["refs"]) if it["refs"] else "(없음)"),
               "- 레터링: " + (" / ".join((f"{l['speaker']}: " if l["speaker"] else "") + l["text"] for l in it["lettering"]) or "(없음)"), ""]
    (H / f"prompts/ep{ep}_prompts.md").write_text("\n".join(md) + "\n", encoding="utf-8")

# 사본
def cp(src, dst):
    dst = H / dst; dst.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(P / src, dst)

for s, d in [("storyboard/source/storyboard.md", "storyboard/storyboard.md"),
             ("storyboard/source/storyboard.docx", "storyboard/storyboard.docx"),
             ("storyboard/data/cuts.json", "storyboard/cuts.json"),
             ("storyboard/data/chapter_notes.json", "storyboard/chapter_notes.json"),
             ("storyboard/SPEC.md", "storyboard/SPEC.md"),
             ("story/novel.md", "story/novel.md"), ("story/script.md", "story/script.md"),
             ("story/bible.md", "story/bible.md"), ("story/pitch.md", "story/pitch.md"),
             ("story/beats.md", "story/beats.md"),
             ("story/direction.md", "story/direction.md"), ("story/sfx_list.md", "story/sfx_list.md"),
             ("anim/storyboard_anim.md", "anim/storyboard_anim.md"), ("anim/sound_cues.md", "anim/sound_cues.md"),
             ("decisions.md", "decisions.md")]:
    cp(s, d)

# 매니페스트
rows = [["file", "kind", "subject", "variant", "track", "prompt_ref", "tool", "status", "approved_by", "notes"]]
for ch in chars:
    for sheet, ref in [("turnaround", "3-a"), ("expressions", "표정"), ("outfits-a", "의상"), ("outfits-b", "의상"),
                       ("hand", "클로즈업"), ("keyvisual", "키 비주얼")]:
        rows.append([f"refs/characters/{ch['id']}_{sheet}_v1.png", "character", ch["id"], sheet, "1",
                     f"characters/{ch['id']}.md#{ref}", "ChatGPT", "todo", "", ""])
for p, v in PROPS.items():
    rows.append([f"refs/props/{p}_sheet_v1.png", "prop", p, "sheet", "1", f"props.md#{p}", "ChatGPT", "todo", "", v["name"]])
for k, v in sets.items():
    rows.append([f"refs/sets/{SET_CODE[k]}_main_v1.png", "set", SET_CODE[k], "main", "1", f"sets.md#{k}", "ChatGPT", "todo", "",
                 f"{v['name']} — 시간대별 조명(sets.md N-3)마다 variant를 늘린다"])
for ep, items in by_ep.items():
    for it in items:
        rows.append([f"renders/ep{ep}/{it['cut']}_v1.png", "cut", it["cut"], it["size"], str(it["track"]),
                     f"prompts/ep{ep}_prompts.md#{it['cut']}", "ChatGPT", "todo", "", ";".join(it["flags"])])
with open(H / "asset_manifest.csv", "w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(rows)

n = sum(len(v) for v in by_ep.values())
print(f"프롬프트 {n}컷({', '.join(f'{k}화 {len(v)}' for k, v in sorted(by_ep.items()))}) / PROP LOCK {len(PROPS)}개 / 매니페스트 {len(rows)-1}행")
