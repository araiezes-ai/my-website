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
.b{{font-family:'Noto Sans JP';font-weight:400;font-size:7.7px;line-height:1.85;letter-spacing:.2px;color:{G1};text-align:justify}}
.s{{font-family:'Noto Sans JP';font-weight:400;font-size:6.7px;line-height:1.6;color:{G2}}}
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
CSS2+=".out{font-family:IT;font-weight:300;line-height:.8;letter-spacing:-.04em;color:transparent;-webkit-text-stroke:.8px #c9ced3}\n"
def OUT(x,y,t,size=140,col='#c9ced3'): return T(x,y,t,None,'out',f'font-size:{size}px;-webkit-text-stroke-color:{col}')
def BAND(x,y,w,h,f='brush_a',pos='50% 50%'): return f'<img class="a ph" src="{uri("v9/"+f+".png",2400,"PNG")}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-position:{pos}">'
pages=[]

# ============ P02-03  OPENING ============
g=4
b=tile(0,0,330,250,'r-022.png','50% 60%','都市','鉄・銅・アルミ')
b+=tile(334,0,261,123,'x_vc_ev.jpg','50% 55%','モビリティ','鉄・銅・リチウム')
b+=ptile(334,127,261,123,'鉄道','鉄・銅','鉄道の写真（ストック）')
b+=tile(0,254,163,146,'x_vc_wind.jpg','50% 30%','再生可能エネルギー','銅・鉄')
b+=tile(167,254,163,146,'x_case_pylon.jpg','50% 50%','送電網','銅・アルミ')
b+=ptile(334,254,261,146,'デバイス','銅・リチウム・ニッケル','スマートフォン・データセンターの写真（ストック）')
b+=tile(599,0,330,264,'mr_03_01@2x.webp','50% 50%','金属','現代の暮らしを支える素材',2000)
b+=tile(933,0,257,264,'x_vc_smelter.jpg','50% 50%','製錬・精製','')
b+=tile(599,268,257,132,'r-023.png','50% 60%','海上輸送','')
b+=tile(860,268,330,132,'r-054.png','50% 55%','銅地金','')
# copy
b+=T(L,438,'導入',None,'k')+T(L,449,'導入｜社会と金属',None,'kj')
b+=T(L,470,'Metals shape<br>the way we live.',540,'d','font-size:50px')
b+=A(L,580,'',22,'',f'border-top:1.4px solid {RED}')
b+=T(L,592,'暮らしのすべてに、金属がある。',None,'h','font-size:15px')
b+=para(L,620,250,'ビル、鉄道、自動車、スマートフォン、送電網、再生可能エネルギー——私たちの豊かな暮らしは、鉄や銅をはじめとする金属に支えられています。人口の増加と新興国の発展、そして社会の電化によって、金属の需要はこれからも拡大を続けます。一方で、良質な資源の開発は年々難しくなり、地政学的なリスクも常態化しつつあります。')
# demand vs supply concept chart
cx0,cy0,cw,ch=L+290,612,225,140
o=f'<rect x="{cx0}" y="{cy0}" width="{cw}" height="{ch}" fill="{PAN}"/>'
dem=[(cx0+16+i*(cw-32)/10, cy0+ch-24-(i**1.45)*3.6) for i in range(11)]
sup=[(cx0+16+i*(cw-32)/10, cy0+ch-24-min(i,6)*6.5-max(0,i-6)*1.8) for i in range(11)]
area='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in dem)+' L'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in reversed(sup))+'Z'
o+=f'<path d="{area}" fill="{BRL}" opacity=".35"/>'
o+=f'<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in dem)+f'" fill="none" stroke="{INK}" stroke-width="1.6"/>'
o+=f'<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in sup)+f'" fill="none" stroke="{G2}" stroke-width="1.6" stroke-dasharray="3 2"/>'
o+=f'<line x1="{cx0+16}" y1="{cy0+ch-22}" x2="{cx0+cw-14}" y2="{cy0+ch-22}" stroke="{G3}" stroke-width=".6"/>'
b+=S(o)
b+=T(cx0+10,cy0+8,'需要と供給',None,'k','color:'+G1)+T(cx0+10,cy0+18,'概念図（数値は入れない）',None,'s','font-size:5.4px')
b+=T(cx0+cw-70,cy0+30,'需要',None,'l')+T(cx0+cw-70,cy0+39,'人口増・電化',None,'s','font-size:5.6px')
b+=T(cx0+cw-62,cy0+ch-58,'供給',None,'l','color:'+G2)+T(cx0+cw-62,cy0+ch-49,'供給制約・地政学',None,'s','font-size:5.6px')
b+=T(cx0+cw-104,cy0+ch-66,'ギャップ',None,'k','color:'+BR)
b+=T(cx0+16,cy0+ch-14,'現在',None,'s','font-size:5.4px')+T(cx0+cw-40,cy0+ch-14,'将来',None,'s','font-size:5.4px')
# right: core message
b+=T(R,438,'コアメッセージ',None,'k')+T(R,449,'コアメッセージ',None,'kj')
b+=T(R,470,'Strength to Hold.<br>Power to Connect.',W,'dl','font-size:42px')
b+=T(R,566,'持つ力と、つなぐ力。',None,'h','font-size:13px')
b+=para(R,590,300,'資源は、そこに「ある」だけでは、まだ価値ではありません。誰かが見出し、育て、必要とする場所へ届けて、はじめて力になる。私たちは、世界有数の資産に関わり、投資とトレーディングの両輪で川上から川下までをつなぎます。フェアな立場だからこそ、埋められる隙間がある。多様なパートナーと使い手の間に立ち、その時々の最適解を導く。世界に眠る価値を、社会の力へ。')
toc=[('01','我々は何者か'),('02','資産の強み'),('03','原料炭と銅'),('04','資源から価値へ'),('05','パートナーシップ'),('06','バリューチェーン')]
b+=T(R+330,590,'目次',None,'k')
for i,(n,e) in enumerate(toc):
    y=606+i*21; b+=rule(R+330,y,185)+T(R+330,y+6,n,None,'l','color:'+BR)+T(R+350,y+6,e,None,'l')+T(R+495,y+6,f'P.{[4,5,6,8,9,10][i]:02d}',None,'fo','font-size:5.4px')
