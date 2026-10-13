# 表紙 v19（表紙のみ）：会社案内2026の「赤い山形3本」の強さを、鉄鋼・金属の色で。3本／上昇・推進／金属の光沢
import math
exec(open('cover17.py').read().split('def FOLD')[0])
STEEL=('#1d242c','#5f6c7a','#e3e8ee'); COPPER=('#6e3519','#c27a4a','#efc6a2')
def mgrad(id_,c,x1,y1,x2,y2):  # 会社案内の赤のような、明暗が流れる金属グラデーション
    d,m,l=c
    return (f'<linearGradient id="{id_}" gradientUnits="userSpaceOnUse" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">'
            f'<stop offset="0" stop-color="{d}"/><stop offset=".22" stop-color="{m}"/><stop offset=".38" stop-color="{l}"/>'
            f'<stop offset=".52" stop-color="{m}"/><stop offset=".7" stop-color="{d}"/><stop offset=".86" stop-color="{m}"/><stop offset="1" stop-color="{l}"/></linearGradient>')
def offset_poly(pts,s):
    def off(p0,p1):
        dx,dy=p1[0]-p0[0],p1[1]-p0[1]; L=math.hypot(dx,dy); return (-dy/L*s,dx/L*s)
    def isect(a,da,b,db):
        den=da[0]*db[1]-da[1]*db[0]; t=((b[0]-a[0])*db[1]-(b[1]-a[1])*db[0])/den; return (a[0]+t*da[0],a[1]+t*da[1])
    segs=[]
    for k in range(len(pts)-1):
        o=off(pts[k],pts[k+1]); segs.append(((pts[k][0]+o[0],pts[k][1]+o[1]),(pts[k+1][0]-pts[k][0],pts[k+1][1]-pts[k][1])))
    P=[segs[0][0]]+[isect(segs[k][0],segs[k][1],segs[k+1][0],segs[k+1][1]) for k in range(len(segs)-1)]
    P.append((segs[-1][0][0]+segs[-1][1][0],segs[-1][0][1]+segs[-1][1][1])); return P
def lines3(center_pts,c,W=20,gap=22,gid='g'):
    o=f'<defs>{mgrad(gid,c,0,842,595,0)}</defs>'
    for k in (-1,0,1):
        pl=offset_poly(center_pts,k*(W+gap))
        quads,U,D=miter_quads(pl,W)
        outline=U+D[::-1]
        d='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in outline)+'Z'
        o+=f'<path d="{d}" fill="url(#{gid})"/>'+brushed(d,0,90+k,bbox=(-300,-300,900,1100),op=.10)
    return o
def UP(c,gid):    # 上を向く山形3本：下端で断ち落とし、頂点が上へ
    return lines3([(-200,1140),(352,452),(904,1140)],c,gid=gid)
def RISE(c,gid):  # 前へ進み、一点で上へ向きを変える3本：左端と右上で断ち落とし
    return lines3([(-40,676),(250,676),(560,140),(640,1)],c,gid=gid)
def front(svg,acc):
    foot=('<rect x="0" y="772" width="595" height="70" fill="#fff"/><line x1="48" y1="784" x2="547" y2="784" stroke="#9aa0a6" stroke-width=".5"/>'+logo(297.5-66,808))
    bg=('<defs><linearGradient id="bgf" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff"/><stop offset=".6" stop-color="#fff"/><stop offset="1" stop-color="#eceef0"/></linearGradient></defs><rect width="595" height="842" fill="url(#bgf)"/>')
    return f'<div class="pg"><svg class="a" style="left:0;top:0" width="595" height="842" viewBox="0 0 595 842">{bg}{svg}{foot}</svg>{head("JO",acc)}</div>'
P=[(front(UP(STEEL,'u1'),STEEL[1]),'E1_UP_スチール'),(front(UP(COPPER,'u2'),COPPER[1]),'E2_UP_カッパー'),
   (front(RISE(STEEL,'r1'),STEEL[1]),'F1_RISE_スチール'),(front(RISE(COPPER,'r2'),COPPER[1]),'F2_RISE_カッパー')]
open('cover19.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS2+'</style>'+''.join(p for p,_ in P))
import json; json.dump([n for _,n in P],open('cover19_names.json','w'),ensure_ascii=False)
