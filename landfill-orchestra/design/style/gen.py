"""G6 그림체 맛보기: 같은 장면(1화 S#11 '첫 소리')을 세 화풍으로 그린 도식 SVG.

작화가 아니라 선·채색·명암·효과음 처리의 차이를 보이는 러프다.
python design/style/gen.py  → design/style/style_a.svg, style_b.svg, style_c.svg, style_final.svg(확정)
"""
import os
import random

W, H = 420, 600
HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = ("@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&amp;family=Gowun+Batang"
         "&amp;family=Nanum+Pen+Script&amp;family=Gaegu:wght@700&amp;family=Black+Han+Sans&amp;family=Jua"
         "&amp;family=Nanum+Myeongjo:wght@700&amp;family=East+Sea+Dokdo&amp;display=swap');")

# ── 공통 도형 (420x600 좌표) ─────────────────────────────
HILL = ("M0 600 L0 470 L40 466 L52 452 L96 448 L108 434 L140 430 L150 416 L300 416 L310 430 L342 434 "
        "L354 448 L398 452 L410 466 L420 468 L420 600 Z")  # 꼭대기가 평평하고 층진 쓰레기 산(고증)
HILL_FAR = "M0 380 L0 350 L30 346 L44 330 L70 326 L84 306 L190 306 L204 326 L230 330 L244 346 L280 350 L420 352 L420 380 Z"
# 은주: 왼쪽을 보고 서서 동그리를 왼쪽 어깨에 얹고 켠다
JACKET = ("M196 268 C186 270 176 278 172 292 L166 352 C176 358 196 360 214 358 "
          "C230 358 244 354 250 348 L244 294 C240 280 230 270 220 267 Z")
PANTS = "M176 352 L180 404 L194 404 L200 360 L208 360 L212 404 L226 404 L232 352 Z"
BOOTS = "M176 400 L196 400 L198 418 L172 418 Z M208 400 L228 400 L232 418 L206 418 Z"
HEAD = "M210 222 C224 222 232 234 232 248 C232 262 222 270 210 270 C198 270 188 262 188 248 C188 234 196 222 210 222 Z"
HAIR = ("M188 248 C186 230 198 218 212 218 C228 218 236 232 234 246 C230 238 222 234 214 236 "
        "C204 238 196 244 192 254 Z M228 252 C238 262 240 276 236 292 C232 296 228 294 228 288 C230 276 230 266 226 258 Z")
CAN = "M156 266 L192 252 L204 284 L168 298 Z"           # 분유 깡통(비스듬)
CAN_TOP = "M156 266 L192 252"
NECK = "M160 272 L104 252 L102 258 L158 280 Z"            # 나무 숟가락 목
ARM_L = "M176 300 C150 300 124 286 108 262"               # 왼팔(목 쪽으로)
ARM_R = "M240 300 C252 312 256 326 250 336"               # 오른팔(활)
BOW = (226, 236, 262, 330)                                # 활 막대 (x1,y1,x2,y2)


def svg(body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
            f'<title>{title}</title><style>{FONTS}</style>' + "".join(body) + "</svg>")


def junk(seed, n, colors, stroke=None, sw=0, y0=420, y1=600, op=1.0):
    """쓰레기 더미의 깡통·판자·비닐 조각."""
    random.seed(seed)
    out = []
    for _ in range(n):
        x = random.uniform(-10, 420)
        y = random.uniform(y0, y1)
        w = random.uniform(8, 28)
        h = random.uniform(4, 14)
        r = random.uniform(-40, 40)
        c = random.choice(colors)
        st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        out.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="2" fill="{c}"{st} '
                   f'opacity="{op}" transform="rotate({r:.0f} {x:.0f} {y:.0f})"/>')
    return out


def figure(skin, hair, jacket, pants, boots, can, neck, ink, sw, hand=None):
    hand = hand or skin
    s = f' stroke="{ink}" stroke-width="{sw}" stroke-linejoin="round"' if sw else ""
    x1, y1, x2, y2 = BOW
    return [
        f'<path d="{PANTS}" fill="{pants}"{s}/>',
        f'<path d="{BOOTS}" fill="{boots}"{s}/>',
        f'<path d="{JACKET}" fill="{jacket}"{s}/>',
        f'<path d="{ARM_L}" fill="none" stroke="{jacket}" stroke-width="16" stroke-linecap="round"/>',
        f'<path d="{ARM_L}" fill="none" stroke="{ink}" stroke-width="{max(sw, .8)}" stroke-dasharray="0" opacity="{1 if sw else .35}"/>' if sw else "",
        f'<path d="{NECK}" fill="{neck}"{s}/>',
        f'<path d="{CAN}" fill="{can}"{s}/>',
        f'<path d="M162 270 L196 257 M164 276 L198 263 M166 282 L200 269" stroke="{ink}" stroke-width=".8" opacity=".5"/>',
        f'<circle cx="106" cy="257" r="7" fill="{hand}"{s}/>',
        f'<path d="{HEAD}" fill="{skin}"{s}/>',
        f'<path d="{HAIR}" fill="{hair}"{s}/>',
        f'<path d="{ARM_R}" fill="none" stroke="{jacket}" stroke-width="15" stroke-linecap="round"/>',
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{ink}" stroke-width="2.4" stroke-linecap="round"/>',
        f'<circle cx="252" cy="334" r="7" fill="{hand}"{s}/>',
        f'<path d="M196 248 C198 246 201 246 203 248" stroke="{ink}" stroke-width="1.2" fill="none"/>',  # 감은 눈
    ]


