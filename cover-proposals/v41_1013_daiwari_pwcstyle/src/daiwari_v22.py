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
NV='#3f464e'; NVL='#9aa1a8'
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


# ===== P08-09 主力3事業（3カラム）＋新技術 =====
def box(x,y,w,h,html,bd=G3,bg='#fff',cls='l',st=''):
    return A(x,y,html,w,'',f'height:{h}px;border:.8px solid {bd};background:{bg};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;{st}')
def msq3(x,y,w,rows,lw=54):
    o=''
    for i,(k_,v,d_) in enumerate(rows):
        yy=y+i*30; o+=rule(x,yy,w,INK if i==0 else G3,.9 if i==0 else .5)
        o+=T(x,yy+9,k_,None,'l','font-size:5.4px;letter-spacing:1.4px;color:'+G2)+T(x+lw,yy+5,v,w-lw,'hs','font-size:9.4px;font-weight:700')+T(x+lw,yy+18,d_,w-lw,'s','font-size:5.8px')
    return o+rule(x,y+len(rows)*30,w,G3,.5)
C1,C2,C3,CW_=40,429,818,332
b=BGN(300,520,'02',240)+BGN(890,520,'02',240)
b+=tile(0,0,392,170,'r-047.png','60% 40%','原料炭','豪州')+tile(399,0,392,170,'mr_02_01@2x.webp','50% 50%','銅','南米',1400)+tile(798,0,392,170,'r-023.png','50% 60%','トレーディング','')
def hd(x,k1,en,jt,w=CW_,size=21):
    return T(x,184,k1,None,'k')+T(x,198,en,w,'d',f'font-size:{size}px')+A(x,198+(en.count('<br>')+1)*size*1.05+8,'',22,'',f'border-top:1.4px solid {RED}')+T(x,198+(en.count('<br>')+1)*size*1.05+16,jt,w,'h','font-size:9px')
# --- 原料炭
b+=hd(C1,'PILLAR 1　原料炭事業','World-class metallurgical coal.','鉄の主原料“産業のコメ”を、世界最高品位で届ける')
b+=para(C1,252,CW_,'原料炭は鉄の主原料。BHPとの50:50の合弁BMAを通じ、豪州クイーンズランド州ボーエン・ベースンで世界最高品位の原料炭を生産。炭鉱から港湾・鉄道までを保有し、全体最適の操業で安定供給を実現しています。','font-size:6.8px')
b+=msq3(C1,296,CW_,[('MARKET','上位5社で約80%','寡占度が高く、供給は漸減'),('SCALE','BMAで約50%','一級強粘炭の世界供給に占めるシェア'),('QUALITY','高品位に集約','7炭鉱から高品位の5炭鉱へ。港湾・鉄道も自社保有')])
oy=398
b+=T(C1,oy,'出資構成',None,'k','font-size:5.6px')
b+=box(C1,oy+14,92,20,'<span class="l" style="font-size:6.6px;font-family:Noto Sans JP;font-weight:700">三菱商事</span>',INK)
b+=box(C1,oy+50,92,20,'<span class="l" style="font-size:7px">MDP</span>',INK)+box(C1+100,oy+50,30,20,'<span class="l" style="font-size:6px">BHP</span>',G2)
b+=box(C1,oy+90,130,26,'<span class="l" style="font-size:8px;font-weight:600">BMA</span><span class="s" style="font-size:5px">BHP Mitsubishi Alliance</span>',INK,PAN)
o=arrow(C1+46,oy+34,C1+46,oy+48,INK)+arrow(C1+46,oy+70,C1+46,oy+88,INK)+arrow(C1+115,oy+70,C1+115,oy+88,G2)
b+=S(o)+T(C1+50,oy+38,'100%',None,'s','font-size:5.4px')+T(C1+50,oy+74,'50%',None,'s','font-size:5.4px')+T(C1+119,oy+74,'50%',None,'s','font-size:5.4px')
# map
mx,my,mw,mh=C1+146,oy,CW_-146,122
b+=A(mx,my,'',mw,'',f'height:{mh}px;background:{PAN}')
LO0,LO1,LA0,LA1=147.6,151.4,-20.9,-23.9
Q=lambda lo,la:(mx+6+(lo-LO0)/(LO1-LO0)*(mw*0.62), my+14+(LA0-la)/(LA0-LA1)*(mh-22))
coast=[(149.0,-20.9),(149.2,-21.25),(149.4,-21.6),(149.75,-22.1),(150.2,-22.4),(150.7,-22.75),(150.85,-23.3),(151.3,-23.9)]
b+=S('<polygon points="'+' '.join(f'{Q(*c)[0]:.1f},{Q(*c)[1]:.1f}' for c in coast)+f' {Q(151.4,-23.9)[0]:.1f},{my+mh} {Q(151.4,-20.9)[0]:.1f},{my} " fill="#e8ecef"/>')
o=''
mines=[('Broadmeadow',148.08,-21.55,1),('Goonyella Riverside',147.98,-21.75,1),('Caval Ridge',148.05,-22.12,1),('Peak Downs',148.2,-22.25,1),('Saraji',148.3,-22.45,1),('Daunia',148.35,-22.0,0),('Blackwater',148.85,-23.55,0)]
hp=Q(149.29,-21.28); gl=Q(151.25,-23.85)
for path in ([(148.08,-21.55),(147.98,-21.75),(148.3,-21.6),(149.29,-21.28)],[(148.3,-22.45),(148.2,-22.25),(148.05,-22.12),(148.3,-21.6)],[(148.85,-23.55),(150.1,-23.6),(151.25,-23.85)]):
    o+='<polyline points="'+' '.join(f'{Q(*c)[0]:.1f},{Q(*c)[1]:.1f}' for c in path)+f'" fill="none" stroke="{G1}" stroke-width="1" stroke-dasharray="3 2"/>'
