# 表紙 幾何学案 A〜E（白ベース・抽象・さりげない色）
import base64, math, random
N_='f/ns/package/files/'
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
INK='#2b2f34'; GR='#8e959c'; SV='#c3c8cd'; GOLD='#b08a4a'; GOLDL='#d8c39a'; RED='#C8102E'
def mark(x,y,s=6.6):
    o=''
    for th in (-90,30,150):
        p=lambda a,d:(x+d*math.cos(math.radians(a)),y+d*math.sin(math.radians(a)))
        q=[(x,y),p(th-30,s),p(th,s*math.sqrt(3)),p(th+30,s)]
        o+='<path d="M'+' L'.join(f'{a:.2f},{b:.2f}' for a,b in q)+'Z" fill="#E60012"/>'
    return o
def logo(x,y,s=6.2,fs=11.8):
    return mark(x,y,s)+f'<text x="{x+17*s/6.6}" y="{y+4*s/6.6}" font-family="Liberation Serif" font-size="{fs}" fill="#1a1a1a">Mitsubishi Corporation</text>'
CSS=f"""@font-face{{font-family:NS;font-weight:300;src:url(data:font/woff2;base64,{b64(N_+'noto-sans-latin-300-normal.woff2')})}}
@page{{size:210mm 297mm;margin:0}}*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#fff}}
.pg{{position:relative;width:595px;height:842px;overflow:hidden;background:#fff;page-break-after:always;zoom:1.3333;font-family:NS}}
.a{{position:absolute}}
.ttl{{font-weight:300;font-size:19px;line-height:1.42;color:{INK};letter-spacing:.3px}}
"""
def page(svg,dark=False):
    t=(f'<div class="a ttl" style="left:48px;top:92px">Mitsubishi Corporation<br>Mineral Resources Group<br>Corporate Profile</div>'
       f'<div class="a" style="left:48px;top:182px;width:44px;border-top:1px solid {RED}"></div>')
    return f'<div class="pg"><svg class="a" style="left:0;top:0" width="595" height="842" viewBox="0 0 595 842">{svg}{logo(232,792)}</svg>{t}</div>'
pages=[]

# ---------- A. 二つの輪（両輪） ----------
def ringset(cx,cy,r,col,n=4,gap=2.0,w=.5):
    return ''.join(f'<circle cx="{cx}" cy="{cy}" r="{r+i*gap}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{1-i*.18:.2f}"/>' for i in range(n))
R=150; c1=(330,600); c2=(470,568)
d=math.dist(c1,c2); a=d/2; h=math.sqrt(R*R-a*a)
mx=(c1[0]+c2[0])/2; my=(c1[1]+c2[1])/2
p1=(mx+h*(c2[1]-c1[1])/d, my-h*(c2[0]-c1[0])/d); p2=(mx-h*(c2[1]-c1[1])/d, my+h*(c2[0]-c1[0])/d)
lens=f'M{p1[0]:.1f},{p1[1]:.1f} A{R},{R} 0 0 1 {p2[0]:.1f},{p2[1]:.1f} A{R},{R} 0 0 1 {p1[0]:.1f},{p1[1]:.1f}Z'
s_=('<defs><linearGradient id="ga" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f3ead8"/><stop offset="1" stop-color="#c9ab72"/></linearGradient></defs>'
   f'<path d="{lens}" fill="url(#ga)" opacity=".42"/>'
   +ringset(*c1,R,GR)+ringset(*c2,R,'#5f7487')
   +f'<circle cx="{p1[0]:.1f}" cy="{p1[1]:.1f}" r="2.4" fill="{GOLD}"/><circle cx="{p2[0]:.1f}" cy="{p2[1]:.1f}" r="2.4" fill="{GOLD}"/>')
pages.append(('A','二つの輪',page(s_)))

# ---------- B. 三つの環（ボロメオの環：投資・トレーディング・CVC） ----------
r=128; cx,cy=410,585
cs=[(cx+74*math.cos(math.radians(a)),cy+74*math.sin(math.radians(a))) for a in (-90,30,150)]
cols=['#3d4249','#5f7487',GOLD]
def rings(c,col,a0=0,a1=360):
    out=''
    for k in range(4):
        rr=r+k*2.2
        pts=[(c[0]+rr*math.cos(math.radians(t)),c[1]+rr*math.sin(math.radians(t))) for t in [a0+(a1-a0)*q/80 for q in range(81)]]
        out+='<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+f'" fill="none" stroke="{col}" stroke-width=".55" opacity="{1-k*.18:.2f}"/>'
    return out
