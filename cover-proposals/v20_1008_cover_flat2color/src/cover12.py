# 表紙 v12：白地＋2色のフラットな幾何学（ポストモダン／バウハウス的）。形ごとに意味を持たせる
import math
exec(open('cover11.py').read().split('pages=[]')[0].split('UID=[0]')[0])  # mark/logo/CSS 流用
CU='#B4693E'; VR='#D24A2B'; GP='#2E3136'
PAIRS=[('1','カッパー × グラファイト',CU,GP),('2','朱 × グラファイト',VR,GP),('3','朱 × カッパー',VR,CU)]
def page2(svg,c1):
    t=(f'<div class="a k1" style="left:48px;top:74px">MITSUBISHI CORPORATION</div>'
       f'<div class="a" style="left:48px;top:104px;width:3px;height:74px;background:{c1}"></div>'
       f'<div class="a ttl" style="left:62px;top:102px">MINERAL<br>RESOURCES</div>'
       f'<div class="a k2" style="left:62px;top:192px">CORPORATE PROFILE</div>')
    foot='<line x1="48" y1="784" x2="547" y2="784" stroke="#9aa0a6" stroke-width=".5"/>'+logo(400,806)
    return f'<div class="pg"><svg class="a" style="left:0;top:0" width="595" height="842" viewBox="0 0 595 842">{svg}{foot}</svg>{t}</div>'
def P(pts): return 'M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'Z'
def A(c1,c2):  # 両輪：持つ（面）と動かす（線）
    o=f'<path d="M48,720 A126,126 0 0 1 300,720Z" fill="{c2}"/>'
    for k in range(12):
        r=126-k*10.5
        o+=f'<path d="M{426-r:.1f},720 A{r:.1f},{r:.1f} 0 0 1 {426+r:.1f},720" fill="none" stroke="{c1}" stroke-width="3.2"/>'
    o+=f'<rect x="48" y="728" width="504" height="10" fill="{c1}"/>'
    return o
def B(c1,c2):  # 循環：投資→事業運営→トレーディング→CVC
    s=166; x0,y0=128,392; o=''
    cells=[(0,0,(0,1)),(1,0,(0,0)),(1,1,(1,0)),(0,1,(1,1))]
    for k,(i,j,(pi,pj)) in enumerate(cells):
        x=x0+i*s; y=y0+j*s; cx=x+pi*s; cy=y+pj*s
        # 四分円：中心(cx,cy)、セル内側へ
        sx=1 if pi==0 else -1; sy=1 if pj==0 else -1
        p1=(cx+sx*s,cy); p2=(cx,cy+sy*s); sweep=1 if sx*sy>0 else 0
        col=c1 if k==3 else c2
        o+=f'<path d="M{cx},{cy} L{p1[0]},{p1[1]} A{s},{s} 0 0 {sweep} {p2[0]},{p2[1]}Z" fill="{col}"/>'
    return o
def C(c1,c2):  # つなぐ：二つの側を結ぶ線の束、その間に生まれる価値
    cx,by=372,610; o=''
    for k in range(10):
        r=140-k*11
        o+=f'<path d="M{cx-r},300 L{cx-r},{by-r*0+0} A{r},{r} 0 0 0 {cx+r},{by} L{cx+r},300" fill="none" stroke="{c2}" stroke-width="3.4"/>'
    o+=f'<circle cx="{cx}" cy="{by}" r="34" fill="{c1}"/>'
    return o
def D(c1,c2):  # バリューチェーン：原石（四角）が磨かれて製品（円）になる
    s=96; g=12; x0,y0=104,400; o=''
    for j in range(3):
        for i in range(4):
            x=x0+i*(s+g); y=y0+j*(s+g); h=s/2
            col=c1 if i==3 else c2
            if i==0: o+=f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{col}"/>'
            elif i==1: o+=f'<path d="M{x},{y} L{x+h},{y} A{h},{h} 0 0 1 {x+s},{y+h} L{x+s},{y+s} L{x},{y+s}Z" fill="{col}"/>'
            elif i==2: o+=f'<path d="M{x},{y+h} A{h},{h} 0 0 1 {x+s},{y+h} L{x+s},{y+s} L{x},{y+s}Z" fill="{col}"/>'
            else: o+=f'<circle cx="{x+h}" cy="{y+h}" r="{h}" fill="{col}"/>'
    return o
def E(c1,c2):  # 持つ力：器（資産）が資源を抱える
    cx,cy,R=350,560,170
    o=f'<path d="M{cx-R},{cy} A{R},{R} 0 0 0 {cx+R},{cy}Z" fill="{c2}"/>'
    o+=f'<circle cx="{cx}" cy="{cy-84}" r="78" fill="{c1}"/>'
    return o
def F(c1,c2):  # 前へ：一手先へ進み続ける
    o=''; w=118; h=52
    for j in range(5):
        for i in range(4):
            x=150+i*(w+6)-(j%2)*40; y=430+j*(h+8)
            col=c1 if (i,j)==(2,2) else c2
            o+=f'<path d="{P([(x,y),(x+w-34,y),(x+w,y+h/2),(x+w-34,y+h),(x,y+h),(x+34,y+h/2)])}" fill="{col}"/>'
    return o
M=[('A','両輪',A),('B','循環',B),('C','つなぐ',C),('D','バリューチェーン',D),('E','持つ力',E),('F','前へ',F)]
pages=[]
for n,pn,c1,c2 in PAIRS:
    for mk,mn,f in M: pages.append((mk,n,page2(f(c1,c2),c1)))
open('cover12.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS+'</style>'+''.join(p for *_,p in pages))
