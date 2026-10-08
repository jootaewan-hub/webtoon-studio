"""G5 대본 점검·합치기 도구 (표준 라이브러리만).

  python tools/script_check.py merge   # story/script_parts/ep{1,2,3}{a,b}.md → story/script.md (S# 재번호, 정본이 있으면 멈춤)
  python tools/script_check.py check   # 소설 대사가 script.md에 있는지, S# 연속인지 점검

--dir 기본값은 이 파일의 상위 폴더(프로젝트 루트).
"""
import argparse
import re
import sys
from pathlib import Path

SCENE_RE = re.compile(r"^S#(\d+)\.", re.M)
QUOTE_RE = re.compile(r"\"([^\"\n]+)\"|“([^”\n]+)”")


def norm(s):
    s = s.replace("...", "…")
    return re.sub(r"[\s ]+", "", s)


def renumber(text, offset):
    return SCENE_RE.sub(lambda m: f"S#{int(m.group(1)) + offset}.", text)


def split_body_log(text):
    """조각을 본문과 변경 기록으로 나눈다."""
    m = re.search(r"^## 변경 기록.*$", text, re.M)
    if not m:
        return text.rstrip(), ""
    return text[: m.start()].rstrip(), text[m.start():].strip()


def merge(root, force=False):
    target = root / "story" / "script.md"
    if target.exists() and "## 1화" in target.read_text(encoding="utf-8") and not force:
        sys.exit("script.md가 이미 있다. 합친 뒤 교정한 정본을 덮어쓰지 않으려면 멈춘다(--force로 강제).")
    parts = root / "story" / "script_parts"
    out = ["# 깡통 바이올린 (가제) — 대본 (애니형)", "",
           "형식 기준: story/script_format.md. 이름표·표기 규칙은 그 문서를 따른다.", ""]
    logs = []
    titles = {1: "1화. 귀신과 깡통", 2: "2화. 버려진 소리", 3: "3화. 깡통 바이올린"}
    for ep in (1, 2, 3):
        out += [f"## {titles[ep]}", ""]
        offset = 0
        for half in ("a", "b"):
            p = parts / f"ep{ep}{half}.md"
            text = p.read_text(encoding="utf-8").replace("\r\n", "\n")
            # 조각 머리의 '## n화' 제목 줄은 버린다
            text = re.sub(r"^## \d화.*\n", "", text, flags=re.M)
            body, log = split_body_log(text)
            nums = [int(n) for n in SCENE_RE.findall(body)]
            body = renumber(body, offset)
            out += [body.strip(), ""]
            if log:
                logs.append(log)
            offset += max(nums) if nums else 0
    out += ["---", "", "## 변경 기록", "", "소설 위치(파일:줄)로 가리킨다. 씬 번호는 합칠 때 다시 매겼다.", ""]
    for log in logs:
        log = re.sub(r"^## 변경 기록", "###", log, flags=re.M)
        out += [log, ""]
    (root / "story" / "script.md").write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print("script.md written")


def check(root):
    script = (root / "story" / "script.md").read_text(encoding="utf-8")
    eps = re.split(r"^## (?=\d화)", script, flags=re.M)
    body_all, _, log = script.partition("\n## 변경 기록")
    ok = True
    # S# 연속성
    for chunk in eps[1:]:
        title = chunk.splitlines()[0]
        chunk = chunk.split("\n## 변경 기록")[0]
        nums = [int(n) for n in SCENE_RE.findall(chunk)]
        if nums != list(range(1, len(nums) + 1)):
            ok = False
            print(f"[S#] {title}: 번호가 끊기거나 중복 {nums}")
        else:
            print(f"[S#] {title}: S#1~{len(nums)} 정상")
    # 대사 대조
    sn = norm(body_all)
    lognorm = norm(log)
    for ep in (1, 2, 3):
        lines = (root / "story" / "parts" / f"ep{ep}.md").read_text(encoding="utf-8").splitlines()
        missing = []
        for i, line in enumerate(lines, 1):
            for m in QUOTE_RE.finditer(line):
                q = m.group(1) or m.group(2)
                nq = norm(q)
                if len(nq) < 2 or nq in sn:
                    continue
                # 줄을 나눠 쓴 경우: 문장 조각이 모두 있으면 통과
                pieces = [norm(x) for x in re.split(r"(?<=[.?!…])\s+", q) if norm(x)]
                if pieces and all(pc in sn for pc in pieces):
                    continue
                flagged = f"ep{ep}.md:{i}" in log
                missing.append((i, q, flagged))
        unexplained = [x for x in missing if not x[2]]
        print(f"[대사] ep{ep}: 누락 {len(missing)}건 (변경 기록 없는 것 {len(unexplained)}건)")
        for i, q, flagged in missing:
            mark = "기록있음" if flagged else "기록없음"
            print(f"   ep{ep}.md:{i} [{mark}] \"{q}\"")
        if unexplained:
            ok = False
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["merge", "check"])
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dir", default=str(Path(__file__).resolve().parent.parent))
    a = ap.parse_args()
    root = Path(a.dir)
    merge(root, a.force) if a.cmd == "merge" else check(root)
