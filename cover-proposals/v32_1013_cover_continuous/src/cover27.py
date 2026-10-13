# 表紙 v27：途切れない3本・長さ違い。L1（上昇）／L3（推進）× 先端 フラット／尖り
import math
exec(open('cover25.py').read().split('def UPM')[0])
CID=[0]
def band(xb,y0,y1,W,tip,orient,cap):
    """orient='up'：上端が先端／'right'：右辺が先端。tip=True で先端を尖らせる"""
    xt=xb+(y0-y1)*K
    BL,BR,TR,TL=(xb,y0),(xb+W,y0),(xt+W,y1),(xt,y1)
    if orient=='up':
        if tip:
            L=math.hypot(K,1); u=(K/L,-1/L); n=(1/L,K/L)
            c=((TL[0]+TR[0])/2,y1); w=W*math.sin(math.radians(56)); h=w*1.35
            pL=(c[0]-n[0]*w/2,c[1]-n[1]*w/2); pR=(c[0]+n[0]*w/2,c[1]+n[1]*w/2)
            pts=[BL,BR,pR,(c[0]+u[0]*h,c[1]+u[1]*h),pL]   # 帯の軸に対して左右対称な先端
        else: pts=[BL,BR,TR,TL]
    else:
        if tip:
            m=((TR[0]+BR[0])/2,(y0+y1)/2); h=(y0-y1)*0.9
            pts=[BL,BR,(m[0]+h,m[1]),TR,TL]
        else: pts=[BL,BR,TR,TL]
    d='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'Z'
    CID[0]+=1; c=f'bc{CID[0]}'
    g=f'sh{CID[0]}'
    o=(f'<defs><linearGradient id="{g}" gradientUnits="userSpaceOnUse" x1="0" y1="900" x2="595" y2="100">'
       '<stop offset="0" stop-color="#000" stop-opacity=".18"/><stop offset=".42" stop-color="#fff" stop-opacity=".0"/>'
       '<stop offset=".55" stop-color="#fff" stop-opacity=".22"/><stop offset=".68" stop-color="#fff" stop-opacity="0"/>'
       '<stop offset="1" stop-color="#000" stop-opacity=".12"/></linearGradient></defs>')
    o+=f'<clipPath id="{c}"><path d="{d}"/></clipPath><path d="{d}" fill="{MAIN}"/><g clip-path="url(#{c})">'
    o+=f'<path d="{para(xb,y0,y1-200,13)}" fill="{DARK}"/>'                       # 片側の濃い縁
    if cap=='bot': o+=f'<path d="{para(xb,y0,y0-16,W+400)}" fill="{DARK}"/>'      # 下側の厚み
    if cap=='top' and not tip: o+=f'<path d="{para(xat(xb,y0,y1+20),y1+20,y1,W)}" fill="{DARK}"/>'
    o+=f'<rect x="-200" y="-200" width="1000" height="1200" fill="url(#{g})"/>'     # 鋼板の光沢
    ang=-56 if orient=='up' else 0
    o+=brushed(d,ang,300+CID[0],bbox=(-400,-400,1000,1300),op=.30)               # ヘアラインの筋目
    return o+'</g>'
def UPC(tip):   # 上昇：左から短・中・長、右の1本だけが上端へ突き抜ける
    o=''
    for xb,y1 in [(-56,540),(56,350),(168,-80)]:
        o+=band(xb,900,y1,96,tip,'up','top')
    o+=f'<path d="{para(70,760,330,74)}" fill="{PANE}" opacity=".42"/>'
    o+=f'<path d="{para(-150,900,420,70)}" fill="{PANE2}" opacity=".45"/>'
    return o
def RIGHTC(tip):  # 推進：上から短・中・長、下の1本だけが右端へ突き抜ける
    o='<g transform="rotate(-17 300 600)">'
    for y0,y1,end in [(530,466,370),(616,552,520),(702,638,1000)]:
        o+=band(-400,y0,y1,end+400,tip,'right','bot')
    o+=f'<path d="{para(250,740,420,84)}" fill="{PANE}" opacity=".40"/>'
    o+=f'<path d="{para(20,660,380,110)}" fill="{PANE2}" opacity=".42"/>'
    return o+'</g>'
P=[(front(UPC(False),MAIN),'L1_上昇_長さ違い_フラット'),(front(UPC(True),MAIN),'L1_上昇_長さ違い_尖り'),
   (front(RIGHTC(False),MAIN),'L3_推進_長さ違い_フラット'),(front(RIGHTC(True),MAIN),'L3_推進_長さ違い_尖り')]
open('cover27.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS2+'</style>'+''.join(p for p,_ in P))
import json; json.dump([n for _,n in P],open('cover27_names.json','w'),ensure_ascii=False)
