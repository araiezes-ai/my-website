# 表紙 v21：RISEの帯を「球の線画」と同じ細線の束で描く2案
import math
exec(open('cover20.py').read().split('P=[(front(G1()')[0])
GPH='#2E3136'; CUL='#B4693E'
C=[(-40,676),(250,676),(560,140),(640,1)]
def bundle(center,s0,W,n,stroke):
    o=''
    for i in range(n):
        s=s0-W/2+W*i/(n-1)
        pl=offset_poly(center,s)
        o+='<polyline points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pl)+f'" fill="none" stroke="{stroke}" stroke-width=".6"/>'
    return o
def H1():  # F1の構成（同じ幅の3本）を細線で。横はグラファイト、上がるほどカッパーへ
    g=('<defs><linearGradient id="hg" gradientUnits="userSpaceOnUse" x1="120" y1="700" x2="560" y2="120">'
       f'<stop offset="0" stop-color="{GPH}"/><stop offset=".45" stop-color="{GPH}"/><stop offset="1" stop-color="{CUL}"/></linearGradient></defs>')
    return g+''.join(bundle(C,k*42,20,11,'url(#hg)') for k in (-1,0,1))
def H2():  # G1の構成（太・中・細）を細線で。太い束ほど線が多い。細い1本だけカッパー
    spec=[(-27,9,6,CUL),(0,14,7,GPH),(37,28,14,GPH)]
    return ''.join(bundle(C,s,w,n,col) for s,w,n,col in spec)
def frontCG(svg,acc):
    foot=('<rect x="0" y="772" width="595" height="70" fill="#fff"/><line x1="48" y1="784" x2="547" y2="784" stroke="#9aa0a6" stroke-width=".5"/>'+logo(297.5-66,808))
    return f'<div class="pg"><svg class="a" style="left:0;top:0" width="595" height="842" viewBox="0 0 595 842"><rect width="595" height="842" fill="#fff"/>{svg}{foot}</svg>{head("CG",acc)}</div>'
P=[(frontCG(H1(),CUL),'H1_RISE線画_同じ幅'),(frontCG(H2(),CUL),'H2_RISE線画_太さ違い')]
open('cover21.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS2+'</style>'+''.join(p for p,_ in P))
import json; json.dump([n for _,n in P],open('cover21_names.json','w'),ensure_ascii=False)
