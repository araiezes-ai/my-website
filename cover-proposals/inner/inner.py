import base64, math
from hl import hairmap
N='f/ns/package/files/'
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
CSS=f"""
@font-face{{font-family:NS;font-weight:300;src:url(data:font/woff2;base64,{b64(N+'noto-sans-latin-300-normal.woff2')})}}
@font-face{{font-family:NS;font-weight:400;src:url(data:font/woff2;base64,{b64(N+'noto-sans-latin-400-normal.woff2')})}}
@font-face{{font-family:NS;font-weight:500;src:url(data:font/woff2;base64,{b64(N+'noto-sans-latin-500-normal.woff2')})}}
@page{{size:420mm 297mm;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:NS,'IPAPGothic',sans-serif;color:#2e3135;background:#fff}}
.sp{{position:relative;width:1190px;height:842px;overflow:hidden;background:#fff;page-break-after:always;zoom:1.3333}}
.sp:after{{content:"";position:absolute;left:595px;top:0;bottom:0;border-left:1px dashed #e4e6e8}}
.a{{position:absolute}}
.lab{{font-size:7.2px;letter-spacing:2.2px;color:#6b7076;font-weight:400;text-transform:uppercase;white-space:nowrap}}
.lab b{{display:inline-block;width:14px;height:1px;background:#C8102E;vertical-align:middle;margin-right:8px}}
.h1{{font-weight:300;font-size:25px;line-height:1.28;letter-spacing:.1px;color:#24272b}}
.h2{{font-weight:400;font-size:10.5px;letter-spacing:.3px;color:#2e3135}}
.h2:before{{content:"";display:block;width:16px;height:1px;background:#2e3135;margin-bottom:7px}}
.cap{{font-size:6.6px;letter-spacing:1.6px;color:#7a7f85;text-transform:uppercase}}
.num{{font-weight:300;color:#24272b;letter-spacing:-.3px;line-height:1}}
.body{{font-weight:300;font-size:8.6px;line-height:1.62;color:#45494e}}
.note{{font-family:'IPAPGothic';font-size:6.4px;color:#9a6a6f}}
.ph{{background-color:#f6f7f8;background-image:repeating-linear-gradient(90deg,#dfe2e5 0 .55px,transparent .55px 2.3px);display:flex;align-items:center;justify-content:center}}
.ph span{{font-family:'IPAPGothic';font-size:7px;color:#8a8f95;background:#f6f7f8;padding:2px 6px}}
.bar{{height:2.4px;background:#e1e4e7;margin-bottom:6.4px}}
.rule{{position:absolute;height:0;border-top:.6px solid #cdd0d4}}
.vrule{{position:absolute;width:0;border-left:.6px solid #cdd0d4}}
.fol{{font-size:7px;letter-spacing:1.6px;color:#8a8f95}}
"""
def A(x,y,html,w=None,cls='',style=''):
    ws=f'width:{w}px;' if w else ''
    return f'<div class="a {cls}" style="left:{x}px;top:{y}px;{ws}{style}">{html}</div>'
from PIL import Image as _I
import io as _io
IMG={'画像：三綱領':('r-000.png','contain'),
'写真：鉱山（上流）':'x_vc_mine.jpg','写真：製錬所（中流）':'x_vc_smelter.jpg','写真：洋上風力（用途）':'x_vc_wind.jpg','写真：EV（需要家）':'x_vc_ev.jpg',
'写真：BMA鉱山・重機':'r-047.png','写真：原料炭':'r-048.png','写真：港湾・鉄道':'r-023.png','写真：パートナー':'r-051.png',
'写真：銅鉱山':'r-053.png','写真：低炭素銅の取り組み':'r-046.png','写真：安定的な供給基盤':'r-054.png','写真：長期的な価値創造':'r-052.png',
'写真：積出港・銅カソード':'r-072.png','写真：鉱山':'c_94ce967e-016.png','写真：製錬':'c_a5a586a7-010.png','写真：最終製品':'r-022.png',
'写真：夜空と鉱山車両':'r-075.png',
'写真：鉄鉱石':('x_ironore.jpg','contain'),'写真：ニッケル':('r-073.png','contain'),'写真：リチウム':('x_lithium.jpg','contain'),'写真：アルミ':('x_alu.jpg','contain'),'写真：ボーキサイト':('r-055.png','contain'),'写真：二次資源':'r-074.png',
'写真：現場で働く人々':'r-082.png','写真：植生調査・環境':'r-084.png','写真：都市・人口':'x_ch076.jpg','写真：鉱山開発':'x_ch078.jpg','写真：港湾・物流':'x_ch080.jpg'}
_cache={}
def _uri(f):
    if f not in _cache:
        im=_I.open('img/'+f).convert('RGB'); im.thumbnail((1400,1400)); bf=_io.BytesIO(); im.save(bf,'JPEG',quality=86)
        _cache[f]='data:image/jpeg;base64,'+base64.b64encode(bf.getvalue()).decode()
    return _cache[f]