lx=mx+mw*0.6; LB=[]
for k_,(n,lo,la,keep) in enumerate(mines):
    X_,Y_=Q(lo,la); ly=my+16+k_*12
    o+=f'<path d="M{X_:.1f},{Y_:.1f} L{lx-3:.1f},{ly+3}" stroke="{G3}" stroke-width=".5"/>'
    o+=(f'<circle cx="{X_:.1f}" cy="{Y_:.1f}" r="3" fill="{BR}" stroke="#fff" stroke-width=".7"/>' if keep else f'<circle cx="{X_:.1f}" cy="{Y_:.1f}" r="2.6" fill="#fff" stroke="{G2}" stroke-width=".8"/>')
    LB.append((lx,ly-2,n+('' if keep else '（売却）'),keep))
for (px,py_),n in ((hp,'ヘイポイント港'),(gl,'グラッドストーン港')):
    o+=f'<rect x="{px-3:.1f}" y="{py_-3:.1f}" width="6" height="6" fill="{INK}"/>'
    LB.append((px+5,py_-4,n,2))
b+=S(o)
for x_,y_,t_,k_ in LB: b+=T(x_,y_,t_,None,'s',f'font-size:5px;font-family:IN;white-space:nowrap;color:{INK if k_ else G2}')+T(mx+6,my+4,'ボーエン・ベースン（クイーンズランド州）',None,'k','font-size:5.2px')
b+=T(mx+6,my+mh-11,f'<span style="color:{BR}">●</span>操業中　○売却（中低品位）　- -鉄道　■港湾',mw,'s','font-size:5px')
# --- 銅（ノドをまたぐため左右2段に分割）
cl,cr_=C2,607; sw_=154
b+=hd(cl,'PILLAR 2　銅事業','The partner<br>the copper industry<br>calls first.','日本最大の銅生産者として、業界から声がかかる',sw_,17)
b+=para(cl,306,sw_,'電化や再エネ、AI・データセンターの広がりを背景に、銅の需要は拡大を続けています。主要メジャー各社との協業を通じ、世界最大級の銅ポジションを築いています。','font-size:6.6px')
b+=msq3(cl,372,sw_,[('MARKET','上位5社で約25%','寡占化が進まず再編の機運'),('SCALE','持分生産量で日本最大','パートナー型の生産者'),('QUALITY','5鉱山すべて世界Top15','平均コストは世界上位25%')],44)
# 早期の参画（縦タイムライン）
b+=T(cr_,184,'早期の参画',None,'k')+T(cr_,196,'主要銅鉱山への参画年',None,'kj')
tl=[(1988,'Escondida','チリ'),(1997,'Los Pelambres','チリ'),(1999,'Antamina','ペルー'),(2011,'Anglo American Sur','チリ'),(2011,'Quellaveco','ペルー'),(2023,'Marimaca','チリ・開発中'),(2025,'Copper World','米国・開発中')]
o=f'<line x1="{cr_+30}" y1="214" x2="{cr_+30}" y2="{214+6*17+6}" stroke="{INK}" stroke-width=".8"/>'
for i,(yr,n,c) in enumerate(tl):
    y=216+i*17; dev='開発' in c
    o+=f'<circle cx="{cr_+30}" cy="{y+4}" r="3" fill="{"#fff" if dev else BR}" stroke="{BR}" stroke-width=".9"/>'
    b+=T(cr_,y,str(yr),None,'l','font-size:6px;color:'+G1)+T(cr_+38,y-1,f'<b style="font-family:IN;font-weight:600;color:{INK}">{n}</b><br><span>{c}</span>',120,'s','font-size:5.4px;line-height:1.25')
