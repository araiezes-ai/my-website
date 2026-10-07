# 台割 v8 — B案（ガラスの地球儀）のデザイン言語で組んだ構成デザイン案
import base64, io, math, random
from PIL import Image
import glassglobe as G
N_='f/ns/package/files/'
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
_c={}
def uri(f,mx=1400,fmt='JPEG',crop=None,light=0):
    k=(f,mx,fmt,crop,light)
    if k not in _c:
        im=Image.open(f if '/' in f else 'img/'+f)
        im=im.convert('RGBA' if fmt=='PNG' else 'RGB')
        if crop: w,h=im.size; im=im.crop((int(crop[0]*w),int(crop[1]*h),int(crop[2]*w),int(crop[3]*h)))
        if light:
            wh=Image.new(im.mode,im.size,(255,255,255,0) if fmt=='PNG' else (255,255,255))
            a=im.split()[-1] if fmt=='PNG' else None
            im=Image.blend(im,wh,light)
            if a: im.putalpha(a)
        im.thumbnail((mx,mx)); bf=io.BytesIO(); im.save(bf,fmt,**({'quality':84} if fmt=='JPEG' else {}))
        _c[k]=f'data:image/{fmt.lower()};base64,'+base64.b64encode(bf.getvalue()).decode()
    return _c[k]
INK='#23272c'; SUB='#5d636a'; MUTE='#9aa0a6'; GOLD='#b38f4f'; GOLDL='#dcc9a2'; GLASS='#e6eef5'; BLUE='#4f7aa3'; DEEP='#2c4c6e'; RED='#C8102E'; HAIR='#d8dce0'
CSS=f"""@font-face{{font-family:NS;font-weight:200;src:url(data:font/woff2;base64,{b64(N_+'noto-sans-latin-200-normal.woff2')})}}
@font-face{{font-family:NS;font-weight:300;src:url(data:font/woff2;base64,{b64(N_+'noto-sans-latin-300-normal.woff2')})}}
@font-face{{font-family:NS;font-weight:400;src:url(data:font/woff2;base64,{b64(N_+'noto-sans-latin-400-normal.woff2')})}}
@font-face{{font-family:NS;font-weight:500;src:url(data:font/woff2;base64,{b64(N_+'noto-sans-latin-500-normal.woff2')})}}
@page{{size:420mm 297mm;margin:0}}*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:NS,'Noto Sans JP',sans-serif;color:{INK};background:#fff}}
.sp{{position:relative;width:1190px;height:842px;overflow:hidden;background:#fff;page-break-after:always;zoom:1.3333}}
.a{{position:absolute}}
.lab{{font-size:6.6px;letter-spacing:2.2px;color:{GOLD};font-weight:400}}
.labj{{font-size:6.6px;letter-spacing:.6px;color:{MUTE};font-weight:300}}
.en{{font-weight:200;color:{INK};letter-spacing:-.2px;line-height:1.12}}
.jt{{font-family:'Noto Sans JP';font-weight:500;font-size:11px;letter-spacing:.8px;color:{INK}}}
.js{{font-family:'Noto Sans JP';font-weight:300;font-size:8.2px;letter-spacing:.4px;color:{SUB};line-height:1.6}}
.bd{{font-size:7.4px;line-height:1.72;color:#7b8188;font-weight:300;letter-spacing:.1px}}
.cap{{font-size:6px;letter-spacing:1.4px;color:{MUTE}}}
.num{{font-weight:200;color:{INK};line-height:1;letter-spacing:-.5px}}
.sm{{font-family:'Noto Sans JP';font-size:6.6px;line-height:1.55;color:{SUB};font-weight:300}}
.smb{{font-family:'Noto Sans JP';font-size:7.4px;line-height:1.45;color:{INK};font-weight:400}}
.memo{{font-family:'Noto Sans JP';font-size:5.6px;color:#a3a8ae;background:rgba(255,255,255,.85);padding:1px 3px;letter-spacing:.2px;line-height:1.5}}
.fo{{font-size:6.2px;letter-spacing:1.6px;color:{MUTE}}}
.ph{{object-fit:cover;display:block}}
"""
def A(x,y,h,w=None,c='',s=''):
    return f'<div class="a {c}" style="left:{x}px;top:{y}px;{f"width:{w}px;" if w else ""}{s}">{h}</div>'
