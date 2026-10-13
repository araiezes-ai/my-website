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
CSS2+=""".b{font-size:8.4px !important;line-height:1.85 !important}.s{font-size:7.2px}.k,.kj{font-size:7.2px}.l{font-size:7px}.hs{font-size:9px}
.ttl{font-family:'Noto Sans JP';font-weight:700;letter-spacing:.5px;color:#121519}
"""


# ===== P02-03 =====
exec(P23.replace("pages.append(spread(b,2,3,'',''))","b+=LINE('M0,420 H1190',[(L+2,420),(R+2,420)])\npages.append(spread(b,2,3,'',''))").replace("b+=kick(L,438,","b+=kick(L,440,").replace("b+=kick(R,438,","b+=kick(R,440,"))


# ===== P04-05 第1章：7グループの輪 → 金属資源グループ =====
b=BGN(340,110,'01',260)+BGN(930,110,'01',260)
b+=tile(0,0,392,112,'r-022.png','50% 60%')+tile(396,0,199,112,'mr_01_01@2x.webp','50% 60%',mx=1200)+tile(599,0,296,112,'r-047.png','60% 40%')+tile(899,0,291,112,'mr_02_01@2x.webp','50% 50%',mx=1200)
b+=T(L,136,'第1章　我々は何者か｜三菱商事とは',None,'k')
b+=T(L,154,'Who we are.',W,'d','font-size:40px')+A(L,204,'',22,'',f'border-top:1.4px solid {RED}')
b+=T(L,214,'三綱領を精神の根幹に、「総合力」で価値を生む',None,'ttl','font-size:13px')
b+=para(L,238,250,'三菱商事は三綱領を企業理念とし、事業を通じて経済価値・社会価値・環境価値の同時実現を目指しています。幅広い産業と地域にまたがる事業と人のつながり＝「総合力」が、三菱商事の強みです。')
# wheel
cx,cy,R1,R0=318,585,226,92
n=7; seg=360/n
def sector(r0,r1,a0,a1,dx=0,dy=0):
    P=lambda r,a:(cx+dx+r*math.cos(math.radians(a)),cy+dy+r*math.sin(math.radians(a)))
    p1,p2,p3,p4=P(r1,a0),P(r1,a1),P(r0,a1),P(r0,a0)
    return f'M{p1[0]:.1f},{p1[1]:.1f} A{r1},{r1} 0 0 1 {p2[0]:.1f},{p2[1]:.1f} L{p3[0]:.1f},{p3[1]:.1f} A{r0},{r0} 0 0 0 {p4[0]:.1f},{p4[1]:.1f}Z'
o=''.join(f'<circle cx="{cx}" cy="{cy}" r="{R1+10+k*9}" fill="none" stroke="#d5dade" stroke-width=".6"/>' for k in range(4))
for k_ in range(4):
    a=math.radians(200+k_*38); o+=f'<circle cx="{cx+(R1+28)*math.cos(a):.1f}" cy="{cy+(R1+28)*math.sin(a):.1f}" r="16" fill="#fff" stroke="#c7cdd2" stroke-width=".6"/>'
tints=['#eef0f2','#e6e9ec','#eef0f2','#e6e9ec','#eef0f2','#e6e9ec','#eef0f2']
o+=f'<defs><linearGradient id="cug" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#c58456"/><stop offset="1" stop-color="#8f4a22"/></linearGradient></defs>'
for i in range(n):
    a0=-seg/2+i*seg+1; a1=a0+seg-2
    if i==0:
        m=math.radians(0); o+=f'<path d="{sector(R0+6,R1+16,a0,a1,16,0)}" fill="url(#cug)"/>'
    else:
        o+=f'<path d="{sector(R0,R1,a0,a1)}" fill="{tints[i]}"/>'
o+=f'<circle cx="{cx}" cy="{cy}" r="{R0-4}" fill="#fff"/><circle cx="{cx}" cy="{cy}" r="{R0-14}" fill="none" stroke="{BR}" stroke-width=".7" stroke-dasharray="1.5 3"/>'
b+=S(o)
for i in range(1,n):
    a=math.radians(i*seg); x=cx+(R0+R1)/2*math.cos(a); y=cy+(R0+R1)/2*math.sin(a)
    b+=T(x-46,y-12,'○○グループ',92,'ttl','text-align:center;font-size:9px;color:#8a9097')+T(x-46,y+4,'事業・製品',92,'s','text-align:center;color:#a7adb3')