b+=S(o)
# 参画鉱山の表
ty_=346
b+=T(cr_,ty_,'参画鉱山',None,'k')+T(cr_+50,ty_,'鉱山別生産量ランキング／出資比率',None,'kj')
rows=[('Escondida','チリ','1位','8.25%'),('Los Pelambres','チリ','12位','5%'),('AA Sur','チリ','10位','20.44%'),('Marimaca','チリ','開発中','5%'),('Antamina','ペルー','4位','10%'),('Quellaveco','ペルー','15位','40%'),('Copper World','米国','開発中','30%')]
b+=T(cr_,ty_+16,'鉱山',None,'l','font-size:5.2px;color:'+G2)+T(cr_+66,ty_+16,'国',None,'l','font-size:5.2px;color:'+G2)+T(cr_+92,ty_+16,'順位',None,'l','font-size:5.2px;color:'+G2)+T(cr_+124,ty_+16,'出資',None,'l','font-size:5.2px;color:'+G2)
for i,(n,c,r_,p) in enumerate(rows):
    y=ty_+28+i*15; b+=rule(cr_,y,sw_,G3,.5)+T(cr_,y+4,n,66,'l','font-size:5.8px;font-weight:600')+T(cr_+66,y+4,c,None,'s','font-size:5.6px')+T(cr_+92,y+3,r_,None,'nb',f'font-size:7.4px;color:{BR if "位" in r_ else G2}')+T(cr_+124,y+4,p,None,'l','font-size:5.8px')
b+=rule(cr_,ty_+28+7*15,sw_,INK,.8)
# --- トレーディング
b+=hd(C3,'PILLAR 3　トレーディング事業（RtM）','Resource to Market.','一つの商品の中で、投資から販売までを一気通貫でつなぐ')
for i,(n,e,j) in enumerate([('15','INDUSTRIES','業界に販売'),('50','COUNTRIES','カ国に販売'),('〜1,000','CUSTOMERS','社の販売先')]):
    x=C3+i*112; b+=rule(x,252,100,INK,.9)+T(x,258,n,None,'n','font-size:22px')+T(x,284,e,None,'l','font-size:5px;letter-spacing:1.2px;color:'+BR)+T(x,292,j,None,'s','font-size:5.6px')