def ph(x,y,w,h,label):
    v=IMG.get(label)
    if v:
        f,fit=(v if isinstance(v,tuple) else (v,'cover'))
        return f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:#fff;overflow:hidden"><img src="{_uri(f)}" style="width:100%;height:100%;object-fit:{fit};display:block"></div>'
    return f'<div class="a ph" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><span>{label}</span></div>'
def bars(x,y,w,n,last=.55):
    s=''.join(f'<div class="bar" style="width:{(last if i==n-1 else 1)*100:.0f}%"></div>' for i in range(n))
    return A(x,y,s,w)
def rule(x,y,w): return f'<div class="rule" style="left:{x}px;top:{y}px;width:{w}px"></div>'
def vrule(x,y,h): return f'<div class="vrule" style="left:{x}px;top:{y}px;height:{h}px"></div>'
def lab(x,y,t): return A(x,y,f'<b></b>{t}',cls='lab')
def h2(x,y,t,w=None): return A(x,y,t,w,'h2')
def note(x,y,t,w=None): return A(x,y,'※'+t,w,'note')
def folio(n,left):
    t=f'{n:02d}'
    if left: return A(48,806,f'{t}&nbsp;&nbsp;&nbsp;&nbsp;MITSUBISHI CORPORATION&nbsp;&nbsp;·&nbsp;&nbsp;MINERAL RESOURCES GROUP',cls='fol')
    return A(1190-48-20,806,t,cls='fol')
def svg(x,y,w,h,inner): return f'<svg class="a" style="left:{x}px;top:{y}px;overflow:visible" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{inner}</svg>'
def hairbar(x,y,w,h,shade=90,step=1.5,sw=.4):
    c=f'rgb({shade},{shade+3},{shade+7})'
    d=''.join(f'M{x+i*step:.1f},{y}v{h}' for i in range(int(w/step)+1))
    return f'<path d="{d}" stroke="{c}" stroke-width="{sw}"/>'
def spread(body,l,r): return f'<div class="sp">{body}{folio(l,True)}{folio(r,False)}</div>'
L=48; R=595+48; CW=595-96
pages=[]