# ── 1안: 금빛 먼지 수채 ───────────────────────────────────
def style_a():
    b = ['''<defs>
<linearGradient id="a_sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7C8FB0"/><stop offset=".45" stop-color="#E9B887"/><stop offset=".7" stop-color="#F6D08A"/><stop offset="1" stop-color="#F2B66B"/></linearGradient>
<radialGradient id="a_sun" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFF4D2"/><stop offset=".4" stop-color="#FFE29A" stop-opacity=".9"/><stop offset="1" stop-color="#F6C46E" stop-opacity="0"/></radialGradient>
<linearGradient id="a_hill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C99A62"/><stop offset="1" stop-color="#6E5640"/></linearGradient>
<filter id="a_wash" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="3" seed="7"/><feDisplacementMap in="SourceGraphic" scale="7"/><feGaussianBlur stdDeviation=".6"/></filter>
<filter id="a_paper"><feTurbulence type="fractalNoise" baseFrequency=".75" numOctaves="2" seed="3"/><feColorMatrix values="0 0 0 0 .45  0 0 0 0 .35  0 0 0 0 .25  0 0 0 .10 0"/></filter>
<filter id="a_blur"><feGaussianBlur stdDeviation="3"/></filter>
</defs>''',
         f'<rect width="{W}" height="{H}" fill="url(#a_sky)"/>',
         '<circle cx="320" cy="300" r="120" fill="url(#a_sun)"/>',
         '<rect x="0" y="318" width="420" height="22" fill="#F4CF8E" opacity=".8"/>',
         f'<path d="{HILL_FAR}" fill="#B48A6A" opacity=".55" filter="url(#a_wash)"/>',
         f'<path d="{HILL}" fill="url(#a_hill)" filter="url(#a_wash)"/>']
    b += junk(11, 70, ["#A77C55", "#8F6E52", "#D9B27A", "#7D8A8C", "#B9A27F"], op=.75)
    # 금빛 림라이트(역광)
    b.append('<g filter="url(#a_wash)">')
    b += figure("#E7B790", "#3A2A20", "#3C4A6E", "#5A5048", "#3A3633", "#C9C2B2", "#B88A5A", "#5A3E2C", 0)
    b.append('</g>')
    b.append(f'<path d="{JACKET}" fill="none" stroke="#FFE3A8" stroke-width="3" opacity=".7" filter="url(#a_blur)"/>')
    b.append(f'<path d="{HEAD}" fill="none" stroke="#FFE7B8" stroke-width="3" opacity=".8" filter="url(#a_blur)"/>')
    # 가는 갈색 연필 선
    b.append(f'<g fill="none" stroke="#5A3E2C" stroke-width=".9" opacity=".75"><path d="{JACKET}"/><path d="{HEAD}"/><path d="{CAN}"/><path d="{NECK}"/><path d="{PANTS}"/></g>')
    # 소리 = 부드러운 금빛 동심원
    for i, r in enumerate((30, 52, 76, 102)):
        b.append(f'<circle cx="180" cy="276" r="{r}" fill="none" stroke="#FFF1C9" stroke-width="{2.4 - i * .4:.1f}" opacity="{.75 - i * .15:.2f}"/>')
    b.append(f'<rect width="{W}" height="{H}" filter="url(#a_paper)"/>')
    b.append('<text x="276" y="232" font-family="\'Nanum Pen Script\',cursive" font-size="44" fill="#7A4A22" opacity=".9" transform="rotate(-6 276 232)">동―</text>')
    b.append('<g><rect x="22" y="22" width="196" height="52" rx="4" fill="#FFF8EA" fill-opacity=".82"/>'
             '<text x="36" y="54" font-family="\'Gowun Batang\',serif" font-size="15" fill="#4A3524">동그란 소리가 났어요.</text></g>')
    return svg(b, "1안 금빛 먼지 수채")