b+=BAND(0,824,1190,18)
pages.append(spread(b,2,3,'動画01 OPENING。地球儀は使わず、暮らしと金属の写真を見開きで1枚のモザイクに（左＝暮らし、右＝それを支える金属）。キャッチコピー＋需要と供給のギャップを概念図で。','コアメッセージ（英・和）全文と目次。写真の帯が見開きをつなぎ、下段は左右で「問い」と「答え」の関係に。鉄道・スマホは素材待ち。'))

# ============ P04-05  WHO WE ARE / OUR STRENGTHS（+歩みを見開きで） ============
o,yy=head(L,40,'01｜我々は何者か','第1章　我々は何者か','Who we are.','三菱商事 金属資源グループとは',size=44)
b=o
b+=para(L,yy+4,250,'三菱商事は、三綱領（所期奉公・処事光明・立業貿易）を企業理念に、経済価値・環境価値・社会価値の同時実現を目指す総合商社です。そのなかで金属資源グループは、社会に不可欠な金属資源を世界から確保し、安定的に届ける役割を担っています。原料炭と銅は、全社としてコミットする中核事業です。')
# mission panel
b+=A(L+270,yy-26,'',245,'',f'height:118px;background:{PAN}')
b+=T(L+284,yy-14,'グループミッション',None,'k')+T(L+284,yy+2,'社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する',215,'hs','font-size:9.4px;line-height:1.6')
b+=T(L+284,yy+60,'',215,'s','font-family:IN;font-size:6.2px')
# organisation infographic
oy=yy+110
b+=T(L,oy,'組織',None,'k')+T(L+80,oy,'投資を担う2本部と、トレーディングを担う1本部',None,'kj')
b+=A(L+190,oy+22,'<div class="l" style="text-align:center">グループCEO</div>',130,'',f'height:22px;border:1px solid {INK};display:flex;align-items:center;justify-content:center')
o=f'<line x1="{L+255}" y1="{oy+44}" x2="{L+255}" y2="{oy+56}" stroke="{INK}" stroke-width=".8"/><line x1="{L+85}" y1="{oy+56}" x2="{L+430}" y2="{oy+56}" stroke="{INK}" stroke-width=".8"/>'
divs=[('','鉄鋼原料本部','原料炭・鉄鉱石','MDP',BR),('','クリティカルミネラル本部','銅・ニッケル・リチウム・アルミ ほか','MCI · MCIP',BR),('','金属資源トレーディング本部','RtM（Resource to Market）','RtM · Triland Metals',NV)]
for i,(e,j,c,a,col) in enumerate(divs):
    x=L+i*172; o+=f'<line x1="{x+85}" y1="{oy+56}" x2="{x+85}" y2="{oy+66}" stroke="{INK}" stroke-width=".8"/>'
    b+=A(x,oy+66,f'<div style="font-family:IN;font-size:5.6px;letter-spacing:1.2px;color:#fff;text-transform:uppercase">{"投資" if i<2 else "トレーディング"}</div><div style="font-family:Noto Sans JP;font-weight:700;font-size:8.4px;color:#fff;margin-top:2px">{j}</div><div style="font-family:IN;font-size:5.8px;color:#fff;opacity:.85">{e}</div>',165,'',f'height:46px;background:{col};padding:7px 9px')
    b+=T(x,oy+118,c,165,'hs','font-size:7.4px')+T(x,oy+132,'主要関係会社：'+a,165,'s')
b+=S(o)
vy=oy+156
b+=rule(L,vy,W,INK,1)
b+=T(L,vy+10,'三綱領',None,'k')+T(L+170,vy+10,'三綱領｜三菱商事の企業理念',None,'kj')
for i,(j,r_,e) in enumerate([('所期奉公','しょきほうこう','事業を通じ、物心ともに豊かな社会の実現に努める'),('処事光明','しょじこうめい','公明正大で品格のある行動を旨とする'),('立業貿易','りつぎょうぼうえき','全世界的、宇宙的視野に立脚した事業展開を図る')]):
    x=L+i*172
    b+=T(x,vy+30,j,None,'h','font-size:14px')+T(x,vy+50,r_,165,'l','font-size:6.4px;color:'+BR)+T(x,vy+62,e,160,'s')