xm=cx+16+(R0+R1+22)/2
b+=T(xm-64,cy-30,'金属資源<br>グループ',128,'ttl','text-align:center;font-size:14px;line-height:1.3;color:#fff')+T(xm-64,cy+12,'中核グループ',128,'k','text-align:center;color:#f3dcc8')+T(xm-64,cy+26,'原料炭・銅 ほか',128,'s','text-align:center;color:#f3dcc8')
b+=T(cx-70,cy-44,'三菱商事',140,'ttl','text-align:center;font-size:15px')+T(cx-70,cy-20,'総合力',140,'k','text-align:center;color:'+BR+';font-size:8px')
b+=T(cx-70,cy-2,'所期奉公<br>処事光明<br>立業貿易',140,'s','text-align:center;line-height:1.6;color:'+INK)
b+=T(cx-70,cy+46,'三綱領',140,'k','text-align:center;font-size:6.6px')
b+=T(L,328,'7つの営業グループのうち、<br>長年三菱商事を支えてきた<br>中核グループの一つ。',170,'ttl','font-size:9.6px;line-height:1.6')
b+=T(L,780,'※グループ名称は確認後に記載',None,'s','color:#a7adb3')
b+=LINE(f'M0,420 C40,420 60,{cy} {cx-R1-40},{cy}')
b+=LINE(f'M{cx+R1+32},{cy} C620,{cy} 610,650 690,650 H1190')
# right page
b+=T(R,136,'第1章　我々は何者か｜金属資源グループとは',None,'k')
b+=T(R,154,'The core that has carried us.',W,'d','font-size:30px')+A(R,194,'',22,'',f'border-top:1.4px solid {RED}')
b+=T(R,204,'三綱領を体現する中核グループとして',None,'ttl','font-size:13px')
b+=para(R,228,W,'社会に不可欠な金属資源を世界から確保し、安定的に届けてきました。三綱領を事業で体現する中核グループとして、市況の波を越え、長年にわたり会社の屋台骨を支えています。')
py=282
b+=A(R,py,'',W,'',f'height:84px;background:{INK}')+T(R+20,py+14,'GROUP MISSION　グループミッション',None,'k','color:#e9d6ac')+T(R+20,py+32,'社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する',W-40,'ttl','font-size:12px;line-height:1.55;color:#fff')
cy2=392
b+=T(R,cy2,'これまでの変遷',None,'ttl','font-size:12px')+T(R+100,cy2+3,'先見性をもって先手を打ってきた歩み',None,'s')
sx0,sx1,sb=R+70,R+W,600
xs_=[sx0+i*(sx1-sx0)/4 for i in range(5)]
trd=[30,34,38,44,50]; inv=[4,26,56,80,100]
tt=[(x,sb-v) for x,v in zip(xs_,trd)]; ii=[(x,sb-t-v) for x,t,v in zip(xs_,trd,inv)]
o=f'<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in tt)+f' L{sx1},{sb} L{sx0},{sb}Z" fill="{G1}"/>'
o+=f'<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in ii)+' L'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in reversed(tt))+f'Z" fill="{BR}"/>'
b+=S(o)+T(R,sb-78,'事業の重心',70,'k')+T(R,sb-62,f'<span style="color:{BR}">■</span> 資源投資<br><span style="color:{G1}">■</span> トレーディング',70,'s','line-height:1.7')
eras=[('1980〜90年代','日本の産業に、資源を。','トレーディングで参入し、少数出資から事業に関わる'),('1990年代','仲介から、担い手へ。','投資モデルへ転換し、JV運営の知見を蓄える'),('2000年代','一級資産に、早くから。','BHPと原料炭の合弁を組成し、事業経営に参画'),('2010年代','次の柱を、先回りして。','銅へ領域を広げ、販売機能をRtMに集約'),('2020年代〜','投資と販売を、一つの力に。','両輪を一体で動かす、グローバルな事業者へ')]
o=''
for i,(yr,th,ac) in enumerate(eras):
    x=R+64+i*96
    o+=f'<circle cx="{x}" cy="650" r="4.5" fill="{CU if i in (2,3) else INK}" stroke="#fff" stroke-width="1"/>'
    b+=T(x-4,622,yr,None,'nb','font-size:12px')+T(x-4,664,th,94,'ttl','font-size:8.6px;line-height:1.45')+T(x-4,692,ac,90,'s')
b+=S(o)
b+=rule(R,752,W,G3)+T(R,762,'事業領域',None,'k')+T(R+64,760,'<b style="color:'+CU+'">原料炭　銅</b>　鉄鉱石　ニッケル　リチウム　アルミ・ボーキサイト　肥料資源　二次資源',W-64,'ttl','font-size:9px;letter-spacing:.6px;font-weight:500')
b+=BAND(0,824,1190,18)
pages.append(spread(b,4,5,'',''))

# ===== P06-07 第2章（導入）：両輪のハブと4つのシーン =====
b=BGN(330,60,'02',260)
b+=T(L,40,'第2章　独自価値｜投資とトレーディングの両輪',None,'k')
b+=T(L,58,'Two wheels,<br>one flow.',W,'d','font-size:44px')+A(L,158,'',22,'',f'border-top:1.4px solid {RED}')
b+=T(L,168,'資源の流れ全体に関わり、互いを強め合ってきた',None,'ttl','font-size:13px')
b+=para(L,194,300,'投資とトレーディングの両輪で、資源の流れ全体に関わる。互いを強め合いながら、長い時間をかけて積み重ねてきたこと。それが、鉱山会社でも純粋なトレーダーでもない、金属資源グループならではの強さです。')
# A–E list on right top
b+=T(R+40,40,'金属資源グループならではの強み',None,'ttl','font-size:12px')
AE=[('A','持つ力・つなぐ力','資源に投資して育てる力と、市場へ届ける力の両方を持つ'),('B','互いを強め合う','市場の情報を投資判断に、投資の資源を市場へ'),('C','流れ全体を進化させる','業界の課題に挑む新技術へ投資し、両輪に還元'),('D','長い時間をかけて','市況に左右されず関わり続け、先見性を培う'),('E','その結果としての、いま','原料炭・銅・トレーディング　→ P.08')]
for i,(k_,t_,d_) in enumerate(AE):
    y=64+i*38; b+=rule(R+40,y,W-40,G3,.6)+badge(R+40,y+8,k_,RED if k_=='E' else (CU if k_=='C' else BR),18)+T(R+68,y+7,t_,None,'ttl','font-size:9.6px')+T(R+68,y+22,d_,W-70,'s')
