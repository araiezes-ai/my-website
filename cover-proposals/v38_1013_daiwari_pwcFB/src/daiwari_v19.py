# 台割 v19（10/13 PwC FB反映）— 案②（帯・アウトライン数字）のデザインで、全12P構成に再編
exec(open('v19_head.py').read())
import math
CU='#a8622f'   # 銅（金属資源グループのハイライト）
def kick(x,y,en,jp,col=BR): return T(x,y,en,None,'k',f'color:{col}')+T(x,y+11,jp,None,'kj')
def lead(x,y,t,w=None,size=11.5): return A(x,y,'',22,'',f'border-top:1.4px solid {RED}')+T(x,y+10,t,w,'h',f'font-size:{size}px')
def arrow(x1,y1,x2,y2,col=INK,sw=.8):
    a=math.atan2(y2-y1,x2-x1); h=4
    p1=(x2-h*math.cos(a-.5),y2-h*math.sin(a-.5)); p2=(x2-h*math.cos(a+.5),y2-h*math.sin(a+.5))
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{sw}"/><path d="M{p1[0]:.1f},{p1[1]:.1f} L{x2},{y2} L{p2[0]:.1f},{p2[1]:.1f}" fill="none" stroke="{col}" stroke-width="{sw}"/>'
def chev(cx,y,w=34,col=RED): return f'<path d="M{cx-w/2},{y} L{cx},{y+9} L{cx+w/2},{y}" fill="none" stroke="{col}" stroke-width="1.2"/>'
def badge(x,y,t,col=BR,d=16): return A(x,y,f'<div style="font-family:IT;font-weight:600;font-size:{d*.55}px;color:#fff">{t}</div>',d,'',f'height:{d}px;border-radius:50%;background:{col};display:flex;align-items:center;justify-content:center')
def msq(x,y,w,rows):
    o=''
    for i,(k_,v,d_) in enumerate(rows):
        yy=y+i*34; o+=rule(x,yy,w,INK if i==0 else G3,1 if i==0 else .6)
        o+=T(x,yy+7,k_,None,'l','font-size:5.8px;letter-spacing:1.4px;color:'+G2)+T(x+58,yy+5,v,w-58,'hs','font-size:9px;font-weight:700')+T(x+58,yy+19,d_,w-58,'s','font-size:6.2px')
    return o
pages=[]

# ================= P02-03  CORE MESSAGE / CONTENTS =================
b=tile(0,0,330,250,'r-022.png','50% 60%','都市','鉄・銅・アルミ')
b+=tile(334,0,261,123,'x_vc_ev.jpg','50% 55%','モビリティ','鉄・銅・リチウム')
b+=ptile(334,127,261,123,'鉄道','鉄・銅','鉄道の写真（ストック）')
b+=tile(0,254,163,146,'x_vc_wind.jpg','50% 30%','再生可能エネルギー','銅・鉄')
b+=tile(167,254,163,146,'x_case_pylon.jpg','50% 50%','送電網','銅・アルミ')
b+=ptile(334,254,261,146,'デバイス','銅・リチウム・ニッケル','スマートフォン・データセンターの写真（ストック）')
b+=tile(599,0,330,264,'mr_03_01@2x.webp','50% 50%','金属素材','暮らしを形づくる鉄・銅・アルミ',2000)
b+=tile(933,0,257,264,'x_vc_smelter.jpg','50% 50%','製錬・精製','')
b+=tile(599,268,257,132,'r-023.png','50% 60%','海上輸送','')
b+=tile(860,268,330,132,'r-054.png','50% 55%','銅地金','')
b+=kick(L,438,'コアメッセージ','私たちの存在意義')
b+=T(L,466,'Strength to Hold.<br>Power to Connect.',W,'dl','font-size:46px')
b+=lead(L,570,'持つ力と、つなぐ力。',None,15)
b+=para(L,604,300,'資源は、そこに「ある」だけでは、まだ価値ではありません。誰かが見出し、育て、必要とする場所へ届けて、はじめて力になる。私たちは、世界有数の資産に関わり、投資とトレーディングの両輪で川上から川下までをつなぎます。フェアな立場だからこそ、埋められる隙間がある。多様なパートナーと使い手の間に立ち、その時々の最適解を導く。世界に眠る価値を、社会の力へ。')
b+=kick(R,438,'目次','Contents')
toc=[('01','我々は何者か','三菱商事とは／金属資源グループとは','04'),('02','独自価値','投資とトレーディングの両輪／原料炭・銅・トレーディング・新技術','06'),('03','選ばれ続ける理由','Partner of Choice','10'),('04','何を実現するか','社会課題への取り組み','11')]
for i,(n,e,j,p) in enumerate(toc):
    y=466+i*72
    b+=rule(R,y,W,INK if i==0 else G3,1 if i==0 else .6)+T(R,y+10,n,None,'n','font-size:40px;color:'+BR)+T(R+84,y+14,e,None,'h','font-size:14px')+T(R+84,y+36,j,320,'s','font-size:7.2px')+T(R+W-34,y+16,'P.'+p,None,'fo')