def inter(c0,c1):
    d=math.dist(c0,c1); a=d/2; h=math.sqrt(r*r-a*a); mx=(c0[0]+c1[0])/2; my=(c0[1]+c1[1])/2
    return [(mx+h*(c1[1]-c0[1])/d, my-h*(c1[0]-c0[0])/d),(mx-h*(c1[1]-c0[1])/d, my+h*(c1[0]-c0[0])/d)]
o=''.join(rings(c,col) for c,col in zip(cs,cols))
for i_,j_ in [(0,1),(1,2),(2,0)]:
    for p in inter(cs[i_],cs[j_]):
        c=cs[i_]; ang=math.degrees(math.atan2(p[1]-c[1],p[0]-c[0]))
        pts=[(c[0]+(r+3.3)*math.cos(math.radians(t)),c[1]+(r+3.3)*math.sin(math.radians(t))) for t in [ang-9+18*q/20 for q in range(21)]]
        o+='<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'" fill="none" stroke="#fff" stroke-width="12"/>'
        o+=rings(c,cols[i_],ang-11,ang+11)
pages.append(('B','三つの環',page(o)))

# ---------- C. 収束する線（つなぐ） ----------
random.seed(3); o='<defs><linearGradient id="gc" x1="0" x2="1"><stop offset="0" stop-color="#9aa1a8"/><stop offset=".7" stop-color="#5f7487"/><stop offset="1" stop-color="#b08a4a"/></linearGradient></defs>'
n=64
for i in range(n):
    t=i/(n-1); y0=300+t*520+random.uniform(-3,3); x0=-10
    y1=600+(t-.5)*26; x1=640
    o+=f'<path d="M{x0},{y0:.1f} C230,{y0:.1f} 300,{y1+(t-.5)*60:.1f} {x1},{y1:.1f}" fill="none" stroke="url(#gc)" stroke-width="{.45 if i%7 else .8}" opacity="{.5+.5*math.sin(math.pi*t):.2f}"/>'
o+=f'<circle cx="560" cy="600" r="2.8" fill="{GOLD}"/>'
pages.append(('C','収束する線',page(o)))

# ---------- D. 結晶とネットワーク ----------
o=''; step=34; pts={}
for j in range(-2,16):
    for i in range(-2,14):
        x=200+i*step+(j%2)*step/2; y=360+j*step*math.sqrt(3)/2
        cxh,cyh=440,600
        dd=math.dist((x,y),(cxh,cyh))
        if dd<250: pts[(i,j)]=(x,y,dd)
for (i,j),(x,y,dd) in pts.items():
    for (di,dj) in [(1,0),(0,1),(-1,1) if j%2==0 else (1,1)]:
        q=pts.get((i+di,j+dj))
        if q:
            op=max(0,1-dd/250)*.9
            o+=f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="#8e959c" stroke-width=".45" opacity="{op:.2f}"/>'
    o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{1.4 if dd>90 else 1.8}" fill="{INK}" opacity="{max(0,1-dd/250):.2f}"/>'
# hexagon crystal outline + gold nodes
hx=[(440+120*math.cos(math.radians(30+60*k)),600+120*math.sin(math.radians(30+60*k))) for k in range(6)]
o+='<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in hx)+f'Z" fill="none" stroke="{INK}" stroke-width=".9"/>'
for x,y in hx[::2]: o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{GOLD}"/>'
pages.append(('D','結晶とネットワーク',page(o)))

# ---------- E. 支える形とひらく形（Hold / Connect） ----------
o=(f'<rect x="74" y="600" width="126" height="126" fill="none" stroke="{INK}" stroke-width=".9"/>'
   f'<rect x="80" y="606" width="114" height="114" fill="none" stroke="{SV}" stroke-width=".5"/>')
for k in range(7):
    rr=360+k*12
    o+=f'<path d="M200,{600+0} A{rr},{rr} 0 0 1 {200+rr*0.98:.1f},{600-rr*0.8:.1f}" fill="none" stroke="{"#5f7487" if k<3 else SV}" stroke-width=".55" opacity="{1-k*.1:.2f}"/>'
o+=f'<circle cx="200" cy="600" r="3" fill="{GOLD}"/>'
pages.append(('E','支える形とひらく形',page(o)))

open('cover10.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS+'</style>'+''.join(p for _,_,p in pages))
