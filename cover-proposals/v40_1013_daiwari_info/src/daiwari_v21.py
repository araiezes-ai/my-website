# 台割 v21 — v20 + 背景の白抜き章番号を全ページに／インフォグラフィックを作り込み
exec(open('v20_parts.py').read().split('\n#P23\n')[0])
import math
P23=open('v20_parts.py').read().split('\n#P23\n')[1].split('\n',1)[1]
LW=1.3
def LINE(d,dots=()):
    o=f'<path d="{d}" fill="none" stroke="{CU}" stroke-width="{LW}"/>'
    for x,y in dots: o+=f'<circle cx="{x}" cy="{y}" r="3.4" fill="{CU}" stroke="#fff" stroke-width="1"/>'
    return S(o)
def shade(x,y,w,h): return A(x,y,'',w,'',f'height:{h}px;background:linear-gradient(0deg,rgba(10,14,18,.72),rgba(10,14,18,.05) 60%,rgba(10,14,18,.25))')
def BGN(x,y,t,size=300): return T(x,y,t,None,'out',f'font-size:{size}px;-webkit-text-stroke:1px #e3e6ea')
IC={'mine':'M2,20 L9,9 L13,14 L16,10 L22,20 Z M2,20 H22',
'ship':'M3,15 H21 L18,20 H6 Z M7,15 V10 H14 V15 M10,10 V6',
'factory':'M3,20 V11 L8,14 V11 L13,14 V5 H17 V20 Z',
'bolt':'M13,3 L6,13 H11 L10,21 L18,10 H13 Z',
'recycle':'M5,13 A7,7 0 0 1 17,7 M19,11 A7,7 0 0 1 7,17 M17,3 V7 H13 M7,21 V17 H11',
'flask':'M9,3 H15 M10,3 V9 L5,20 H19 L14,9 V3 M7,15 H17',
'chart':'M4,20 V4 M4,20 H20 M7,16 L11,11 L14,13 L19,7 M16,7 H19 V10',
'link':'M4,12 a5,5 0 1,0 10,0 a5,5 0 1,0 -10,0 M10,12 a5,5 0 1,0 10,0 a5,5 0 1,0 -10,0',
'people':'M5,9 a3,3 0 1,0 6,0 a3,3 0 1,0 -6,0 M3,20 C3,14 13,14 13,20 M14,8 a2.5,2.5 0 1,0 5,0 a2.5,2.5 0 1,0 -5,0 M14,14 C18,12 21,15 21,19',
'shield':'M12,3 L20,6 V12 C20,17 16,20 12,21 C8,20 4,17 4,12 V6 Z M8,12 L11,15 L16,9',
'eye':'M2,12 C6,5 18,5 22,12 C18,19 6,19 2,12 Z M9,12 a3,3 0 1,0 6,0 a3,3 0 1,0 -6,0',
'box':'M4,8 L12,4 L20,8 V17 L12,21 L4,17 Z M4,8 L12,12 L20,8 M12,12 V21',
'truck':'M2,7 H14 V17 H2 Z M14,10 H19 L22,13 V17 H14 M4,19 a2,2 0 1,0 4,0 a2,2 0 1,0 -4,0 M16,19 a2,2 0 1,0 4,0 a2,2 0 1,0 -4,0',
'hedge':'M12,4 V20 M7,20 H17 M4,7 H20 M4,7 L1.5,13 H6.5 Z M20,7 L17.5,13 H22.5 Z',
'grid':'M4,4 H10 V10 H4 Z M14,4 H20 V10 H14 Z M4,14 H10 V20 H4 Z M14,14 H20 V20 H14 Z',
'time':'M6,3 H18 M6,21 H18 M7,3 C7,9 17,15 17,21 M17,3 C17,9 7,15 7,21',
'lock':'M6,11 H18 V21 H6 Z M8,11 V7 A4,4 0 0 1 16,7 V11',
'alert':'M12,3 L22,20 H2 Z M12,9 V14 M12,17 V17.6',
'target':'M4,12 a8,8 0 1,0 16,0 a8,8 0 1,0 -16,0 M8,12 a4,4 0 1,0 8,0 a4,4 0 1,0 -8,0 M12,12 L21,3',
'coin':'M4,12 a8,8 0 1,0 16,0 a8,8 0 1,0 -16,0 M12,7 V17 M9,9.5 H14 a2,2 0 0 1 0,4 H10 a2,2 0 0 0 0,4 H15'}
def ICON(n,x,y,s=20,col=INK,sw=1.4):
    return f'<svg class="a" style="left:{x}px;top:{y}px" width="{s}" height="{s}" viewBox="0 0 24 24"><path d="{IC[n]}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"/></svg>'