b+=BAND(0,824,1190,18)
pages.append(spread(b,2,3,'',''))

# ================= P04-05  第1章 三菱商事とは → 金属資源グループとは =================
b=OUT(436,6,'01')
o,yy=head(L,40,'第1章','我々は何者か｜三菱商事とは','Who we are.','三綱領を精神の根幹に、「総合力」で価値を生む',size=44)
b+=o
b+=para(L,yy+4,250,'三菱商事は、三綱領を企業理念とし、事業を通じて経済価値・社会価値・環境価値の同時実現を目指しています。エネルギー、金属、機械、化学品、食品、生活産業まで、幅広い産業と地域にまたがる事業と人のつながり。その「総合力」こそが、三菱商事の強みです。')
# 7 groups ring → metals group highlighted, line opens to right page
cx,cy,rr=290,455,150
o=f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="none" stroke="{G3}" stroke-width=".8"/>'
angs=[0,51.4,102.8,154.3,205.7,257.1,308.6]
for i,a in enumerate(angs):
    t=math.radians(a-0); x=cx+rr*math.cos(t); y=cy+rr*math.sin(t)
    if i==0: continue
    o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="24" fill="#fff" stroke="{G2}" stroke-width=".8"/>'
mx_,my_=cx+rr,cy
o+=f'<circle cx="{cx}" cy="{cy}" r="74" fill="{PAN}" stroke="{INK}" stroke-width="1"/>'
# zoom lines from metals circle to right page panel
o+=f'<path d="M{mx_},{my_-24} L635,150 L635,800 L{mx_},{my_+24}Z" fill="{CU}" opacity=".06"/>'
o+=f'<line x1="{mx_}" y1="{my_-24}" x2="635" y2="150" stroke="{CU}" stroke-width=".7"/><line x1="{mx_}" y1="{my_+24}" x2="635" y2="800" stroke="{CU}" stroke-width=".7"/>'
o+=f'<circle cx="{mx_}" cy="{my_}" r="24" fill="{CU}"/>'
b+=S(o)
b+=T(cx-60,cy-22,'三菱商事',120,'h','text-align:center;font-size:14px')+T(cx-60,cy,'総合力',120,'k','text-align:center;color:'+BR)+T(cx-60,cy+12,'7つの営業グループ',120,'s','text-align:center')
b+=T(mx_-21,my_-7,'金属<br>資源',42,'l','text-align:center;color:#fff;font-family:Noto Sans JP;font-size:6.4px;font-weight:700;line-height:1.15')
b+=T(cx-150,cy+186,'金属資源グループは、7つの営業グループのうち、長年にわたり三菱商事を支えてきた中核グループの一つです。',300,'hs','text-align:center;font-size:8.2px')
b+=T(L,236,'総合力とは',None,'k')+T(L,250,'産業・地域・機能をまたぐ事業ポートフォリオと、そこから得られる知見・ネットワーク・信用。',220,'s')
# 三綱領
vy=704
b+=rule(L,vy,W-40,INK,1)+T(L,vy+10,'三綱領',None,'k')+T(L+60,vy+10,'三菱商事の企業理念',None,'kj')
for i,(j,r_,e) in enumerate([('所期奉公','しょきほうこう','事業を通じ、物心共に豊かな社会の実現に努力すると同時に、かけがえのない地球環境の維持にも貢献する'),('処事光明','しょじこうめい','公明正大で品格のある行動を旨とし、活動の公開性、透明性を堅持する'),('立業貿易','りつぎょうぼうえき','全世界的、宇宙的視野に立脚した事業展開を図る')]):
    x=L+i*160
    b+=T(x,vy+28,j,None,'h','font-size:13px')+T(x,vy+46,r_,150,'l','font-size:6.2px;color:'+BR)+T(x,vy+57,e,148,'s','font-size:6.2px')