# ---------- P.02-03 ----------
b=''
b+=lab(L,52,'Introduction')
b+=A(L,96,'Strength to Hold.<br>Power to Connect.',cls='h1',style='font-size:34px;line-height:1.22')
core=("Resources, on their own, do not hold value. It takes someone to discover them, nurture them, and deliver them to where they're needed. "
"Only then do they become true power.<br><br>We engage with world-class assets, connecting the value chain from upstream to downstream through investment and trading. "
"Because we stand on fair ground, we can bridge gaps others cannot. Because we stand between diverse partners and users, we find the right answer for every moment. "
"Because we hold the assets, we turn the value dormant in the world into power for society.")
b+=A(L,200,core,330,'body',style='font-size:9.4px;line-height:1.75')
b+=rule(L,452,CW)
b+=h2(L,470,'Mitsubishi Corporation at a Glance')
b+=A(L,496,"One of Japan's leading integrated trading companies",cls='cap',style='text-transform:none;letter-spacing:.3px;font-size:8px')
b+=ph(L,530,150,72,'画像：三綱領')+A(L,608,'The Three Corporate Principles',150,'cap',style='letter-spacing:1px')
facts=[('1954','Founded'),('76','Countries &amp; regions<br>104 locations'),('Diverse','Business base across<br>industries'),('Integrated','Strength of a general<br>trading company')]
for i,(n,c) in enumerate(facts):
    fx=L+178+(i%2)*162; fy=524+(i//2)*100
    b+=rule(fx,fy,140)
    b+=A(fx,fy+12,n,cls='num',style=f'font-size:{30 if n[0].isdigit() else 19}px')
    b+=A(fx,fy+52,c,cls='cap',style='line-height:1.6')
b+=note(L,724,'P.02 下段は事実情報のみ。数字は大きく細く、アイコン・色面は使わない')
# right: contents
b+=lab(R,52,'Contents')
toc=[('00','Who We Are','Mitsubishi Corporation / The Mineral Resources Group at the core','02'),
('01','How We Work','Credibility and integrated strength / Value across the full value chain','04'),
('02','What We Have','Metallurgical coal / Copper / Trading network / Expanding possibilities','06'),
('03','Proof','The partner of choice in the resources industry','10'),
('04','Vision &amp; Action','A sustainable supply of the quality metal resources society needs','11')]
for i,(n,t,s,p) in enumerate(toc):
    ty=92+i*50
    b+=rule(R,ty,CW)
    b+=A(R,ty+11,n,cls='num',style='font-size:20px;color:#9aa0a6')
    b+=A(R+52,ty+9,t,style='font-size:13px;font-weight:300;color:#24272b')
    b+=A(R+52,ty+29,s,cls='body',style='font-size:7.8px;color:#7a7f85')
    b+=A(R+CW-20,ty+12,p,cls='fol',style='text-align:right;width:20px')
b+=rule(R,342,CW)
b+=h2(R,378,'The Mineral Resources Group at the Core')
b+=bars(R,404,300,2,.7)
# group list
b+=A(R,442,'Business groups of<br>Mitsubishi Corporation',cls='cap',style='line-height:1.6')
for i in range(10):
    gy=470+i*17
    if i==2: b+=A(R,gy,'Mineral Resources Group',cls='h2',style='font-size:8.6px;color:#C8102E;letter-spacing:.2px').replace('h2','')
    else: b+=A(R,gy+3,'<div class="bar" style="width:%dpx;margin:0"></div>'%(80+(i*23)%50))
    b+=rule(R,gy+13,150)
b+=note(R,646,'正式なグループ名称を挿入',150)
# three pillars diagram
cx,cy=R+352,560; r=62
inner=''
for k,(ang,t1,t2) in enumerate([(-90,'Resource Investment','&amp; Development'),(150,'Metal Resources','Trading'),(30,'Business Management','&amp; Partnerships')]):
    px_=cx+44*math.cos(math.radians(ang)); py_=cy+44*math.sin(math.radians(ang))
    inner+=f'<circle cx="{px_-R+20:.1f}" cy="{py_-440:.1f}" r="{r}" fill="none" stroke="#9ea3a9" stroke-width=".6"/>'
b+=svg(R-20,440,500,260,inner)
for ang,t in [(-90,'Resource Investment<br>&amp; Development'),(150,'Metal Resources<br>Trading'),(30,'Business Management<br>&amp; Partnerships')]:
    tx=cx+62*math.cos(math.radians(ang))-50; ty=cy+(-136 if ang==-90 else 92)
    b+=A(tx,ty,t,100,'cap',style='text-align:center;line-height:1.6;letter-spacing:1px')
b+=A(cx-40,cy-8,'Mineral<br>Resources Group',80,'h2',style='text-align:center;font-size:8px').replace('class="a h2"','class="a"')
b+=note(R,724,'三本柱は線画の円で表現（色面なし）。各柱の説明文は図の下に追加可',300)
pages.append(spread(b,2,3))

# ---------- P.04-05 ----------
b=''
b+=lab(L,52,'01&nbsp;&nbsp;How We Work')
b+=A(L,84,'Driving business with credibility<br>and integrated strength',cls='h1')
b+=bars(L,160,420,4)
b+=rule(L,212,CW)
b+=h2(L,228,'Financial strength of an integrated trading company')
b+=A(L,258,'Group total assets',cls='cap')
b+=A(L,272,'¥4,538.1<span style="font-size:15px;margin-left:4px">bn</span>',cls='num',style='font-size:40px')
b+=A(L,318,'As of March 31, 2025',cls='cap',style='letter-spacing:1px')
# two stacked hairline bar charts
def chart(x,y,title,v1,v2):
    s=A(x,y,title,cls='cap')
    inner=''
    W1=150*v1/230; W2=150*v2/230
    segs=[.38,.24,.18,.2]; shades=[95,140,180,212]; cx_=0
    for sg,sh in zip(segs,shades):
        inner+=hairbar(cx_,0,W1*sg-1.5,16,sh); cx_+=W1*sg
    inner+=hairbar(0,40,W2,16,212)
    s+=svg(x+86,y+18,220,60,inner)
    s+=A(x,y+18,'FY2024',cls='cap',style='letter-spacing:1px')+A(x,y+27,f'¥{v1:.1f}bn',cls='num',style='font-size:12px')
    s+=A(x,y+58,'FY2025 forecast',cls='cap',style='letter-spacing:1px')+A(x,y+67,f'¥{v2:.1f}bn',cls='num',style='font-size:12px;color:#7a7f85')
    return s
b+=chart(L,350,'Group operating revenue',178.7,145.0)
b+=chart(L+258,350,'Group net income (consolidated)',227.8,114.0)
leg=''.join(f'<span style="display:inline-block;width:10px;height:7px;margin:0 4px 0 {0 if i==0 else 12}px;vertical-align:-1px;background:repeating-linear-gradient(90deg,rgb({s},{s+3},{s+7}) 0 .6px,transparent .6px 1.6px)"></span>{t}' for i,(s,t) in enumerate([(95,'Metallurgical coal'),(140,'Copper'),(180,'Iron ore'),(212,'Other')]))
b+=A(L,440,leg,cls='cap',style='letter-spacing:.8px;white-space:nowrap')
b+=note(L,456,'金額は粗原稿（億円）を英文表記に換算。内訳比率はダミー、名称・会計期間の表記は要確認',CW)
b+=rule(L,482,CW)
b+=h2(L,498,'Integrated strength through collaboration across the company')
b+=bars(L,522,230,3)
stats=[('4','Countries','Quality asset portfolio'),('57','Countries','Global presence'),('6','Commodities','Investment &amp; mining'),('13+','Commodities','Trading')]
for i,(n,u,c) in enumerate(stats):
    sx=L+(i%4)*125; sy=580
    b+=vrule(sx,sy,62) if i else ''
    b+=A(sx+(10 if i else 0),sy,f'{n}<span style="font-size:10px;margin-left:3px">{u}</span>',cls='num',style='font-size:28px')
    b+=A(sx+(10 if i else 0),sy+38,c,cls='cap')
b+=A(L,660,'<b style="font-weight:400;color:#2e3135">Investment &amp; mining:</b> Metallurgical coal, iron ore, copper (molybdenum, zinc), bauxite, nickel, lithium&nbsp;&nbsp;·&nbsp;&nbsp;<b style="font-weight:400;color:#2e3135">Trading:</b> also aluminium, precious metals, thermal coal, chrome, lead, tin, rare earths, fertiliser resources etc.',CW,'body',style='font-size:7.6px')
b+=rule(L,706,CW)
b+=h2(L,722,'Governance that supports speed')
b+=bars(L+250,722,249,3)
# right page
b+=lab(R,52,'01&nbsp;&nbsp;How We Work')
b+=A(R,84,'Delivering value to society<br>across the full value chain',cls='h1')
b+=bars(R,160,420,4)
b+=rule(R,212,CW)
b+=h2(R,228,'Creating value seamlessly, from upstream to downstream')
# flow line
fl='<line x1="0" y1="6" x2="490" y2="6" stroke="#9ea3a9" stroke-width=".6"/>'
for i in range(3): fl+=f'<circle cx="{i*170+3}" cy="6" r="3" fill="#fff" stroke="#2e3135" stroke-width=".7"/>'
fl+='<path d="M484,2 L492,6 L484,10" fill="none" stroke="#9ea3a9" stroke-width=".6"/>'
b+=svg(R,268,500,14,fl)
cols=[('Upstream','Resource investment<br>&amp; development'),('Midstream','Smelting, processing<br>&amp; logistics'),('Downstream','Sales &amp; supply<br>to end users')]
for i,(t,s) in enumerate(cols):
    x=R+i*170
    b+=A(x,292,t,cls='cap',style='color:#C8102E' if i==0 else '')
    b+=A(x,306,s,150,'h2',style='font-size:11px;font-weight:300;line-height:1.35').replace('class="a h2"','class="a"')
    b+=bars(x,344,150,4)
b+=rule(R,392,CW)
labels=['写真：鉱山（上流）','写真：製錬所（中流）','写真：洋上風力（用途）','写真：EV（需要家）']
for i,l in enumerate(labels):
    b+=ph(R+i*127,412,115,150,l)
    if i<3: b+=svg(R+i*127+115,484,12,6,'<path d="M2,3H10M7,0.5L10,3L7,5.5" stroke="#9ea3a9" stroke-width=".6" fill="none"/>')
b+=A(R,574,'Mine&nbsp;&nbsp;→&nbsp;&nbsp;Smelter&nbsp;&nbsp;→&nbsp;&nbsp;Applications&nbsp;&nbsp;→&nbsp;&nbsp;End users',cls='cap')
b+=note(R,600,'粗原稿の三色矢印・赤三角の装飾は廃止。1本の細線と3点で流れを示し、色は上流の朱1点のみ',CW)
pages.append(spread(b,4,5))

# ---------- P.06-07 ----------
b=''
b+=lab(L,52,'02&nbsp;&nbsp;What We Have&nbsp;&nbsp;—&nbsp;&nbsp;Metallurgical Coal')
b+=A(L,84,'World-class metallurgical coal<br>that supports steelmaking',cls='h1')
b+=bars(L,160,220,6)
b+=ph(L+250,150,249,170,'写真：BMA鉱山・重機')
b+=rule(L,340,CW)
b+=A(L,356,'BMA share of seaborne premium hard coking coal supply (2026)',cls='cap')
b+=A(L,374,'≈50<span style="font-size:18px">%</span>',cls='num',style='font-size:46px')
sh=''
sh+=hairbar(0,0,58,12,95)+hairbar(60,0,58,12,150)+hairbar(120,0,150,12,215)
b+=svg(L,432,250,14,sh)
b+=A(L,450,'BHP<br>≈23%',56,'cap',style='line-height:1.5;letter-spacing:.6px')+A(L+60,450,'MC<br>≈23%',56,'cap',style='line-height:1.5;letter-spacing:.6px')+A(L+120,450,'Other<br>suppliers',80,'cap',style='line-height:1.5;letter-spacing:.6px')
b+=note(L,474,'MC＝三菱商事。粗原稿の円グラフを横一本のヘアラインバーに。比率は要確認',260)
m,mw,mh,mpx=hairmap(160,112,155,-44,-9,step=1.3,sw=.4,japan=False,dark=135,light=225,sites=[(148.3,-22.3,'#C8102E')])
bx,by=mpx(148.3,-22.3)
b+=svg(L+330,356,160,mh,m+f'<line x1="{bx:.1f}" y1="{by:.1f}" x2="{bx-30:.1f}" y2="{by-34:.1f}" stroke="#2e3135" stroke-width=".5"/>')
b+=A(L+330+bx-80,356+by-44,'Bowen Basin',cls='cap',style='color:#2e3135')
b+=A(L+330,356+mh+6,'Queensland, Australia',cls='cap')
b+=rule(L,506,CW)
feats=[('Quality','High calorific value and low impurities: a stable supply of high-grade coking coal.'),
('Scale','Large-scale production and transport infrastructure in the Bowen Basin ensure stable supply.'),
('Partnership','Long-standing partnerships build a robust foundation for sustainable growth.')]
for i,(t,s) in enumerate(feats):
    x=L+i*170
    b+=A(x,522,t,cls='cap',style='color:#2e3135;font-weight:500')
    b+=A(x,538,s,150,'body')
    b+=ph(x,600,155,150,['写真：原料炭','写真：港湾・鉄道','写真：パートナー'][i])
b+=lab(R,52,'02&nbsp;&nbsp;What We Have&nbsp;&nbsp;—&nbsp;&nbsp;Copper')
b+=A(R,84,'A copper portfolio that powers<br>an electrified society',cls='h1')
b+=bars(R,160,220,6)
b+=ph(R+250,150,249,170,'写真：銅鉱山')
b+=rule(R,340,CW)
b+=A(R,356,'Major mines in our portfolio (examples)',cls='cap')
mines=[('Escondida','Chile','One of the largest copper mines in the world'),('Los Pelambres','Chile','Long-term supply through stable production and expansion'),
('Antamina','Peru','A high-quality copper and zinc polymetallic mine'),('Quellaveco','Peru','A large copper mine set to be a next-generation core asset'),('Others','','Expanding the portfolio by capturing growth opportunities')]
for i,(n,c,d) in enumerate(mines):
    y=374+i*26
    b+=A(R,y,f'{i+1:02d}',cls='num',style='font-size:11px;color:#9aa0a6')
    b+=A(R+24,y,n,cls='h2',style='font-size:9.5px').replace('class="a h2"','class="a"')
    b+=A(R+24,y+12,c,cls='cap',style='letter-spacing:1px')
    b+=A(R+100,y+1,d,140,'body',style='font-size:7.4px;line-height:1.4')
    b+=rule(R,y+21,290)
m,mw,mh,mpx=hairmap(110,-90,-56,-36,-2,step=1.3,sw=.4,japan=False,dark=135,light=225,sites=[(-69.07,-24.27,'#C8102E'),(-70.5,-31.7,'#C8102E'),(-77.05,-9.53,'#C8102E'),(-70.6,-17.1,'#C8102E')])
lbl=''
for n,lo,la,dx in [('Antamina',-77.05,-9.53,10),('Quellaveco',-70.6,-17.1,10),('Escondida',-69.07,-24.27,10),('Los Pelambres',-70.5,-31.7,10)]:
    x,y=mpx(lo,la); lbl+=A(R+360+x-78,346+y-4,n,70,cls='cap',style='color:#2e3135;letter-spacing:.8px;text-align:right')
b+=svg(R+360,346,110,mh,m)+lbl
b+=rule(R,530,CW)
b+=h2(R,546,'Low-carbon copper (Green Copper)')
b+=bars(R,570,230,4)
b+=ph(R+250,546,249,110,'写真：低炭素銅の取り組み')
b+=ph(R,670,240,90,'写真：安定的な供給基盤')+ph(R+259,670,240,90,'写真：長期的な価値創造')
pages.append(spread(b,6,7))

# ---------- P.08-09 ----------
b=''
b+=lab(L,52,'02&nbsp;&nbsp;What We Have&nbsp;&nbsp;—&nbsp;&nbsp;Trading')
b+=A(L,84,'A sales network connecting<br>global resources and demand',cls='h1')
b+=bars(L,160,220,5)
b+=ph(L+250,150,249,140,'写真：積出港・銅カソード')
b+=rule(L,312,CW)
b+=A(L,328,'A sales network that connects markets',cls='cap')
nums=[('15','industries'),('50','countries'),('~1,000','companies')]
x=L
for i,(n,u) in enumerate(nums):
    b+=A(x,346,f'{n}<span style="font-size:8.5px;margin-left:2px">{u}</span>',cls='num',style='font-size:24px')
    x+= [78,82,0][i]
    if i<2: b+=A(x-13,354,'×',cls='num',style='font-size:11px;color:#9aa0a6')
b+=A(L+330,328,'Global network',cls='cap')
b+=A(L+330,346,'10<span style="font-size:8.5px;margin-left:2px">offices</span>',cls='num',style='font-size:24px')
b+=A(L+330,378,'Singapore · Japan · India · China · United States · United Kingdom · UAE · Indonesia · Thailand · Chile',170,'body',style='font-size:7.6px')
b+=rule(L,430,CW)
b+=h2(L,446,'The RtM business model')
dg=''
for i,(t,y) in enumerate([('Mitsubishi Corporation',0),('RtM (Resource Trading &amp; Marketing)',62),('Customers',124)]):
    dg+=f'<rect x="0" y="{y}" width="200" height="22" fill="none" stroke="#9ea3a9" stroke-width=".6"/>'
for y in (22,84):
    dg+=f'<line x1="70" y1="{y}" x2="70" y2="{y+40}" stroke="#2e3135" stroke-width=".6"/><path d="M67,{y+35} L70,{y+40} L73,{y+35}" fill="none" stroke="#2e3135" stroke-width=".6"/>'
    dg+=f'<line x1="130" y1="{y+40}" x2="130" y2="{y}" stroke="#9ea3a9" stroke-width=".6"/><path d="M127,{y+5} L130,{y} L133,{y+5}" fill="none" stroke="#9ea3a9" stroke-width=".6"/>'
b+=svg(L,474,200,150,dg)
for t,y in [('Mitsubishi Corporation',0),('RtM',62),('Customers',124)]:
    b+=A(L,474+y+6,t,200,'cap',style='text-align:center;color:#2e3135')
b+=A(L+210,500,'Supply from owned assets',90,'cap',style='line-height:1.5')
b+=A(L+210,550,'Market insight &amp; new business opportunities',100,'cap',style='line-height:1.5')
b+=A(L+210,580,'Intelligence from broad industry touchpoints',100,'cap',style='line-height:1.5')
# performance chart
ch=''
vals=[30,34,38,45,52,60,66,72,78,86,95]
for i,v in enumerate(vals):
    ch+=hairbar(i*15,100-v,10,v,120 if i<6 else 200,step=1.5)
ch+='<line x1="0" y1="100.5" x2="165" y2="100.5" stroke="#9ea3a9" stroke-width=".5"/>'
b+=A(L+330,446,'Trading performance',cls='cap')
b+=svg(L+330,470,170,104,ch)
b+=A(L+330,580,'FY20&nbsp;&nbsp;—&nbsp;&nbsp;FY25&nbsp;&nbsp;—&nbsp;&nbsp;FY30 (plan)',cls='cap',style='letter-spacing:1px')
b+=A(L+330,452+12,'Base earnings: ¥16–17bn → ¥25bn (target)',170,'cap',style='color:#C8102E;letter-spacing:.8px')+note(L+330,596,'棒の値はダミー。粗原稿のグラフ数値を挿入',170)
b+=rule(L,636,CW)
b+=h2(L,650,'Case: from mine to end user')
steps=['Mine','Trading','Smelting &amp; refining','Trading','End use']
for i,s in enumerate(steps):
    x=L+i*101
    b+=ph(x,676,92,64,['写真：鉱山','RtM','写真：製錬','RtM','写真：最終製品'][i])
    b+=A(x,746,s,92,'cap',style='color:#C8102E' if s=='Trading' else '')
b+=lab(R,52,'02&nbsp;&nbsp;What We Have&nbsp;&nbsp;—&nbsp;&nbsp;Other Businesses')
b+=A(R,84,'Expanding the potential<br>of resources',cls='h1')
b+=bars(R,160,220,5)
b+=ph(R+250,150,249,110,'写真：夜空と鉱山車両')
b+=rule(R,282,CW)
b+=A(R,298,'Where we operate',cls='cap')
S=[(13.2,65.8),(-0.1,51.5),(77.2,28.6),(103.8,1.3),(139.7,35.7,'#C8102E'),(148.3,-22.3),(141.7,-13.3),(121.4,-30.0),(153.0,-27.5),
(-128.9,58.5),(-94.0,51.6),(-66.9,52.9),(-77.0,40.4),(-96.0,33.0),(-77.05,-9.53),(-77.0,-12.0),(-70.6,-17.1),(-70.3,-22.9),(-69.07,-24.27),(-70.9,-28.6),(-70.5,-31.7),(-70.65,-33.45),(-70.3,-33.15)]
m,mw,mh,mpx=hairmap(CW,-25,335,-56,76,step=1.3,sw=.4,sites=S,site_r=1.4,dark=120,light=222)
b+=svg(R,318,CW,mh,m)
def tag(lo,la,text,dx,dy,anchor='left'):
    x,y=mpx(lo,la); X=R+x; Y=318+y
    s=svg(0,0,1,1,'')
    line=f'<line x1="{X:.1f}" y1="{Y:.1f}" x2="{X+dx:.1f}" y2="{Y+dy:.1f}" stroke="#6b7076" stroke-width=".4"/>'
    s=f'<svg class="a" style="left:0;top:0;overflow:visible" width="1" height="1">{line}</svg>'
    tx=X+dx+(3 if dx>=0 else -153); al='left' if dx>=0 else 'right'
    return s+A(tx,Y+dy-4,text,150,'cap',style=f'text-align:{al};letter-spacing:.6px;font-size:5.8px;line-height:1.4;color:#45494e')
REG=[('01','Europe',(5,58),'Arctial — aluminium<br>RtM Europe / Triland Metals'),
('02','Asia',(104,20),'RtM Japan<br>RtM International<br>RtM Bharat'),
('03','Australia',(146,-34),'BMA — coking coal<br>Aurukun — bauxite<br>Goongarrie Hub — nickel<br>MDP'),
('04','North America',(-104,60),'Turnagain — nickel<br>PAK Lithium<br>IOC — iron ore<br>Elemental USA — recycling<br>RtM Americas'),
('05','Chile &amp; Peru',(-84,-24),'Escondida · Los Pelambres<br>Antamina · Quellaveco<br>Marimaca · Anglo American Sur<br>CAP/CMP — iron ore<br>MCI · MCIP')]
for i,(n,t,(lo,la),items) in enumerate(REG):
    x,y=mpx(lo,la)
    b+=A(R+x-7,318+y-6,n,14,style='font-size:6.5px;text-align:center;background:#fff;color:#C8102E;letter-spacing:.5px;line-height:12px;border:.5px solid #C8102E;border-radius:7px')
    cx_=R+i*100
    b+=A(cx_,318+mh+12,f'<span style="color:#C8102E">{n}</span>&nbsp;&nbsp;{t}',96,'cap',style='color:#2e3135')
    b+=A(cx_,318+mh+26,items,96,'body',style='font-size:6.6px;line-height:1.55')
b+=note(R,318+mh+96,'表紙と同じヘアライン地図を再利用。凡例は色分けせず、名称＋商品名のテキストで示す',CW)
tiles=['Iron ore','Nickel','Lithium','Aluminium','Bauxite','Recycled resources']
for i,t in enumerate(tiles):
    x=R+i*84; y=640
    b+=ph(x,y,76,96,'写真：'+['鉄鉱石','ニッケル','リチウム','アルミ','ボーキサイト','二次資源'][i])
    b+=A(x,y+116,t,80,'cap',style='color:#2e3135')
pages.append(spread(b,8,9))

# ---------- P.10-11 ----------
b=''
b+=lab(L,52,'03&nbsp;&nbsp;Proof')
b+=A(L,84,'The partner of choice<br>in the resources industry',cls='h1')
b+=bars(L,160,220,5)
b+=ph(L+250,150,249,150,'写真：現場で働く人々')
b+=rule(L,322,CW)
b+=h2(L,338,'An indispensable presence in the resources industry')
b+=bars(L,362,CW,2,.8)
gx,gy,gw,gh=L,410,CW,330
b+=f'<div class="rule" style="left:{gx}px;top:{gy+gh/2}px;width:{gw}px"></div><div class="vrule" style="left:{gx+gw/2}px;top:{gy}px;height:{gh}px"></div>'
b+=A(gx+gw/2-70,gy+gh/2-34,'<div style="background:#fff;padding:12px 0;text-align:center"><div style="width:14px;height:1px;background:#C8102E;margin:0 auto 10px"></div><span class="num" style="font-size:22px">Partner<br>of Choice</span></div>',140)
quad=[('Cultural affinity with resource majors',0,0),('JV management capability backed by investment experience',1,0),('A sound financial base built on our business portfolio',0,1),('Deep insight into the macro environment and resource value chain',1,1)]
for t,qx,qy in quad:
    x=gx+qx*(gw/2)+(30 if qx else 0); y=gy+qy*(gh/2)+(70 if qy else 22)
    b+=A(x,y,t,170,'h2',style='font-size:10px;font-weight:300;line-height:1.4').replace('class="a h2"','class="a"')
    b+=bars(x,y+44,170,3)
b+=note(L,750,'粗原稿の黄色い円は廃止。十字の細線で4要素を等価に並べ、中心に Partner of Choice',CW)
b+=lab(R,52,'04&nbsp;&nbsp;Vision &amp; Action')
b+=A(R,84,'Sustainably supplying the quality<br>metal resources society needs',cls='h1')
b+=bars(R,160,220,5)
b+=ph(R+250,150,249,150,'写真：植生調査・環境')
b+=rule(R,322,CW)
b+=A(R,338,'Group mission',cls='cap')
b+=A(R,358,'“To contribute to a better society by providing a stable and sustainable supply of the quality metal resources that society needs.”',CW,'num',style='font-size:16px;line-height:1.45')
b+=rule(R,430,CW)
ch=[('01','Growing demand',['Global population growth','Rising metal demand from electrification and decarbonisation','Infrastructure development in emerging economies']),
('02','Supply constraints',['Intensifying competition for quality assets','Increasing difficulty of mine development','Growing importance of regulation and community consent']),
('03','Geopolitics &amp; supply chains',['Rising geopolitical risk','Increasingly complex supply chains','Building flexible, resilient supply networks'])]
for i,(n,t,items) in enumerate(ch):
    x=R+i*170
    b+=A(x,446,n,cls='num',style='font-size:22px;color:'+('#C8102E' if i==0 else '#9aa0a6'))
    b+=A(x,474,t,150,'h2',style='font-size:10.5px;font-weight:300').replace('class="a h2"','class="a"')
    b+=ph(x,496,155,90,['写真：都市・人口','写真：鉱山開発','写真：港湾・物流'][i])
    b+=A(x,596,''.join(f'<div style="padding-left:8px;text-indent:-8px;margin-bottom:3px">–&nbsp;{s}</div>' for s in items),150,'body',style='font-size:7.6px;line-height:1.45')
b+=rule(R,672,CW)
b+=h2(R,688,'Our initiatives for social challenges')
b+=bars(R+250,688,249,4)
pages.append(spread(b,10,11))

html=f'<!doctype html><meta charset=utf-8><style>{CSS}</style>'+''.join(pages)
open('inner.html','w').write(html)
