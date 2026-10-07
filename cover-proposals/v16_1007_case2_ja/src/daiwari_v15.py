# 台割 v9（篠原修正案）— 10/6 手書き修正を反映
exec(open('v9_head.py').read())
CSS+=f""".sec{{font-size:8.2px;letter-spacing:2.6px;color:{GOLD};font-weight:400}}
.secj{{font-family:'Noto Sans JP';font-size:8.2px;letter-spacing:.4px;color:{SUB};font-weight:300}}
.big{{font-weight:200;font-size:250px;line-height:1;color:transparent;-webkit-text-stroke:.6px #e6e9ec;letter-spacing:-8px}}
.em{{font-family:'Noto Sans JP';font-weight:500;font-size:9.4px}}
"""
SPH=['v9/sph1.png','v9/sph2.png','v9/sph3.png']
def sph(cx,cy,d,i=0): return f'<img class="a" src="{uri(SPH[i],700,"PNG")}" style="left:{cx-d/2}px;top:{cy-d/2}px;width:{d}px;height:{d}px">'
def BIG(x,y,t): return A(x,y,t,None,'big')
def SEC(x,y,en,jp,gap=None):
    if jp==en or en.startswith(jp) or jp.startswith(en): jp=''
    return A(x,y,en,None,'sec')+A(x+(gap if gap else len(en)*12+14),y,jp,None,'secj')
