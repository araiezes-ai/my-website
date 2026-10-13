# 台割 v20 — 全ページをP2-3のトンマナに統一。1本の銅のラインが P2→P11 を貫く
exec(open('v20_parts.py').read().split('\n#P23\n')[0])
import math
P23=open('v20_parts.py').read().split('\n#P23\n')[1].split('\n',1)[1]
LW=1.3
def LINE(d,dots=()):
    o=f'<path d="{d}" fill="none" stroke="{CU}" stroke-width="{LW}"/>'
    for x,y in dots: o+=f'<circle cx="{x}" cy="{y}" r="3.4" fill="{CU}" stroke="#fff" stroke-width="1"/>'
    return S(o)
def shade(x,y,w,h): return A(x,y,'',w,'',f'height:{h}px;background:linear-gradient(0deg,rgba(10,14,18,.72),rgba(10,14,18,.05) 60%,rgba(10,14,18,.25))')
pages=[]

# ===== P02-03 =====
exec(P23.replace("pages.append(spread(b,2,3,'',''))","b+=LINE('M0,420 H1190',[(L+2,420),(R+2,420)])\npages.append(spread(b,2,3,'',''))").replace("b+=kick(L,438,","b+=kick(L,440,").replace("b+=kick(R,438,","b+=kick(R,440,"))

# ===== P04-05  第1章 =====
b=tile(0,0,380,200,'r-022.png','50% 60%','三菱商事','東京・丸の内')+tile(384,0,211,200,'mr_01_01@2x.webp','50% 60%','総合力','産業と地域をまたぐ',1400)
b+=tile(599,0,300,200,'r-047.png','60% 40%','原料炭','豪州')+tile(903,0,287,200,'mr_02_01@2x.webp','50% 50%','銅','南米',1400)
b+=OUT(300,200,'01',150)
o,yy=head(L,222,'第1章','我々は何者か｜三菱商事とは','Who we are.','三綱領を精神の根幹に、「総合力」で価値を生む',size=40)
b+=o+para(L,yy+2,250,'三菱商事は三綱領を企業理念とし、事業を通じて経済価値・社会価値・環境価値の同時実現を目指しています。幅広い産業と地域にまたがる事業と人のつながり＝「総合力」が、三菱商事の強みです。')
# 三綱領 stacked
ty=446
b+=T(L,ty,'三綱領',None,'k')+T(L+50,ty,'三菱商事の企業理念',None,'kj')
for i,(j,r_,e) in enumerate([('所期奉公','しょきほうこう','事業を通じ、物心共に豊かな社会の実現に努力すると同時に、かけがえのない地球環境の維持にも貢献する'),('処事光明','しょじこうめい','公明正大で品格のある行動を旨とし、活動の公開性、透明性を堅持する'),('立業貿易','りつぎょうぼうえき','全世界的、宇宙的視野に立脚した事業展開を図る')]):
    y=ty+20+i*76; b+=rule(L,y,210,INK if i==0 else G3,1 if i==0 else .6)+T(L,y+8,j,None,'h','font-size:16px')+T(L+80,y+13,r_,None,'l','font-size:6.2px;color:'+BR)+T(L,y+32,e,205,'s','font-size:6.6px')
# ring
cx,cy,rr=440,572,112
o=f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="none" stroke="{G3}" stroke-width=".8"/><circle cx="{cx}" cy="{cy}" r="66" fill="{PAN}"/>'
for k in range(1,7):
    t=math.radians(k*360/7); x=cx+rr*math.cos(t); y=cy+rr*math.sin(t)
    o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="24" fill="#fff" stroke="{G2}" stroke-width=".8"/>'
