"""콘티 컷 데이터(shot·screen·lines)로 레이아웃 썸네일 SVG를 만든다. 표준 라이브러리만 사용.

샷 크기에 따라 인물 크기를, 위치(좌·중·우·전경·후경)에 따라 배치를 정하고,
실루엣·분할·말풍선·내레이션·효과음 자리를 표시한다. 구도 참고용 러프다.
"""
import re
from html import escape

W = 400
NAMES = {
    "무진": dict(hair="side", glasses=True, hairc="#1C1F26"),
    "서희": dict(hair="pony", cap=True, hairc="#3B2A22"),
    "정만": dict(hair="buzz", hairc="#1C1F26"),
    "인턴": dict(hair="spiky", hairc="#2B2B2B"),
    "치프": dict(hair="side", hairc="#9AA0A8"),
    "방주먹": dict(hair="slick", shades=True, hairc="#1C1F26"),
    "상철": dict(hair="bald", hairc="#3A3A3A"),
    "신입 간호사": dict(hair="buzz", cap=True, hairc="#4A3426"),
}
POSX = {"좌": 0.25, "중": 0.5, "우": 0.75}
SHOT_RE = re.compile(r"^\s*(ECU|CU|BS|MS|FS|LS|ELS|INS|TXT)\b")


def parse_shot(shot):
    parts = [p.strip() for p in shot.split("·")]
    code = (SHOT_RE.match(shot) or [None, ""])[1] if SHOT_RE.match(shot) else ""
    angle = parts[1] if len(parts) > 1 else ""
    people_txt = "·".join(parts[2:]) if len(parts) > 2 else ""
    people = []
    if people_txt and "인물 없음" not in people_txt:
        for m in re.finditer(r"([^,()]+?)\s*\(([^)]*)\)|([^,()]+)", people_txt):
            name = (m.group(1) or m.group(3) or "").strip(" ,")
            opts = m.group(2) or ""
            if not name:
                continue
            pos = next((k for k in POSX if k in opts), "중")
            people.append(dict(name=name, pos=pos, fg="전경" in opts, bg="후경" in opts, sil="실루엣" in opts))
    return code, angle, people


def bg_color(c):
    t = c.get("screen", "") + c.get("scene", "")
    if "초록" in t and ("유도등" in t or "녹색" in t):
        return "#16251D", True
    if any(k in t for k in ["밤", "새벽", "어둠", "어두운", "역광", "남색", "검은 바탕", "#0F1626"]):
        return "#1E2638", True
    return "#ECEEF1", False


def head(cx, cy, r, spec, sil, dark):
    ink = "#E8EAEE" if (sil and dark) else "#1C1F26"
    skin = "#0D1018" if sil else "#F6D5BB"
    hc = "#0D1018" if sil else spec.get("hairc", "#1C1F26")
    sw = max(1.5, r / 14)
    st = f'stroke="{ink if sil else "#1C1F26"}" stroke-width="{sw:.1f}"'
    g = ""
    if spec.get("hair") == "pony":
        g += f'<ellipse cx="{cx + r * .95:.1f}" cy="{cy - r * .2:.1f}" rx="{r * .32:.1f}" ry="{r * .6:.1f}" fill="{hc}" {st}/>'
    g += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{skin}" {st}/>'
    hair = spec.get("hair", "side")
    if hair == "bald":
        g += f'<path d="M{cx - r:.1f} {cy:.1f} q{-r * .05:.1f} {-r * .5:.1f} {r * .2:.1f} {-r * .7:.1f} M{cx + r:.1f} {cy:.1f} q{r * .05:.1f} {-r * .5:.1f} {-r * .2:.1f} {-r * .7:.1f}" fill="none" stroke="{hc}" stroke-width="{r * .18:.1f}"/>'
    elif hair == "spiky":
        pts = " ".join(f"{cx + r * x:.1f},{cy + r * y:.1f}" for x, y in [(-1, -.1), (-1.2, -.6), (-.7, -.8), (-.6, -1.3), (-.1, -1), (.3, -1.35), (.5, -.95), (1.15, -1), (.95, -.5), (1, -.1), (.6, -.6), (-.6, -.6)])
        g += f'<polygon points="{pts}" fill="{hc}" {st}/>'
    else:
        top = {"buzz": .55, "slick": .9, "side": .85}.get(hair, .85)
        g += f'<path d="M{cx - r:.1f} {cy - r * .05:.1f} A{r:.1f} {r:.1f} 0 0 1 {cx + r:.1f} {cy - r * .05:.1f} Q{cx + r * .2:.1f} {cy - r * top:.1f} {cx - r:.1f} {cy - r * .05:.1f}Z" fill="{hc}" {st}/>'
    if spec.get("cap"):
        g += f'<path d="M{cx - r * .6:.1f} {cy - r * .8:.1f} L{cx - r * .45:.1f} {cy - r * 1.35:.1f} L{cx + r * .45:.1f} {cy - r * 1.35:.1f} L{cx + r * .6:.1f} {cy - r * .8:.1f}Z" fill="#fff" {st}/>'
    if not sil:
        er = max(1.2, r * .09)
        g += f'<circle cx="{cx - r * .35:.1f}" cy="{cy + r * .05:.1f}" r="{er:.1f}" fill="#1C1F26"/><circle cx="{cx + r * .35:.1f}" cy="{cy + r * .05:.1f}" r="{er:.1f}" fill="#1C1F26"/>'
        if spec.get("glasses"):
            g += f'<circle cx="{cx - r * .35:.1f}" cy="{cy + r * .05:.1f}" r="{r * .28:.1f}" fill="none" {st}/><circle cx="{cx + r * .35:.1f}" cy="{cy + r * .05:.1f}" r="{r * .28:.1f}" fill="none" {st}/>'
        if spec.get("shades"):
            g += f'<rect x="{cx - r * .65:.1f}" y="{cy - r * .12:.1f}" width="{r * 1.3:.1f}" height="{r * .32:.1f}" rx="{r * .1:.1f}" fill="#1C1F26"/>'
        g += f'<path d="M{cx - r * .2:.1f} {cy + r * .5:.1f} h{r * .4:.1f}" {st}/>'
    elif spec.get("glasses"):
        g += f'<circle cx="{cx - r * .35:.1f}" cy="{cy:.1f}" r="{r * .12:.1f}" fill="#E8EAEE"/><circle cx="{cx + r * .35:.1f}" cy="{cy:.1f}" r="{r * .12:.1f}" fill="#E8EAEE"/>'
    return g


