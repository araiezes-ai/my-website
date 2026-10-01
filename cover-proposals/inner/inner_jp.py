exec(open('jp_head.py').read())
IMG.update({'BMAロゴ':('r-040.png','contain'),'写真：鉱山会社':'x_case_mine.jpg','写真：製錬会社':'x_case_smelt.jpg','写真：最終用途':'x_case_pylon.jpg'})
CSS+="""
.jl{font-size:7.6px;letter-spacing:.6px;color:#6b7076;font-weight:400}
.jh1{font-weight:300;font-size:23px;line-height:1.45;letter-spacing:1px;color:#24272b}
.jh2{font-weight:400;font-size:10.5px;letter-spacing:.6px;color:#2e3135}
.jh2:before{content:"";display:block;width:16px;height:1px;background:#2e3135;margin-bottom:7px}
.jb{font-weight:300;font-size:8.2px;line-height:1.7;color:#45494e;letter-spacing:.2px}
.red{color:#C8102E}
"""
RED='#C8102E'
def jl(x,y,t,w=None,style=''): return A(x,y,t,w,'jl',style)
def jh2(x,y,t,w=None): return A(x,y,t,w,'jh2')
def chap(x,y,c,t): return A(x,y,f'<b></b>{c}&nbsp;&nbsp;<span style="letter-spacing:2px">{t}</span>',cls='lab',style='text-transform:none')
def sec(x,y,t): return A(x,y,t,cls='jl',style='color:#2e3135;font-weight:500;letter-spacing:1.5px')
L=48; R=595+48; CW=595-96
pages=[]

