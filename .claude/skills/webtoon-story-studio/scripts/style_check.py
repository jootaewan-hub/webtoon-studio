"""문체 점검 (표준 라이브러리만) — 'AI처럼 읽히는' 문장 후보를 줄 단위로 짚는다. 기준은 webtoon-story-studio 스킬 references/prose_style.md.

  python3 tools/style_check.py story/parts/ep1.md [다른 파일 …]     → 요약 + 후보 줄
  python3 tools/style_check.py --summary story/parts/*.md          → 요약만
  python3 tools/style_check.py --column 4 storyboard/source/storyboard.md   → 표의 n번째 칸만(콘티 화면 칸은 4)

목표 수치를 맞추려고 문장을 늘리지 않는다. 짚힌 줄을 사람이 읽고 고칠지 정한다.
대사(따옴표 안)는 점검하지 않는다. 대사는 인물의 말이라 대본·콘티와 묶여 있다.
"""
import re
import statistics
import sys
from pathlib import Path

CHECKS = [
    ("조각 문장", "서술어 없이 끝난 문장(예: '한 번.' '회청색 하늘.')",
     lambda s: re.search(r"[가-힣]\.$", s) and not re.search(r"(다|요|까|지|네|죠|라|자|오|니|게|야|군|걸|데|며|고)\.$", s) and len(s) < 25),
    ("경구형 끝맺음", "해설로 못 박는 마무리(예: '이것이 인사다.' '그게 전부였다.')",
     lambda s: re.search(r"^(이것|그것|이게|그게|그건|이건|그것은|이것은)[이가은는]?\s.{0,20}(다|였다|이었다)\.$", s) or re.search(r"(전부였다|뿐이었다|셈이었다|법이다|이었다\. ?그뿐)", s)),
    ("의인화·추상 주어", "사물·시간·감정이 사람처럼 움직임(예: '새벽은 소리가 먼저 왔다')",
     lambda s: re.search(r"(새벽|아침|저녁|밤|시간|침묵|정적|공기|기억|마음|슬픔|기쁨|소리|빛|어둠|바람)[은는이가]\s?[^.]{0,12}(왔다|굴러|걸어|기어|번졌다|내려앉|스며|찾아왔|머물렀|삼켰|품었|속삭|웃었|울었|말했다|안았다|감쌌)", s)),
    ("비유 표지", "처럼·듯·마치·같은 — 생활에서 나온 비유인지 확인",
     lambda s: re.search(r"처럼|듯이|듯한|듯 |듯했|마치|같이 |같은 |같았", s)),
    ("감정 해설", "감정을 이름으로 말함 — 몸짓·행동으로 보일 수 있는지",
     lambda s: re.search(r"(슬픔|기쁨|두려움|외로움|그리움|안도|분노|설렘|절망|희망)(이|가|을|를|에|과|와)\s", s)),
    ("번역투", "~에 대한·~을 통해·~에 의해·~의 ~의·그것은",
     lambda s: re.search(r"에 대한|에 대해|을 통해|를 통해|에 의해|에 의한|의 [가-힣]+의 |^그것은 ", s)),
    ("어려운 말", "한자어·외래 전문어 — 쉬운 말이 있으면 바꾼다",
     lambda s: re.search(r"정점|위계|기제|양상|층위|병치|환기|함의|수렴|내재|존재감|감각적|상징적|본질|순간적|무의식|공명|잔향|여운이|정적이", s)),
    ("축약 기호", "가운뎃점(·)·줄표(—)로 잇는 문장",
     lambda s: "·" in s or re.search(r"[가-힣] ?— ?[가-힣]", s)),
]


def narration_sentences(text, column=None):
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        if column:
            if not re.match(r"^\| ?\d-\d{3} ", line):
                continue
            cells = line.split("|")
            line = cells[column] if len(cells) > column else ""
        line = line.strip()
        if not line or line.startswith(("#", "|", "```", "[", "S#", "---")):
            continue
        if re.match(r"^[^\s\t]{1,14}\t", line):  # 대본 대사 줄(이름<탭>대사)
            continue
        line = re.sub(r'"[^"]*"|“[^”]*”|「[^」]*」', "", line)  # 따옴표 안 대사 제외
        for s in re.split(r"(?<=[.?!…])\s+", line):
            s = s.strip()
            if len(re.sub(r"\W", "", s)) >= 2:
                out.append((i, s))
    return out


def run(path, column=None, summary_only=False):
    sents = narration_sentences(Path(path).read_text(encoding="utf-8"), column)
    if not sents:
        print(f"{path}: 서술 문장 없음")
        return
    L = [len(re.sub(r"\s", "", s)) for _, s in sents]
    n = sum(L)
    hits = {name: [] for name, _, _ in CHECKS}
    for ln, s in sents:
        for name, _, fn in CHECKS:
            if fn(s):
                hits[name].append((ln, s))
    print(f"\n## {path}{f' (칸 {column})' if column else ''}")
    print(f"서술 문장 {len(sents)} · 평균 {statistics.mean(L):.1f}자 · 15자 이하 {sum(l <= 15 for l in L) / len(L):.0%} · 40자 이상 {sum(l >= 40 for l in L) / len(L):.0%}")
    print(" · ".join(f"{name} {len(v)} ({len(v) * 1000 / n:.1f}/천자)" for name, v in hits.items()))
    if summary_only:
        return
    for name, desc, _ in CHECKS:
        if hits[name]:
            print(f"\n[{name}] {desc}")
            for ln, s in hits[name][:60]:
                print(f"  {ln}: {s[:90]}")
            if len(hits[name]) > 60:
                print(f"  … 외 {len(hits[name]) - 60}")


if __name__ == "__main__":
    args = sys.argv[1:]
    summary = "--summary" in args
    col = None
    if "--column" in args:
        k = args.index("--column")
        col = int(args[k + 1])
        del args[k:k + 2]
    for p in [a for a in args if not a.startswith("--")]:
        run(p, col, summary)
