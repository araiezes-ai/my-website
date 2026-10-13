# 表紙 v29：L1フラット 赤／グラファイト。帯の鉄鋼感アップ（白を使わず同色相のハイライト）、影はニュートラルなグレー
import math, random
exec(open('cover27.py').read().split('def band(')[0])
def grain(d,ang,seed,hl,op=.35):
    """同色相のハイライトと黒の極細線で、鋼材のヘアライン"""
    UID[0]+=1; cid=f'gr{UID[0]}'; random.seed(seed)
    o=f'<clipPath id="{cid}"><path d="{d}"/></clipPath><g clip-path="url(#{cid})"><g transform="rotate({ang} 300 420)">'
    y=-500
    while y<1400:
        a=random.random()**2*op; col=hl if random.random()<.5 else '#000'
        o+=f'<line x1="-500" y1="{y:.1f}" x2="1200" y2="{y:.1f}" stroke="{col}" stroke-width="{random.choice((.3,.45,.6))}" opacity="{a:.3f}"/>'
        y+=random.uniform(.9,2.2)
    return o+'</g></g>'
def band(xb,y0,y1,W):  # F1と同じ「長さ方向に光が流れる」鏡面の金属
    xt=xb+(y0-y1)*K; d=f'M{xb},{y0} L{xb+W},{y0} L{xt+W:.1f},{y1} L{xt:.1f},{y1}Z'
    CID[0]+=1; g=f'mg{CID[0]}'; c=f'bc{CID[0]}'
    o='<defs>'+mgrad(g,(DARK,MAIN,HL),0,842,595,0)+'</defs>'
    o+=f'<clipPath id="{c}"><path d="{d}"/></clipPath><path d="{d}" fill="url(#{g})"/><g clip-path="url(#{c})">'
    o+=f'<path d="{para(xat(xb,y0,y1+20),y1+20,y1,W)}" fill="{DARK}" opacity=".85"/>'
    o+=grain(d,-56,400+CID[0],HL,op=.12)+'</g>'
    return o
def UPS():
    o=''
    bands=[(-56,540),(56,350),(168,-80)]
    # 影：ニュートラルなグレーが白へ溶ける
    o+=('<defs><linearGradient id="shd" gradientUnits="userSpaceOnUse" x1="0" y1="900" x2="0" y2="420">'
        f'<stop offset="0" stop-color="{SH}"/><stop offset="1" stop-color="{SH}" stop-opacity="0"/></linearGradient></defs>')
    o+=f'<path d="{para(-150,900,420,70)}" fill="url(#shd)"/>'
    for xb,y1 in bands: o+=band(xb,900,y1,96)
    CID[0]+=1; uc=f'uc{CID[0]}'
    o+=f'<clipPath id="{uc}">'+''.join(f'<path d="{para(xb,900,y1,96)}"/>' for xb,y1 in bands)+'</clipPath>'
    return o
COLS=[('赤','#a3122a','#3e040d','#e8485c','#7d0c1f','#1f252c',.36,'multiply','#c9ced4'),
      ('グラファイト','#5f6c7a','#1d242c','#e3e8ee','#454e58','#6f8aa3',.45,'screen','#c9ced4')]
P=[]
for nm,m,dk,hl,mid,pa,po,pb,sh in COLS:
    MAIN,DARK,HL,MID,PA,PA_OP,PA_BL,SH=m,dk,hl,mid,pa,po,pb,sh
    P.append((front(UPS(),m),f'L1_上昇_フラット_{nm}_鏡面'))
open('cover30.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS2+'</style>'+''.join(p for p,_ in P))
import json; json.dump([n for _,n in P],open('cover30_names.json','w'),ensure_ascii=False)
