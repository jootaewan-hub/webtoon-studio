#!/usr/bin/env python3
"""콘티 자동 검사: 형식·번호·크기·샷 표기 + 원작 대사/내레이션 대조.
usage: check_board.py <five-doors dir> <ep no> [--list]"""
import re, sys, os, json

SHOTS = {"ECU", "CU", "BS", "MS", "FS", "LS", "ELS", "INS", "TXT"}
ANGLES = ["아이레벨", "로우", "하이", "부감", "앙각", "POV", "측면", "뒷모습", "오버숄더"]


def norm(s):
    s = s.replace("...", "…").replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"\s+", "", s)
    s = re.sub(r"[.,!?…~·\-—–'\"()]", "", s)
    return s


def main():
    root, ep = sys.argv[1], int(sys.argv[2])
    show = "--list" in sys.argv
    board = open(os.path.join(root, f"storyboard/parts/ep{ep}.md"), encoding="utf-8").read()
    novel = open(os.path.join(root, f"story/parts/novel_ep{ep}.md"), encoding="utf-8").read()
    probs, rows, scenes = [], [], 0
    expect = {}
    lines = board.splitlines()
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if s.startswith("#### "):
            scenes += 1
            if not re.match(r"^#### 장면: S#\d+", s):
                probs.append(f"L{i} 장면 소제목에 S# 없음: {s[:60]}")
            nxt = lines[i].strip() if i < len(lines) else ""
            if not nxt.startswith("연출 메모"):
                probs.append(f"L{i} 장면 바로 아래 '연출 메모' 줄 없음")
            continue
        if not s.startswith("|") or s.startswith("|---") or s.startswith("| 컷"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if not re.match(r"^\d-\d{3}$", cells[0]):
            probs.append(f"L{i} 컷 번호 형식 오류: {cells[0][:20]}")
            continue
        if len(cells) != 5:
            probs.append(f"L{i} {cells[0]} 열 수 {len(cells)} (5여야 함, 칸 안의 | 문자 의심)")
        cid = cells[0]
        pre, num = cid.split("-")
        n = int(num)
        if pre in expect and n != expect[pre]:
            probs.append(f"L{i} {cid} 번호 불연속 (기대 {pre}-{expect[pre]:03d})")
        expect[pre] = n + 1
        m = re.match(r"^800×(\d+)$", cells[1])
        if not m:
            probs.append(f"L{i} {cid} 크기 형식 오류: {cells[1]}")
        else:
            h = int(m.group(1))
            if not (360 <= h <= 1800) or h % 40:
                probs.append(f"L{i} {cid} 높이 {h} (360~1800, 40 단위)")
        if len(cells) >= 3:
            parts = [p.strip() for p in cells[2].split("·")]
            if len(parts) < 3:
                probs.append(f"L{i} {cid} 샷·앵글·인물 3요소 아님: {cells[2][:40]}")
            else:
                if parts[0] not in SHOTS:
                    probs.append(f"L{i} {cid} 샷 코드 오류: {parts[0]}")
                if not any(parts[1].startswith(a) for a in ANGLES):
                    probs.append(f"L{i} {cid} 앵글 오류: {parts[1]}")
        if len(cells) >= 5 and not cells[4]:
            probs.append(f"L{i} {cid} 대사 칸 비어 있음((무음)이라도 써야 함)")
        rows.append(cells)
    sizes = [int(re.match(r"^800×(\d+)$", r[1]).group(1)) for r in rows if re.match(r"^800×(\d+)$", r[1])]
    main_cuts = [r for r in rows if r[0].startswith(f"{ep}-")]
    dialog_col = norm(" ".join(r[4] for r in rows if len(r) >= 5))
    all_col = norm(" ".join(" ".join(r[2:]) for r in rows))

    # 원작 대사
    quotes = re.findall(r'"([^"\n]+)"', novel) + re.findall(r"“([^”\n]+)”", novel)
    miss_q = [q for q in quotes if norm(q) and norm(q) not in dialog_col]
    # 내레이션 문장(따옴표 밖, 제목 제외)
    body = "\n".join(l for l in novel.splitlines() if not l.startswith("#"))
    body = re.sub(r'"[^"\n]+"', "\n", body)
    sents = [x.strip() for x in re.split(r"(?<=[.!?…])\s+|\n+", body) if len(x.strip()) >= 6]
    miss_n = [x for x in sents if norm(x) not in dialog_col]
    miss_n_any = [x for x in miss_n if norm(x) not in all_col]
    rep = {
        "ep": ep, "본편 컷": len(main_cuts), "전체 컷": len(rows), "장면": scenes,
        "형식 문제": len(probs), "트랙2": sum(1 for r in rows if "[트랙2]" in r[3]),
        "트랙3": sum(1 for r in rows if "[트랙3]" in r[3]),
        "높이 합(px)": sum(sizes), "원작 대사 수": len(quotes), "대사 누락": len(miss_q),
        "내레이션 문장 수": len(sents), "대사 칸에 원문 없음": len(miss_n),
        "(그중 화면 칸에도 원문 없음)": len(miss_n_any),
    }
    print(json.dumps(rep, ensure_ascii=False))
    for p in probs[:60]:
        print("  형식:", p)
    for q in miss_q:
        print("  대사 누락:", q)
    if show:
        for x in miss_n:
            print("  내레이션 미수록:", x)


if __name__ == "__main__":
    main()