# P05 strengths map
o,yy=head(R,40,'02｜資産の強み','第2章　独自価値｜資産の強み','Tier-1 assets<br>at the source.','バリューチェーンの起点で、一級資産を保有する',size=44)
b+=o
b+=para(R,yy+4,250,'資源事業は規模の経済が働くビジネスです。私たちは、規模で世界上位に入る優良鉱山に早くから参画し、現在では資金があっても手に入らない資産のポートフォリオを築いてきました。その中核が、原料炭と銅です。')
MW=530; MH=MW*996/2600; mx,my=R-10,yy+70
b+=IMG(mx,my,MW,MH,'v8/flat_std.png',fmt='PNG',light=.55,mx=1800)
P=lambda lon,lat:(mx+(lon+170)/360*MW,my+(80-lat)/138*MH)
o=''
pts=[((148.3,-22.3),'原料炭','豪州 ボーエン・ベースン',-118,-6),((-70,-24),'銅','チリ・ペルー',10,-4),((-110.9,31.9),'銅','米国',-56,-14)]
for (lo,la),e,j,dx,dy in pts:
    x,y=P(lo,la); o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="{BR}" opacity=".18"/><circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{BR}" stroke="#fff" stroke-width="1"/>'
    b+=T(x+dx,y+dy,f'<b style="font-family:IT;font-weight:600;font-size:8.6px">{e}</b><br><span class="s">{j}</span>',120)
for lo,la in [(-69.07,-24.27),(-70.5,-31.7),(-70.3,-33.15),(-77.05,-9.53),(-70.6,-17.1)]:
    x,y=P(lo,la); o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.4" fill="{BR}"/>'
b+=S(o)
ky=my+MH+14
for i,(n,u,t) in enumerate([('5','5鉱山中','銅の主要5鉱山すべてが規模で世界Top15'),('~50%','シェア','一級強粘炭の世界供給に占めるBMAのシェア'),('60+','年以上','原料炭の炭鉱寿命')]):
    x=R+i*176; b+=rule(x,ky,160,INK,1)+T(x,ky+8,n,None,'nb','font-size:34px')+T(x,ky+44,u.upper(),None,'l','font-size:5.8px;letter-spacing:1.4px;color:'+G2)+T(x,ky+55,t,160,'s')
# journey band across the spread
jy=640
b+=A(0,jy-14,'',1190,'',f'height:186px;background:{PAN}')
b+=T(L,jy,'歩み｜先見性',None,'k')+T(L+150,jy,'時代を先読みし、事業モデルを変え続けてきた歩み',None,'kj')
o=f'<line x1="{L}" y1="{jy+46}" x2="{1190-L}" y2="{jy+46}" stroke="{INK}" stroke-width=".8"/>'
eras=[('1980s–90s','トレーディングで参入','日本が世界最大の消費国だった時代。資源を日本へ運ぶ役割から始まり、少数株主として出資。'),
      ('1990s','投資モデルへ転換','口銭モデルから投資モデルへ。JV運営の知見を蓄積し、事業経営へと舵を切る。'),
      ('2000s','BHPと50:50のBMA','2001年、BHPと50:50でBMAを組成。中国の成長を捉え、世界の一級原料炭資産の経営に参画。'),
      ('2010s','銅の権益を拡大','「原料炭だけでよいのか」という問いから銅へ。Anglo Americanと組みQuellavecoなど大型化。'),
      ('2020s','グローバルなトレーダーへ','各地のマーケティングをRtMとしてシンガポールに集約。地域特化から世界の市場へ。')]
for i,(yr,t,d_) in enumerate(eras):
    x=L+i*226
    o+=f'<circle cx="{x+4}" cy="{jy+46}" r="4" fill="{BR if i in (2,3) else INK}"/>'
    b+=T(x,jy+18,yr,None,'nb','font-size:18px')+T(x,jy+58,t,210,'hs','font-size:8.2px')+T(x,jy+74,d_,205,'b','font-size:6.6px;line-height:1.7')
b+=S(o)
b=OUT(436,6,'01')+OUT(1000,6,'02')+b+BAND(0,824,1190,18,'brush_a')
pages.append(spread(b,4,5,'動画02 Who we are。三菱商事→金属資源G→組織（投資2本部＋トレーディング1本部、関係会社）を1ページに。ミッションはパネルで強調。','動画03 Our Strengths。【強調】一級資産の地図と数字3つ。下段の「歩み（先見性）」は見開き全幅の帯で左右をつなぐ（参考資料P34の意向）。'))

# ============ P06-07  COAL & COPPER（強調） ============
b=tile(0,0,595,330,'r-047.png','60% 40%')+tile(595,0,595,330,'mr_02_01@2x.webp','50% 50%',mx=2000)
b+=A(0,0,'',1190,'','height:330px;background:linear-gradient(0deg,rgba(10,14,18,.7) 0%,rgba(10,14,18,.15) 45%,rgba(10,14,18,0) 70%,rgba(10,14,18,.3) 100%)')
b+=T(L,40,'02｜原料炭',None,'k','color:#e9d6ac')+T(R,40,'02｜銅',None,'k','color:#e9d6ac')
b+=T(L,270,'~50%',None,'nb','font-size:64px;color:#fff')+T(L+170,282,'一級強粘炭の世界供給に<br>占めるBMAのシェア',None,'hs','color:#fff;font-size:8.6px')
b+=T(R,270,'No.1',None,'nb','font-size:64px;color:#fff')+T(R+150,282,'ノンオペレーター（自社操業を伴わない<br>参画者）として世界最大の銅生産者',None,'hs','color:#fff;font-size:8.6px')
# coal text
b+=T(L,352,'World-class<br>metallurgical coal.',W,'d','font-size:30px')+A(L,420,'',22,'',f'border-top:1.4px solid {RED}')+T(L,430,'原料炭事業｜鉄の主原料“産業のコメ”を、世界最高品位で',None,'h')
b+=para(L,452,250,'BHPと50:50の合弁であるBMA（BHP Mitsubishi Alliance）を通じ、豪州クイーンズランド州ボーエン・ベースンで世界最高品位の原料炭事業に参画しています。炭鉱（露天掘4・坑内掘1）に加え、港湾と鉄道までを自社で保有し、山から港まで全体最適で運営。保有鉱山は高品位のものに集約し、高品位原料の供給を通じて鉄鋼業の脱炭素にも貢献しています。')
# 4-step logic
lx,ly=L+270,452
for i,(n,t) in enumerate([('01','世界最高品位の原料炭を保有'),('02','原料炭は鉄の主原料＝“産業のコメ”'),('03','鉄は今後も底堅く必要とされる'),('04','ゆえに、社会に不可欠')]):
    y=ly+i*30; b+=T(lx,y,n,None,'nb','font-size:15px;color:'+BR)+T(lx+28,y+3,t,220,'hs','font-size:8px')+(rule(lx,y+24,245) if i<3 else '')
