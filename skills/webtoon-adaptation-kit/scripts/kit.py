#!/usr/bin/env python3
"""webtoon-kit: 소설·콘티·콘티 이미지를 실사 웹툰 / 성인 웹툰 / 쇼츠 / 애니메이션 제작용 패키지로 변환.

사용법 (킷 폴더에서 실행, Python 3.9+, 외부 패키지 불필요):
  python kit.py import  [--novel source/novel.md] [--storyboard source/storyboard.md]
  python kit.py validate
  python kit.py prompts --track webtoon_real|webtoon_adult|shorts|anim|all
  python kit.py editor           # tools/editor_ready.html 생성 (데이터 내장)
  python kit.py merge-edits FILE # 편집기에서 내려받은 cuts.json 병합
  python kit.py shorts-script    # 장별 쇼츠 러프컷 ffmpeg 스크립트
  python kit.py docx             # source/*.md → source/*.docx
  python kit.py thumbs-auto      # 샷·앵글·인물 칸으로 레이아웃 썸네일(SVG) 자동 생성
  python kit.py board            # tools/board.html 썸네일 보드
  python kit.py pack             # outputs/ 를 zip 으로 묶기
"""
import argparse, json, re, sys, zipfile, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
OUT = ROOT / "outputs"
ID_RE = re.compile(r"^(?:\d-\d{2,3}|E-\d{2,3})$")

# 강한 단서: 장면 전체로 전파 / 약한 단서: 해당 컷에만
INTIMATE_STRONG = ["키스", "정사", "맨어깨", "맨살", "맨등", "몸을 섞", "허리를 감", "잇자국", "쇄골", "목덜미", "밀어붙", "가운 깃", "초록 유도등"]
INTIMATE_WEAK = ["단추", "입술", "흘러내", "이불", "속삭임", "삐걱", "옷깃", "숨소리", "뒷머리", "스타킹"]
VIOLENCE_STRONG = ["퍽", "타격", "휘두", "휘둘"]
VIOLENCE_WEAK = ["망치", "무너", "폭력"]
SELFHARM_STRONG = ["유서", "투신", "자살", "강물에", "물속", "헤엄"]
SELFHARM_WEAK = ["강물", "물보라", "가지런히 놓인", "가지런한 구두"]
INTIMATE_KW = INTIMATE_STRONG + INTIMATE_WEAK
VIOLENCE_KW = VIOLENCE_STRONG + VIOLENCE_WEAK
SELFHARM_KW = SELFHARM_STRONG + SELFHARM_WEAK


def load(name, default=None):
    p = DATA / name
    if not p.exists():
        return default
    return json.loads(p.read_text(encoding="utf-8"))


