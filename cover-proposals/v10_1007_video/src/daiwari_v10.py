# 台割 案③ — 動画の流れ（社会→Who we are→強み→原料炭→銅→資源から価値へ→パートナーシップ→バリューチェーン→締め）に合わせた順番
exec(open('v10_head.py').read())
CSS+=""".wt{color:#fff!important}
.hero{font-weight:200;color:#fff;line-height:.92;letter-spacing:-3px}
.tag{font-size:6px;letter-spacing:1.8px;color:#fff;border:.6px solid rgba(255,255,255,.7);border-radius:9px;padding:2px 8px}
"""
def placeholder(x,y,w,h,label,r=0):
    return A(x,y,f'<span class="sm" style="color:#6d87a1">{label}</span>',w,'',f'height:{h}px;border-radius:{r}px;background:radial-gradient(circle at 30% 25%,#fff,{GLASS} 60%,#d3e0ec);display:flex;align-items:center;justify-content:center;text-align:center;padding:6px')
def lens(cx,cy,d,f=None,label='',pos='50% 50%'):
    if f: return CIRC(cx,cy,d,f,pos)
    return placeholder(cx-d/2,cy-d/2,d,d,label,d/2)+f'<div class="a" style="left:{cx-d/2-4}px;top:{cy-d/2-4}px;width:{d+8}px;height:{d+8}px;border-radius:50%;border:.6px solid {GOLDL}"></div>'
pages=[]

# =================== P02-03  OPENING：社会と金属 ===================
FG=uri('v9/globe_new.png',1400,'PNG')
gx,gy,gd=315,520,420
_s=gd/875
b=f'<img class="a" src="{FG}" style="left:{gx-755*_s:.1f}px;top:{gy-515*_s:.1f}px;width:{1536*_s:.1f}px;height:{1024*_s:.1f}px">'
ring=f'<ellipse cx="{gx}" cy="{gy}" rx="245" ry="125" transform="rotate(-10 {gx} {gy})" fill="none" stroke="{GOLD}" stroke-width=".8"/>'
b=svg(0,0,1190,842,ring.replace(f'stroke="{GOLD}"',f'stroke="{GOLDL}"'))+b
life=[('x_ch076.jpg','Cities','都市・ビル',200),('x_case_pylon.jpg','Power','電力網',250),('x_vc_ev.jpg','Mobility','自動車・EV',300),(None,'Railways','鉄道',345),('x_vc_wind.jpg','Energy','再生可能エネルギー',30),(None,'Devices','スマートフォン',90),('x_ch080.jpg','Trade','物流・港湾',140)]
for f,e,j,a in life:
    t=math.radians(a); x=gx+245*math.cos(t); y=gy+125*math.sin(t); r=math.radians(-10)
    X=gx+(x-gx)*math.cos(r)-(y-gy)*math.sin(r); Y=gy+(x-gx)*math.sin(r)+(y-gy)*math.cos(r)
    b+=lens(X,Y,74,f,'画像<br>（ストック）')+A(X-40,Y+42,e,80,'','text-align:center;font-size:6.8px;font-weight:400')+A(X-40,Y+52,j,80,'sm','text-align:center;font-size:5.8px')
b+=svg(0,0,1190,842,f'<path d="M{gx-245*math.cos(math.radians(10))+4},{gy+245*math.sin(math.radians(10))-2} A245,125 -10 0 0 {gx+245*math.cos(math.radians(10))-4},{gy-245*math.sin(math.radians(10))+2}" fill="none" stroke="{GOLD}" stroke-width=".9"/>')
b+=A(L,52,'INTRODUCTION',None,'lab')+A(L,63,'導入　社会と金属',None,'labj')
b+=A(L,86,'Metals power<br>everyday life.',W,'en','font-size:34px')
b+=A(L,166,'',26,'',f'border-top:1px solid {RED}')+A(L,176,'私たちの暮らしを支える金属',None,'jt')+A(L,193,'ビル、鉄道、車、スマートフォン——豊かな暮らしに、金属は欠かせない',None,'js')
# right page: rising demand -> core message -> contents
b+=SEC(R,56,'A WORLD OF RISING DEMAND','人口増加と途上国の発展で、世界の需要は拡大している')
fz=[('Demand shift','人口増・電化による<br>需要拡大'),('Supply constraints','供給制約の深刻化'),('Geopolitics','地政学リスクの常態化')]
for i,(e,j) in enumerate(fz):
    x=R+60+i*190; y=140
    b+=sph(x,y,96,i)+A(x-55,y-14,f'<div style="font-size:8px;font-weight:400">{e}</div><div class="sm" style="font-size:5.8px;margin-top:2px">{j}</div>',110,'','text-align:center')