# right page: 金属資源グループとは
b+=A(R-40,150,'',595,'',f'height:650px;background:linear-gradient(90deg,rgba(168,98,47,.05),rgba(168,98,47,0) 60%)')
o,yy=head(R,40,'第1章','我々は何者か｜金属資源グループとは','The core that has<br>carried us.','三綱領を体現する中核グループとして',size=34)
b+=o
b+=para(R,yy+4,W,'金属資源グループは、社会に不可欠な金属資源を世界から確保し、安定的に届ける役割を担ってきました。三綱領を事業で体現する中核グループとして、長年にわたり会社の屋台骨を支えています。')
py=yy+52
b+=A(R,py,'',W,'',f'height:84px;background:{INK}')
b+=T(R+16,py+12,'グループミッション',None,'k','color:#e9d6ac')+T(R+16,py+28,'社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する',W-32,'hs','font-size:10.5px;line-height:1.55;color:#fff')
cy2=py+104
b+=T(R,cy2,'長年の貢献',None,'k')+T(R+80,cy2,'会社の屋台骨として',None,'kj')
b+=T(R,cy2+18,'市況の波を越えて、全社の利益を長く支えてきた。',W,'h','font-size:12px')
b+=para(R,cy2+38,W,'資源価格には浮き沈みがあります。それでも事業から離れず、優良な資産に関わり続けてきたことが、三菱商事の利益の柱を長年にわたって支えてきました。')
jy=cy2+92
b+=rule(R,jy,W,INK,1)+T(R,jy+10,'歩み',None,'k')+T(R+50,jy+10,'先見性をもって、先手を打ってきた',None,'kj')
eras=[('1980〜90年代','日本の産業に、資源を。','トレーディングで参入し、少数出資から事業に関わる'),
      ('1990年代','仲介から、担い手へ。','投資モデルへ転換し、JV運営の知見を蓄える'),
      ('2000年代','一級資産に、早くから。','BHPと原料炭の合弁を組成し、事業経営に参画'),
      ('2010年代','次の柱を、先回りして。','銅へ領域を広げ、販売機能をRtMに集約'),
      ('2020年代〜','投資と販売を、一つの力に。','両輪を一体で動かす、グローバルな事業者へ')]
o=f'<line x1="{R}" y1="{jy+52}" x2="{R+W}" y2="{jy+52}" stroke="{INK}" stroke-width=".8"/>'
for i,(yr,th,ac) in enumerate(eras):
    x=R+i*104
    o+=f'<circle cx="{x+4}" cy="{jy+52}" r="3.6" fill="{CU if i in (2,3) else INK}"/>'
    b+=T(x,jy+30,yr,None,'nb','font-size:11px')+T(x,jy+62,th,98,'hs','font-size:8px;font-weight:700')+T(x,jy+88,ac,96,'s','font-size:6.2px')
b+=S(o)
py2=jy+136
b+=rule(R,py2,W,INK,1)+T(R,py2+10,'事業領域',None,'k')+T(R+70,py2+10,'原料炭と銅を中核に、世界に広がる取扱資源',None,'kj')
com=[('r-048.png','原料炭',1),('r-054.png','銅',1),('x_ironore.jpg','鉄鉱石',0),('x_case_mine.jpg','ニッケル',0),('x_lithium.jpg','リチウム',0),('x_alu.jpg','アルミ',0),(None,'肥料資源',0),('r-074.png','二次資源',0)]
xx=R+4; rowy=py2+66
for f,e,big in com:
    d=62 if big else 46; c=xx+d/2
    b+=(CIRC(c,rowy,d,f,ring=bool(big)) if f else A(c-d/2,rowy-d/2,'',d,'',f'height:{d}px;border-radius:50%;border:1px solid {BR}'))
    b+=T(c-34,rowy+d/2+6,e,68,'l','text-align:center;font-size:6.6px;font-weight:'+('600' if big else '400'))
    xx+=d+(16 if big else 14)
b+=BAND(0,824,1190,18)
pages.append(spread(b,4,5,'',''))

# ================= P06-07  第2章（導入） 独自価値：バリューチェーン全体像 =================
b=OUT(430,6,'02')
o,yy=head(L,40,'第2章','独自価値｜投資とトレーディングの両輪','Two wheels,<br>one flow.','資源の流れ全体に関わり、互いを強め合ってきた',size=44)
b+=o
b+=para(R,110,330,'投資とトレーディングの両輪で、資源の流れ全体に関わる。互いを強め合いながら、長い時間をかけて積み重ねてきたこと。それが、鉱山会社でも純粋なトレーダーでもない、金属資源グループならではの強さです。',)
# central diagram
dy=380; xs=[L+60,L+300,L+555,L+810,L+1050]
stg=[('x_vc_mine.jpg','川上','鉱山・資源開発'),('_mr_project_06.png','中間流通','トレーディング'),('x_vc_smelter.jpg','川中','製錬・製鉄'),('r-072.png','中間流通','トレーディング'),('x_vc_ev.jpg','川下','需要家・最終製品')]
o=f'<line x1="{xs[0]}" y1="{dy}" x2="{xs[-1]}" y2="{dy}" stroke="{INK}" stroke-width=".8"/>'
for i in range(4): o+=arrow(xs[i]+44,dy,xs[i+1]-46,dy,INK,.9)
# investment arc (above) and trading arc (below)
o+=f'<path d="M{xs[0]},{dy-48} C{xs[0]},{dy-120} {xs[2]},{dy-120} {xs[2]},{dy-48}" fill="none" stroke="{BR}" stroke-width="2.4"/>'
o+=f'<path d="M{xs[0]},{dy+76} C{xs[0]+40},{dy+140} {xs[4]-40},{dy+140} {xs[4]},{dy+76}" fill="none" stroke="{NV}" stroke-width="2.4"/>'
# reinforcing loop B
lx,ly=(xs[1]+xs[2])/2+60,dy-150
o+=f'<path d="M{lx-26},{ly} A26,26 0 1 1 {lx+18},{ly+18}" fill="none" stroke="{G1}" stroke-width="1"/>'+arrow(lx+24,ly+12,lx+18,ly+18,G1,1)
# new tech line C
ty_=dy+160
o+=f'<line x1="{xs[0]}" y1="{ty_}" x2="{xs[-1]}" y2="{ty_}" stroke="{CU}" stroke-width="1" stroke-dasharray="3 3"/>'
for x in (xs[0]+120,xs[1]+120,xs[3]+120,xs[4]-60): o+=f'<line x1="{x}" y1="{ty_}" x2="{x}" y2="{dy+10}" stroke="{CU}" stroke-width=".6" stroke-dasharray="2 2"/><circle cx="{x}" cy="{ty_}" r="3" fill="{CU}"/>'
b+=S(o)
for (f,e,j),x in zip(stg,xs):
    b+=CIRC(x,dy,84,f)+T(x-60,dy+50,e,120,'l','text-align:center;font-size:7.6px;font-weight:600')+T(x-60,dy+62,j,120,'s','text-align:center')
