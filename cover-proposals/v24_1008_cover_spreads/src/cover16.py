# 表紙＋裏表紙（見開きでつながる）5案：A-b両輪の球／A-2ネイビー／A-2カッパー／C-2三本の帯／届ける力
import math
exec(open('cover15.py').read().split('pages=[(pg(')[0])
WB=(-700,-700,1900,1600)
def brushedW(d,ang,seed,op=.22): return brushed(d,ang,seed,bbox=WB,op=op)
ADDR='Mineral Resources Group　|　2-3-1 Marunouchi, Chiyoda-ku, Tokyo 100-8086, Japan　|　www.mitsubishicorp.com'
def spread(svg,font,acc,bg=False):
    b=('<defs><linearGradient id="bgs" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff"/><stop offset=".55" stop-color="#fff"/><stop offset="1" stop-color="#eceef0"/></linearGradient></defs><rect width="1190" height="842" fill="url(#bgs)"/>') if bg else '<rect width="1190" height="842" fill="#fff"/>'
    foot=('<rect x="0" y="772" width="1190" height="70" fill="#fff"/>'
          '<line x1="48" y1="784" x2="547" y2="784" stroke="#9aa0a6" stroke-width=".5"/><line x1="643" y1="784" x2="1142" y2="784" stroke="#9aa0a6" stroke-width=".5"/>'
          +logo(595+297.5-66,808)+logo(297.5-66,808))
    ff='JO' if font=='JO' else 'CG'; fz='7px' if font=='JO' else '8px'
    back=f'<div class="a" style="left:0;width:595px;text-align:center;top:822px;font:400 {fz} {ff};letter-spacing:1.2px;color:#6b7178;white-space:nowrap">{ADDR}</div>'
    return (f'<div class="pg" style="width:1190px"><svg class="a" style="left:0;top:0" width="1190" height="842" viewBox="0 0 1190 842">{b}{svg}{foot}</svg>'
            f'<div class="a" style="left:595px;top:0;width:595px;height:842px">{head(font,acc)}</div>{back}</div>')
# ---- A-b 両輪の球：縦の球は背（ノド）にまたがり、裏表紙から表紙へ続く
def SPH2(c1,c2):  # 表紙中央に小さく二つの球。裏表紙の中央にはカッパーの○一つ（両輪がかみ合って生まれた価値）
    r=82; cy=488; a=(595+297.5-59,cy); b=(595+297.5+59,cy)
    o=sph_v(*a,r,c2,N=54)+sph_h(*b,r,c2,N=54)
    o+=f'<clipPath id="ov"><circle cx="{b[0]}" cy="{b[1]}" r="{r}"/></clipPath><clipPath id="ov2"><circle cx="{a[0]}" cy="{a[1]}" r="{r}"/></clipPath>'
    o+=f'<g clip-path="url(#ov)"><g clip-path="url(#ov2)"><rect x="0" y="0" width="1190" height="842" fill="#fff"/>'+sph_v(*a,r,c1,N=54)+sph_h(*b,r,c1,N=54)+'</g></g>'
    o+=sph_v(297.5,cy,22,c1,N=16,w=.5)+sph_h(297.5,cy,22,c1,N=16,w=.5)   # 裏表紙：縦横の線が編まれたカッパーの球
    return o
# ---- A-2 二本の帯：裏表紙では一本（B）だけが流れ、表紙で二本目が加わり重なる
def BANDS2(cw):
    T=CW[cw]['t']; o='<defs>'; gs=[]
    for c in T[:2]:
        i,g=metal(c,-60); o+=g; gs.append(i)
    o+='</defs>'
    dA,aA=band((535,905),(1275,470),118)
    dB,aB=band((-80,719),(1275,545),118)
    o+=f'<path d="{dB}" fill="url(#{gs[1]})" opacity=".78"/>'+brushedW(dB,aB,1)
    o+=f'<path d="{dA}" fill="url(#{gs[0]})" opacity=".82" style="mix-blend-mode:multiply"/>'+brushedW(dA,aA,2)
    return o
# ---- C-2 三本の帯：金属の二本は表紙だけ。赤い一本が裏表紙から背をまたいで表紙へ通る
def BARS3S():
    T=CW['2']['t']; o='<defs>'; gs=[]
    for c in (T[0],T[1]):
        i,g=metal(c,0); o+=g; gs.append(i)
    o+='</defs>'; y=566
    for x,h,g in [(765,40,gs[0]),(691,40,gs[1])]:
        d=f'M{x},{y} L1200,{y} L1200,{y+h} L{x},{y+h}Z'
        o+=f'<path d="{d}" fill="url(#{g})"/>'+brushedW(d,0,30+y,op=.28); y+=h+14
    o+=f'<rect x="300" y="{y+2}" width="900" height="7" fill="{RED}"/>'
    return o
# ---- 届ける力：表紙右下の一点（源）から、線が裏表紙まで広がる。外へ行くほど細く淡く
def ARCS(c1,c2):
    cx,cy=700,512; o=""; N=25
    for k in range(N):
        r=34+k*8.2; t=k/(N-1)
        w=2.0-1.45*t; op=1-.55*t
        o+=f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="none" stroke="{c2}" stroke-width="{w:.2f}" opacity="{op:.2f}"/>'
    o+=f'<circle cx="{cx}" cy="{cy}" r="22" fill="{c1}"/>'
    return o
def RIP(cx,cy,r0,pitch,N,c1,c2,dot):
    o=''
    for k in range(N):
        r=r0+k*pitch; t=k/(N-1)
        o+=f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="none" stroke="{c2}" stroke-width="{2.0-1.45*t:.2f}" opacity="{1-.55*t:.2f}"/>'
    return o+f'<circle cx="{cx}" cy="{cy}" r="{dot}" fill="{c1}"/>'
def ARCS_A(c1,c2):  # 中心を背の下端に。表紙・裏表紙それぞれに1/4ずつ、見開きで半円
    return '<clipPath id="ha"><rect x="0" y="0" width="1190" height="772"/></clipPath><g clip-path="url(#ha)">'+RIP(595,772,40,10,45,c1,c2,40)+'</g>'
def ARCS_B(c1,c2):  # 円を大きく、表紙側に置き、直径の1/4が背をまたいで裏表紙へ
    return RIP(722,516,30,9.0,26,c1,c2,22)
S=[(spread(SPH2(CU,GP),'CG',CU),'1_A-b_両輪の球'),
   (spread(BANDS2('2'),'JO',RED,True),'2_A-2_二本の帯_ネイビー'),
   (spread(BANDS2('1'),'JO',CW['1']['t'][0][1],True),'3_A-2_二本の帯_カッパー'),
   (spread(BARS3S(),'JO',RED,True),'4_C-2_三本の帯'),
   (spread(ARCS_A(CU,GP),'CG',CU),'5a_届ける力_背で四分円'),(spread(ARCS_B(CU,GP),'CG',CU),'5b_届ける力_大きい円')]
css=CSS2.replace('@page{size:210mm 297mm;margin:0}','@page{size:420mm 297mm;margin:0}')
open('cover16.html','w').write('<!doctype html><meta charset=utf-8><style>'+css+'</style>'+''.join(p for p,_ in S))
import json; json.dump([n for _,n in S],open('cover16_names.json','w'),ensure_ascii=False)