b+=svg(R,196,W,40,f'<path d="M60,0 L250,28 L440,0 M250,0 L250,28" fill="none" stroke="{GOLD}" stroke-width=".7"/><circle cx="250" cy="28" r="2.6" fill="{GOLD}"/>')
b+=A(R,232,'社会が必要とする金属を、持続可能な形で届け続けるために——',W,'smb','font-size:8.2px')
b+=A(R,280,'Strength to Hold.<br>Power to Connect.',W,'en','font-size:38px;line-height:1.1')
b+=A(R,374,'',26,'',f'border-top:1px solid {RED}')+A(R,386,'コアメッセージ（英文主体・和文は確認用）',None,'labj')
b+=BODY(R,404,330,60,'font-size:7.8px;line-height:1.75')
toc=[('Who We Are','三菱商事 金属資源グループとは','04'),('Our Strengths','強み：世界の優良資産','05'),('Metallurgical Coal &amp; Copper','原料炭と銅','06'),('From Resources to Value','資源から価値へ','08'),('Global Partnerships','パートナーシップと販売網','09'),('Integrated Value Chain','川上から川下までをつなぐ','10')]
b+=A(R,560,'CONTENTS',None,'sec')
for i,(e,j,p) in enumerate(toc):
    y=580+i*33
    b+=A(R,y,'',W-40,'',f'border-top:.5px solid {HAIR}')+A(R,y+8,f'0{i+1}',None,'num','font-size:14px;color:'+GOLD)
    b+=A(R+36,y+6,e,None,'','font-size:9.4px;font-weight:300')+A(R+36,y+19,j,None,'sm','font-size:5.8px')+A(R+W-60,y+9,'P.'+p,None,'fo')
orb=flow('M560,330 C600,284 700,272 1200,266',GOLDL,.7,.9)
pages.append(spread(b,2,3,'動画01 OPENING と同じ入り。地球を中心に、暮らしを支える金属の場面（都市・電力・EV・鉄道・再エネ・スマホ・物流）を金の軌道上に並べる。鉄道・スマホは素材待ち。','外部環境（需要拡大・供給制約・地政学）を冒頭に置き、「だから私たちが必要」とコアメッセージにつなぐ。目次は動画と同じ6項目。',orb))

# =================== P04 Who we are（軽め） / P05 Our strengths（資産の大きさ） ===================
b=placeholder(0,0,595,330,'三菱商事 本社ビル・世界各地で働く社員の画像（MC様ご提供／動画02と共通素材）')
b+=svg(0,0,595,842,f'<path d="M0,330 C200,348 420,342 595,316" fill="none" stroke="{GOLD}" stroke-width=".8"/>')
o,yy=H2(L,368,'01　WHO WE ARE','第1章　我々は何者か','Who we are.','三菱商事 金属資源グループとは','世界の金属業界を牽引する力',body=50,bw=330)
b+=o
b+=BIG(380,340,'01')
cols=[('MISSION','グループミッション','社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する'),
      ('TWO WHEELS','投資×トレーディング','資源投資（鉄鋼原料本部・クリティカルミネラル本部）と、トレーディング（金属資源トレーディング本部）の両輪'),
      ('HERITAGE','時代を先読みした変革','トレーディングから投資へ、そしてグローバルなトレーダーへ。事業モデルを変え続けてきた')]
for i,(e,j,t) in enumerate(cols):
    x=L+i*170; y=yy+30
    b+=A(x,y,'',150,'',f'border-top:.6px solid {GOLD}')+A(x,y+10,e,None,'sec','font-size:7px')+A(x,y+24,j,150,'smb')+A(x,y+42,t,150,'sm')
