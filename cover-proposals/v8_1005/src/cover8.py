import base64, io, math, os, sys
import glassglobe as G
from PIL import Image
N_='f/ns/package/files/'
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
def png(im):
    bf=io.BytesIO(); im.save(bf,'PNG',optimize=True); return 'data:image/png;base64,'+base64.b64encode(bf.getvalue()).decode()
GOLD='#b38f4f'; GOLDL='#d9c49a'
def mark(x,y,s=6.6):
    o=''
    for th in (-90,30,150):
        p=lambda a,d:(x+d*math.cos(math.radians(a)),y+d*math.sin(math.radians(a)))
        q=[(x,y),p(th-30,s),p(th,s*math.sqrt(3)),p(th+30,s)]
        o+='<path d="M'+' L'.join(f'{a:.2f},{b:.2f}' for a,b in q)+'Z" fill="#E60012"/>'
    return o
def logo(x,y,s=6.6,fs=12.5,col='#1a1a1a'):
    return mark(x,y,s)+f'<text x="{x+18*s/6.6}" y="{y+4*s/6.6}" font-family="Liberation Serif" font-size="{fs}" fill="{col}">Mitsubishi Corporation</text>'
CSS=f"""@font-face{{font-family:NS;font-weight:300;src:url(data:font/woff2;base64,{b64(N_+'noto-sans-latin-300-normal.woff2')})}}
@font-face{{font-family:NS;font-weight:400;src:url(data:font/woff2;base64,{b64(N_+'noto-sans-latin-400-normal.woff2')})}}
@page{{size:420mm 297mm;margin:0}}*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#fff}}
.sp{{position:relative;width:1190px;height:842px;overflow:hidden;background:#fff;page-break-after:always;zoom:1.3333;font-family:NS}}
.a{{position:absolute}}
.ttl{{font-weight:300;font-size:21px;line-height:1.38;color:#2b2f34;letter-spacing:.35px}}
.cap{{font-size:6.6px;letter-spacing:1.6px;color:#8a8f95}}
"""
def title(x,y):
    return (f'<div class="a ttl" style="left:{x}px;top:{y}px">Mitsubishi Corporation<br>Mineral Resources Group<br>Corporate Profile</div>'
            f'<div class="a" style="left:{x}px;top:{y+104}px;width:58px;border-top:1px solid #C8102E"></div>')
def img(x,y,w,h,uri,extra=''):
    return f'<img class="a" src="{uri}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}">'
def shadow(cx,cy,rx,ry,op=.22):
    return f'<div class="a" style="left:{cx-rx}px;top:{cy-ry}px;width:{2*rx}px;height:{2*ry}px;border-radius:50%;background:radial-gradient(closest-side,rgba(60,80,100,{op}),rgba(60,80,100,0));filter:blur(2px)"></div>'
def globe_block(gx,gy,D,view,orbits,res=1700,back_alpha=.20):
    """gx,gy top-left, D diameter (page px). view=(lon0,lat0,roll). returns (behind_svg, img, front_svg)"""
    key=f'v8/gl_{view[0]}_{view[1]}_{view[2]}_{res}_{back_alpha}.png'
    if not os.path.exists(key): G.render(res,*view,back_a=back_alpha).save(key)
    uri=png(Image.open(key))
    bk='';fr=''
    for o in orbits:
        f,b,ds=G.orbit(D,*view,cx=gx,cy=gy,**o)
        bk+=f'<path d="{b}" fill="none" stroke="{GOLDL}" stroke-width=".55" opacity=".55"/>'
        fr+=f'<path d="{f}" fill="none" stroke="{GOLD}" stroke-width=".75" opacity=".9"/>'
        for x,y,front in ds:
            if front: fr+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{GOLD}" opacity=".18"/><circle cx="{x:.1f}" cy="{y:.1f}" r="2.1" fill="{GOLD}"/>'
    return bk, img(gx,gy,D,D,uri), fr
def svg(inner,w=1190,h=842): return f'<svg class="a" style="left:0;top:0;overflow:visible" width="{w}" height="{h}">{inner}</svg>'
def fold(): return '<div class="a" style="left:595px;top:0;height:842px;border-left:.5px dashed #d9dcdf"></div>'
def back_info(x=56,y=742,extra=''):
    return (svg(logo(x+6,y,5.4,10.5))+f'<div class="a cap" style="left:{x}px;top:{y+20}px;line-height:1.7">MINERAL RESOURCES GROUP<br>2-3-1 Marunouchi, Chiyoda-ku, Tokyo 100-8086, Japan<br>www.mitsubishicorp.com</div>'+extra)
pages=[]

