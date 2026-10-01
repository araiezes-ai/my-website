import re
src=open('inner_jp.py').read()
BLUE='#2a5d8a'; GOLD='#b38f4f'
src=src.replace("RED='#C8102E'",f"RED='{BLUE}'").replace(".red{color:#C8102E}",f".red{{color:{BLUE}}}").replace("#C8102E",BLUE)
src=re.sub(r"b\+=bars\((L|R),170,(\d+),\d\)",r"b+=bars(\1,194,\2,3)",src)
src=re.sub(r"b\+=bars\((L|R),206,(\d+),\d\)",r"b+=bars(\1,238,\2,3)",src)
src=src.replace('fill="#5d6268"/><text','fill="#1f3c58"/><text')
src=src.replace(f"color:{BLUE};letter-spacing:.5px;line-height:12px;border:.5px solid {BLUE}",f"color:{GOLD};letter-spacing:.5px;line-height:12px;border:.5px solid {GOLD}")
OVR=r'''
import math as _m, re as _re
BLUE='#2a5d8a'; GOLD='#b38f4f'
CSS+=""".jh1:after,.h1:after{content:"";display:block;width:34px;height:1px;background:#C8102E;margin-top:12px}
.lab b{background:#b38f4f!important}
.ph{background-image:none!important;background:linear-gradient(135deg,#f1f6fa,#dde8f1)!important}
.ph span{background:transparent!important;color:#7d95ab!important}
.sp:after{border-left-color:#e6edf3!important}
"""
def _mix(a,b,t):
    t=max(0,min(1,t)); return '#%02x%02x%02x'%tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))
def hairbar(x,y,w,h,shade=90,step=1.5,sw=.4):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(w,0):.1f}" height="{h}" fill="{_mix((40,82,122),(214,228,239),(shade-90)/125)}"/>'
_orig_hm=hairmap
def hairmap(w,lon0,lon1,lat0,lat1,step=1.1,sw=.45,sites=(),japan=True,seed=3,dark=70,light=0xd2,site_r=1.6):
    s,w_,h,px=_orig_hm(w,lon0,lon1,lat0,lat1,step=.75,sw=.8,sites=[(q[0],q[1],GOLD) for q in sites],japan=japan,seed=seed,dark=dark,light=light,site_r=site_r)
    def rc(mo):
        c=int(mo.group(1)); return 'stroke="'+_mix((50,72,96),(170,194,216),(c-dark)/max(1,light-dark))+'"'
    s=_re.sub(r'stroke="rgb\((\d+),\d+,\d+\)"',rc,s).replace('fill="#C8102E"',f'fill="{GOLD}"')
    return s,w_,h,px
def _orbit(cx,cy,rx,ry,rot,dots):
    o=f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" transform="rotate({rot} {cx} {cy})" fill="none" stroke="#d2c3a0" stroke-width=".6"/>'
    for a in dots:
        t=_m.radians(a); x=rx*_m.cos(t); y=ry*_m.sin(t); r=_m.radians(rot)
        o+=f'<circle cx="{cx+x*_m.cos(r)-y*_m.sin(r):.1f}" cy="{cy+x*_m.sin(r)+y*_m.cos(r):.1f}" r="2" fill="{GOLD}"/>'
    return o
_orig_sp=spread
def spread(body,l,r):
    k=l//2
    orb=_orbit(1190+150,-30+k*4,330,96+k*4,-10-k*2,[160+k*6,196-k*4])+_orbit(-80,905,330,105,-8,[305+k*8])
    return _orig_sp(f'<svg class="a" style="left:0;top:0" width="1190" height="842">{orb}</svg>'+body,l,r)
IMG.update({'GLOBE':('g_globe.jpg','cover')})
'''
src=src.replace("exec(open('jp_head.py').read())","exec(open('jp_head.py').read())"+OVR,1)
# P.02 globe visual from the cover
src=src.replace("b+=note(L,388,'コアメッセージ","b+=A(392,40,f'<img src=\"{_uri(\"g_globe.jpg\")}\" style=\"width:203px;height:300px;object-fit:cover;object-position:0 0\">')\nb+=note(L,388,'コアメッセージ",1)
# P.09 ocean + gold arcs from Tokyo
old="b+=svg(R,312,CW,mh,m+mk)"
new='''tx,ty=P_(139.7,35.7); arcs=''
for lo,la in OF+SUB+INV[:3]+[(-69.07,-24.27),(13.2,65.8)]:
    x,y=P_(lo,la); mx,my=(tx+x)/2,min(ty,y)-abs(x-tx)*.18-6
    arcs+=f'<path d="M{tx:.1f},{ty:.1f}Q{mx:.1f},{my:.1f} {x:.1f},{y:.1f}" fill="none" stroke="#c9a96b" stroke-width=".5" opacity=".85"/>'
b+=A(R-6,309,'',CW+12,style=f'height:{mh+6}px;background:radial-gradient(ellipse at 60% 40%,#eef5fa 0%,#dbe8f2 60%,#e9f1f7 100%);border-radius:4px')
b+=svg(R,312,CW,mh,m+arcs+mk)'''
assert old in src; src=src.replace(old,new)
src=src.replace("open('inner_jp.html','w').write(html)","open('inner_globe.html','w').write(html)")
open('inner_globe.py','w').write(src)