b+=A(L,yy+140,'Guided by the Three Corporate Principles of Mitsubishi Corporation.',W,'bd','font-size:6.4px;color:'+MUTE)
# P05 — map of assets, emphasized
b+=A(R,52,'02　OUR STRENGTHS',None,'lab')+A(R,63,'第2章　独自価値',None,'labj')
b+=A(R,86,'Our strengths.',W,'en','font-size:30px')
b+=A(R,130,'',26,'',f'border-top:1px solid {RED}')+A(R,140,'強みは、原料炭と銅',None,'jt')+A(R,157,'世界各地の優良資産から、資源を安定的に確保する',None,'js')
b+=BIG(985,30,'02')
MW=640; MH=MW*996/2600; mx,my=R-46,215
b+=IMG(mx,my,MW,MH,'v8/flat_std.png',fmt='PNG',light=.3,mx=2000)
P=lambda lon,lat:(mx+(lon+170)/360*MW,my+(80-lat)/138*MH)
COAL=[(148.3,-22.3)]; COP=[(-69.07,-24.27),(-70.5,-31.7),(-70.3,-33.15),(-77.05,-9.53),(-70.6,-17.1),(-70.3,-22.9),(-110.9,31.9)]
OTH=[(-66.9,52.9),(-71.2,-28.5),(-128.9,58.5),(121.4,-30.7),(-94.0,51.6),(141.7,-13.3),(25.7,64.2),(-0.6,54.4)]
o=''
for lo,la in OTH: x,y=P(lo,la); o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="#fff" stroke="{GOLD}" stroke-width="1"/>'
for lo,la in COAL+COP:
    x,y=P(lo,la); o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="16" fill="{GOLD}" opacity=".12"/><circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="{GOLD}" opacity=".22"/><circle cx="{x:.1f}" cy="{y:.1f}" r="3.6" fill="{GOLD}" stroke="#fff" stroke-width=".8"/>'
b+=svg(0,0,1190,842,o)
for (lo,la),t,dx,dy in [((148.3,-22.3),'Metallurgical Coal<br><span class="sm">Queensland, Australia</span>',-130,-26),((-70.6,-22),'Copper<br><span class="sm">Chile · Peru</span>',22,-6),((-110.9,31.9),'Copper<br><span class="sm">USA</span>',-70,-22)]:
    x,y=P(lo,la); b+=A(x+dx,y+dy,t,120,'','font-size:8px;font-weight:400;line-height:1.3')
ky=my+MH+30
b+=A(R,ky,'',W,'',f'border-top:.6px solid {HAIR}')
for i,(n,u,t) in enumerate([('2','pillars','原料炭と銅、2つの柱'),('5 / 5','Top15 mines','銅の主要5鉱山すべてが世界Top15'),('60+','years','原料炭の炭鉱寿命')]):
    x=R+i*170; b+=A(x,ky+14,n,None,'num','font-size:36px')+A(x,ky+56,u.upper(),None,'cap')+A(x,ky+66,t,160,'sm')
b+=svg(R,ky+100,W,30,f'<circle cx="4" cy="6" r="3.6" fill="{GOLD}"/><circle cx="124" cy="6" r="2.6" fill="#fff" stroke="{GOLD}" stroke-width="1"/>')
b+=A(R+12,ky+101,'原料炭・銅の資産',None,'sm')+A(R+132,ky+101,'その他の資産・プロジェクト（鉄鉱石・ニッケル・リチウム ほか）',None,'sm')
pages.append(spread(b,4,5,'動画02 Who we are。第1章は1ページに軽く。ミッション・両輪・変革の3点だけ。写真枠は本社・社員（動画と素材共通化）。','動画03 Our Strengths。【強調】資産の大きさ。地図を大きく、原料炭・銅の拠点だけを光らせ、他は控えめに。数字3つで規模感。'))

# =================== P06 Coal / P07 Copper（強調：全面写真＋巨大数字） ===================
def hero(x0,img,pos,lab,en,jt,js,big,bigu,bigt,subs,extra=''):
    o=f'<img class="a ph" src="{uri(img,1800)}" style="left:{x0}px;top:0;width:595px;height:842px;object-position:{pos}">'
    o+=A(x0,0,'',595,'','height:842px;background:linear-gradient(180deg,rgba(12,18,26,.55) 0%,rgba(12,18,26,.05) 32%,rgba(12,18,26,.15) 52%,rgba(12,18,26,.82) 100%)')
    x=x0+48
    o+=A(x,52,lab,None,'lab','color:#e9d6ac')
    o+=A(x,82,en,500,'en wt','font-size:30px')
    o+=A(x,160,'',26,'',f'border-top:1px solid {RED}')+A(x,170,jt,None,'jt wt')+A(x,187,js,None,'js','color:#e3e7eb')
    o+=A(x,470,big+f'<span style="font-size:48px;letter-spacing:0">{bigu}</span>',None,'hero','font-size:150px')
    o+=A(x,612,bigt,420,'','font-family:Noto Sans JP;font-size:11px;color:#fff;font-weight:400;letter-spacing:.6px')
    for i,(n,t) in enumerate(subs):
        xx=x+i*170; o+=A(xx,660,'',150,'','border-top:.6px solid rgba(233,214,172,.8)')+A(xx,670,n,None,'num','font-size:30px;color:#fff')+A(xx,708,t,150,'sm','color:#dfe4e9')
    return o+extra
