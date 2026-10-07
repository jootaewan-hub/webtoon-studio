#!/usr/bin/env python3
"""story/direction.md 2부(장면별 연출 포인트)를 웹툰 콘티 데이터에서 다시 만든다.

  python3 five-doors/tools/direction_scenes.py   (저장소 루트 또는 아무 데서나)

입력: storyboard/data/cuts.json, storyboard/data/chapter_notes.json (kit.py import 결과)
출력: story/direction.md 의 '# 2부.' 아래를 통째로 교체한다(1부는 건드리지 않는다).
표준 라이브러리만 쓴다.
"""
import json, re
from collections import OrderedDict, Counter
from pathlib import Path

P = Path(__file__).resolve().parent.parent
cuts = json.loads((P / "storyboard/data/cuts.json").read_text(encoding="utf-8"))
notes = json.loads((P / "storyboard/data/chapter_notes.json").read_text(encoding="utf-8"))

LABELS = ["장소", "조명", "의상", "트랙", "수위 장치", "노출 관리", "감정 목표"]


def memo_fields(memo):
    """연출 메모를 라벨별로 나눈다(구분자 ' · ' 또는 ' / ' 뒤의 라벨)."""
    pos = []
    for lab in LABELS:
        for m in re.finditer(rf"(?:^|\s[·/]\s){re.escape(lab)}\s*[:：(]?", memo):
            pos.append((m.start(), m.end(), lab))
    pos.sort()
    out = {}
    for i, (s, e, lab) in enumerate(pos):
        end = pos[i + 1][0] if i + 1 < len(pos) else len(memo)
        val = memo[e:end].strip(" ·/:：")
        if lab == "장소":
            val = memo[s:end].strip(" ·/")
        out.setdefault(lab, val)
    return out


def bar(h):
    return "▪" if h <= 600 else ("◼" if h < 1200 else "█")


scenes = OrderedDict()
for c in cuts:
    scenes.setdefault((c["chapter"], c["scene"]), []).append(c)

lines = ["# 2부. 장면별 연출 포인트", "",
         "콘티 데이터에서 자동으로 뽑은 표다(`five-doors/tools/direction_scenes.py`). 콘티를 고치면 kit.py import 뒤에 다시 돌린다.", "",
         "- **템포 띠**: 컷 높이 순서. ▪ 짧은 컷(≤600px), ◼ 중간 컷(640~1160px), █ 긴 컷(≥1200px). 왼쪽부터 컷 순서다.",
         "- **샷**: 많이 쓴 샷 크기와 눈에 띄는 앵글(POV·부감·로우·오버숄더·뒷모습).",
         "- **효과음**: 콘티 대사 칸의 SFX를 컷 순서대로 적는다. 표기는 `story/sfx_list.md`를 따른다. **무음**은 대사 칸이 (무음)인 컷이다.",
         "- **목표 감정·조명·수위 처리**: 장면 연출 메모 원문을 그대로 옮긴다.", ""]
chap_now = None
ep_tot = Counter()
for (chap, scene), cs in scenes.items():
    ep_tot[chap] += sum(c["height"] for c in cs)
for (chap, scene), cs in scenes.items():
    if chap != chap_now:
        chap_now = chap
        n = len([c for c in cuts if c["chapter"] == chap])
        lines += ["", f"## {chap} — {n}컷, 높이 합 {ep_tot[chap]:,}px", ""]
    memo = notes.get(f"{chap} / {scene}", "")
    f = memo_fields(memo)
    hs = [c["height"] for c in cs]
    shots = Counter(re.match(r"\s*(\w+)", c["shot"]).group(1) for c in cs if c.get("shot"))
    angles = Counter()
    for c in cs:
        parts = c.get("shot", "").split("·")
        if len(parts) > 1:
            a = parts[1].strip()
            for key in ("POV", "부감", "로우", "오버숄더", "뒷모습", "앙각", "하이"):
                if a.startswith(key):
                    angles[key] += 1
    sfx, silent, t2, t3 = [], [], [], []
    for c in cs:
        for l in c["lines"]:
            if l["type"] == "sfx":
                spec = re.search(r"\((.*?)\)", l["speaker"])
                sfx.append(f"{l['text']}{'('+spec.group(1)+')' if spec else ''} {c['id']}")
        if any(l["text"] == "(무음)" for l in c["lines"]) or not c["lines"]:
            silent.append(c["id"])
        if "[트랙2]" in c["screen"]:
            t2.append(c["id"])
        if "[트랙3]" in c["screen"]:
            t3.append(c["id"])
    longest = max(cs, key=lambda c: c["height"])
    lines.append(f"### {scene}")
    lines.append(f"- 컷: {cs[0]['id']} ~ {cs[-1]['id']} ({len(cs)}컷, 높이 합 {sum(hs):,}px, 최장 {longest['id']} {longest['height']}px)")
    if f.get("감정 목표"):
        lines.append(f"- 목표 감정: {f['감정 목표']}")
    lines.append(f"- 템포 띠: {''.join(bar(h) for h in hs)}")
    sh = ", ".join(f"{k} {v}" for k, v in shots.most_common(4))
    an = ", ".join(f"{k} {v}" for k, v in angles.most_common())
    lines.append(f"- 샷: {sh}" + (f" / 앵글: {an}" if an else ""))
    if f.get("조명"):
        lines.append(f"- 조명·색: {f['조명']}")
    if f.get("트랙") or t2 or t3:
        tr = f.get("트랙", "1")
        extra = (f" — 트랙2 컷 {', '.join(t2)}" if t2 else "") + (f" — 트랙3 컷 {', '.join(t3)}" if t3 else "")
        lines.append(f"- 트랙: {tr}{extra}")
    lines.append(f"- 효과음: {' / '.join(sfx) if sfx else '없음'}" + (f" · 무음 컷: {', '.join(silent)}" if silent else ""))
    safety = f.get("수위 장치") or f.get("노출 관리")
    if safety:
        lines.append(f"- 수위 처리: {safety}")
    if any("child_present" in c.get("flags", []) for c in cs):
        lines.append("- 아이 등장 장면: 관능 요소 없음(킷 child_present 규칙)")
    lines.append("")

doc = (P / "story/direction.md").read_text(encoding="utf-8")
head = doc.split("# 2부. 장면별 연출 포인트")[0].rstrip() + "\n\n"
(P / "story/direction.md").write_text(head + "\n".join(lines) + "\n", encoding="utf-8")
print(f"장면 {len(scenes)}개 기록 → story/direction.md")
