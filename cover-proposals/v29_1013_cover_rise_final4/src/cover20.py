# 表紙 v20：F（前へ、そして上へ）を会社案内2026から差別化
#  1) 3本の役割を変える（太さ違い／折れ位置ずらし） 2) 1本だけカッパー 3) つやではなくヘアラインのマットな金属
import math
exec(open('cover19.py').read().split('P=[(front(')[0])
STEEL_M=('#3a434d','#6f7b88','#b9c1ca'); COPPER_M=('#7a3d1f','#b8724a','#dcae8c')
def mattegrad(id_,c,x1,y1,x2,y2):
    d,m,l=c
    return (f'<linearGradient id="{id_}" gradientUnits="userSpaceOnUse" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">'
            f'<stop offset="0" stop-color="{d}"/><stop offset=".45" stop-color="{m}"/><stop offset=".62" stop-color="{l}"/><stop offset="1" stop-color="{m}"/></linearGradient>')
def bandpoly(pl,W):
    quads,U,D=miter_quads(pl,W); out=U+D[::-1]
    return 'M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in out)+'Z'
def G1():  # 太・中・細。細い一本（新しい力）だけカッパーで、一番先へ
    C=[(-40,676),(250,676),(560,140),(640,1)]
    spec=[(-27,7,COPPER_M),(0,14,STEEL_M),(37,28,STEEL_M)]  # (オフセット, 線幅, 色)
    o='<defs>'+''.join(mattegrad(f'm{k}',c,0,842,595,0) for k,(_,_,c) in enumerate(spec))+'</defs>'
    for k,(s,w,c) in enumerate(spec):
        d=bandpoly(offset_poly(C,s),w)
        o+=f'<path d="{d}" fill="url(#m{k})"/>'+brushed(d,0,120+k,bbox=(-300,-300,900,1100),op=.32)
    return o
def G2():  # 折れ位置をずらした3本。手前から順に上へ向きを変える＝段階的に上昇。中央の一本だけカッパー
    dx,dy=0.5,-0.866; o='<defs>'
    spec=[((168,632),16,STEEL_M),((262,676),16,COPPER_M),((356,720),16,STEEL_M)]
    o+=''.join(mattegrad(f'n{k}',c,0,842,595,0) for k,(_,_,c) in enumerate(spec))+'</defs>'
    for k,((x,y),w,c) in enumerate(spec):
        t=(y+40)/(-dy); pl=[(-40,y),(x,y),(x+dx*t,y+dy*t)]
        d=bandpoly(pl,w)
        o+=f'<path d="{d}" fill="url(#n{k})"/>'+brushed(d,0,130+k,bbox=(-300,-300,900,1100),op=.32)
    return o
P=[(front(G1(),COPPER_M[1]),'G1_RISE_太さ違い'),(front(G2(),COPPER_M[1]),'G2_RISE_折れ位置ずらし')]
open('cover20.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS2+'</style>'+''.join(p for p,_ in P))
import json; json.dump([n for _,n in P],open('cover20_names.json','w'),ensure_ascii=False)
