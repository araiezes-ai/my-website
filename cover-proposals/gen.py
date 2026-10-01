import json, math, numpy as np
from global_land_mask import globe
W,H=595,842
L0,P0=math.radians(120),math.radians(18)
def inv(x,y,cx,cy,R):
    xs=(x-cx)/R; ys=-(y-cy)/R; rho=np.hypot(xs,ys); m=rho<1
    c=np.arcsin(np.clip(rho,0,1)); rho=np.where(rho==0,1e-9,rho)
    lat=np.arcsin(np.cos(c)*math.sin(P0)+ys*np.sin(c)*math.cos(P0)/rho)
    lon=L0+np.arctan2(xs*np.sin(c),rho*np.cos(c)*math.cos(P0)-ys*np.sin(c)*math.sin(P0))
    lon=(np.degrees(lon)+180)%360-180
    return np.degrees(lat),lon,m
def fwd(lon,lat,cx,cy,R):
    l=math.radians(lon)-L0; p=math.radians(lat)
    x=R*math.cos(p)*math.sin(l); y=R*(math.cos(P0)*math.sin(p)-math.sin(P0)*math.cos(p)*math.cos(l))
    return cx+x, cy-y
jp=json.load(open('japan.geojson'))
def japan_path(cx,cy,R):
    d=[]
    g=jp['geometry']; polys=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
    for poly in polys:
        ring=poly[0]
        pts=[fwd(lo,la,cx,cy,R) for lo,la in ring]
        d.append('M'+'L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'Z')
    return ''.join(d)
def globe_svg(cx,cy,R,step=4.6,top=480,dot='#c2c4c6'):
    xs=np.arange(0,W+step,step); ys=np.arange(top,H,step)
    X,Y=np.meshgrid(xs,ys); X=X.ravel(); Y=Y.ravel()
    lat,lon,m=inv(X,Y,cx,cy,R)
    land=np.zeros_like(m); land[m]=globe.is_land(lat[m],lon[m])
    # hide japan dots (drawn solid)
    from shapely.geometry import shape, Point
    from shapely.prepared import prep
    J=prep(shape(jp['geometry']).buffer(0.25))
    jpm=np.array([J.contains(Point(a,b)) if (128<a<147 and 29<b<46) else False for a,b in zip(lon,lat)])
    sel=land.astype(bool)&~jpm
    dots=''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.15"/>' for x,y in zip(X[sel],Y[sel]))
    return f'''<defs><radialGradient id="sph" cx="38%" cy="30%" r="75%"><stop offset="0" stop-color="#ffffff"/><stop offset=".7" stop-color="#f3f4f5"/><stop offset="1" stop-color="#e6e7e9"/></radialGradient></defs>
<circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#sph)"/>
<g fill="none" stroke="#d9dbdd" stroke-width=".6"><circle cx="{cx+260}" cy="{cy-250}" r="210"/><circle cx="{cx-40}" cy="{cy+80}" r="300"/><circle cx="{cx+180}" cy="{cy+160}" r="160"/></g>
<g fill="{dot}">{dots}</g>'''
def arcs(cx,cy,R,pairs,col):
    out=''
    for (a,b) in pairs:
        la1,lo1=map(math.radians,a); la2,lo2=map(math.radians,b)
        p1=np.array([math.cos(la1)*math.cos(lo1),math.cos(la1)*math.sin(lo1),math.sin(la1)])
        p2=np.array([math.cos(la2)*math.cos(lo2),math.cos(la2)*math.sin(lo2),math.sin(la2)])
        om=math.acos(np.dot(p1,p2)); pts=[]
        for t in np.linspace(0,1,60):
            p=(math.sin((1-t)*om)*p1+math.sin(t*om)*p2)/math.sin(om)
            h=1+0.06*math.sin(math.pi*t)
            lat=math.degrees(math.asin(p[2])); lon=math.degrees(math.atan2(p[1],p[0]))
            x,y=fwd(lon,lat,cx,cy,R*h); pts.append((x,y))
        out+='<path d="M'+'L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+f'" fill="none" stroke="{col}" stroke-width=".7"/>'
        for x,y in (pts[0],):
            out+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.2" fill="{col}"/>'
    return out
def coil_svg():
    cx,cy=440,640; out=[]
    for i,r in enumerate(np.arange(64,420,5.2)):
        n=int(2*math.pi*r/5.2)
        for k in range(n):
            a=2*math.pi*k/n+i*0.13
            x=cx+r*math.cos(a); y=cy+r*0.97*math.sin(a)
            if y<480 or x>W+3 or y>780 or x<100: continue
            shade=0.55+0.45*(0.5+0.5*math.cos(a+2.3))
            g=int(120+110*shade); out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.1" fill="rgb({g},{g+2},{g+4})"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="56" fill="none" stroke="#c9cbcd" stroke-width=".6"/>')
    return ''.join(out)
ICON='''<g fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
<ellipse cx="34" cy="44" rx="17" ry="17"/><ellipse cx="34" cy="44" rx="6" ry="6"/><path d="M34 27 A17 17 0 0 1 34 27"/>
<path d="M22 32 A13 13 0 0 1 46 32" opacity=".0"/><path d="M34 27 L62 27 M34 61 L62 61"/><path d="M62 27 A6 17 0 0 1 62 61"/>
<path d="M50 14 H72 M50 22 H72 M61 14 V22"/></g>'''
def page(visual,title_lines,tag=None,accent='#EB7357'):
    t=''.join(f'<text x="62" y="{(372 if tag else 390)+i*24}">{s}</text>' for i,s in enumerate(title_lines))
    tg=f'<text x="62" y="448" font-size="9.5" fill="#8a8d90" letter-spacing=".3">{tag}</text>' if tag else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" fill="#fff"/>
<defs><linearGradient id="fx" x1="0" x2="1"><stop offset="0" stop-color="#000"/><stop offset=".22" stop-color="#fff"/></linearGradient><linearGradient id="fy" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000"/><stop offset=".12" stop-color="#fff"/><stop offset=".9" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>
<mask id="mk"><rect x="110" y="486" width="{W-110}" height="290" fill="url(#fx)"/></mask><mask id="mk2"><rect x="110" y="486" width="{W-110}" height="290" fill="url(#fy)"/></mask></defs>
<g mask="url(#mk2)"><g mask="url(#mk)"><svg x="110" y="486" width="{W-110}" height="290" viewBox="110 486 {W-110} 290" overflow="hidden">{visual}</svg></g></g>
<rect x="62" y="261" width="85" height="85" fill="{accent}"/><g transform="translate(66.5,265.5)">{ICON}</g>
<g font-family="Liberation Sans, Arial" font-size="18.5" fill="#4a4d50">{t}</g>{tg}
<line x1="0" y1="468" x2="520" y2="468" stroke="#5a5d60" stroke-width=".7"/>
<rect x="208" y="790" width="180" height="28" fill="#fff" stroke="#b5b7b9" stroke-dasharray="3 2" stroke-width=".6"/>
<text x="298" y="808" text-anchor="middle" font-family="IPAPGothic" font-size="8" fill="#9a9c9e">三菱商事ロゴ（正規データ配置）</text>
</svg>'''
TITLE=['Mitsubishi Corporation','Mineral Resources Group','Steel Team Brochure']
import math as _m
R=500
_x,_y=fwd(137.5,36.5,0,0,R)
cx,cy=440-_x,650-_y
gA=globe_svg(cx,cy,R)+f'<path d="{japan_path(cx,cy,R)}" fill="#55585b"/>'
gB=globe_svg(cx,cy,R)+arcs(cx,cy,R,[((-20.3,118.6),(34.4,133.5)),((-21.3,149.3),(35.2,137.0)),((13.7,100.5),(34.7,135.4))],'#d0312d')+f'<path d="{japan_path(cx,cy,R)}" fill="#55585b"/>'
gC=coil_svg()
pages=[page(gA,TITLE),page(gB,TITLE,'A partner forging the future of resources — together.'),page(gC,TITLE,'A partner forging the future of resources — together.')]
labels=['案A｜フォーマット準拠：地球儀＋日本','案B｜原料→日本の流れを細線で一筋','案C｜鋼材コイルのドット表現']
html='<!doctype html><meta charset=utf-8><style>@page{size:A4;margin:0}body{margin:0}.p{width:210mm;height:297mm;page-break-after:always;position:relative}.p svg{width:210mm;height:297mm;display:block}</style>'+''.join(f'<div class=p>{p}</div>' for p in pages)
open('covers.html','w').write(html)
sheet='<!doctype html><meta charset=utf-8><body style="margin:0;background:#e9eaec;font-family:IPAPGothic"><div style="display:flex;gap:28px;padding:28px">'+''.join(f'<div><div style="box-shadow:0 2px 10px rgba(0,0,0,.18);width:595px;height:842px">{p}</div><div style="margin-top:12px;font-size:17px;color:#333">{l}</div></div>' for p,l in zip(pages,labels))+'</div>'
open('sheet.html','w').write(sheet)