# ownership + facts
fy=572
b+=T(L,fy,'出資構成',None,'k')
b+=A(L,fy+16,'<div class="l">三菱商事</div>',90,'',f'height:24px;border:1px solid {INK};display:flex;align-items:center;justify-content:center')
b+=A(L+120,fy+16,'<div class="l">MDP</div>',70,'',f'height:24px;border:1px solid {INK};display:flex;align-items:center;justify-content:center')
b+=A(L+120,fy+48,'<div class="l">BHP</div>',70,'',f'height:24px;border:1px solid {G2};display:flex;align-items:center;justify-content:center')
b+=A(L+226,fy+30,'<div class="l" style="color:#fff">BMA</div>',80,'',f'height:28px;background:{BR};display:flex;align-items:center;justify-content:center')
b+=S(f'<path d="M{L+90},{fy+28} H{L+118} M{L+190},{fy+28} H{L+206} V{fy+60} H{L+190} M{L+206},{fy+44} H{L+224}" fill="none" stroke="{INK}" stroke-width=".8"/>')
b+=T(L+96,fy+19,'100%',None,'s','font-size:5.4px')+T(L+193,fy+20,'50%',None,'s','font-size:5.4px')+T(L+193,fy+62,'50%',None,'s','font-size:5.4px')
facts=[('設立','1968年 MDP設立／2001年 BMA組成'),('所在地','豪州クイーンズランド州 Bowen Basin'),('保有資産','炭鉱5（露天掘4・坑内掘1）・港湾・鉄道'),('炭鉱寿命','60年以上'),('海上輸出シェア','原料炭の海上輸出市場で約20%')]
for i,(k_,v) in enumerate(facts):
    y=fy+84+i*15; b+=rule(L,y,W)+T(L,y+4,k_,None,'l','color:'+G2)+T(L+110,y+3,v,None,'hs','font-size:7.2px')
# copper text
b+=T(R,352,'The partner the copper<br>industry calls first.',W+20,'d','font-size:30px')+A(R,420,'',22,'',f'border-top:1.4px solid {RED}')+T(R,430,'銅事業｜自社操業を伴わずに、世界最大級の銅ポジションを築く',None,'h')
b+=para(R,452,250,'銅は原料炭に比べてプレイヤーが多く、寡占化が進んでいない市場です。そのなかで私たちは、規模で世界上位15に入る優良鉱山に複数参画し、日本最大・世界第20位の持分生産量を有しています。特定の1社に偏らず、主要メジャーのほぼすべてと共同事業・取引を行い、販売を通じた幅広い関係から、新しい案件で“声がかかる存在”であり続けています。')
# mines timeline (early mover)
tx,ty=R+270,452
b+=T(tx,ty,'主要鉱山への参画',None,'k')+T(tx+70,ty,'主要鉱山への参画年',None,'kj')
mines=[(1988,'Escondida','チリ'),(1997,'Los Pelambres','チリ'),(1999,'Antamina','ペルー'),(2011,'Anglo American Sur','チリ'),(2011,'Quellaveco','ペルー'),(2023,'Marimaca','チリ・開発中'),(2025,'Copper World','米国・開発中')]
X=lambda yr: tx+(yr-1985)/42*245
o=f'<line x1="{tx}" y1="{ty+30}" x2="{tx+245}" y2="{ty+30}" stroke="{INK}" stroke-width=".8"/>'
for yr in (1990,2000,2010,2020):
    o+=f'<line x1="{X(yr):.1f}" y1="{ty+27}" x2="{X(yr):.1f}" y2="{ty+33}" stroke="{INK}" stroke-width=".6"/>'; b+=T(X(yr)-10,ty+16,str(yr),None,'s','font-family:IN;font-size:5.6px')
for i,(yr,n,c) in enumerate(mines):
    x=X(yr); y=ty+42+i*13
    o+=f'<line x1="{x:.1f}" y1="{ty+30}" x2="{x:.1f}" y2="{y+4}" stroke="{G3}" stroke-width=".6"/><circle cx="{x:.1f}" cy="{y+4}" r="2.6" fill="{BR if "開発" not in c else "#fff"}" stroke="{BR}" stroke-width="1"/>'
    lab=f'<b style="font-family:IN;font-weight:600">{n}</b> <span class="s">{c}・{yr}</span>'
    b+=(T(x+6,y,lab,200,'l','font-size:6.4px') if yr<2015 else T(x-206,y,lab,200,'l','font-size:6.4px;text-align:right'))