def H2(x,y,lab,labj,en,jt,js,size=30,body=0,bw=330):
    o,yy=HEAD(x,y,lab,labj,en,jt,js,size=size)
    if body: o+=BODY(x,yy+4,bw,body); yy+=4+(-(-body*5.6//bw)+1)*12.7
    return o,yy
def flow(d,col=GOLD,sw=.75,op=.85,dots=()):
    o=f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}" opacity="{op}"/>'
    for x,y in dots: o+=f'<circle cx="{x}" cy="{y}" r="2.1" fill="{GOLD}"/>'
    return o
_JB=iter(['資源は、そこに「ある」だけでは、まだ価値ではありません。誰かが見出し、育て、必要とする場所へ届けて、はじめて力になる。私たちは、世界有数の資産に関わり、投資とトレーディングの両輪で川上から川下までをつなぎます。フェアな立場だからこそ、埋められる隙間がある。多様なパートナーと使い手の間に立ち、その時々の最適解を導く。世界に眠る価値を、社会の力へ。', '三菱商事は、三綱領に基づき、経済価値・環境価値・社会価値の同時実現を目指す総合商社です。そのなかで金属資源グループは、社会に不可欠な金属資源を世界から確保し、安定的に届ける役割を担っています。資源投資を担う2本部と、トレーディングを担う1本部の両輪で、川上の鉱山から川下の需要家までをつないでいます。', '原料炭と銅を中核に、鉄鉱石、電池資源、アルミ、肥料、二次資源へと事業領域を広げています。資産を保有する地域だけでなく、世界各地にトレーディング拠点と金属資源の担当者を置き、新しい事業機会を探っています。鉄鉱石を先頭に、世界に広がる事業と人の拠点を一覧で示します。', 'BHPと50:50の合弁であるBMAを通じ、豪州クイーンズランド州ボーエン・ベースンで世界最高品位の原料炭事業に参画しています。炭鉱に加えて港湾と鉄道も保有し、山から港まで全体最適で運営しています。', '特定の1社に偏らず、主要メジャーのほぼすべてと共同事業・取引を行っています。販売を通じた幅広い関係と長年の実績が、新しい案件での信頼につながっています。', '出資案件から得られるオフテイクをRtMが引き受け、ヘッジ・在庫・物流などの機能を付加して世界の顧客に届けます。顧客との接点から得た市場の生きた情報は、資源投資の判断へと還元されます。', '新技術の把握は、既存事業の高度化と将来価値の創出に還元されます。鉱石品位の低下、回収率、リサイクルといった業界のボトルネックに挑むスタートアップへの投資を通じ、川上から川下までに網を張っています。', '資源業界では、良い案件があっても単独では規模が大きすぎることが少なくありません。そのとき「三菱に声をかけよう」と思われる存在であること。業界最大手とJVを組み、人材派遣・ガバナンス参画・総合力で事業価値の最大化に貢献してきました。'])
def BODY(x,y,w,n,s=''): return A(x,y,next(_JB),w,'bd','font-family:"Noto Sans JP";text-align:justify;'+s)
pages=[]

# =================== P02-03 ===================
FG=uri('v9/globe_new.png',1800,'PNG')
_s=640/875
b=f'<img class="a" src="{FG}" style="left:{190-755*_s:.1f}px;top:{500-515*_s:.1f}px;width:{1536*_s:.1f}px;height:{1024*_s:.1f}px">'
b+=A(L,58,'三菱商事　金属資源グループ',None,'lab')
b+=A(R,150,'Strength to Hold.<br>Power to Connect.',470,'en','font-size:40px;line-height:1.1')
b+=A(R,256,'',26,'',f'border-top:1px solid {RED}')+A(R,270,'コアメッセージ（英文主体・和文は確認用）',None,'labj')
b+=BODY(R,290,300,80,'font-size:8.2px;line-height:1.8;color:#6c7279')
toc=[('01','我々は何者か','我々は何者か｜三菱商事 金属資源グループ','04'),('02','独自価値','独自価値｜フットプリント・原料炭・銅・トレーディング・新技術','05'),('03','選ばれ続ける理由','Partner of Choice','10'),('04','何を実現するか','何を実現するか｜外部環境と私たちの約束','11')]
b+=A(R,592,'目次',None,'sec')
for i,(n,e,j,p) in enumerate(toc):
    y=614+i*44
    b+=A(R,y,'',W-40,'',f'border-top:.5px solid {HAIR}')+A(R,y+9,n,None,'num','font-size:18px;color:'+GOLD)
    b+=A(R+44,y+8,e,None,'','font-size:11px;font-weight:300')+A(R+44,y+24,j,None,'sm')+A(R+W-60,y+10,'P.'+p,None,'fo')
fr=flow('M624,544 C800,512 1000,504 1210,498',GOLDL,.7,1,[(1000,504)])
b+=svg(0,0,1190,842,fr)
pages.append(spread(b,2,3,'導入。表紙の地球儀を大きく扉に。軌道の輪がノドを越えて右ページへ伸び、コアメッセージと目次の間を通る。','コアメッセージと目次のみ。軌道線は文字に重ならない高さで横断させ、右端から次の見開きへ抜ける。'))

# =================== P04 / P05 ===================
orb=flow('M-10,318 C250,322 450,305 620,262 S950,254 1190,254',GOLD,.75,.8,[(300,318),(980,254)])
b=BIG(400,30,'01')+BIG(985,30,'02')
o,yy=H2(L,52,'01｜我々は何者か','第1章　我々は何者か','From resource<br>to market.','三菱商事 金属資源グループとは','投資とトレーディングの両輪で、川上から川下までをつなぐ',body=60,bw=330)
b+=o
# value chain = two rings
cx,vy=L+250,470; rx,ry=218,75
rings=(f'<ellipse cx="{cx}" cy="{vy-6}" rx="{rx+8}" ry="{ry+10}" fill="none" stroke="{GOLD}" stroke-width="1.6"/>'
       f'<ellipse cx="{cx}" cy="{vy+4}" rx="{rx-4}" ry="{ry}" fill="none" stroke="{BLUE}" stroke-width="1.6"/>')
b+=svg(0,0,595,842,rings)
b+=A(cx-90,vy-26,'バリューチェーン',180,'en','font-size:22px;text-align:center;color:#7d8794')+A(cx-90,vy+2,'バリューチェーン',180,'secj','text-align:center')
st=[('x_vc_mine.jpg','採掘','資源開発・保有'),('_mr_project_06.png','流通','トレーディング'),('x_vc_smelter.jpg','加工','製錬・製鉄'),('r-072.png','流通','トレーディング'),('x_vc_ev.jpg','需要家','最終製品・需要家')]
for k,(f,e,j) in enumerate(st):
    x=cx-rx+k*rx/2
    y=vy+ry*math.sqrt(max(0,1-((x-cx)/rx)**2))
    b+=CIRC(x,y,78,f)+A(x-45,y+45,e,90,'','text-align:center;font-size:7.6px;font-weight:400')+A(x-45,y+57,j,90,'sm','text-align:center')
b+=A(L+30,vy-118,f'<span style="color:{GOLD};font-weight:500;font-size:8.2px;letter-spacing:1.6px">投資</span>　<span class="em" style="color:{GOLD}">資源投資</span><span class="sm">｜鉄鋼原料本部・クリティカルミネラル本部</span>',440)
b+=A(L+30,vy+152,f'<span style="color:{BLUE};font-weight:500;font-size:8.2px;letter-spacing:1.6px">トレーディング（RtM）</span>　<span class="em" style="color:{BLUE}">トレーディング</span><span class="sm">｜金属資源トレーディング本部</span>',440)
jy=664
b+=SEC(L,jy,'歩み','時代を先読みし、事業モデルを変革してきた歩み')
b+=svg(L,jy+42,W,20,f'<line x1="0" y1="10" x2="{W}" y2="10" stroke="{GOLDL}" stroke-width=".8"/>'+''.join(f'<circle cx="{4+i*101}" cy="10" r="3" fill="{GOLD}"/>' for i in range(5)))
era=[('〜1990s','トレーディングに参入し、少数株主として出資'),('1990s','口銭モデルから投資モデルへ。JV運営の知見を蓄積'),('2000s','中国の成長を捉え、事業経営に関与（BHPと50:50）'),('2010s','原料炭偏重から脱却。資産価値の最大化へ'),('2020s〜','地域特化から、グローバルなトレーダーへ')]
for i,(y_,t) in enumerate(era):
    x=L+i*101; b+=A(x,jy+20,y_,None,'num','font-size:15px')+A(x,jy+62,t,92,'sm')
b+=A(L,jy+102,'三菱商事の三綱領（所期奉公・処事光明・立業貿易）を企業理念とする',W,'bd','font-size:6.4px;color:'+MUTE)
# P05
o,yy=H2(R,52,'02｜独自価値','第2章　独自価値','Where we work.','グローバル・フットプリント','多様な資源と地域で、事業と人の拠点を広げる',body=60,bw=380)
b+=o
MW=W+40; MH=MW*996/2600; my=272
b+=IMG(R-10,my,MW,MH,'v8/flat_std.png',fmt='PNG',light=.35,mx=1800)
P=lambda lon,lat:(R-10+(lon+170)/360*MW,my+(80-lat)/138*MH)
PRJ=[(-66.9,52.9),(-71.2,-28.5),(-70.6,-33.4),(148.3,-22.3),(-69.07,-24.27),(-70.5,-31.7),(-70.3,-33.15),(-77.05,-9.53),(-70.6,-17.1)]
DEV=[(-70.3,-22.9),(-110.9,31.9),(-128.9,58.5),(121.4,-30.7),(-94.0,51.6),(141.7,-13.3),(25.7,64.2),(-0.6,54.4)]
OFF=[(139.7,35.7),(103.8,1.3),(77.2,28.6),(-0.1,51.5),(-77.0,40.4),(55.3,25.2),(106.8,-6.2),(100.5,13.7),(-70.65,-33.45),(28.0,-26.2),(-58.4,-34.6),(-46.6,-23.5),(153.0,-27.5),(-77.0,-12.0),(-123.1,49.3),(121.5,31.2)]
o=''
for lo,la in OFF: x,y=P(lo,la); o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{BLUE}" stroke="#fff" stroke-width=".8"/>'
for lo,la in DEV: x,y=P(lo,la); o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.3" fill="#fff" stroke="{GOLD}" stroke-width="1.3"/>'
for lo,la in PRJ: x,y=P(lo,la); o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.3" fill="{GOLD}" stroke="#fff" stroke-width=".8"/>'
b+=svg(0,0,1190,842,o)
ly=my+MH+6
b+=svg(R,ly,W,12,f'<circle cx="4" cy="5" r="3.3" fill="{GOLD}"/><circle cx="104" cy="5" r="3.3" fill="#fff" stroke="{GOLD}" stroke-width="1.3"/><circle cx="234" cy="5" r="3" fill="{BLUE}"/>')
b+=A(R+11,ly,'事業・資産',None,'sm')+A(R+111,ly,'開発・探鉱プロジェクト',None,'sm')+A(R+241,ly,'トレーディング拠点・金属資源の駐在',None,'sm')
cy_=ly+30
b+=SEC(R,cy_,'取扱資源','鉄鉱石から電池資源・肥料・アルミまで、世界に広がる事業領域')
com=[('r-048.png','原料炭','',1),('r-054.png','銅','',1),('x_ironore.jpg','鉄鉱石','',0),('x_case_mine.jpg','ニッケル','',0),('x_lithium.jpg','リチウム','',0),('x_alu.jpg','アルミ・ボーキサイト','',0),('r-074.png','二次資源','',0),(None,'肥料資源','',0)]
rowy=cy_+50
b+=svg(R-10,rowy-2,W+20,6,f'<line x1="0" y1="3" x2="{W+20}" y2="3" stroke="{GOLDL}" stroke-width=".8"/>')
x=R+4
for f,e,j,big in com:
    d=60 if big else 42; c=x+d/2
    if f: b+=CIRC(c,rowy,d,f,ring=bool(big))
    else: b+=f'<div class="a" style="left:{c-d/2}px;top:{rowy-d/2}px;width:{d}px;height:{d}px;border-radius:50%;background:#fff;border:.8px solid {GOLD}"></div>'
    b+=A(c-34,rowy+d/2+6,e,68,'','text-align:center;font-size:6.6px;font-weight:'+('500' if big else '300'))+A(c-34,rowy+d/2+17,j,68,'sm','text-align:center;font-size:5.8px')
    x+=d+(16 if big else 17)
hy=rowy+84
b+=SEC(R,hy,'販売網','世界の資源と需要をつなぐ販売網')
hub=[('RtMI','RtM International'),('RtMJ','RtM Japan'),('RtMB','RtM Bharat'),('RtME','RtM Europe'),('RtMA','RtM Americas')]
sub=['中国','UAE','インドネシア','タイ','チリ']
hr=hy+52
b+=svg(R-10,hr-2,W+20,6,f'<line x1="0" y1="3" x2="{W+20}" y2="3" stroke="{GOLDL}" stroke-width=".8"/>')
for i,(a,n) in enumerate(hub):
    c=R+26+i*68
    b+=f'<div class="a" style="left:{c-25}px;top:{hr-25}px;width:50px;height:50px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#fff,{GLASS} 70%);border:.8px solid {GOLD};display:flex;align-items:center;justify-content:center;font-size:8px;color:{DEEP};font-weight:400">{a}</div>'
    b+=A(c-34,hr+30,n,68,'','text-align:center;font-size:6px;font-weight:300')
for i,n in enumerate(sub):
    c=R+364+i*34
    b+=f'<div class="a" style="left:{c-14}px;top:{hr-14}px;width:28px;height:28px;border-radius:50%;background:#fff;border:.8px solid {GOLD}"></div>'+A(c-20,hr+19,n,40,'sm','text-align:center;font-size:5.8px')
pages.append(spread(b,4,5,'第1章を1ページに。「投資×トレーディング」を2つの輪（金＝投資、青＝トレーディング）として描き、両輪が事業の軸であることを強調。','第2章の扉＝全体像。地図＋取扱資源（肥料資源を追加）＋販売網（RtM 5社と主要拠点）。拠点・駐在（青）は名称なし。',orb))

# =================== P06 / P07 ===================
WAVE=lambda x:280+62*math.sin(math.pi*x/1190)
def wave_clip(x0):
    pts=' L'.join(f'{x-x0:.1f},{WAVE(x):.1f}' for x in range(x0+595,x0-1,-17))
    return f"clip-path:path('M0,0 L595,0 L{pts} Z')"
b=f'<img class="a ph" src="{uri("r-047.png",1600)}" style="left:0;top:0;width:595px;height:350px;object-position:50% 40%;{wave_clip(0)}">'
b+=f'<img class="a ph" src="{uri("r-054.png",1600)}" style="left:595px;top:0;width:595px;height:350px;object-position:50% 60%;{wave_clip(595)}">'
wv=lambda off:'M'+' L'.join(f'{x},{WAVE(x)+off:.1f}' for x in range(0,1191,17))
b+=svg(0,0,1190,842,flow(wv(10),GOLD,.7,.85,[(595,WAVE(595)+10)])+flow(wv(20),GOLDL,.6,.9))
b+=A(L,40,'02｜独自価値　原料炭',None,'lab','color:#fff;text-shadow:0 0 6px rgba(0,0,0,.35)')+A(R,40,'02｜独自価値　銅',None,'lab','color:#fff;text-shadow:0 0 6px rgba(0,0,0,.35)')
hh=360
for x,en,jt,js in [(L,'World-class<br>metallurgical coal.','原料炭事業','鉄の主原料“産業のコメ”を、世界最高品位で届ける'),(R,'The partner the copper<br>industry calls first.','銅事業','自社操業を伴わずに、世界最大級の銅ポジションを築く')]:
    b+=A(x,hh,en,W+10,'en','font-size:28px')+A(x,hh+72,'',26,'',f'border-top:1px solid {RED}')+A(x,hh+82,jt,None,'jt')+A(x,hh+99,js,None,'js')
def kpis(x0,kp):
    o=''
    for i,(n,t) in enumerate(kp):
        x=x0+i*168; o+=A(x,hh+130,'',150,'',f'border-top:.6px solid {GOLD}')+A(x,hh+142,n,None,'num','font-size:34px')+A(x,hh+184,t,150,'sm')
    return o
b+=kpis(L,[('~50<span style="font-size:16px">%</span>','一級強粘炭の供給に占める<br>BMAのシェア'),('~20<span style="font-size:16px">%</span>','原料炭の海上輸出市場<br>シェア'),('60<span style="font-size:16px">+ yrs</span>','炭鉱寿命。<br>港湾・鉄道まで自社保有')])
b+=kpis(R,[('No.1','ノンオペレーターとして<br>世界最大の銅生産者'),('5 / 5','参画する主要5鉱山すべてが<br>世界Top15'),('Top 25<span style="font-size:16px">%</span>','平均コストは世界の<br>上位25%に位置')])
ty=hh+222
b+=BODY(L,ty,260,48)
# BMA structure
by=ty+86
b+=SEC(L,by,'出資構成','出資構成｜BMAはMDPとBHPの50:50合弁会社')
def pill(x,y,w,t,sub_='',fill='#fff',col=INK):
    return A(x,y,f'<div style="font-size:7.6px;font-weight:400;color:{col}">{t}</div>'+(f'<div class="sm" style="font-size:5.6px">{sub_}</div>' if sub_ else ''),w,'',f'height:30px;border:.8px solid {GOLD};border-radius:15px;background:{fill};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center')
y0=by+24
b+=pill(L,y0,70,'三菱商事','三菱商事')+pill(L+104,y0,70,'MDP','三菱商事 100%出資')+pill(L+104,y0+40,70,'BHP')
b+=pill(L+208,y0+20,90,'BMA','BHP Mitsubishi Alliance','#f6f1e6')
ar=(f'<line x1="70" y1="15" x2="102" y2="15" stroke="{GOLD}" stroke-width=".8"/><path d="M98,12 L103,15 L98,18" fill="none" stroke="{GOLD}" stroke-width=".8"/>'
    f'<path d="M174,15 H190 V35 H206 M174,55 H190 V35" fill="none" stroke="{GOLD}" stroke-width=".8"/><path d="M202,32 L207,35 L202,38" fill="none" stroke="{GOLD}" stroke-width=".8"/>')
b+=svg(L,y0,320,80,ar)+A(L+74,y0+2,'100%',None,'sm','font-size:5.8px')+A(L+176,y0+3,'50%',None,'sm','font-size:5.8px')+A(L+176,y0+43,'50%',None,'sm','font-size:5.8px')
# Australia crystal map
mx,my2,mw=L+300,ty-6,200; mh=mw*252/310
b+=IMG(mx,my2,mw,mh,'v9/au.png',fmt='PNG',mx=800)
bx=mx+(148.3-112)/43*mw; byy=my2+(-9+22.3)/35*mh
b+=svg(0,0,1190,842,f'<ellipse cx="{bx:.1f}" cy="{byy:.1f}" rx="22" ry="9" transform="rotate(-18 {bx:.1f} {byy:.1f})" fill="none" stroke="{GOLD}" stroke-width=".8"/><circle cx="{bx:.1f}" cy="{byy:.1f}" r="3.4" fill="{GOLD}" stroke="#fff" stroke-width=".8"/>')
b+=A(bx-78,byy-16,'Bowen Basin',None,'','font-size:6.6px;font-weight:500')+A(bx-78,byy-6,'豪州クイーンズランド州',None,'cap')
b+=A(mx,my2+mh+6,'1968年 MDP設立／2001年 BMA組成',mw,'sm')
# copper lower
mx,my2,mw=R,ty-6,140; mh=mw*252/216
b+=IMG(mx,my2,mw,mh,'v9/andes.png',fmt='PNG',mx=800)
PJ=lambda lo,la:(mx+(lo+84)/30*mw,my2+(-2-la)/35*mh)
mines=[('Antamina',-77.05,-9.53),('Quellaveco',-70.6,-17.1),('Escondida',-69.07,-24.27),('Marimaca',-70.3,-22.9),('Los Pelambres',-70.5,-31.7),('Anglo American Sur',-70.3,-33.15)]
o=''.join(f'<circle cx="{PJ(lo,la)[0]:.1f}" cy="{PJ(lo,la)[1]:.1f}" r="2.8" fill="{GOLD}" stroke="#fff" stroke-width=".7"/>' for n,lo,la in mines)
b+=svg(0,0,1190,842,o)
for n,lo,la in mines:
    x,y=PJ(lo,la); b+=A(x+5,y-4,n,None,'','font-size:5.4px;color:'+INK+';white-space:nowrap;background:rgba(255,255,255,.7);padding:0 2px')
b+=A(mx,my2+mh+4,'チリ・ペルーを中心に参画（ほか米国 Copper World）',220,'sm')
cx0=R+170
b+=A(cx0,ty,'パートナー企業が多く、規模が大きく、業界と幅広い関係を築いている。だから、新たな案件で“声がかかる存在”である。',W-170,'smb','font-size:8.2px;line-height:1.6')
b+=BODY(cx0,ty+32,W-170,40)
four=[('','規模で世界上位の優良鉱山に参画'),('','特定1社に偏らず、主要メジャーと協業'),('','販売を通じ、業界の幅広い関係を構築'),('','業界のボトルネックに挑む技術へ投資')]
for i,(e,j) in enumerate(four):
    x=cx0+(i%2)*165; y=ty+104+(i//2)*40
    b+=A(x,y,f'0{i+1}',None,'num','font-size:13px;color:'+GOLD)+A(x+20,y,e,140,'','font-size:7.4px;font-weight:400')+A(x+20,y+11,j,140,'sm','font-size:6px')
pages.append(spread(b,6,7,'主力① 原料炭。写真2枚を波形に切り抜き、金の軌道でつなぐ。BMA＝MDPとBHPの50:50合弁と分かる出資構成図を追加。','主力② 銅。本文（パートナーが多く、規模が大きく、幅広い関係＝声がかかる存在）を主に、強み4点は下段に移動。'))

# =================== P08 / P09 ===================
orb=flow('M-10,338 C300,326 700,318 1190,352',GOLD,.75,.8,[(420,325),(1020,336)])
b=''
o,yy=H2(L,52,'02｜独自価値　トレーディング','第2章　独自価値','Resource to Market.','トレーディング事業（RtM）','一つの商品の中で、投資から販売までを一気通貫でつなぐ')
b+=o
nb=[('15','','業界'),('50','','カ国'),('~1,000','','社の販売先')]
for i,(n,e,j) in enumerate(nb):
    x=L+i*160; b+=A(x,yy+8,n,None,'num','font-size:38px')+A(x,yy+50,e.upper(),None,'cap')+A(x,yy+60,j,None,'sm')
    if i<2: b+=A(x+118,yy+18,'×',None,'','font-size:18px;font-weight:200;color:'+GOLD)
b+=BODY(L,yy+82,W,40)
cx,cy=L+140,450
b+=svg(0,0,595,842,f'<ellipse cx="{cx}" cy="{cy}" rx="122" ry="52" transform="rotate(-8 {cx} {cy})" fill="none" stroke="{GOLDL}" stroke-width=".8"/>')
b+=sph(cx,cy,104,0)+A(cx-40,cy-12,'RtM',80,'','text-align:center;font-size:17px;font-weight:300;color:'+DEEP)+A(cx-40,cy+9,'5つの機能',80,'cap','text-align:center;color:#7d93a9')
fn=[('販売・調達','販売・調達',200),('脱炭素','脱炭素',245),('リスク管理','リスク管理',300),('ファイナンス','ファイナンス',350),('物流','物流',90)]
for e,j,a in fn:
    t=math.radians(a); x=cx+122*math.cos(t); y=cy+52*math.sin(t); r=math.radians(-8)
    X=cx+(x-cx)*math.cos(r)-(y-cy)*math.sin(r); Y=cy+(x-cx)*math.sin(r)+(y-cy)*math.cos(r)
    b+=f'<div class="a" style="left:{X-25}px;top:{Y-25}px;width:50px;height:50px;border-radius:50%;background:rgba(255,255,255,.92);border:.8px solid {GOLD};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center"><div style="font-size:5.8px;font-weight:400;line-height:1.2">{e}</div><div class="sm" style="font-size:5.2px">{j}</div></div>'
b+=A(cx-80,cy+82,'お客様に提供できる5つの機能',160,'smb','text-align:center')
bx,by=L+320,370
b+=A(bx,by,'ビジネスモデル',None,'sec')
bm=[('','MC保有資産と第三者取引の両方を扱う'),('','資源確保による安定供給'),('','市場・業界動向の発信と知見共有で、事業機会を発掘'),('','トレーディング機能の強化で、付加価値を生み続ける')]
for i,(e,j) in enumerate(bm):
    y=by+20+i*44; b+=A(bx,y,'',180,'',f'border-top:.6px solid {HAIR}')+A(bx,y+7,e,180,'','font-size:8.2px;font-weight:300')+A(bx,y+20,j,180,'sm')
b+=svg(bx-14,by+20,10,176,f'<line x1="5" y1="0" x2="5" y2="172" stroke="{GOLD}" stroke-width=".8"/><path d="M1,166 L5,174 L9,166" fill="none" stroke="{GOLD}" stroke-width=".8"/>')
# copper value chain example
ey=618
b+=A(L,ey-10,'',W,'',f'border-top:.6px solid {HAIR}')
b+=SEC(L,ey,'トレーディング事業例','銅のバリューチェーン')
steps=[('鉱山会社','',0),('トレーディング','RtM',1),('製鉄・製錬','',0),('トレーディング','RtM',1)]
sx=L; syy=ey+34
for i,(j,e,rt) in enumerate(steps):
    w=78
    b+=A(sx,syy,f'<div style="font-family:Noto Sans JP;font-size:7.4px;font-weight:{500 if rt else 400};color:{BLUE if rt else INK}">{j}</div><div class="cap" style="font-size:5.6px;margin-top:2px">{e}</div>',w,'',f'height:38px;border-radius:19px;border:.8px solid {BLUE if rt else GOLD};background:{GLASS if rt else "#fff"};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center')
    b+=svg(sx+w,syy+19,16,2,f'<line x1="2" y1="1" x2="13" y2="1" stroke="{GOLD}" stroke-width=".8"/><path d="M10,-2 L14,1 L10,4" fill="none" stroke="{GOLD}" stroke-width=".8"/>')
    sx+=w+16
b+=A(sx,syy-6,'主な最終用途（例）',None,'sm','font-size:6.2px')
for i,t in enumerate(['基礎需要','エネルギー転換','AI・データセンター']):
    b+=A(sx,syy+8+i*13,'● '+t,None,'','font-size:7.6px;font-weight:300').replace('● ',f'<span style="color:{GOLD};font-size:6px">●</span> ')
b+=A(L,syy+56,'RtMは鉱山会社から製錬所へ、製錬所から需要家へ、2度の流通を担い、川上と川下をつなぐ',W,'sm')
# P09
o,yy=H2(R,52,'02｜独自価値　新技術','第2章　独自価値','Investing in<br>what\'s next.','新技術への取り組み','加工技術・回収・リサイクルなど、業界のボトルネックに挑む技術へ投資する',body=50,bw=360)
b+=o
cx,cy=R+250,500; rx,ry=225,78
b+=sph(cx,cy,190,1)
b+=svg(0,0,1190,842,f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{GOLD}" stroke-width="1"/>')
stg=[(180,'','採掘',-48,-6),(140,'','選鉱・浸出',-62,8),(60,'','製錬・精製',6,6),(0,'','電化・再エネ・AI/DC',-40,10),(270,'','リサイクル',-18,-30)]
for a,e,j,ox,oy in stg:
    t=math.radians(a); x=cx+rx*math.cos(t); y=cy+ry*math.sin(t)
    b+=f'<div class="a" style="left:{x-4}px;top:{y-4}px;width:8px;height:8px;border-radius:50%;background:{GOLD}"></div>'+A(x+ox,y+oy,f'<b style="font-weight:400;font-size:7px;color:{INK}">{e}</b><br>{j}',80,'sm')
chips=[(cx-178,cy-56,'CiDRA','銅｜スタートアップ','浮遊選鉱の高度化','回収率・処理能力を向上'),(cx+28,cy-56,'Jetti','銅｜スタートアップ','硫化鉱のリーチング化','触媒で硫化鉱から銅を回収'),(cx-75,cy+16,'DESCycle','リサイクル','銅スクラップの回収強化','電子スクラップから銅・貴金属を回収')]
for x,y,n,t,h,d in chips:
    b+=A(x,y,f'<div style="font-size:5.4px;letter-spacing:1.2px;color:{GOLD}">{t}</div><div style="font-size:9.5px;font-weight:400">{n}</div><div class="smb" style="font-size:6.8px">{h}</div><div class="sm" style="font-size:5.8px">{d}</div>',150,'',f'height:58px;padding:6px 12px;background:rgba(255,255,255,.88);border:.6px solid {HAIR};border-radius:29px')
pages.append(spread(b,8,9,'ハブ図は削除し、5つの機能＝ガラス球を回る衛星に。本文を追加し、拠点一覧はP.05の販売網へ移動。銅を例にトレーディングが2度介在するバリューチェーンを追加。','CVCを「新技術」の枠で。CiDRA（浮遊選鉱の高度化）・Jetti（硫化鉱のリーチング化）・DESCycle（銅スクラップ回収）の3例。原料炭の枠は削除。',orb))

# =================== P10 / P11 ===================
orb=flow('M-10,300 C120,360 300,385 595,330 S900,242 1190,240',GOLD,.75,.8,[(300,371),(900,248)])
b=f'<img class="a ph" src="{uri("r-084.png",1600)}" style="left:0;top:0;width:595px;height:400px;object-position:50% 30%;clip-path:circle(330px at 300px 40px)">'
b+=svg(0,0,595,842,f'<ellipse cx="300" cy="230" rx="330" ry="40" transform="rotate(-6 300 230)" fill="none" stroke="{GOLDL}" stroke-width=".7"/>')
b+=A(L,40,'03｜選ばれ続ける理由',None,'lab','color:#fff;text-shadow:0 0 6px rgba(0,0,0,.4)')
b+=BIG(400,350,'03')
o,yy=H2(L,370,'','','Partner of choice.','第3章　選ばれ続ける理由','資源業界に不可欠な存在として、世界のトッププレイヤーから選ばれ続ける',body=46,bw=W)
b+=o
st4=[('','資源メジャーとの企業文化的親和性'),('','資源投資経験に裏打ちされたJV経営力'),('','事業ポートフォリオを活かした健全な財務基盤'),('','マクロ環境とバリューチェーンに対する深い知見')]
for i,(e,j) in enumerate(st4):
    x=L+(i%2)*255; y=yy+14+(i//2)*44
    b+=A(x,y,f'0{i+1}',None,'num','font-size:26px;color:'+GOLD)+A(x+40,y+2,e,205,'','font-size:8.6px;font-weight:400')+A(x+40,y+16,j,205,'sm')
jy=yy+112
b+=A(L,jy,'',W,'',f'border-top:.6px solid {HAIR}')
b+=SEC(L,jy+10,'業界最大手とのJV実績','業界最大手とのJV実績',300)
for i,n in enumerate(['BHP','Rio Tinto','Anglo American']):
    b+=A(L+i*130,jy+30,n,None,'','font-size:14px;font-weight:300')
b+=A(L,jy+54,'単なる共同出資者に留まらず、人材派遣・ガバナンス参画・総合力でJVの事業価値を最大化',W,'sm')
b+=SEC(L,jy+76,'パートナーに評価される理由','パートナーに評価される理由',190)
for i,(e,j) in enumerate([('','中長期的な視座'),('','リスクシェアリング'),('','総合力')]):
    x=L+i*168
    b+=A(x,jy+96,f'<div class="smb">{j}</div><div class="cap" style="font-size:5.6px;margin-top:2px">{e.upper()}</div>',156,'',f'height:34px;border-radius:17px;border:.8px solid {GOLD};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center')
# P11
b+=BIG(935,40,'04')
o,yy=H2(R,52,'04｜何を実現するか','第4章　何を実現するか','Building the future<br>of resources, together.','共に、資源の未来を築く','クリティカルミネラルを取り巻く外部環境に、安定供給と効率的な供給の両面で応える')
b+=o
cy=yy+105; cxs=[R+85,R+250,R+415]
fz=[('需要の拡大','産業構造の転換<br>人口増・電化による需要拡大'),('供給制約','供給制約の深刻化'),('地政学リスク','地政学リスクの常態化')]
for i,(x,(e,j)) in enumerate(zip(cxs,fz)):
    b+=svg(0,0,1190,842,f'<ellipse cx="{x}" cy="{cy+6}" rx="80" ry="18" transform="rotate(8 {x} {cy+6})" fill="none" stroke="{GOLD}" stroke-width=".7" opacity=".9"/>')
    b+=sph(x,cy,124,i)+A(x-60,cy-18,f'<div style="font-size:8.6px;font-weight:400">{e}</div><div class="sm" style="font-size:6px;margin-top:3px">{j}</div>',120,'','text-align:center')
b+=svg(R,cy+70,W,60,f'<path d="M70,0 L250,46 L430,0" fill="none" stroke="{GOLD}" stroke-width=".8"/><circle cx="250" cy="46" r="3" fill="{GOLD}"/>')
b+=A(R,cy+124,'サプライチェーン確保の重要性と、川上資源への参入障壁が増大',W,'smb','text-align:center')
b+=SEC(R,cy+170,'私たちの約束','私たちの約束',150)
b+=A(R,cy+190,'「社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する」',W-20,'en','font-size:15px;line-height:1.45')

FB=uri('v9/globe_new.png',1000,'PNG')
_s=300/875
b+=f'<img class="a" src="{FB}" style="left:{R+440-755*_s:.1f}px;top:{790-515*_s:.1f}px;width:{1536*_s:.1f}px;height:{1024*_s:.1f}px">'
b+=SEC(R,690,'お問い合わせ','お問い合わせ',90)+A(R,710,'三菱商事　金属資源グループ<br>〒100-8086 東京都千代田区丸の内2-3-1<br>www.mitsubishicorp.com',260,'','font-size:7px;line-height:1.7;font-weight:300;color:'+SUB)
pages.append(spread(b,10,11,'写真を丸い「レンズ」で切り抜き、金の軌道が周回。本文を追加。JV実績のラベルを拡大し、「パートナーに評価される理由」（中長期的な視座・リスクシェアリング・総合力）を復活。','外部環境の3つの変化を3つのガラス球に。最後に日本側の地球儀が現れ、軌道が裏表紙へ抜けて冊子を閉じる。',orb))

links=''.join(f'<link rel="stylesheet" href="f/nsjp/package/{w}.css">' for w in (300,400,500))
open('daiwari_v15.html','w').write('<!doctype html><meta charset=utf-8>'+links+'<style>'+CSS+'</style>'+''.join(pages))
