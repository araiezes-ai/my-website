# 台割 v9（篠原修正案）— 10/6 手書き修正を反映
exec(open('v9_head.py').read())
CSS+=f""".sec{{font-size:8.2px;letter-spacing:2.6px;color:{GOLD};font-weight:400}}
.secj{{font-family:'Noto Sans JP';font-size:8.2px;letter-spacing:.4px;color:{SUB};font-weight:300}}
.big{{font-weight:200;font-size:250px;line-height:1;color:transparent;-webkit-text-stroke:.6px #e6e9ec;letter-spacing:-8px}}
.em{{font-family:'Noto Sans JP';font-weight:500;font-size:9.4px}}
"""
SPH=['v9/sph1.png','v9/sph2.png','v9/sph3.png']
def sph(cx,cy,d,i=0): return f'<img class="a" src="{uri(SPH[i],700,"PNG")}" style="left:{cx-d/2}px;top:{cy-d/2}px;width:{d}px;height:{d}px">'
def BIG(x,y,t): return A(x,y,t,None,'big')
def SEC(x,y,en,jp,gap=None):
    return A(x,y,en,None,'sec')+A(x+(gap if gap else len(en)*7.4+14),y,jp,None,'secj')
def H2(x,y,lab,labj,en,jt,js,size=30,body=0,bw=330):
    o,yy=HEAD(x,y,lab,labj,en,jt,js,size=size)
    if body: o+=BODY(x,yy+4,bw,body); yy+=4+(-(-body*5.6//bw)+1)*12.7
    return o,yy
def flow(d,col=GOLD,sw=.75,op=.85,dots=()):
    o=f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}" opacity="{op}"/>'
    for x,y in dots: o+=f'<circle cx="{x}" cy="{y}" r="2.1" fill="{GOLD}"/>'
    return o