def svg(x,y,w,h,inner): return f'<svg class="a" style="left:{x}px;top:{y}px;overflow:visible" width="{w}" height="{h}">{inner}</svg>'
def IMG(x,y,w,h,f,pos='50% 50%',r=0,**k):
    return f'<img class="a ph" src="{uri(f,**k)}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-position:{pos};{f"border-radius:{r}px;" if r else ""}">'
def CIRC(cx,cy,d,f,pos='50% 50%',ring=True):
    o=f'<img class="a ph" src="{uri(f,600)}" style="left:{cx-d/2}px;top:{cy-d/2}px;width:{d}px;height:{d}px;border-radius:50%;object-position:{pos}">'
    if ring: o+=f'<div class="a" style="left:{cx-d/2-4}px;top:{cy-d/2-4}px;width:{d+8}px;height:{d+8}px;border-radius:50%;border:.6px solid {GOLDL}"></div>'
    return o
random.seed(4)
LO='lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua enim ad minim veniam quis nostrud exercitation ullamco laboris nisi aliquip ex ea commodo consequat duis aute irure in reprehenderit voluptate velit esse cillum fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt culpa qui officia deserunt mollit anim id est laborum'.split()
def lorem(n):
    w=[random.choice(LO) for _ in range(n)]; w[0]=w[0].capitalize(); s=''
    for i,x in enumerate(w): s+=x+('. ' if i%13==12 else ' ')
    return s.strip()+'.'
def BODY(x,y,w,n,s=''): return A(x,y,lorem(n),w,'bd',s)
def HEAD(x,y,lab,labj,en,jt,js,w=440,size=30):
    o=A(x,y,lab,None,'lab')+A(x,y+11,labj,None,'labj')
    o+=A(x,y+34,en,w,'en',f'font-size:{size}px')
    lines=en.count('<br>')+1; yy=y+34+lines*size*1.12+12
    o+=A(x,yy,'',26,'',f'height:0;border-top:1px solid {RED}')
    o+=A(x,yy+10,jt,w,'jt')+A(x,yy+27,js,w,'js')
    return o, yy+27+ (js.count('<br>')+1)*13.5
def orbit(cx,cy,rx,ry,rot,dots=(),col=GOLDL,sw=.6,op=1):
    o=f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" transform="rotate({rot} {cx} {cy})" fill="none" stroke="{col}" stroke-width="{sw}" opacity="{op}"/>'
    for a in dots:
        t=math.radians(a); x=rx*math.cos(t); y=ry*math.sin(t); r=math.radians(rot)
        px,py=cx+x*math.cos(r)-y*math.sin(r),cy+x*math.sin(r)+y*math.cos(r)
        o+=f'<circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="{GOLD}" opacity=".16"/><circle cx="{px:.1f}" cy="{py:.1f}" r="2" fill="{GOLD}"/>'
    return o
def spread(body,l,r,memo_l,memo_r,orb=''):
    o=f'<div class="sp">'+(svg(0,0,1190,842,orb) if orb else '')+body
    o+=A(48,806,f'{l:02d}',None,'fo')+A(1130,806,f'{r:02d}',None,'fo')
    o+=A(48,818,'台割メモ｜'+memo_l,480,'memo')+A(643,818,'台割メモ｜'+memo_r,480,'memo')
    return o+'<div class="a" style="left:595px;top:0;height:842px;border-left:.5px dashed #e3e6e9"></div></div>'
L=48; R=643; W=499
pages=[]
GLOBE_F='v8/gl_-28_-8_-10_1700_0.34.png'; GLOBE_B='v8/gl_138_-14_6_1700_0.2.png'

