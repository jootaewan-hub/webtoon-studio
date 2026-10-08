#!/usr/bin/env python3
"""webtoon-story-studio 작업 도구 (표준 라이브러리만 사용)

python studio.py init <이름>            프로젝트 폴더·템플릿 생성 (이 파일과 md2docx.js를 tools/에 복사)
python studio.py sketch [--variants]    design/characters.json → design/sheets/*.svg
python studio.py props                  design/props.json (+design/props/<id>.svg) → design/props_sheet.svg
python studio.py colorscript            story/beats.json → design/colorscript.svg
python studio.py board                  design/board.html (artifact 규격: <title><style>로 시작)
python studio.py docx                   story/·anim/·design/의 .md → .docx (node + docx 패키지 필요)
python studio.py pack                   프로젝트 zip
모든 명령은 --dir <프로젝트 폴더> 를 받는다(기본: 현재 폴더).
"""
import argparse, base64, datetime, html, json, math, os, re, shutil, subprocess, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
INK = "#1C1F26"
TODAY = datetime.date.today().isoformat()

# ───────────────────────── 공통 ─────────────────────────

def esc(s):
    return html.escape(str(s), quote=True)

def text_w(s, size):
    w = 0.0
    for ch in str(s):
        o = ord(ch)
        w += size if (o >= 0x1100 and not 0xFF61 <= o <= 0xFFDC) else size * 0.56
    return w

def wrap(s, width, size):
    out = []
    for para in str(s).split("\n"):
        line = ""
        for word in re.split(r"(\s+)", para):
            if text_w(line + word, size) <= width:
                line += word
                continue
            if line.strip():
                out.append(line.rstrip())
            line = word.lstrip()
            while text_w(line, size) > width:          # 띄어쓰기 없는 긴 단어
                cut = len(line)
                while cut > 1 and text_w(line[:cut], size) > width:
                    cut -= 1
                out.append(line[:cut]); line = line[cut:]
        out.append(line.rstrip())
    return [l for l in out if l != ""] or [""]

def tspan_block(x, y, s, width, size, fill=INK, weight="normal", lh=1.45, max_lines=None, anchor="start"):
    lines = wrap(s, width, size)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]; lines[-1] = lines[-1].rstrip()[:-1] + "…"
    parts = [f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">']
    for i, l in enumerate(lines):
        parts.append(f'<tspan x="{x}" dy="{0 if i == 0 else size * lh:.1f}">{esc(l)}</tspan>')
    parts.append("</text>")
    return "".join(parts), len(lines) * size * lh

def svg_doc(w, h, body, bg="#FBFAF7"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'font-family="\'Noto Sans KR\',\'Apple SD Gothic Neo\',\'Malgun Gothic\',sans-serif">'
            f'<rect width="{w}" height="{h}" fill="{bg}"/>{body}</svg>')

def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        txt = f.read().strip()
    return json.loads(txt) if txt else default

def write(path, s):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)

def shade(hex_, k):
    """k<0 어둡게, k>0 밝게 (-1..1)"""
    h = hex_.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    try:
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        return hex_
    f = (lambda c: c + (255 - c) * k) if k > 0 else (lambda c: c * (1 + k))
    return "#%02X%02X%02X" % tuple(max(0, min(255, int(f(c)))) for c in (r, g, b))

def luminance(hex_):
    h = hex_.lstrip("#")
    try:
        r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    except ValueError:
        return 0.5
    return 0.299 * r + 0.587 * g + 0.114 * b

# ───────────────────────── init ─────────────────────────

TEMPLATES = {
    "project.md": """# {name} — 접수

| 항목 | 내용 | 상태 |
|---|---|---|
| 원문 | source/original.md | |
| 각색 수준 | (원문 최대 반영 / 모티프만 / 자유 각색) | |
| 등급 | (전체 / 15세 / 성인) | |
| 분량 | (단편 1화 / 3화 / 시즌) | |
| 범위 | (이야기 G1~G5 / 그림 G6~G8 / 화면 G9~G11 / 전부) | |
| 실화·실존 인물 여부 | | |
| 기본값으로 정한 것 | | |
""",
    "decisions.md": """# 결정 로그

| 게이트 | 결정 | 고른 안 | 이유(사용자 말 그대로 있으면 인용) | 상태 | 날짜 |
|---|---|---|---|---|---|
""",
    "source/original.md": "# 원문\n\n(받은 글을 손대지 않고 붙여 넣는다)\n",
    "research/notes.md": """# 고증 노트

| 항목 | 확인 내용 | 출처 | 작품 반영 |
|---|---|---|---|
""",
    "story/pitch.md": "# 기획\n\n## 로그라인\n\n## 장르·톤\n\n## 결말 방향\n\n## 기획 의도\n- 왜 지금:\n- 무엇이 재밌나:\n- 독자:\n",
    "story/bible.md": "# 캐릭터 바이블\n\n## 인물 이름\n- 나이·직업:\n- 욕망(겉):\n- 결핍(속):\n- 비밀:\n- 말버릇·사투리:\n- 대표 대사:\n- 관계:\n- 변화 곡선:\n- 외형 고정값: design/characters.json\n- 연기 포인트:\n",
    "story/synopsis.md": "# 시놉시스\n\n## 회차 구성\n",
    "story/beats.md": "# 비트 시트\n\n| 회차 | 비트 | 장면 | 감정(색 키워드) | 훅 여부 |\n|---|---|---|---|---|\n",
    "story/novel.md": "# 소설\n",
    "story/script.md": "# 대본\n\n## 변경 기록\n",
    "story/direction.md": "# 연출 노트\n\n## 작품 전체 원칙\n\n## 장면별 포인트\n",
    "story/sfx_list.md": "# 효과음·사운드 큐 사전\n\n| 효과음 | 뜻·소리 | 장면 | 글꼴·크기 | 애니/쇼츠 사운드 큐 |\n|---|---|---|---|---|\n",
    "design/style_options.md": "# 그림체 안\n\n## 1안 — \n\n## 2안 — \n\n## 3안 — \n",
    "design/sets.md": "# 배경 설정\n\n## 장소 이름\n- 배치:\n- 시간대별 조명:\n- 대표 색:\n- 반복 소품:\n- 카메라 자리:\n",
    "anim/storyboard_anim.md": "# 애니메이션 콘티\n",
    "anim/sound_cues.md": "# 사운드 큐 시트\n\n| 타임코드 | 샷 | 종류(SFX/BGM/AMB/VO) | 내용 | 메모 |\n|---|---|---|---|---|\n",
}
JSON_TEMPLATES = {
    "story/beats.json": [],
    "design/characters.json": [],
    "design/props.json": [],
    "design/style.json": {"name": "", "line": "", "color": "", "shading": "", "background": "",
                          "proportion": "", "sfx_style": "", "palette": [],
                          "fonts": {"dialogue": "", "narration": "", "sfx": "", "handwriting": ""},
                          "notes": ""},
}

def cmd_init(a):
    root = os.path.abspath(a.name)
    if os.path.exists(root) and os.listdir(root) and not a.force:
        sys.exit(f"이미 있는 폴더입니다: {root} (--force로 빈 템플릿만 채움)")
    name = os.path.basename(root)
    for rel, body in TEMPLATES.items():
        p = os.path.join(root, rel)
        if not os.path.exists(p):
            write(p, body.replace("{name}", name))
    for rel, obj in JSON_TEMPLATES.items():
        p = os.path.join(root, rel)
        if not os.path.exists(p):
            write(p, json.dumps(obj, ensure_ascii=False, indent=2) + "\n")
    for d in ("design/sheets", "design/props", "storyboard"):
        os.makedirs(os.path.join(root, d), exist_ok=True)
    tools = os.path.join(root, "tools"); os.makedirs(tools, exist_ok=True)
    shutil.copy(os.path.abspath(__file__), os.path.join(tools, "studio.py"))
    for cand in (os.path.join(HERE, "md2docx.js"), os.path.join(HERE, "..", "assets", "md2docx.js")):
        if os.path.exists(cand):
            shutil.copy(cand, os.path.join(tools, "md2docx.js")); break
    print(f"생성: {root}\n다음: source/original.md에 원문을 넣고 G0 접수부터 진행 (python tools/studio.py <명령> --dir {a.name})")

# ───────────────────────── 인물 스케치 ─────────────────────────

BUILD = {  # 어깨, 허리, 엉덩이 (머리 높이 배수), 팔 두께
    "slim":    (1.45, 1.05, 1.15, 0.20),
    "average": (1.65, 1.25, 1.30, 0.23),
    "stocky":  (2.00, 1.65, 1.60, 0.30),
    "curvy":   (1.50, 0.98, 1.55, 0.21),
    "petite":  (1.35, 1.00, 1.15, 0.18),
}