b+=S(o)
b+=LINE(f'M0,420 H{cx-120} C{cx-60},420 {cx-30},{cy-rr} {cx},{cy-rr} A{rr},{rr} 0 0 1 {cx+rr},{cy} C{cx+rr+60},{cy} 610,650 690,650 H1190',[(cx,cy-rr)])
b+=S(f'<circle cx="{cx+rr}" cy="{cy}" r="27" fill="{CU}"/>')
b+=T(cx-60,cy-24,'三菱商事',120,'h','text-align:center;font-size:15px')+T(cx-60,cy-2,'総合力',120,'k','text-align:center;color:'+BR)+T(cx-60,cy+12,'7つの営業グループ',120,'s','text-align:center')
b+=T(cx+rr-24,cy-8,'金属<br>資源',48,'l','text-align:center;color:#fff;font-family:Noto Sans JP;font-size:7px;font-weight:700;line-height:1.15')
b+=T(cx-130,cy+rr+34,'金属資源グループは、7つの営業グループのうち、長年にわたり三菱商事を支えてきた中核グループの一つ。',260,'hs','text-align:center;font-size:8.4px;font-weight:700')
# right page
o,yy=head(R,222,'第1章','我々は何者か｜金属資源グループとは','The core that has<br>carried us.','三綱領を体現する中核グループとして',size=36)
b+=o+para(R,yy+2,W,'社会に不可欠な金属資源を世界から確保し、安定的に届けてきました。三綱領を事業で体現する中核グループとして、長年にわたり会社の屋台骨を支えています。')
py=yy+40
b+=A(R,py,'',W,'',f'height:70px;background:{INK}')+T(R+16,py+11,'グループミッション',None,'k','color:#e9d6ac')+T(R+16,py+27,'社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する',W-32,'hs','font-size:10px;line-height:1.5;color:#fff')
cy2=py+84
b+=T(R,cy2,'長年の貢献',None,'k')+T(R+70,cy2,'会社の屋台骨として',None,'kj')+T(R,cy2+16,'市況の波を越えて、全社の利益を長く支えてきた。',W,'h','font-size:13px')
b+=T(R,cy2+46,'歩み',None,'k')+T(R+40,cy2+46,'先見性をもって、先手を打ってきた',None,'kj')
eras=[('1980〜90年代','日本の産業に、資源を。','トレーディングで参入し、少数出資から事業に関わる'),('1990年代','仲介から、担い手へ。','投資モデルへ転換し、JV運営の知見を蓄える'),('2000年代','一級資産に、早くから。','BHPと原料炭の合弁を組成し、事業経営に参画'),('2010年代','次の柱を、先回りして。','銅へ領域を広げ、販売機能をRtMに集約'),('2020年代〜','投資と販売を、一つの力に。','両輪を一体で動かす、グローバルな事業者へ')]
o=''
for i,(yr,th,ac) in enumerate(eras):
    x=R+64+i*96
    o+=f'<circle cx="{x}" cy="650" r="4" fill="{CU if i in (2,3) else INK}" stroke="#fff" stroke-width="1"/>'
    b+=T(x-4,620,yr,None,'nb','font-size:12px')+T(x-4,664,th,92,'hs','font-size:8px;font-weight:700')+T(x-4,692,ac,90,'s','font-size:6.2px')
b+=S(o)
b+=rule(R,752,W,G3)+T(R,762,'事業領域',None,'k')+T(R+64,760,'原料炭　銅　鉄鉱石　ニッケル　リチウム　アルミ・ボーキサイト　肥料資源　二次資源',W-64,'hs','font-size:8.6px;letter-spacing:.6px')
b+=BAND(0,824,1190,18)
pages.append(spread(b,4,5,'',''))

