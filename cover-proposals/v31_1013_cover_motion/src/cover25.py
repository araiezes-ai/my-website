# 表紙 v25：参考画像の幾何学感と方向感（帯が分断され、ずれ、濃い縁と半透明の面が重なる）を白地・3本・はっきりした赤で
import math
exec(open('cover20.py').read().split('P=[(front(G1()')[0])
K=1/math.tan(math.radians(56))
MAIN='#a01d30'; DARK='#5e0a14'; PANE='#ffffff'; PANE2='#d9dcdf'
def para(xb,y0,y1,W):
    xt=xb+(y0-y1)*K
    return f'M{xb:.1f},{y0} L{xb+W:.1f},{y0} L{xt+W:.1f},{y1} L{xt:.1f},{y1}Z'
def xat(xb,y0,y): return xb+(y0-y)*K
def piece(xb,y0,y1,W,cap='top'):
    o=f'<path d="{para(xb,y0,y1,W)}" fill="{MAIN}"/>'
    o+=f'<path d="{para(xb,y0,y1,13)}" fill="{DARK}"/>'                     # 片側の濃い縁
    if cap=='top':  o+=f'<path d="{para(xat(xb,y0,y1+20),y1+20,y1,W)}" fill="{DARK}"/>'   # 端の濃い帯（厚み・折れ）
    if cap=='bot':  o+=f'<path d="{para(xb,y0,y0-16,W)}" fill="{DARK}"/>'
    return o
def UPM():   # 上昇：3本の帯がそれぞれ途中で切れ、ずれながら上へ抜ける
    o=''
    for xb,ycut,shift in [(-6,560,26),(124,430,-22),(254,620,30)]:
        W=96
        o+=piece(xb,900,ycut,W,'top')
        xb2=xat(xb,900,ycut-18)+shift
        o+=piece(xb2,ycut-18,-60,W,'none')
    o+=f'<path d="{para(150,760,330,74)}" fill="{PANE}" opacity=".42"/>'
    o+=f'<path d="{para(300,560,240,60)}" fill="{PANE}" opacity=".38"/>'
    o+=f'<path d="{para(-150,900,420,70)}" fill="{PANE2}" opacity=".45"/>'
    return o
def RIGHT(): # 推進：3段の帯。先頭は段ごとに前へずれ（階段状に前進）、後ろに短い「残像」の帯。右端へ抜ける
    o='<g transform="rotate(-17 300 600)">'
    rows=[(530,466,150),(616,552,236),(702,638,322)]
    for k,(y0,y1,lead) in enumerate(rows):
        o+=piece(lead,y0,y1,800,'bot')
        tw=lead-28+320-k*60
        o+=piece(lead-28-tw,y0,y1,tw,'bot')
    o+=f'<path d="{para(300,740,420,84)}" fill="{PANE}" opacity=".40"/>'
    o+=f'<path d="{para(60,660,380,110)}" fill="{PANE2}" opacity=".42"/>'
    return o+'</g>'
P=[(front(UPM(),MAIN),'L1_上昇_分断とずれ'),(front(RIGHT(),MAIN),'L2_推進_左から右へ')]
open('cover25.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS2+'</style>'+''.join(p for p,_ in P))
import json; json.dump([n for _,n in P],open('cover25_names.json','w'),ensure_ascii=False)