def figure(code, p, H, n_same, k, dark, n_total=1):
    spec = NAMES.get(p["name"], dict(hair="side", hairc="#555"))
    x = W * POSX[p["pos"]] + (k - (n_same - 1) / 2) * 46
    scale = 1.3 if p["fg"] else 0.72 if p["bg"] else 1.0
    sil = p["sil"]
    body = "#0D1018" if sil else "#B9C3CF"
    edge = "#E8EAEE" if (sil and dark) else "#1C1F26"
    if code == "ECU" and n_total > 1:
        code = "CU"
    if code == "ECU":
        r = H * .55 * scale
        return head(x, H * .55, r, spec, sil, dark)
    if code == "CU":
        r = min(H * .3, 110) * scale
        cy = H * .55
        return f'<path d="M{x - r * 1.3:.1f} {H:.1f} Q{x:.1f} {cy + r * .6:.1f} {x + r * 1.3:.1f} {H:.1f}Z" fill="{body}" stroke="{edge}" stroke-width="2"/>' + head(x, cy, r, spec, sil, dark)
    if code in ("BS", "MS"):
        r = (min(H * .17, 62) if code == "BS" else min(H * .12, 44)) * scale
        cy = H - r * (3.2 if code == "BS" else 4.4)
        return f'<path d="M{x - r * 2.2:.1f} {H:.1f} Q{x - r * 2:.1f} {cy + r * 1.3:.1f} {x:.1f} {cy + r * 1.1:.1f} Q{x + r * 2:.1f} {cy + r * 1.3:.1f} {x + r * 2.2:.1f} {H:.1f}Z" fill="{body}" stroke="{edge}" stroke-width="2"/>' + head(x, cy, r, spec, sil, dark)
    # FS / LS / ELS: whole body
    frac = {"FS": .62, "LS": .32, "ELS": .14}.get(code, .45) * scale
    hgt = H * frac
    foot = H * (.92 if code == "FS" else .82 if code == "LS" else .78)
    r = hgt * .12
    cy = foot - hgt + r
    return (f'<path d="M{x - r * 1.4:.1f} {foot:.1f} L{x - r * 1.6:.1f} {cy + r * 1.3:.1f} Q{x:.1f} {cy + r * .9:.1f} {x + r * 1.6:.1f} {cy + r * 1.3:.1f} L{x + r * 1.4:.1f} {foot:.1f}Z" fill="{body}" stroke="{edge}" stroke-width="1.6"/>'
            + head(x, cy, r, spec, sil, dark))


def wrap(t, n):
    out, line = [], ""
    for ch in t:
        line += ch
        if len(line) >= n:
            out.append(line); line = ""
    if line:
        out.append(line)
    return out


