# 台割 案③ v3 — エディトリアル・グリッド＋カラーのヘアライン（表紙案①のモチーフ）
exec(open('v12_head.py').read())
import numpy as np, random
from global_land_mask import globe
CSS2+=f""".q{{font-family:'Noto Sans JP';font-weight:400;font-size:15px;line-height:1.65;letter-spacing:.6px;color:{INK}}}
.v{{writing-mode:vertical-rl;font-family:IN;font-weight:600;font-size:6px;letter-spacing:2.4px;color:{G2};text-transform:uppercase}}
.idx{{font-family:IT;font-weight:300;font-size:120px;letter-spacing:-.05em;line-height:.8;color:{G4}}}
"""
def mixc(a,b,t):
    a=[int(a[i:i+2],16) for i in (1,3,5)]; b=[int(b[i:i+2],16) for i in (1,3,5)]
    return '#%02x%02x%02x'%tuple(int(a[k]+(b[k]-a[k])*t) for k in range(3))
def hcol(t,shade):
    base=mixc(BR,NV,t); return mixc(base,'#ffffff',.08+.62*shade)
# ---- colored hairline map (cover option ① motif) ----
def hmap(x0,y0,w,lon0,lon1,lat0,lat1,step=1.5,sw=.6,seed=3,t0=0,t1=1):
    rnd=random.Random(seed); sc=w/(lon1-lon0); h=(lat1-lat0)*sc
    lats=np.linspace(lat1,lat0,int(h*2.2)); ys=(lat1-lats)*sc; out=''
    x=.4
    while x<w:
        lon=((lon0+x/sc)+180)%360-180
        m=globe.is_land(lats,np.full_like(lats,lon)); t=x/w
        shade=.5+.3*math.cos(2*math.pi*(t*1.7-.1))+.15*math.cos(2*math.pi*(t*4.1+.3))+rnd.uniform(-.06,.06)
        col=hcol(t0+(t1-t0)*t,max(0,min(1,shade)))
        d=''; i=0; n=len(m)
        while i<n:
            if m[i]:
                j=i
                while j+1<n and m[j+1]: j+=1
                if ys[j]-ys[i]>.3: d+=f'M{x0+x:.1f},{y0+ys[i]:.1f}V{y0+ys[j]:.1f}'
                i=j+1
            else: i+=1
        if d: out+=f'<path d="{d}" stroke="{col}" stroke-width="{sw}" fill="none"/>'
        x+=step
    P=lambda lon,lat:(x0+((lon-lon0)%360)*sc, y0+(lat1-lat)*sc)
    return out,h,P
def riser(x,yb,yt,col,r=2.2,sw=.6):
    return f'<line x1="{x:.1f}" y1="{yb:.1f}" x2="{x:.1f}" y2="{yt:.1f}" stroke="{col}" stroke-width="{sw}"/><circle cx="{x:.1f}" cy="{yb:.1f}" r="{r}" fill="{col}"/>'
def hband(x0,x1,ybase,hmax,up=True,seed=5,step=1.6,sw=.55,minh=.15):
    rnd=random.Random(seed); o=''; x=x0
    while x<x1:
        t=(x-x0)/(x1-x0); hh=hmax*(minh+(1-minh)*(.55+.45*math.sin(t*9+rnd.random()))*rnd.random())
        col=hcol(t,.25+.5*rnd.random())
        o+=f'<line x1="{x:.1f}" y1="{ybase}" x2="{x:.1f}" y2="{ybase-hh if up else ybase+hh:.1f}" stroke="{col}" stroke-width="{sw}"/>'
        x+=step
    return o
def kick(x,y,k,kj): return T(x,y,k,None,'k')+T(x,y+11,kj,None,'kj')
def redrule(x,y): return A(x,y,'',22,'',f'border-top:1.4px solid {RED}')
pages=[]

# ================= P02-03 OPENING =================
b=kick(L,44,'Introduction','導入｜社会と金属')
b+=T(L,70,'Metals shape<br>the way we live.',560,'d','font-size:56px')
b+=redrule(L,196)+T(L,206,'暮らしのすべてに、金属がある。',None,'h','font-size:14px')
b+=para(L,232,250,'ビル、鉄道、自動車、スマートフォン、送電網、再生可能エネルギー——私たちの豊かな暮らしは、鉄や銅をはじめとする金属に支えられています。人口の増加と新興国の発展、社会の電化によって、金属の需要はこれからも拡大を続けます。')
b+=para(L+268,232,250,'一方で、良質な資源の開発は年々難しくなり、供給の制約や地政学的なリスクが常態化しつつあります。社会が必要とする金属を、これからも持続可能な形で届け続けること——それが、私たち金属資源グループの使命です。')
# core message (right)
b+=kick(R,44,'Core message','コアメッセージ')
b+=T(R,70,'Strength to Hold.<br>Power to Connect.',W,'dl','font-size:44px')
b+=T(R,170,'持つ力と、つなぐ力。',None,'h','font-size:13px')
b+=para(R,196,W,'資源は、そこに「ある」だけでは、まだ価値ではありません。誰かが見出し、育て、必要とする場所へ届けて、はじめて力になる。私たちは、世界有数の資産に関わり、投資とトレーディングの両輪で川上から川下までをつなぎます。フェアな立場だからこそ、埋められる隙間がある。多様なパートナーと使い手の間に立ち、その時々の最適解を導く。世界に眠る価値を、社会の力へ。','font-size:7.6px')
# film strip with hairline risers
strip=[('r-022.png','50% 60%','Cities','Fe · Cu · Al',200),('x_vc_ev.jpg','50% 55%','Mobility','Fe · Cu · Li · Ni',160),(None,'','Railways','Fe · Cu',130),('x_case_pylon.jpg','50% 40%','Power grids','Cu · Al',150),('x_vc_wind.jpg','50% 30%','Renewables','Cu · Fe',150),(None,'','Devices','Cu · Li · Ni',130),('r-023.png','50% 60%','Trade','Fe · Cu',226)]
sy,sh=420,190; x=0; o=''
for i,(f,pos,cap,met,w_) in enumerate(strip):
    b+=(tile(x,sy,w_,sh,f,pos,cap,'') if f else ptile(x,sy,w_,sh,cap,'','写真（ストック）'))
    cx=x+w_*.5; yt=[318,346,330,356,322,340,312][i]; col=hcol(cx/1190,.15)
    o+=riser(cx,sy-1,yt,col)
    b+=T(cx-30,yt-14,met,60,'l',f'text-align:center;font-size:6.2px;color:{col};font-weight:600')
    x+=w_+4