# ---------- B-1  Twin hemispheres (wrap) ----------
FR=(-42,6,-8); BK=(138,-14,6)
D1=580; gx1,gy1=595+250,205
D2=380; gx2,gy2=110,190
orb1=[dict(tilt=-72,yaw=-14,rr=1.16,dots=(200,320)),dict(tilt=-64,yaw=22,rr=1.30,dots=(150,250))]
orb2=[dict(tilt=-70,yaw=-10,rr=1.22,dots=(330,))]
b1,i1,f1=globe_block(gx1,gy1,D1,FR,orb1)
b2,i2,f2=globe_block(gx2,gy2,D2,BK,orb2)
# big arc connecting the two hemispheres across the spine
arc=f'<path d="M-20,640 C260,820 760,860 1210,640" fill="none" stroke="{GOLD}" stroke-width=".7" opacity=".7"/><path d="M-20,300 C300,190 700,170 1210,250" fill="none" stroke="{GOLDL}" stroke-width=".55" opacity=".6"/>'
body=svg(b1+b2+arc)+shadow(gx1+D1/2,gy1+D1+34,D1*.36,22)+shadow(gx2+D2/2,gy2+D2+24,D2*.36,12,.18)+i1+i2+svg(f1+f2)
body+=title(595+48,96)+svg(logo(595+232,800))+back_info()
body+=f'<div class="a cap" style="left:56px;top:612px;line-height:1.8">METALLURGICAL COAL&nbsp;&nbsp;·&nbsp;&nbsp;COPPER&nbsp;&nbsp;·&nbsp;&nbsp;IRON ORE&nbsp;&nbsp;·&nbsp;&nbsp;CRITICAL MINERALS&nbsp;&nbsp;·&nbsp;&nbsp;TRADING</div>'
pages.append(('B-1',f'<div class="sp">{body}{fold()}</div>'))

# ---------- B-2  Panorama (wrap, A x B hybrid) ----------
LA,LB,LT,LBt=50,410,80,-58
W2,H2=1190,int(1190*(LT-LBt)/(LB-LA)*1.0)
key='v8/flat.png'
if not os.path.exists(key): G.render_flat(3000,int(3000*H2/W2),LA,LB,LT,LBt).save(key)
my=250
glass=f'<div class="a" style="left:0;top:{my-30}px;width:1190px;height:{H2+60}px;background:linear-gradient(180deg,rgba(255,255,255,0) 0%,rgba(214,228,240,.55) 22%,rgba(198,216,233,.75) 52%,rgba(220,232,242,.5) 80%,rgba(255,255,255,0) 100%)"></div>'
glass+=f'<div class="a" style="left:-200px;top:{my-60}px;width:900px;height:{H2+120}px;background:radial-gradient(closest-side,rgba(255,255,255,.75),rgba(255,255,255,0));"></div>'
P=lambda la,lo:G.flat_xy(la,lo,W2,H2,LA,LB,LT,LBt)
tk=P(35.7,139.7)
hubs=[(-23,-69),(-14,-73),(-22,148),(-23,119),(-26,28),(33,-111),(51,0),(-6,-50),(52,-120)]
arcs=''
for la,lo in hubs:
    x,y=P(la,lo); x0,y0=tk
    # route that wraps the right way round the sheet
    if x<x0 and lo<0: x0=x0  # Americas sit to the right on this sheet
    mx=(x0+x)/2; myy=min(y0,y)-abs(x-x0)*.16-10
    arcs+=f'<path d="M{x0:.1f},{y0+my:.1f} Q{mx:.1f},{myy+my:.1f} {x:.1f},{y+my:.1f}" fill="none" stroke="{GOLD}" stroke-width=".6" opacity=".75"/><circle cx="{x:.1f}" cy="{y+my:.1f}" r="4.5" fill="{GOLD}" opacity=".2"/><circle cx="{x:.1f}" cy="{y+my:.1f}" r="1.8" fill="{GOLD}"/>'
arcs+=f'<circle cx="{tk[0]:.1f}" cy="{tk[1]+my:.1f}" r="2.6" fill="#C8102E"/>'
orbit=f'<ellipse cx="640" cy="{my+H2*.52}" rx="760" ry="250" transform="rotate(-6 640 {my+H2*.52})" fill="none" stroke="{GOLDL}" stroke-width=".6" opacity=".7"/>'
body=glass+svg(orbit)+img(0,my,W2,H2,png(Image.open(key)))+svg(arcs)
body+=title(595+48,96)+svg(logo(595+232,800))+back_info()
pages.append(('B-2',f'<div class="sp">{body}{fold()}</div>'))

# ---------- B-3  Centred jewel globe, see-through (front-led) ----------
V3=(-28,-8,-10); D3=500; gx3,gy3=595+297-D3/2,250
orb3=[dict(tilt=-78,yaw=-12,rr=1.13,dots=(205,330)),dict(tilt=-70,yaw=18,rr=1.26,dots=(160,250)),dict(tilt=-74,yaw=4,rr=1.40,dots=(290,))]
b3,i3,f3=globe_block(gx3,gy3,D3,V3,orb3,res=1700,back_alpha=.34)
back_orb=f'<path d="M-10,560 C220,500 480,520 600,560" fill="none" stroke="{GOLD}" stroke-width=".7" opacity=".7"/><path d="M-10,610 C240,560 470,590 600,630" fill="none" stroke="{GOLDL}" stroke-width=".55" opacity=".6"/>'
body=svg(b3+back_orb)+shadow(gx3+D3/2,gy3+D3+40,D3*.38,16)+i3+svg(f3)+title(595+48,96)
body+=svg(logo(595+232,800))+back_info()
pages.append(('B-3',f'<div class="sp">{body}{fold()}</div>'))

html='<!doctype html><meta charset=utf-8><style>'+CSS+'</style>'+''.join(p for _,p in pages)
open('v8/covers8.html','w').write(html)