b=hero(0,'r-047.png','62% 40%','02　OUR STRENGTHS｜METALLURGICAL COAL','World-class<br>metallurgical coal.','原料炭事業','鉄の主原料“産業のコメ”を、世界最高品位で届ける',
       '~50','%','一級強粘炭の世界供給に占める BMA のシェア',[('~20%','原料炭の海上輸出市場シェア'),('60+ yrs','炭鉱寿命。港湾・鉄道まで自社保有')],
       A(L+340,668,'<div class="sm" style="color:#e9d6ac">OWNERSHIP</div><div style="font-size:7.4px;color:#fff;line-height:1.6">三菱商事 →100%→ MDP<br>MDP 50% ＋ BHP 50%<br>＝ BMA（BHP Mitsubishi Alliance）</div>',160,'','border-left:.6px solid rgba(233,214,172,.8);padding-left:10px'))
b+=hero(595,'r-054.png','45% 60%','02　OUR STRENGTHS｜COPPER','The world\'s largest<br>non-operating copper producer.','銅事業','パートナーが多く、規模が大きく、“声がかかる存在”である',
       'No.1','','ノンオペレーターとして世界最大の銅生産者',[('5 / 5','参画する主要5鉱山すべてが世界Top15'),('Top 25%','平均コストは世界の上位25%')],
       A(R+340,668,'<div class="sm" style="color:#e9d6ac">PARTNERSHIPS</div><div style="font-size:7.4px;color:#fff;line-height:1.6">特定1社に偏らず、<br>主要メジャーと協業<br>チリ・ペルー・米国</div>',160,'','border-left:.6px solid rgba(233,214,172,.8);padding-left:10px'))
b+=svg(0,0,1190,842,flow('M-10,440 C300,410 800,410 1200,380','#e9d6ac',.7,.8,[(595,418)]))
pages.append(spread(b,6,7,'動画04 Coking Coal。【強調】全面写真＋巨大数字（~50%）。“資産の大きさ”を1つの数字で伝える。出資構成は1行に。','動画05 Copper。【強調】原料炭と同じ型で対に。No.1を最大に。金の軌道が2枚の写真をつなぐ。'))

# =================== P08 From resources to value（軽め） / P09 Global partnerships ===================
o,yy=H2(L,52,'02　FROM RESOURCES TO VALUE','第2章　独自価値','From resources<br>to value.','資源は、届けてはじめて価値になる','確保し、精錬し、必要とする産業へ届ける。鉄鉱石から電池資源・アルミまで',body=40,bw=360)
b=o
rowy=yy+150
b+=svg(0,rowy-2,595,6,f'<line x1="0" y1="3" x2="595" y2="3" stroke="{GOLDL}" stroke-width=".8"/>')
res=[('x_ironore.jpg','Iron Ore','鉄鉱石'),('x_case_mine.jpg','Nickel','ニッケル'),('x_lithium.jpg','Lithium','リチウム'),('x_alu.jpg','Aluminium','アルミ・ボーキサイト'),(None,'Fertilizer','肥料資源'),('r-074.png','Recycled','二次資源')]
for i,(f,e,j) in enumerate(res):
    c=L+38+i*85
    b+=(CIRC(c,rowy,66,f) if f else lens(c,rowy,66,None,''))+A(c-40,rowy+40,e,80,'','text-align:center;font-size:7.2px;font-weight:400')+A(c-40,rowy+51,j,80,'sm','text-align:center')
ty=rowy+120
b+=SEC(L,ty,'NEW TECHNOLOGY','加工技術・回収・リサイクルなど、業界のボトルネックに挑む技術へ投資')
for i,(n,t,h) in enumerate([('CiDRA','COPPER｜STARTUP','浮遊選鉱の高度化'),('Jetti','COPPER｜STARTUP','硫化鉱のリーチング化'),('DESCycle','RECYCLING','銅スクラップの回収強化')]):
    x=L+i*168
    b+=A(x,ty+26,f'<div style="font-size:5.4px;letter-spacing:1.2px;color:{GOLD}">{t}</div><div style="font-size:9.5px;font-weight:400">{n}</div><div class="smb" style="font-size:6.8px">{h}</div>',156,'',f'height:50px;padding:7px 14px;border:.6px solid {HAIR};border-radius:25px;background:#fff')