b+=T(xs[0]+60,dy-118,'<span style="color:'+BR+'">資源投資</span>　鉱山・製錬への出資　<span class="s">鉄鋼原料本部・クリティカルミネラル本部</span>',440,'hs','font-size:8.4px;font-weight:700')
b+=T(xs[1]+60,dy+126,'<span style="color:'+NV+'">トレーディング（RtM）</span>　川上から川下まで、流れをつなぐ　<span class="s">金属資源トレーディング本部</span>',600,'hs','font-size:8.4px;font-weight:700')
b+=T(lx-52,ly-12,'',None,'')+T(lx+34,ly-14,'市場の情報を投資へ<br>投資の資源を市場へ',120,'s','font-size:6.4px')
b+=T(xs[0]-14,ty_+8,'新技術への投資　業界のボトルネックに挑む技術が、流れ全体を進化させる',600,'s','color:'+CU+';font-size:6.8px')
# letter markers on diagram
b+=badge(xs[0]-40,dy-130,'A')+badge(lx-48,ly-30,'B')+badge(xs[4]+24,ty_-8,'C',CU)+badge(xs[4]+40,dy-60,'E',RED)
dyy=ty_+40
b+=S(f'<line x1="{xs[0]}" y1="{dyy}" x2="{xs[-1]}" y2="{dyy}" stroke="{INK}" stroke-width="1.2"/>'+arrow(xs[-1]-10,dyy,xs[-1]+6,dyy,INK,1.2))
b+=badge(xs[0]-40,dyy-8,'D',INK)+T(xs[0],dyy+6,'長い時間をかけて、流れに関わり続ける',400,'s','font-size:6.8px;color:'+INK)
b+=T(xs[4]-120,dy-70,'原料炭・銅・トレーディング　→ P.08',140,'s','font-size:6.6px;color:'+RED+';text-align:right')
# A-E cards
cards=[('A','持つ力・つなぐ力','投資とトレーディングの両輪','資源に投資して育てる力と、市場へ届ける力の両方を持つ。鉱山会社でも、純粋なトレーダーでもない立ち位置。',BR),
       ('B','互いを強め合う','一方通行ではない循環','トレーディングで得た市場の情報を投資判断に生かし、投資で得た資源をトレーディングで市場へ届ける。',G1),
       ('C','流れ全体を進化させる','新技術への投資','業界の課題に挑む新技術に投資し、その知見を投資とトレーディングの両方に還元する。',CU),
       ('D','長い時間をかけて','積み重ねが先見性に','市況の浮き沈みに左右されず、流れに関わり続けてきた。その積み重ねが、先を見据えて手を打つ力になる。',INK),
       ('E','その結果としての、いま','原料炭・銅・トレーディング','強みがあることの「結果」として、いまの主力事業がある。→ 次ページへ',RED)]
cy_=650
for i,(k_,e,j,d_,col) in enumerate(cards):
    x=L+i*226
    b+=A(x,cy_,'',210,'',f'border-top:1.4px solid {col}')+badge(x,cy_+10,k_,col,18)+T(x+26,cy_+10,e,180,'hs','font-size:9px;font-weight:700')+T(x+26,cy_+24,j,180,'s','font-size:6.4px;color:'+col)+T(x,cy_+44,d_,205,'b','font-size:7px;line-height:1.75')
b+=BAND(0,824,1190,18)
pages.append(spread(b,6,7,'',''))