# ================= P.02-03 =================
b=''
b+=chap(L,52,'序','CORE MESSAGE')
b+=jl(L,80,'すべての読み手に伝える、ただひとつのメッセージ')
b+=A(L,104,'Strength to Hold.<br>Power to <span class="red">Connect.</span>',cls='h1',style='font-size:34px;line-height:1.22')
core=("Resources, on their own, do not hold value. It takes someone to discover them, nurture them, and deliver them to where they're needed. "
"Only then do they become true power.<br><br>We engage with world-class assets, connecting the value chain from upstream to downstream through investment and trading. "
"Because we stand on fair ground, we can bridge gaps others cannot. Because we stand between diverse partners and users, we find the right answer for every moment. "
"Because we hold the assets, we turn the value dormant in the world into power for society.")
b+=A(L,206,core,330,'body',style='font-size:9.2px;line-height:1.75')
b+=note(L,388,'コアメッセージは粗原稿で英文のため英文のまま',330)
b+=rule(L,452,CW)
b+=jh2(L,470,'日本有数の総合商社・三菱商事')
b+=ph(L,500,150,67,'画像：三綱領')+jl(L,572,'三綱領')
b+=bars(L,594,150,4)
facts=[('1954<span style="font-size:12px">年</span>','創立',''),('<span class="red">76</span><span style="font-size:12px">カ国／</span>104<span style="font-size:12px">拠点</span>','',''),('多様な','事業基盤',''),('総合力を活かす','総合商社','')]
for i,(n,c,_) in enumerate(facts):
    fx=L+178+(i%2)*162; fy=500+(i//2)*112
    b+=rule(fx,fy,140)
    big=i<2
    b+=A(fx,fy+12,n,cls='num',style=f'font-size:{26 if big else 15}px;'+('' if big else 'font-weight:300;letter-spacing:1px'))
    b+=A(fx,fy+(46 if big else 32),c,cls='jl')
    b+=bars(fx,fy+(62 if big else 50),140,2)
# right
b+=chap(R,52,'目次','CONTENTS')
toc=[('序','序・目次 Core Message','日本有数の総合商社・三菱商事<br>WHO WE ARE（仮）　中核をなす金属資源グループ','02–03'),
('第1章','HOW WE WORK（仮）','信用力と総合力で強力に事業を推進<br>フルバリューチェーンで社会に価値を届ける','04–05'),
('第2章','WHAT WE HAVE（仮）','鉄を支える世界有数の原料炭事業　／　電化社会を支える銅ポートフォリオ<br>世界の資源と需要をつなぐ販売網　／　資源の可能性をさらに広げる','06–09'),
('第3章','PROOF（仮）','資源業界で選ばれ続けるパートナー','10'),
('第4章','VISION &amp; ACTION（仮）','社会に必要な良質な金属資源を持続的に供給する','11')]
for i,(n,t,s_,p) in enumerate(toc):
    ty=82+i*52
    b+=rule(R,ty,CW)
    b+=A(R,ty+12,n,cls='jl',style='color:'+(RED if i==0 else '#9aa0a6')+';font-size:9px')
    b+=A(R+56,ty+9,t,style='font-size:12px;font-weight:300;color:#24272b;letter-spacing:.5px')
    b+=A(R+56,ty+27,s_,cls='jb',style='font-size:7.6px;line-height:1.6;color:#6b7076')
    b+=A(R+CW-40,ty+12,p,40,'fol',style='text-align:right')
b+=rule(R,342,CW)
b+=jh2(R,364,'中核をなす金属資源グループ')
b+=bars(R+200,364,299,2,.6)
b+=jl(R,404,'三菱商事の事業グループ',style='color:#2e3135')
groups=['天然ガスグループ','総合素材グループ','金属資源グループ','エネルギーソリューショングループ','機械グループ','化学品グループ','生活産業グループ','食料産業グループ','社会インフラグループ','自動車・モビリティグループ','電力ソリューショングループ']
for i,g in enumerate(groups):
    gy=422+i*17
    b+=A(R,gy,g,cls='jl',style=('color:'+RED+';font-weight:500' if i==2 else 'color:#45494e'))
    b+=rule(R,gy+13,160)
cx,cy=R+356,548; r=64
inner=''
for ang in (-90,150,30):
    px_=cx+46*math.cos(math.radians(ang)); py_=cy+46*math.sin(math.radians(ang))
    inner+=f'<circle cx="{px_-R+20:.1f}" cy="{py_-400:.1f}" r="{r}" fill="none" stroke="#9ea3a9" stroke-width=".6"/>'
b+=svg(R-20,400,520,330,inner)
pil=[(-90,'資源投資・開発','優良資産への投資・開発で<br>長期的な安定供給を実現'),(150,'金属資源トレーディング','グローバルなネットワークで<br>最適な供給・販売を構築'),(30,'事業経営・パートナーシップ','パートナーとの協業で持続的な<br>成長と社会的価値を創出')]
for ang,t,d in pil:
    if ang==-90: tx,ty=cx-70,cy-150
    else: tx,ty=cx+(-150 if ang==150 else 10),cy+104
    b+=A(tx,ty,f'<div style="font-size:9px;color:#2e3135;font-weight:400;letter-spacing:.5px;margin-bottom:3px">{t}</div><div class="jb" style="font-size:7.2px;line-height:1.55">{d}</div>',140,style='text-align:center')
b+=A(cx-45,cy-10,'<div style="font-size:9px;color:#C8102E;font-weight:500;letter-spacing:.5px">金属資源グループ</div><div style="font-size:6px;letter-spacing:1px;color:#7a7f85">MINERAL RESOURCES GROUP</div>',90,style='text-align:center')
pages.append(spread(b,2,3))

# ================= P.04-05 =================
b=''
b+=chap(L,52,'第1章','HOW WE WORK（仮）')
b+=sec(L,80,'事業概要')
b+=A(L,98,'信用力と総合力で<br>強力に事業を推進',cls='jh1')
b+=bars(L,170,440,4)
b+=rule(L,218,CW)
b+=jh2(L,232,'総合商社としての信用力・財務基盤')
b+=jl(L,262,'グループ総資産　2025年3月期')
b+=A(L,276,'45,381<span style="font-size:16px;margin-left:3px">億円</span>',cls='num red',style='font-size:40px')
def chart(x,y,title,v1,v2,segs,axis,extra=0):
    s_=A(x,y,title,cls='jl',style='color:#2e3135')
    W=118; sc=W/axis; inner=''
    cx_=0
    for val,sh in zip(segs,[95,140,180,212]):
        w=val*sc; inner+=hairbar(cx_,0,w-1.2,16,sh); cx_+=w
    for k,val in enumerate(segs[:3]):
        pass
    if extra:
        inner+=f'<rect x="{cx_:.1f}" y="0" width="22" height="16" fill="#5d6268"/><text x="{cx_+11:.1f}" y="11" fill="#fff" font-size="7" text-anchor="middle">※</text><path d="M{cx_+15:.1f},-2 l3,10 l-3,10" stroke="#fff" stroke-width="1.5" fill="none"/>'
    inner+=hairbar(0,40,v2*sc,16,212)
    inner+=f'<line x1="{W:.1f}" y1="-4" x2="{W:.1f}" y2="60" stroke="#c9ccd0" stroke-dasharray="1.5 1.5" stroke-width=".5"/>'
    s_+=svg(x+104,y+18,200,62,inner)
    s_+=A(x+104+W-10,y+82,f'{axis:,}',20,'jl',style='font-size:6px;text-align:center')
    s_+=A(x,y+18,'2025年3月期',cls='jl',style='font-size:6.8px')+A(x,y+28,f'{v1:,}<span style="font-size:8px">億円</span>',cls='num',style='font-size:13px')
    s_+=A(x,y+56,'2026年3月期見通し（5/2公表）',cls='jl',style='font-size:6.2px')+A(x,y+66,f'{v2:,}<span style="font-size:8px">億円</span>',cls='num',style='font-size:13px;color:#7a7f85')
    return s_
b+=chart(L,336,'グループ営業収益（CF）',1787,1450,[907,533,208,139],1600)
b+=chart(L+262,336,'グループ連結純利益',2278,1140,[401,741,153,54],1300,extra=1)
leg=''.join(f'<span style="display:inline-block;width:10px;height:7px;margin:0 4px 0 {0 if i==0 else 12}px;vertical-align:-1px;background:repeating-linear-gradient(90deg,rgb({s_},{s_+3},{s_+7}) 0 .6px,transparent .6px 1.6px)"></span>{t}' for i,(s_,t) in enumerate([(95,'❶ 原料炭事業'),(140,'❷ 銅事業'),(180,'❸ 鉄鉱石事業'),(212,'その他')]))
b+=A(L,432,leg+'&nbsp;&nbsp;&nbsp;&nbsp;※ 一過性要因（粗原稿の※部分）',cls='jl',style='white-space:nowrap;font-size:7px')
b+=note(L,448,'内訳は粗原稿グラフからの読み取り値。「営業収益」と「営業収益CF」の表記ゆれ、※の内容、その他（凡例なし）を要確認',CW)
b+=rule(L,474,CW)
b+=jh2(L,488,'他部門との連携による総合力で<br>巨大バリューチェーン構築')
b+=bars(L,534,220,3)
stats=[('<span class="red">4</span>','カ国','優良資産ポートフォリオ'),('57','カ国','グローバルプレゼンス')]
for i,(n,u,c) in enumerate(stats):
    sx=L+250+i*125
    if i: b+=vrule(sx-12,490,58)
    b+=A(sx,490,f'{n}<span style="font-size:11px;margin-left:2px">{u}</span>',cls='num',style='font-size:30px')
    b+=A(sx,530,c,cls='jl')
b+=A(L+250,560,'<b style="font-weight:500;color:#2e3135">投資・鉱山開発　計6商品</b><br>原料炭／鉄鉱石／銅（モリブデン、亜鉛）／ボーキサイト／ニッケル／リチウム',CW-250,'jb',style='font-size:7.4px;line-height:1.6')
b+=A(L+250,598,'<b style="font-weight:500;color:#2e3135">トレーディング　計13+商品</b><br>原料炭／鉄鉱石／銅（モリブデン、亜鉛）／ボーキサイト・アルミ／ニッケル／リチウム／貴金属／一般炭／クロム／鉛／錫／レアアース／肥料資源 etc.',CW-250,'jb',style='font-size:7.4px;line-height:1.6')
b+=rule(L,666,CW)
b+=jh2(L,680,'スピードを支えるガバナンス')
b+=bars(L+250,680,249,4)
# right
b+=chap(R,52,'第1章','HOW WE WORK（仮）')
b+=sec(R,80,'事業概要')
b+=A(R,98,'フルバリューチェーンで<br>社会に価値を届ける',cls='jh1')
b+=bars(R,170,440,4)
b+=rule(R,218,CW)
b+=jh2(R,232,'川上から川下まで一気通貫で価値を創造')
fl=f'<line x1="0" y1="6" x2="490" y2="6" stroke="{RED}" stroke-width=".7"/>'
for i in range(3): fl+=f'<circle cx="{i*170+3}" cy="6" r="3" fill="#fff" stroke="{RED}" stroke-width=".8"/>'
fl+=f'<path d="M484,2 L492,6 L484,10" fill="none" stroke="{RED}" stroke-width=".7"/>'
b+=svg(R,268,500,14,fl)
cols=[('上流','資源投資・開発','世界各地の優良な鉱山・権益への投資で安定的な供給を確保し、長期的な事業の基盤を築きます。'),
('中流','製錬・加工・物流','確保した資源を、環境にも配慮した技術で製錬・加工し、付加価値の高い製品として供給します。'),
('下流','販売・需要家','グローバルな物流網とトレーディング機能で、世界の需要に応じた最適な供給を実現します。')]
for i,(t,s1,d) in enumerate(cols):
    x=R+i*170
    b+=A(x,292,t,cls='jl',style='color:#2e3135;letter-spacing:2px')
    b+=A(x,306,s1,150,style='font-size:12px;font-weight:300;letter-spacing:.5px')
    b+=bars(x,330,150,4)
b+=note(R,368,'各工程の説明文は粗原稿ではダミー文のため帯で表示',CW)
b+=rule(R,392,CW)
for i,l in enumerate(['写真：鉱山（上流）','写真：製錬所（中流）','写真：洋上風力（用途）','写真：EV（需要家）']):
    b+=ph(R+i*127,412,115,150,l)
    if i<3: b+=svg(R+i*127+115,484,12,6,'<path d="M2,3H10M7,0.5L10,3L7,5.5" stroke="#9ea3a9" stroke-width=".6" fill="none"/>')
pages.append(spread(b,4,5))

# ================= P.06-07 =================
b=''
b+=chap(L,52,'第2章','WHAT WE HAVE（仮）')
b+=sec(L,80,'原料炭事業')
b+=A(L,98,'鉄を支える、<br>世界有数の原料炭事業',cls='jh1')
b+=bars(L,170,220,6)
b+=ph(L+250,150,249,170,'写真：BMA鉱山・重機')
b+=rule(L,340,CW)
b+=jl(L,354,'BMAは一級強粘炭供給の約50%のシェア',style='color:#2e3135;font-weight:500')
b+=jl(L,368,'一級強粘炭の供給（2026年）',style='font-size:6.8px')
b+=A(L,384,'約<span style="font-size:46px">50</span><span style="font-size:18px">%</span>',cls='num red',style='font-size:16px')
sh=hairbar(0,0,58,12,95)+hairbar(60,0,58,12,150)+hairbar(120,0,130,12,215)
b+=svg(L,440,250,14,sh)
b+=A(L,458,'BHP<br>23%',56,'jl',style='line-height:1.5')+A(L+60,458,'三菱商事<br>23%',56,'jl',style='line-height:1.5')+A(L+120,458,'その他',80,'jl')
b+=ph(L+186,452,64,44,'BMAロゴ')
b+=note(L,490,'粗原稿の円グラフを横一本のヘアラインバーに。比率は要確認',240)
m,mw,mh,mpx=hairmap(150,112,155,-44,-9,step=1.3,sw=.4,japan=False,dark=135,light=225,sites=[(148.3,-22.3,RED)])
bx,by=mpx(148.3,-22.3)
b+=jl(L+300,354,'豪州ボーエン盆地の中核資産',style='color:#2e3135;font-weight:500')
b+=svg(L+300,372,150,mh,m+f'<line x1="{bx:.1f}" y1="{by:.1f}" x2="{bx+12:.1f}" y2="{by-26:.1f}" stroke="#2e3135" stroke-width=".5"/>')
b+=A(L+300+bx-4,372+by-38,'Bowen Basin',cls='cap',style='color:#2e3135')
b+=bars(L+300,372+mh+8,199,2,.7)
b+=rule(L,526,CW)
feats=[('QUALITY','品質','高い発熱量と低不純物の高品位な原料炭を安定的に供給しています。','写真：原料炭','高品質な供給'),
('SCALE','規模','豪州ボーエン盆地における大規模な生産基盤と輸送インフラを活かし、安定供給を実現しています。','写真：港湾・鉄道','安定生産とインフラ'),
('PARTNERSHIP','パートナーシップ','パートナーシップにより、強固な事業基盤を構築し、持続的な成長を目指しています。','写真：パートナー','長期的な連携')]
for i,(e,t,d,p,c) in enumerate(feats):
    x=L+i*170
    b+=A(x,540,f'<span class="cap" style="color:{RED if i==0 else "#7a7f85"}">{e}</span>&nbsp;&nbsp;<span style="font-size:10px;font-weight:400">{t}</span>',160)
    b+=A(x,562,d,152,'jb')
    b+=ph(x,612,155,92,p)
    b+=jl(x,710,c,style='color:#2e3135')
    b+=bars(x,724,155,2,.6)
b+=chap(R,52,'第2章','WHAT WE HAVE（仮）')
b+=sec(R,80,'銅事業')
b+=A(R,98,'電化社会を支える、<br>銅ポートフォリオ',cls='jh1')
b+=bars(R,170,220,6)
b+=ph(R+250,150,249,170,'写真：銅鉱山')
b+=rule(R,340,CW)
b+=jl(R,354,'主要鉱山参画プロジェクト（例）',style='color:#2e3135;font-weight:500')
mines=[('Escondida','チリ','世界最大級の銅鉱山の一つ'),('Los Pelambres','チリ','安定生産と拡張による長期的な供給'),('Antamina','ペルー','高品質な銅・亜鉛の複合鉱山'),('Quellaveco','ペルー','次世代の中核資産となる大型銅鉱山'),('その他のプロジェクト','','成長機会の取り込みによるポートフォリオの拡充')]
for i,(n,c,d) in enumerate(mines):
    y=372+i*26
    b+=A(R,y,f'{i+1}',cls='num',style=f'font-size:12px;color:{RED}')
    b+=A(R+16,y,n,style='font-size:9px;font-weight:400')
    b+=A(R+16,y+12,c,cls='jl',style='font-size:6.6px')
    b+=A(R+120,y+2,d,170,'jb',style='font-size:7.6px')
    b+=rule(R,y+21,300)
m,mw,mh,mpx=hairmap(110,-90,-56,-36,-2,step=1.3,sw=.4,japan=False,dark=135,light=225,sites=[(-69.07,-24.27,RED),(-70.5,-31.7,RED),(-77.05,-9.53,RED),(-70.6,-17.1,RED)])
lbl=''
for n,lo,la in [('Antamina',-77.05,-9.53),('Quellaveco',-70.6,-17.1),('Escondida',-69.07,-24.27),('Los Pelambres',-70.5,-31.7)]:
    x,y=mpx(lo,la); lbl+=A(R+360+x-78,346+y-4,n,70,cls='cap',style='color:#2e3135;letter-spacing:.8px;text-align:right')
b+=svg(R+360,346,110,mh,m)+lbl
b+=rule(R,526,CW)
b+=A(R,542,'■ 低炭素銅（Green Copper）への取り組み',style='font-size:10px;font-weight:400')
b+=bars(R,566,230,4)
b+=ph(R+250,540,249,110,'写真：低炭素銅の取り組み')
b+=ph(R,664,240,70,'写真：安定的な供給基盤')+ph(R+259,664,240,70,'写真：長期的な価値創造')
b+=jl(R,740,'安定的な供給基盤',style='color:#2e3135')+jl(R+259,740,'長期的な価値創造',style='color:#2e3135')
b+=bars(R+90,740,150,1,1)+bars(R+349,740,150,1,1)
pages.append(spread(b,6,7))

# ================= P.08-09 =================
b=''
b+=chap(L,52,'第2章','WHAT WE HAVE（仮）')
b+=sec(L,80,'トレーディング事業')
b+=A(L,98,'世界の資源と<br>需要をつなぐ販売網',cls='jh1')
b+=bars(L,170,220,5)
b+=ph(L+250,150,249,130,'写真：積出港・銅カソード')
b+=rule(L,298,CW)
b+=jl(L,312,'市場をつなぐ販売網',style='color:#2e3135;font-weight:500')
b+=A(L,330,'15<span style="font-size:9px">業界</span><span style="font-size:11px;color:#9aa0a6;margin:0 5px">×</span>50<span style="font-size:9px">カ国</span><span style="font-size:11px;color:#9aa0a6;margin:0 5px">×</span>約1,000<span style="font-size:9px">社</span>',cls='num',style='font-size:24px;white-space:nowrap')
b+=jl(L+300,312,'グローバルネットワーク',style='color:#2e3135;font-weight:500')
b+=A(L+300,330,'10<span style="font-size:9px;margin-left:2px">拠点</span>',cls='num',style='font-size:24px')
b+=A(L+300,362,'シンガポール、日本、インド、中国、米国、英国、UAE、インドネシア、タイ、チリ',199,'jb',style='font-size:7.4px')
b+=rule(L,394,CW)
b+=jh2(L,408,'RtM事業のビジネスモデル')
dg=''
for y in (0,70,140):
    dg+=f'<rect x="0" y="{y}" width="250" height="20" fill="none" stroke="#9ea3a9" stroke-width=".6"/>'
for y in (20,90):
    dg+=f'<line x1="14" y1="{y}" x2="14" y2="{y+50}" stroke="#2e3135" stroke-width=".6"/><path d="M11,{y+45} L14,{y+50} L17,{y+45}" fill="none" stroke="#2e3135" stroke-width=".6"/>'
    dg+=f'<line x1="136" y1="{y+50}" x2="136" y2="{y}" stroke="#9ea3a9" stroke-width=".6"/><path d="M133,{y+5} L136,{y} L139,{y+5}" fill="none" stroke="#9ea3a9" stroke-width=".6"/>'
b+=svg(L,434,250,160,dg)
for t,y in [('Mitsubishi Corporation',0),('RtM',70),('顧客基盤',140)]:
    b+=A(L,434+y+5,t,250,'jl',style='text-align:center;color:#2e3135;font-weight:500')
st='font-size:6.8px;line-height:1.5'
b+=A(L+22,460,'第三者取引／<b style="font-weight:500">MC保有資産</b><br>資源確保による<span class="red">安定供給</span>',104,'jb',style=st)
b+=A(L+144,460,'市場・業界動向の発信・知見共有による<b style="font-weight:500">事業機会の発掘</b>',104,'jb',style=st)
b+=A(L+22,530,'トレーディング機能強化による<b style="font-weight:500">継続的な付加価値創出</b>',104,'jb',style=st)
b+=A(L+144,530,'広い産業接地面を活かした<b style="font-weight:500">インテリジェンス機能の発揮</b>',104,'jb',style=st)
# trading chart with values read from rough
vals=[178,180,281,245,121,470,272,251,262,277,292]
ch=''; H_=100; top=300
for i,v in enumerate(vals):
    h=min(v,300)/top*H_
    ch+=hairbar(i*17,H_-h,11,h,110 if i<6 else 175,step=1.5)
    if v>300: ch+=f'<path d="M{i*17-1},{H_-h+8} l13,-4 M{i*17-1},{H_-h+12} l13,-4" stroke="#fff" stroke-width="2"/>'
y165=H_-165/top*H_; y250=H_-250/top*H_
ch+=f'<line x1="-2" y1="{y165:.1f}" x2="100" y2="{y165:.1f}" stroke="#7a7f85" stroke-dasharray="2 1.5" stroke-width=".6"/>'
ch+=f'<line x1="100" y1="{y250:.1f}" x2="186" y2="{y250:.1f}" stroke="{RED}" stroke-dasharray="2 1.5" stroke-width=".7"/>'
ch+=f'<line x1="0" y1="{H_+.5}" x2="186" y2="{H_+.5}" stroke="#9ea3a9" stroke-width=".5"/>'
for i in range(11): ch+=f'<text x="{i*17+5.5}" y="{H_+9}" font-size="5.5" fill="#7a7f85" text-anchor="middle">{"FY20" if i==0 else 20+i}</text>'
b+=jl(L+300,408,'トレーディング事業　業績推移（億円）',style='color:#2e3135;font-weight:500')
b+=A(L+300,428,'基礎収益 160〜170億円',cls='jl',style='font-size:6.8px')
b+=A(L+400,420,'基礎収益 <span style="font-size:13px">250</span>億円',cls='jl red',style='font-size:7px;color:#C8102E')
b+=svg(L+305,440,190,112,ch)
b+=note(L+300,566,'棒の値は粗原稿グラフからの読み取り値（FY25は軸超え）。正式数値を要確認',199)
b+=rule(L,600,CW)
b+=jh2(L,612,'事例）トレーディング事業')
steps=[('鉱山','鉱山会社','写真：鉱山会社','銅鉱石・ボーキサイト','クリティカルミネラル本部'),('トレーディング','RtM','','','金属資源トレーディング本部'),('製鉄／製錬','製錬会社','写真：製錬会社','銅地金・アルミ地金','クリティカルミネラル本部'),('トレーディング','RtM','','','金属資源トレーディング本部'),('最終製品／需要家','主な最終用途','写真：最終用途','電線・再エネ発電・EV内配線、モーター','')]
for i,(h,t,p,sub,dept) in enumerate(steps):
    x=L+i*101
    b+=A(x,640,h,92,'jl',style=f'color:{RED if "トレ" in h else "#2e3135"};font-weight:500;border-top:.6px solid {RED if "トレ" in h else "#2e3135"};padding-top:4px')
    b+=A(x,660,t,92,'jl')
    if p: b+=ph(x,674,92,50,p)
    else: b+=A(x,674,'RtM',92,style='height:50px;line-height:50px;text-align:center;font-size:14px;font-weight:300;color:#9aa0a6;border:.6px solid #dfe2e5')
    b+=A(x,728,sub,92,'jb',style='font-size:6.6px;line-height:1.45')
    b+=A(x,752,dept,92,'jl',style='font-size:6.2px')
b+=note(L,772,'粗原稿で上段（鉄鋼原料本部の行）が見切れているため要確認',CW)
# right
b+=chap(R,52,'第2章','WHAT WE HAVE（仮）')
b+=sec(R,80,'その他の事業')
b+=A(R,98,'資源の可能性を<br>さらに広げる',cls='jh1')
b+=bars(R,170,220,5)
b+=ph(R+250,150,249,110,'写真：夜空と鉱山車両')
b+=rule(R,276,CW)
b+=jh2(R,288,'事業展開')
OF=[(-0.1,51.5),(77.2,28.6),(103.8,1.3),(-77.0,40.4)]
SUB=[(153.0,-27.5),(-70.65,-33.45),(-77.0,-12.0)]
INV=[(148.3,-22.3),(-66.9,52.9),(-96.0,33.0),(-77.05,-9.53),(-70.6,-17.1),(-69.07,-24.27),(-70.5,-31.7),(-70.9,-28.6),(-70.3,-33.15)]
EXP=[(13.2,65.8),(-128.9,58.5),(-94.0,51.6),(121.4,-30.0),(141.7,-13.3),(-70.3,-22.9)]
m,mw,mh,mpx=hairmap(CW,-25,335,-56,76,step=1.3,sw=.4,sites=[],dark=120,light=222)
mk=''
def P_(lo,la): x,y=mpx(lo,la); return x,y
for lo,la in OF: x,y=P_(lo,la); mk+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.8" fill="#2e3135"/>'
x,y=P_(139.7,35.7); mk+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.8" fill="#2e3135" stroke="#fff" stroke-width=".5"/>'
for lo,la in SUB: x,y=P_(lo,la); mk+=f'<rect x="{x-1.6:.1f}" y="{y-1.6:.1f}" width="3.2" height="3.2" fill="#fff" stroke="#2e3135" stroke-width=".7"/>'
for lo,la in INV: x,y=P_(lo,la); mk+=f'<path d="M{x:.1f},{y-2.2:.1f} l2.2,3.8 h-4.4z" fill="#2e3135"/>'
for lo,la in EXP: x,y=P_(lo,la); mk+=f'<path d="M{x:.1f},{y-2.3:.1f} l2.1,2.3 l-2.1,2.3 l-2.1,-2.3z" fill="#fff" stroke="#2e3135" stroke-width=".6"/>'
b+=svg(R,312,CW,mh,m+mk)
REG=[('01','欧州',(5,58),'Arctial（低炭素アルミ）<br>Triland Metals（先物取引）<br>RtM Europe（トレーディング）'),
('02','アジア',(104,20),'RtM Japan（トレーディング）<br>RtM International（トレーディング）<br>RtM Bharat（トレーディング）'),
('03','豪州',(146,-34),'BMA（原料炭）<br>Aurukun（ボーキサイト）<br>Goongarrie Hub（ニッケル）<br>MDP（アセットマネジメント）'),
('04','北米',(-104,60),'Turnagain（ニッケル）<br>PAK Lithium（リチウム）<br>IOC（鉄鉱石）<br>Elemental USA（二次資源）<br>RtM Americas（トレーディング）'),
('05','チリ・ペルー',(-84,-24),'Escondida・Los Pelambres・Antamina・Quellaveco・Marimaca・Anglo American Sur（銅）<br>CAP／CMP（鉄鉱石）<br>MCI・MCIP（アセットマネジメント）')]
for i,(n,t,(lo,la),items) in enumerate(REG):
    x,y=mpx(lo,la)
    b+=A(R+x-7,312+y-6,n,14,style='font-size:6.5px;text-align:center;background:#fff;color:#C8102E;letter-spacing:.5px;line-height:12px;border:.5px solid #C8102E;border-radius:7px')
    cx_=R+i*100
    b+=A(cx_,312+mh+12,f'<span style="color:#C8102E">{n}</span>&nbsp;&nbsp;{t}',96,'jl',style='color:#2e3135;font-weight:500')
    b+=A(cx_,312+mh+26,items,96,'jb',style='font-size:6.4px;line-height:1.55')
lg=('<svg width="9" height="7"><circle cx="4" cy="3.5" r="2" fill="#2e3135"/></svg> 金属資源トレーディング関連／RtMオフィス　'
'<svg width="9" height="7"><rect x="2" y="1.5" width="4" height="4" fill="#fff" stroke="#2e3135" stroke-width=".8"/></svg> 子会社／支店　'
'<svg width="9" height="7"><path d="M4,1 l2.6,4.6 h-5.2z" fill="#2e3135"/></svg> 投資案件　'
'<svg width="9" height="7"><path d="M4,.8 l2.5,2.7 l-2.5,2.7 l-2.5,-2.7z" fill="#fff" stroke="#2e3135" stroke-width=".7"/></svg> 探査・調査・開発中案件')
b+=A(R,312+mh+112,lg,CW,'jl',style='font-size:6.6px;white-space:nowrap')
b+=A(R,312+mh+126,'商品：原料炭／銅／リチウム／鉄鉱石／ボーキサイト・アルミ／二次資源／ニッケル（色ではなく各案件名の（　）内に表記）',CW,'jl',style='font-size:6.4px')
b+=note(R,312+mh+140,'記号の割当は粗原稿の地図から判読。要確認',CW)
tiles=['鉄鉱石','ニッケル','リチウム','アルミ','ボーキサイト','二次資源']
for i,t in enumerate(tiles):
    x=R+i*84; y=672
    b+=ph(x,y,76,80,'写真：'+t)
    b+=A(x,y+84,t,80,'jl',style='color:#2e3135')
pages.append(spread(b,8,9))

# ================= P.10-11 =================
b=''
b+=chap(L,52,'第3章','PROOF（仮）')
b+=A(L,98,'資源業界で<br>選ばれ続ける<br>パートナー',cls='jh1')
b+=bars(L,206,220,4)
b+=ph(L+250,150,249,150,'写真：現場で働く人々')
b+=rule(L,322,CW)
b+=jh2(L,336,'資源業界における不可欠な存在')
b+=bars(L,362,CW,2,.8)
gx,gy,gw,gh=L,404,CW,340
b+=f'<div class="rule" style="left:{gx}px;top:{gy+gh/2}px;width:{gw}px"></div><div class="vrule" style="left:{gx+gw/2}px;top:{gy}px;height:{gh}px"></div>'
b+=A(gx+gw/2-70,gy+gh/2-34,f'<div style="background:#fff;padding:12px 0;text-align:center"><div style="width:14px;height:1px;background:{RED};margin:0 auto 10px"></div><span class="num red" style="font-size:22px">Partner<br>of Choice</span></div>',140)
quad=[('資源メジャーとの<br>企業文化的親和性',0,0),('資源投資経験に裏打ちされた<br>JV経営力',1,0),('事業PFを活かした<br>健全な財務基盤',0,1),('マクロ環境と資源バリューチェーン<br>に対する深い知見',1,1)]
for t,qx,qy in quad:
    x=gx+qx*(gw/2)+(30 if qx else 0); y=gy+qy*(gh/2)+(70 if qy else 22)
    b+=A(x,y,t,190,style='font-size:10.5px;font-weight:300;line-height:1.5;letter-spacing:.5px')
    b+=bars(x,y+40,170,3)
b+=chap(R,52,'第4章','VISION &amp; ACTION（仮）')
b+=A(R,98,'社会に必要な<br>良質な金属資源を<br>持続的に供給する',cls='jh1')
b+=bars(R,206,220,4)
b+=ph(R+250,150,249,150,'写真：植生調査・環境')
b+=rule(R,322,CW)
b+=jl(R,336,'グループミッション',style='color:#2e3135;font-weight:500')
b+=A(R,356,'<span class="red">「</span>社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する<span class="red">」</span>',CW,style='font-size:15px;font-weight:300;line-height:1.65;letter-spacing:.8px')
b+=rule(R,422,CW)
ch3=[('01','社会課題','需要の拡大',['世界の人口増加','電化・脱炭素による金属需要の拡大','新興国のインフラ整備'],'写真：都市・人口'),
('02','安定供給','開発難易度・供給制約',['優良資産の獲得競争の激化','鉱山開発の難易度上昇','環境規制・地域合意の重要性'],'写真：鉱山開発'),
('03','地政学と供給網','トレーディング・供給の最適化',['地政学リスクの高まり','サプライチェーンの複雑化','柔軟で強靭な供給網の構築'],'写真：港湾・物流')]
for i,(n,t1,t2,items,p) in enumerate(ch3):
    x=R+i*170
    b+=A(x,436,n,cls='num red',style='font-size:22px')
    b+=A(x+34,438,f'<div class="jl" style="color:#C8102E">{t1}</div><div style="font-size:8.4px;font-weight:400;margin-top:2px;white-space:nowrap">{t2}</div>',130)
    b+=ph(x,472,155,90,p)
    b+=A(x,572,''.join(f'<div style="padding-left:9px;text-indent:-9px;margin-bottom:2px">・{s_}</div>' for s_ in items),155,'jb',style='font-size:7.6px;line-height:1.5')
b+=rule(R,640,CW)
b+=jh2(R,654,'社会課題への取り組み')
b+=bars(R+250,654,249,4)
pages.append(spread(b,10,11))

links=''.join(f'<link rel="stylesheet" href="f/nsjp/package/{w}.css">' for w in (300,400,500))
html=f'<!doctype html><meta charset=utf-8>{links}<style>{CSS}</style>'+''.join(pages)
open('inner_jp.html','w').write(html)