b+=S(o)
# copper ranking (dataviz: single highlight, gray others, direct labels)
ry=fy-4
b+=T(R,ry,'会社別 世界銅生産量（2025年）',None,'k')+T(R+150,ry,'会社別 世界銅生産量（kt）',None,'kj')
rk=[('BHP',1501),('Codelco',1432),('Freeport',1099),('Southern Copper',948),('Zijin Mining',850),('Glencore',812),('Rio Tinto',740),('China Moly',558),('KGHM',538),('Anglo American',496),('三菱商事',326)]
o=''
for i,(n,v) in enumerate(rk):
    y=ry+18+i*12.4; me=n.startswith('三菱商事'); w_=v/1501*300
    if me: y+=4
    o+=f'<rect x="{R+92}" y="{y}" width="{w_:.1f}" height="8" rx="1" fill="{BR if me else G3}"/>'
    b+=T(R,y-.5,('#20 ' if me else f'#{i+1} ')+n,90,'l',f'font-size:6px;text-align:right;padding-right:6px;{"color:"+BR+";font-weight:600" if me else "color:"+G1}')+T(R+96+w_,y-.5,f'{v:,}',None,'l','font-size:5.8px;color:'+(BR if me else G2))
b+=S(o)
b+=T(R+330,ry+100,'上位には協業が難しい国有・政府系なども含まれる。協業可能で、オペレーターシップを求めないパートナーとしては最大規模。',185,'s')
# market structure bar across spread bottom
mb=768
b+=rule(L,mb-8,1190-2*L,INK,.8)
b+=T(L,mb,'市場構造',None,'k')+T(L+110,mb,'上位5社のシェア',None,'kj')
for x0,lab,v,t in [(L,'原料炭',80,'上位5社で約80%｜寡占度が高く、供給は漸減'),(R,'銅',25,'上位5社で約25%｜寡占化が進まず、再編の機運')]:
    b+=T(x0,mb+16,lab,None,'l','font-size:7px')+A(x0+100,mb+16,'',400,'',f'height:10px;background:{G4}')+A(x0+100,mb+16,'',400*v/100,'',f'height:10px;background:{INK}')+T(x0+100+400*v/100+6,mb+15,f'{v}%',None,'nb','font-size:10px')+T(x0+100,mb+30,t,None,'s')
b+=BAND(0,824,1190,18)
pages.append(spread(b,6,7,'動画04 Coking Coal。【強調】写真の上に大きな数字。品位→鉄→需要→社会の4段ロジック、出資構成図、基本データ表。','動画05 Copper。【強調】参画年のタイムライン（先行して一級資産を確保）と生産量ランキング（当社のみ色）。最下段の「市場構造」バーが原料炭と銅を見開きで比較する。'))