# ================= P08-09  第2章 主力3事業＋新技術 =================
b=''
cols=[(L,255),(L+280,255),(R,W)]
# --- coal
x,w=cols[0]
b+=tile(x,40,w,92,'r-047.png','60% 40%')
b+=kick(x,146,'PILLAR 1　原料炭事業','鉄の主原料“産業のコメ”')
b+=T(x,172,'World-class<br>metallurgical coal.',w,'d','font-size:20px')+lead(x,220,'社会に欠かせない資源を、世界最高品位で',w,9.4)
b+=para(x,250,w,'原料炭は鉄の主原料。鉄はこれからも底堅く必要とされます。BHPと50:50の合弁BMAを通じ、豪州ボーエン・ベースンの世界最高品位の炭鉱に参画。長期にわたるコミットメントで、一級資産を育ててきました。','font-size:6.9px')
b+=msq(x,318,w,[('MARKET','上位5社で約80%','寡占度が高く、供給は漸減'),('SCALE','一級強粘炭の約50%','BMAが世界供給に占めるシェア'),('QUALITY','高品位の炭鉱に厳選','港湾・鉄道まで保有し、山から港までを一体運営')])
vy=428
b+=T(x,vy,'高品位への集約',None,'k')+T(x+80,vy,'7炭鉱から5炭鉱へ',None,'kj')
o=''
for i in range(7):
    cx_=x+16+i*20; keep=i<5
    o+=f'<circle cx="{cx_}" cy="{vy+30}" r="7" fill="{BR if keep else "#fff"}" stroke="{BR if keep else G3}" stroke-width="1"/>'
o+=arrow(x+156,vy+30,x+176,vy+30,INK)
for i in range(5): o+=f'<circle cx="{x+188+i*14}" cy="{vy+30}" r="5" fill="{BR}"/>'
b+=S(o)+T(x,vy+44,'中品位の2炭鉱を売却し、高品位の5炭鉱に集約。',w,'s')
b+=T(x,vy+62,'<b style="font-family:IN;font-weight:600;color:'+INK+'">MDP</b>（三菱商事100%）　50%　＋　<b style="font-family:IN;font-weight:600;color:'+INK+'">BHP</b>　50%　→　<b style="font-family:IN;font-weight:600;color:'+BR+'">BMA</b>',w,'s','font-size:6.6px')
# --- copper
x,w=cols[1]
b+=tile(x,40,w,92,'mr_02_01@2x.webp','50% 50%',mx=1400)
b+=kick(x,146,'PILLAR 2　銅事業','電化と成長を支えるクリティカルミネラル')
b+=T(x,172,'The partner the copper<br>industry calls first.',w+10,'d','font-size:20px')+lead(x,220,'日本最大の銅生産者として、業界から声がかかる',w,9.4)
b+=para(x,250,w,'銅は電化と経済成長を支える資源です。特定の1社と深く組むのではなく、主要メジャーのほとんどと共同で事業を行い、ジュニア鉱山からも立場を保ったまま組める相手として選ばれています。','font-size:6.9px')
b+=msq(x,318,w,[('MARKET','上位5社で約25%','寡占化が進まず、再編の機運'),('SCALE','持分生産量で日本最大','パートナー型の生産者として世界最大級'),('QUALITY','5鉱山すべてが世界Top15','生産コストは世界の上位25%')])
vy=428
b+=T(x,vy,'参画鉱山',None,'k')+T(x+60,vy,'世界の鉱山別生産量ランキング',None,'kj')
o=f'<line x1="{x}" y1="{vy+34}" x2="{x+w}" y2="{vy+34}" stroke="{G3}" stroke-width="3" stroke-linecap="round"/>'
X=lambda r: x+6+(r-1)/14*(w-12)
for r_ in (1,5,10,15): b+=T(X(r_)-8,vy+42,f'{r_}位',None,'s','font-size:5.4px;font-family:IN')
mines=[(1,'Escondida','チリ',-1),(4,'Antamina','ペルー',1),(10,'Anglo American Sur','チリ',-1),(12,'Los Pelambres','チリ',1),(15,'Quellaveco','ペルー',-1)]
for r_,n,c,sd in mines:
    xx=X(r_); o+=f'<circle cx="{xx:.1f}" cy="{vy+34}" r="4" fill="{BR}" stroke="#fff" stroke-width="1"/>'
    b+=T(xx-40,vy+(14 if sd<0 else 50),f'<b style="font-family:IN;font-weight:600;color:{INK}">{n}</b> {c}',80,'s','text-align:center;font-size:5.6px')
b+=S(o)+T(x,vy+66,'開発中：Marimaca（チリ）・Copper World（米国）',w,'s','font-size:6.2px')
# --- trading (right page)
x,w=cols[2]
b+=tile(x,40,w,92,'r-023.png','50% 60%')
b+=kick(x,146,'PILLAR 3　トレーディング事業（RtM）','Resource to Market')
b+=T(x,172,'Resource to Market.',w,'d','font-size:20px')+lead(x,200,'資源と市場をつなぎ、必要な場所へ確かに届ける',w,9.4)
for i,(n,j) in enumerate([('15','業界'),('50','カ国'),('約1,000','社の販売先')]):
    xx=x+i*120; b+=T(xx,230,n,None,'nb','font-size:30px')+T(xx,264,j,None,'s')
    if i<2: b+=T(xx+92,238,'×',None,'','font-size:14px;color:'+BR)