# ── 2안: 깡통 팝 셀 ─────────────────────────────────────
def style_b():
    ink = "#1B1A1F"
    b = [f'<rect width="{W}" height="{H}" fill="#FFB547"/>',
         '<rect x="0" y="0" width="420" height="190" fill="#FF8A4C"/>',
         '<rect x="0" y="190" width="420" height="80" fill="#FFC861"/>',
         f'<circle cx="320" cy="300" r="64" fill="#FFF1A8" stroke="{ink}" stroke-width="4"/>',
         f'<rect x="0" y="318" width="420" height="22" fill="#5EC6C9" stroke="{ink}" stroke-width="4"/>',
         f'<path d="{HILL_FAR}" fill="#C97A52" stroke="{ink}" stroke-width="4" stroke-linejoin="round"/>',
         f'<path d="{HILL}" fill="#9C6B4E" stroke="{ink}" stroke-width="5" stroke-linejoin="round"/>',
         '<path d="M0 470 C80 452 140 444 210 448 C300 452 360 470 420 476 L420 600 L0 600 Z" fill="#7E553F"/>']
    b += junk(11, 46, ["#E2574C", "#4FA3D9", "#F2D04B", "#B7C2C9", "#6BBF7A"], stroke=ink, sw=2.5)
    b += figure("#F6C49E", "#2A211C", "#2F55A4", "#4A4A58", "#26252B", "#E9E4D8", "#D9A35E", ink, 3.5, hand="#F6C49E")
    b.append(f'<path d="M176 300 L170 350 L206 354 L210 300 Z" fill="#203E7E" opacity=".9"/>')  # 셀 그림자 1단
    # 소리 = 그래픽 효과선 + 큰 효과음
    for a in range(-60, 61, 20):
        b.append(f'<line x1="150" y1="276" x2="{150 - 120:.0f}" y2="{276 + a * 2:.0f}" stroke="{ink}" stroke-width="3" stroke-linecap="round" opacity=".85"/>')
    b.append(f'<g font-family="\'Black Han Sans\',sans-serif" transform="rotate(-10 300 210)"><text x="250" y="220" font-size="64" fill="#FFF7E6" stroke="{ink}" stroke-width="10" paint-order="stroke">동―!</text></g>')
    b.append(f'<g font-family="\'Black Han Sans\',sans-serif" transform="rotate(8 60 120)"><text x="28" y="130" font-size="34" fill="#E2574C" stroke="{ink}" stroke-width="7" paint-order="stroke">끼익</text></g>')
    b.append(f'<path d="M24 470 h150 a16 16 0 0 1 16 16 v26 a16 16 0 0 1 -16 16 h-96 l-12 16 l-2 -16 h-40 a16 16 0 0 1 -16 -16 v-26 a16 16 0 0 1 16 -16 z" fill="#FFFDF6" stroke="{ink}" stroke-width="4"/>'
             f'<text x="38" y="506" font-family="\'Jua\',sans-serif" font-size="18" fill="{ink}">고양이 밟았냐!</text>')
    b.append(f'<rect x="4" y="4" width="{W - 8}" height="{H - 8}" fill="none" stroke="{ink}" stroke-width="8"/>')
    return svg(b, "2안 깡통 팝 셀")


# ── 3안: 잿빛 섬, 소리만 색 ─────────────────────────────
def style_c():
    b = ['''<defs>
<filter id="c_char"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" seed="5"/><feColorMatrix values="0 0 0 0 .1  0 0 0 0 .1  0 0 0 0 .1  0 0 0 .22 0"/></filter>
<filter id="c_rough" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="2"/><feDisplacementMap in="SourceGraphic" scale="3"/></filter>
<radialGradient id="c_bloom" cx="180" cy="276" r="210" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#F5C04A" stop-opacity=".95"/><stop offset=".35" stop-color="#E8944A" stop-opacity=".55"/><stop offset=".7" stop-color="#C46A4A" stop-opacity=".15"/><stop offset="1" stop-color="#C46A4A" stop-opacity="0"/></radialGradient>
<linearGradient id="c_sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5E5B57"/><stop offset="1" stop-color="#A8A39B"/></linearGradient>
</defs>''',
         f'<rect width="{W}" height="{H}" fill="url(#c_sky)"/>',
         '<circle cx="320" cy="300" r="40" fill="#D8D3CA"/>',
         '<rect x="0" y="318" width="420" height="22" fill="#8E8A84"/>',
         f'<path d="{HILL_FAR}" fill="#6E6A65" filter="url(#c_rough)"/>',
         f'<path d="{HILL}" fill="#3E3B38" filter="url(#c_rough)"/>']
    b += junk(11, 70, ["#55514D", "#6B6762", "#2E2C2A", "#7E7A74"], op=.9)
    b.append('<g filter="url(#c_rough)">')
    b += figure("#B9B3AA", "#1E1C1B", "#3A3836", "#2C2A28", "#1C1B1A", "#8E8983", "#6E6A65", "#141312", 1.8)
    b.append('</g>')
    # 소리가 나는 곳만 색이 번진다
    b.append(f'<rect width="{W}" height="{H}" fill="url(#c_bloom)" style="mix-blend-mode:overlay"/>')
    b.append(f'<rect width="{W}" height="{H}" fill="url(#c_bloom)" opacity=".55"/>')
    b.append('<path d="M156 266 L192 252 L204 284 L168 298 Z" fill="#E9B04A" stroke="#141312" stroke-width="1.8"/>')
    b.append(f'<rect width="{W}" height="{H}" filter="url(#c_char)"/>')
    b.append('<text x="240" y="208" font-family="\'East Sea Dokdo\',cursive" font-size="62" fill="#F5C04A" transform="rotate(-8 240 208)">동―</text>')
    b.append('<text x="30" y="56" font-family="\'Nanum Myeongjo\',serif" font-weight="700" font-size="15" fill="#E8E4DC">그날, 섬에 처음으로 색이 났다.</text>')
    return svg(b, "3안 잿빛 섬, 소리만 색")


