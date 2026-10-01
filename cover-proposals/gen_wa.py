import math, random, base64
random.seed(7)
W,H=595,842
F='f/fontsource-shippori-mincho-5.3.0/package/files/'; G='f/fontsource-cormorant-garamond-5.3.0/package/files/'
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
css=f"""@font-face{{font-family:SM;src:url(data:font/woff2;base64,{b64(F+'shippori-mincho-japanese-400-normal.woff2')})}}
@font-face{{font-family:SM;src:url(data:font/woff2;base64,{b64(F+'shippori-mincho-latin-400-normal.woff2')});unicode-range:U+0000-00FF}}
@font-face{{font-family:CG;src:url(data:font/woff2;base64,{b64(G+'cormorant-garamond-latin-500-normal.woff2')})}}"""
# 円相 = wire-rod coil drawn as fine ink loops
cx,cy,R=300,390,168
loops=[]
for i in range(46):
    t=i/45
    ox=cx-26+52*t+random.uniform(-1.5,1.5); oy=cy+random.uniform(-2,2)
    r=R+random.uniform(-5,5)
    a0=math.radians(-70+random.uniform(-14,6)); a1=math.radians(235+random.uniform(-8,22))
    pts=[]
    n=140
    for k in range(n+1):
        a=a0+(a1-a0)*k/n
        rr=r*(1+0.012*math.sin(3*a+i))
        pts.append((ox+rr*math.cos(a)*1.0, oy+rr*math.sin(a)*0.985))
    d='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)
    op=0.18+0.5*(math.sin(math.pi*t))**1.5
    loops.append(f'<path d="{d}" stroke="#2b2b2b" stroke-opacity="{op:.2f}" stroke-width="{random.uniform(.3,.6):.2f}" fill="none" stroke-linecap="round"/>')
# Mitsubishi three-diamond mark (draft; replace with official artwork)
def mark(x,y,s):
    out=''
    for th in (-90,30,150):
        def p(ang,dist): a=math.radians(ang); return (x+dist*math.cos(a), y+dist*math.sin(a))
        pts=[(x,y),p(th-30,s),p(th,s*math.sqrt(3)),p(th+30,s)]
        out+='<path d="M'+' L'.join(f'{a:.2f},{b:.2f}' for a,b in pts)+'Z" fill="#E60012"/>'
    return out
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" fill="#fff"/>
<text x="48" y="64" font-family="CG" font-size="9" letter-spacing="2.2" fill="#6b6b6b">MINERAL RESOURCES GROUP</text>
<line x1="48" y1="74" x2="72" y2="74" stroke="#9a9a9a" stroke-width=".5"/>
<g>{''.join(loops)}</g>
<text x="530" y="118" font-family="SM" font-size="15.5" fill="#222" letter-spacing="7" style="writing-mode:vertical-rl">資源の未来を、ともに鍛える。</text>
<rect x="522.5" y="408" width="15" height="15" fill="#B7282E"/>
<text x="530" y="419.5" font-family="SM" font-size="10.5" fill="#fff" text-anchor="middle">鋼</text>
<text x="48" y="640" font-family="SM" font-size="30" fill="#1f1f1f" letter-spacing="10">鉄鋼</text>
<text x="49" y="664" font-family="CG" font-size="11" letter-spacing="3.2" fill="#555">STEEL BUSINESS</text>
<text x="49" y="690" font-family="CG" font-size="10" font-style="italic" fill="#8a8a8a" letter-spacing=".4">A partner forging the future of resources — together.</text>
<g transform="translate(0,0)">{mark(232,786,7.2)}</g>
<text x="250" y="790" font-family="Liberation Serif" font-size="12.5" fill="#1a1a1a">Mitsubishi Corporation</text>
</svg>'''
html=f'<!doctype html><meta charset=utf-8><style>{css}@page{{size:A4;margin:0}}body{{margin:0}}svg{{width:210mm;height:297mm;display:block}}</style>{svg}'
open('wa.html','w').write(html)
open('wa_prev.html','w').write(f'<!doctype html><meta charset=utf-8><style>{css}body{{margin:0;background:#e6e6e4;display:flex;justify-content:center;padding:30px;align-items:flex-start}}svg{{width:595px;height:842px;box-shadow:0 3px 14px rgba(0,0,0,.15)}}</style>{svg}')