pts3=[('自社アセットに限らず、第三者の資源も扱う','顧客との接点から得た市場の生きた情報を、投資の側に返す。'),('ロジ・在庫・ヘッジなど幅広いサービス','資源を引き受けたうえで、機能を付けて顧客に届ける。'),('アジアに限らない、グローバルな販売網','欧州・シンガポール・米州など、幅広い産業と国の顧客へ。')]
for i,(h_,d_) in enumerate(pts3):
    y=290+i*42; b+=rule(x,y,250)+T(x,y+6,f'0{i+1}',None,'nb','font-size:12px;color:'+NV)+T(x+22,y+7,h_,228,'hs','font-size:8px;font-weight:700')+T(x+22,y+21,d_,228,'s','font-size:6.2px')
# RtM model
mx0=x+280; mw=235
b+=T(mx0,290,'ビジネスモデル',None,'k','color:'+NV)
b+=A(mx0,306,'<div class="l" style="font-size:6.4px">第三者の資源</div>',110,'',f'height:24px;border:1px solid {G2};display:flex;align-items:center;justify-content:center')
b+=A(mx0+125,306,'<div class="l" style="font-size:6.4px">三菱商事の保有資産</div>',110,'',f'height:24px;border:1px solid {BR};display:flex;align-items:center;justify-content:center')
b+=A(mx0,350,'<div style="font-family:IT;font-weight:600;font-size:13px;color:#fff">RtM</div>',mw,'',f'height:30px;background:{NV};display:flex;align-items:center;justify-content:center')
b+=A(mx0,400,'<div class="l" style="font-size:6.4px">世界の顧客（15業界・50カ国）</div>',mw,'',f'height:24px;border:1px solid {INK};display:flex;align-items:center;justify-content:center')
o=arrow(mx0+55,330,mx0+55,348,NV)+arrow(mx0+180,330,mx0+180,348,NV)+arrow(mx0+70,380,mx0+70,398,NV)+arrow(mx0+165,398,mx0+165,380,BR)
b+=S(o)+T(mx0+80,384,'安定供給',None,'s','font-size:5.6px')+T(mx0+172,384,'市場の情報',None,'s','font-size:5.6px;color:'+BR)
b+=T(mx0,436,'多様な取引機能',None,'k','color:'+NV)
for i,t in enumerate(['取扱商品の広さ','在庫','輸送手配','ヘッジ']):
    b+=A(mx0+i*60,452,f'<div class="s" style="font-size:6.2px;color:{INK}">{t}</div>',56,'',f'height:26px;border-top:1.4px solid {NV};background:{PAN};display:flex;align-items:center;justify-content:center;text-align:center')
# --- NEW TECHNOLOGY (bottom, across spread)
ny=520
b+=A(0,ny-12,'',1190,'',f'height:306px;background:{PAN}')
b+=kick(L,ny,'NEW TECHNOLOGY　新技術','資源業界のボトルネックに挑む')
b+=T(L,ny+26,"Investing in what's next.",W,'d','font-size:24px')+lead(L,ny+58,'課題を解く技術に投資し、現場に取り入れる',W,9.4)
b+=para(L,ny+86,250,'資源の流れの中で業界の課題になっている部分を見極め、課題を解く技術を持つスタートアップに出資しています。トレーディングや業界とのつながりを生かして技術を現場に取り入れ、得られた知見を既存事業の高度化に還元しています。','font-size:6.9px')
# simplified copper chain
cx0=L+275; st=[('鉱石','採掘','Cu 約1%'),('銅精鉱','選鉱・浸出','Cu 20〜30%'),('銅地金','製錬・精製','Cu 99.99%'),('最終用途','電化・インフラ','需要家へ'),('リサイクル','回収','再び供給へ')]
o=''
for i,(e,j,g_) in enumerate(st):
    xx=cx0+i*100; y=ny+86
    b+=A(xx,y,'',92,'',f'height:46px;background:#fff;border-top:1.4px solid {INK}')+T(xx+8,y+6,e,None,'l','font-size:7.4px;font-weight:600')+T(xx+8,y+18,j,None,'s')+T(xx+8,y+30,g_,None,'nb','font-size:9px;color:'+CU)
    if i<4: o+=arrow(xx+93,y+23,xx+99,y+23,INK)
techs=[(1,'CiDRA','選鉱','浮遊選鉱の高度化で、回収率と処理能力を高める'),(1,'Jetti','浸出','新たな触媒で、硫化鉱から銅を回収する'),(4,'DESCycle','リサイクル','電子スクラップから銅・貴金属を回収する')]
for k_,(si,n,t_,d_) in enumerate(techs):
    xx=cx0+k_*170; y=ny+176; sx_=cx0+si*100+46+(-14 if k_==0 else 14 if k_==1 else 0)
    o+=f'<path d="M{sx_},{ny+133} V{ny+156} H{xx+12} V{y}" fill="none" stroke="{CU}" stroke-width=".8"/><circle cx="{sx_}" cy="{ny+133}" r="2.4" fill="{CU}"/>'
    b+=A(xx,y,f'<div style="font-family:IN;font-weight:600;font-size:5.6px;letter-spacing:1.2px;color:{CU}">{t_.upper() if False else t_}｜スタートアップ</div><div class="l" style="font-weight:600;font-size:9.5px;margin-top:2px">{n}</div><div class="s" style="margin-top:2px">{d_}</div>',158,'',f'height:56px;padding:7px 10px;border-top:1.4px solid {CU};background:#fff')