# ── 확정: 정밀 셀 반실사 「소리의 색」 ──────────────────────
def style_final():
    ink = "#2B2420"
    b = ['''<defs>
<linearGradient id="f_sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7C8FB0"/><stop offset=".5" stop-color="#E9B887"/><stop offset="1" stop-color="#F6D08A"/></linearGradient>
<filter id="f_desat"><feColorMatrix type="saturate" values=".4"/></filter>
<filter id="f_soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2"/></filter>
</defs>''', '<g filter="url(#f_desat)">',
         f'<rect width="{W}" height="{H}" fill="url(#f_sky)"/>',
         '<circle cx="320" cy="300" r="46" fill="#FFF1C9"/>',
         '<rect x="0" y="318" width="420" height="22" fill="#F4CF8E"/>',
         f'<path d="{HILL_FAR}" fill="#B48A6A" stroke="{ink}" stroke-width="1"/>',
         f'<path d="{HILL}" fill="#C99A62" stroke="{ink}" stroke-width="2" stroke-linejoin="round"/>',
         '<path d="M0 500 C80 488 140 484 210 486 C300 490 360 500 420 504 L420 600 L0 600 Z" fill="#9C7650"/>',
         f'<g stroke="{ink}" stroke-width="1.4" fill="none"><path d="M352 352 L366 230 L380 352 M356 320 L376 320 M359 290 L373 290 M362 260 L370 260 M352 352 L373 290 M380 352 L359 290 M350 250 L382 250 M354 238 L378 238"/></g>']
    b += junk(11, 50, ["#A77C55", "#8F6E52", "#D9B27A", "#7D8A8C", "#B9A27F"], stroke=ink, sw=1)
    b += figure("#E2B48E", "#2A211C", "#2E3A5C", "#5A5048", "#3A3633", "#C9C2B2", "#B88A5A", ink, 2)
    b.append(f'<path d="M176 300 L170 350 L200 354 L204 300 Z" fill="#232C46"/>')        # 셀 그림자 1단(남색)
    b.append(f'<path d="M204 222 C200 236 200 256 206 270 L210 270 C198 262 194 244 204 222 Z" fill="#C9966D"/>')
    b.append('</g>')
    # 소리 색 규칙: 동그리 소리만 금빛
    for i, r in enumerate((28, 50, 74, 100, 128)):
        b.append(f'<circle cx="180" cy="276" r="{r}" fill="none" stroke="#F5C04A" stroke-width="{5 - i * .8:.1f}" opacity="{.9 - i * .15:.2f}" filter="url(#f_soft)"/>')
    b.append(f'<path d="{CAN}" fill="#F5D27A" stroke="{ink}" stroke-width="2"/>')
    b.append('<text x="262" y="226" font-family="\'Gaegu\',cursive" font-weight="700" font-size="50" fill="#F5C04A" stroke="#2B2420" stroke-width="1.2" transform="rotate(-6 262 226)">동―</text>')
    b.append('<g><rect x="22" y="22" width="206" height="50" rx="2" fill="#FFF8EA" fill-opacity=".85"/>'
             '<text x="36" y="53" font-family="\'Gowun Batang\',serif" font-size="15" fill="#2B2420">동그란 소리가 났어요.</text></g>')
    return svg(b, "확정 정밀 셀 반실사 「소리의 색」")


if __name__ == "__main__":
    for name, fn in (("style_a", style_a), ("style_b", style_b), ("style_c", style_c), ("style_final", style_final)):
        with open(os.path.join(HERE, f"{name}.svg"), "w", encoding="utf-8") as f:
            f.write(fn())
    print("wrote style_a/b/c/final.svg")