# ===== P06-07  第2章 導入 =====
xs=[0,238,476,714,952]; tw=234
stg=[('x_vc_mine.jpg','01 川上','鉱山・資源開発'),('_mr_project_06.png','02 中間流通','トレーディング'),('x_vc_smelter.jpg','03 川中','製錬・製鉄'),('r-072.png','04 中間流通','トレーディング'),('x_vc_ev.jpg','05 川下','需要家・最終製品')]
b=''
for (f,e,j),x in zip(stg,xs): b+=tile(x,0,tw if x<952 else 238,330,f,'50% 50%',e,j)
roles=[('資源投資',BR),('トレーディング',NV),('資源投資',BR),('トレーディング',NV),('需要家',G2)]
for (t_,col),x in zip(roles,xs): b+=A(x,334,f'<div style="font-family:Noto Sans JP;font-weight:700;font-size:7.4px;color:#fff;padding:3px 10px">{t_}</div>',tw if x<952 else 238,'',f'height:18px;background:{col}')
b+=OUT(430,352,'02',150)
o,yy=head(L,372,'第2章','独自価値｜投資とトレーディングの両輪','Two wheels,<br>one flow.','資源の流れ全体に関わり、互いを強め合ってきた',size=44)
b+=o
b+=para(R,380,300,'投資とトレーディングの両輪で、資源の流れ全体に関わる。互いを強め合いながら、長い時間をかけて積み重ねてきたこと。それが、鉱山会社でも純粋なトレーダーでもない、金属資源グループならではの強さです。')
# cycle infographic
ccx,ccy=R+440,450
o=f'<path d="M{ccx-52},{ccy} A52,52 0 0 1 {ccx+52},{ccy}" fill="none" stroke="{BR}" stroke-width="5"/><path d="M{ccx+52},{ccy} A52,52 0 0 1 {ccx-52},{ccy}" fill="none" stroke="{NV}" stroke-width="5"/>'
o+=f'<path d="M{ccx+44},{ccy-12} l8,12 l8,-12" fill="{BR}"/><path d="M{ccx-60},{ccy+12} l8,-12 l8,12" fill="{NV}"/>'
b+=S(o)+T(ccx-40,ccy-30,'投資',80,'nb','text-align:center;font-size:12px;color:'+BR)+T(ccx-40,ccy+16,'トレーディング',80,'l','text-align:center;font-size:7px;color:'+NV+';font-family:Noto Sans JP;font-weight:700')
b+=T(ccx-80,ccy-74,'投資で得た資源を、市場へ',160,'s','text-align:center;color:'+BR)+T(ccx-80,ccy+62,'市場の情報を、投資判断へ',160,'s','text-align:center;color:'+NV)
# A-E along the line

cards=[('A','持つ力・つなぐ力','投資とトレーディングの両輪','資源に投資して育てる力と、市場へ届ける力の両方を持つ。鉱山会社でも、純粋なトレーダーでもない。',BR),
       ('B','互いを強め合う','一方通行ではない循環','市場の情報を投資判断に生かし、投資で得た資源を市場へ届ける。',NV),
       ('C','流れ全体を進化させる','新技術への投資','業界の課題に挑む技術に投資し、その知見を両輪に還元する。',CU),
       ('D','長い時間をかけて','積み重ねが先見性に','市況の浮き沈みに左右されず、流れに関わり続けてきた。',INK),
       ('E','その結果としての、いま','原料炭・銅・トレーディング','強みがあることの「結果」として、いまの主力事業がある。→ P.08',RED)]
dots=[]
for i,(k_,e,j,d_,col) in enumerate(cards):
    x=L+i*232; dots.append((x+9,650))
    b+=T(x,590,e,210,'h','font-size:12px')+T(x,612,j,210,'s','font-size:6.8px;color:'+col)
    b+=T(x,672,d_,200,'b','font-size:7.2px;line-height:1.8')
b+=LINE('M0,650 H1190')
for i,(k_,e,j,d_,col) in enumerate(cards): b+=badge(L+i*232,641,k_,col,18)
b+=rule(L,730,1110,G3)+T(L,744,'Not a miner. Not just a trader.',700,'dl','font-size:30px;color:'+G1)+T(R+180,752,'鉱山会社でも、純粋なトレーダーでもない。',400,'h','font-size:13px;text-align:right')
b+=BAND(0,824,1190,18)
pages.append(spread(b,6,7,'',''))