# RtM事業のビジネスモデル（PwC資料の図を整理）
by=312; bx=C3; bw=CW_
b+=T(bx,by,'RtM事業のビジネスモデル',None,'k')
b+=box(bx+60,by+14,bw-120,18,'<span class="l" style="font-size:6.8px;font-family:Noto Sans JP;font-weight:700">三菱商事</span>',INK)
b+=box(bx+60,by+38,(bw-130)/2,16,'<span class="s" style="font-size:5.8px;color:'+INK+'">第三者取引</span>',G2)+box(bx+70+(bw-130)/2,by+38,(bw-130)/2,16,'<span class="s" style="font-size:5.8px;color:'+INK+'">MC保有資産</span>',BR)
b+=box(bx+60,by+86,bw-120,24,'<span style="font-family:IT;font-weight:600;font-size:12px">RtM</span>',INK,PAN)
b+=box(bx+60,by+144,bw-120,18,'<span class="l" style="font-size:6.6px;font-family:Noto Sans JP;font-weight:700">顧客基盤</span>',INK)
o=arrow(bx+100,by+56,bx+100,by+84,INK)+arrow(bx+bw-100,by+84,bx+bw-100,by+56,BR)+arrow(bx+100,by+112,bx+100,by+142,INK)+arrow(bx+bw-100,by+142,bx+bw-100,by+112,BR)
b+=S(o)
b+=T(bx,by+62,'資源確保による<br>安定供給',92,'s','font-size:5.6px;text-align:right;color:'+INK)+T(bx+bw-92,by+60,'市場・業界動向の<br>発信と知見共有で<br>事業機会を発掘',92,'s','font-size:5.6px;color:'+BR)
b+=T(bx,by+118,'トレーディング機能<br>強化による継続的な<br>付加価値創出',92,'s','font-size:5.6px;text-align:right;color:'+INK)+T(bx+bw-92,by+118,'広い産業接点を<br>生かした<br>インテリジェンス',92,'s','font-size:5.6px;color:'+BR)
for i,t in enumerate(['Sustainability','Market Intelligence','Professionalism','Global Network']):
    b+=T(C3+i*84,by+170,t,80,'l','font-size:5.6px;font-weight:600;color:'+G1)
b+=T(C3,494,'多様な取引機能',None,'k')
for i,(ic,t) in enumerate([('grid','取扱商品の広さ'),('box','在庫'),('truck','輸送手配'),('hedge','ヘッジ')]):
    xx=C3+i*84; b+=A(xx,506,'',78,'',f'height:20px;border-top:.9px solid {INK};background:{PAN}')+ICON(ic,xx+4,508,14,G1)+T(xx+20,511,t,58,'s','font-size:5.8px;color:'+INK)
# ===== 新技術：銅バリューチェーン（PwC資料を整理）
ny=540
b+=A(0,ny,'',1190,'',f'height:284px;background:{PAN}')
b+=T(L,ny+18,'NEW TECHNOLOGY　新技術',None,'k')+T(L,ny+34,"Investing in<br>what's next.",250,'d','font-size:22px')+A(L,ny+86,'',22,'',f'border-top:1.4px solid {RED}')+T(L,ny+94,'業界のボトルネックに挑む新技術へ投資する',250,'h','font-size:9px')
b+=para(L,ny+116,240,'業界の課題を見極め、課題を解く技術を持つスタートアップに出資。トレーディングや業界とのつながりを生かして技術を現場に取り入れ、知見を既存事業の高度化に還元しています。','font-size:6.7px')
X0=300; X1=900
seg=[('Upstream',300,470,0),('Trading',472,520,1),('Midstream',522,708,0),('Trading',710,758,1),('Downstream',760,900,0)]
for n,a_,b_,tr in seg: b+=A(a_,ny+14,f'<span class="l" style="font-size:6px;color:{"#fff" if tr else INK}">{n}</span>',b_-a_,'',f'height:14px;background:{BR if tr else "#dfe3e7"};display:flex;align-items:center;justify-content:center')
# grade row
gy=ny+34
for x,t_ in [(330,'鉱石 Cu約1%'),(480,'銅精鉱 Cu20〜30%'),(612,'銅地金 Cu99.99%')]: b+=T(x,gy,t_,None,'l','font-size:6px;color:'+BR)
yb=ny+52
def pbox(x,y,w,h,t,sub=''): return A(x,y,f'<div class="l" style="font-size:6.8px;font-weight:600">{t}</div><div class="s" style="font-size:5.4px">{sub}</div>',w,'',f'height:{h}px;border:.8px solid {G2};background:#fff;padding:5px 6px')
b+=pbox(300,yb,104,200,'Mining','採掘')
for i,(n,p) in enumerate([('Escondida','8.25%'),('Los Pelambres','5%'),('AA Sur','20.44%'),('Antamina','10%'),('Quellaveco','40%'),('Marimaca','5%'),('Copper World','30%')]):
    b+=T(306,yb+30+i*14,f'<span style="color:{INK}">{n}</span>　<b style="color:{BR}">{p}</b>',96,'s','font-size:5.4px')