# flow line (behind)
hx,hy,hr=595,500,104
SC=[('mine','川上','鉱山・資源開発','世界上位の優良鉱山に参画し、育てる','x_vc_mine.jpg',190,500),
    ('factory','川中','製錬・製鉄','精鉱・原料を製錬所・製鉄所へ','x_vc_smelter.jpg',370,708),
    ('bolt','川下','需要家・最終製品','電化・インフラ・モビリティへ','x_vc_ev.jpg',1000,500),
    ('flask','新技術','業界のボトルネックへ','選鉱・浸出・リサイクルの技術に投資','x_case_smelt.jpg',820,708)]
b+=LINE(f'M0,650 C70,650 100,500 190,500 H1000 C1090,500 1120,650 1190,650')
o=''
for ic,t1,t2,d_,f,x,y in SC[:3]:
    pass
o+=f'<path d="M{SC[0][5]+60},{SC[0][6]+70} Q300,640 {SC[1][5]-40},{SC[1][6]-80}" fill="none" stroke="{BR}" stroke-width="1" stroke-dasharray="3 3"/>'
o+=f'<path d="M{SC[1][5]+92},{SC[1][6]-20} Q480,640 {hx-70},{hy+78}" fill="none" stroke="{G1}" stroke-width="1" stroke-dasharray="3 3"/>'
o+=f'<path d="M{hx+70},{hy+78} Q700,640 {SC[3][5]-92},{SC[3][6]-20}" fill="none" stroke="{CU}" stroke-width="1" stroke-dasharray="3 3"/>'
b+=S(o)
# hub
o=(f'<circle cx="{hx}" cy="{hy}" r="{hr+22}" fill="none" stroke="#d5dade" stroke-width=".6"/>'
   f'<path d="M{hx-4},{hy-hr} A{hr},{hr} 0 0 0 {hx-4},{hy+hr}Z" fill="{BR}"/>'
   f'<path d="M{hx+4},{hy-hr} A{hr},{hr} 0 0 1 {hx+4},{hy+hr}Z" fill="{G1}"/>'
   f'<path d="M{hx-60},{hy-hr-12} A{hr+12},{hr+12} 0 0 1 {hx+60},{hy-hr-12}" fill="none" stroke="{BR}" stroke-width="2"/>'+f'<path d="M{hx+54},{hy-hr-19} L{hx+64},{hy-hr-11} L{hx+52},{hy-hr-6}" fill="none" stroke="{BR}" stroke-width="2"/>'
   f'<path d="M{hx+60},{hy+hr+12} A{hr+12},{hr+12} 0 0 1 {hx-60},{hy+hr+12}" fill="none" stroke="{G1}" stroke-width="2"/>'+f'<path d="M{hx-54},{hy+hr+19} L{hx-64},{hy+hr+11} L{hx-52},{hy+hr+6}" fill="none" stroke="{G1}" stroke-width="2"/>')
