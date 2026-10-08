#!/usr/bin/env python3
"""스킬 원본(skills/<이름>/)을 점검하고 사본·패키지를 맞춘다.

  python3 tools/sync_skills.py          # 점검 → .claude/skills/ 사본 갱신 → skills/<이름>.skill 재패키징
  python3 tools/sync_skills.py --check  # 아무것도 쓰지 않고 점검과 어긋남만 보고(어긋나면 종료 코드 1)

원본은 skills/ 하나다. .claude/skills/(Claude Code용)와 skills/*.skill(claude.ai 업로드용)은 이 스크립트로만 만든다.
점검 항목: SKILL.md frontmatter(name=폴더명, description 200자 이하 권장·1024자 이하 필수, < > 금지),
md2docx.js 사본 일치, 캐시 파일(__pycache__, .DS_Store) 제거.
Python 3.9+ 표준 라이브러리만 쓴다.
"""
import argparse, filecmp, re, shutil, sys, zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "skills"
MIRROR = REPO / ".claude" / "skills"
JUNK = ("__pycache__", ".DS_Store")
# 같은 내용이어야 하는 파일 묶음(첫 파일이 기준)
SAME = [["webtoon-story-studio/scripts/md2docx.js",
         "webtoon-adaptation-kit/scripts/md2docx.js",
         "webtoon-adaptation-kit/assets/kit_template/tools/md2docx.js"]]


def skill_dirs():
    return sorted(p for p in SRC.iterdir() if p.is_dir() and (p / "SKILL.md").exists())


def files(d):
    return sorted(p for p in d.rglob("*") if p.is_file() and not any(j in p.parts for j in JUNK))


def check_frontmatter(d, errs, warns):
    t = (d / "SKILL.md").read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    if not m:
        errs.append(f"{d.name}: SKILL.md frontmatter 없음"); return
    fm = dict(l.split(":", 1) for l in m.group(1).splitlines() if ":" in l)
    name, desc = fm.get("name", "").strip(), fm.get("description", "").strip()
    if name != d.name:
        errs.append(f"{d.name}: name({name})이 폴더명과 다름")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name) or "claude" in name or "anthropic" in name:
        errs.append(f"{d.name}: name 형식 위반(소문자·숫자·하이픈 64자, claude/anthropic 금지)")
    if not desc or len(desc) > 1024:
        errs.append(f"{d.name}: description 길이 {len(desc)}자(1~1024자)")
    elif len(desc) > 200:
        warns.append(f"{d.name}: description {len(desc)}자 — claude.ai 도움말 권장 200자 초과")
    if re.search(r"[<>]", desc):
        errs.append(f"{d.name}: description에 < > 문자")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="쓰지 않고 점검만")
    a = ap.parse_args()
    errs, warns, drift = [], [], []

    for d in skill_dirs():
        check_frontmatter(d, errs, warns)
    for group in SAME:
        base = SRC / group[0]
        for other in group[1:]:
            if not filecmp.cmp(base, SRC / other, shallow=False):
                drift.append(f"{other}가 {group[0]}과 다름")
                if not a.check:
                    shutil.copy2(base, SRC / other)
    junk = [p for p in SRC.rglob("*") if p.name in JUNK]
    for p in junk:
        drift.append(f"캐시 파일: {p.relative_to(REPO)}")
        if not a.check:
            shutil.rmtree(p) if p.is_dir() else p.unlink()

    for d in skill_dirs():
        dst = MIRROR / d.name
        same =dst.exists() and [p.relative_to(d) for p in files(d)] == [p.relative_to(dst) for p in files(dst)] \
            and all(filecmp.cmp(p, dst / p.relative_to(d), shallow=False) for p in files(d))
        if not same:
            drift.append(f".claude/skills/{d.name} 사본이 원본과 다름")
        pkg = SRC / f"{d.name}.skill"
        if pkg.exists():
            with zipfile.ZipFile(pkg) as z:
                names = sorted(z.namelist())
                pk_same = names == sorted(f"{d.name}/{p.relative_to(d).as_posix()}" for p in files(d)) and \
                    all(z.read(f"{d.name}/{p.relative_to(d).as_posix()}") == p.read_bytes() for p in files(d))
        else:
            pk_same = False
        if not pk_same:
            drift.append(f"skills/{d.name}.skill 패키지가 원본과 다름")
        if a.check or errs:
            continue
        if not same:
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(d, dst, ignore=shutil.ignore_patterns(*JUNK))
        if not pk_same:
            with zipfile.ZipFile(pkg, "w", zipfile.ZIP_DEFLATED) as z:
                for p in files(d):
                    z.write(p, f"{d.name}/{p.relative_to(d).as_posix()}")

    for e in errs:
        print("[오류]", e)
    for w in warns:
        print("[주의]", w)
    for x in drift:
        print("[어긋남]" if a.check else "[맞춤]", x)
    if errs:
        print("오류가 있어 사본·패키지를 만들지 않았습니다."); sys.exit(2)
    if a.check and drift:
        sys.exit(1)
    print("완료:", ", ".join(d.name for d in skill_dirs()), "— 어긋남 없음" if not drift else f"— {len(drift)}건 처리")


if __name__ == "__main__":
    main()