b+=pbox(470,yb,92,72,'Flotation','選鉱')+pbox(620,yb,92,72,'Smelting & Refining','製錬・精製')+pbox(470,yb+120,240,80,'Leaching','浸出（硫化鉱・酸化鉱）')+pbox(770,yb,130,200,'End Use','最終用途')
for i,t in enumerate(['Base Demand　基礎需要','Energy Transition　エネルギー転換','AI & Data Centers　AI・データセンター']):
    b+=T(778,yb+32+i*22,'— '+t,118,'s','font-size:5.6px;color:'+INK)
def vol(x,y,t): return A(x,y,f'<span class="l" style="font-size:6.4px;color:#fff;font-weight:600">{t}</span>',34,'',f'height:14px;background:{G1};display:flex;align-items:center;justify-content:center')
b+=vol(362,yb+182,'24Mt')+vol(522,yb+54,'21Mt')+vol(670,yb+182,'3Mt')+vol(860,yb+182,'28Mt')
o=(arrow(404,yb+30,468,yb+30,INK)+arrow(404,yb+150,468,yb+150,INK)+arrow(562,yb+30,618,yb+30,INK)+arrow(712,yb+30,768,yb+30,INK)+arrow(710,yb+150,768,yb+150,INK)
   +f'<path d="M835,{yb} V{yb-8} H700 V{yb-2}" fill="none" stroke="{BR}" stroke-width=".9"/>'+arrow(700,yb-6,700,yb-1,BR))
b+=S(o)
b+=T(410,yb+20,'硫化鉱',None,'s','font-size:5px')+T(410,yb+140,'酸化鉱・硫化鉱',None,'s','font-size:5px')+T(566,yb+20,'銅精鉱',None,'s','font-size:5px')+T(716,yb+20,'銅地金',None,'s','font-size:5px')+T(716,yb+140,'銅地金',None,'s','font-size:5px')
b+=T(712,yb-20,'Recycling 4Mt',None,'s','font-size:5.4px;color:'+BR)
for x,y,t in [(566,yb+38,'RtM'),(716,yb+38,'RtM')]: b+=A(x,y,f'<span style="font-family:IT;font-weight:600;font-size:6px;color:#fff">{t}</span>',26,'',f'height:12px;background:{BR};display:flex;align-items:center;justify-content:center')
def tech(x,y,t): return A(x,y,f'<span class="l" style="font-size:6px;font-weight:600;color:{BR}">{t}</span>',58,'',f'height:14px;border:1px solid {BR};background:#fff;border-radius:7px;display:flex;align-items:center;justify-content:center')
b+=tech(486,yb+80,'CiDRA')+tech(560,yb+100,'Jetti')+tech(842,yb-24,'DESCycle')
b+=T(300,yb+210,f'<span style="color:{BR}">●</span> 三菱商事の関与（資産・トレーディング・技術投資）　｜　LME・CMEでのヘッジはTriland Metalsが担う',600,'s','font-size:5.6px')
jx=920; jw=1150-jx
b+=A(jx,ny+14,'',jw,'',f'height:254px;background:#fff')
b+=T(jx+14,ny+26,'営業グループ取り組み事例',None,'k')
b+=box(jx+14,ny+42,jw-28,30,'<span class="l" style="font-size:8.6px;font-weight:600">JETTI</span><span class="s" style="font-size:5.6px">銅生産の革新技術を有するスタートアップ</span>',INK)
b+=T(jx+14,ny+76,'× 価値共創',jw-28,'l','text-align:center;font-size:6.6px;color:'+BR)
b+=box(jx+14,ny+90,jw-28,30,'<span class="l" style="font-size:8.6px;font-weight:600;font-family:Noto Sans JP">三菱商事</span><span class="s" style="font-size:5.6px">銅資源開発／トレーディング分野のリーディングプレイヤー</span>',INK,PAN)
b+=para(jx+14,ny+132,jw-28,'銅鉱石からの銅分回収に関する革新技術を有する米Jettiに出資参画し、同社の事業拡大を支援しています。同社技術で生産される環境価値の高い銅地金を販売するほか、当社の銅事業のネットワークを活用し、低品位の銅鉱石からの銅分回収に課題を抱える鉱山に同社技術が導入されるよう、共同検討を行っています。','font-size:6.5px')
b+=LINE('M0,650 H290 C298,650 300,806 312,812 H1140 C1165,812 1170,650 1190,650')
b+=BAND(0,824,1190,18)
pages.append(spread(b,8,9,'',''))

