# 表紙 v14：細線の二つの球（両輪）／向きを変える流れ（カッパー）
import math
exec(open('cover13.py').read().split('# 1 連なる半円')[0])
def sph_v(cx,cy,r,col,N=78,w=.6):  # 縦の経線：深さ＝事業投資
    o=''
    for k in range(1,N):
        sv=math.sin(-math.pi/2+math.pi*k/N)
        pts=[(cx+sv*r*math.cos(t),cy+r*math.sin(t)) for t in [-math.pi/2+math.pi*q/60 for q in range(61)]]
        o+='<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+f'" fill="none" stroke="{col}" stroke-width="{w}"/>'
    return o
def sph_h(cx,cy,r,col,N=78,w=.6):  # 横の緯線：広がり＝トレーディング
    o=''
    for k in range(1,N):
        sv=math.sin(-math.pi/2+math.pi*k/N); y=cy+sv*r; hw=r*math.sqrt(1-sv*sv)
        o+=f'<line x1="{cx-hw:.1f}" y1="{y:.1f}" x2="{cx+hw:.1f}" y2="{y:.1f}" stroke="{col}" stroke-width="{w}"/>'
    return o
def W1(c1,c2):  # 両輪 a：縦の球（グラファイト）と横の球（カッパー）が重なる
    return sph_v(218,566,152,c2)+sph_h(378,566,152,c1)
def W2(c1,c2):  # 両輪 b：二つともグラファイト、重なった部分だけカッパー
    a,b=(218,566),(378,566); r=152
    o=sph_v(*a,r,c2)+sph_h(*b,r,c2)
    o+=f'<clipPath id="ov"><circle cx="{b[0]}" cy="{b[1]}" r="{r}"/></clipPath><clipPath id="ov2"><circle cx="{a[0]}" cy="{a[1]}" r="{r}"/></clipPath>'
    o+=f'<g clip-path="url(#ov)"><g clip-path="url(#ov2)"><rect x="0" y="0" width="595" height="842" fill="#fff"/>'+sph_v(*a,r,c1)+sph_h(*b,r,c1)+'</g></g>'
    return o
def F(c1,c2,grad):  # 向きを変える流れ
    Cx,Cy=292,452; o=''
    if grad:
        o+=f'<defs><linearGradient id="fg" gradientUnits="userSpaceOnUse" x1="40" y1="760" x2="560" y2="200"><stop offset="0" stop-color="{c2}"/><stop offset=".45" stop-color="{c2}"/><stop offset=".8" stop-color="{c1}"/></linearGradient></defs>'
        col='url(#fg)'
    else: col=c1
    for i in range(24):
        r=10+i*12
        o+=f'<path d="M-10,{Cy+r} L{Cx},{Cy+r} A{r},{r} 0 0 0 {Cx+r},{Cy} L{Cx+r},-10" fill="none" stroke="{col}" stroke-width="5"/>'
    return o
pages=[page3(W1(CU,GP),CU),page3(W2(CU,GP),CU),page3(F(CU,GP,False),CU),page3(F(CU,GP,True),CU)]
open('cover14.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS+'</style>'+''.join(pages))