# ===== P08-09  主力3事業＋新技術 =====
b=tile(0,0,305,206,'r-047.png','60% 40%')+tile(309,0,286,206,'mr_02_01@2x.webp','50% 50%',mx=1400)+tile(599,0,591,206,'r-023.png','50% 60%')
b+=shade(0,0,1190,206)
for x,k1,big,sub in [(L,'PILLAR 1　原料炭事業','約50%','BMAが一級強粘炭の<br>世界供給に占めるシェア'),(L+284,'PILLAR 2　銅事業','日本最大','銅の持分生産量'),(R,'PILLAR 3　トレーディング事業（RtM）','15 × 50 × 1,000','業界 × カ国 × 販売先')]:
    b+=T(x,24,k1,None,'k','color:#e9d6ac')+T(x,140,big,None,'nb','font-size:40px;color:#fff')+T(x,182,sub,240,'hs','color:#fff;font-size:7.4px')
def bar(x,y,w,v,lab):
    return A(x,y,'',w,'',f'height:6px;background:{G4}')+A(x,y,'',w*v/100,'',f'height:6px;background:{INK}')+T(x+w*v/100+4,y-3,lab,None,'nb','font-size:9px')
cols=[(L,256),(L+284,256),(R,W)]
# coal
x,w=cols[0]
b+=T(x,222,'World-class<br>metallurgical coal.',w,'d','font-size:20px')+lead(x,270,'社会に欠かせない資源を、世界最高品位で',w,9.2)
b+=T(x,302,'MARKET',None,'l','font-size:5.8px;letter-spacing:1.4px;color:'+G2)+T(x+60,300,'上位5社で約80%｜寡占度が高い',w-60,'s')+bar(x+60,314,150,80,'80%')
b+=T(x,332,'SCALE',None,'l','font-size:5.8px;letter-spacing:1.4px;color:'+G2)+T(x+60,330,'一級強粘炭の約50%をBMAが供給',w-60,'s')+bar(x+60,344,150,50,'50%')
b+=T(x,362,'QUALITY',None,'l','font-size:5.8px;letter-spacing:1.4px;color:'+G2)+T(x+60,360,'高品位の5炭鉱に集約。港湾・鉄道も保有',w-60,'s')
# coal map (Bowen Basin, schematic) — PwC資料の地図を描き起こし
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
b+=T(mx+8,my+5,'ボーエン・ベースン｜豪州クイーンズランド州',None,'k','font-size:5.6px')
b+=T(mx+8,my+mh-14,f'<span style="color:{BR}">●</span> 保有5炭鉱　○ 売却した中品位2炭鉱　<span style="color:{RED}">- -</span> 鉄道　■ 港湾',w,'s','font-size:5.3px')
b+=T(x,my+mh+6,'BMA＝MDP（三菱商事100%）50%：BHP 50%',w,'s','font-size:6.2px')
# copper
x,w=cols[1]
b+=T(x,222,'The partner the copper<br>industry calls first.',w+12,'d','font-size:20px')+lead(x,270,'業界から最初に声がかかる、日本最大の生産者',w,9.2)
b+=T(x,302,'MARKET',None,'l','font-size:5.8px;letter-spacing:1.4px;color:'+G2)+T(x+60,300,'上位5社で約25%｜再編の機運',w-60,'s')+bar(x+60,314,150,25,'25%')
b+=T(x,332,'SCALE',None,'l','font-size:5.8px;letter-spacing:1.4px;color:'+G2)+T(x+60,330,'主要メジャーのほとんどとJV',w-60,'s')
b+=T(x,362,'QUALITY',None,'l','font-size:5.8px;letter-spacing:1.4px;color:'+G2)+T(x+60,360,'生産コストは世界の上位25%',w-60,'s')
vy=384
b+=A(x,vy,'',w,'',f'height:140px;background:{PAN}')
b+=T(x+8,vy+6,'参画鉱山の世界ランキング（鉱山別生産量）',None,'k','font-size:5.6px')
mines=[(1,'Escondida','チリ'),(4,'Antamina','ペルー'),(10,'Anglo American Sur','チリ'),(12,'Los Pelambres','チリ'),(15,'Quellaveco','ペルー')]
for i,(r_,n,c) in enumerate(mines):
    y=vy+24+i*18
    b+=T(x+8,y,f'{r_}<span style="font-size:7px">位</span>',None,'nb','font-size:13px;color:'+BR)+T(x+44,y+2,f'<b style="font-family:IN;font-weight:600;color:{INK}">{n}</b>　{c}',w-52,'s','font-size:6.6px')+A(x+150,y+6,'',(16-r_)*6,'',f'height:4px;background:{BR}')
