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
# 1 連なる半円：つなぐ（バトンを渡すように、形を変えながら次へ）
def P1(c1,c2):
    o=f'<rect x="0" y="236" width="530" height="520" fill="{c1}"/>'
    x=40; R=210; cy=496; ds=[]
    for k in range(6):
        ds.append(f'<path d="M{x},{cy-R} A{R},{R} 0 0 1 {x},{cy+R}Z" fill="{c2}" stroke="{c1}" stroke-width="5"/>')
        x+=R*0.55; R*=0.8
    o+=''.join(reversed(ds))
    return o
# 2 傾いた四角と円：持つ力（資産が資源を抱え、そこから新しい価値＝点が生まれる）
def P2(c1,c2):
    cx,cy,s=330,520,380
    o=f'<g transform="rotate(-11 {cx} {cy})"><rect x="{cx-s/2}" y="{cy-s/2}" width="{s}" height="{s}" fill="{c2}"/></g>'
    o+=f'<circle cx="{cx+38}" cy="{cy+66}" r="112" fill="#fff"/>'
    o+=f'<circle cx="{cx-150}" cy="{cy+182}" r="22" fill="{c1}"/>'
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
def P5(c1,c2):
    o=''; cx=300
    st=[(200,104),(158,84),(112,62)]; y=760; cs=[]
    for rx,ry in st:
        cy=y-ry; cs.append((cy,rx,ry)); y=cy-ry+22
    for k,(cy,rx,ry) in enumerate(cs):
        if k>0:
            pcy,prx,pry=cs[k-1]; o+=f'<ellipse cx="{cx}" cy="{pcy-pry+16}" rx="{rx*0.92:.0f}" ry="18" fill="{c2}"/>'
        d=f'M{cx-rx},{cy} A{rx},{ry} 0 1 0 {cx+rx},{cy} A{rx},{ry} 0 1 0 {cx-rx},{cy}Z'
        cd,cu=clip(d); o+=cd+f'<path d="{d}" fill="#fff"/><g clip-path="{cu}">'
        yy=cy-ry
        while yy<cy+ry: o+=f'<line x1="{cx-rx}" y1="{yy:.1f}" x2="{cx+rx}" y2="{yy:.1f}" stroke="{c1}" stroke-width="2.4"/>'; yy+=4.8
        o+='</g>'
    return o
M=[('1','連なる半円','つなぐ力',P1),('2','傾いた四角と円','持つ力',P2),('3','四分円の同心線','届ける力',P3),('4','二つのU','両輪',P4),('5','積み石','積み重ねる力',P5)]
PAIRS=[('a',CU,GP),('b',VR,GP)]
pages=[]
for m,*_,f in M:
    for pa,c1,c2 in PAIRS: pages.append(page3(f(c1,c2),c1))
open('cover13.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS+'</style>'+''.join(pages))
