# 台割 案③ v2 — 地球儀に頼らない、モダンで力強い編集デザイン（動画順）
exec(open('v9_head.py').read())
import math
F='f/'
def ff(name,w,path): return f"@font-face{{font-family:{name};font-weight:{w};src:url(data:font/woff2;base64,{b64(path)})}}\n"
CSS2=''.join(ff('IT',w,F+f'intert/package/files/inter-tight-latin-{w}-normal.woff2') for w in (300,500,600,700))
CSS2+=''.join(ff('IN',w,F+f'inter/package/files/inter-latin-{w}-normal.woff2') for w in (300,400,500,600))
INK='#121519'; G1='#3d4249'; G2='#7d838a'; G3='#cfd3d7'; G4='#ecedee'; PAN='#f5f4f1'; BR='#9c7442'; BRL='#c9ad82'; NV='#1f3a56'; NVL='#9fb1c3'; RED='#C8102E'
CSS2+=f"""@page{{size:420mm 297mm;margin:0}}*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:IN,'Noto Sans JP',sans-serif;color:{INK};background:#fff}}
.sp{{position:relative;width:1190px;height:842px;overflow:hidden;background:#fff;page-break-after:always;zoom:1.3333}}
.a{{position:absolute}}
.k{{font-family:IN;font-weight:600;font-size:6.6px;letter-spacing:1.9px;color:{BR};text-transform:uppercase}}
.kj{{font-family:'Noto Sans JP';font-weight:400;font-size:6.6px;letter-spacing:.6px;color:{G2}}}
.d{{font-family:IT;font-weight:600;letter-spacing:-.025em;line-height:1.02;color:{INK}}}
.dl{{font-family:IT;font-weight:300;letter-spacing:-.02em;line-height:1.05;color:{INK}}}
.h{{font-family:'Noto Sans JP';font-weight:700;font-size:11.5px;letter-spacing:.5px;line-height:1.5;color:{INK}}}
.hs{{font-family:'Noto Sans JP';font-weight:500;font-size:8.6px;letter-spacing:.3px;line-height:1.55;color:{INK}}}
.b{{font-family:'Noto Sans JP';font-weight:400;font-size:7.3px;line-height:1.85;letter-spacing:.2px;color:{G1};text-align:justify}}
.s{{font-family:'Noto Sans JP';font-weight:400;font-size:6.2px;line-height:1.6;color:{G2}}}
.n{{font-family:IT;font-weight:300;letter-spacing:-.03em;line-height:.95;color:{INK}}}
.nb{{font-family:IT;font-weight:600;letter-spacing:-.03em;line-height:.95;color:{INK}}}
.l{{font-family:IN;font-weight:500;font-size:6.4px;letter-spacing:.3px;color:{INK}}}
.cap{{font-family:IN;font-weight:500;font-size:5.8px;letter-spacing:1.4px;color:#fff;text-transform:uppercase}}
.memo{{font-family:'Noto Sans JP';font-size:5.4px;color:#a3a8ae;line-height:1.5;background:rgba(255,255,255,.88);padding:1px 3px}}
.fo{{font-family:IN;font-weight:500;font-size:6px;letter-spacing:1.6px;color:{G2}}}
.ph{{object-fit:cover;display:block}}
"""
def T(x,y,html,w=None,c='',s=''): return A(x,y,html,w,c,s)
def rule(x,y,w,c=G3,wd=.6): return A(x,y,'',w,'',f'border-top:{wd}px solid {c}')
def vrule(x,y,h,c=G3,wd=.6): return A(x,y,'',None,'',f'height:{h}px;border-left:{wd}px solid {c}')
def tile(x,y,w,h,f,pos='50% 50%',cap='',sub='',mx=1600):
    o=f'<img class="a ph" src="{uri(f,mx)}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-position:{pos}">'
    if cap: o+=A(x,y+h-34,'',w,'',f'height:34px;background:linear-gradient(0deg,rgba(10,14,18,.55),rgba(10,14,18,0))')+T(x+10,y+h-20,cap,None,'cap')+(T(x+10,y+h-11,sub,None,'cap','font-weight:400;letter-spacing:.8px;text-transform:none;opacity:.85') if sub else '')
    return o
def ptile(x,y,w,h,cap,sub,note):
    return A(x,y,f'<span class="s" style="color:#8a96a3">{note}</span>',w,'',f'height:{h}px;background:linear-gradient(135deg,#e9ecef,#d9dee3);display:flex;align-items:center;justify-content:center;text-align:center')+T(x+10,y+h-20,cap,None,'cap','color:#5a6570')+T(x+10,y+h-11,sub,None,'cap','color:#5a6570;font-weight:400;letter-spacing:.8px;text-transform:none')
def head(x,y,k,kj,en,jt,size=40,w=500):
    o=T(x,y,k,None,'k')+T(x,y+11,kj,None,'kj')+T(x,y+30,en,w,'d',f'font-size:{size}px')
    yy=y+30+(en.count('<br>')+1)*size*1.02+12
    o+=A(x,yy,'',22,'',f'border-top:1.4px solid {RED}')+T(x,yy+10,jt,w,'h')
    return o,yy+10+(jt.count('<br>')+1)*17
def para(x,y,w,t,s=''): return T(x,y,t,w,'b',s)
def spread(b,l,r,ml,mr):
    o='<div class="sp">'+b+T(40,812,f'{l:02d}',None,'fo')+T(1138,812,f'{r:02d}',None,'fo')
    o+=T(66,812,'台割メモ｜'+ml,470,'memo')+T(640,812,'台割メモ｜'+mr,470,'memo')
    return o+'<div class="a" style="left:595px;top:0;height:842px;border-left:.5px dashed #e6e8ea"></div></div>'
def S(inner): return svg(0,0,1190,842,inner)
L=40; R=635; W=515
pages=[]
