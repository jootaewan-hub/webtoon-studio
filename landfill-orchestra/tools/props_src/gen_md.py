import json, os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from common import ROOT
from research import RES, ANACHRONISM, GUARD
from judgments import JUDG

P = json.load(open(os.path.join(ROOT, "design", "props.json"), encoding="utf-8"))
TIER = {"A": "A 핵심", "B": "B 반복", "C": "C 디테일"}


def comp(sc):
    """['2-1','2-2','2-3','2-5'] → '2-1~2-3, 2-5'"""
    out, i = [], 0
    while i < len(sc):
        e, n = sc[i].split("-")
        j = i
        while j + 1 < len(sc) and sc[j + 1].split("-")[0] == e and int(sc[j + 1].split("-")[1]) == int(sc[j].split("-")[1]) + 1:
            j += 1
        out.append(sc[i] if i == j else f"{sc[i]}~{sc[j]}")
        i = j + 1
    return ", ".join(out)


def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


def unverified(p):
    if "미확인" in p["ref"]:
        return True
    r = p.get("research")
    return bool(r) and all(x["status"] in ("미확인", "추측") for x in r)


def md():
    L = []
    cnt = {t: sum(p["tier"] == t for p in P) for t in "ABC"}
    nstate = sum(len(p.get("states", [])) for p in P)
    L += ["# 소품 시안서 — 깡통 바이올린 (G8)", "",
          "기준: `story/script.md`(대본 정본) · `design/scene_presets.json` props 칸 · `story/continuity.md` 악기 표 · `design/style_guide.md`. "
          "기계용 원본은 `design/props.json`, GPT에 붙일 프롬프트는 `design/gen/prop_prompts.md`. 그림은 그리지 않는다(작화는 ChatGPT·Codex).", "",
          "원칙: 악기 재료·형태는 continuity.md 악기 표와 대본 Insert 문장을 글자 그대로 따르고, 카테우라 실물은 형태 참고로만. 실존 상표·로고·실제 화폐 도안·올림픽 마스코트·엠블럼 없음. "
          "글자가 정체인 소품(공고·신문·전당표·상장·'찾을 돈' 깡통·현수막)은 이미지에 글자를 넣지 않고 빈 띠·흐린 선으로 두며, 글자는 식자 단계에서 얹는다. 소리 색 규칙은 장면 효과라 소품 시트에 넣지 않는다.", "",
          "## 한눈에", "",
          "| 등급 | 개수 | 뜻 |", "|---|---|---|",
          f"| A 핵심 | {cnt['A']} (상태 단계 {nstate}) | 악기·복선·플롯 소품. 상태가 바뀌는 단계마다 따로 시트 |",
          f"| B 반복 | {cnt['B']} | 2개 이상 씬에 나오는 생활 소품·차량·도구·가구·의상 |",
          f"| C 디테일 | {cnt['C']} | 한 씬에만 나오는 것(음식·회상 소품 포함) |",
          f"| 합계 | {len(P)} | |", ""]
    # 고증 미확인
    L += ["## 고증 미확인 목록", "", "A·B 등급 중 1987~88년 실물 모양을 출처로 확인하지 못한 소품. 이 소품들의 프롬프트에는 대본·연속성 문서에 적힌 것과 확인된 일반 사실만 넣고, 나머지는 디자인 판단으로 표시했다.", ""]
    def ok(p):
        return any(r["status"] in ("확인", "일부 확인") for r in p.get("research", []))
    for t in "AB":
        none_ = [p for p in P if p["tier"] == t and not ok(p)]
        part = [p for p in P if p["tier"] == t and ok(p) and ("미확인" in p["ref"] or any(r["status"] in ("미확인", "추측") for r in p.get("research", [])))]
        L.append(f"- **{t} — 출처 확인 없음** ({len(none_)}): " + ", ".join(f"{p['name']}(`{p['id']}`)" for p in none_))
        L.append(f"- **{t} — 일부만 확인** ({len(part)}): " + ", ".join(f"{p['name']}(`{p['id']}`)" for p in part))
    cu = [p for p in P if p["tier"] == "C" and unverified(p)]
    L += [f"- **C** ({len(cu)}): 시대 착오 점검만 했다. 아래 '시대 착오 점검' 참고.", ""]
    # 고증 출처 표
    L += ["## 고증 출처 표", "", "웹 검색으로 확인한 1987~88년 한국 실물. 상태: 확인 / 일부 확인 / 미확인 / 추측. '(검색 요약)'은 원문을 열지 못하고 검색 결과 요약만 본 것이다. research/notes.md의 기존 고증(난지도 시각 고증 [A] 등)은 그 문서에 있다.", "",
          "| 소품 | 확인 내용 | 출처 | 상태 |", "|---|---|---|---|"]
    names = {p["id"]: p["name"] for p in P}
    for pid, rows in RES.items():
        for f, s, st in rows:
            L.append(f"| {cell(names.get(pid, pid))} | {cell(f)} | {cell(s)} | {st} |")
    L += ["", "## 대본 시대 착오 의심", "", "대본은 고치지 않았다. 판단은 사용자 몫.", ""]
    L += [f"- **{cell(w)}** (`{pid}`): {cell(why)}" for pid, w, why in ANACHRONISM] + [""]
    L += ["## 그림에서 피할 시대 착오(대본 밖)", "", "대본에는 없지만 GPT가 요즘 물건으로 그리기 쉬운 것. 조사에서 나온 주의점.", ""] + [f"- {x}" for x in GUARD] + [""]
    L += ["## 디자인 판단(애매했던 곳)", ""] + [f"- {j}" for j in JUDG] + [""]
    # 등급별 절
    for t in "ABC":
        ps = [p for p in P if p["tier"] == t]
        L += [f"## {TIER[t]} ({len(ps)})", ""]
        if t == "A":
            for p in ps:
                L += [f"### {p['name']} `{p['id']}`", "",
                      "| 별칭 | 시대 | 재질 | 크기 | 색 | 낡음·상태 | 등장 씬 |", "|---|---|---|---|---|---|---|",
                      f"| {cell(', '.join(p['aliases']))} | {cell(p['era'])} | {cell(p['material'])} | {cell(p['size'])} | {' '.join(p['colors'])} | {cell(p['condition'])} | {comp(p['scenes'])} |", "",
                      f"- 형태: {p['shape']}", f"- 역할: {p['role']}", f"- 고증: {p['ref']}"]
                if p.get("offscreen"): L.append(f"- 화면 밖(소리·대사만): {p['offscreen']}")
                if p.get("notes"): L.append(f"- 메모: {p['notes']}")
                L += ["", "| 상태 키 | 단계 | 씬 | 바뀌는 점 |", "|---|---|---|---|"]
                for s in p["states"]:
                    L.append(f"| `{s['key']}` | {cell(s['label'])} | {comp(s['scenes'])} | {cell(s['change'])} |")
                L.append("")
        else:
            L += ["| id | 이름 | 재질 | 크기 | 색 | 형태·낡음 | 역할 | 등장 씬 | 고증 |", "|---|---|---|---|---|---|---|---|---|"]
            for p in ps:
                extra = (f" 화면 밖: {p['offscreen']}." if p.get("offscreen") else "") + (f" 메모: {p['notes']}" if p.get("notes") else "")
                L.append(f"| `{p['id']}` | {cell(p['name'])} | {cell(p['material'])} | {cell(p['size'])} | {' '.join(p['colors'])} | {cell(p['shape'] + ' / ' + p['condition'])} | {cell(p['role'] + extra)} | {comp(p['scenes'])} | {cell(p['ref'])} |")
            L.append("")
    if True:
        L += ["## 시대 착오 점검(C 등급)", "", "C 등급은 '그 시기에 있었나, 모양이 달랐나'만 봤다. 2003·1970년대·1950년대 소품은 프롬프트 끝 시대 표기를 그 시대로 바꿨다.", ""]
        for p in P:
            if p["tier"] == "C" and p.get("research"):
                for r in p["research"]:
                    L.append(f"- {p['name']}: {r['fact']} — {r['source']} ({r['status']})")
        L.append("- 그 밖의 C 소품: 1987~88 서울에 흔했던 물건이거나(분필·칠판·주판·가위·행주 등) 회상·2003년 소품으로 시대 표기를 맞췄다. 개별 출처는 미확인.")
        L.append("")
    return "\n".join(L)