b+=T(x+8,vy+120,'開発中：Marimaca（チリ）・Copper World（米国）',w-16,'s','font-size:6px')
# trading
x,w=cols[2]
b+=T(x,222,'Resource to Market.',w,'d','font-size:20px')+lead(x,250,'資源と市場をつなぎ、必要な場所へ確かに届ける',w,9.2)
pts3=[('第三者の資源も扱う','市場の生きた情報を、投資の側へ返す'),('ロジ・在庫・ヘッジ','機能を付けて、顧客に届ける'),('グローバルな販売網','欧州・シンガポール・米州の顧客へ')]
for i,(h_,d_) in enumerate(pts3):
    y=286+i*40; b+=rule(x,y,240)+T(x,y+6,f'0{i+1}',None,'nb','font-size:13px;color:'+NV)+T(x+24,y+7,h_,210,'hs','font-size:8.6px;font-weight:700')+T(x+24,y+21,d_,210,'s')
mx0=x+270; mw=245; myy=286
b+=A(mx0,myy,'<div class="l" style="font-size:6.6px">第三者の資源</div>',115,'',f'height:26px;border:1px solid {G2};display:flex;align-items:center;justify-content:center')
b+=A(mx0+130,myy,'<div class="l" style="font-size:6.6px">三菱商事の保有資産</div>',115,'',f'height:26px;border:1px solid {BR};display:flex;align-items:center;justify-content:center')
b+=A(mx0,myy+46,'<div style="font-family:IT;font-weight:600;font-size:15px;color:#fff">RtM</div>',mw,'',f'height:34px;background:{NV};display:flex;align-items:center;justify-content:center')
b+=A(mx0,myy+100,'<div class="l" style="font-size:6.6px">世界の顧客</div>',mw,'',f'height:26px;border:1px solid {INK};display:flex;align-items:center;justify-content:center')
o=arrow(mx0+57,myy+26,mx0+57,myy+44,NV)+arrow(mx0+187,myy+26,mx0+187,myy+44,NV)+arrow(mx0+70,myy+80,mx0+70,myy+98,NV)+arrow(mx0+175,myy+98,mx0+175,myy+80,BR)
b+=S(o)+T(mx0+80,myy+84,'安定供給',None,'s','font-size:5.8px')+T(mx0+182,myy+84,'市場の情報',None,'s','font-size:5.8px;color:'+BR)
for i,t in enumerate(['取扱商品の広さ','在庫','輸送手配','ヘッジ']):
    b+=A(x+i*128,430,f'<div class="hs" style="font-size:7.6px;font-weight:700;color:{NV}">{t}</div>',122,'',f'height:30px;border-top:1.4px solid {NV};background:{PAN};display:flex;align-items:center;justify-content:center')
# NEW TECH
ny=540
b+=A(0,ny,'',1190,'',f'height:284px;background:{PAN}')
b+=T(L,ny+16,'NEW TECHNOLOGY　新技術',None,'k')+T(L,ny+36,"Investing in what's next.",300,'d','font-size:22px')+T(L,ny+64,'資源業界のボトルネックに、新しい技術で挑む',300,'h','font-size:9.4px')
b+=para(L,ny+132,250,'業界の課題を見極め、課題を解く技術を持つスタートアップに出資。トレーディングと業界とのつながりを生かして現場に取り入れ、その知見を既存事業の高度化に還元しています。','font-size:6.9px')
b+=LINE('M0,650 H1190')
st=[('鉱石','Cu 約1%'),('銅精鉱','Cu 20〜30%'),('銅地金','Cu 99.99%'),('最終用途','電化・インフラ'),('リサイクル','再び供給へ')]
cx0=L+300
for i,(e,g_) in enumerate(st):
    xx=cx0+i*104
    b+=T(xx,ny+70,e,None,'h','font-size:11px')+T(xx,ny+88,g_,None,'nb','font-size:10px;color:'+CU)+S(f'<circle cx="{xx+4}" cy="650" r="4" fill="{INK}" stroke="#fff" stroke-width="1"/>')
