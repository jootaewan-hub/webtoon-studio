"""G9 콘티 조각 합치기: storyboard/parts/ep1·ep2·ep3a·ep3b.md → storyboard/source/storyboard.md (+ 사양 jsonl 재번호).

  python tools/sb_merge.py

- ep3b의 임시 번호(3-201…)를 ep3a 다음 번호로 바꾸고, 사양 cut_spec_ep3a·3b를 cut_spec_ep3.jsonl로 합친다(원본 조각 사양은 지운다).
- 조각 끝 '## 작업 메모' 절은 콘티에서 떼어 storyboard/source/work_notes.md로 모은다.
- 이미 storyboard.md가 있으면 storyboard_prev.md로 남긴다.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SB = ROOT / "storyboard"
PARTS = ["ep1", "ep2", "ep3a", "ep3b"]

HEAD = """# 깡통 바이올린 — 웹툰 콘티 (G9)

- 정본 대본 `story/script.md`(애니형 80씬)를 웹툰 컷으로 옮겼다. 규격은 `storyboard/SPEC.md`(밀도 B안: 컷당 말풍선 최대 3개, 소리 색 컷은 단독).
- 대사·내레이션은 대본(= 소설 대사)을 글자 그대로 옮겼다. 대본의 연기 메모는 화면·연출 칸에 있다. 원작의 '○○가 말했다' 같은 화자 지시문은 말풍선이 화자를 보여 주므로 옮기지 않는다.
- 내레이션은 모두 어른 은주의 회고 목소리다. 소리 색 `SFX(색 HEX)`는 `design/style_guide.md` 2절 규칙을 따른다.
- 컷마다 GPT용 영어 사양이 `storyboard/source/cut_spec_ep*.jsonl`에 있다. 조립된 프롬프트는 `storyboard/out/cel/`에 있다.
"""


def split_notes(md):
    m = re.search(r"^## 작업 메모.*$", md, re.M)
    return (md[:m.start()].rstrip() + "\n", md[m.start():].strip() + "\n") if m else (md.rstrip() + "\n", "")


def main():
    texts, notes = {}, []
    for p in PARTS:
        f = SB / "parts" / f"{p}.md"
        if not f.exists():
            raise SystemExit(f"조각 없음: {f}")
        body, note = split_notes(f.read_text(encoding="utf-8"))
        texts[p] = body
        if note:
            notes.append(note)
    last3a = max(int(m.group(1)) for m in re.finditer(r"^\|\s*3-(\d{3})\s*\|", texts["ep3a"], re.M))
    mapping = {}
    for m in re.finditer(r"^\|\s*3-(\d{3})\s*\|", texts["ep3b"], re.M):
        old = int(m.group(1))
        mapping[f"3-{old:03d}"] = f"3-{last3a + 1 + len(mapping):03d}"
    texts["ep3b"] = re.sub(r"^(\|\s*)(3-\d{3})(\s*\|)", lambda m: m.group(1) + mapping.get(m.group(2), m.group(2)) + m.group(3),
                           texts["ep3b"], flags=re.M)
    out = SB / "source" / "storyboard.md"
    if out.exists():
        out.replace(SB / "source" / "storyboard_prev.md")
    out.write_text(HEAD + "\n" + "\n".join(texts[p] for p in PARTS), encoding="utf-8")
    (SB / "source" / "work_notes.md").write_text("# G9 콘티 작업 메모 (작가 조각별)\n\n" + "\n".join(notes), encoding="utf-8")
    src = SB / "source"
    a, b = src / "cut_spec_ep3a.jsonl", src / "cut_spec_ep3b.jsonl"
    if a.exists() and b.exists():
        rows = [l for l in a.read_text(encoding="utf-8").splitlines() if l.strip()]
        for l in b.read_text(encoding="utf-8").splitlines():
            if l.strip():
                d = json.loads(l)
                d["id"] = mapping.get(d["id"], d["id"])
                rows.append(json.dumps(d, ensure_ascii=False))
        (src / "cut_spec_ep3.jsonl").write_text("\n".join(rows) + "\n", encoding="utf-8")
        a.unlink()
        b.unlink()
    n = len(re.findall(r"^\|\s*\d+-\d{3}\s*\|", out.read_text(encoding="utf-8"), re.M))
    print(f"→ {out} ({n}컷), 3화 후반 재번호 {len(mapping)}컷 (3-{last3a + 1:03d}부터)")


if __name__ == "__main__":
    main()