def save(name, obj):
    DATA.mkdir(exist_ok=True)
    (DATA / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------- import ----------
def split_lines(cell):
    """'무진: 대사 / 내레이션: 문장 / SFX: 퍽' -> 구조화 리스트"""
    out = []
    for raw in [s.strip() for s in re.split(r"\s+/\s+", cell) if s.strip()]:
        if raw in ("(대사 없음)",):
            continue
        m = re.match(r"^([^:：]{1,24})[:：]\s*(.+)$", raw)
        speaker, text = (m.group(1).strip(), m.group(2).strip()) if m else ("", raw)
        kind = "dialogue"
        if speaker.startswith("내레이션"):
            kind = "narration"
        elif speaker.upper().startswith("SFX"):
            kind = "sfx"
        elif "(생각)" in speaker:
            kind = "thought"
        elif "(속삭임)" in speaker:
            kind = "whisper"
        elif speaker.startswith(("손글씨", "메모", "차트", "고지문", "초시계", "제목", "말풍선", "타이틀", "TXT", "간판", "자막")):
            kind = "caption"
        out.append({"type": kind, "speaker": speaker, "text": text})
    return out


def flags_for(text, strong_only=False):
    f = []
    for name, strong, weak in (("intimate", INTIMATE_STRONG, INTIMATE_WEAK),
                               ("violence", VIOLENCE_STRONG, VIOLENCE_WEAK),
                               ("self_harm_theme", SELFHARM_STRONG, SELFHARM_WEAK)):
        kws = strong if strong_only else strong + weak
        if any(k in text for k in kws):
            f.append(name)
    return f


def parse_storyboard(md):
    """4열(v1: 컷|크기|화면|대사) 또는 5열(v2: 컷|크기|샷·앵글·인물|화면|대사) 표를 읽는다.
    `### 장`, `#### 장면: …`, `연출 메모: …`를 인식한다."""
    cuts, notes, chapter, scene = [], {}, "", ""
    for line in md.splitlines():
        s = line.strip()
        if s.startswith("#### "):
            scene = re.sub(r"^장면\s*[:：]\s*", "", s[5:].strip())
            continue
        if s.startswith("### "):
            chapter, scene = s[4:].strip(), ""
            continue
        if s.startswith("연출 메모") and chapter:
            key = f"{chapter} / {scene}" if scene else chapter
            notes[key] = s.split(":", 1)[-1].strip()
            continue
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 4 or not ID_RE.match(cells[0]):
            continue
        if len(cells) >= 5:
            cid, size, shot, screen, lines = cells[0], cells[1], cells[2], cells[3], " | ".join(cells[4:])
        else:
            cid, size, shot, screen, lines = cells[0], cells[1], "", cells[2], " | ".join(cells[3:])
        m = re.match(r"(\d+)\s*[×x]\s*(\d+)", size)
        w, h = (int(m.group(1)), int(m.group(2))) if m else (800, 800)
        first = re.split(r"(?<=[.다])\s", screen, maxsplit=1)[0]
        cuts.append({"id": cid, "chapter": chapter, "scene": scene, "width": w, "height": h,
                     "shot": shot, "screen": screen, "summary": first[:60],
                     "lines": split_lines(lines), "flags": flags_for(screen + lines)})
    # 장면 단위 전파: 한 장면에서 하나라도 태그가 붙으면 그 장면 전체 컷에 같은 안전 규칙을 적용
    groups = {}
    for c in cuts:
        groups.setdefault((c["chapter"], c["scene"]), []).append(c)
    for (ch, sc), cs in groups.items():
        memo = notes.get(f"{ch} / {sc}", "")
        union = set(flags_for(sc + memo, strong_only=True))
        for c in cs:
            union |= set(flags_for(c["screen"] + json.dumps(c["lines"], ensure_ascii=False), strong_only=True))
        for c in cs:
            c["flags"] = sorted(union | set(c["flags"]))
    return cuts, notes


def parse_novel(md):
    chapters, cur = [], None
    for line in md.splitlines():
        if line.startswith("## "):
            cur = {"title": line[3:].strip(), "text": ""}
            chapters.append(cur)
        elif cur is not None:
            cur["text"] += line + "\n"
    for c in chapters:
        c["text"] = c["text"].strip()
    return chapters


def cmd_import(a):
    cuts = {c["id"]: c for c in load("cuts.json", [])}
    if a.storyboard and Path(a.storyboard).exists():
        parsed, notes = parse_storyboard(Path(a.storyboard).read_text(encoding="utf-8"))
        if a.replace:
            cuts = {}
        for p in parsed:
            base = cuts.get(p["id"], {})
            base.update({k: v for k, v in p.items()})
            for ext in ("png", "svg"):
                if (ROOT / "thumbs" / f"{p['id']}.{ext}").exists():
                    base["thumb"] = f"thumbs/{p['id']}.{ext}"; break
            else:
                base.setdefault("thumb", f"thumbs/{p['id']}.svg")
            cuts[p["id"]] = base
        save("chapter_notes.json", notes)
        print(f"콘티: {len(parsed)}컷 가져옴")
    elif a.storyboard:
        print(f"[경고] 콘티 파일 없음: {a.storyboard}")
    if a.novel and Path(a.novel).exists():
        ch = parse_novel(Path(a.novel).read_text(encoding="utf-8"))
        save("novel_chapters.json", ch)
        print(f"소설: {len(ch)}개 장 가져옴")
    elif a.novel:
        print(f"[경고] 소설 파일 없음: {a.novel}")
    order = lambda k: (0 if k.startswith("0") else 9 if k.startswith("E") else int(k[0]), k)
    save("cuts.json", [cuts[k] for k in sorted(cuts, key=order)])


# ---------- validate ----------
def cmd_validate(a):
    cuts = load("cuts.json", [])
    ids = [c["id"] for c in cuts]
    probs = []
    if len(ids) != len(set(ids)):
        probs.append("중복 컷 번호가 있습니다.")
    for c in cuts:
        if not c.get("screen"):
            probs.append(f"{c['id']}: 화면·연출 없음 (콘티 import 필요)")
        if not (ROOT / c.get("thumb", "")).exists():
            probs.append(f"{c['id']}: 썸네일 파일 없음")
    print(f"컷 {len(cuts)}개 / 문제 {len(probs)}건")
    for p in probs[:60]:
        print(" -", p)
    tally = {}
    for c in cuts:
        for f in c.get("flags", []):
            tally[f] = tally.get(f, 0) + 1
    print("수위 태그:", tally)


# ---------- prompts ----------
def char_block(text, chars):
    used = [c for c in chars if c["name"] in text or any(al in text for al in c.get("aliases", []))]
    return "\n".join(f"- {c['name']}: {c['look']}" for c in used)


def dur(c):
    chars = sum(len(l["text"]) for l in c.get("lines", []))
    return round(min(8.0, max(1.5, 1.2 + chars * 0.075 + c.get("height", 800) / 1600)), 1)


SHOT_CAM = {"ECU": "slow push-in (macro)", "CU": "slow push-in", "INS": "insert hold, rack focus",
            "BS": "static hold, subtle parallax", "MS": "static hold, subtle parallax",
            "FS": "slow pan", "LS": "slow tilt down", "ELS": "slow tilt down", "TXT": "hold on black/white, text fade"}


def shot_code(c):
    m = re.match(r"\s*(ECU|CU|BS|MS|FS|LS|ELS|INS|TXT)\b", c.get("shot", ""))
    return m.group(1) if m else ""


def camera(c):
    t = c.get("screen", "")
    if "집중선" in t or "SFX(대형" in str(c.get("lines")):
        return "snap zoom + shake 4f"
    if "분할" in t:
        return "cut sequence (split)"
    sc = shot_code(c)
    if sc:
        return SHOT_CAM[sc]
    if "클로즈업" in t:
        return "slow push-in"
    if "원경" in t or c.get("height", 0) >= 1100:
        return "slow tilt down"
    return "static hold, subtle parallax"


def safety(track, c, tracks):
    rules = list(tracks["global_negative"])
    if "intimate" in c.get("flags", []):
        rules += tracks["intimate_rule"]
    if "violence" in c.get("flags", []):
        rules += tracks["violence_rule"]
    if "self_harm_theme" in c.get("flags", []):
        rules += tracks["self_harm_rule"]
    return rules


def prompt_for(track, c, chars, style, tracks):
    t = tracks["tracks"][track]
    who = char_block(c.get("shot", "") + c.get("screen", "") + json.dumps(c.get("lines", []), ensure_ascii=False), chars)
    lines = "\n".join(f"  - [{l['type']}] {l['speaker']}: {l['text']}" if l['speaker'] else f"  - [{l['type']}] {l['text']}" for l in c.get("lines", []))
    neg = "\n".join(f"- {r}" for r in safety(track, c, tracks))
    head = f"## {c['id']} ({c.get('chapter','')}{' / ' + c['scene'] if c.get('scene') else ''})\n" + (f"- 샷·앵글·인물: {c['shot']}\n" if c.get("shot") else "")
    if track in ("webtoon_real", "webtoon_adult"):
        return head + f"""**이미지 프롬프트**
{t['style']}
- 캔버스: {c.get('width',800)}×{c.get('height',800)} (세로 스크롤 컷)
- 시대·장소: {style['era']}
- 화면·연출: {c.get('screen') or c.get('summary','')}
- 등장인물(외형 고정값):
{who or '- (인물 없음 또는 실루엣)'}
- 조명·색: {style['palette_hint']}
- 말풍선·글자는 이미지에 넣지 말 것 (레터링은 후공정)

**레터링(후공정)**
{lines or '  - (없음)'}

**금지·수위**
{neg}
- 참고 썸네일: {c.get('thumb','')}
"""
    if track == "shorts":
        return head + f"""- 길이: {dur(c)}초 / 화면비 9:16 (1080×1920), 원본 컷을 세로로 재프레이밍
- 카메라: {camera(c)}
- 화면: {c.get('screen') or c.get('summary','')}
- 자막·VO:
{lines or '  - (무음)'}
- 금지·수위:
{neg}
"""
    if track == "anim":
        return head + f"""- 샷 길이: {dur(c)}초 @24fps ({int(dur(c)*24)}프레임)
- 카메라: {camera(c)}
- 레이어: BG / 인물 / FX / 레터링
- 연기·화면: {c.get('screen') or c.get('summary','')}
- 대사(립싱크·VO):
{lines or '  - (없음)'}
- 인물 시트:
{who or '- (없음)'}
- 금지·수위:
{neg}
"""
    raise SystemExit(f"알 수 없는 트랙: {track}")


def cmd_prompts(a):
    cuts = load("cuts.json", [])
    chars, style, tracks = load("characters.json", []), load("style.json", {}), load("tracks.json", {})
    names = list(tracks["tracks"]) if a.track == "all" else [a.track]
    for tr in names:
        d = OUT / tr
        d.mkdir(parents=True, exist_ok=True)
        info = tracks["tracks"][tr]
        parts = [f"# {info['title']}\n\n{info['brief']}\n"]
        if tr == "shorts":
            by = {}
            for c in cuts:
                by.setdefault(c.get("chapter", ""), []).append(c)
            for chap, cs in by.items():
                total = round(sum(dur(c) for c in cs), 1)
                parts.append(f"\n# 에피소드: {chap} (예상 {total}초{' — 60초 초과 시 컷 압축 필요' if total > 60 else ''})\n")
                parts += [prompt_for(tr, c, chars, style, tracks) for c in cs]
        else:
            for c in cuts:
                p = prompt_for(tr, c, chars, style, tracks)
                (d / f"{c['id']}.md").write_text(p, encoding="utf-8")
                parts.append(p)
        (d / f"_{tr}_ALL.md").write_text("\n".join(parts), encoding="utf-8")
        print(f"{tr}: {len(cuts)}컷 → {d}")


# ---------- editor ----------
def cmd_editor(a):
    tpl = (ROOT / "tools" / "editor.html").read_text(encoding="utf-8")
    payload = json.dumps({"cuts": load("cuts.json", []), "characters": load("characters.json", []),
                          "style": load("style.json", {}), "tracks": load("tracks.json", {})}, ensure_ascii=False)
    out = ROOT / "tools" / "editor_ready.html"
    out.write_text(tpl.replace("/*__KIT_DATA__*/null", payload.replace("</", "<\\/")), encoding="utf-8")
    print(f"편집기 생성: {out}")


def cmd_merge(a):
    new = json.loads(Path(a.file).read_text(encoding="utf-8"))
    new = new.get("cuts", new)
    cur = {c["id"]: c for c in load("cuts.json", [])}
    for c in new:
        cur[c["id"]] = {**cur.get(c["id"], {}), **c}
    save("cuts.json", list(cur.values()))
    print(f"병합: {len(new)}컷")


def cmd_pack(a):
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    z = ROOT / f"package_{stamp}.zip"
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as f:
        for p in list(OUT.rglob("*")) + list(DATA.glob("*.json")) + list((ROOT / "thumbs").glob("*.png")):
            if p.is_file():
                f.write(p, p.relative_to(ROOT))
    print(f"패키지: {z}")


# ---------- shorts rough-cut ----------
def cmd_shorts_script(a):
    """장별 쇼츠 러프컷용 ffmpeg 스크립트 생성. 이미지 우선순위: renders/shorts > renders/webtoon_real > thumbs"""
    cuts = load("cuts.json", [])
    d = OUT / "shorts_ffmpeg"
    d.mkdir(parents=True, exist_ok=True)
    by = {}
    for c in cuts:
        by.setdefault(c.get("chapter", ""), []).append(c)
    for n, (chap, cs) in enumerate(by.items()):
        sh = ["#!/usr/bin/env bash", "set -e", f"# {chap}", 'cd "$(dirname "$0")/../.."', f"mkdir -p outputs/shorts_ffmpeg/seg{n:02d}"]
        lst = []
        for c in cs:
            img = next((p for p in [f"renders/shorts/{c['id']}.png", f"renders/webtoon_real/{c['id']}.png", c.get("thumb", "")] if p and (ROOT / p).exists()), c.get("thumb", ""))
            t = dur(c); seg = f"outputs/shorts_ffmpeg/seg{n:02d}/{c['id']}.mp4"
            vf = ("scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,"
                  f"zoompan=z='min(zoom+0.0008,1.08)':d={int(t*24)}:s=1080x1920:fps=24,format=yuv420p")
            sh.append(f'ffmpeg -y -loglevel error -loop 1 -i "{img}" -t {t} -vf "{vf}" -r 24 "{seg}"')
            lst.append(f"file '{c['id']}.mp4'")
        (d / f"seg{n:02d}" ).mkdir(exist_ok=True)
        (d / f"seg{n:02d}" / "list.txt").write_text("\n".join(lst) + "\n", encoding="utf-8")
        sh.append(f'ffmpeg -y -loglevel error -f concat -safe 0 -i outputs/shorts_ffmpeg/seg{n:02d}/list.txt -c copy "outputs/shorts_ffmpeg/short_{n:02d}.mp4"')
        sh.append(f'echo "완료: outputs/shorts_ffmpeg/short_{n:02d}.mp4 ({chap})"')
        p = d / f"short_{n:02d}.sh"
        p.write_text("\n".join(sh) + "\n", encoding="utf-8")
        p.chmod(0o755)
    print(f"쇼츠 러프컷 스크립트 {len(by)}개 → {d} (ffmpeg 필요, 무음)")


# ---------- docx ----------
def cmd_docx(a):
    """source/*.md → source/*.docx (읽기·공유용). node+docx 패키지 우선, 없으면 pandoc."""
    import shutil, subprocess
    jobs = [("source/novel.md", "source/novel.docx", "portrait"), ("source/storyboard.md", "source/storyboard.docx", "landscape")]
    js = ROOT / "tools" / "md2docx.js"
    node_ok = shutil.which("node") and js.exists() and subprocess.run(["node", "-e", "require('docx')"], cwd=ROOT, capture_output=True).returncode == 0
    for src, dst, orient in jobs:
        if not (ROOT / src).exists():
            print(f"[건너뜀] {src} 없음"); continue
        if node_ok:
            subprocess.run(["node", str(js), src, dst, orient], cwd=ROOT, check=True)
        elif shutil.which("pandoc"):
            subprocess.run(["pandoc", src, "-o", dst], cwd=ROOT, check=True)
            print(f"wrote {dst} (pandoc, 기본 서식)")
        else:
            print("[실패] node+docx 또는 pandoc이 필요합니다. 설치: npm install docx  (또는 pandoc 설치)"); return


# ---------- thumbnails & board ----------
def cmd_thumbs_auto(a):
    """샷·앵글·인물 칸을 읽어 thumbs/<컷>.svg 레이아웃 썸네일 생성. 같은 이름의 .png가 있으면 그것을 우선 사용."""
    sys.path.insert(0, str(ROOT))
    from thumbgen import svg_for
    cuts = load("cuts.json", [])
    (ROOT / "thumbs").mkdir(exist_ok=True)
    made = 0
    for c in cuts:
        png = ROOT / "thumbs" / f"{c['id']}.png"
        if png.exists() and not a.force:
            c["thumb"] = f"thumbs/{c['id']}.png"; continue
        (ROOT / "thumbs" / f"{c['id']}.svg").write_text(svg_for(c), encoding="utf-8")
        c["thumb"] = f"thumbs/{c['id']}.svg"; made += 1
    save("cuts.json", cuts)
    print(f"썸네일 {made}개 생성 → thumbs/*.svg (PNG가 있는 컷은 PNG 유지)")


def cmd_board(a):
    """tools/board.html: 장·장면별 썸네일 보드(SVG 내장, 단일 파일)."""
    import html as H
    sys.path.insert(0, str(ROOT))
    from thumbgen import svg_for
    cuts = load("cuts.json", [])
    groups = []
    for c in cuts:
        key = (c.get("chapter", ""), c.get("scene", ""))
        if not groups or groups[-1][0] != key:
            groups.append((key, []))
        groups[-1][1].append(c)
    nav, body, last_ch = [], [], None
    for (ch, sc), cs in groups:
        if ch != last_ch:
            anchor = f"c{len(nav)}"; nav.append(f'<a href="#{anchor}">{H.escape(ch)}</a>')
            n = sum(1 for c in cuts if c.get("chapter") == ch)
            body.append(f'<h2 id="{anchor}">{H.escape(ch)} <small>{n}컷</small></h2>'); last_ch = ch
        if sc:
            body.append(f'<h3>{H.escape(sc)}</h3>')
        cards = []
        for c in cs:
            svg = svg_for(c)
            lines = " / ".join((l["speaker"] + ": " if l["speaker"] else "") + l["text"] for l in c.get("lines", []))
            tag = "".join(f'<i class="t {f}">{ {"intimate":"19","violence":"폭력","self_harm_theme":"주의"}[f] }</i>' for f in c.get("flags", []))
            cards.append(f'<figure class="card">{svg}<figcaption><b>{c["id"]}</b><span class="sz">{c["width"]}×{c["height"]}</span>{tag}'
                         f'<p class="shot">{H.escape(c.get("shot",""))}</p><p>{H.escape(c.get("screen",""))}</p>'
                         f'{"<p class=ln>" + H.escape(lines) + "</p>" if lines else ""}</figcaption></figure>')
        body.append('<div class="grid">' + "".join(cards) + "</div>")
    title = a.title
    html = f"""<title>{H.escape(title)}</title><style>
:root{{--page:#EEF0F3;--card:#fff;--text:#1C1F26;--muted:#5D6470;--line:#D3D7DD}}
@media (prefers-color-scheme:dark){{:root:not([data-theme=light]){{--page:#14171C;--card:#1E2228;--text:#E8EAEE;--muted:#9AA1AC;--line:#343A44;color-scheme:dark}}}}
:root[data-theme=dark]{{--page:#14171C;--card:#1E2228;--text:#E8EAEE;--muted:#9AA1AC;--line:#343A44;color-scheme:dark}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--page);color:var(--text);font-family:'Apple SD Gothic Neo','Malgun Gothic','Noto Sans KR',sans-serif}}
.wrap{{max-width:1240px;margin:0 auto;padding:24px 16px 64px}}h1{{font-size:clamp(22px,4vw,32px);margin:0 0 6px}}.lead{{color:var(--muted);font-size:14px;line-height:1.6;margin:0 0 12px;max-width:52em}}
nav{{display:flex;flex-wrap:wrap;gap:6px;position:sticky;top:env(safe-area-inset-top,0px);background:var(--page);padding:8px 0;z-index:2}}nav a{{font-size:12px;color:var(--text);text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:4px 10px;background:var(--card)}}
h2{{margin:36px 0 4px;font-size:22px}}h2 small{{font-size:13px;color:var(--muted);font-weight:400}}h3{{font-size:14px;color:var(--muted);margin:18px 0 8px;font-weight:600}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px;align-items:start}}
.card{{margin:0;background:var(--card);border:1px solid var(--line);border-radius:8px;overflow:hidden}}.card svg{{display:block;width:100%;height:auto}}
figcaption{{padding:8px 10px 10px;font-size:12px;line-height:1.5}}figcaption b{{font-size:14px}}.sz{{color:var(--muted);margin-left:6px}}
.shot{{color:var(--muted);margin:2px 0}}figcaption p{{margin:4px 0 0}}.ln{{border-left:3px solid var(--line);padding-left:6px;color:var(--muted)}}
.t{{font-style:normal;font-size:10px;color:#fff;background:#C93A46;border-radius:3px;padding:0 4px;margin-left:4px}}.t.violence{{background:#6B4A2E}}.t.self_harm_theme{{background:#555}}
</style><div class="wrap"><h1>{H.escape(title)}</h1>
<p class="lead">총 {len(cuts)}컷. 썸네일은 콘티의 '샷·앵글·인물' 칸으로 자동 배치한 구도 러프입니다(인물 크기 = 샷 크기, 위치 = 좌·중·우·전경·후경, 검은 인물 = 실루엣, 흰 상자 = 말풍선 자리, 노란/남색 박스 = 내레이션 자리, 붉은 글자 = 효과음). 세부 연출은 각 카드의 설명이 기준입니다.</p>
<nav>{''.join(nav)}</nav>{''.join(body)}</div>"""
    out = ROOT / "tools" / "board.html"
    out.write_text(html, encoding="utf-8")
    print(f"보드 생성: {out} ({len(cuts)}컷)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    i = sub.add_parser("import"); i.add_argument("--replace", action="store_true", help="기존 cuts.json을 버리고 콘티로 새로 만듦(컷 번호 체계가 바뀌었을 때)"); i.add_argument("--novel", default="source/novel.md"); i.add_argument("--storyboard", default="source/storyboard.md"); i.set_defaults(fn=cmd_import)
    sub.add_parser("validate").set_defaults(fn=cmd_validate)
    p = sub.add_parser("prompts"); p.add_argument("--track", default="all"); p.set_defaults(fn=cmd_prompts)
    sub.add_parser("editor").set_defaults(fn=cmd_editor)
    m = sub.add_parser("merge-edits"); m.add_argument("file"); m.set_defaults(fn=cmd_merge)
    sub.add_parser("pack").set_defaults(fn=cmd_pack)
    sub.add_parser("shorts-script").set_defaults(fn=cmd_shorts_script)
    sub.add_parser("docx").set_defaults(fn=cmd_docx)
    t = sub.add_parser("thumbs-auto"); t.add_argument("--force", action="store_true", help="PNG가 있어도 SVG로 다시 생성"); t.set_defaults(fn=cmd_thumbs_auto)
    b = sub.add_parser("board"); b.add_argument("--title", default="콘티 썸네일 보드"); b.set_defaults(fn=cmd_board)
    a = ap.parse_args()
    import os; os.chdir(ROOT)
    a.fn(a)


if __name__ == "__main__":
    main()