def expr_params(label):
    s = str(label)
    table = [
        (("입꼬리", "비웃", "능글", "smirk"), "smirk"),
        (("발랄", "환한", "신남", "활짝", "밝"), "bright"),
        (("유혹", "나른", "요염", "곁눈"), "sultry"),
        (("웃", "미소", "smile"), "smile"),
        (("당황", "놀", "충격", "surprise"), "shock"),
        (("분노", "화", "angry", "격분"), "angry"),
        (("식은땀", "초조", "긴장", "sweat"), "sweat"),
        (("공허", "멍", "허탈"), "blank"),
        (("슬픔", "울", "눈물", "sad"), "sad"),
        (("무표정", "냉정", "neutral", "평온"), "neutral"),
        (("단호", "결의", "진지"), "stern"),
        (("겁", "공포", "두려"), "fear"),
    ]
    for keys, k in table:
        if any(x in s for x in keys):
            return k
    return "neutral"

def hair_paths(style, cx, cy, rx, ry, color, view):
    """머리카락. view: front / tq / side / back. 머리 위에 겹쳐 그린다. (behind, front) 반환"""
    top = cy - ry
    behind, front = [], []
    st = f'fill="{color}" stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"'
    cap = (f'M{cx - rx * 1.06:.1f},{cy - ry * 0.05:.1f} '
           f'C{cx - rx * 1.12:.1f},{top - ry * 0.25:.1f} {cx + rx * 1.12:.1f},{top - ry * 0.25:.1f} {cx + rx * 1.06:.1f},{cy - ry * 0.05:.1f}')
    if style == "bald":
        return "", ""
    if view == "back":
        if style in ("long",):
            behind.append(f'<path d="M{cx - rx * 1.1:.1f},{cy:.1f} Q{cx - rx * 1.25:.1f},{cy + ry * 2.2:.1f} {cx - rx * 0.8:.1f},{cy + ry * 2.6:.1f} L{cx + rx * 0.8:.1f},{cy + ry * 2.6:.1f} Q{cx + rx * 1.25:.1f},{cy + ry * 2.2:.1f} {cx + rx * 1.1:.1f},{cy:.1f} Z" {st}/>')
        front.append(f'<ellipse cx="{cx}" cy="{cy - ry * 0.05:.1f}" rx="{rx * 1.06:.1f}" ry="{ry * 1.03:.1f}" {st}/>')
        if style == "pony":
            front.append(f'<path d="M{cx - rx * 0.18:.1f},{cy - ry * 0.1:.1f} Q{cx - rx * 0.5:.1f},{cy + ry * 1.4:.1f} {cx:.1f},{cy + ry * 1.9:.1f} Q{cx + rx * 0.5:.1f},{cy + ry * 1.4:.1f} {cx + rx * 0.18:.1f},{cy - ry * 0.1:.1f} Z" {st}/>')
            front.append(f'<rect x="{cx - rx * 0.2:.1f}" y="{cy - ry * 0.18:.1f}" width="{rx * 0.4:.1f}" height="{ry * 0.16:.1f}" fill="#C93A46"/>')
        if style == "bob":
            front.append(f'<path d="M{cx - rx * 1.12:.1f},{cy - ry * 0.1:.1f} L{cx - rx * 1.1:.1f},{cy + ry * 0.75:.1f} L{cx + rx * 1.1:.1f},{cy + ry * 0.75:.1f} L{cx + rx * 1.12:.1f},{cy - ry * 0.1:.1f} Z" {st}/>')
        if style == "spiky":
            pts = " ".join(f"{cx - rx * 1.05 + i * rx * 0.35:.1f},{top - (ry * 0.35 if i % 2 else 0) + ry * 0.12:.1f}" for i in range(7))
            front.append(f'<polyline points="{pts}" {st}/>')
        return "".join(behind), "".join(front)

    side_sign = 0 if view == "front" else 1
    if style in ("long", "bob"):
        length = ry * (2.3 if style == "long" else 0.95)
        behind.append(f'<path d="M{cx - rx * 1.12:.1f},{cy - ry * 0.3:.1f} L{cx - rx * 1.18:.1f},{cy + length:.1f} '
                      f'L{cx + rx * 1.18:.1f},{cy + length:.1f} L{cx + rx * 1.12:.1f},{cy - ry * 0.3:.1f} Z" {st}/>')
    if style == "pony" and view in ("tq", "side"):
        bx = cx - rx * 1.05
        behind.append(f'<path d="M{bx + rx * 0.25:.1f},{cy - ry * 0.55:.1f} Q{bx - rx * 0.9:.1f},{cy - ry * 0.2:.1f} {bx - rx * 0.55:.1f},{cy + ry * 1.3:.1f} Q{bx - rx * 0.05:.1f},{cy + ry * 0.4:.1f} {bx + rx * 0.3:.1f},{cy - ry * 0.25:.1f} Z" {st}/>')
    if style == "pony" and view == "front":
        behind.append(f'<path d="M{cx + rx * 0.9:.1f},{cy - ry * 0.5:.1f} Q{cx + rx * 1.6:.1f},{cy:.1f} {cx + rx * 1.25:.1f},{cy + ry * 1.2:.1f} Q{cx + rx * 1.05:.1f},{cy + ry * 0.3:.1f} {cx + rx * 0.85:.1f},{cy - ry * 0.2:.1f} Z" {st}/>')

    if style == "buzz":
        front.append(f'<path d="{cap} Q{cx:.1f},{top + ry * 0.35:.1f} {cx - rx * 1.06:.1f},{cy - ry * 0.05:.1f} Z" {st} opacity="0.85"/>')
    elif style == "spiky":
        pts = [f"{cx - rx * 1.08:.1f},{cy - ry * 0.05:.1f}"]
        n = 7
        for i in range(n + 1):
            x = cx - rx * 1.05 + i * (rx * 2.1 / n)
            y = top - (ry * 0.45 if i % 2 else ry * 0.02)
            pts.append(f"{x:.1f},{y:.1f}")
        pts.append(f"{cx + rx * 1.08:.1f},{cy - ry * 0.05:.1f}")
        pts.append(f"{cx:.1f},{top + ry * 0.5:.1f}")
        front.append(f'<polygon points="{" ".join(pts)}" {st}/>')
    elif style == "slick":
        front.append(f'<path d="{cap} Q{cx + rx * 0.4:.1f},{top + ry * 0.25:.1f} {cx - rx * 1.06:.1f},{cy - ry * 0.05:.1f} Z" {st}/>')
        front.append(f'<path d="M{cx - rx * 0.6:.1f},{top + ry * 0.08:.1f} Q{cx:.1f},{top - ry * 0.05:.1f} {cx + rx * 0.7:.1f},{top + ry * 0.2:.1f}" fill="none" stroke="{shade(color, 0.35)}" stroke-width="1.4"/>')
    else:  # side, pony, long, bob — 앞머리 있는 기본형
        part = cx - rx * 0.35 if side_sign == 0 else cx - rx * 0.05
        front.append(f'<path d="{cap} L{cx + rx * 1.0:.1f},{cy - ry * 0.25:.1f} '
                     f'Q{part + rx * 0.4:.1f},{top + ry * 0.55:.1f} {part:.1f},{top + ry * 0.32:.1f} '
                     f'Q{cx - rx * 0.6:.1f},{top + ry * 0.7:.1f} {cx - rx * 1.0:.1f},{cy - ry * 0.15:.1f} Z" {st}/>')
        if style in ("long", "bob") and view != "side":
            front.append(f'<path d="M{cx - rx * 1.06:.1f},{cy - ry * 0.2:.1f} Q{cx - rx * 1.2:.1f},{cy + ry * 0.4:.1f} {cx - rx * 1.12:.1f},{cy + ry * (0.9 if style == "bob" else 1.6):.1f}" fill="none" stroke="{INK}" stroke-width="1.4"/>')
            front.append(f'<path d="M{cx + rx * 1.06:.1f},{cy - ry * 0.2:.1f} Q{cx + rx * 1.2:.1f},{cy + ry * 0.4:.1f} {cx + rx * 1.12:.1f},{cy + ry * (0.9 if style == "bob" else 1.6):.1f}" fill="none" stroke="{INK}" stroke-width="1.4"/>')
    return "".join(behind), "".join(front)

