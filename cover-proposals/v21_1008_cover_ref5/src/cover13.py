# 表紙 v13：参考ポスター5型（青丸）をベースに、白地＋2色・意味づけ
import math
exec(open('cover11.py').read().split('pages=[]')[0].split('UID=[0]')[0])
CU='#B4693E'; VR='#D24A2B'; GP='#2E3136'; W_='#ffffff'
def page3(svg,c1):
    t=(f'<div class="a k1" style="left:48px;top:58px">MITSUBISHI CORPORATION</div>'
       f'<div class="a" style="left:48px;top:84px;width:3px;height:60px;background:{c1}"></div>'
       f'<div class="a ttl" style="left:62px;top:82px;font-size:24px">MINERAL<br>RESOURCES</div>'
       f'<div class="a k2" style="left:62px;top:156px">CORPORATE PROFILE</div>')
    foot='<rect x="0" y="784" width="595" height="58" fill="#fff"/><line x1="48" y1="784" x2="547" y2="784" stroke="#9aa0a6" stroke-width=".5"/>'+logo(400,806)
    return f'<div class="pg"><svg class="a" style="left:0;top:0" width="595" height="842" viewBox="0 0 595 842">{svg}{foot}</svg>{t}</div>'
CID=[0]
def clip(d):
    CID[0]+=1; return f'<clipPath id="k{CID[0]}"><path d="{d}"/></clipPath>', f'url(#k{CID[0]})'
# 1 連なる半円：つなぐ力（白地版。最後の一つだけ色）
def P1(c1,c2):
    o=''; x=48; R=200; cy=500; ds=[]
    for k in range(6):
        col=c1 if k==5 else c2
        ds.append(f'<path d="M{x},{cy-R} A{R},{R} 0 0 1 {x},{cy+R}Z" fill="{col}" stroke="#fff" stroke-width="4"/>')
        x+=R*0.55; R*=0.8
    return o+''.join(reversed(ds))
# 2 器と資源：持つ力（器に半分沈んだ円。下半分＝いま持つ資源、上半分の線＝これから持つ資源）
def P2(c1,c2):
    top=572; cx=300; r=104
    o=f'<rect x="48" y="{top}" width="560" height="212" fill="{c2}"/>'
    o+=f'<path d="M{cx-r},{top} A{r},{r} 0 0 0 {cx+r},{top}Z" fill="{c1}"/>'
    o+=f'<path d="M{cx-r},{top} A{r},{r} 0 0 1 {cx+r},{top}" fill="none" stroke="{c2}" stroke-width="2.4"/>'
    return o
# 3 四分円の同心線：届ける力（一つの源から、世界へ広がる供給）
def P3(c1,c2):
    ox,oy=548,770; o=''
    for k in range(30):
        r=70+k*15.2
        o+=f'<path d="M{ox-r:.1f},{oy} A{r:.1f},{r:.1f} 0 0 1 {ox},{oy-r:.1f}" fill="none" stroke="{c2}" stroke-width="6.6"/>'
    o+=f'<path d="M{ox-52},{oy} A52,52 0 0 1 {ox},{oy-52} L{ox},{oy}Z" fill="{c1}"/>'
    o+=f'<rect x="0" y="0" width="595" height="232" fill="#fff"/>'
    return o
# 4 二つのU：両輪（投資とトレーディングが、一本の線で結ばれている）
def P4(c1,c2):
    r=s=96; cx1=105; cm=cx1+r+s; cx2=cm+s+r; Y1=600; Y0=440; top=236; o=''
    for k in range(-13,10):
        d=k*6.6
        a=r+d; b=s-d
        if a<=2 or b<=2: continue
        p=(f'M{cx1-a:.1f},{top} L{cx1-a:.1f},{Y1} A{a:.1f},{a:.1f} 0 0 0 {cx1+a:.1f},{Y1} L{cx1+a:.1f},{Y0} '
           f'A{b:.1f},{b:.1f} 0 0 1 {cm+b:.1f},{Y0} L{cm+b:.1f},{Y1} A{a:.1f},{a:.1f} 0 0 0 {cx2+a:.1f},{Y1} L{cx2+a:.1f},{top}')
        o+=f'<path d="{p}" fill="none" stroke="{c2}" stroke-width="2.8"/>'
    o+=f'<circle cx="{cm}" cy="{Y0+80}" r="20" fill="{c1}"/>'
    return o
# 5 積み石：積み重ねる力（長期の資産を、一段ずつ積み上げてきた）
def supel(cx,cy,rx,ry,n=2.7,N=120):
    pts=[]
    for t in range(N):
        a=2*math.pi*t/N; c,sn=math.cos(a),math.sin(a)
        pts.append((cx+rx*math.copysign(abs(c)**(2/n),c), cy+ry*math.copysign(abs(sn)**(2/n),sn)))
    return 'M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'Z'
def P5(c1,c2):  # 積み重ねる力：経線状の細線で描く三つの石。最上段＝次の一段だけ色を変える
    cx=298; o=''
    def hw(dy,rx,ry,n=2.2):
        t=abs(dy)/ry
        return 0 if t>=1 else rx*(1-t**n)**(1/n)
    def stone(cy,rx,ry,cut,col,N=96):
        out=''; y0=cy-ry*0.93; y1=min(cy+ry*0.93,cut)
        for k in range(N+1):
            ph=-math.pi/2+math.pi*k/N; sv=math.sin(ph)
            pts=[]; steps=60
            for q in range(steps+1):
                y=y0+(y1-y0)*q/steps; pts.append((cx+sv*hw(y-cy,rx,ry),y))
            out+='<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+f'" fill="none" stroke="{col}" stroke-width=".55"/>'
        return out
    def bowl(top,w,d):
        pts=[(cx-w,top)]+[(cx+w*math.cos(a),top+d*math.sin(a)) for a in [math.pi-math.pi*q/60 for q in range(61)]]
        pts=[(cx-w,top)]+[(cx-w*math.cos(math.pi*q/60) ,top+d*math.sin(math.pi*q/60)**0.6) for q in range(61)]
        return '<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+f'Z" fill="{c2}"/>'
    o+=stone(649,214,122,9999,c2)
    o+=bowl(536,148,44)
    o+=stone(481,168,100,536,c2)
    o+=bowl(390,106,36)
    o+=stone(339,120,92,390,c1)
    return o
M=[('1','連なる半円','つなぐ力',P1),('2','器と資源','持つ力',P2),('3','四分円の同心線','届ける力',P3),('4','二つのU','両輪',P4),('5','積み石','積み重ねる力',P5)]
PAIRS=[('a',CU,GP),('b',VR,GP)]
pages=[]
for m,*_,f in M:
    for pa,c1,c2 in PAIRS: pages.append(page3(f(c1,c2),c1))
open('cover13.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS+'</style>'+''.join(pages))
