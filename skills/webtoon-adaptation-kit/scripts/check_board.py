#!/usr/bin/env python3
"""웹툰 콘티 자동 검사: 형식·번호·크기·샷 표기 + 원작 대사/내레이션 대조.

  python3 check_board.py <프로젝트> <회차> [--list]
  python3 check_board.py --board 콘티.md --novel 소설.md [--ep N] [--list]

기본 경로: <프로젝트>/storyboard/parts/ep<N>.md, 소설은 <프로젝트>/story/parts/novel_ep<N>.md
(없으면 story/novel.md에서 '## N화' 절을 잘라 쓴다).
출력 JSON의 '형식 문제'와 '대사 누락'이 0이어야 통과. --list는 대사 칸에 원문이 없는 내레이션 문장을 보여 준다
(해설·내면 문장이 빠졌으면 넣고, 순수한 동작·시각 묘사는 화면 칸 반영으로 충분하다).
표준 라이브러리만 쓴다.
"""
import argparse, json, os, re

SHOTS = {"ECU", "CU", "BS", "MS", "FS", "LS", "ELS", "INS", "TXT"}
ANGLES = ["아이레벨", "로우", "하이", "부감", "앙각", "POV", "측면", "뒷모습", "오버숄더"]


def norm(s):
    s = s.replace("...", "…").replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"\*+", "", s)  # 원문의 굵게·기울임 표시
    s = re.sub(r"\s+", "", s)
    return re.sub(r"[.,!?…~·\-—–'\"()]", "", s)


def novel_for(project, ep):
    p = os.path.join(project, f"story/parts/novel_ep{ep}.md")
    if os.path.exists(p):
        return open(p, encoding="utf-8").read()
    full = open(os.path.join(project, "story/novel.md"), encoding="utf-8").read()
    parts = re.split(r"^## ", full, flags=re.M)
    for part in parts:
        if re.match(rf"{ep}\s*(화|장)", part):
            return part
    raise SystemExit(f"{ep}화 소설을 찾지 못함")


def check(board, novel, ep, show=False):
    probs, rows, scenes, expect = [], [], 0, {}
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
        cid = cells[0]; pre, num = cid.split("-"); n = int(num)
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
            parts = [p.strip() for p in cells[2].split("·", 2)]
            if len(parts) < 3:
                probs.append(f"L{i} {cid} 샷·앵글·인물 3요소 아님: {cells[2][:40]}")
            else:
                if parts[0] not in SHOTS:
                    probs.append(f"L{i} {cid} 샷 코드 오류: {parts[0]}")
                if not any(parts[1].startswith(a) for a in ANGLES):
                    probs.append(f"L{i} {cid} 앵글 오류: {parts[1]}")
                if "·" in re.sub(r"\([^)]*\)", "", parts[2]):  # 위치 괄호 밖의 '·'는 인물 나열 오류
                    probs.append(f"L{i} {cid} 인물을 '·'로 나열함(쉼표로 구분: 유진(우), 미란(우))")
        if len(cells) >= 5 and not cells[4]:
            probs.append(f"L{i} {cid} 대사 칸 비어 있음((무음)이라도 써야 함)")
        rows.append(cells)
    sizes = [int(re.match(r"^800×(\d+)$", r[1]).group(1)) for r in rows if re.match(r"^800×(\d+)$", r[1])]
    main_cuts = [r for r in rows if r[0].startswith(f"{ep}-")] if ep else rows
    dialog_col = norm(" ".join(r[4] for r in rows if len(r) >= 5))
    all_col = norm(" ".join(" ".join(r[2:]) for r in rows))
    quotes = re.findall(r'"([^"\n]+)"', novel) + re.findall(r"“([^”\n]+)”", novel)
    miss_q = [q for q in quotes if norm(q) and norm(q) not in dialog_col]
    body = "\n".join(l for l in novel.splitlines() if not l.startswith("#"))
    body = re.sub(r'"[^"\n]+"', "\n", body)
    sents = [x.strip() for x in re.split(r"(?<=[.!?…])\s+|\n+", body) if len(x.strip()) >= 6]
    miss_n = [x for x in sents if norm(x) not in dialog_col]
    rep = {"ep": ep, "본편 컷": len(main_cuts), "전체 컷": len(rows), "장면": scenes, "형식 문제": len(probs),
           "트랙2": sum(1 for r in rows if len(r) > 3 and "[트랙2]" in r[3]),
           "트랙3": sum(1 for r in rows if len(r) > 3 and "[트랙3]" in r[3]),
           "높이 합(px)": sum(sizes), "원작 대사 수": len(quotes), "대사 누락": len(miss_q),
           "내레이션 문장 수": len(sents), "대사 칸에 원문 없음": len(miss_n),
           "(그중 화면 칸에도 원문 없음)": len([x for x in miss_n if norm(x) not in all_col])}
    print(json.dumps(rep, ensure_ascii=False))
    for p in probs[:60]:
        print("  형식:", p)
    for q in miss_q:
        print("  대사 누락:", q)
    if show:
        for x in miss_n:
            print("  내레이션 미수록:", x)
    return rep


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project", nargs="?")
    ap.add_argument("ep", nargs="?", type=int)
    ap.add_argument("--board"); ap.add_argument("--novel"); ap.add_argument("--ep", dest="ep_opt", type=int)
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    if a.board:
        board = open(a.board, encoding="utf-8").read()
        novel = open(a.novel, encoding="utf-8").read() if a.novel else ""
        check(board, novel, a.ep_opt or a.ep, a.list)
    else:
        board = open(os.path.join(a.project, f"storyboard/parts/ep{a.ep}.md"), encoding="utf-8").read()
        check(board, novel_for(a.project, a.ep), a.ep, a.list)


if __name__ == "__main__":
    main()