def face(cx, cy, rx, ry, expr, view, acc, scale=1.0):
    """얼굴 특징. view front/tq/side. cx는 얼굴 중심(3/4은 이미 이동한 값)."""
    s = scale
    out = []
    sw = 1.6 * s
    if view == "side":
        ex = [cx + rx * 0.45]
    elif view == "tq":
        ex = [cx - rx * 0.28, cx + rx * 0.42]
    else:
        ex = [cx - rx * 0.38, cx + rx * 0.38]
    ey = cy + ry * 0.05
    er = rx * 0.11
    my = cy + ry * 0.55
    mx = cx + (rx * 0.5 if view == "side" else rx * 0.08 if view == "tq" else 0)
    mw = rx * (0.22 if view == "side" else 0.3)
    # 눈
    for i, x in enumerate(ex):
        if expr in ("shock", "fear"):
            out.append(f'<circle cx="{x:.1f}" cy="{ey:.1f}" r="{er * 1.5:.1f}" fill="#fff" stroke="{INK}" stroke-width="{sw}"/><circle cx="{x:.1f}" cy="{ey:.1f}" r="{er * 0.45:.1f}" fill="{INK}"/>')
        elif expr == "smile":
            out.append(f'<path d="M{x - er * 1.3:.1f},{ey + er * 0.4:.1f} Q{x:.1f},{ey - er * 1.3:.1f} {x + er * 1.3:.1f},{ey + er * 0.4:.1f}" fill="none" stroke="{INK}" stroke-width="{sw}"/>')
        elif expr == "bright":
            out.append(f'<ellipse cx="{x:.1f}" cy="{ey:.1f}" rx="{er * 1.0:.1f}" ry="{er * 1.45:.1f}" fill="{INK}"/><circle cx="{x + er * 0.35:.1f}" cy="{ey - er * 0.5:.1f}" r="{er * 0.38:.1f}" fill="#fff"/>')
        elif expr in ("blank", "sultry"):
            out.append(f'<path d="M{x - er * 1.3:.1f},{ey:.1f} L{x + er * 1.3:.1f},{ey:.1f}" stroke="{INK}" stroke-width="{sw * 1.3}"/><path d="M{x - er * 0.9:.1f},{ey:.1f} Q{x:.1f},{ey + er * 1.4:.1f} {x + er * 0.9:.1f},{ey:.1f}" fill="{INK}"/>')
        elif expr == "sad":
            out.append(f'<ellipse cx="{x:.1f}" cy="{ey + er * 0.2:.1f}" rx="{er * 0.8:.1f}" ry="{er:.1f}" fill="{INK}"/>')
            if i == 0:
                out.append(f'<path d="M{x:.1f},{ey + er * 1.5:.1f} q{-er * 0.4:.1f},{er * 1.6:.1f} 0,{er * 2.2:.1f} q{er * 0.4:.1f},{-er * 0.6:.1f} 0,{-er * 2.2:.1f}" fill="#8EC8F0" stroke="{INK}" stroke-width="0.8"/>')
        else:
            out.append(f'<ellipse cx="{x:.1f}" cy="{ey:.1f}" rx="{er * 0.85:.1f}" ry="{er * 1.15:.1f}" fill="{INK}"/>')
        # 눈썹
        bx0, bx1 = x - er * 1.6, x + er * 1.6
        by = ey - er * 2.4
        inner_left = (i == 0) if view != "side" else False
        if expr in ("angry", "stern"):
            d = er * (1.4 if expr == "angry" else 0.7)
            y0, y1 = (by - d * 0.3, by + d) if inner_left else (by + d, by - d * 0.3)
        elif expr in ("sad", "fear", "sweat"):
            d = er * 1.0
            y0, y1 = (by + d * 0.5, by - d * 0.6) if inner_left else (by - d * 0.6, by + d * 0.5)
        elif expr == "shock":
            y0 = y1 = by - er
        else:
            y0 = y1 = by
        out.append(f'<path d="M{bx0:.1f},{y0:.1f} L{bx1:.1f},{y1:.1f}" stroke="{INK}" stroke-width="{sw * 1.3}" stroke-linecap="round"/>')
    # 코
    if view == "front":
        out.append(f'<path d="M{cx:.1f},{cy + ry * 0.25:.1f} l{-rx * 0.06:.1f},{ry * 0.12:.1f}" stroke="{INK}" stroke-width="{sw * 0.8}" fill="none"/>')
    elif view == "tq":
        out.append(f'<path d="M{cx + rx * 0.15:.1f},{cy + ry * 0.12:.1f} l{rx * 0.1:.1f},{ry * 0.2:.1f} l{-rx * 0.1:.1f},{ry * 0.03:.1f}" stroke="{INK}" stroke-width="{sw * 0.8}" fill="none"/>')
    # 입
    if expr == "smile":
        out.append(f'<path d="M{mx - mw:.1f},{my:.1f} Q{mx:.1f},{my + ry * 0.18:.1f} {mx + mw:.1f},{my:.1f}" fill="none" stroke="{INK}" stroke-width="{sw}"/>')
    elif expr == "bright":
        out.append(f'<path d="M{mx - mw * 1.1:.1f},{my - ry * 0.03:.1f} Q{mx:.1f},{my + ry * 0.3:.1f} {mx + mw * 1.1:.1f},{my - ry * 0.03:.1f} Z" fill="#9C3B44" stroke="{INK}" stroke-width="{sw}"/>')
    elif expr == "smirk":
        out.append(f'<path d="M{mx - mw:.1f},{my + ry * 0.03:.1f} Q{mx + mw * 0.2:.1f},{my + ry * 0.06:.1f} {mx + mw:.1f},{my - ry * 0.08:.1f}" fill="none" stroke="{INK}" stroke-width="{sw}"/>')
    elif expr in ("shock", "fear"):
        out.append(f'<ellipse cx="{mx:.1f}" cy="{my + ry * 0.04:.1f}" rx="{mw * 0.45:.1f}" ry="{ry * 0.09:.1f}" fill="#5A2228" stroke="{INK}" stroke-width="{sw}"/>')
    elif expr == "angry":
        out.append(f'<path d="M{mx - mw:.1f},{my + ry * 0.06:.1f} Q{mx:.1f},{my - ry * 0.1:.1f} {mx + mw:.1f},{my + ry * 0.06:.1f} Z" fill="#fff" stroke="{INK}" stroke-width="{sw}"/>')
    elif expr == "sweat":
        pts = " ".join(f"{mx - mw + i * mw / 2:.1f},{my + (ry * 0.04 if i % 2 else -ry * 0.02):.1f}" for i in range(5))
        out.append(f'<polyline points="{pts}" fill="none" stroke="{INK}" stroke-width="{sw}"/>')
    elif expr in ("sad",):
        out.append(f'<path d="M{mx - mw:.1f},{my + ry * 0.06:.1f} Q{mx:.1f},{my - ry * 0.08:.1f} {mx + mw:.1f},{my + ry * 0.06:.1f}" fill="none" stroke="{INK}" stroke-width="{sw}"/>')
    elif expr == "sultry":
        out.append(f'<path d="M{mx - mw * 0.8:.1f},{my:.1f} Q{mx:.1f},{my + ry * 0.07:.1f} {mx + mw * 0.9:.1f},{my - ry * 0.03:.1f}" fill="none" stroke="#9C3B44" stroke-width="{sw * 1.5}"/>')
    else:
        out.append(f'<path d="M{mx - mw * 0.8:.1f},{my:.1f} L{mx + mw * 0.8:.1f},{my:.1f}" stroke="{INK}" stroke-width="{sw}"/>')
    # 땀
    if expr in ("sweat", "shock", "fear"):
        sx, sy = cx + rx * 0.95, cy - ry * 0.35
        out.append(f'<path d="M{sx:.1f},{sy:.1f} q{-rx * 0.12:.1f},{ry * 0.25:.1f} 0,{ry * 0.3:.1f} q{rx * 0.12:.1f},{-ry * 0.05:.1f} 0,{-ry * 0.3:.1f}" fill="#BFE3F7" stroke="{INK}" stroke-width="1"/>')
    if expr == "blank":
        out.append(f'<path d="M{cx - rx * 0.6:.1f},{cy - ry * 0.75:.1f} l0,{ry * 0.35:.1f} M{cx - rx * 0.4:.1f},{cy - ry * 0.75:.1f} l0,{ry * 0.3:.1f} M{cx - rx * 0.2:.1f},{cy - ry * 0.75:.1f} l0,{ry * 0.25:.1f}" stroke="#5E7F99" stroke-width="1.2" opacity="0.7"/>')
    # 장신구(얼굴)
    if "glasses" in acc and view != "side":
        r = er * 2.3
        out.append(f'<circle cx="{ex[0]:.1f}" cy="{ey:.1f}" r="{r:.1f}" fill="#DDE8F0" fill-opacity="0.25" stroke="{INK}" stroke-width="{sw}"/>')
        out.append(f'<circle cx="{ex[-1]:.1f}" cy="{ey:.1f}" r="{r:.1f}" fill="#DDE8F0" fill-opacity="0.25" stroke="{INK}" stroke-width="{sw}"/>')
        out.append(f'<path d="M{ex[0] + r:.1f},{ey:.1f} L{ex[-1] - r:.1f},{ey:.1f}" stroke="{INK}" stroke-width="{sw}"/>')
        out.append(f'<path d="M{ex[-1] - r * 0.5:.1f},{ey - r * 0.55:.1f} l{r * 0.5:.1f},{r * 0.35:.1f}" stroke="#fff" stroke-width="{sw}"/>')
    elif "glasses" in acc:
        r = er * 2.3
        out.append(f'<ellipse cx="{ex[0]:.1f}" cy="{ey:.1f}" rx="{r * 0.45:.1f}" ry="{r:.1f}" fill="none" stroke="{INK}" stroke-width="{sw}"/><path d="M{ex[0] - r * 0.45:.1f},{ey:.1f} L{cx - rx * 0.6:.1f},{ey:.1f}" stroke="{INK}" stroke-width="{sw}"/>')
    if "shades" in acc and view != "side":
        w = er * 4.2
        for x in ex:
            out.append(f'<rect x="{x - w / 2:.1f}" y="{ey - er * 1.6:.1f}" width="{w:.1f}" height="{er * 3:.1f}" rx="{er:.1f}" fill="{INK}"/>')
        out.append(f'<path d="M{ex[0]:.1f},{ey - er:.1f} L{ex[-1]:.1f},{ey - er:.1f}" stroke="{INK}" stroke-width="{sw * 1.5}"/>')
    if "scar_r" in acc and view != "side":
        sx = ex[0]
        out.append(f'<path d="M{sx - er * 0.8:.1f},{ey + er * 2:.1f} l{er * 1.6:.1f},{er * 3:.1f}" stroke="#A0505A" stroke-width="{sw * 1.2}"/>'
                   f'<path d="M{sx - er * 0.4:.1f},{ey + er * 3.2:.1f} l{er * 0.9:.1f},{-er * 0.4:.1f}" stroke="#A0505A" stroke-width="{sw * 0.8}"/>')
    return "".join(out)