b+=S(o)
b+=ICON('mine',hx-62,hy-56,22,'#fff')+T(hx-100,hy-26,'資源投資',92,'ttl','text-align:right;font-size:14px;color:#fff')+T(hx-100,hy-4,'資源に投資し<br>育てる力',92,'s','text-align:right;color:#f3e3d2;line-height:1.5')
b+=ICON('ship',hx+40,hy-56,22,'#fff')+T(hx+10,hy-26,'トレー<br>ディング',92,'ttl','font-size:14px;color:#fff;line-height:1.15')+T(hx+10,hy+12,'市場へ<br>届ける力',92,'s','color:#dfe3e7;line-height:1.5')
b+=T(hx-100,hy-hr-46,'投資で得た資源を、市場へ',200,'s','text-align:center;color:'+BR)+T(hx-100,hy+hr+30,'市場の情報を、投資判断へ',200,'s','text-align:center;color:'+G1)
b+=badge(hx-9,hy-hr-74,'A',BR,18)+badge(hx+110,hy-hr+4,'B',BR,18)
# scene circles
for ic,t1,t2,d_,f,x,y in SC:
    r=92; col=CU if t1=='新技術' else INK
    b+=S(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{PAN}"/>')
    b+=CIRC(x,y+34,92,f,ring=False)
    b+=S(f'<circle cx="{x}" cy="{y-r}" r="17" fill="{col}"/>')+ICON(ic,x-11,y-r-11,22,'#fff')
    b+=T(x-80,y-r+24,f'{t1}｜{t2}',160,'ttl','text-align:center;font-size:10px')+T(x-74,y-r+42,d_,148,'s','text-align:center')
b+=badge(SC[3][5]+70,SC[3][6]-90,'C',CU,18)+badge(SC[2][5]+70,SC[2][6]-90,'E',RED,18)
b+=T(L,800,'D｜これらの流れに、長い時間をかけて関わり続けてきた積み重ねが、先見性につながっている。',600,'s','color:'+INK)
b+=BAND(0,824,1190,18)
pages.append(spread(b,6,7,'',''))

# ===== P08-09 主力3事業（3カラム）＋新技術 =====
def box(x,y,w,h,html,bd=G3,bg='#fff',cls='l',st=''):
    return A(x,y,html,w,'',f'height:{h}px;border:.8px solid {bd};background:{bg};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;{st}')
def msq3(x,y,w,rows,lw=54):
    o=''
    for i,(k_,v,d_) in enumerate(rows):
        yy=y+i*30; o+=rule(x,yy,w,INK if i==0 else G3,.9 if i==0 else .5)
        o+=T(x,yy+9,k_,None,'l','font-size:6.6px;letter-spacing:1.4px;color:'+G2)+T(x+lw,yy+5,v,w-lw,'hs','font-size:9.4px;font-weight:700')+T(x+lw,yy+18,d_,w-lw,'s','font-size:6.6px')
    return o+rule(x,y+len(rows)*30,w,G3,.5)
C1,C2,C3,CW_=40,429,818,332
b=BGN(300,520,'02',240)+BGN(890,520,'02',240)
b+=tile(0,0,392,170,'r-047.png','60% 40%','原料炭','豪州')+tile(399,0,392,170,'mr_02_01@2x.webp','50% 50%','銅','南米',1400)+tile(798,0,392,170,'r-023.png','50% 60%','トレーディング','')
def hd(x,k1,en,jt,w=CW_,size=21):
    return T(x,184,k1,None,'k')+T(x,198,en,w,'d',f'font-size:{size}px')+A(x,198+(en.count('<br>')+1)*size*1.05+8,'',22,'',f'border-top:1.4px solid {RED}')+T(x,198+(en.count('<br>')+1)*size*1.05+16,jt,w,'h','font-size:9.0px')
# --- 原料炭
b+=hd(C1,'PILLAR 1　原料炭事業','World-class metallurgical coal.','鉄の主原料“産業のコメ”を、世界最高品位で届ける')
b+=para(C1,252,CW_,'原料炭は鉄の主原料。BHPとの50:50の合弁BMAを通じ、豪州クイーンズランド州ボーエン・ベースンで世界最高品位の原料炭を生産。炭鉱から港湾・鉄道までを保有し、全体最適の操業で安定供給を実現しています。','font-size:7.2px')
b+=msq3(C1,304,CW_,[('MARKET','上位5社で約80%','寡占度が高く、供給は漸減'),('SCALE','BMAで約50%','一級強粘炭の世界供給に占めるシェア'),('QUALITY','高品位に集約','7炭鉱から高品位の5炭鉱へ。港湾・鉄道も自社保有')])
oy=398
b+=T(C1,oy,'出資構成',None,'k','font-size:6.6px')
b+=box(C1,oy+14,92,20,'<span class="l" style="font-size:7.2px;font-family:Noto Sans JP;font-weight:700">三菱商事</span>',INK)
b+=box(C1,oy+50,92,20,'<span class="l" style="font-size:7.4px">MDP</span>',INK)+box(C1+100,oy+50,30,20,'<span class="l" style="font-size:7.2px">BHP</span>',G2)
b+=box(C1,oy+90,130,26,'<span class="l" style="font-size:8.4px;font-weight:600">BMA</span><span class="s" style="font-size:6.6px">BHP Mitsubishi Alliance</span>',INK,PAN)
o=arrow(C1+46,oy+34,C1+46,oy+48,INK)+arrow(C1+46,oy+70,C1+46,oy+88,INK)+arrow(C1+115,oy+70,C1+115,oy+88,G2)
b+=S(o)+T(C1+50,oy+38,'100%',None,'s','font-size:6.6px')+T(C1+50,oy+74,'50%',None,'s','font-size:6.6px')+T(C1+119,oy+74,'50%',None,'s','font-size:6.6px')
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
    LB.append((px+5 if not n.startswith('ヘイ') else px-12,py_-4 if not n.startswith('ヘイ') else py_-16,n,2))
b+=S(o)
for x_,y_,t_,k_ in LB: b+=T(x_,y_,t_,None,'s',f'font-size:6.6px;font-family:IN;white-space:nowrap;color:{INK if k_ else G2}')+T(mx+6,my+4,'ボーエン・ベースン（クイーンズランド州）',None,'k','font-size:6.6px')
b+=T(mx+6,my+mh+4,f'<span style="color:{BR}">●</span>操業中　○売却　- -鉄道　■港湾',mw,'s','font-size:6.6px')
# --- 銅（ノドをまたぐため左右2段に分割）
cl,cr_=C2,607; sw_=154
b+=hd(cl,'PILLAR 2　銅事業','The partner<br>the copper industry<br>calls first.','日本最大の銅生産者として、業界から声がかかる',sw_,17)
b+=para(cl,306,sw_,'電化や再エネ、AI・データセンターの広がりを背景に、銅の需要は拡大を続けています。主要メジャー各社との協業を通じ、世界最大級の銅ポジションを築いています。','font-size:7.2px')
b+=msq3(cl,396,sw_,[('MARKET','上位5社で約25%','寡占化が進まず再編の機運'),('SCALE','持分生産量で日本最大','パートナー型の生産者'),('QUALITY','5鉱山すべて世界Top15','平均コストは世界上位25%')],44)
# 早期の参画（縦タイムライン）
b+=T(cr_,184,'早期の参画',None,'k')+T(cr_,196,'主要銅鉱山への参画年',None,'kj')
tl=[(1988,'Escondida','チリ'),(1997,'Los Pelambres','チリ'),(1999,'Antamina','ペルー'),(2011,'Anglo American Sur','チリ'),(2011,'Quellaveco','ペルー'),(2023,'Marimaca','チリ・開発中'),(2025,'Copper World','米国・開発中')]
o=f'<line x1="{cr_+30}" y1="214" x2="{cr_+30}" y2="{214+6*17+6}" stroke="{INK}" stroke-width=".8"/>'
for i,(yr,n,c) in enumerate(tl):
    y=216+i*17; dev='開発' in c
    o+=f'<circle cx="{cr_+30}" cy="{y+4}" r="3" fill="{"#fff" if dev else BR}" stroke="{BR}" stroke-width=".9"/>'
    b+=T(cr_,y,str(yr),None,'l','font-size:7.2px;color:'+G1)+T(cr_+38,y-1,f'<b style="font-family:IN;font-weight:600;color:{INK}">{n}</b><br><span>{c}</span>',120,'s','font-size:6.6px;line-height:1.25')
b+=S(o)
# 参画鉱山の表
ty_=346
b+=T(cr_,ty_,'参画鉱山',None,'k')+T(cr_+50,ty_,'鉱山別生産量ランキング／出資比率',None,'kj')
rows=[('Escondida','チリ','1位','8.25%'),('Los Pelambres','チリ','12位','5%'),('AA Sur','チリ','10位','20.44%'),('Marimaca','チリ','開発中','5%'),('Antamina','ペルー','4位','10%'),('Quellaveco','ペルー','15位','40%'),('Copper World','米国','開発中','30%')]
b+=T(cr_,ty_+16,'鉱山',None,'l','font-size:6.6px;color:'+G2)+T(cr_+66,ty_+16,'国',None,'l','font-size:6.6px;color:'+G2)+T(cr_+92,ty_+16,'順位',None,'l','font-size:6.6px;color:'+G2)+T(cr_+124,ty_+16,'出資',None,'l','font-size:6.6px;color:'+G2)
for i,(n,c,r_,p) in enumerate(rows):
    y=ty_+28+i*15; b+=rule(cr_,y,sw_,G3,.5)+T(cr_,y+4,n,66,'l','font-size:6.6px;font-weight:600')+T(cr_+66,y+4,c,None,'s','font-size:6.6px')+T(cr_+92,y+3,r_,None,'nb',f'font-size:7.800000000000001px;color:{BR if "位" in r_ else G2}')+T(cr_+124,y+4,p,None,'l','font-size:6.6px')
b+=rule(cr_,ty_+28+7*15,sw_,INK,.8)
# --- トレーディング
b+=hd(C3,'PILLAR 3　トレーディング事業（RtM）','Resource to Market.','一つの商品の中で、投資から販売までを一気通貫でつなぐ')
for i,(n,e,j) in enumerate([('15','INDUSTRIES','業界に販売'),('50','COUNTRIES','カ国に販売'),('〜1,000','CUSTOMERS','社の販売先')]):
    x=C3+i*112; b+=rule(x,252,100,INK,.9)+T(x,258,n,None,'n','font-size:22.0px')+T(x,284,e,None,'l','font-size:6.6px;letter-spacing:1.2px;color:'+BR)+T(x,292,j,None,'s','font-size:6.6px')
# RtM事業のビジネスモデル（PwC資料の図を整理）
by=312; bx=C3; bw=CW_
b+=T(bx,by,'RtM事業のビジネスモデル',None,'k')
b+=box(bx+110,by+14,bw-220,18,'<span class="l" style="font-size:7.2px;font-family:Noto Sans JP;font-weight:700">三菱商事</span>',INK)
b+=box(bx+110,by+38,(bw-230)/2,16,'<span class="s" style="font-size:6.6px;color:'+INK+'">第三者取引</span>',G2)+box(bx+120+(bw-230)/2,by+38,(bw-230)/2,16,'<span class="s" style="font-size:6.6px;color:'+INK+'">MC保有資産</span>',BR)
b+=box(bx+110,by+86,bw-220,24,'<span style="font-family:IT;font-weight:600;font-size:12.0px">RtM</span>',INK,PAN)
b+=box(bx+110,by+144,bw-220,18,'<span class="l" style="font-size:7.2px;font-family:Noto Sans JP;font-weight:700">顧客基盤</span>',INK)
o=arrow(bx+130,by+56,bx+130,by+84,INK)+arrow(bx+bw-130,by+84,bx+bw-130,by+56,BR)+arrow(bx+130,by+112,bx+130,by+142,INK)+arrow(bx+bw-130,by+142,bx+bw-130,by+112,BR)
b+=S(o)
b+=T(bx,by+62,'資源確保による<br>安定供給',92,'s','font-size:6.6px;text-align:right;color:'+INK)+T(bx+bw-92,by+60,'市場・業界動向の<br>発信と知見共有で<br>事業機会を発掘',92,'s','font-size:6.6px;color:'+BR)
b+=T(bx,by+118,'トレーディング機能<br>強化による継続的な<br>付加価値創出',92,'s','font-size:6.6px;text-align:right;color:'+INK)+T(bx+bw-92,by+118,'広い産業接点を<br>生かした<br>インテリジェンス',92,'s','font-size:6.6px;color:'+BR)
for i,t in enumerate(['Sustainability','Market Intelligence','Professionalism','Global Network']):
    b+=T(C3+i*84,by+170,t,80,'l','font-size:6.6px;font-weight:600;color:'+G1)
b+=T(C3,494,'多様な取引機能',None,'k')
for i,(ic,t) in enumerate([('grid','取扱商品の広さ'),('box','在庫'),('truck','輸送手配'),('hedge','ヘッジ')]):
    xx=C3+i*84; b+=A(xx,506,'',78,'',f'height:20px;border-top:.9px solid {INK};background:{PAN}')+ICON(ic,xx+4,508,14,G1)+T(xx+20,511,t,58,'s','font-size:6.6px;color:'+INK)
# ===== 新技術：銅バリューチェーン（PwC資料を整理）
ny=540
b+=A(0,ny,'',1190,'',f'height:284px;background:{PAN}')
b+=T(L,ny+18,'NEW TECHNOLOGY　新技術',None,'k')+T(L,ny+34,"Investing in<br>what's next.",250,'d','font-size:22.0px')+A(L,ny+86,'',22,'',f'border-top:1.4px solid {RED}')+T(L,ny+94,'業界のボトルネックに挑む新技術へ投資する',250,'h','font-size:9.0px')
b+=para(L,ny+116,240,'業界の課題を見極め、課題を解く技術を持つスタートアップに出資。トレーディングや業界とのつながりを生かして技術を現場に取り入れ、知見を既存事業の高度化に還元しています。','font-size:7.2px')
X0=300; X1=900
seg=[('Upstream',300,470,0),('Trading',472,520,1),('Midstream',522,708,0),('Trading',710,758,1),('Downstream',760,900,0)]
for n,a_,b_,tr in seg: b+=A(a_,ny+14,f'<span class="l" style="font-size:7.2px;color:{"#fff" if tr else INK}">{n}</span>',b_-a_,'',f'height:14px;background:{BR if tr else "#dfe3e7"};display:flex;align-items:center;justify-content:center')
# grade row
gy=ny+34
for x,t_ in [(330,'鉱石 Cu約1%'),(480,'銅精鉱 Cu20〜30%'),(612,'銅地金 Cu99.99%')]: b+=T(x,gy,t_,None,'l','font-size:7.2px;color:'+BR)
yb=ny+52
def pbox(x,y,w,h,t,sub=''): return A(x,y,f'<div class="l" style="font-size:7.2px;font-weight:600">{t}</div><div class="s" style="font-size:6.6px">{sub}</div>',w,'',f'height:{h}px;border:.8px solid {G2};background:#fff;padding:5px 6px')
b+=pbox(300,yb,104,200,'Mining','採掘')
for i,(n,p) in enumerate([('Escondida','8.25%'),('Los Pelambres','5%'),('AA Sur','20.44%'),('Antamina','10%'),('Quellaveco','40%'),('Marimaca','5%'),('Copper World','30%')]):
    b+=T(306,yb+30+i*14,f'<span style="color:{INK}">{n}</span>　<b style="color:{BR}">{p}</b>',96,'s','font-size:6.6px')
b+=pbox(470,yb,92,72,'Flotation','選鉱')+pbox(620,yb,92,72,'Smelting & Refining','製錬・精製')+pbox(470,yb+120,240,80,'Leaching','浸出（硫化鉱・酸化鉱）')+pbox(770,yb,130,200,'End Use','最終用途')
for i,t in enumerate(['Base Demand　基礎需要','Energy Transition　エネルギー転換','AI & Data Centers　AI・データセンター']):
    b+=T(778,yb+32+i*22,'— '+t,118,'s','font-size:6.6px;color:'+INK)
def vol(x,y,t): return A(x,y,f'<span class="l" style="font-size:7.2px;color:#fff;font-weight:600">{t}</span>',34,'',f'height:14px;background:{G1};display:flex;align-items:center;justify-content:center')
b+=vol(362,yb+182,'24Mt')+vol(522,yb+54,'21Mt')+vol(670,yb+182,'3Mt')+vol(860,yb+182,'28Mt')
o=(arrow(404,yb+30,468,yb+30,INK)+arrow(404,yb+150,468,yb+150,INK)+arrow(562,yb+30,618,yb+30,INK)+arrow(712,yb+30,768,yb+30,INK)+arrow(710,yb+150,768,yb+150,INK)
   +f'<path d="M835,{yb} V{yb-8} H700 V{yb-2}" fill="none" stroke="{BR}" stroke-width=".9"/>'+arrow(700,yb-6,700,yb-1,BR))
b+=S(o)
b+=T(410,yb+20,'硫化鉱',None,'s','font-size:6.6px')+T(410,yb+140,'酸化鉱・硫化鉱',None,'s','font-size:6.6px')+T(566,yb+20,'銅精鉱',None,'s','font-size:6.6px')+T(716,yb+20,'銅地金',None,'s','font-size:6.6px')+T(716,yb+140,'銅地金',None,'s','font-size:6.6px')
b+=T(712,yb-20,'Recycling 4Mt',None,'s','font-size:6.6px;color:'+BR)
for x,y,t in [(566,yb+38,'RtM'),(716,yb+38,'RtM')]: b+=A(x,y,f'<span style="font-family:IT;font-weight:600;font-size:7.2px;color:#fff">{t}</span>',26,'',f'height:12px;background:{BR};display:flex;align-items:center;justify-content:center')
def tech(x,y,t): return A(x,y,f'<span class="l" style="font-size:7.2px;font-weight:600;color:{BR}">{t}</span>',58,'',f'height:14px;border:1px solid {BR};background:#fff;border-radius:7px;display:flex;align-items:center;justify-content:center')
b+=tech(486,yb+80,'CiDRA')+tech(560,yb+100,'Jetti')+tech(842,yb-24,'DESCycle')
b+=T(300,yb+210,f'<span style="color:{BR}">●</span> 三菱商事の関与（資産・トレーディング・技術投資）　｜　LME・CMEでのヘッジはTriland Metalsが担う',600,'s','font-size:6.6px')
jx=920; jw=1150-jx
b+=A(jx,ny+14,'',jw,'',f'height:254px;background:#fff')
b+=T(jx+14,ny+26,'営業グループ取り組み事例',None,'k')
b+=box(jx+14,ny+42,jw-28,30,'<span class="l" style="font-size:9.0px;font-weight:600">JETTI</span><span class="s" style="font-size:6.6px">銅生産の革新技術を有するスタートアップ</span>',INK)
b+=T(jx+14,ny+76,'× 価値共創',jw-28,'l','text-align:center;font-size:7.2px;color:'+BR)
b+=box(jx+14,ny+90,jw-28,30,'<span class="l" style="font-size:9.0px;font-weight:600;font-family:Noto Sans JP">三菱商事</span><span class="s" style="font-size:6.6px">銅資源開発／トレーディング分野のリーディングプレイヤー</span>',INK,PAN)
b+=para(jx+14,ny+132,jw-28,'銅鉱石からの銅分回収に関する革新技術を有する米Jettiに出資参画し、同社の事業拡大を支援しています。同社技術で生産される環境価値の高い銅地金を販売するほか、当社の銅事業のネットワークを活用し、低品位の銅鉱石からの銅分回収に課題を抱える鉱山に同社技術が導入されるよう、共同検討を行っています。','font-size:7.2px')
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
    b+=T(x,y,f'0{i+1}',None,'n','font-size:20.0px;color:'+BR)+T(x+32,y+1,e,220,'l','font-size:7.2px;color:'+G2)+T(x+32,y+11,j,220,'hs','font-size:8.8px;font-weight:700')
fy=yy+80
b+=T(L,fy,'JVへの貢献',None,'k')+T(L+70,fy,'経営から現場まで伴走する',None,'kj')
for x,t_,items in [(L,'現場',['長期目線での戦略策定と案件開発','幅広い産業接点を生かした知見の提供','人材派遣による操業支援']),(L+262,'経営',['中長期の事業計画・資本政策への参画','販売戦略・人事計画への関与','他JVのベストプラクティスの導入'])]:
    b+=A(x,fy+16,f'<div class="hs" style="font-size:8.8px;font-weight:700;color:#fff">{t_}</div>',252,'',f'height:20px;padding:4px 10px;background:{INK}')
    b+=A(x,fy+36,'<br>'.join('・'+s_ for s_ in items),252,'s',f'font-size:7.2px;line-height:1.85;padding:6px 10px;border:.8px solid {G3};height:62px;color:{INK}')
b+=S(arrow(L+126,fy+100,L+126,632,G1)+arrow(L+388,fy+100,L+206,632,G1))
b+=LINE('M0,650 H595 C620,650 640,700 660,712',[])
for x,t_,wd in [(L,'資源メジャー各社と「会社対会社」の関係へ',240),(L+256,'新たな協業',120),(L+392,'積み重ねが強み・信頼に',123)]:
    b+=A(x,636,f'<div class="hs" style="font-size:8.2px;font-weight:700;text-align:center">{t_}</div>',wd,'',f'height:28px;border:1px solid {G2};background:#fff;display:flex;align-items:center;justify-content:center')
b+=T(L,684,'新たな協業が生まれ、その積み重ねが、さらなる強み・知見・信頼につながる。',W,'b','font-size:7.6000000000000005px')
b+=T(L,730,'主なJVパートナー',None,'k')+T(L+90,726,'BHP　　Rio Tinto　　Anglo American',None,'nb','font-size:15.0px')
# P11
o,yy=head(R,186,'第4章','何を実現するか','Building the future<br>of resources, together.','社会の「当たり前」を、支え続ける',size=30)
b+=o
ey=yy+4
b+=T(R,ey,'外部環境と社会課題',None,'k')
ccx,ccy=R+80,ey+64
b+=S(f'<circle cx="{ccx}" cy="{ccy}" r="46" fill="{PAN}" stroke="{G3}" stroke-width=".8"/><path d="M{ccx},{ccy-46} A46,46 0 0 1 {ccx+46},{ccy}" fill="none" stroke="{INK}" stroke-width="3"/>')
b+=T(ccx-40,ccy-8,'クリティカル<br>ミネラル',80,'hs','text-align:center;font-size:8.4px;font-weight:700;line-height:1.3')
env=[('産業構造の転換','脱炭素化に加え、生成AI・データセンターの普及で電力需要が拡大。高効率・高性能化を前提とした設備・製品設計が一般化'),('供給制約の深刻化','良質な資源の開発はより難しく、時間とコストがかかるように'),('地政学リスクの常態化','輸出規制など資源の囲い込みが進み、サプライチェーンに構造的に影響')]
o=''
for i,(e,d_) in enumerate(env):
    y=ey+12+i*40; o+=f'<path d="M{ccx+46},{ccy} C{ccx+70},{ccy} {ccx+70},{y+8} {R+150},{y+8}" fill="none" stroke="{G2}" stroke-width=".7"/>'
    b+=T(R+156,y,e,None,'hs','font-size:8.8px;font-weight:700')+T(R+156,y+13,d_,W-156,'s','font-size:7.2px')
b+=S(o)
y2=ey+132
b+=A(R,y2,'<div class="hs" style="font-size:9.0px;font-weight:700;color:#fff;text-align:center">クリティカルミネラルのサプライチェーン確保の重要性・川上資源への参入障壁が増大</div>',W,'',f'height:22px;padding:4px 10px;background:{INK}')
y3=y2+34
b+=T(R,y3,'当社の取り組み',None,'k')+T(R+80,y3,'資源の安定供給と効率的な供給で社会を支えている',None,'kj')
cw=212
for x,t_,items in [(R,'資源投資',['銅などの基幹事業で、大規模資産の持分を拡大','成長が期待される領域に、早い段階から参画','信頼できるパートナーと、投資先の価値向上を推進']),(R+W-cw,'トレーディング',['権益の引き取りと外部調達で、安定供給の体制を確立','需給の変化をつかみ、試験的な取引から先行して動く','国際的な取引基盤を軸に、業界ネットワークを構築'])]:
    b+=A(x,y3+16,f'<div class="hs" style="font-size:9.0px;font-weight:700;color:#fff;text-align:center">{t_}</div>',cw,'',f'height:20px;padding:4px;background:{G1}')
    b+=A(x,y3+36,'<br>'.join('・'+s_ for s_ in items),cw,'s',f'font-size:7.2px;line-height:1.85;padding:6px 8px;border:.8px solid {G3};height:58px;color:{INK}')
vx=R+W/2; vy_=y3+60
b+=S(f'<path d="M{vx-28},{vy_-6} A28,28 0 0 1 {vx+28},{vy_-6}" fill="none" stroke="{BR}" stroke-width="3"/><path d="M{vx+28},{vy_+6} A28,28 0 0 1 {vx-28},{vy_+6}" fill="none" stroke="{BR}" stroke-width="3"/>'+f'<path d="M{vx+22},{vy_-12} L{vx+28},{vy_-2} L{vx+34},{vy_-12}Z" fill="{BR}"/><path d="M{vx-22},{vy_+12} L{vx-28},{vy_+2} L{vx-34},{vy_+12}Z" fill="{BR}"/>')
b+=T(vx-20,vy_-6,'連携',40,'h','text-align:center;font-size:9.0px;color:'+BR)
b+=T(R,y3+108,'「金属＝経済活動を支える礎」。“儲ける”ではなく、社会に必要な資源を支えることを、私たちの責務と考えています。',W,'h','font-size:9.0px;line-height:1.6;text-align:center')
b+=LINE('M660,712 H1150',[(1150,712)])
b+=A(R,724,'',W,'',f'height:92px;background:{INK}')
b+=T(R+18,734,'グループミッション｜共に、持続可能で豊かな未来を築く',None,'k','color:#e9d6ac')
b+=T(R+18,752,'社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する',W-36,'hs','font-size:10.4px;color:#fff;line-height:1.5')
b+=T(R+18,794,'To contribute to a better society by providing a stable supply of high-quality mineral resources that society needs, in a sustainable way.',W-36,'s','color:#9aa1a8;font-family:IN')
b+=BAND(0,824,1190,18)
pages.append(spread(b,10,11,'',''))

links=''.join(f'<link rel="stylesheet" href="f/nsjp/package/{w}.css">' for w in (400,500,700))
open('daiwari_v23.html','w').write('<!doctype html><meta charset=utf-8>'+links+'<style>'+CSS2+'</style>'+''.join(pages))
