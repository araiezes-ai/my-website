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
def RIGHT(): # 推進：途切れない3本。上から短・中・長、いちばん下の1本だけが右端へ突き抜ける
    o='<g transform="rotate(-17 300 600)">'
    rows=[(530,466,370),(616,552,520),(702,638,1000)]   # (下端y, 上端y, 先端x)
    for y0,y1,end in rows:
        o+=piece(-400,y0,y1,end+400,'bot')
    o+=f'<path d="{para(250,740,420,84)}" fill="{PANE}" opacity=".40"/>'
    o+=f'<path d="{para(20,660,380,110)}" fill="{PANE2}" opacity=".42"/>'
    return o+'</g>'
P=[(front(RIGHT(),MAIN),'L3_推進_長さ違い')]
open('cover26.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS2+'</style>'+''.join(p for p,_ in P))
import json; json.dump([n for _,n in P],open('cover26_names.json','w'),ensure_ascii=False)