def ICIRC(n,cx,cy,r=15,col=INK,fill='#fff'):
    return S(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{col}" stroke-width="1"/>')+ICON(n,cx-r*.62,cy-r*.62,r*1.24,col)
def DONUT(cx,cy,r,p,col,lab,sub):
    a=math.radians(-90+360*p/100); x=cx+r*math.cos(a); y=cy+r*math.sin(a); lg=1 if p>50 else 0
    o=S(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{G4}" stroke-width="6"/><path d="M{cx},{cy-r} A{r},{r} 0 {lg} 1 {x:.1f},{y:.1f}" fill="none" stroke="{col}" stroke-width="6"/>')
    return o+T(cx-r,cy-7,f'{p}<span style="font-size:7px">%</span>',2*r,'nb','text-align:center;font-size:12px')+T(cx-40,cy+r+6,lab,80,'hs','text-align:center;font-size:7px;font-weight:700')+T(cx-40,cy+r+18,sub,80,'s','text-align:center;font-size:5.8px')
pages=[]

# ===== P02-03 =====
exec(P23.replace("pages.append(spread(b,2,3,'',''))","b+=LINE('M0,420 H1190',[(L+2,420),(R+2,420)])\npages.append(spread(b,2,3,'',''))").replace("b+=kick(L,438,","b+=kick(L,440,").replace("b+=kick(R,438,","b+=kick(R,440,"))

# ===== P04-05 第1章 =====
b=BGN(300,196,'01')+BGN(900,196,'01')
b+=tile(0,0,380,200,'r-022.png','50% 60%','三菱商事','')+tile(384,0,211,200,'mr_01_01@2x.webp','50% 60%','総合力','産業と地域をまたぐ',1400)
b+=tile(599,0,300,200,'r-047.png','60% 40%','原料炭','豪州')+tile(903,0,287,200,'mr_02_01@2x.webp','50% 50%','銅','南米',1400)
o,yy=head(L,222,'第1章','我々は何者か｜三菱商事とは','Who we are.','三綱領を精神の根幹に、「総合力」で価値を生む',size=40)
b+=o+para(L,yy+2,250,'三菱商事は三綱領を企業理念とし、事業を通じて経済価値・社会価値・環境価値の同時実現を目指しています。幅広い産業と地域にまたがる事業と人のつながり＝「総合力」が、三菱商事の強みです。')
ty=446
b+=T(L,ty,'三綱領',None,'k')+T(L+50,ty,'三菱商事の企業理念',None,'kj')
for i,(j,r_,e) in enumerate([('所期奉公','しょきほうこう','事業を通じ、物心共に豊かな社会の実現に努力すると同時に、かけがえのない地球環境の維持にも貢献する'),('処事光明','しょじこうめい','公明正大で品格のある行動を旨とし、活動の公開性、透明性を堅持する'),('立業貿易','りつぎょうぼうえき','全世界的、宇宙的視野に立脚した事業展開を図る')]):
    y=ty+20+i*76; b+=rule(L,y,210,INK if i==0 else G3,1 if i==0 else .6)+T(L,y+8,j,None,'h','font-size:16px')+T(L+80,y+13,r_,None,'l','font-size:6.2px;color:'+BR)+T(L,y+32,e,205,'s','font-size:6.6px')
# 総合力リング：中心＝三綱領、内環＝7グループ、外環＝産業・地域・機能
cx,cy,rr=440,572,112
o=(f'<defs><radialGradient id="glow"><stop offset="0" stop-color="{CU}" stop-opacity=".45"/><stop offset="1" stop-color="{CU}" stop-opacity="0"/></radialGradient></defs>'
   f'<circle cx="{cx}" cy="{cy}" r="{rr+34}" fill="none" stroke="{G4}" stroke-width="14"/>'
   f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="none" stroke="{G3}" stroke-width=".8" stroke-dasharray="2 3"/>'
   f'<circle cx="{cx}" cy="{cy}" r="70" fill="{PAN}"/><circle cx="{cx}" cy="{cy}" r="44" fill="#fff" stroke="{G3}" stroke-width=".6"/>')
for k in range(1,7):
    t=math.radians(k*360/7); x=cx+rr*math.cos(t); y=cy+rr*math.sin(t)
    o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="20" fill="#fff" stroke="{G2}" stroke-width=".8"/><circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{G3}"/>'
o+=f'<circle cx="{cx+rr}" cy="{cy}" r="46" fill="url(#glow)"/><circle cx="{cx+rr}" cy="{cy}" r="27" fill="{CU}" stroke="#fff" stroke-width="2"/>'
b+=S(o)
b+=LINE(f'M0,420 H{cx-120} C{cx-60},420 {cx-30},{cy-rr} {cx},{cy-rr} A{rr},{rr} 0 0 1 {cx+rr},{cy} C{cx+rr+60},{cy} 610,650 690,650 H1190',[(cx,cy-rr)])
for lab,a_ in (('産業',200),('地域',245),('機能',290)):
    t=math.radians(a_); b+=T(cx+(rr+34)*math.cos(t)-16,cy+(rr+34)*math.sin(t)-6,lab,32,'l','text-align:center;font-family:Noto Sans JP;font-weight:700;font-size:7px;color:'+G1)
b+=T(cx-44,cy-50,'三菱商事',88,'h','text-align:center;font-size:11px')+T(cx-40,cy-12,'三綱領',80,'nb','text-align:center;font-size:10px;font-family:Noto Sans JP')+T(cx-40,cy+4,'精神の根幹',80,'s','text-align:center;font-size:5.8px')+T(cx-44,cy+32,'7つの営業グループ',88,'s','text-align:center;font-size:5.8px')
b+=T(cx+rr-24,cy-8,'金属<br>資源',48,'l','text-align:center;color:#fff;font-family:Noto Sans JP;font-size:7px;font-weight:700;line-height:1.15')
b+=T(cx+rr-36,cy+34,'中核グループ',72,'k','text-align:center;color:'+CU)
b+=T(cx-150,cy+rr+44,'産業・地域・機能をまたぐ「総合力」の中で、金属資源グループは長年三菱商事を支えてきた中核グループの一つ。',300,'hs','text-align:center;font-size:8.2px;font-weight:700')
# right page
o,yy=head(R,222,'第1章','我々は何者か｜金属資源グループとは','The core that has<br>carried us.','三綱領を体現する中核グループとして',size=36)
b+=o+para(R,yy+2,W,'社会に不可欠な金属資源を世界から確保し、安定的に届けてきました。三綱領を事業で体現する中核グループとして、長年にわたり会社の屋台骨を支えています。')
py=yy+40
b+=A(R,py,'',W,'',f'height:70px;background:{INK}')+T(R+16,py+11,'グループミッション',None,'k','color:#e9d6ac')+T(R+16,py+27,'社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する',W-32,'hs','font-size:10px;line-height:1.5;color:#fff')
cy2=py+84
b+=T(R,cy2,'歩み',None,'k')+T(R+40,cy2,'先見性をもって先手を打ち、市況の波を越えて全社の利益を支えてきた',None,'kj')
# 事業モデルの進化（ストリーム図）
sx0,sx1,sb=R+60,R+W,612
xs_=[sx0+i*(sx1-sx0)/4 for i in range(5)]
trd=[14,16,18,22,26]; inv=[2,10,22,30,36]
def area(base,vals,up):
    top=[(x,base-v) for x,v in zip(xs_,vals)]
    d='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in top)+f' L{sx1},{base} L{sx0},{base}Z'
    return d
o=''
tt=[(x,sb-v) for x,v in zip(xs_,trd)]; ii=[(x,sb-t-v) for x,t,v in zip(xs_,trd,inv)]
o+=f'<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in tt)+f' L{sx1},{sb} L{sx0},{sb}Z" fill="{NV}" opacity=".9"/>'
o+=f'<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in ii)+' L'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in reversed(tt))+f'Z" fill="{BR}" opacity=".9"/>'
b+=S(o)+T(R,sb-52,'事業の重心',56,'s','font-size:6px')+T(R,sb-38,'<span style="color:'+BR+'">■</span> 資源投資<br><span style="color:'+NV+'">■</span> トレーディング',58,'s','font-size:5.6px;line-height:1.6')
eras=[('1980〜90年代','日本の産業に、資源を。','トレーディングで参入し、少数出資から事業に関わる'),('1990年代','仲介から、担い手へ。','投資モデルへ転換し、JV運営の知見を蓄える'),('2000年代','一級資産に、早くから。','BHPと原料炭の合弁を組成し、事業経営に参画'),('2010年代','次の柱を、先回りして。','銅へ領域を広げ、販売機能をRtMに集約'),('2020年代〜','投資と販売を、一つの力に。','両輪を一体で動かす、グローバルな事業者へ')]
o=''
for i,(yr,th,ac) in enumerate(eras):
    x=R+64+i*96
    o+=f'<circle cx="{x}" cy="650" r="4" fill="{CU if i in (2,3) else INK}" stroke="#fff" stroke-width="1"/>'
    b+=T(x-4,622,yr,None,'nb','font-size:11px')+T(x-4,664,th,92,'hs','font-size:8px;font-weight:700')+T(x-4,692,ac,90,'s','font-size:6.2px')
b+=S(o)
b+=rule(R,752,W,G3)+T(R,762,'事業領域',None,'k')+T(R+64,760,'<b style="color:'+CU+'">原料炭　銅</b>　鉄鉱石　ニッケル　リチウム　アルミ・ボーキサイト　肥料資源　二次資源',W-64,'hs','font-size:8.6px;letter-spacing:.6px')
b+=BAND(0,824,1190,18)
pages.append(spread(b,4,5,'',''))

# ===== P06-07 第2章 導入 =====
xs=[0,238,476,714,952]; tw=234
stg=[('x_vc_mine.jpg','01 川上','鉱山・資源開発'),('_mr_project_06.png','02 中間流通','トレーディング'),('x_vc_smelter.jpg','03 川中','製錬・製鉄'),('r-072.png','04 中間流通','トレーディング'),('x_vc_ev.jpg','05 川下','需要家・最終製品')]
b=BGN(330,352,'02')+BGN(780,352,'02')
for (f,e,j),x in zip(stg,xs): b+=tile(x,0,tw if x<952 else 238,330,f,'50% 50%',e,j)
roles=[('資源投資',BR),('トレーディング',NV),('資源投資',BR),('トレーディング',NV),('需要家',G2)]
for (t_,col),x in zip(roles,xs): b+=A(x,334,f'<div style="font-family:Noto Sans JP;font-weight:700;font-size:7.4px;color:#fff;padding:3px 10px">{t_}</div>',tw if x<952 else 238,'',f'height:18px;background:{col}')
o,yy=head(L,372,'第2章','独自価値｜投資とトレーディングの両輪','Two wheels,<br>one flow.','資源の流れ全体に関わり、互いを強め合ってきた',size=44)
b+=o
b+=para(R,380,250,'投資とトレーディングの両輪で、資源の流れ全体に関わる。互いを強め合いながら、長い時間をかけて積み重ねてきたこと。それが、鉱山会社でも純粋なトレーダーでもない、金属資源グループならではの強さです。')
# 両輪の循環（大）
ccx,ccy,cr=R+400,464,52
o=(f'<circle cx="{ccx}" cy="{ccy}" r="{cr+20}" fill="none" stroke="{CU}" stroke-width=".8" stroke-dasharray="1 4"/>'
   f'<path d="M{ccx-cr},{ccy} A{cr},{cr} 0 0 1 {ccx+cr},{ccy}" fill="none" stroke="{BR}" stroke-width="12"/>'
   f'<path d="M{ccx+cr},{ccy} A{cr},{cr} 0 0 1 {ccx-cr},{ccy}" fill="none" stroke="{NV}" stroke-width="12"/>'
   f'<path d="M{ccx+cr-12},{ccy-8} L{ccx+cr},{ccy+10} L{ccx+cr+12},{ccy-8}Z" fill="{BR}"/><path d="M{ccx-cr-12},{ccy+8} L{ccx-cr},{ccy-10} L{ccx-cr+12},{ccy+8}Z" fill="{NV}"/>'
   f'<circle cx="{ccx}" cy="{ccy}" r="40" fill="{PAN}"/>')
t=math.radians(-35); o+=f'<circle cx="{ccx+(cr+20)*math.cos(t):.1f}" cy="{ccy+(cr+20)*math.sin(t):.1f}" r="5" fill="{CU}"/>'
b+=S(o)
b+=ICON('mine',ccx-9,ccy-cr-32,18,BR)+T(ccx-60,ccy-cr-50,'資源投資',120,'h','text-align:center;font-size:9.5px;color:'+BR)
b+=ICON('ship',ccx-9,ccy+cr+14,18,NV)+T(ccx-60,ccy+cr+34,'トレーディング',120,'h','text-align:center;font-size:9.5px;color:'+NV)
b+=T(ccx-36,ccy-16,'互いを<br>強め合う',72,'hs','text-align:center;font-size:8.6px;font-weight:700;line-height:1.35')
b+=T(ccx+cr+16,ccy-62,'新技術が<br>流れを進化',60,'s','font-size:5.8px;color:'+CU)
b+=T(ccx-cr-118,ccy-40,'投資で得た資源を<br>市場へ届ける',100,'s','text-align:right;color:'+BR)+T(ccx+cr+22,ccy+26,'市場の情報を<br>投資判断へ',90,'s','color:'+NV)
cards=[('A','link','持つ力・つなぐ力','投資とトレーディングの両輪','資源に投資して育てる力と、市場へ届ける力の両方を持つ。',BR),
       ('B','recycle','互いを強め合う','一方通行ではない循環','市場の情報を投資判断に生かし、投資の資源を市場へ届ける。',NV),
       ('C','flask','流れ全体を進化させる','新技術への投資','業界の課題に挑む技術に投資し、知見を両輪に還元する。',CU),
       ('D','time','長い時間をかけて','積み重ねが先見性に','市況の浮き沈みに左右されず、流れに関わり続けてきた。',INK),
       ('E','target','その結果としての、いま','原料炭・銅・トレーディング','強みがあることの「結果」として、いまの主力事業がある。→ P.08',RED)]
for i,(k_,ic,e,j,d_,col) in enumerate(cards):
    x=L+i*232
    b+=ICIRC(ic,x+190,602,15,col)
    b+=T(x,586,e,180,'h','font-size:12px')+T(x,608,j,180,'s','font-size:6.8px;color:'+col)
    b+=T(x,672,d_,200,'b','font-size:7.2px;line-height:1.8')
b+=LINE('M0,650 H1190')
for i,(k_,*_r,col) in enumerate(cards): b+=badge(L+i*232,641,k_,col,18)
b+=rule(L,730,1110,G3)+T(L,744,'Not a miner. Not just a trader.',700,'dl','font-size:30px;color:'+G1)+T(R+115,752,'鉱山会社でも、純粋なトレーダーでもない。',400,'h','font-size:13px;text-align:right')
b+=BAND(0,824,1190,18)
pages.append(spread(b,6,7,'',''))

# ===== P08-09 主力3事業＋新技術 =====
b=BGN(330,210,'02',260)+BGN(930,210,'02',260)
b+=tile(0,0,305,206,'r-047.png','60% 40%')+tile(309,0,286,206,'mr_02_01@2x.webp','50% 50%',mx=1400)+tile(599,0,591,206,'r-023.png','50% 60%')
b+=shade(0,0,1190,206)
for x,k1,big,sub in [(L,'PILLAR 1　原料炭事業','約50%','BMAが一級強粘炭の<br>世界供給に占めるシェア'),(L+284,'PILLAR 2　銅事業','日本最大','銅の持分生産量'),(R,'PILLAR 3　トレーディング事業（RtM）','15 × 50 × 1,000','業界 × カ国 × 販売先')]:
    b+=T(x,24,k1,None,'k','color:#e9d6ac')+T(x,140,big,None,'nb','font-size:40px;color:#fff')+T(x,182,sub,240,'hs','color:#fff;font-size:7.4px')
cols=[(L,256),(L+284,256),(R,W)]
x,w=cols[0]
b+=T(x,222,'World-class<br>metallurgical coal.',w,'d','font-size:20px')+lead(x,266,'社会に欠かせない資源を、世界最高品位で',w,9.2)
b+=DONUT(x+40,318,20,80,INK,'MARKET','上位5社で寡占')+DONUT(x+128,318,20,50,BR,'SCALE','一級強粘炭のBMAシェア')
b+=T(x+178,300,'5<span style="font-size:10px">/7</span>',None,'nb','font-size:24px;color:'+BR)+T(x+176,344,'QUALITY',80,'hs','font-size:7px;font-weight:700')+T(x+176,356,'高品位の5炭鉱に集約',80,'s','font-size:5.8px')
mx,my,mw,mh=x,384,w,140
b+=A(mx,my,'',mw,'',f'height:{mh}px;background:{PAN}')
LO0,LO1,LA0,LA1=147.5,151.4,-20.9,-23.9
Q=lambda lo,la:(mx+8+(lo-LO0)/(LO1-LO0)*(mw*0.62), my+16+(LA0-la)/(LA0-LA1)*(mh-24))
coast=[(149.0,-20.9),(149.2,-21.25),(149.4,-21.6),(149.75,-22.1),(150.2,-22.4),(150.7,-22.75),(150.85,-23.3),(151.3,-23.9)]
o='<polygon points="'+' '.join(f'{Q(*c)[0]:.1f},{Q(*c)[1]:.1f}' for c in coast)+f' {Q(151.4,-23.9)[0]:.1f},{my+mh} {Q(151.4,-20.9)[0]:.1f},{my} " fill="#dfe6ec"/>'
mines=[('Broadmeadow',148.08,-21.55,1),('Goonyella Riverside',147.98,-21.75,1),('Caval Ridge',148.05,-22.12,1),('Peak Downs',148.2,-22.25,1),('Saraji',148.3,-22.45,1),('Daunia',148.35,-22.0,0),('Blackwater',148.85,-23.55,0)]
hp=Q(149.29,-21.28); gl=Q(151.25,-23.85)
for path in ([(148.08,-21.55),(147.98,-21.75),(148.3,-21.6),(149.29,-21.28)],[(148.3,-22.45),(148.2,-22.25),(148.05,-22.12),(148.3,-21.6)],[(148.85,-23.55),(150.1,-23.6),(151.25,-23.85)]):
    o+='<polyline points="'+' '.join(f'{Q(*c)[0]:.1f},{Q(*c)[1]:.1f}' for c in path)+f'" fill="none" stroke="{RED}" stroke-width="1.1" stroke-dasharray="4 2"/>'
lx=mx+mw*0.66
for k_,(n,lo,la,keep) in enumerate(mines):
    X_,Y_=Q(lo,la); ly=my+20+k_*14
    o+=f'<path d="M{X_:.1f},{Y_:.1f} L{lx-4:.1f},{ly+3}" stroke="{G3}" stroke-width=".5"/>'
    o+=(f'<circle cx="{X_:.1f}" cy="{Y_:.1f}" r="3.4" fill="{BR}" stroke="#fff" stroke-width=".8"/>' if keep else f'<circle cx="{X_:.1f}" cy="{Y_:.1f}" r="3" fill="#fff" stroke="{G2}" stroke-width=".9"/>')
    b+=T(lx,ly-2,n+('' if keep else '（売却）'),mw*0.34,'s',f'font-size:5.4px;font-family:IN;color:{INK if keep else G2}')
for (px,py_),n in ((hp,'ヘイポイント港'),(gl,'グラッドストーン港')):
    o+=f'<rect x="{px-3.5:.1f}" y="{py_-3.5:.1f}" width="7" height="7" fill="{INK}"/>'
    b+=T(px+6,py_-4,n,None,'s','font-size:5.4px;color:'+INK)
b+=S(o)
b+=T(mx+8,my+5,'ボーエン・ベースン｜BMA＝MDP 50%：BHP 50%',None,'k','font-size:5.6px')
b+=T(mx+8,my+mh-14,f'<span style="color:{BR}">●</span> 保有5炭鉱　○ 売却した中品位2炭鉱　<span style="color:{RED}">- -</span> 鉄道　■ 港湾',w,'s','font-size:5.3px')
# (出資構成は地図タイトルへ)
# copper
x,w=cols[1]
b+=T(x,222,'The partner the copper<br>industry calls first.',w+12,'d','font-size:20px')+lead(x,266,'業界から最初に声がかかる、日本最大の生産者',w,9.2)
b+=DONUT(x+40,318,20,25,INK,'MARKET','上位5社でも約25%')
b+=ICON('link',x+110,300,30,BR)+T(x+88,344,'SCALE',80,'hs','text-align:center;font-size:7px;font-weight:700')+T(x+88,356,'主要メジャーの多くとJV',80,'s','text-align:center;font-size:5.8px')
o=''
for i in range(12):
    h=6+i*2.2; o+=f'<rect x="{x+184+i*5.6:.1f}" y="{334-h:.1f}" width="4.6" height="{h:.1f}" fill="{BR if i<3 else G3}"/>'
b+=S(o)+T(x+178,344,'QUALITY',80,'hs','font-size:7px;font-weight:700')+T(x+178,356,'コストは世界上位25%',80,'s','font-size:5.8px')
vy=384
b+=A(x,vy,'',w,'',f'height:150px;background:{PAN}')
b+=T(x+10,vy+8,'世界の鉱山別生産量 Top15 のうち、5鉱山に参画',w-20,'k','font-size:5.6px')
own={1:'Escondida',4:'Antamina',10:'AA Sur',12:'Los Pelambres',15:'Quellaveco'}
o=''
for r_ in range(1,16):
    cx_=x+16+(r_-1)*16; me=r_ in own
    o+=f'<circle cx="{cx_}" cy="{vy+38}" r="6.4" fill="{BR if me else "#fff"}" stroke="{BR if me else G3}" stroke-width=".8"/>'
    b+=T(cx_-8,vy+34,str(r_),16,'l',f'text-align:center;font-size:5.4px;color:{"#fff" if me else G2}')
b+=S(o)
for k_,(r_,n) in enumerate(own.items()):
    y=vy+56+k_*14; b+=T(x+10,y,f'<b style="font-family:IT;font-weight:600;color:{BR};font-size:9px">{r_}位</b>　<b style="font-family:IN;font-weight:600;color:{INK}">{n}</b>　<span>{["チリ","ペルー","チリ","チリ","ペルー"][k_]}・出資{["8.25%","10%","20.44%","5%","40%"][k_]}</span>',w-20,'s','font-size:6.2px')
b+=T(x+10,vy+130,'開発中：Marimaca（チリ）・Copper World（米国）',w-20,'s','font-size:5.8px')
# trading
x,w=cols[2]
b+=T(x,222,'Resource to Market.',w,'d','font-size:20px')+lead(x,248,'資源と市場をつなぎ、必要な場所へ確かに届ける',w,9.2)
pts3=[('第三者の資源も扱う','市場の生きた情報を、投資の側へ返す'),('ロジ・在庫・ヘッジ','機能を付けて、顧客に届ける'),('グローバルな販売網','欧州・シンガポール・米州の顧客へ')]
for i,(h_,d_) in enumerate(pts3):
    y=284+i*38; b+=rule(x,y,236)+T(x,y+6,f'0{i+1}',None,'nb','font-size:13px;color:'+NV)+T(x+24,y+7,h_,210,'hs','font-size:8.6px;font-weight:700')+T(x+24,y+21,d_,210,'s')
b+=T(x,406,'多様な取引機能',None,'k','color:'+NV)
for i,(ic,t) in enumerate([('grid','取扱商品の広さ'),('box','在庫'),('truck','輸送手配'),('hedge','ヘッジ')]):
    xx=x+i*60; b+=A(xx,420,'',54,'',f'height:62px;background:{PAN};border-top:1.4px solid {NV}')+ICON(ic,xx+16,428,22,NV)+T(xx,456,t,54,'s','text-align:center;font-size:5.8px;color:'+INK)
# RtM hub
hx=x+262; hw=W-262; hc=hx+hw/2
b+=A(hx,282,'<div class="l" style="font-size:6.4px">第三者の資源</div>',112,'',f'height:24px;border:1px solid {G2};display:flex;align-items:center;justify-content:center;background:#fff')
b+=A(hx+hw-112,282,'<div class="l" style="font-size:6.4px;color:'+BR+'">三菱商事の保有資産</div>',112,'',f'height:24px;border:1px solid {BR};display:flex;align-items:center;justify-content:center;background:#fff')
o=(f'<circle cx="{hc}" cy="382" r="54" fill="none" stroke="{NVL}" stroke-width=".8" stroke-dasharray="2 3"/><circle cx="{hc}" cy="382" r="34" fill="{NV}"/>'
   +arrow(hx+56,306,hc-20,352,NV)+arrow(hx+hw-56,306,hc+20,352,NV)
   +arrow(hc,416,hc,444,NV))
for k_,a_ in enumerate((200,240,300,340)):
    t=math.radians(a_); o+=f'<circle cx="{hc+54*math.cos(t):.1f}" cy="{382+54*math.sin(t):.1f}" r="3" fill="{NV}"/>'
o+=f'<path d="M{hc+90},{460} C{hc+125},{420} {hc+125},{330} {hx+hw-40},{310}" fill="none" stroke="{BR}" stroke-width=".9" stroke-dasharray="3 2"/>'+arrow(hx+hw-34,316,hx+hw-40,308,BR)
b+=S(o)+T(hc-34,370,'RtM',68,'nb','text-align:center;font-size:16px;color:#fff')+T(hc-34,388,'Resource to Market',68,'s','text-align:center;font-size:5px;color:#c9d6e3;font-family:IN')
b+=T(hc+86,382,'市場の情報',None,'s','font-size:5.8px;color:'+BR)
for k_,rg in enumerate(['欧州','アジア','米州']):
    b+=A(hx+k_*(hw/3)+4,448,f'<div class="l" style="font-size:6.4px">{rg}</div>',hw/3-8,'',f'height:22px;border:1px solid {INK};display:flex;align-items:center;justify-content:center;background:#fff')
b+=T(hx,474,'世界の顧客（15業界・50カ国・約1,000社）',hw,'s','text-align:center;font-size:5.8px')
# NEW TECH
ny=540
b+=A(0,ny,'',1190,'',f'height:284px;background:{PAN}')
b+=T(L,ny+16,'NEW TECHNOLOGY　新技術',None,'k')+T(L,ny+36,"Investing in what's next.",300,'d','font-size:22px')+T(L,ny+64,'資源業界のボトルネックに、新しい技術で挑む',300,'h','font-size:9.4px')
b+=para(L,ny+132,250,'業界の課題を見極め、課題を解く技術を持つスタートアップに出資。トレーディングと業界とのつながりを生かして現場に取り入れ、その知見を既存事業の高度化に還元しています。','font-size:6.9px')
b+=LINE('M0,650 H1190')
st=[('mine','鉱石','Cu 約1%',8),('flask','銅精鉱','Cu 20〜30%',24),('factory','銅地金','Cu 99.99%',40),('bolt','最終用途','電化・インフラ',0),('recycle','リサイクル','再び供給へ',0)]
cx0=L+320; o=''
for i,(ic,e,g_,h) in enumerate(st):
    xx=cx0+i*104
    b+=T(xx-40,ny+12,e,80,'h','text-align:center;font-size:10px')
    if h:
        o+=f'<rect x="{xx-9}" y="{628-h}" width="18" height="{h}" fill="{CU}" opacity=".85"/>'
        b+=T(xx-40,628-h-14,g_,80,'nb','text-align:center;font-size:8.6px;color:'+CU)
    else: b+=T(xx-40,600,g_,80,'s','text-align:center;font-size:6.6px;color:'+CU)
    if i<4: o+=arrow(xx+20,650,xx+82,650,INK,.9)
b+=S(o)
for i,(ic,*_r) in enumerate(st): b+=ICIRC(ic,cx0+i*104,650,16,INK)
b+=T(cx0-60,ny+40,'銅の品位',None,'k','font-size:5.6px')
techs=[(0,'CiDRA','選鉱','浮遊選鉱を高度化し、回収率と処理能力を高める'),(1,'Jetti','浸出','新たな触媒で、硫化鉱から銅を回収する'),(4,'DESCycle','リサイクル','電子スクラップから銅・貴金属を回収する')]
o=''
for k_,(si,n,t_,d_) in enumerate(techs):
    xx=cx0-40+k_*170; sx=cx0+si*104+(18 if si==0 else 0)
    o+=f'<path d="M{sx},666 V684 H{xx+14} V700" fill="none" stroke="{CU}" stroke-width=".9"/><circle cx="{sx}" cy="666" r="2.4" fill="{CU}"/>'
    b+=A(xx,700,f'<div style="font-family:IN;font-weight:600;font-size:5.8px;letter-spacing:1.2px;color:{CU}">{t_}｜スタートアップ</div><div class="l" style="font-weight:600;font-size:11px;margin-top:2px">{n}</div><div class="s" style="margin-top:2px">{d_}</div>',160,'',f'height:64px;padding:8px 10px;border-top:2px solid {CU};background:#fff')
b+=S(o)
jx=900; jw=1150-jx
b+=A(jx,ny+16,'',jw,'',f'height:254px;background:#fff')
b+=T(jx+14,ny+28,'取り組み事例',None,'k','color:'+CU)
b+=A(jx+14,ny+44,'<div class="l" style="font-size:9px;font-weight:600">Jetti</div><div class="s" style="font-size:5.6px">銅生産の革新技術</div>',92,'',f'height:36px;border:1px solid {CU};display:flex;flex-direction:column;align-items:center;justify-content:center')
b+=T(jx+108,ny+52,'×',None,'','font-size:14px;color:'+CU)
b+=A(jx+130,ny+44,'<div class="l" style="font-size:9px;font-weight:600;font-family:Noto Sans JP">三菱商事</div><div class="s" style="font-size:5.6px">資源開発・トレーディング</div>',92,'',f'height:36px;border:1px solid {INK};display:flex;flex-direction:column;align-items:center;justify-content:center')
b+=T(jx+14,ny+86,'価値共創',jw-28,'k','text-align:center;color:'+CU)
b+=tile(jx+14,ny+100,jw-28,56,'x_case_smelt.jpg','50% 50%')
b+=para(jx+14,ny+164,jw-28,'米Jettiに出資参画し、事業拡大を支援。同社技術で生産される環境価値の高い銅地金を販売するほか、低品位の鉱石に課題を抱える鉱山への技術導入を共同で検討しています。','font-size:6.7px')
b+=BAND(0,824,1190,18)
pages.append(spread(b,8,9,'',''))

# ===== P10-11 =====
b=BGN(330,286,'03')+BGN(930,180,'04')
b+=tile(0,0,595,280,'r-084.png','50% 35%','パートナーシップ','')+tile(599,0,591,170,'r-075.png','50% 55%','社会を支える資源','')
o,yy=head(L,296,'第3章','選ばれ続ける理由','Partner of choice.','資源業界に不可欠な存在として、選ばれ続ける',size=36)
b+=o
four=[('people','企業文化的親和性','資源メジャーと同じ、中長期の視座'),('chart','JV経営力','実質的な経営貢献と、高い目利き力'),('shield','健全な財務基盤','リスクを分かち合える体力'),('eye','深い知見','マクロ環境とバリューチェーンへの理解')]
for i,(ic,e,d_) in enumerate(four):
    x=L+(i%2)*262; y=yy+6+(i//2)*40
    b+=ICIRC(ic,x+14,y+14,14,BR)+T(x+36,y+2,e,220,'hs','font-size:9px;font-weight:700')+T(x+36,y+17,d_,220,'s','font-size:6.6px')
# JVへの貢献：三菱商事 → 経営／現場 → JV
fy=yy+92; jy=fy+62
b+=T(L,fy,'JVへの貢献',None,'k')+T(L+70,fy,'経営から現場まで伴走する',None,'kj')
ax,bx2=L+36,L+W-36
o=(f'<path d="M{ax},{jy} C{ax+120},{jy-58} {bx2-120},{jy-58} {bx2},{jy}" fill="none" stroke="{BR}" stroke-width="2"/>'
   f'<path d="M{ax},{jy} C{ax+120},{jy+58} {bx2-120},{jy+58} {bx2},{jy}" fill="none" stroke="{BR}" stroke-width="2" stroke-dasharray="5 3"/>'
   f'<circle cx="{ax}" cy="{jy}" r="26" fill="{INK}"/><circle cx="{bx2}" cy="{jy}" r="26" fill="#fff" stroke="{INK}" stroke-width="1.2"/>')
b+=S(o)+T(ax-26,jy-6,'三菱商事',52,'l','text-align:center;color:#fff;font-family:Noto Sans JP;font-size:6.6px;font-weight:700')+T(bx2-26,jy-6,'JV',52,'nb','text-align:center;font-size:11px')
for k_,t_ in enumerate(['中長期計画','資本政策','販売戦略']):
    b+=A(L+124+k_*92,jy-46,f'<div class="s" style="font-size:6.2px;color:{INK}">{t_}</div>',84,'',f'height:16px;border-radius:8px;background:#fff;border:.8px solid {BR};display:flex;align-items:center;justify-content:center')
for k_,t_ in enumerate(['人材派遣','操業支援','ベストプラクティス']):
    b+=A(L+124+k_*92,jy+30,f'<div class="s" style="font-size:6.2px;color:{INK}">{t_}</div>',84,'',f'height:16px;border-radius:8px;background:{PAN};border:.8px solid {BR};display:flex;align-items:center;justify-content:center')
b+=T(L+206,jy-28,'経営',None,'h','font-size:9px;color:'+BR)+T(L+206,jy+12,'現場',None,'h','font-size:9px;color:'+BR)
b+=LINE('M0,650 H595 C620,650 640,700 660,712',[])
for x,t_ in [(L,'会社対会社の関係へ'),(L+178,'新たな協業が生まれる'),(L+356,'積み重ねが、強み・信頼に')]:
    b+=A(x,636,f'<div class="hs" style="font-size:8.6px;font-weight:700">{t_}</div>',160,'',f'height:28px;border:1.2px solid {CU};background:#fff;display:flex;align-items:center;justify-content:center')
b+=T(L,684,'資源メジャー各社と、単なる共同出資を越えた「会社対会社」の関係へ。新たな協業が生まれ、その積み重ねが、さらなる強み・知見・信頼につながる。',W,'b','font-size:7.2px')
b+=T(L,730,'主なJVパートナー',None,'k')+T(L+90,726,'BHP　　Rio Tinto　　Anglo American',None,'nb','font-size:15px')
# P11
o,yy=head(R,186,'第4章','何を実現するか','Building the future<br>of resources, together.','社会の「当たり前」を、支え続ける',size=30)
b+=o
env=[('chart','産業構造の転換','電化・AI・データセンターで、素材の需要が拡大'),('lock','供給制約の深刻化','良質な資源の開発が、より難しく'),('alert','地政学リスクの常態化','資源の囲い込みが、供給網に影響')]
for i,(ic,e,d_) in enumerate(env):
    x=R+i*176; b+=A(x,yy+6,'',166,'',f'height:62px;border-top:1.4px solid {INK};background:{PAN}')+ICON(ic,x+10,yy+16,22,INK)+T(x+40,yy+14,e,120,'hs','font-size:8.6px;font-weight:700')+T(x+40,yy+30,d_,120,'s','font-size:6.2px')
y2=yy+76
o=''.join(f'<path d="M{R+83+i*176},{y2} C{R+83+i*176},{y2+10} {R+W/2},{y2+8} {R+W/2},{y2+20}" fill="none" stroke="{INK}" stroke-width=".8"/>' for i in range(3))
b+=S(o)+A(R,y2+20,'<div class="hs" style="font-size:8.8px;font-weight:700;color:#fff;text-align:center">クリティカルミネラルの供給網確保が重要に。川上資源への参入障壁は高まる</div>',W,'',f'height:24px;padding:5px 10px;background:{INK}')
y3=y2+52
b+=S(chev(R+W/2,y3))
vc=y3+70; vx=R+W/2
o=(f'<circle cx="{vx-34}" cy="{vc}" r="50" fill="{BR}" opacity=".88"/><circle cx="{vx+34}" cy="{vc}" r="50" fill="{NV}" opacity=".88" style="mix-blend-mode:multiply"/>')
b+=S(o)
b+=T(vx-80,vc-6,'資源投資',56,'h','text-align:center;font-size:8.6px;color:#fff')+T(vx+24,vc-6,'トレー<br>ディング',56,'h','text-align:center;font-size:8px;color:#fff;line-height:1.25;margin-top:-6px')+T(vx-20,vc-6,'連携',40,'nb','text-align:center;font-size:9px;color:#fff;font-family:Noto Sans JP')
b+=T(R,vc-30,'大規模資産の持分を確保し、<br>成長領域に早くから参画',150,'s','text-align:right;font-size:6.6px;color:'+BR)
b+=T(R+W-150,vc-30,'権益の引き取りと外部調達で<br>安定供給の体制を確立',150,'s','font-size:6.6px;color:'+NV)
b+=T(R,vc+20,'安定供給',150,'h','text-align:right;font-size:11px')+T(R+W-150,vc+20,'効率的な供給',150,'h','font-size:11px')
b+=T(R,vc+64,'「金属＝経済活動を支える礎」。社会に必要な資源を支えることを、私たちの責務と考えています。',W,'h','font-size:10.2px;line-height:1.6;text-align:center')
b+=LINE('M660,712 H1150',[(1150,712)])
b+=A(R,724,'',W,'',f'height:92px;background:{INK}')
b+=T(R+18,734,'グループミッション｜共に、資源の未来を築く',None,'k','color:#e9d6ac')
b+=T(R+18,752,'社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する',W-36,'hs','font-size:10.4px;color:#fff;line-height:1.5')
b+=T(R+18,794,'To contribute to a better society by providing a stable supply of high-quality mineral resources, in a sustainable way.',W-36,'s','color:#9aa1a8;font-family:IN')
b+=BAND(0,824,1190,18)
pages.append(spread(b,10,11,'',''))

links=''.join(f'<link rel="stylesheet" href="f/nsjp/package/{w}.css">' for w in (400,500,700))
open('daiwari_v21.html','w').write('<!doctype html><meta charset=utf-8>'+links+'<style>'+CSS2+'</style>'+''.join(pages))