def figure(c, ox, oy, hh, view, outfit_color=None, expr="neutral"):
    """전신 한 개. ox=중심 x, oy=정수리 y, hh=머리 높이"""
    build = c.get("build", "average")
    sh, wa, hp, aw = BUILD.get(build, BUILD["average"])
    ratio = float(c.get("head_ratio", 7) or 7)
    skin = c.get("skin", "#F2D2B6")
    hair_c = c.get("hair_color", "#2B2F3A")
    o0 = (c.get("outfits") or [{}])[0]
    outf = outfit_color or o0.get("color") or "#8E9AAA"
    bottom = o0.get("bottom", c.get("bottom", "pants"))
    pants = c.get("legwear", skin) if bottom in ("skirt", "long_skirt") else o0.get("pants", shade(outf, -0.25))
    acc = c.get("accessories", [])
    rx, ry = hh * 0.40, hh * 0.5
    H = hh * ratio
    neck_y = oy + hh * 0.98
    sh_y = oy + hh * 1.25
    waist_y = oy + hh * 2.55
    hip_y = oy + hh * (3.3 + (ratio - 7) * 0.4)
    foot_y = oy + H
    st = f'stroke="{INK}" stroke-width="2" stroke-linejoin="round"'
    parts = []
    k = {"front": 1.0, "tq": 0.82, "side": 0.55, "back": 1.0}[view]
    S, W, P = sh * hh / 2 * k, wa * hh / 2 * k, hp * hh / 2 * k
    cx = ox
    # 다리
    leg_w = hh * 0.36 * (1.25 if build == "stocky" else 1.0)
    gap = hh * 0.08 if view != "side" else -leg_w * 0.7
    for sgn in ((-1, 1) if view != "side" else (1, -1)):
        lx = cx + sgn * (gap / 2 + leg_w / 2) if view != "side" else cx + sgn * hh * 0.08
        parts.append(f'<path d="M{lx - leg_w / 2:.1f},{hip_y - hh * 0.1:.1f} L{lx - leg_w * 0.38:.1f},{foot_y - hh * 0.12:.1f} '
                     f'L{lx + leg_w * 0.38:.1f},{foot_y - hh * 0.12:.1f} L{lx + leg_w / 2:.1f},{hip_y - hh * 0.1:.1f} Z" fill="{pants}" {st}/>')
        fx = hh * (0.32 if view == "side" else 0.05)
        parts.append(f'<path d="M{lx - leg_w * 0.42:.1f},{foot_y - hh * 0.14:.1f} L{lx - leg_w * 0.45:.1f},{foot_y:.1f} L{lx + leg_w * 0.45 + fx:.1f},{foot_y:.1f} '
                     f'Q{lx + leg_w * 0.45 + fx:.1f},{foot_y - hh * 0.12:.1f} {lx + leg_w * 0.4:.1f},{foot_y - hh * 0.14:.1f} Z" fill="#2B2F3A" {st}/>')
    # 뒤쪽 팔
    arm_len = hh * 2.75
    def arm(sgn, ax=None):
        if ax is None:
            ax = cx + sgn * (S - aw * hh * 0.35)
        hx = ax + sgn * hh * 0.18
        hy = sh_y + arm_len
        w = aw * hh
        return (f'<path d="M{ax - w / 2:.1f},{sh_y + hh * 0.05:.1f} L{hx - w * 0.42:.1f},{hy - hh * 0.25:.1f} L{hx + w * 0.42:.1f},{hy - hh * 0.25:.1f} L{ax + w / 2:.1f},{sh_y + hh * 0.05:.1f} Z" fill="{outf}" {st}/>'
                f'<ellipse cx="{hx:.1f}" cy="{hy - hh * 0.12:.1f}" rx="{w * 0.48:.1f}" ry="{hh * 0.17:.1f}" fill="{skin}" {st}/>')
    # 상체(몸통)
    if view == "side":
        chest = hh * {"curvy": 0.40, "stocky": 0.38, "petite": 0.28}.get(build, 0.31)
        back = hh * (0.36 if build == "stocky" else 0.30)
        bust = 1.25 if build == "curvy" else 1.0
        belly = 1.0 if build == "stocky" else 0.55
        parts.append(f'<path d="M{cx - back:.1f},{sh_y:.1f} Q{cx + chest * bust:.1f},{sh_y + hh * 0.35:.1f} {cx + chest:.1f},{sh_y + hh * 0.85:.1f} '
                     f'Q{cx + chest * belly:.1f},{waist_y:.1f} {cx + chest * 0.7:.1f},{hip_y:.1f} L{cx - back * 1.1:.1f},{hip_y:.1f} '
                     f'Q{cx - back * 0.75:.1f},{waist_y:.1f} {cx - back:.1f},{sh_y:.1f} Z" fill="{outf}" {st}/>')
    else:
        parts.append(f'<path d="M{cx - S:.1f},{sh_y + hh * 0.08:.1f} Q{cx:.1f},{sh_y - hh * 0.12:.1f} {cx + S:.1f},{sh_y + hh * 0.08:.1f} '
                     f'C{cx + S * 1.02:.1f},{sh_y + hh * 0.8:.1f} {cx + W:.1f},{waist_y - hh * 0.4:.1f} {cx + W:.1f},{waist_y:.1f} '
                     f'Q{cx + P * 1.08:.1f},{(waist_y + hip_y) / 2:.1f} {cx + P:.1f},{hip_y:.1f} L{cx - P:.1f},{hip_y:.1f} '
                     f'Q{cx - P * 1.08:.1f},{(waist_y + hip_y) / 2:.1f} {cx - W:.1f},{waist_y:.1f} '
                     f'C{cx - W:.1f},{waist_y - hh * 0.4:.1f} {cx - S * 1.02:.1f},{sh_y + hh * 0.8:.1f} {cx - S:.1f},{sh_y + hh * 0.08:.1f} Z" fill="{outf}" {st}/>')
        if view != "back":
            parts.append(f'<path d="M{cx - hh * 0.22:.1f},{sh_y - hh * 0.04:.1f} L{cx:.1f},{sh_y + hh * 0.35:.1f} L{cx + hh * 0.22:.1f},{sh_y - hh * 0.04:.1f}" fill="{skin}" {st}/>')
        parts.append(f'<path d="M{cx - W:.1f},{waist_y:.1f} L{cx + W:.1f},{waist_y:.1f}" stroke="{shade(outf, -0.35)}" stroke-width="1.4" stroke-dasharray="4 3"/>')
    # 치마
    if bottom in ("skirt", "long_skirt"):
        hem = hip_y + (foot_y - hip_y) * (0.45 if bottom == "skirt" else 0.82)
        if view == "side":
            parts.append(f'<path d="M{cx - hh * 0.33:.1f},{waist_y:.1f} L{cx + hh * 0.3:.1f},{waist_y:.1f} L{cx + hh * 0.42:.1f},{hem:.1f} L{cx - hh * 0.45:.1f},{hem:.1f} Z" fill="{outf}" {st}/>')
        else:
            fl = P * 1.12
            parts.append(f'<path d="M{cx - W:.1f},{waist_y:.1f} Q{cx - P * 1.05:.1f},{(waist_y + hip_y) / 2:.1f} {cx - P:.1f},{hip_y:.1f} L{cx - fl:.1f},{hem:.1f} L{cx + fl:.1f},{hem:.1f} L{cx + P:.1f},{hip_y:.1f} Q{cx + P * 1.05:.1f},{(waist_y + hip_y) / 2:.1f} {cx + W:.1f},{waist_y:.1f} Z" fill="{outf}" {st}/>')
    # 팔
    if view == "side":
        parts.append(arm(1, ax=cx))
    else:
        parts.append(arm(-1)); parts.append(arm(1))
    # 목
    parts.append(f'<rect x="{cx - hh * 0.13:.1f}" y="{neck_y - hh * 0.1:.1f}" width="{hh * 0.26:.1f}" height="{sh_y - neck_y + hh * 0.12:.1f}" fill="{skin}" {st}/>')
    if "chain" in acc and view != "back":
        parts.append(f'<path d="M{cx - hh * 0.2:.1f},{sh_y:.1f} Q{cx:.1f},{sh_y + hh * 0.42:.1f} {cx + hh * 0.2:.1f},{sh_y:.1f}" fill="none" stroke="#E3BB38" stroke-width="2.4"/>')
    # 머리
    hcx = cx + (hh * 0.06 if view == "tq" else hh * 0.08 if view == "side" else 0)
    hcy = oy + ry
    b, f_ = hair_paths(c.get("hair", "side"), hcx, hcy, rx, ry, hair_c, view)
    parts.append(b)
    if view == "side":
        parts.append(f'<path d="M{hcx - rx * 0.95:.1f},{hcy:.1f} C{hcx - rx:.1f},{hcy - ry * 1.3:.1f} {hcx + rx * 1.1:.1f},{hcy - ry * 1.2:.1f} {hcx + rx * 0.95:.1f},{hcy - ry * 0.1:.1f} '
                     f'L{hcx + rx * 1.12:.1f},{hcy + ry * 0.25:.1f} L{hcx + rx * 0.92:.1f},{hcy + ry * 0.35:.1f} Q{hcx + rx * 0.85:.1f},{hcy + ry * 0.95:.1f} {hcx + rx * 0.2:.1f},{hcy + ry:.1f} '
                     f'Q{hcx - rx * 0.7:.1f},{hcy + ry * 0.8:.1f} {hcx - rx * 0.95:.1f},{hcy:.1f} Z" fill="{skin}" {st}/>')
        parts.append(f'<ellipse cx="{hcx - rx * 0.15:.1f}" cy="{hcy + ry * 0.1:.1f}" rx="{rx * 0.13:.1f}" ry="{ry * 0.2:.1f}" fill="{shade(skin, -0.12)}" {st}/>')
    else:
        parts.append(f'<ellipse cx="{hcx:.1f}" cy="{hcy:.1f}" rx="{rx * (0.95 if view == "tq" else 1):.1f}" ry="{ry:.1f}" fill="{skin}" {st}/>')
    if view != "back":
        parts.append(face(hcx, hcy, rx, ry, expr, view, acc))
    parts.append(f_)
    if "earring" in acc and view in ("front", "tq", "side"):
        exx = hcx - rx * 0.15 if view == "side" else hcx - rx * 0.98
        parts.append(f'<circle cx="{exx:.1f}" cy="{hcy + ry * 0.38:.1f}" r="{hh * 0.05:.1f}" fill="#E3BB38" stroke="{INK}" stroke-width="1"/>')
    if "cap" in acc:
        parts.append(f'<path d="M{hcx - rx * 0.6:.1f},{hcy - ry * 0.85:.1f} L{hcx - rx * 0.45:.1f},{hcy - ry * 1.25:.1f} L{hcx + rx * 0.45:.1f},{hcy - ry * 1.25:.1f} L{hcx + rx * 0.6:.1f},{hcy - ry * 0.85:.1f} Z" fill="#fff" {st}/>'
                     f'<path d="M{hcx - rx * 0.12:.1f},{hcy - ry * 1.08:.1f} h{rx * 0.24:.1f} M{hcx:.1f},{hcy - ry * 1.2:.1f} v{ry * 0.24:.1f}" stroke="#C93A46" stroke-width="2"/>')
    return "".join(parts), H