techs=[(1,'CiDRA','選鉱','回収率と処理能力を高める'),(1,'Jetti','浸出','硫化鉱から銅を回収する'),(4,'DESCycle','リサイクル','電子スクラップから銅を回収')]
o=''
for k_,(si,n,t_,d_) in enumerate(techs):
    xx=cx0+k_*176; sx=cx0+si*104+4+(-18 if k_==0 else 18 if k_==1 else 0)
    o+=f'<path d="M{sx},650 V676 H{xx+10} V690" fill="none" stroke="{CU}" stroke-width=".8"/>'
    b+=A(xx,690,f'<div style="font-family:IN;font-weight:600;font-size:5.8px;letter-spacing:1.2px;color:{CU}">{t_}</div><div class="l" style="font-weight:600;font-size:11px;margin-top:2px">{n}</div><div class="s" style="margin-top:2px">{d_}</div>',164,'',f'height:60px;padding:8px 10px;border-top:1.4px solid {CU};background:#fff')
b+=S(o)
jx=900; jw=1150-jx
b+=A(jx,ny+16,'',jw,'',f'height:250px;background:#fff')
b+=T(jx+14,ny+28,'取り組み事例',None,'k','color:'+CU)+T(jx+14,ny+44,'Jetti × 三菱商事',jw-28,'h','font-size:12px')
b+=tile(jx+14,ny+66,jw-28,60,'x_case_smelt.jpg','50% 50%')
b+=para(jx+14,ny+136,jw-28,'銅鉱石からの銅分回収に関する革新技術を持つ米Jettiに出資参画。同社技術で生産される環境価値の高い銅地金を販売するほか、当社のネットワークを生かし、低品位の鉱石に課題を抱える鉱山への技術導入を共同で検討しています。','font-size:6.7px')
b+=BAND(0,824,1190,18)
pages.append(spread(b,8,9,'',''))