b+=S(o)
# bottom: demand vs supply + 3 forces / contents
by=652
b+=kick(L,by,'A world of rising demand','需要の拡大と、深まる供給の制約')
cx0,cy0,cw,ch=L,by+30,250,110
o=''
dem=[(cx0+i*cw/10, cy0+ch-10-(i**1.45)*3.0) for i in range(11)]
sup=[(cx0+i*cw/10, cy0+ch-10-min(i,6)*5.5-max(0,i-6)*1.5) for i in range(11)]
o+='<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in dem)+' L'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in reversed(sup))+f'Z" fill="{BRL}" opacity=".3"/>'
o+='<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in dem)+f'" fill="none" stroke="{INK}" stroke-width="1.6"/>'
o+='<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in sup)+f'" fill="none" stroke="{NV}" stroke-width="1.6" stroke-dasharray="3 2"/>'
o+=f'<line x1="{cx0}" y1="{cy0+ch-8}" x2="{cx0+cw}" y2="{cy0+ch-8}" stroke="{G3}" stroke-width=".6"/>'
b+=S(o)+T(cx0+cw-50,cy0+4,'Demand',None,'l')+T(cx0+cw-50,cy0+ch-44,'Supply',None,'l','color:'+NV)+T(cx0+cw-102,cy0+ch-62,'GAP',None,'k')+T(cx0,cy0+ch-2,'概念図（数値なし）',None,'s','font-size:5.4px')
for i,(e,j,d_) in enumerate([('Demand shift','需要の拡大','人口増・電化による産業構造の転換'),('Supply constraints','供給制約','良質な資源の開発がより困難に'),('Geopolitics','地政学リスク','サプライチェーン確保の重要性が増大')]):
    y=by+30+i*38; b+=rule(L+272,y,243,INK,.8)+T(L+272,y+6,e,None,'l','font-weight:600;font-size:7.2px')+T(L+370,y+6,j,None,'hs','font-size:7.6px')+T(L+370,y+19,d_,None,'s')
