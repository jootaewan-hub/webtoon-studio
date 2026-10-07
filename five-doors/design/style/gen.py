import random
W,H=420,600
# back-view woman at window, right hand raised on glass. coords in 420x600
BODY=("M196 156 C194 166 186 174 168 179 C152 183 145 194 145 208 "
      "C144 236 142 262 141 290 C140 302 148 308 154 300 C157 270 161 242 165 224 "
      "C170 246 178 260 184 272 C164 298 150 320 150 346 "
      "C152 380 156 410 160 432 L178 434 C181 470 182 520 184 572 L198 572 C199 520 202 470 206 442 "
      "L214 442 C218 470 221 520 222 572 L236 572 C238 520 239 470 242 434 L260 432 "
      "C264 410 268 380 270 346 C270 320 256 298 236 272 C242 258 248 242 252 226 "
      "C264 204 278 178 294 146 C298 138 302 128 304 120 C306 110 294 106 290 116 "
      "C284 130 268 152 256 170 C250 168 242 167 230 166 C222 164 216 160 214 156 Z")
DRESS=("M166 196 C172 230 178 258 184 272 C164 298 150 320 150 346 C152 380 156 410 160 432 "
       "L260 432 C264 410 268 380 270 346 C270 320 256 298 236 272 C242 256 248 236 252 214 "
       "C238 210 226 214 212 222 C200 214 182 208 166 196 Z")
HEAD="M205 92 C226 92 238 108 238 128 C238 146 228 160 212 162 L198 162 C182 160 172 146 172 128 C172 108 184 92 205 92 Z"
HAIR="M170 126 C168 100 186 86 205 86 C226 86 242 100 240 126 C240 140 238 152 236 162 C226 166 214 167 205 167 C194 167 182 166 174 162 C172 152 170 140 170 126 Z"
def lights(seed,n,colors,rmin,rmax,y0=40,y1=470):
    random.seed(seed); out=[]
    for _ in range(n):
        x=random.uniform(20,400); y=random.uniform(y0,y1); r=random.uniform(rmin,rmax)
        out.append((x,y,r,random.choice(colors)))
    return out
def window(stroke,op):
    return (f'<g stroke="{stroke}" stroke-width="6" opacity="{op}" fill="none">'
            f'<line x1="70" y1="0" x2="70" y2="600"/><line x1="350" y1="0" x2="350" y2="600"/>'
            f'<line x1="0" y1="500" x2="420" y2="500"/></g>')

def style_a():
    defs='''<defs>
<linearGradient id="a_sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1A1E3A"/><stop offset=".55" stop-color="#3B2F55"/><stop offset="1" stop-color="#6B4566"/></linearGradient>
<filter id="a_blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4"/></filter>
<filter id="a_glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.5"/></filter>
<linearGradient id="a_skin" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#C98F78"/><stop offset=".55" stop-color="#F3CDB6"/><stop offset="1" stop-color="#FFE6D6"/></linearGradient>
<linearGradient id="a_silk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0B0B10"/><stop offset=".45" stop-color="#2A2733"/><stop offset=".62" stop-color="#6E6680"/><stop offset=".72" stop-color="#25222D"/><stop offset="1" stop-color="#121117"/></linearGradient>
<linearGradient id="a_hair" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2A1C16"/><stop offset=".6" stop-color="#5A3D30"/><stop offset="1" stop-color="#22160F"/></linearGradient>
<radialGradient id="a_vig" cx=".5" cy=".45" r=".75"><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".55"/></radialGradient>
</defs>'''
    b=[defs,f'<rect width="{W}" height="{H}" fill="url(#a_sky)"/>']
    for x,y,r,c in lights(3,70,["#F2C26B","#F6D9A0","#E98A6B","#BFA6E8"],3,16,60,470):
        b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="{c}" opacity=".55" filter="url(#a_blur)"/>')
    b.append(window("#0C0D18",.85))
    b.append('<rect x="0" y="500" width="420" height="100" fill="#120F1C" opacity=".9"/>')
    b.append(f'<path d="{BODY}" fill="url(#a_skin)" stroke="#5A3328" stroke-width="1" stroke-opacity=".6"/>')
    b.append(f'<path d="{DRESS}" fill="url(#a_silk)" stroke="#000" stroke-width=".8"/>')
    b.append('<path d="M186 206 C188 190 190 178 192 170 M232 214 C232 196 230 182 228 172" stroke="#1A1820" stroke-width="1.6" fill="none"/>')
    b.append(f'<path d="{HAIR}" fill="url(#a_hair)"/>')
    b.append(f'<path d="{BODY}" fill="none" stroke="#FFE3C4" stroke-width="2.4" opacity=".55" filter="url(#a_glow)" clip-path="none"/>')
    b.append('<path d="M226 290 C236 330 240 380 238 428" stroke="#9A90B0" stroke-width="3" fill="none" opacity=".5" filter="url(#a_glow)"/>')
    b.append(f'<rect width="{W}" height="{H}" fill="url(#a_vig)"/>')
    b.append('<g font-family="\'Gowun Batang\',serif"><rect x="24" y="24" width="214" height="54" rx="2" fill="#0F1222" fill-opacity=".72"/><text x="38" y="57" font-size="15" fill="#F4E9DC">밤 열 시 반, 38층.</text></g>')
    return b