def svg_for(c):
    H = max(160, round(c.get("height", 800) / 2))
    code, angle, people = parse_shot(c.get("shot", ""))
    bg, dark = bg_color(c)
    fg = "#E8EAEE" if dark else "#1C1F26"
    g = [f'<rect width="{W}" height="{H}" fill="{bg}"/>']
    t = c.get("screen", "")
    if code in ("LS", "ELS", "FS"):
        g.append(f'<path d="M0 {H * .82:.0f} H{W}" stroke="{fg}" stroke-opacity=".35" stroke-width="2"/>')
    if code == "INS" or (code == "" and not people):
        g.append(f'<rect x="60" y="{H * .25:.0f}" width="280" height="{H * .5:.0f}" rx="10" fill="none" stroke="{fg}" stroke-dasharray="8 6" stroke-width="2"/>')
        g.append(f'<text x="200" y="{H * .25 + 24:.0f}" font-size="14" fill="{fg}" fill-opacity=".7" text-anchor="middle" font-family="sans-serif">INSERT</text>')
        for i, ln in enumerate(wrap(c.get("summary", ""), 18)[:3]):
            g.append(f'<text x="200" y="{H * .5 + i * 20:.0f}" font-size="15" fill="{fg}" text-anchor="middle" font-family="sans-serif">{escape(ln)}</text>')
    if code == "TXT":
        nar = [l["text"] for l in c.get("lines", []) if l["type"] in ("narration", "caption")]
        txt = nar[0] if nar else c.get("summary", "")
        for i, ln in enumerate(wrap(txt, 16)[:5]):
            g.append(f'<text x="200" y="{H * .35 + i * 28:.0f}" font-size="20" fill="{fg}" text-anchor="middle" font-family="sans-serif" font-weight="700">{escape(ln)}</text>')
    elif code != "INS":
        from collections import Counter
        cnt = Counter(p["pos"] for p in people); seen = Counter()
        for p in sorted(people, key=lambda p: (not p["bg"], p["fg"])):
            g.append(figure(code or "MS", p, H, cnt[p["pos"]], seen[p["pos"]], dark, len(people))); seen[p["pos"]] += 1
    if "3분할" in t:
        g += [f'<path d="M{x} 0 V{H}" stroke="#fff" stroke-width="6"/>' for x in (133, 267)] if "세로" in t else [f'<path d="M0 {H * y:.0f} H{W}" stroke="#fff" stroke-width="6"/>' for y in (1 / 3, 2 / 3)]
    elif "2분할" in t:
        g.append(f'<path d="M200 0 V{H}" stroke="#fff" stroke-width="6"/>' if "세로" in t else f'<path d="M0 {H / 2:.0f} H{W}" stroke="#fff" stroke-width="6"/>')
    if "POV" in angle and ("철문" in t or "문틈" in t):
        g.append(f'<rect x="0" y="0" width="70" height="{H}" fill="#000"/><rect x="330" y="0" width="70" height="{H}" fill="#000"/>')
    if "집중선" in t:
        import math
        for i in range(36):
            a = i / 36 * 2 * math.pi
            g.append(f'<line x1="{200 + math.cos(a) * 120:.0f}" y1="{H / 2 + math.sin(a) * 120:.0f}" x2="{200 + math.cos(a) * 420:.0f}" y2="{H / 2 + math.sin(a) * 420:.0f}" stroke="{fg}" stroke-opacity=".5" stroke-width="2"/>')
    talk = [l for l in c.get("lines", []) if l["type"] in ("dialogue", "thought", "whisper")]
    for i, l in enumerate(talk[:2]):
        x = 16 + (i % 2) * 190; y = 14 + i * 46
        dash = ' stroke-dasharray="5 4"' if l["type"] in ("thought", "whisper") else ""
        g.append(f'<rect x="{x}" y="{y}" width="178" height="38" rx="18" fill="#fff" stroke="#1C1F26" stroke-width="2"{dash}/>')
        g.append(f'<text x="{x + 89}" y="{y + 24}" font-size="13" fill="#1C1F26" text-anchor="middle" font-family="sans-serif">{escape(l["speaker"][:6])}</text>')
    if any(l["type"] == "narration" for l in c.get("lines", [])) and code != "TXT":
        g.append(f'<rect x="14" y="{H - 44}" width="250" height="32" fill="{"#0F1626" if dark else "#FFF4CF"}" stroke="{fg}" stroke-width="1.5"/>')
    sfx = [l["text"] for l in c.get("lines", []) if l["type"] == "sfx"]
    if sfx:
        s = sfx[0].split("(")[0].strip()[:8]
        g.append(f'<text x="{W - 20}" y="{min(H - 60, 90)}" font-size="34" fill="#C93A46" stroke="#fff" stroke-width="4" paint-order="stroke" text-anchor="end" font-family="sans-serif" font-weight="900">{escape(s)}</text>')
    label = f'{c["id"]} · {code or "?"} · {angle}'
    g.append(f'<rect x="0" y="0" width="{min(W, 14 + len(label) * 8)}" height="22" fill="#000" fill-opacity=".55"/><text x="6" y="16" font-size="13" fill="#fff" font-family="sans-serif">{escape(label)}</text>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{escape(c["id"] + " " + c.get("summary", ""))}">{"".join(g)}</svg>'
