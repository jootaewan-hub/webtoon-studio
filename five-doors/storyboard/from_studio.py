#!/usr/bin/env python3
"""스튜디오 프로젝트(webtoon-story-studio) → 킷 입력 만들기.

킷 폴더가 스튜디오 프로젝트의 storyboard/ 일 때(G9) 쓴다. 표준 라이브러리만 쓴다.

  cd <프로젝트>/storyboard
  python3 from_studio.py            # 아래 파일을 다시 만든다
  python3 kit.py import --replace && python3 kit.py validate && python3 kit.py prompts --track all

만드는 것 (원본 문장은 한 글자도 바꾸지 않는다)
  source/novel.md       ← ../story/novel.md
  source/storyboard.md  ← parts/ep*.md 합본(회차 번호 순)
  data/characters.json  ← ../design/characters.json(id·name) + ../handoff/characters/<id>.md 의 CHARACTER LOCK
                           (LOCK 파일이 없으면 characters.json의 외형 필드로 한 문단을 만든다)
  data/sets.json        ← ../handoff/sets.md 의 장소별 SET LOCK  (`## 1. 이름` / `## 짧게 A. 이름` 아래 `### 1-8. SET LOCK` 코드블록)
  data/tracks.json      ← ../handoff/style_lock.md 의 트랙 1·2·3 문구를 style / style_track2 / style_track3 에 넣는다
                           (금지·수위 규칙 등 나머지 키는 그대로 둔다)
data/style.json, data/flags.json 은 작품마다 손으로 관리한다(덮어쓰지 않음).
"""
import argparse, json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent


def code_block_after(text, heading_re):
    m = re.search(heading_re, text, re.M)
    if not m:
        return None
    b = re.search(r"```text\n(.+?)\n```", text[m.end():], re.S)
    return b.group(1).strip() if b else None


def short_name(name):
    # 한국어 세 글자 이름은 성을 뺀 두 글자를 콘티 표기 이름으로 쓴다(예: 한도겸 → 도겸).
    return name[1:] if re.fullmatch(r"[가-힣]{3}", name) else name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default=str(HERE.parent), help="스튜디오 프로젝트 폴더(기본: 킷 폴더의 상위)")
    a = ap.parse_args()
    P = Path(a.project)
    DATA, SRC = HERE / "data", HERE / "source"
    DATA.mkdir(exist_ok=True); SRC.mkdir(exist_ok=True)
    log = []

    # 1. 원본
    novel = (P / "story/novel.md").read_text(encoding="utf-8")
    (SRC / "novel.md").write_text(novel, encoding="utf-8")
    title = re.search(r"^# (.+)$", novel, re.M)
    title = title.group(1).strip() if title else P.name
    parts = sorted((HERE / "parts").glob("ep*.md"), key=lambda p: int(re.sub(r"\D", "", p.stem) or 0))
    head = (f"# {title} — 웹툰 콘티(G9)\n\n"
            "컷 번호는 `회차-세자리`, 표지는 `0-001`부터. 형식 규격은 storyboard/SPEC.md(없으면 킷 references/storyboard_spec.md).\n"
            "원작 대사·내레이션은 story/novel.md 원문 그대로이며, 순수한 동작·시각 묘사는 화면·연출 칸의 그림 지시로 옮겼다.\n")
    (SRC / "storyboard.md").write_text(head + "\n\n" + "\n\n".join(p.read_text(encoding="utf-8").strip() for p in parts) + "\n",
                                       encoding="utf-8")
    log.append(f"source: novel.md, storyboard.md({len(parts)}개 회차 파일)")

    # 2. 인물
    dc = P / "design/characters.json"
    chars = []
    if dc.exists():
        for ch in json.loads(dc.read_text(encoding="utf-8")):
            cid, full = ch.get("id"), ch.get("name", "")
            name = ch.get("short") or short_name(full)
            aliases = [x for x in [full] + ch.get("aliases", []) if x and x != name]
            lock = None
            lf = P / f"handoff/characters/{cid}.md"
            if lf.exists():
                lock = code_block_after(lf.read_text(encoding="utf-8"), r"^##\s*\d*\.?\s*CHARACTER LOCK")
            if not lock:
                bits = [f"{full}, fictional adult character, not resembling any real person", ch.get("age", ""), ch.get("height", ""),
                        ch.get("build", ""), f"hair {ch.get('hair', '')} {ch.get('hair_color', '')}", f"skin {ch.get('skin', '')}", ch.get("face", "")]
                lock = ", ".join(b for b in bits if b and b.strip())
                log.append(f"[주의] {cid}: CHARACTER LOCK 파일 없음 → characters.json 필드로 대체")
            chars.append({"id": cid, "name": name, "aliases": aliases, "look": lock,
                          "lock_file": f"handoff/characters/{cid}.md" if lf.exists() else ""})
        (DATA / "characters.json").write_text(json.dumps(chars, ensure_ascii=False, indent=2), encoding="utf-8")
        log.append(f"인물 {len(chars)}명")

    # 3. 장소 SET LOCK
    sm = P / "handoff/sets.md"
    if not sm.exists():
        sm = P / "design/sets.md"
    sets = {}
    if sm.exists():
        t = sm.read_text(encoding="utf-8")
        for m in re.finditer(r"^## (\d+|짧게 [A-Z]|[A-Z])\. (.+)$", t, re.M):
            key, name = m.group(1), m.group(2).strip()
            sec_id = key if key.isdigit() else key[-1]
            lock = code_block_after(t[m.start():], rf"^### {re.escape(sec_id)}-\d+\. SET LOCK")
            if lock:
                sets[key] = {"name": name, "lock": lock}
        (DATA / "sets.json").write_text(json.dumps(sets, ensure_ascii=False, indent=2), encoding="utf-8")
        log.append(f"장소 SET LOCK {len(sets)}곳")

    # 4. 트랙 문구
    sl = P / "handoff/style_lock.md"
    tp = DATA / "tracks.json"
    if sl.exists() and tp.exists():
        s = sl.read_text(encoding="utf-8")
        tracks = json.loads(tp.read_text(encoding="utf-8"))
        main_track = "webtoon_adult" if "webtoon_adult" in tracks["tracks"] else next(iter(tracks["tracks"]))
        for key, rx in (("style", r"^## 트랙 1"), ("style_track2", r"^## 트랙 2"), ("style_track3", r"^## 트랙 3")):
            txt = code_block_after(s, rx)
            if txt:
                tracks["tracks"][main_track][key] = txt
        if "shorts" in tracks["tracks"]:
            t3 = code_block_after(s, r"^## 트랙 3")
            if t3:
                tracks["tracks"]["shorts"]["style"] = t3
        tp.write_text(json.dumps(tracks, ensure_ascii=False, indent=2), encoding="utf-8")
        log.append(f"트랙 문구 → tracks.json({main_track})")
    print(" / ".join(log))


if __name__ == "__main__":
    main()