def head_bust(c, cx, cy, hh, expr):
    """표정 시트용 흉상"""
    skin = c.get("skin", "#F2D2B6"); hair_c = c.get("hair_color", "#2B2F3A")
    outf = (c.get("outfits") or [{}])[0].get("color") or "#8E9AAA"
    acc = c.get("accessories", [])
    rx, ry = hh * 0.40, hh * 0.5
    st = f'stroke="{INK}" stroke-width="2"'
    sh, *_ = BUILD.get(c.get("build", "average"), BUILD["average"])
    S = sh * hh / 2
    by = cy + ry + hh * 0.25
    p = [f'<path d="M{cx - S:.1f},{by + hh * 0.9:.1f} Q{cx - S:.1f},{by:.1f} {cx:.1f},{by - hh * 0.05:.1f} Q{cx + S:.1f},{by:.1f} {cx + S:.1f},{by + hh * 0.9:.1f} Z" fill="{outf}" {st}/>',
         f'<rect x="{cx - hh * 0.13:.1f}" y="{cy + ry * 0.7:.1f}" width="{hh * 0.26:.1f}" height="{hh * 0.35:.1f}" fill="{skin}" {st}/>']
    b, f_ = hair_paths(c.get("hair", "side"), cx, cy, rx, ry, hair_c, "front")
    p += [b, f'<ellipse cx="{cx}" cy="{cy}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{skin}" {st}/>', face(cx, cy, rx, ry, expr, "front", acc), f_]
    if "cap" in acc:
        p.append(f'<path d="M{cx - rx * 0.6:.1f},{cy - ry * 0.85:.1f} L{cx - rx * 0.45:.1f},{cy - ry * 1.25:.1f} L{cx + rx * 0.45:.1f},{cy - ry * 1.25:.1f} L{cx + rx * 0.6:.1f},{cy - ry * 0.85:.1f} Z" fill="#fff" {st}/>')
    if "earring" in acc:
        p.append(f'<circle cx="{cx - rx * 0.98:.1f}" cy="{cy + ry * 0.38:.1f}" r="{hh * 0.05:.1f}" fill="#E3BB38" stroke="{INK}" stroke-width="1"/>')
    return "".join(p)