def prompts():
    L = ["# 소품 이미지 프롬프트 — 깡통 바이올린 (G8)", "",
         "1. 한 번에 하나씩 붙여 넣는다(소품 시트 하나 = 프롬프트 하나). 그림체 문구는 이미 들어 있으니 덧붙이지 않는다.",
         "2. 생성 결과는 `renders/props/<id>.png`로 저장한다(상태 단계는 `<상태 키>.png`, 예: `renders/props/dongguri__s2_thrown.png`). 콘티 단계에서 이 파일을 참조한다.",
         "3. A 등급(상태별) → B → C 순. '기본 시트와 같음'이라고 적힌 상태는 따로 만들지 않고 기본 그림을 쓴다.", ""]
    for t in "ABC":
        L += [f"## {TIER[t]}", ""]
        for p in [x for x in P if x["tier"] == t]:
            L += [f"### [{p['id']}] {p['name']} — {comp(p['scenes'])}", "", "```", p["prompt_en"], "```", ""]
            for s in p.get("states", []):
                L.append(f"### [{s['key']}] {p['name']} · {s['label']} — {comp(s['scenes'])}")
                L.append("")
                if s["prompt_en"] == p["prompt_en"]:
                    L += [f"기본 시트와 같음 → `renders/props/{p['id']}.png`를 쓴다. 바뀌는 점: {s['change']}", ""]
                else:
                    L += ["```", s["prompt_en"], "```", ""]
    return "\n".join(L)


if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "design", "gen"), exist_ok=True)
    open(os.path.join(ROOT, "design", "props.md"), "w", encoding="utf-8").write(md())
    open(os.path.join(ROOT, "design", "gen", "prop_prompts.md"), "w", encoding="utf-8").write(prompts())
    print("md written")