b+=kick(R,by,'Contents','目次')
toc=[('01','Who We Are','三菱商事 金属資源グループとは','04'),('02','Our Strengths','一級資産と歩み','05'),('03','Coal &amp; Copper','原料炭事業・銅事業','06'),('04','Footprint &amp; Technology','事業領域と新技術','08'),('05','Partner of Choice','パートナーシップと販売網','09'),('06','Integrated Value Chain','川上から川下まで／私たちの約束','10')]
for i,(n,e,j,p) in enumerate(toc):
    x=R+(i//3)*262; y=by+30+(i%3)*38
    b+=rule(x,y,243,INK,.8)+T(x,y+6,n,None,'nb','font-size:15px;color:'+BR)+T(x+30,y+6,e,None,'l','font-weight:600;font-size:7.4px')+T(x+30,y+19,j,None,'s')+T(x+222,y+7,'P.'+p,None,'fo','font-size:5.4px')
pages.append(spread(b,2,3,'動画01 OPENING。暮らしの場面の写真を1本のフィルムストリップに。各写真から金属のヘアライン（表紙案①のモチーフ）が立ち上がり、使われている金属を示す。','コアメッセージ全文と目次。下段は外部環境（需要の拡大・供給制約・地政学）を概念図と3項目で——冒頭で「なぜ私たちが必要か」を示す。'))

# ================= P04-05 WHO WE ARE / STRENGTHS =================
b=T(L-4,30,'01',None,'idx')
b+=kick(L,118,'01 · Who we are','第1章　我々は何者か')
b+=T(L,144,'Who we are.',W,'d','font-size:48px')+redrule(L,206)+T(L,216,'三菱商事 金属資源グループとは',None,'h')
b+=para(L,242,250,'三菱商事は、三綱領（所期奉公・処事光明・立業貿易）を企業理念に、経済価値・環境価値・社会価値の同時実現を目指す総合商社です。エネルギー、素材、金属資源、社会インフラ、モビリティ、食品産業、S.L.C.の7グループで、世界の産業と暮らしを支えています。')
b+=para(L+268,242,247,'そのなかで金属資源グループは、社会に不可欠な金属資源を世界から確保し、安定的に届ける役割を担っています。資源投資とトレーディングを両輪に、原料炭と銅を中核として、全社としてコミットする事業領域です。')
# mission pull quote
b+=A(L,338,'',3,'',f'height:66px;background:{BR}')
b+=T(L+16,334,'GROUP MISSION',None,'k')+T(L+16,348,'社会が必要とする良質な金属資源を、持続可能な形で<br>安定供給することで、より良い社会の実現に寄与する',W-20,'q')
b+=T(L+16,394,'To contribute to a better society by providing a stable supply of high-quality mineral resources that society needs, in a sustainable way.',W-20,'s','font-family:IN')
# organisation — line diagram, no boxes
oy=440
b+=kick(L,oy,'Organization','投資を担う2本部と、トレーディングを担う1本部')
o=f'<line x1="{L+257}" y1="{oy+44}" x2="{L+257}" y2="{oy+56}" stroke="{INK}" stroke-width=".7"/><line x1="{L}" y1="{oy+56}" x2="{L+W}" y2="{oy+56}" stroke="{INK}" stroke-width=".7"/>'
b+=T(L+207,oy+30,'Group CEO',100,'l','text-align:center;font-weight:600')
divs=[('INVESTMENT','鉄鋼原料本部','Steelmaking Raw Materials','原料炭・鉄鉱石','MDP（原料炭）',BR),('INVESTMENT','クリティカルミネラル本部','Critical Minerals','銅・ニッケル・リチウム・アルミ ほか','MCI（南米の銅・鉄鉱石）・MCIP（ペルーの銅）',BR),('TRADING','金属資源トレーディング本部','Mineral Resources Trading','RtM（Resource to Market）','Triland Metals（LME・CMEのブローカー／ヘッジ）',NV)]
for i,(k_,j,e,c,a,col) in enumerate(divs):
    x=L+i*175
    b+=A(x,oy+66,'',165,'',f'border-top:2.4px solid {col}')
    b+=T(x,oy+74,k_,None,'k','color:'+col)+T(x,oy+86,j,165,'h','font-size:10px')+T(x,oy+102,e,165,'s','font-family:IN')+T(x,oy+118,c,165,'hs','font-size:7.4px')+T(x,oy+132,a,165,'s')
b+=S(o)
# three principles — vertical type rhythm
py=596
b+=kick(L,py,'Three corporate principles','三綱領')
for i,(j,e,d_) in enumerate([('所期奉公','Corporate Responsibility to Society','事業を通じ、物心ともに豊かな社会の実現に努める'),('処事光明','Integrity and Fairness','公明正大で品格のある行動を旨とする'),('立業貿易','Global Understanding through Business','全世界的、宇宙的視野に立脚した事業展開を図る')]):
    x=L+i*175
    if i: b+=vrule(x-10,py+28,80,G3)
    b+=T(x,py+28,j,None,'h','font-size:18px;letter-spacing:2px')+T(x,py+56,e,160,'l','color:'+BR)+T(x,py+70,d_,158,'s')
# right page: assets with hairline map + risers
b+=T(R-4,30,'02',None,'idx')
b+=kick(R,118,'02 · Our strengths','第2章　独自価値｜資産の強み')
b+=T(R,144,'Tier-1 assets<br>at the source.',W,'d','font-size:44px')+redrule(R,246)+T(R,256,'バリューチェーンの起点で、一級資産を保有する',None,'h')
b+=para(R,280,250,'資源事業は規模の経済が働くビジネスです。大規模な鉱山ほどコスト競争力が高い。私たちは規模で世界上位に入る優良鉱山に早くから参画し、いまでは資金があっても手に入らない資産のポートフォリオを築いてきました。')
b+=para(R+268,282,247,'その中核が、原料炭と銅です。原料炭は寡占度の高い市場で圧倒的なプレゼンスを、銅は寡占化が進まない市場で、協業可能なパートナーとして世界最大級のポジションを持ちます。')
hm,hh,P=hmap(600,392,590,-180,180,-56,78,step=1.35,sw=.6)
o=hm
sites=[((148.3,-22.3),'Metallurgical Coal','BMA · Australia',380,BR),((-110.9,31.9),'Copper','Copper World · USA',380,BR)]
for (lo,la),e,j,yt,col in sites:
    x,y=P(lo,la); o+=riser(x,y,yt,INK,2.6,.7)
    lab=f'<b style="font-family:IT;font-weight:600;font-size:8px;color:{INK}">{e}</b> <span class="s">{j}</span>'
    b+=(T(x-154,yt-5,lab,150,'','text-align:right') if lo>100 else T(x+4,yt-5,lab,150,''))
for lo,la in [(-69.07,-24.27),(-70.5,-31.7),(-70.3,-33.15),(-77.05,-9.53),(-70.6,-17.1)]:
    x,y=P(lo,la); o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="{INK}" stroke="#fff" stroke-width=".6"/>'
x,y=P(-50,-22); b+=T(x,y-6,'<b style="font-family:IT;font-weight:600;font-size:8px">Copper</b> <span class="s">Chile · Peru<br>Escondida・Quellaveco ほか</span>',None,'','background:rgba(255,255,255,.92);padding:2px 4px')
b+=S(o)
ky=392+hh+10
for i,(n,u,t) in enumerate([('5 / 5','Top-15 mines','銅の主要5鉱山すべてが規模で世界Top15'),('~50%','Premium coking coal','一級強粘炭の世界供給に占めるBMAのシェア'),('No.20','Equity production','銅の持分生産量で世界20位・日本最大')]):
    x=R+i*176; b+=T(x,ky,n,None,'nb','font-size:30px')+T(x,ky+34,u.upper(),None,'l','font-size:5.8px;letter-spacing:1.4px;color:'+BR)+T(x,ky+45,t,160,'s')
# journey across bottom of spread with hairline band
jy=742
b+=S(hband(0,1190,jy,18,True,seed=11))+A(0,jy,'',1190,'',f'border-top:.8px solid {INK}')
eras=[('1980s–90s','トレーディングで参入','日本が世界最大の消費国だった時代。資源を日本へ運ぶ役割から始まり、少数株主として出資。'),('1990s','投資モデルへ','口銭モデルから投資モデルへ。JV運営の知見を蓄積し、事業経営へと舵を切る。'),('2000s','BHPと50:50のBMA','2001年にBMAを組成。中国の成長を捉え、一級原料炭資産の経営に参画。'),('2010s','銅の権益を拡大','「原料炭だけでよいのか」という問いから銅へ。Anglo Americanと組み大型化。'),('2020s','グローバルトレーダーへ','各地のマーケティングをRtMとしてシンガポールに集約。')]
b+=T(R,jy-44,'OUR JOURNEY｜FORESIGHT',None,'k')+T(R+150,jy-44,'先見性——時代を先読みし、事業モデルを変え続けてきた',None,'kj')
for i,(yr,t,d_) in enumerate(eras):
    x=L+i*226
    b+=T(x,jy+6,yr,None,'nb','font-size:13px;color:'+(BR if i in (2,3) else INK))+T(x+(len(yr)*6.6+8),jy+8,t,150,'hs','font-size:7.6px')+T(x,jy+24,d_,212,'s','line-height:1.55')
pages.append(spread(b,4,5,'動画02 Who we are。大きな章番号と2段組の本文、ミッションを引用として大きく。組織は箱を使わず色の罫で投資（ブロンズ）／トレーディング（ネイビー）を区別。','動画03 Our Strengths。カラーのヘアライン世界地図（表紙案①のモチーフ）から一級資産の位置が立ち上がる。最下段の「歩み」はヘアラインの帯で見開きをつなぐ。'))

# ================= P06-07 COAL & COPPER =================
b=tile(0,0,595,344,'r-047.png','60% 40%')+tile(595,0,595,344,'mr_02_01@2x.webp','50% 50%',mx=2000)
b+=A(0,0,'',1190,'','height:344px;background:linear-gradient(0deg,rgba(10,14,18,.72) 0%,rgba(10,14,18,.12) 48%,rgba(10,14,18,0) 70%,rgba(10,14,18,.28) 100%)')
b+=S(hband(0,1190,344,16,False,seed=21,minh=.2))
b+=T(L,40,'03 · Metallurgical coal',None,'k','color:#e9d6ac')+T(R,40,'03 · Copper',None,'k','color:#e9d6ac')
b+=T(L,250,'~50%',None,'nb','font-size:72px;color:#fff')+T(L+200,266,'一級強粘炭の世界供給に<br>占めるBMAのシェア',None,'hs','color:#fff;font-size:9px')
b+=T(R,250,'No.1',None,'nb','font-size:72px;color:#fff')+T(R+168,266,'自社操業を伴わない参画者として<br>世界最大の銅生産者',None,'hs','color:#fff;font-size:9px')
# coal
b+=T(L,378,'World-class<br>metallurgical coal.',W,'d','font-size:30px')+redrule(L,446)+T(L,456,'原料炭事業｜鉄の主原料“産業のコメ”を、世界最高品位で',None,'h')
b+=para(L,482,250,'BHPと50:50の合弁であるBMA（BHP Mitsubishi Alliance）を通じ、豪州クイーンズランド州ボーエン・ベースンで世界最高品位の原料炭事業に参画しています。炭鉱に加えて港湾と鉄道までを保有し、山から港まで全体最適で運営。保有鉱山を高品位のものに集約し、高品位原料の供給を通じて鉄鋼業の脱炭素にも貢献しています。')
lx=L+272
o=f'<line x1="{lx+8}" y1="490" x2="{lx+8}" y2="600" stroke="{BRL}" stroke-width=".8"/>'
for i,t in enumerate(['世界最高品位の原料炭を保有','原料炭は鉄の主原料＝“産業のコメ”','鉄は今後も底堅く必要とされる','ゆえに、社会に不可欠']):
    y=482+i*36; o+=f'<circle cx="{lx+8}" cy="{y+9}" r="{3.4 if i<3 else 4.6}" fill="{BR if i==3 else "#fff"}" stroke="{BR}" stroke-width="1.2"/>'
    b+=T(lx+22,y,f'0{i+1}',None,'nb','font-size:10px;color:'+BR)+T(lx+44,y+1,t,200,'hs','font-size:8.4px'+(';font-weight:700' if i==3 else ''))
b+=S(o)
fy=640
b+=T(L,fy,'OWNERSHIP',None,'k')
o=f'<path d="M{L+70},{fy+30} H{L+96} M{L+136},{fy+30} H{L+156} V{fy+46} H{L+176} M{L+136},{fy+62} H{L+156} V{fy+46}" fill="none" stroke="{INK}" stroke-width=".7"/>'
b+=T(L,fy+24,'三菱商事',70,'hs','font-size:8px')+T(L+100,fy+24,'MDP',40,'l','font-weight:600')+T(L+100,fy+56,'BHP',40,'l','font-weight:600')+T(L+180,fy+38,'BMA',None,'nb','font-size:16px;color:'+BR)
b+=T(L+72,fy+18,'100%',None,'s','font-size:5.4px')+T(L+138,fy+18,'50%',None,'s','font-size:5.4px')+T(L+138,fy+66,'50%',None,'s','font-size:5.4px')
b+=S(o)
for i,(k_,v) in enumerate([('Since','1968年 MDP設立／2001年 BMA組成'),('Location','豪州クイーンズランド州 Bowen Basin'),('Assets','炭鉱5（露天掘4・坑内掘1）・港湾・鉄道'),('Mine life','60年以上'),('Seaborne','原料炭の海上輸出市場シェア 約20%')]):
    y=fy+i*15; b+=rule(L+250,y,265)+T(L+250,y+4,k_,None,'l','color:'+G2)+T(L+305,y+3,v,None,'hs','font-size:7px')
# copper
b+=T(R,378,'The world\'s largest<br>non-operating copper producer.',W+20,'d','font-size:30px')+redrule(R,446)+T(R,456,'銅事業｜自社操業を伴わずに、世界最大級の銅ポジションを築く',None,'h')
b+=para(R,482,250,'銅は原料炭に比べてプレイヤーが多く、寡占化が進んでいない市場です。私たちは規模で世界上位15に入る優良鉱山に複数参画し、日本最大・世界第20位の持分生産量を有します。特定の1社に偏らず主要メジャーのほぼすべてと協業し、販売を通じた幅広い関係から、新しい案件で“声がかかる存在”であり続けています。')
tx,ty=R+272,482
b+=T(tx,ty-2,'EARLY MOVER',None,'k')+T(tx+72,ty-2,'主要鉱山への参画年',None,'kj')
mines=[(1988,'Escondida','Chile'),(1997,'Los Pelambres','Chile'),(1999,'Antamina','Peru'),(2011,'Anglo American Sur','Chile'),(2011,'Quellaveco','Peru'),(2023,'Marimaca','Chile・開発中'),(2025,'Copper World','USA・開発中')]
X=lambda yr: tx+(yr-1985)/42*243
o=f'<line x1="{tx}" y1="{ty+30}" x2="{tx+243}" y2="{ty+30}" stroke="{INK}" stroke-width=".7"/>'
for yr in (1990,2000,2010,2020):
    o+=f'<line x1="{X(yr):.1f}" y1="{ty+27}" x2="{X(yr):.1f}" y2="{ty+33}" stroke="{INK}" stroke-width=".6"/>'; b+=T(X(yr)-10,ty+16,str(yr),None,'s','font-family:IN;font-size:5.6px')
for i,(yr,n,c) in enumerate(mines):
    x=X(yr); y=ty+42+i*13
    o+=riser(x,y+4,ty+30,BR if '開発' not in c else NVL,2.4,.6)
    lab=f'<b style="font-family:IN;font-weight:600">{n}</b> <span class="s">{c}・{yr}</span>'
    b+=(T(x+6,y,lab,200,'l','font-size:6.4px') if yr<2015 else T(x-206,y,lab,200,'l','font-size:6.4px;text-align:right'))
b+=S(o)
ry=fy-6
b+=T(R,ry,'COPPER PRODUCTION 2025',None,'k')+T(R+150,ry,'会社別 世界銅生産量（kt）',None,'kj')
rk=[('BHP',1501),('Codelco',1432),('Freeport',1099),('Southern Copper',948),('Zijin Mining',850),('Glencore',812),('Rio Tinto',740),('China Moly',558),('KGHM',538),('Anglo American',496),('Mitsubishi Corp.',326)]
o=''
for i,(n,v) in enumerate(rk):
    y=ry+16+i*9.6+(4 if i==10 else 0); me=(i==10); w_=v/1501*250
    o+=f'<rect x="{R+92}" y="{y}" width="{w_:.1f}" height="6" rx="1" fill="{BR if me else G3}"/>'
    b+=T(R,y-1.5,('#20 ' if me else f'#{i+1} ')+n,90,'l',f'font-size:5.6px;text-align:right;padding-right:6px;{"color:"+BR+";font-weight:600" if me else "color:"+G1}')+T(R+96+w_,y-1.5,f'{v:,}',None,'l','font-size:5.4px;color:'+(BR if me else G2))
b+=S(o)
b+=T(R+372,ry+60,'上位には協業が難しい国有・政府系も含まれる。協業可能で、オペレーターシップを求めないパートナーとしては最大規模。',143,'s')
mb=766
b+=T(L,mb,'MARKET STRUCTURE｜上位5社のシェア',None,'k')
for x0,lab,v,t in [(L,'Metallurgical coal',80,'寡占度が高く、供給は漸減'),(R,'Copper',25,'寡占化が進まず、再編の機運')]:
    b+=T(x0,mb+16,lab,None,'l','font-size:7px')+A(x0+100,mb+17,'',330,'',f'height:6px;background:{G4}')+A(x0+100,mb+17,'',330*v/100,'',f'height:6px;background:{INK}')+T(x0+436,mb+12,f'{v}%',None,'nb','font-size:13px')+T(x0+100,mb+27,t,None,'s')
pages.append(spread(b,6,7,'動画04 Coking Coal。【強調】写真の下端にヘアラインの縁取り。品位→鉄→需要→社会の4段ロジックは縦のライン、出資構成は罫線のみで簡潔に。','動画05 Copper。【強調】参画年はヘアラインのライザーで「先行して確保」を表現。ランキングは当社のみ色。最下段の市場構造バーで原料炭と比較。'))

# ================= P08-09 FOOTPRINT & TECH / PARTNER OF CHOICE + NETWORK =================
b=T(L-4,30,'04',None,'idx')
b+=kick(L,118,'04 · Footprint &amp; technology','第2章　独自価値｜事業・プロジェクト一覧')
b+=T(L,144,'Resources become<br>value when delivered.',W,'d','font-size:34px')+redrule(L,222)+T(L,232,'鉄鉱石から電池資源・肥料・アルミまで、世界に広がる事業領域',None,'h')
b+=para(L,258,W,'資源は、ただ存在するだけでは社会の価値になりません。良質な資源を安定的に確保し、高品質な金属へと精錬し、必要とする産業へ届けてはじめて価値になります。原料炭と銅に加え、鉄鉱石、電池資源、アルミ、肥料へと事業領域を広げ、世界各地にトレーディング拠点と人材を配しています。')
hm,hh,P=hmap(L-6,312,W+12,-170,190,-56,76,step=1.25,sw=.55,seed=7)
o=hm
PRJ=[(-66.9,52.9),(-71.2,-28.5),(-70.6,-33.4),(148.3,-22.3),(-69.07,-24.27),(-70.5,-31.7),(-70.3,-33.15),(-77.05,-9.53),(-70.6,-17.1)]
DEV=[(-70.3,-22.9),(-110.9,31.9),(-128.9,58.5),(121.4,-30.7),(-94.0,51.6),(141.7,-13.3),(25.7,64.2),(-0.6,54.4)]
OFF=[(139.7,35.7),(103.8,1.3),(77.2,28.6),(-0.1,51.5),(-77.0,40.4),(55.3,25.2),(106.8,-6.2),(100.5,13.7),(-70.65,-33.45),(28.0,-26.2),(-58.4,-34.6),(-46.6,-23.5),(153.0,-27.5),(-77.0,-12.0),(-123.1,49.3),(121.5,31.2)]
for lo,la in OFF: x,y=P(lo,la); o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.4" fill="{NV}" stroke="#fff" stroke-width=".6"/>'
for lo,la in DEV: x,y=P(lo,la); o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="#fff" stroke="{BR}" stroke-width="1"/>'
for lo,la in PRJ: x,y=P(lo,la); o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.8" fill="{BR}" stroke="#fff" stroke-width=".6"/>'
b+=S(o)
ly=312+hh+4
b+=S(f'<circle cx="{L+3}" cy="{ly+4}" r="2.8" fill="{BR}"/><circle cx="{L+83}" cy="{ly+4}" r="2.6" fill="#fff" stroke="{BR}"/><circle cx="{L+203}" cy="{ly+4}" r="2.4" fill="{NV}"/>')
b+=T(L+9,ly,'事業・資産',None,'s')+T(L+89,ly,'開発・探鉱プロジェクト',None,'s')+T(L+209,ly,'トレーディング拠点・金属資源の駐在（名称は記載しない）',None,'s')
gy=ly+22
port=[('Iron Ore','鉄鉱石','IOC（カナダ）・CMP（チリ）'),('Coking Coal','原料炭','BMA（豪州）'),('Copper','銅','Escondida・Los Pelambres・AA Sur・Antamina・Quellaveco ほか'),('Nickel','ニッケル','Turnagain（カナダ）・Kalgoorlie（豪州）'),('Lithium','リチウム','PAK Lithium（カナダ）'),('Bauxite · Aluminium','ボーキサイト・低炭素アルミ','Aurukun（豪州）・Arctial（北欧）'),('Fertilizer','肥料資源','Woodsmith（英国）'),('Trading','トレーディング','RtM International・Japan・Bharat・Europe・Americas')]
for i,(e,j,p_) in enumerate(port):
    x=L+(i%4)*130; y=gy+(i//4)*46
    b+=A(x,y,'',122,'',f'border-top:1.2px solid {hcol(i/7,.0)}')+T(x,y+5,e,None,'l','font-weight:600;font-size:6.6px')+T(x+0,y+15,j,None,'hs','font-size:7px')+T(x,y+26,p_,120,'s','font-size:5.6px;line-height:1.45')
# new tech
cy=gy+108
b+=T(L,cy,'NEW TECHNOLOGY',None,'k')+T(L+100,cy,'加工技術・回収・リサイクル——業界のボトルネックに挑む技術へ投資する（CVC）',None,'kj')
st=[('Mine','採掘','Cu ~1%'),('Concentrate','選鉱・浸出','Cu 20–30%'),('Cathode','製錬・精製','Cu 99.99%'),('End use','最終製品','電化・インフラ'),('Recycle','回収','再び供給へ')]
o=f'<line x1="{L}" y1="{cy+42}" x2="{L+W}" y2="{cy+42}" stroke="{INK}" stroke-width=".7"/>'
for i,(e,j,g_) in enumerate(st):
    x=L+i*106; o+=f'<circle cx="{x+4}" cy="{cy+42}" r="3" fill="{INK}"/>'
    b+=T(x,cy+16,e,None,'l','font-weight:600')+T(x,cy+26,g_,None,'nb','font-size:8px;color:'+BR)+T(x,cy+48,j,None,'s')
tech=[(1,'CiDRA','STARTUP','浮遊選鉱の高度化で回収率・処理能力を向上'),(1.5,'Jetti','STARTUP','新しい触媒で硫化鉱からリーチング'),(2.5,'Triland Metals','100%子会社','LME・CMEのブローカー・ヘッジ'),(4,'DESCycle','RECYCLING','電子スクラップから銅・貴金属を回収')]
for k,(si,n,t_,d_) in enumerate(tech):
    x=L+k*130; sx_=L+si*106+4
    o+=f'<path d="M{sx_:.1f},{cy+42} V{cy+66} H{x+2} V{cy+74}" fill="none" stroke="{BR}" stroke-width=".6"/>'
    b+=T(x,cy+76,t_,None,'k','font-size:5.4px')+T(x,cy+87,n,None,'l','font-weight:600;font-size:8.4px')+T(x,cy+99,d_,122,'s')
b+=S(o)
# right page: partner of choice
b+=tile(R+260,0,300,300,'r-084.png','55% 35%')
b+=kick(R,118,'05 · Partner of choice','第3章　選ばれ続ける理由')
b+=T(R,144,'Partner<br>of choice.',240,'d','font-size:44px')+redrule(R,246)+T(R,256,'資源業界に不可欠な存在として',None,'h')
b+=para(R,280,240,'資源業界では、良い案件があっても単独では規模が大きすぎることが少なくありません。そのとき「三菱に声をかけよう」と思われる存在であること。業界最大手とJVを組み、単なる共同出資者に留まらず、人材派遣・ガバナンス参画・総合力で事業価値の最大化に貢献してきました。')
b+=T(R+260,304,'BHP　　Rio Tinto　　Anglo American',300,'nb','font-size:15px')+T(R+260,324,'JOINT VENTURES WITH INDUSTRY LEADERS｜業界最大手とのJV実績（他社ロゴは使用しない）',300,'s','font-size:5.6px')
py=384
four=[('Cultural affinity','資源メジャーとの企業文化的親和性'),('JV management','資源投資経験に裏打ちされたJV経営力'),('Financial strength','事業ポートフォリオを活かした健全な財務基盤'),('Deep insight','マクロ環境とバリューチェーンへの深い知見')]
for i,(e,j) in enumerate(four):
    x=R+i*130; b+=T(x,py,f'0{i+1}',None,'nb','font-size:22px;color:'+BR)+T(x,py+26,e.upper(),122,'l','font-size:5.6px;letter-spacing:1.2px;color:'+G2)+T(x,py+36,j,120,'hs','font-size:7.6px')
vy=py+80
b+=T(R,vy,'WHY PARTNERS VALUE US',None,'k')+T(R+140,vy,'パートナーに評価される理由',None,'kj')
for i,(j,d_) in enumerate([('中長期的な視座','資源事業は長期にわたる。短期的リターンを求める投資家とは一線を画す。'),('リスクシェアリング','リスクの高い案件ほど資金面の分担を担保。財務貢献に留まらない。'),('総合力','幅広い産業接点を通じ、多様なバリューチェーンに知見を提供する。')]):
    x=R+i*175; b+=A(x,vy+18,'',160,'',f'border-top:1.2px solid {hcol(i/2,0)}')+T(x,vy+24,j,None,'hs','font-size:8.6px;font-weight:700')+T(x,vy+40,d_,160,'s')
# trading network on hairline map (navy side)
ny=vy+82
b+=T(R,ny,'GLOBAL TRADING NETWORK',None,'k')+T(R+150,ny,'RtM＝Resource to Market｜シンガポールに集約した10拠点',None,'kj')
hm,hh2,P2=hmap(R-6,ny+14,340,-170,190,-56,76,step=1.3,sw=.5,seed=9,t0=.55,t1=1)
o=hm; sx,sy=P2(103.8,1.3)
offs=[(139.7,35.7),(77.2,28.6),(121.5,31.2),(-77.0,40.4),(-0.1,51.5),(55.3,25.2),(106.8,-6.2),(100.5,13.7),(-70.65,-33.45)]
for lo,la in offs:
    x,y=P2(lo,la); mxp=(sx+x)/2; myp=min(sy,y)-abs(x-sx)*.18-6
    o+=f'<path d="M{sx:.1f},{sy:.1f} Q{mxp:.1f},{myp:.1f} {x:.1f},{y:.1f}" fill="none" stroke="{BR}" stroke-width=".6"/><circle cx="{x:.1f}" cy="{y:.1f}" r="2.2" fill="{BR}"/>'
o+=f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="3.4" fill="{RED}"/>'
b+=S(o)
nx=R+352
for i,(n,u,j) in enumerate([('15','industries','業界'),('50','countries','カ国'),('~1,000','customers','社の販売先')]):
    y=ny+16+i*38; b+=rule(nx,y,163,INK,.8)+T(nx,y+5,n,None,'nb','font-size:22px')+T(nx+90,y+12,f'{u.upper()}<br>{j}',None,'l','font-size:5.6px;letter-spacing:1px;color:'+G2)
b+=T(R,ny+14+hh2+4,'Singapore・Japan・India・China・USA・UK・UAE・Indonesia・Thailand・Chile',340,'s','font-family:IN')
pages.append(spread(b,8,9,'動画06 From Resources to Value。ヘアラインの世界地図に事業（金）・開発（白抜き）・拠点と駐在（紺）を重ね、商品別の案件一覧と新技術（CVC）を続ける。開いたまま使える“フットプリント”ページ。','動画07 Global Partnerships。円形でない写真の裁ち落としとJV実績、4つの強み、評価される理由。下段はヘアライン地図で販売網（シンガポール発の金の線）。'))

# ================= P10-11 VALUE CHAIN + CLOSING =================
b=T(L,40,'06 · Integrated value chain',None,'k')+T(L,51,'第2章　独自価値｜バリューチェーン全体像とトレーディング',None,'kj')
b+=T(L,70,'From mine to market —<br>one integrated chain.',700,'d','font-size:44px')
b+=redrule(L,170)+T(L,180,'投資と販売の両輪で、川上から川下までをつなぐ。採掘・製造・販売をつなぐトレーディング力こそが、総合商社の強み。',700,'h')
b+=para(R+150,74,365,'資源を保有するだけでは、社会に届けることはできません。私たちは川上の鉱山から、製鉄・製錬、そして最終製品の需要家までのバリューチェーン全体に関わり、その間をトレーディングでつないでいます。だからこそ、需給や役割の間にある課題を見極め、資源の価値を最も生かすかたちへと導くことができます。')
cols=[('UPSTREAM','川上','資源開発・保有'),('TRADING','中間流通','トレーディング（RtM）'),('MIDSTREAM','川中','製鉄・製錬'),('TRADING','中間流通','トレーディング（RtM）'),('DOWNSTREAM','川下','最終製品・需要家')]
cx=[L,L+226,L+442,L+668,L+884]; cw=[206,196,206,196,226]
hy=226
b+=S(hband(L,1190-L,hy-4,14,True,seed=31,step=1.4))
for i,(e,j,d_) in enumerate(cols):
    tr=i in (1,3); col=NV if tr else BR
    b+=A(cx[i],hy,'',cw[i],'',f'border-top:2.4px solid {col}')+T(cx[i],hy+8,e,None,'k','color:'+col)+T(cx[i],hy+20,f'{j}｜{d_}',None,'h','font-size:9.4px')
rows=[('STEEL｜鉄鋼',['原料炭・鉄鉱石','BMA・IOC ほか当社資産／鉱山会社'],['原料炭・鉄鉱石','RtMが供給'],['製鉄会社','鋼材を製造'],['鋼材','鋼材販売はメタルワン（別グループ）'],['建材・自動車用鋼板','インフラ・モビリティ']),
      ('NON-FERROUS｜非鉄',['銅鉱石・ボーキサイト','Escondida・Quellaveco ほか'],['銅精鉱・ボーキサイト','RtMが供給'],['製錬会社','銅地金・アルミ地金'],['銅地金・アルミ地金','RtM・Triland Metals'],['電線・再エネ・EV','配線・モーター・AI/DC'])]
o=''
for r_,(lab,*cells) in enumerate(rows):
    y=hy+50+r_*62
    b+=T(L,y-2,lab,None,'k','color:'+G1)
    for i,(t,s_) in enumerate(cells):
        tr=i in (1,3)
        b+=T(cx[i],y+12,t,cw[i]-14,'hs','font-size:9px;font-weight:700;color:'+(NV if tr else INK))+T(cx[i],y+27,s_,cw[i]-14,'s')
        if i<4: o+=f'<path d="M{cx[i]+cw[i]-12},{y+18} H{cx[i+1]-8}" stroke="{G3}" stroke-width=".7"/><path d="M{cx[i+1]-11},{y+15} l3,3 l-3,3" fill="none" stroke="{G2}" stroke-width=".7"/>'
    o+=f'<line x1="{L}" y1="{y+50}" x2="{1190-L}" y2="{y+50}" stroke="{G4}" stroke-width=".8"/>'
b+=S(o)
wy=hy+182
b+=A(cx[0],wy,f'<span style="font-family:IN;font-weight:600;font-size:6px;letter-spacing:1.6px;color:#fff">INVESTMENT</span>　<span style="font-family:Noto Sans JP;font-weight:700;font-size:8px;color:#fff">資源投資（鉱山・製鉄／製錬）｜鉄鋼原料本部・クリティカルミネラル本部</span>',cx[2]+cw[2]-cx[0],'',f'height:20px;padding:4px 10px;line-height:12px;background:{BR}')
b+=A(cx[0],wy+23,f'<span style="font-family:IN;font-weight:600;font-size:6px;letter-spacing:1.6px;color:#fff">TRADING · RtM</span>　<span style="font-family:Noto Sans JP;font-weight:700;font-size:8px;color:#fff">トレーディング｜金属資源トレーディング本部 — 15業界 × 50カ国 × 約1,000社</span>',cx[4]+cw[4]-cx[0],'',f'height:20px;padding:4px 10px;line-height:12px;background:{NV}')
# lower left: business model + virtuous cycle
by=wy+66
b+=T(L,by,'RtM BUSINESS MODEL',None,'k')+T(L+120,by,'一つの商品の中で、投資から販売までを一気通貫に',None,'kj')
bm=[('MC assets + Third party','MC保有資産と第三者取引の両方を扱う'),('Stable supply','資源確保による安定供給'),('Market intelligence','市場・業界動向の発信と知見共有で、事業機会を発掘'),('Continuous value','トレーディング機能の強化で付加価値を生み続ける')]
for i,(e,j) in enumerate(bm):
    x=L+(i%2)*130; y=by+18+(i//2)*44
    b+=A(x,y,'',120,'',f'border-top:1.2px solid {NV}')+T(x,y+5,e.upper(),120,'l','font-size:5.6px;letter-spacing:1px;color:'+NV)+T(x,y+15,j,120,'hs','font-size:7.2px')
b+=para(L+270,by+18,245,'出資案件から得られる持分見合いのオフテイクをRtMが引き受け、ヘッジ・在庫・物流などの機能を付加して欧州・シンガポール・米州の顧客に届けます。顧客と接するRtMが得た市場の“生きた情報”は、資源投資の判断へ還元されます。肥料資源では本格投資に先立ちトレーディングデスクを設け、市場を理解してから投資へ——この好循環こそ、投資と販売を併せ持つ私たちのアイデンティティです。','font-size:6.8px')
fy2=by+114
b+=T(L,fy2,'RtM FUNCTIONS',None,'k')+T(L+90,fy2,'お客様に提供できる5つの機能',None,'kj')
for i,(e,j) in enumerate([('Marketing &amp; Procurement','販売・調達'),('Logistics','物流'),('Financing','ファイナンス'),('Risk Management','リスク管理'),('Carbon Reduction','脱炭素')]):
    x=L+i*104; b+=T(x,fy2+18,f'0{i+1}',None,'nb','font-size:12px;color:'+NV)+T(x+20,fy2+18,e,None,'l','font-weight:600;font-size:6px;white-space:nowrap')+T(x+20,fy2+28,j,80,'s')
# lower right: commitment
cxp=R+20
b+=A(cxp,by-10,'',1190-cxp,'',f'height:{842-by+10}px;background:{INK}')
b+=S(hmap(cxp+250,by+120,320,-20,190,-50,60,step=1.6,sw=.5,seed=12,t0=0,t1=.5)[0].replace('stroke="#','opacity=".55" stroke="#'))
b+=T(cxp+30,by+8,'Our commitment',None,'k','color:#e9d6ac')
b+=T(cxp+30,by+24,'Supporting society<br>with the resources it needs.',460,'d','font-size:26px;color:#fff')
b+=T(cxp+30,by+88,'社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する。',300,'hs','color:#fff;font-size:9px')
b+=T(cxp+30,by+124,'需要の拡大、供給制約、地政学リスク——変化する外部環境に、①安定的な資源確保による安定供給と、②バリューチェーン全体の効率化による効率的な供給の両面で応えていきます。共に、持続可能で豊かな未来を。',230,'b','color:#c9ced3;font-size:6.6px')
b+=T(cxp+30,by+202,'Mitsubishi Corporation　Mineral Resources Group',None,'l','color:#fff')+T(cxp+30,by+213,'2-3-1 Marunouchi, Chiyoda-ku, Tokyo 100-8086, Japan｜www.mitsubishicorp.com',None,'s','color:#9aa1a8;font-family:IN')
pages.append(spread(b,10,11,'動画08 Integrated Value Chain。【強調】見開き全幅で、鉄鋼・非鉄×川上→川下。投資（ブロンズ）とトレーディング（ネイビー）の色を全ページで統一。下段にRtMのビジネスモデル・好循環・5つの機能。','動画09 Closing。濃色パネルに約束（ミッション）と外部環境への答え、ヘアラインの地図を薄く重ねて冊子を閉じる。連絡先を含む。'))

links=''.join(f'<link rel="stylesheet" href="f/nsjp/package/{w}.css">' for w in (400,500,700))
open('daiwari_v12.html','w').write('<!doctype html><meta charset=utf-8>'+links+'<style>'+CSS2+'</style>'+''.join(pages))