def char_sheet(c):
    W = 1400
    hh = 46
    ratio = float(c.get("head_ratio", 7) or 7)
    fig_h = hh * ratio
    top = 120
    body = []
    name = c.get("name", c.get("id", "?"))
    adult = c.get("adult")
    title = f'{name}  ·  {c.get("age", "")}'
    body.append(f'<rect x="0" y="0" width="{W}" height="92" fill="{INK}"/>')
    body.append(f'<text x="36" y="56" font-size="34" font-weight="700" fill="#fff">{esc(title)}</text>')
    tag = "성인" if adult else ("나이 미기재" if adult is None else "")
    if tag:
        body.append(f'<rect x="{W - 190}" y="28" width="150" height="38" rx="19" fill="{"#3FAE6A" if adult else "#C93A46"}"/><text x="{W - 115}" y="54" font-size="18" fill="#fff" text-anchor="middle" font-weight="700">{tag}</text>')
    body.append(f'<text x="36" y="82" font-size="14" fill="#C9CED6">턴어라운드 러프 — 비율·실루엣·특징 위치 확인용 (완성 작화 아님)</text>')
    # 등신 가이드
    gx0, gx1 = 30, 30 + 4 * 230
    for i in range(int(math.ceil(ratio)) + 1):
        y = top + 20 + i * hh
        if y > top + 20 + fig_h + 1:
            break
        body.append(f'<line x1="{gx0}" y1="{y}" x2="{gx1}" y2="{y}" stroke="#D5D9DF" stroke-dasharray="3 5"/>'
                    f'<text x="{gx0 - 2}" y="{y + hh / 2 + 4:.0f}" font-size="11" fill="#9AA1AC" text-anchor="end">{i + 1 if i < ratio else ""}</text>')
    for i, (v, label) in enumerate((("front", "정면"), ("tq", "3/4"), ("side", "측면"), ("back", "뒷모습"))):
        cx = 30 + 115 + i * 230
        g, _ = figure(c, cx, top + 20, hh, v)
        body.append(g)
        body.append(f'<text x="{cx}" y="{top + 20 + fig_h + 34:.0f}" font-size="16" fill="{INK}" text-anchor="middle" font-weight="700">{label}</text>')
    # 정보 패널
    px, py, pw = 980, top, 390
    body.append(f'<rect x="{px - 16}" y="{py}" width="{pw + 20}" height="{fig_h + 50:.0f}" rx="10" fill="#fff" stroke="#E2E5EA"/>')
    y = py + 32
    rows = [("키·체형", f'{c.get("height", "")} / {c.get("build", "")} / {ratio:g}등신'),
            ("얼굴", c.get("face", "")),
            ("머리", f'{c.get("hair", "")} {c.get("hair_color", "")}'),
            ("소품", ", ".join(c.get("accessories", [])) or "—"),
            ("연기", c.get("acting", ""))]
    for k, v in rows:
        if not v:
            continue
        body.append(f'<text x="{px}" y="{y}" font-size="13" fill="#7A8290" font-weight="700">{esc(k)}</text>')
        t, h = tspan_block(px + 70, y, v, pw - 80, 15, max_lines=5)
        body.append(t); y += max(h, 22) + 10
    outfits = c.get("outfits") or []
    if outfits:
        body.append(f'<text x="{px}" y="{y + 8}" font-size="13" fill="#7A8290" font-weight="700">의상</text>')
        y += 22
        for o in outfits[:5]:
            col = o.get("color", "#ccc")
            body.append(f'<rect x="{px}" y="{y}" width="34" height="22" rx="4" fill="{col}" stroke="{INK}" stroke-width="1"/>'
                        f'<text x="{px + 44}" y="{y + 16}" font-size="14" fill="{INK}">{esc(o.get("label", ""))} <tspan fill="#9AA1AC" font-size="12">{esc(col)}</tspan></text>')
            y += 30
    # 표정
    ey0 = top + fig_h + 80
    body.append(f'<text x="36" y="{ey0:.0f}" font-size="20" font-weight="700" fill="{INK}">표정</text>')
    exprs = (c.get("expressions") or ["무표정", "웃음", "당황", "분노", "식은땀", "공허"])[:6]
    cell = (W - 72) / 6
    for i, e in enumerate(exprs):
        x0 = 36 + i * cell
        body.append(f'<rect x="{x0 + 6:.1f}" y="{ey0 + 16:.0f}" width="{cell - 12:.1f}" height="230" rx="10" fill="#fff" stroke="#E2E5EA"/>')
        body.append(f'<svg x="{x0 + 6:.1f}" y="{ey0 + 16:.0f}" width="{cell - 12:.1f}" height="190" overflow="hidden">{head_bust(c, (cell - 12) / 2, 82, 86, expr_params(e))}</svg>')
        t, _ = tspan_block(x0 + cell / 2, ey0 + 226, e, cell - 30, 15, weight="700", anchor="middle", max_lines=2)
        body.append(t)
    H = int(ey0 + 270)
    return svg_doc(W, H, "".join(body))

def variant_sheet(c):
    vs = c.get("variants") or []
    if not vs:
        return None
    hh = 40
    ratio = float(c.get("head_ratio", 7) or 7)
    colw = 320
    W = 60 + len(vs) * colw
    fig_h = hh * ratio
    H = int(140 + fig_h + 130)
    body = [f'<rect width="{W}" height="86" fill="{INK}"/>',
            f'<text x="30" y="52" font-size="28" font-weight="700" fill="#fff">{esc(c.get("name", ""))} — 시안 비교</text>',
            f'<text x="30" y="76" font-size="13" fill="#C9CED6">G7 고르기용 러프. 섞기도 가능("A 체형 + B 머리")</text>']
    for i, v in enumerate(vs):
        cv = dict(c); cv.update({k: val for k, val in v.items() if k != "label"})
        x0 = 30 + i * colw
        body.append(f'<rect x="{x0}" y="104" width="{colw - 20}" height="{H - 124}" rx="12" fill="#fff" stroke="#E2E5EA"/>')
        body.append(f'<text x="{x0 + 18}" y="136" font-size="20" font-weight="700" fill="{INK}">{esc(v.get("label", chr(65 + i)))}</text>')
        g1, _ = figure(cv, x0 + 95, 156, hh, "front", expr=expr_params((cv.get("expressions") or ["무표정"])[0]))
        g2, _ = figure(cv, x0 + 215, 156, hh, "tq")
        body += [g1, g2]
        diff = [f"{k}: {val}" for k, val in v.items() if k not in ("label",) and not isinstance(val, (list, dict))]
        t, _ = tspan_block(x0 + 18, 156 + fig_h + 40, " / ".join(diff), colw - 56, 14, fill="#4A5160", max_lines=6)
        body.append(t)
    return svg_doc(W, H, "".join(body))

def cmd_sketch(a):
    root = a.dir
    chars = load_json(os.path.join(root, "design/characters.json"), [])
    if not chars:
        sys.exit("design/characters.json이 비어 있습니다.")
    outdir = os.path.join(root, "design/sheets"); os.makedirs(outdir, exist_ok=True)
    made = []
    for c in chars:
        cid = c.get("id") or re.sub(r"\W+", "_", c.get("name", "char"))
        if a.variants:
            s = variant_sheet(c)
            if s:
                p = os.path.join(outdir, f"{cid}_variants.svg"); write(p, s); made.append(p)
        else:
            p = os.path.join(outdir, f"{cid}.svg"); write(p, char_sheet(c)); made.append(p)
    print("\n".join(made) if made else "만든 시트 없음 (--variants는 variants가 있는 인물만)")

# ───────────────────────── 소품 ─────────────────────────

def placeholder_prop(p):
    cols = p.get("colors") or ["#C9CED6"]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300"><rect x="70" y="70" width="160" height="160" rx="18" fill="{cols[0]}" stroke="{INK}" stroke-width="3"/>'
            f'<text x="150" y="160" font-size="20" text-anchor="middle" fill="{INK}" font-family="sans-serif">그림 없음</text></svg>')