b+=svg(0,0,595,842,flow(f'M-10,{ty+120} C200,{ty+100} 420,{ty+130} 600,{ty+90}',GOLDL,.7,.9))
# P09
o,yy=H2(R,52,'02　GLOBAL PARTNERSHIPS','第2章　独自価値','Global partnerships.','メジャーとのパートナーシップと、世界の販売網','優良な鉱山、パートナーのメジャー企業、そして営業拠点。資源を流通させるネットワーク')
b+=o
MW=520; MH=MW*996/2600; mx,my=R-10,yy+12
b+=IMG(mx,my,MW,MH,'v8/flat_std.png',fmt='PNG',light=.45,mx=1600)
P=lambda lon,lat:(mx+(lon+170)/360*MW,my+(80-lat)/138*MH)
mines=[(148.3,-22.3),(-69.07,-24.27),(-77.05,-9.53),(-110.9,31.9),(-66.9,52.9)]
hubs=[(103.8,1.3),(139.7,35.7),(77.2,28.6),(-0.1,51.5),(-77.0,40.4)]
o=''
for (a,c) in zip(mines,hubs):
    for h in hubs[:3]:
        x1,y1=P(*a); x2,y2=P(*h); mxp=(x1+x2)/2; myp=min(y1,y2)-abs(x2-x1)*.15-8
        o+=f'<path d="M{x1:.1f},{y1:.1f} Q{mxp:.1f},{myp:.1f} {x2:.1f},{y2:.1f}" fill="none" stroke="{GOLD}" stroke-width=".45" opacity=".55"/>'
for lo,la in mines: x,y=P(lo,la); o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.2" fill="{GOLD}" stroke="#fff" stroke-width=".8"/>'
for lo,la in hubs: x,y=P(lo,la); o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.2" fill="{BLUE}" stroke="#fff" stroke-width=".8"/>'
b+=svg(0,0,1190,842,o)
ny=my+MH+16
for i,(n,e,j) in enumerate([('15','industries','業界'),('50','countries','カ国'),('~1,000','customers','社の販売先')]):
    x=R+i*165; b+=A(x,ny,n,None,'num','font-size:30px')+A(x,ny+34,e.upper(),None,'cap')+A(x,ny+44,j,None,'sm')
jy=ny+70
b+=A(R,jy,'',W,'',f'border-top:.6px solid {HAIR}')
b+=SEC(R,jy+10,'JOINT VENTURES','業界最大手とのJV実績',120)
for i,n in enumerate(['BHP','Rio Tinto','Anglo American']): b+=A(R+i*130,jy+30,n,None,'','font-size:13px;font-weight:300')
b+=SEC(R,jy+60,'TRADING HUB','RtM International・Japan・Bharat・Europe・Americas ほか',100)
b+=SEC(R,jy+84,'WHY PARTNERS CHOOSE US','企業文化的親和性・JV経営力・健全な財務基盤・深い知見',175)
pages.append(spread(b,8,9,'動画06 From Resources to Value。【軽め】その他資源は丸写真の帯、新技術は3つのチップだけ。主役の前の“間”として余白を多く。','動画07 Global Partnerships。地図上で鉱山（金）と販売拠点（青）を線でつなぎ、エビデンス数値（15×50×1,000）とJV実績を添える。'))

# =================== P10-11 Integrated value chain（強調：見開き全体） ===================
b=A(L,52,'03　INTEGRATED VALUE CHAIN',None,'lab')+A(L,63,'第3章　川上から川下までをつなぐ',None,'labj')
b+=A(L,86,'Integrated value chain.',900,'en','font-size:40px')
b+=A(L,142,'',26,'',f'border-top:1px solid {RED}')+A(L,152,'採掘・製造・販売をつなぐトレーディング力こそが、総合商社 三菱商事の強み',None,'jt')
b+=A(L,170,'このネットワークを活かし、川上の鉱山から、製錬・製鉄、さらに製造業などの川下まで、資源を安定的に流通させる',None,'js')
b+=BIG(850,40,'03')
cy=410; xs=[150,370,595,820,1040]
ring=(f'<ellipse cx="595" cy="{cy-10}" rx="470" ry="118" fill="none" stroke="{GOLD}" stroke-width="1.8"/>'
      f'<ellipse cx="595" cy="{cy+6}" rx="455" ry="104" fill="none" stroke="{BLUE}" stroke-width="1.8"/>')