# ===== P10-11 =====
b=tile(0,0,595,280,'r-084.png','50% 35%','パートナーシップ','')+tile(599,0,591,170,'r-075.png','50% 55%','社会を支える資源','')
b+=OUT(436,280,'03',120)
o,yy=head(L,296,'第3章','選ばれ続ける理由','Partner of choice.','資源業界に不可欠な存在として、選ばれ続ける',size=36)
b+=o
four=[('企業文化的親和性','資源メジャーと同じ、中長期の視座'),('JV経営力','実質的な経営貢献と、高い目利き力'),('健全な財務基盤','リスクを分かち合える体力'),('深い知見','マクロ環境とバリューチェーンへの理解')]
for i,(e,d_) in enumerate(four):
    x=L+(i%2)*262; y=yy+8+(i//2)*40
    b+=T(x,y,f'0{i+1}',None,'nb','font-size:18px;color:'+BR)+T(x+30,y+1,e,220,'hs','font-size:9px;font-weight:700')+T(x+30,y+16,d_,220,'s','font-size:6.6px')
fy=yy+96
b+=T(L,fy,'JVへの貢献',None,'k')+T(L+70,fy,'経営から現場まで伴走する',None,'kj')
for x,t_,d_ in [(L,'経営','中長期計画・資本政策・販売戦略に参画'),(L+262,'現場','人材派遣とベストプラクティスで操業を支援')]:
    b+=A(x,fy+18,f'<div class="hs" style="font-size:9px;font-weight:700;color:#fff">{t_}</div><div class="s" style="color:#e9d6ac;margin-top:2px">{d_}</div>',252,'',f'height:44px;padding:7px 12px;background:{BR}')
b+=S(chev(L+126,fy+68,30,BR)+chev(L+388,fy+68,30,BR))
b+=LINE('M0,650 H595 C620,650 640,700 660,712',[])
nodes=[(L,'会社対会社の関係へ'),(L+178,'新たな協業が生まれる'),(L+356,'積み重ねが、強み・信頼に')]
for x,t_ in nodes:
    b+=A(x,636,f'<div class="hs" style="font-size:8.6px;font-weight:700">{t_}</div>',160,'',f'height:28px;border:1.2px solid {CU};background:#fff;display:flex;align-items:center;justify-content:center')
b+=T(L,684,'資源メジャー各社と、単なる共同出資を越えた「会社対会社」の関係へ。新たな協業が生まれ、その積み重ねが、さらなる強み・知見・信頼につながる。',W,'b','font-size:7.2px')
b+=T(L,730,'主なJVパートナー',None,'k')+T(L+90,726,'BHP　　Rio Tinto　　Anglo American',None,'nb','font-size:15px')
# P11
o,yy=head(R,186,'第4章','何を実現するか','Building the future<br>of resources, together.','社会の「当たり前」を、支え続ける',size=30)
b+=o
env=[('産業構造の転換','電化・AI・データセンターで、素材の需要が拡大'),('供給制約の深刻化','良質な資源の開発が、より難しく'),('地政学リスクの常態化','資源の囲い込みが、供給網に影響')]
for i,(e,d_) in enumerate(env):
    x=R+i*176; b+=A(x,yy+6,f'<div class="hs" style="font-size:8.8px;font-weight:700">{e}</div><div class="s" style="margin-top:4px">{d_}</div>',166,'',f'height:56px;padding:8px 10px;border-top:1.4px solid {INK};background:{PAN}')
y2=yy+72
b+=S(chev(R+W/2,y2))+A(R,y2+14,'<div class="hs" style="font-size:8.8px;font-weight:700;color:#fff;text-align:center">クリティカルミネラルの供給網確保が重要に。川上資源への参入障壁は高まる</div>',W,'',f'height:24px;padding:5px 10px;background:{INK}')
y3=y2+50
b+=S(chev(R+W/2,y3))
for x,t_,col,d_ in [(R,'資源投資',BR,'大規模資産の持分確保と、成長領域への早期参画'),(R+300,'トレーディング',NV,'権益の引き取りと外部調達で、安定供給の体制を確立')]:
    b+=A(x,y3+16,f'<div class="hs" style="font-size:9px;font-weight:700;color:#fff">{t_}</div><div class="s" style="color:#dfe5ea;margin-top:2px">{d_}</div>',215,'',f'height:44px;padding:7px 12px;background:{col}')
b+=S(arrow(R+222,y3+32,R+292,y3+32,G1)+arrow(R+292,y3+46,R+222,y3+46,G1))+T(R+226,y3+50,'連携',62,'s','text-align:center')
b+=T(R,y3+80,'「金属＝経済活動を支える礎」。社会に必要な資源を支えることを、私たちの責務と考えています。',W,'h','font-size:10.5px;line-height:1.6')
b+=LINE('M660,712 H1150',[(1150,712)])
b+=A(R,724,'',W,'',f'height:92px;background:{INK}')
b+=T(R+18,734,'グループミッション｜共に、資源の未来を築く',None,'k','color:#e9d6ac')
b+=T(R+18,752,'社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する',W-36,'hs','font-size:10.4px;color:#fff;line-height:1.5')
b+=T(R+18,794,'To contribute to a better society by providing a stable supply of high-quality mineral resources, in a sustainable way.',W-36,'s','color:#9aa1a8;font-family:IN')
b+=BAND(0,824,1190,18)
pages.append(spread(b,10,11,'',''))

links=''.join(f'<link rel="stylesheet" href="f/nsjp/package/{w}.css">' for w in (400,500,700))
open('daiwari_v20.html','w').write('<!doctype html><meta charset=utf-8>'+links+'<style>'+CSS2+'</style>'+''.join(pages))