def style_b():
    b=[f'<rect width="{W}" height="{H}" fill="#202450"/>']
    random.seed(5)
    for i in range(14):
        x=random.uniform(0,400); w=random.uniform(30,70); h=random.uniform(120,380)
        b.append(f'<rect x="{x:.0f}" y="{500-h:.0f}" width="{w:.0f}" height="{h:.0f}" fill="#2E3470" stroke="#14161C" stroke-width="2"/>')
        for k in range(int(h//28)):
            if random.random()<.55:
                b.append(f'<rect x="{x+8:.0f}" y="{500-h+10+k*28:.0f}" width="{w-16:.0f}" height="9" fill="{random.choice(["#F6D84A","#FFF4E0","#5CC8B0","#E2457A"])}"/>')
    b.append('<g stroke="#14161C" stroke-width="10"><line x1="70" y1="0" x2="70" y2="600"/><line x1="350" y1="0" x2="350" y2="600"/><line x1="0" y1="500" x2="420" y2="500"/></g>')
    b.append('<rect x="0" y="505" width="420" height="95" fill="#14161C"/>')
    b.append(f'<path d="{BODY}" fill="#F7CDB4" stroke="#14161C" stroke-width="4" stroke-linejoin="round"/>')
    b.append('<path d="M145 208 C144 236 142 262 141 290 L152 292 C156 262 160 236 165 216 Z M184 272 C164 298 150 320 150 346 L170 332 Z" fill="#D99A86"/>')
    b.append(f'<path d="{DRESS}" fill="#16161E" stroke="#14161C" stroke-width="4" stroke-linejoin="round"/>')
    b.append('<path d="M226 230 C232 270 236 320 236 360 L246 356 C244 312 238 268 230 228 Z" fill="#E2457A"/>')
    b.append('<path d="M186 206 L192 170 M232 214 L228 172" stroke="#14161C" stroke-width="3"/>')
    b.append(f'<path d="{HAIR}" fill="#3A2A22" stroke="#14161C" stroke-width="4"/>')
    b.append('<path d="M214 100 C226 104 232 116 234 130" stroke="#E2457A" stroke-width="5" fill="none" stroke-linecap="round"/>')
    b.append('<g font-family="\'Black Han Sans\',sans-serif" transform="rotate(-8 330 420)"><text x="290" y="430" font-size="58" fill="#FFF4E0" stroke="#14161C" stroke-width="10" paint-order="stroke">두근</text></g>')
    b.append('<g><path d="M24 26 h188 a18 18 0 0 1 18 18 v28 a18 18 0 0 1 -18 18 h-120 l-14 18 l-2 -18 h-52 a18 18 0 0 1 -18 -18 v-28 a18 18 0 0 1 18 -18 z" fill="#FFF4E0" stroke="#14161C" stroke-width="4"/><text x="36" y="66" font-size="17" font-family="\'Gowun Dodum\',sans-serif" fill="#14161C">오늘도 현장이었어요?</text></g>')
    return b
def style_c():
    defs='''<defs>
<filter id="c_grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="4"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .09 0"/></filter>
<filter id="c_glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="c_bl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
<linearGradient id="c_sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#07081A"/><stop offset="1" stop-color="#1C1240"/></linearGradient>
</defs>'''
    b=[defs,f'<rect width="{W}" height="{H}" fill="url(#c_sky)"/>']
    b.append('<rect x="18" y="300" width="70" height="26" fill="#FF3D9A" filter="url(#c_bl)" opacity=".8"/><rect x="300" y="250" width="90" height="18" fill="#3DE0FF" filter="url(#c_bl)" opacity=".7"/><rect x="250" y="400" width="40" height="40" fill="#FFB547" filter="url(#c_bl)" opacity=".55"/>')
    random.seed(9)
    for _ in range(60):
        x=random.uniform(0,420); y=random.uniform(0,520); l=random.uniform(10,40)
        b.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x-3:.0f}" y2="{y+l:.0f}" stroke="#9FB4FF" stroke-width="1" opacity=".35"/>')
    b.append(window("#03030A",1))
    b.append('<rect x="0" y="500" width="420" height="100" fill="#05050C"/>')
    b.append(f'<path d="{BODY}" fill="#07070D"/>')
    b.append(f'<path d="{HAIR}" fill="#07070D"/>')
    b.append(f'<path d="{BODY}" fill="none" stroke="#FF3D9A" stroke-width="2.2" stroke-dasharray="0 0" opacity=".9" filter="url(#c_glow)" clip-path="url(#c_left)"/>')
    b.append('<path d="M145 208 C144 236 142 262 141 290 M184 272 C164 298 150 320 150 346 C152 380 156 410 160 432" stroke="#FF3D9A" stroke-width="2.5" fill="none"/>')
    b.append('<path d="M256 170 C268 152 284 130 290 116 M236 272 C256 298 270 320 270 346 C268 380 264 410 260 432" stroke="#3DE0FF" stroke-width="2.5" fill="none"/>')
    b.append('<path d="M236 130 C238 146 236 156 234 162" stroke="#3DE0FF" stroke-width="2" fill="none"/>')
    b.append(f'<rect width="{W}" height="{H}" filter="url(#c_grain)"/>')
    b.append('<g font-family="\'Nanum Pen Script\',cursive"><text x="28" y="66" font-size="27" fill="#FFB547">유리에 비친 건 남편이 아니었다.</text></g>')
    return b
for name,fn in (("style_a",style_a),("style_b",style_b),("style_c",style_c)):
    body="".join(fn())
    open(name+".svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{body}</svg>')
print("ok")