b+=svg(0,0,1190,842,ring)
st=[('x_vc_mine.jpg','Mine','鉱山・資源開発','UPSTREAM　川上'),('_mr_project_06.png','Trading','トレーディング（RtM）',''),('x_vc_smelter.jpg','Smelt / Steel','製錬・製鉄','MIDSTREAM　川中'),('r-072.png','Trading','トレーディング（RtM）',''),('x_vc_ev.jpg','End use','最終製品・需要家','DOWNSTREAM　川下')]
for k,(f,e,j,s_) in enumerate(st):
    x=xs[k]; y=cy+104*math.sqrt(max(0,1-((x-595)/455)**2))
    d=112 if k%2==0 else 92
    b+=CIRC(x,y,d,f)+A(x-60,y+d/2+8,e,120,'','text-align:center;font-size:10px;font-weight:400')+A(x-60,y+d/2+22,j,120,'smb','text-align:center;font-size:7.6px'+(f';color:{BLUE}' if k%2 else ''))
    if s_: b+=A(x-60,cy-150,s_,120,'sec','text-align:center;font-size:7px')
b+=A(595-120,cy-40,f'<span style="color:{GOLD};font-weight:500;font-size:9px;letter-spacing:1.8px">INVESTMENT</span>　<span class="em" style="color:{GOLD}">資源投資</span>',240,'','text-align:center')
b+=A(595-120,cy-22,f'<span style="color:{BLUE};font-weight:500;font-size:9px;letter-spacing:1.8px">TRADING (RtM)</span>　<span class="em" style="color:{BLUE}">トレーディング</span>',240,'','text-align:center')
b+=A(1040-60,cy+150,'Base Demand<br>Energy Transition<br>AI &amp; Data Centers',120,'','text-align:center;font-size:7.4px;font-weight:300;line-height:1.6;color:'+SUB)
# functions band
fy=640
b+=A(L,fy-14,'',1094,'',f'border-top:.6px solid {HAIR}')
b+=SEC(L,fy,'RtM FUNCTIONS','お客様に提供できる5つの機能',112)
for i,(e,j) in enumerate([('Marketing &amp; Procurement','販売・調達'),('Logistics','物流'),('Financing','ファイナンス'),('Risk Management','リスク管理'),('Carbon Reduction','脱炭素')]):
    x=L+i*104
    b+=A(x,fy+22,f'<div style="font-size:6.8px;font-weight:400">{e}</div><div class="sm" style="font-size:5.8px">{j}</div>',96,'',f'height:36px;border:.7px solid {GOLD};border-radius:18px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center')
# closing
FB=uri('v9/globe_new.png',900,'PNG')
_s=165/875
b+=f'<img class="a" src="{FB}" style="left:{1142-755*_s:.1f}px;top:{745-515*_s:.1f}px;width:{1536*_s:.1f}px;height:{1024*_s:.1f}px">'
b+=A(R+10,fy,'OUR COMMITMENT',None,'sec')
b+=A(R+10,fy+18,'“To contribute to a better society by providing a stable supply of high-quality mineral resources that society needs, in a sustainable way.”',370,'en','font-size:12.5px;line-height:1.45')
b+=A(R+10,fy+76,'豊かな社会の実現に貢献することを目指して',None,'smb')
b+=A(R+10,fy+100,'Mitsubishi Corporation　Mineral Resources Group｜2-3-1 Marunouchi, Chiyoda-ku, Tokyo｜www.mitsubishicorp.com',380,'sm','font-size:5.8px')
orb=flow('M-10,228 C200,214 400,210 595,218 S1000,232 1200,212',GOLDL,.6,.8)
pages.append(spread(b,10,11,'動画08 Integrated Value Chain。【強調】見開き全体を1枚の図に。投資（金）とトレーディング（青）の2つの輪の上に、川上→川中→川下の5段階を大きく並べる。','動画09 Closing と呼応。約束のステートメントと連絡先、冒頭の地球儀（日本側）で冊子を閉じる。',orb))

links=''.join(f'<link rel="stylesheet" href="f/nsjp/package/{w}.css">' for w in (300,400,500))
open('daiwari_v10.html','w').write('<!doctype html><meta charset=utf-8>'+links+'<style>'+CSS+'</style>'+''.join(pages))