b+=S(o)
# Jetti case
jx=cx0+520; jw=1150-jx
b+=A(jx,ny,'',jw,'',f'height:290px;background:#fff')
b+=T(jx+14,ny+12,'取り組み事例',None,'k','color:'+CU)+T(jx+14,ny+28,'Jetti × 三菱商事',jw-28,'h','font-size:12px')
b+=T(jx+14,ny+50,'銅生産の革新技術を持つスタートアップと、銅資源開発・トレーディングのリーディングプレイヤーによる価値共創。',jw-28,'hs','font-size:7.6px;font-weight:700')
b+=para(jx+14,ny+92,jw-28,'銅鉱石からの銅分回収に関する革新技術を持つ米Jettiに出資参画し、事業拡大を支援しています。同社技術で生産される環境価値の高い銅地金を販売するほか、当社の銅事業のネットワークを生かし、低品位の鉱石からの銅分回収に課題を抱える鉱山に同社技術が導入されるよう、共同で検討しています。','font-size:6.8px')
b+=ptile(jx+14,ny+156,jw-28,110,'JETTI','技術・現場写真','Jetti提供写真（素材待ち）')
b=BAND(0,0,1190,18,'brush_b')+b
pages.append(spread(b,8,9,'',''))

# ================= P10  第3章 Partner of Choice ／ P11 第4章 社会課題 =================
b=OUT(436,6,'03')+OUT(1000,6,'04')
o,yy=head(L,40,'第3章','選ばれ続ける理由','Partner of choice.','資源業界に不可欠な存在として、選ばれ続ける',size=40)
b+=o
b+=para(L,yy+4,330,'資源メジャーをはじめとするパートナーと長期にわたって事業を共に育て、単なる共同出資者に留まらない貢献を重ねてきました。その積み重ねが、資源業界に不可欠な存在として選ばれ続ける理由です。')
b+=CIRC(L+440,yy-40,140,'r-084.png')
ry=yy+70
four=[('資源メジャーとの企業文化的親和性','短期の成果を求める投資家とは一線を画す、中長期の視座'),('資源投資経験に裏打ちされたJV経営力','実質的な経営貢献と、高い目利き力'),('事業ポートフォリオを生かした健全な財務基盤','リスクを分かち合い、制度金融の活用も後押し'),('マクロ環境とバリューチェーンへの深い知見','国・地域の拠点と、幅広い産業との接点から得る知見')]
for i,(e,d_) in enumerate(four):
    x=L+(i%2)*262; y=ry+(i//2)*56
    b+=T(x,y,f'0{i+1}',None,'nb','font-size:18px;color:'+BR)+T(x+30,y+2,e,220,'hs','font-size:8.2px;font-weight:700')+T(x+30,y+16,d_,220,'s','font-size:6.4px')
jy=ry+136
b+=rule(L,jy,W,INK,1)+T(L,jy+10,'JVへの貢献',None,'k')+T(L+80,jy+10,'経営から現場まで伴走する',None,'kj')
bx=[(L,'経営',['中長期の操業計画・資本政策・販売戦略・人事計画への参画','各レイヤーへの人材配置を通じた実務貢献','他のJVで得たベストプラクティスの導入','生産物の引き取り・販売を通じた支援']),(L+262,'現場',['長期目線での戦略策定と案件開発','幅広い産業接点を生かした知見の提供','優良鉱山で培った操業ノウハウの展開','専門人材の派遣による操業支援'])]
for x,t_,items in bx:
    b+=A(x,jy+30,f'<div class="hs" style="font-size:9px;font-weight:700;color:#fff">{t_}</div>',252,'',f'height:24px;padding:5px 10px;background:{BR}')
    b+=A(x,jy+54,'<br>'.join('— '+s_ for s_ in items),252,'s',f'font-size:7px;line-height:2;padding:8px 10px;background:{PAN};height:86px')
fy=jy+170
steps=['資源メジャー各社と「会社対会社」の関係へ','新たな協業が生まれる','協業の積み重ねが、さらなる強み・知見・信頼に']
o=''
for i,t_ in enumerate(steps):
    y=fy+i*48
    b+=A(L,y,f'<div class="hs" style="font-size:{9.4 if i==0 else 8.4}px;font-weight:700;color:{"#fff" if i==0 else INK}">{t_}</div>',W-60,'',f'height:28px;padding:6px 12px;background:{INK if i==0 else PAN}')
    if i<2: o+=chev(L+(W-60)/2,y+31)
o+=f'<path d="M{L+W-58},{fy+110} H{L+W-6} V{jy+20}" fill="none" stroke="{BR}" stroke-width=".9"/>'+arrow(L+W-6,jy+40,L+W-6,jy+20,BR,.9)
b+=S(o)
b+=T(L,fy+150,'主なJVパートナー　BHP ／ Rio Tinto ／ Anglo American ほか',W,'s','font-size:6.6px')
b+=tile(L,fy+172,252,806-fy-172-8,'_mr_project_03.png','50% 50%','銅鉱山','チリ')+tile(L+262,fy+172,253,806-fy-172-8,'r-075.png','50% 60%','操業','')
# P11
o,yy=head(R,40,'第4章','何を実現するか','Building the future<br>of resources, together.','社会の「当たり前」を、支え続ける',size=32)
b+=o
ey=yy+14
b+=T(R,ey,'外部環境と社会課題',None,'k')
env=[('産業構造の転換','脱炭素化に加え、生成AI・データセンターの普及で電力需要が拡大。銅・アルミ・電池資源など基幹素材の重要性が増す。'),('供給制約の深刻化','良質な資源の開発はより難しく、時間とコストがかかるように。'),('地政学リスクの常態化','資源の囲い込みや国家間の対立が、サプライチェーンに構造的に影響する。')]
for i,(e,d_) in enumerate(env):
    x=R+i*176
    b+=A(x,ey+16,f'<div class="hs" style="font-size:8.6px;font-weight:700">{e}</div><div class="s" style="margin-top:4px;font-size:6.3px">{d_}</div>',166,'',f'height:92px;padding:9px 10px;border-top:1.4px solid {INK};background:{PAN}')
o=chev(R+W/2,ey+118)
b+=A(R,ey+136,'<div class="hs" style="font-size:8.6px;font-weight:700;color:#fff;text-align:center">クリティカルミネラルのサプライチェーン確保の重要性と、川上資源への参入障壁が増大</div>',W,'',f'height:26px;padding:6px 10px;background:{INK}')
o+=chev(R+W/2,ey+170)
ty2=ey+192
b+=T(R,ty2,'私たちの取り組み',None,'k')+T(R+100,ty2,'資源の安定供給と、効率的な供給で社会を支える',None,'kj')
inv=['銅などの基幹事業で、大規模資産の持分を確保','成長が期待される領域に、早い段階から参画','信頼できるパートナーと、投資先の価値向上を推進']
trd=['権益の引き取りと外部調達で、安定供給の体制を確立','需給の変化をつかみ、試験的な取引から先行して動く','国際的な取引基盤を生かし、業界のネットワークを築く']
for x,t_,col,items in [(R,'資源投資',BR,inv),(R+300,'トレーディング',NV,trd)]:
    b+=A(x,ty2+18,f'<div class="hs" style="font-size:9px;font-weight:700;color:#fff">{t_}</div>',215,'',f'height:24px;padding:5px 10px;background:{col}')
    b+=T(x,ty2+48,'<br>'.join('— '+s_ for s_ in items),215,'s','font-size:6.6px;line-height:1.9')
o+=f'<path d="M{R+228},{ty2+40} H{R+288}" stroke="{G1}" stroke-width=".9"/>'+arrow(R+280,ty2+40,R+290,ty2+40,G1)+arrow(R+236,ty2+52,R+226,ty2+52,G1)+f'<path d="M{R+236},{ty2+52} H{R+290}" stroke="{G1}" stroke-width=".9"/>'
b+=T(R+228,ty2+58,'連携',60,'l','text-align:center;font-size:6.6px')
o+=chev(R+W/2,ty2+122)
b+=S(o)
cy3=ty2+146
b+=T(R,cy3,'「金属＝経済活動を支える礎」。社会に必要な資源を支えることを、私たちの責務と考えています。',W,'h','font-size:11px;line-height:1.6')
b+=A(R,cy3+50,'',W,'',f'height:170px;background:{INK}')
b+=T(R+20,cy3+68,'共に、資源の未来を築く',None,'k','color:#e9d6ac')
b+=T(R+20,cy3+88,'To contribute to a better society by providing a stable supply of high-quality mineral resources that society needs, in a sustainable way.',W-40,'dl','font-size:13px;color:#fff;line-height:1.3')
b+=T(R+20,cy3+140,'社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する。',W-40,'hs','font-size:8.6px;color:#fff')
b+=T(R+20,cy3+186,'持続可能で豊かな未来を、共に築くパートナーとして。',W-40,'s','color:#c9ced3')
b+=BAND(0,824,1190,18)
pages.append(spread(b,10,11,'',''))

links=''.join(f'<link rel="stylesheet" href="f/nsjp/package/{w}.css">' for w in (400,500,700))
open('daiwari_v19.html','w').write('<!doctype html><meta charset=utf-8>'+links+'<style>'+CSS2+'</style>'+''.join(pages))