# ===== P10-11（PwC構成に寄せる）=====
b=BGN(330,286,'03')+BGN(930,180,'04')
b+=tile(0,0,595,280,'r-084.png','50% 35%','パートナーシップ','')+tile(599,0,591,170,'r-075.png','50% 55%','社会を支える資源','')
o,yy=head(L,296,'第3章','選ばれ続ける理由','Partner of choice.','資源業界に不可欠な存在として、選ばれ続ける',size=36)
b+=o
four=[('Cultural affinity with the majors','資源メジャーとの企業文化的親和性'),('JV management capability','資源投資経験に裏打ちされたJV経営力'),('Sound financial base','事業ポートフォリオを生かした健全な財務基盤'),('Deep insight','マクロ環境とバリューチェーンへの深い知見')]
for i,(e,j) in enumerate(four):
    x=L+(i%2)*262; y=yy+4+(i//2)*34
    b+=T(x,y,f'0{i+1}',None,'n','font-size:20px;color:'+BR)+T(x+32,y+1,e,220,'l','font-size:6px;color:'+G2)+T(x+32,y+11,j,220,'hs','font-size:8.4px;font-weight:700')
fy=yy+80
b+=T(L,fy,'JVへの貢献',None,'k')+T(L+70,fy,'経営から現場まで伴走する',None,'kj')
for x,t_,items in [(L,'現場',['長期目線での戦略策定と案件開発','幅広い産業接点を生かした知見の提供','人材派遣による操業支援']),(L+262,'経営',['中長期の事業計画・資本政策への参画','販売戦略・人事計画への関与','他JVのベストプラクティスの導入'])]:
    b+=A(x,fy+16,f'<div class="hs" style="font-size:8.4px;font-weight:700;color:#fff">{t_}</div>',252,'',f'height:20px;padding:4px 10px;background:{INK}')
    b+=A(x,fy+36,'<br>'.join('・'+s_ for s_ in items),252,'s',f'font-size:6.6px;line-height:1.85;padding:6px 10px;border:.8px solid {G3};height:62px;color:{INK}')
b+=S(arrow(L+126,fy+100,L+126,632,G1)+arrow(L+388,fy+100,L+206,632,G1))
b+=LINE('M0,650 H595 C620,650 640,700 660,712',[])
for x,t_,wd in [(L,'資源メジャー各社と「会社対会社」の関係へ',240),(L+256,'新たな協業',120),(L+392,'積み重ねが強み・信頼に',123)]:
    b+=A(x,636,f'<div class="hs" style="font-size:7.8px;font-weight:700;text-align:center">{t_}</div>',wd,'',f'height:28px;border:1px solid {G2};background:#fff;display:flex;align-items:center;justify-content:center')
b+=T(L,684,'新たな協業が生まれ、その積み重ねが、さらなる強み・知見・信頼につながる。',W,'b','font-size:7.2px')
b+=T(L,730,'主なJVパートナー',None,'k')+T(L+90,726,'BHP　　Rio Tinto　　Anglo American',None,'nb','font-size:15px')
# P11
o,yy=head(R,186,'第4章','何を実現するか','Building the future<br>of resources, together.','社会の「当たり前」を、支え続ける',size=30)
b+=o
ey=yy+4
b+=T(R,ey,'外部環境と社会課題',None,'k')
ccx,ccy=R+80,ey+64
b+=S(f'<circle cx="{ccx}" cy="{ccy}" r="46" fill="{PAN}" stroke="{G3}" stroke-width=".8"/><path d="M{ccx},{ccy-46} A46,46 0 0 1 {ccx+46},{ccy}" fill="none" stroke="{INK}" stroke-width="3"/>')
b+=T(ccx-40,ccy-8,'クリティカル<br>ミネラル',80,'hs','text-align:center;font-size:8px;font-weight:700;line-height:1.3')
env=[('産業構造の転換','脱炭素化に加え、生成AI・データセンターの普及で電力需要が拡大。高効率・高性能化を前提とした設備・製品設計が一般化'),('供給制約の深刻化','良質な資源の開発はより難しく、時間とコストがかかるように'),('地政学リスクの常態化','輸出規制など資源の囲い込みが進み、サプライチェーンに構造的に影響')]
o=''
for i,(e,d_) in enumerate(env):
    y=ey+14+i*34; o+=f'<path d="M{ccx+46},{ccy} C{ccx+70},{ccy} {ccx+70},{y+8} {R+150},{y+8}" fill="none" stroke="{G2}" stroke-width=".7"/>'
    b+=T(R+156,y,e,None,'hs','font-size:8.4px;font-weight:700')+T(R+156,y+13,d_,W-156,'s','font-size:6.1px')
b+=S(o)
y2=ey+120
b+=A(R,y2,'<div class="hs" style="font-size:8.6px;font-weight:700;color:#fff;text-align:center">クリティカルミネラルのサプライチェーン確保の重要性・川上資源への参入障壁が増大</div>',W,'',f'height:22px;padding:4px 10px;background:{INK}')
y3=y2+34
b+=T(R,y3,'当社の取り組み',None,'k')+T(R+80,y3,'資源の安定供給と効率的な供給で社会を支えている',None,'kj')
cw=212
for x,t_,items in [(R,'資源投資',['銅などの基幹事業で、大規模資産の持分を拡大','成長が期待される領域に、早い段階から参画','信頼できるパートナーと、投資先の価値向上を推進']),(R+W-cw,'トレーディング',['権益の引き取りと外部調達で、安定供給の体制を確立','需給の変化をつかみ、試験的な取引から先行して動く','国際的な取引基盤を軸に、業界ネットワークを構築'])]:
    b+=A(x,y3+16,f'<div class="hs" style="font-size:8.6px;font-weight:700;color:#fff;text-align:center">{t_}</div>',cw,'',f'height:20px;padding:4px;background:{G1}')
    b+=A(x,y3+36,'<br>'.join('・'+s_ for s_ in items),cw,'s',f'font-size:6.3px;line-height:1.85;padding:6px 8px;border:.8px solid {G3};height:58px;color:{INK}')
vx=R+W/2; vy_=y3+60
b+=S(f'<path d="M{vx-28},{vy_-6} A28,28 0 0 1 {vx+28},{vy_-6}" fill="none" stroke="{BR}" stroke-width="3"/><path d="M{vx+28},{vy_+6} A28,28 0 0 1 {vx-28},{vy_+6}" fill="none" stroke="{BR}" stroke-width="3"/>'+f'<path d="M{vx+22},{vy_-12} L{vx+28},{vy_-2} L{vx+34},{vy_-12}Z" fill="{BR}"/><path d="M{vx-22},{vy_+12} L{vx-28},{vy_+2} L{vx-34},{vy_+12}Z" fill="{BR}"/>')
b+=T(vx-20,vy_-6,'連携',40,'h','text-align:center;font-size:9px;color:'+BR)
b+=T(R,y3+108,'「金属＝経済活動を支える礎」。“儲ける”ではなく、社会に必要な資源を支えることを、私たちの責務と考えています。',W,'h','font-size:9px;line-height:1.6;text-align:center')
b+=LINE('M660,712 H1150',[(1150,712)])
b+=A(R,724,'',W,'',f'height:92px;background:{INK}')
b+=T(R+18,734,'グループミッション｜共に、持続可能で豊かな未来を築く',None,'k','color:#e9d6ac')
b+=T(R+18,752,'社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する',W-36,'hs','font-size:10.4px;color:#fff;line-height:1.5')
b+=T(R+18,794,'To contribute to a better society by providing a stable supply of high-quality mineral resources that society needs, in a sustainable way.',W-36,'s','color:#9aa1a8;font-family:IN')
b+=BAND(0,824,1190,18)
pages.append(spread(b,10,11,'',''))

links=''.join(f'<link rel="stylesheet" href="f/nsjp/package/{w}.css">' for w in (400,500,700))
open('daiwari_v22.html','w').write('<!doctype html><meta charset=utf-8>'+links+'<style>'+CSS2+'</style>'+''.join(pages))