# ============ P08-09  FROM RESOURCES TO VALUE / GLOBAL PARTNERSHIPS ============
o,yy=head(L,40,'03｜資源から価値へ','第2章　独自価値｜事業領域と新技術','Resources become<br>value when delivered.','鉄鉱石から電池資源・肥料・アルミまで、世界に広がる事業領域',size=36)
b=o
b+=para(L,yy+2,W,'資源は、ただ存在するだけでは社会の価値になりません。良質な資源を安定的に確保し、高品質な金属へと精錬し、必要とする産業へ届けてはじめて価値になります。原料炭と銅に加え、私たちは鉄鉱石、電池資源、アルミ、肥料、二次資源へと事業領域を広げています。')
gy=yy+68
port=[('','鉄鉱石','IOC（カナダ）・CMP（チリ）','x_ironore.jpg'),('','ニッケル','Turnagain（カナダ）・Kalgoorlie（豪州）','x_case_mine.jpg'),('','リチウム','PAK Lithium（カナダ）','x_lithium.jpg'),('','ボーキサイト・低炭素アルミ','Aurukun（豪州）・Arctial（北欧）','x_alu.jpg'),('','肥料資源','Woodsmith（英国）',None),('','二次資源','リサイクル由来の金属資源','r-074.png')]
for i,(e,j,p_,f) in enumerate(port):
    x=L+(i%3)*174; y=gy+(i//3)*104
    b+=(CIRC(x+32,y+34,64,f,ring=False) if f else A(x,y+2,'',64,'',f'height:64px;border-radius:50%;border:1px solid {BR}'))
    b+=T(x+74,y+10,e,None,'l','font-size:7.6px;font-weight:600')+T(x+74,y+22,j,None,'hs','font-size:7.8px')+T(x+74,y+38,p_,92,'s')
    b+=rule(x,y+82,160)
# copper chain + tech
cy=gy+222
b+=T(L,cy,'銅のバリューチェーンと新技術',None,'k')+T(L,cy+11,'山を持つだけでなく、川上から川下までのボトルネックに技術で網を張る',None,'kj')
st=[('採掘','採掘','Cu ~1%'),('銅精鉱','選鉱・浸出','Cu 20–30%'),('銅地金','製錬・精製','Cu 99.99%'),('最終用途','最終製品','電化・インフラ'),('リサイクル','回収','再び供給へ')]
o=''
for i,(e,j,g_) in enumerate(st):
    x=L+i*104; y=cy+34
    b+=A(x,y,'',96,'',f'height:44px;background:{PAN}')
    b+=T(x+8,y+7,e,None,'l','font-size:7.2px;font-weight:600')+T(x+8,y+18,j,None,'s')+T(x+8,y+29,g_,None,'nb','font-size:9px;color:'+BR)
    if i<4: o+=f'<path d="M{x+97},{y+22} l6,0" stroke="{INK}" stroke-width=".8"/>'
tech=[(1,'CiDRA','スタートアップ｜選鉱','浮遊選鉱の高度化で、回収率・処理能力を向上'),(1,'Jetti','スタートアップ｜浸出','新しい触媒で、硫化鉱から銅をリーチング'),(2,'Triland Metals','トレーディング｜100%子会社','LME・CMEでのブローカー・ヘッジ機能'),(4,'DESCycle','リサイクル｜回収','電子スクラップから銅・貴金属を回収')]
for k,(si,n,t_,d_) in enumerate(tech):
    x=L+k*130; y=cy+112; sx_=L+si*104+48+(-12 if k==0 else 12 if k==1 else 0)
    o+=f'<path d="M{sx_},{cy+78} V{cy+96} H{x+10} V{y}" fill="none" stroke="{BR}" stroke-width=".7"/><circle cx="{sx_}" cy="{cy+78}" r="2" fill="{BR}"/>'
    b+=A(x,y,f'<div style="font-family:IN;font-weight:600;font-size:5.4px;letter-spacing:1.2px;color:{BR}">{t_}</div><div class="l" style="font-weight:600;font-size:8.6px;margin-top:2px">{n}</div><div class="s" style="margin-top:2px">{d_}</div>',122,'',f'height:58px;padding:7px 9px;border-top:1.4px solid {BR};background:#fff')
b+=S(o)
py8=cy+196
b+=para(L,py8,250,'新技術の把握は、既存事業の高度化と将来価値の創出に還元されます。業界のボトルネック——鉱石品位の低下、回収率、リサイクル——に挑むスタートアップへの投資を通じ、山を持つだけでも、売るだけでもない、川上から川下までのフットプリントを広げています。')
b+=tile(L+270,py8,245,112,'_mr_project_03.png','50% 50%','銅鉱山','チリ')
# P09 partnerships
o,yy=head(R,40,'04｜パートナーシップ','第3章　選ばれ続ける理由','Partner of choice.','メジャーとのパートナーシップと、世界の販売網',size=36)
b+=o
b+=para(R,yy+2,W,'資源業界では、良い案件があっても単独では規模が大きすぎることが少なくありません。そのとき「三菱に声をかけよう」と思われる存在であること。BHP、Rio Tinto、Anglo Americanをはじめとする業界最大手とJVを組み、単なる共同出資者に留まらず、人材派遣・ガバナンス参画・総合力で事業価値の最大化に貢献してきました。')
py=yy+76
four=[('','資源メジャーとの企業文化的親和性','短期の成果を求める投資家とは一線を画す、中長期の視座。'),('','資源投資経験に裏打ちされたJV経営力','実質的な経営貢献と、高い目利き力。'),('','事業ポートフォリオを活かした健全な財務基盤','リスクシェアリングと制度金融のファシリテーション。'),('','マクロ環境とバリューチェーンへの深い知見','国・地域の拠点と幅広い産業接点からの知見。')]
for i,(e,j,d_) in enumerate(four):
    x=R+(i%2)*262; y=py+(i//2)*74
    b+=T(x,y,f'0{i+1}',None,'nb','font-size:20px;color:'+BR)+T(x+32,y+1,e,None,'l','font-size:7.4px;font-weight:600')+T(x+32,y+12,j,215,'hs','font-size:7.6px')+T(x+32,y+26,d_,215,'s')
# network map
ny=py+164
b+=T(R,ny,'販売網',None,'k')+T(R+108,ny,'RtM＝Resource to Market｜10拠点の販売網',None,'kj')
MW=370; MH=MW*996/2600; mx,my=R-6,ny+16
b+=IMG(mx,my,MW,MH,'v8/flat_std.png',fmt='PNG',light=.6,mx=1400)
P=lambda lon,lat:(mx+(lon+170)/360*MW,my+(80-lat)/138*MH)
offs=[(103.8,1.3),(139.7,35.7),(77.2,28.6),(121.5,31.2),(-77.0,40.4),(-0.1,51.5),(55.3,25.2),(106.8,-6.2),(100.5,13.7),(-70.65,-33.45)]
o=''
sx,sy=P(103.8,1.3)
for lo,la in offs[1:]:
    x,y=P(lo,la); mxp=(sx+x)/2; myp=min(sy,y)-abs(x-sx)*.18-6
    o+=f'<path d="M{sx:.1f},{sy:.1f} Q{mxp:.1f},{myp:.1f} {x:.1f},{y:.1f}" fill="none" stroke="{NV}" stroke-width=".5" opacity=".7"/>'
for lo,la in offs: x,y=P(lo,la); o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="{NV}" stroke="#fff" stroke-width=".7"/>'
b+=S(o)
b+=T(R,my+MH+4,'シンガポール（拠点集約）・日本・インド・中国・米国・英国・UAE・インドネシア・タイ・チリ',330,'s')
nx=R+390
for i,(n,u,j) in enumerate([('15','','業界'),('50','','カ国'),('~1,000','','社の販売先')]):
    y=ny+20+i*48; b+=rule(nx,y,125,INK,1)+T(nx,y+6,n,None,'nb','font-size:24px')+T(nx,y+33,f'{u.upper()}　{j}',None,'l','font-size:5.8px;color:'+G2)
zy=ny+16+MH+40
b+=rule(R,zy,W,INK,1)
b+=T(R,zy+10,'JV実績',None,'k')+T(R+92,zy+10,'業界最大手とのJV実績',None,'kj')
for i,n in enumerate(['BHP','Rio Tinto','Anglo American']): b+=T(R+i*120,zy+26,n,None,'nb','font-size:17px')
b+=T(R+372,zy+26,'他社ロゴは使用せず<br>社名テキストで表記',None,'s')
vy2=zy+70
b+=T(R,vy2,'パートナーに評価される理由',None,'k')+T(R+140,vy2,'パートナーに評価される理由',None,'kj')
for i,(e,j,d_) in enumerate([('','中長期的な視座','資源事業は長期にわたる。短期的リターンを求める投資家とは一線を画す。'),('','リスクシェアリング','リスクの高い案件ほど、資金面の分担を担保する。'),('','総合力','幅広い産業接点を通じ、多様なバリューチェーンに知見を提供する。')]):
    x=R+i*176; b+=A(x,vy2+16,f'<div style="font-family:IN;font-weight:600;font-size:5.6px;letter-spacing:1.2px;color:{BR}">{e.upper()}</div><div class="hs" style="font-size:8.6px;font-weight:700;margin-top:2px">{j}</div><div class="s" style="margin-top:3px">{d_}</div>',164,'',f'height:72px;padding:10px 12px;background:{PAN}')
b=BAND(0,0,1190,22,'brush_b')+OUT(436,26,'03')+OUT(1000,26,'04')+b
pages.append(spread(b,8,9,'動画06 From Resources to Value。その他資源を6つのカードで（案件名と地域）。銅の品位の変化（1%→20–30%→99.99%）の上に、技術投資（CiDRA・Jetti・DESCycle・Triland）を配置。','動画07 Global Partnerships。Partner of Choiceの理由（本文）、4つの強み、RtMの販売網（シンガポール集約の10拠点）とエビデンス数値。'))

# ============ P10-11  INTEGRATED VALUE CHAIN（強調） + CLOSING ============
b=T(L,40,'05｜バリューチェーン全体像',None,'k')+T(L,51,'第2章　独自価値｜バリューチェーン全体像',None,'kj')
b+=T(L,70,'From mine to market — one integrated chain.',1000,'d','font-size:40px')
b+=A(L,128,'',22,'',f'border-top:1.4px solid {RED}')+T(L,138,'投資と販売の両輪で、川上から川下までをつなぐ。採掘・製造・販売をつなぐトレーディング力こそが、総合商社の強み。',None,'h')
# columns header
cols=[('川上','川上','資源開発・保有'),('','中間流通','トレーディング'),('川中','川中','製鉄・製錬'),('','中間流通','トレーディング'),('川下','川下','最終製品・需要家')]
cx=[L,L+230,L+440,L+670,L+880]; cw=[210,190,210,190,230]
hy=190
for i,(e,j,d_) in enumerate(cols):
    tr=(i in (1,3))
    b+=A(cx[i],hy,f'<div style="font-family:IN;font-weight:600;font-size:6px;letter-spacing:1.6px;color:{"#fff" if not tr else NV}">{e or "トレーディング（RtM）"}</div><div style="font-family:Noto Sans JP;font-weight:700;font-size:9px;color:{"#fff" if not tr else NV}">{j}｜{d_}</div>',cw[i],'',f'height:34px;padding:6px 10px;background:{INK if not tr else "#e6ecf2"}')
# rows
rows=[('','鉄鋼',['原料炭・鉄鉱石','鉱山会社／当社資産（BMA・IOC ほか）'],['原料炭・鉄鉱石','RtM'],['製鉄会社','鋼材を製造'],['鋼材','※鋼材販売はメタルワン（別グループ）'],['建材・自動車用鋼板','インフラ・モビリティ']),
      ('','非鉄',['銅鉱石・ボーキサイト','Escondida・Quellaveco ほか'],['銅精鉱・ボーキサイト','RtM'],['製錬会社','銅地金・アルミ地金'],['銅地金・アルミ地金','RtM・Triland Metals'],['電線・再エネ・EV','配線・モーター'])]
for r_,(e,j,*cells) in enumerate(rows):
    y=hy+48+r_*86
    b+=T(L-2,y-12,f'{e.upper()}　{j}',None,'k','color:'+G1)
    for i,(t,s_) in enumerate(cells):
        tr=(i in (1,3))
        b+=A(cx[i],y,f'<div class="hs" style="font-size:8.6px;font-weight:700;color:{NV if tr else INK}">{t}</div><div class="s" style="margin-top:3px">{s_}</div>',cw[i],'',f'height:62px;padding:10px;border:1px solid {NVL if tr else G3};background:#fff')
    o=''.join(f'<path d="M{cx[i]+cw[i]+3},{y+31} H{cx[i+1]-4}" stroke="{INK}" stroke-width=".8"/><path d="M{cx[i+1]-8},{y+28} l4,3 l-4,3" fill="none" stroke="{INK}" stroke-width=".8"/>' for i in range(4))
    b+=S(o)
# two wheels bars
wy=hy+228
b+=A(cx[0],wy,f'<span style="font-family:IN;font-weight:600;font-size:6.4px;letter-spacing:1.6px;color:#fff">投資</span>　<span style="font-family:Noto Sans JP;font-weight:700;font-size:8.4px;color:#fff">資源投資（鉱山・製鉄／製錬）｜鉄鋼原料本部・クリティカルミネラル本部</span>',cx[2]+cw[2]-cx[0],'',f'height:24px;padding:6px 10px;line-height:12px;background:url({uri("v9/brush_inv.png",2400,"PNG")}) center/cover')
b+=A(cx[0],wy+28,f'<span style="font-family:IN;font-weight:600;font-size:6.4px;letter-spacing:1.6px;color:#fff">トレーディング（RtM）</span>　<span style="font-family:Noto Sans JP;font-weight:700;font-size:8.4px;color:#fff">トレーディング｜金属資源トレーディング本部 — 15業界 × 50カ国 × 約1,000社</span>',cx[4]+cw[4]-cx[0],'',f'height:24px;padding:6px 10px;line-height:12px;background:url({uri("v9/brush_trd.png",2400,"PNG")}) center/cover')
# bottom-left: virtuous cycle + functions
by=wy+72
b+=T(L,by,'好循環',None,'k')+T(L+110,by,'投資と販売が連携する好循環',None,'kj')
cxc,cyc=L+80,by+92
o=f'<circle cx="{cxc}" cy="{cyc}" r="58" fill="none" stroke="{G3}" stroke-width="1"/>'
o+=f'<path d="M{cxc-50},{cyc-29} A58,58 0 0 1 {cxc+50},{cyc-29}" fill="none" stroke="{BR}" stroke-width="2.4"/><path d="M{cxc+50},{cyc+29} A58,58 0 0 1 {cxc-50},{cyc+29}" fill="none" stroke="{NV}" stroke-width="2.4"/>'
o+=f'<path d="M{cxc+46},{cyc-36} l6,8 l3,-9" fill="none" stroke="{BR}" stroke-width="1.2"/><path d="M{cxc-46},{cyc+36} l-6,-8 l-3,9" fill="none" stroke="{NV}" stroke-width="1.2"/>'
b+=S(o)
b+=T(cxc-75,cyc-78,'持分見合いのオフテイクをRtMが販売',150,'s','text-align:center;color:'+BR)+T(cxc-75,cyc+64,'顧客接点から得た“生きた情報”を投資判断へ還元',150,'s','text-align:center;color:'+NV)
b+=T(cxc-30,cyc-10,'投資',None,'nb','font-size:11px;color:'+BR)+T(cxc-30,cyc+2,'⇄ 販売',None,'nb','font-size:11px;color:'+NV)
b+=para(L+170,by+22,350,'出資案件から得られる持分見合いのオフテイクをRtMが引き受け、ヘッジ・在庫・物流などの機能を付加して欧州・シンガポール・米州の顧客に届けます。顧客と接するRtMを通じて得た市場の生きた情報は、資源投資の判断へ還元されます。肥料資源では、本格投資に先立ちシンガポールにトレーディングデスクを設け、市場理解を深めてから投資へ——この「事業機会の発掘」こそ、投資と販売を併せ持つ私たちのアイデンティティです。')
fx=L+170; fyy=by+118
b+=T(fx,fyy,'RtMの機能',None,'k')
for i,(e,j) in enumerate([('','販売・調達'),('','物流'),('','ファイナンス'),('','リスク管理'),('','脱炭素')]):
    x=fx+i*70; b+=A(x,fyy+12,f'<div class="l" style="font-size:5.8px;font-weight:600">{e}</div><div class="s">{j}</div>',66,'',f'height:34px;padding:5px 6px;border-top:1.4px solid {NV};background:{PAN}')
# bottom-right closing
b+=A(R+40,by-10,'',555-40,'',f'height:205px;background:{INK}')
b+=T(R+64,by+6,'私たちの約束',None,'k','color:#e9d6ac')
b+=T(R+64,by+22,'Supporting society<br>with the resources it needs.',440,'d','font-size:26px;color:#fff')
b+=T(R+64,by+86,'社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する。',420,'hs','color:#fff;font-size:9px')
b+=T(R+64,by+114,'需要の拡大、供給制約、地政学リスク——変化する外部環境に対し、①安定的な資源確保による安定供給と、②バリューチェーン全体の効率化による効率的な供給の両面で応えていきます。共に、持続可能で豊かな未来を。',420,'b','color:#c9ced3;font-size:6.8px')
b+=S(f'<line x1="{R+64}" y1="{by+156}" x2="{1150}" y2="{by+156}" stroke="#3b4148" stroke-width=".6"/>')
b+=svg(0,0,1190,842,'')+T(R+64,by+164,'三菱商事　金属資源グループ',None,'l','color:#fff')+T(R+64,by+175,'〒100-8086 東京都千代田区丸の内2-3-1｜www.mitsubishicorp.com',None,'s','color:#9aa1a8;font-family:IN')
b+=tile(0,712,393,96,'mr_01_01@2x.webp','50% 60%','港湾・鉄道','',2000)+tile(397,712,396,96,'r-023.png','50% 55%','海上輸送','')+tile(797,712,393,96,'r-075.png','50% 60%','操業','')
b=OUT(1010,6,'05')+b+BAND(0,690,1190,18)
pages.append(spread(b,10,11,'動画08 Integrated Value Chain。【強調】見開き全幅の表で、鉄鋼・非鉄の2段×川上→川下を整理。投資（ブロンズ）とトレーディング（ネイビー）の帯で両輪を明示。左下は投資⇄販売の好循環。','動画09 Closing。右下の濃色パネルで約束（ミッション）と外部環境への答え（安定供給・効率的な供給）、連絡先で締める。'))

links=''.join(f'<link rel="stylesheet" href="f/nsjp/package/{w}.css">' for w in (400,500,700))
open('daiwari_v14.html','w').write('<!doctype html><meta charset=utf-8>'+links+'<style>'+CSS2+'</style>'+''.join(pages))