def cmd_props(a):
    root = a.dir
    props = load_json(os.path.join(root, "design/props.json"), [])
    if not props:
        sys.exit("design/props.json이 비어 있습니다.")
    cols = 3
    cw, ch = 440, 500
    W = 40 + cols * cw
    rows = math.ceil(len(props) / cols)
    H = 110 + rows * ch + 20
    body = [f'<rect width="{W}" height="86" fill="{INK}"/>',
            f'<text x="30" y="54" font-size="30" font-weight="700" fill="#fff">소품 설정</text>',
            f'<text x="30" y="76" font-size="13" fill="#C9CED6">단순 선화 + 고정값. 이미지 생성·작화 때 이 카드의 재질·크기·색을 지킨다.</text>']
    missing = []
    for i, p in enumerate(props):
        x0 = 20 + (i % cols) * cw
        y0 = 106 + (i // cols) * ch
        body.append(f'<rect x="{x0 + 10}" y="{y0}" width="{cw - 20}" height="{ch - 20}" rx="12" fill="#fff" stroke="#E2E5EA"/>')
        svgp = os.path.join(root, "design/props", f'{p.get("id", "")}.svg')
        if os.path.exists(svgp):
            raw = open(svgp, encoding="utf-8").read()
        else:
            raw = placeholder_prop(p); missing.append(p.get("id", "?"))
        b64 = base64.b64encode(raw.encode("utf-8")).decode()
        body.append(f'<rect x="{x0 + 30}" y="{y0 + 20}" width="{cw - 60}" height="250" rx="8" fill="#F4F2EC"/>')
        body.append(f'<image x="{x0 + 30}" y="{y0 + 20}" width="{cw - 60}" height="250" href="data:image/svg+xml;base64,{b64}" preserveAspectRatio="xMidYMid meet"/>')
        y = y0 + 304
        body.append(f'<text x="{x0 + 30}" y="{y}" font-size="21" font-weight="700" fill="{INK}">{esc(p.get("name", ""))}</text>')
        if p.get("era"):
            body.append(f'<text x="{x0 + cw - 30}" y="{y}" font-size="13" fill="#7A8290" text-anchor="end">{esc(p["era"])}</text>')
        y += 26
        cx = x0 + 30
        for col in (p.get("colors") or [])[:6]:
            body.append(f'<rect x="{cx}" y="{y - 13}" width="26" height="18" rx="3" fill="{col}" stroke="{INK}" stroke-width="0.8"/>'); cx += 32
        y += 18
        for k, label in (("material", "재질"), ("size", "크기"), ("role", "역할"), ("scenes", "등장"), ("ref", "고증")):
            v = p.get(k)
            if not v:
                continue
            if isinstance(v, list):
                v = ", ".join(v)
            if k == "ref":
                v = re.sub(r"^https?://(www\.)?", "", v)
                v = v if len(v) <= 34 else v[:33] + "…"
            body.append(f'<text x="{x0 + 30}" y="{y}" font-size="12" fill="#7A8290" font-weight="700">{label}</text>')
            t, h = tspan_block(x0 + 72, y, v, cw - 112, 13, fill="#3A404C", max_lines={"role": 3, "ref": 1}.get(k, 2))
            body.append(t); y += max(h, 18) + 4
    out = os.path.join(root, "design/props_sheet.svg")
    write(out, svg_doc(W, H, "".join(body)))
    print(out)
    if missing:
        print("그림 없는 소품(design/props/<id>.svg를 그려 넣을 것):", ", ".join(missing))

# ───────────────────────── 컬러 스크립트 ─────────────────────────

def cmd_colorscript(a):
    root = a.dir
    beats = load_json(os.path.join(root, "story/beats.json"), [])
    if not beats:
        sys.exit("story/beats.json이 비어 있습니다.")
    n = len(beats)
    bw = max(90, min(160, 1500 // n))
    W = 40 + n * bw
    H = 330
    body = [f'<text x="20" y="38" font-size="24" font-weight="700" fill="{INK}">컬러 스크립트</text>',
            f'<text x="20" y="60" font-size="13" fill="#7A8290">비트 순서대로 지배색. 감정이 바뀌는 지점에서만 색을 바꾼다.</text>']
    prev_ch = None
    for i, b in enumerate(beats):
        x = 20 + i * bw
        col = b.get("color", "#888")
        if b.get("chapter") != prev_ch:
            body.append(f'<line x1="{x}" y1="76" x2="{x}" y2="{H - 10}" stroke="{INK}" stroke-width="2"/>'
                        f'<text x="{x + 6}" y="92" font-size="13" font-weight="700" fill="{INK}">{esc(b.get("chapter", ""))}</text>')
            prev_ch = b.get("chapter")
        body.append(f'<rect x="{x + 3}" y="102" width="{bw - 6}" height="120" rx="6" fill="{col}"/>')
        fg = "#fff" if luminance(col) < 0.55 else INK
        body.append(f'<text x="{x + bw / 2:.1f}" y="170" font-size="12" fill="{fg}" text-anchor="middle">{esc(col)}</text>')
        t, _ = tspan_block(x + 6, 244, b.get("beat", ""), bw - 12, 12, max_lines=3)
        body.append(t)
        body.append(f'<text x="{x + 6}" y="{H - 18}" font-size="12" fill="#7A8290">{esc(b.get("mood", ""))}</text>')
    out = os.path.join(root, "design/colorscript.svg")
    write(out, svg_doc(W, H, "".join(body)))
    print(out)

# ───────────────────────── 보드 ─────────────────────────

def md_to_html(md):
    """표·제목·목록·코드·문단·굵게 정도만 다루는 간이 변환"""
    out, lines, i = [], md.split("\n"), 0
    def inline(s):
        s = esc(s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"(#[0-9A-Fa-f]{6})\b", r'<span class="chip" style="--c:\1"></span>\1', s)
        s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
        return s
    while i < len(lines):
        l = lines[i]
        if l.startswith("```"):
            j = i + 1; buf = []
            while j < len(lines) and not lines[j].startswith("```"):
                buf.append(lines[j]); j += 1
            out.append("<pre>" + esc("\n".join(buf)) + "</pre>"); i = j + 1; continue
        if l.strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i + 1]):
            head = [c.strip() for c in l.strip().strip("|").split("|")]
            rows = []; j = i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                rows.append([c.strip() for c in lines[j].strip().strip("|").split("|")]); j += 1
            t = ["<div class='tw'><table><thead><tr>" + "".join(f"<th>{inline(h)}</th>" for h in head) + "</tr></thead><tbody>"]
            for r in rows:
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            out.append("".join(t) + "</tbody></table></div>"); i = j; continue
        m = re.match(r"^(#{1,4})\s+(.*)", l)
        if m:
            lv = min(len(m.group(1)) + 1, 5)
            out.append(f"<h{lv}>{inline(m.group(2))}</h{lv}>"); i += 1; continue
        if re.match(r"^\s*[-*]\s+", l):
            buf = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                buf.append("<li>" + inline(re.sub(r"^\s*[-*]\s+", "", lines[i])) + "</li>"); i += 1
            out.append("<ul>" + "".join(buf) + "</ul>"); continue
        if l.strip():
            out.append(f"<p>{inline(l)}</p>")
        i += 1
    return "\n".join(out)

def read(root, rel):
    p = os.path.join(root, rel)
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""

def _norm(t):
    return re.sub(r"\s+", "", re.sub(r"^# .*$", "", t, count=1, flags=re.M))

TEMPLATE_NORMS = {_norm(v) for v in TEMPLATES.values()}

def is_template(text):
    """init 템플릿 그대로(제목만 다를 수 있음)이거나 사실상 빈 파일이면 True"""
    n = _norm(text)
    return n in TEMPLATE_NORMS or len(n) < 8

def svg_inline(root, rel):
    s = read(root, rel)
    if not s:
        return ""
    m = re.search(r'<svg[^>]*\swidth="(\d+(?:\.\d+)?)"', s)
    w = m.group(1) if m else "1400"
    s = re.sub(r'(<svg[^>]*?)\s(width|height)="\d+(?:\.\d+)?"', r"\1", s, count=1)
    s = re.sub(r'(<svg[^>]*?)\s(width|height)="\d+(?:\.\d+)?"', r"\1", s, count=1)
    return s.replace("<svg ", f'<svg style="max-width:{w}px" ', 1)

def cmd_board(a):
    root = a.dir
    name = os.path.basename(os.path.abspath(root))
    title = a.title or f"{name} 디자인 보드"
    secs = []
    def sec(sid, label, inner):
        if inner.strip():
            secs.append((sid, label, inner))
    dec = read(root, "decisions.md")
    if dec and not is_template(dec):
        sec("dec", "결정 로그", md_to_html(re.sub(r"^# .*\n", "", dec)))
    pitch = read(root, "story/pitch.md")
    if pitch and not is_template(pitch):
        sec("pitch", "기획", md_to_html(re.sub(r"^# .*\n", "", pitch)))
    so = read(root, "design/style_options.md")
    style = load_json(os.path.join(root, "design/style.json"), {})
    st_html = ""
    if style.get("name") or style.get("palette"):
        chips = "".join(f'<div class="sw"><i style="background:{esc(p.get("hex", p) if isinstance(p, dict) else p)}"></i><span>{esc(p.get("name", "") if isinstance(p, dict) else "")}<br>{esc(p.get("hex", p) if isinstance(p, dict) else p)}</span></div>' for p in style.get("palette", []))
        rows = "".join(f"<tr><th>{esc(k)}</th><td>{esc(v if not isinstance(v, dict) else ', '.join(f'{kk}: {vv}' for kk, vv in v.items()))}</td></tr>"
                       for k, v in style.items() if k not in ("palette",) and v)
        st_html = f'<div class="card"><h3>확정 스타일</h3><div class="pal">{chips}</div><div class="tw"><table>{rows}</table></div></div>'
    if so and not is_template(so):
        st_html += f'<div class="card">{md_to_html(re.sub(r"^# .*\n", "", so))}</div>'
    sec("style", "그림체", st_html)
    sheets_dir = os.path.join(root, "design/sheets")
    figs = []
    if os.path.isdir(sheets_dir):
        files = sorted(os.listdir(sheets_dir))
        for fn in [f for f in files if f.endswith("_variants.svg")] + [f for f in files if f.endswith(".svg") and not f.endswith("_variants.svg")]:
            cap = fn[:-4].replace("_variants", " — 시안 비교")
            figs.append(f'<figure class="sheet">{svg_inline(root, "design/sheets/" + fn)}<figcaption>{esc(cap)}</figcaption></figure>')
    sec("chars", "캐릭터", "".join(figs))
    bible = read(root, "story/bible.md")
    if bible and not is_template(bible):
        sec("bible", "캐릭터 바이블", md_to_html(re.sub(r"^# .*\n", "", bible)))
    if os.path.exists(os.path.join(root, "design/props_sheet.svg")):
        sec("props", "소품", f'<figure class="sheet">{svg_inline(root, "design/props_sheet.svg")}</figure>')
    sets = read(root, "design/sets.md")
    if sets and not is_template(sets):
        sec("sets", "배경 설정", md_to_html(re.sub(r"^# .*\n", "", sets)))
    if os.path.exists(os.path.join(root, "design/colorscript.svg")):
        sec("color", "컬러 스크립트", f'<figure class="sheet wide">{svg_inline(root, "design/colorscript.svg")}</figure>')
    dirn = read(root, "story/direction.md")
    sfx = read(root, "story/sfx_list.md")
    dhtml = (md_to_html(re.sub(r"^# .*\n", "", dirn)) if dirn and not is_template(dirn) else "") + \
            (md_to_html(sfx) if sfx and not is_template(sfx) else "")
    sec("dir", "연출·효과음", dhtml)
    notes = read(root, "research/notes.md")
    if notes and not is_template(notes):
        sec("res", "고증", md_to_html(re.sub(r"^# .*\n", "", notes)))
    if not secs:
        sys.exit("보드에 넣을 내용이 없습니다(템플릿만 있음).")
    nav = "".join(f'<a href="#{sid}">{esc(label)}</a>' for sid, label, _ in secs)
    body = "".join(f'<section id="{sid}"><h2>{esc(label)}</h2>{inner}</section>' for sid, label, inner in secs)
    page = f"""<title>{esc(title)}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
:root{{--bg:#F6F4EF;--fg:#1C1F26;--mut:#6B7280;--card:#FFFFFF;--line:#E2E5EA;--acc:#C93A46;--sheet:#FBFAF7;color-scheme:light dark}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#14171C;--fg:#E8EAED;--mut:#9AA1AC;--card:#1D2128;--line:#2E333C;--acc:#F07884;--sheet:#FBFAF7}}}}
:root[data-theme="dark"]{{--bg:#14171C;--fg:#E8EAED;--mut:#9AA1AC;--card:#1D2128;--line:#2E333C;--acc:#F07884;--sheet:#FBFAF7}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.65 'Noto Sans KR','Apple SD Gothic Neo','Malgun Gothic',sans-serif}}
header{{padding:28px 16px 8px;max-width:1200px;margin:auto}}
header h1{{margin:0;font-size:26px}} header p{{margin:4px 0 0;color:var(--mut)}}
nav{{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding:8px 16px;display:flex;gap:6px;overflow-x:auto;max-width:100%}}
nav a{{flex:none;color:var(--fg);text-decoration:none;padding:5px 12px;border:1px solid var(--line);border-radius:999px;font-size:13px;background:var(--card)}}
main{{max-width:1200px;margin:auto;padding:0 16px 80px}}
section{{padding-top:24px}} h2{{font-size:20px;border-left:4px solid var(--acc);padding-left:10px}}
h3,h4,h5{{margin:18px 0 6px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin:12px 0}}
.tw{{overflow-x:auto}} table{{border-collapse:collapse;width:100%;font-size:14px;background:var(--card)}}
th,td{{border:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}} th{{background:color-mix(in srgb,var(--line) 45%,transparent)}}
figure.sheet{{margin:14px 0;background:var(--sheet);border:1px solid var(--line);border-radius:12px;padding:8px;overflow-x:auto}}
figure.sheet>svg{{width:100%;height:auto;display:block;margin:auto}}
figure.wide>svg{{min-width:900px}}
figcaption{{color:#6B7280;font-size:13px;padding:4px 6px}}
.pal{{display:flex;flex-wrap:wrap;gap:10px;margin:8px 0 12px}} .sw{{display:flex;gap:6px;align-items:center;font-size:12px}}
.sw i{{width:34px;height:34px;border-radius:8px;border:1px solid var(--line);display:block}}
.chip{{display:inline-block;width:12px;height:12px;border-radius:3px;background:var(--c);border:1px solid var(--line);margin-right:3px;vertical-align:-1px}}
pre{{white-space:pre-wrap;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px;font-size:13px}}
code{{font-size:13px}} a{{color:var(--acc)}}
</style>
<header><h1>{esc(title)}</h1><p>갱신 {TODAY} · 결정 로그가 기준. 잠정 항목은 바뀔 수 있음.</p></header>
<nav>{nav}</nav>
<main>{body}</main>
"""
    out = os.path.join(root, "design/board.html")
    write(out, page)
    print(out)

# ───────────────────────── docx / pack ─────────────────────────

DOCX_TARGETS = ["story/pitch.md", "story/bible.md", "story/synopsis.md", "story/beats.md", "story/novel.md",
                "story/script.md", "story/direction.md", "story/sfx_list.md", "design/style_options.md",
                "design/sets.md", "anim/storyboard_anim.md", "anim/sound_cues.md", "decisions.md", "research/notes.md"]
LANDSCAPE = {"anim/storyboard_anim.md", "anim/sound_cues.md", "story/sfx_list.md", "decisions.md", "research/notes.md", "story/beats.md"}

def cmd_docx(a):
    root = a.dir
    js = None
    for cand in (os.path.join(root, "tools/md2docx.js"), os.path.join(HERE, "md2docx.js"), os.path.join(HERE, "..", "assets", "md2docx.js")):
        if os.path.exists(cand):
            js = cand; break
    if not js:
        sys.exit("md2docx.js를 찾지 못했습니다.")
    outdir = os.path.join(root, "docx"); os.makedirs(outdir, exist_ok=True)
    env = dict(os.environ)
    try:
        g = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
        if g:
            env["NODE_PATH"] = g + os.pathsep + env.get("NODE_PATH", "")
    except FileNotFoundError:
        pass
    made, skipped = [], []
    for rel in DOCX_TARGETS:
        p = os.path.join(root, rel)
        if not os.path.exists(p) or is_template(open(p, encoding="utf-8").read()):
            skipped.append(rel); continue
        out = os.path.join(outdir, rel.replace("/", "_").replace(".md", ".docx"))
        args = ["node", js, p, out] + (["landscape"] if rel in LANDSCAPE else [])
        r = subprocess.run(args, capture_output=True, text=True, env=env)
        if r.returncode != 0:
            print(f"실패 {rel}: {r.stderr.strip()[:300]}")
        else:
            made.append(out)
    print("\n".join(made) or "만든 문서 없음")
    if skipped:
        print("건너뜀(없거나 템플릿 상태):", ", ".join(skipped))

def cmd_pack(a):
    root = os.path.abspath(a.dir)
    name = os.path.basename(root)
    out = a.out or os.path.join(os.path.dirname(root), f"{name}.zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for dp, dn, fns in os.walk(root):
            dn[:] = [d for d in dn if d not in ("node_modules", "__pycache__", ".git")]
            for fn in fns:
                fp = os.path.join(dp, fn)
                if os.path.abspath(fp) == os.path.abspath(out):
                    continue
                z.write(fp, os.path.join(name, os.path.relpath(fp, root)))
    print(out)

# ───────────────────────── main ─────────────────────────

def main():
    ap = argparse.ArgumentParser(description="webtoon-story-studio 도구")
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("init"); p.add_argument("name"); p.add_argument("--force", action="store_true")
    for n in ("sketch", "props", "colorscript", "board", "docx", "pack"):
        q = sp.add_parser(n); q.add_argument("--dir", default=".")
        if n == "sketch":
            q.add_argument("--variants", action="store_true")
        if n == "board":
            q.add_argument("--title")
        if n == "pack":
            q.add_argument("--out")
    a = ap.parse_args()
    {"init": cmd_init, "sketch": cmd_sketch, "props": cmd_props, "colorscript": cmd_colorscript,
     "board": cmd_board, "docx": cmd_docx, "pack": cmd_pack}[a.cmd](a)

if __name__ == "__main__":
    main()
