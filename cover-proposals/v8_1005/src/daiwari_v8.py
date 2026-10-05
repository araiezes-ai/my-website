# 台割 v8 — B案（ガラスの地球儀）のデザイン言語で組んだ構成デザイン案
import base64, io, math, random
from PIL import Image
import glassglobe as G
N_='f/ns/package/files/'
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
_c={}
def uri(f,mx=1400,fmt='JPEG',crop=None,light=0):
    k=(f,mx,fmt,crop,light)
    if k not in _c:
        im=Image.open(f if '/' in f else 'img/'+f)
        im=im.convert('RGBA' if fmt=='PNG' else 'RGB')
        if crop: w,h=im.size; im=im.crop((int(crop[0]*w),int(crop[1]*h),int(crop[2]*w),int(crop[3]*h)))
        if light:
            wh=Image.new(im.mode,im.size,(255,255,255,0) if fmt=='PNG' else (255,255,255))
            a=im.split()[-1] if fmt=='PNG' else None
            im=Image.blend(im,wh,light)
            if a: im.putalpha(a)
        im.thumbnail((mx,mx)); bf=io.BytesIO(); im.save(bf,fmt,**({'quality':84} if fmt=='JPEG' else {}))
        _c[k]=f'data:image/{fmt.lower()};base64,'+base64.b64encode(bf.getvalue()).decode()
    return _c[k]
INK='#23272c'; SUB='#5d636a'; MUTE='#9aa0a6'; GOLD='#b38f4f'; GOLDL='#dcc9a2'; GLASS='#e6eef5'; BLUE='#4f7aa3'; DEEP='#2c4c6e'; RED='#C8102E'; HAIR='#d8dce0'
CSS=f"""@font-face{{font-family:NS;font-weight:200;src:url(data:font/woff2;base64,{b64(N_+'noto-sans-latin-200-normal.woff2')})}}
@font-face{{font-family:NS;font-weight:300;src:url(data:font/woff2;base64,{b64(N_+'noto-sans-latin-300-normal.woff2')})}}
@font-face{{font-family:NS;font-weight:400;src:url(data:font/woff2;base64,{b64(N_+'noto-sans-latin-400-normal.woff2')})}}
@font-face{{font-family:NS;font-weight:500;src:url(data:font/woff2;base64,{b64(N_+'noto-sans-latin-500-normal.woff2')})}}
@page{{size:420mm 297mm;margin:0}}*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:NS,'Noto Sans JP',sans-serif;color:{INK};background:#fff}}
.sp{{position:relative;width:1190px;height:842px;overflow:hidden;background:#fff;page-break-after:always;zoom:1.3333}}
.a{{position:absolute}}
.lab{{font-size:6.6px;letter-spacing:2.2px;color:{GOLD};font-weight:400}}
.labj{{font-size:6.6px;letter-spacing:.6px;color:{MUTE};font-weight:300}}
.en{{font-weight:200;color:{INK};letter-spacing:-.2px;line-height:1.12}}
.jt{{font-family:'Noto Sans JP';font-weight:500;font-size:11px;letter-spacing:.8px;color:{INK}}}
.js{{font-family:'Noto Sans JP';font-weight:300;font-size:8.2px;letter-spacing:.4px;color:{SUB};line-height:1.6}}
.bd{{font-size:7.4px;line-height:1.72;color:#7b8188;font-weight:300;letter-spacing:.1px}}
.cap{{font-size:6px;letter-spacing:1.4px;color:{MUTE}}}
.num{{font-weight:200;color:{INK};line-height:1;letter-spacing:-.5px}}
.sm{{font-family:'Noto Sans JP';font-size:6.6px;line-height:1.55;color:{SUB};font-weight:300}}
.smb{{font-family:'Noto Sans JP';font-size:7.4px;line-height:1.45;color:{INK};font-weight:400}}
.memo{{font-family:'Noto Sans JP';font-size:5.6px;color:#a3a8ae;background:rgba(255,255,255,.85);padding:1px 3px;letter-spacing:.2px;line-height:1.5}}
.fo{{font-size:6.2px;letter-spacing:1.6px;color:{MUTE}}}
.ph{{object-fit:cover;display:block}}
"""
def A(x,y,h,w=None,c='',s=''):
    return f'<div class="a {c}" style="left:{x}px;top:{y}px;{f"width:{w}px;" if w else ""}{s}">{h}</div>'
def svg(x,y,w,h,inner): return f'<svg class="a" style="left:{x}px;top:{y}px;overflow:visible" width="{w}" height="{h}">{inner}</svg>'
def IMG(x,y,w,h,f,pos='50% 50%',r=0,**k):
    return f'<img class="a ph" src="{uri(f,**k)}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-position:{pos};{f"border-radius:{r}px;" if r else ""}">'
def CIRC(cx,cy,d,f,pos='50% 50%',ring=True):
    o=f'<img class="a ph" src="{uri(f,600)}" style="left:{cx-d/2}px;top:{cy-d/2}px;width:{d}px;height:{d}px;border-radius:50%;object-position:{pos}">'
    if ring: o+=f'<div class="a" style="left:{cx-d/2-4}px;top:{cy-d/2-4}px;width:{d+8}px;height:{d+8}px;border-radius:50%;border:.6px solid {GOLDL}"></div>'
    return o
random.seed(4)
LO='lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua enim ad minim veniam quis nostrud exercitation ullamco laboris nisi aliquip ex ea commodo consequat duis aute irure in reprehenderit voluptate velit esse cillum fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt culpa qui officia deserunt mollit anim id est laborum'.split()
def lorem(n):
    w=[random.choice(LO) for _ in range(n)]; w[0]=w[0].capitalize(); s=''
    for i,x in enumerate(w): s+=x+('. ' if i%13==12 else ' ')
    return s.strip()+'.'
def BODY(x,y,w,n,s=''): return A(x,y,lorem(n),w,'bd',s)
def HEAD(x,y,lab,labj,en,jt,js,w=440,size=30):
    o=A(x,y,lab,None,'lab')+A(x,y+11,labj,None,'labj')
    o+=A(x,y+34,en,w,'en',f'font-size:{size}px')
    lines=en.count('<br>')+1; yy=y+34+lines*size*1.12+12
    o+=A(x,yy,'',26,'',f'height:0;border-top:1px solid {RED}')
    o+=A(x,yy+10,jt,w,'jt')+A(x,yy+27,js,w,'js')
    return o, yy+27+ (js.count('<br>')+1)*13.5
def orbit(cx,cy,rx,ry,rot,dots=(),col=GOLDL,sw=.6,op=1):
    o=f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" transform="rotate({rot} {cx} {cy})" fill="none" stroke="{col}" stroke-width="{sw}" opacity="{op}"/>'
    for a in dots:
        t=math.radians(a); x=rx*math.cos(t); y=ry*math.sin(t); r=math.radians(rot)
        px,py=cx+x*math.cos(r)-y*math.sin(r),cy+x*math.sin(r)+y*math.cos(r)
        o+=f'<circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="{GOLD}" opacity=".16"/><circle cx="{px:.1f}" cy="{py:.1f}" r="2" fill="{GOLD}"/>'
    return o
def spread(body,l,r,memo_l,memo_r,orb=''):
    o=f'<div class="sp">'+(svg(0,0,1190,842,orb) if orb else '')+body
    o+=A(48,806,f'{l:02d}',None,'fo')+A(1130,806,f'{r:02d}',None,'fo')
    o+=A(48,818,'台割メモ｜'+memo_l,480,'memo')+A(643,818,'台割メモ｜'+memo_r,480,'memo')
    return o+'<div class="a" style="left:595px;top:0;height:842px;border-left:.5px dashed #e3e6e9"></div></div>'
L=48; R=643; W=499
pages=[]
GLOBE_F='v8/gl_-28_-8_-10_1700_0.34.png'; GLOBE_B='v8/gl_138_-14_6_1700_0.2.png'

# =================== P02-03  Opening ===================
b=f'<img class="a" src="{uri(GLOBE_F,1500,"PNG")}" style="left:-150px;top:150px;width:720px;height:720px">'
b+=A(L,58,'MITSUBISHI CORPORATION　MINERAL RESOURCES GROUP',None,'lab')
b+=A(R,150,'Strength to Hold.<br>Power to Connect.',470,'en','font-size:40px;line-height:1.1')
b+=A(R,256,'',26,'',f'border-top:1px solid {RED}')
b+=A(R,270,'コアメッセージ（英文主体・和文は確認用）',None,'labj')
b+=BODY(R,290,300,92,'font-size:8.2px;line-height:1.8;color:#6c7279')
toc=[('01','Who We Are','我々は何者か｜三菱商事 金属資源グループ','04'),('02','What We Do','独自価値｜フットプリント・原料炭・銅・トレーディング・新技術','05'),('03','Why Partners Choose Us','選ばれ続ける理由｜Partner of Choice','10'),('04','Our Vision','何を実現するか｜外部環境と私たちの約束','11')]
b+=A(R,560,'CONTENTS',None,'lab')
for i,(n,e,j,p) in enumerate(toc):
    y=584+i*46
    b+=A(R,y,'',W-40,'',f'border-top:.5px solid {HAIR}')+A(R,y+9,n,None,'num','font-size:18px;color:'+GOLD)
    b+=A(R+44,y+8,e,None,'','font-size:11px;font-weight:300;letter-spacing:.2px')+A(R+44,y+24,j,None,'sm')+A(R+W-60,y+10,'P.'+p,None,'fo')
orb=f'<path d="M-80,640 C300,420 800,470 1210,500" fill="none" stroke="{GOLDL}" stroke-width=".6"/><path d="M-80,720 C380,540 860,540 1210,548" fill="none" stroke="{GOLD}" stroke-width=".7" opacity=".85"/><circle cx="905" cy="512" r="5" fill="{GOLD}" opacity=".16"/><circle cx="905" cy="512" r="2" fill="{GOLD}"/>'
pages.append(spread(b,2,3,'導入。B案の地球儀をそのまま扉に展開し、表紙→扉の連続性で「世界観」に入る。左ページは写真・図を置かずビジュアル1点で余白を確保。','コアメッセージと目次のみ。目次は4章構成（PwC様ストーリーライン準拠）。英文92語想定。',orb))

# =================== P04  Who We Are / P05 Global Footprint ===================
b,yy=HEAD(L,52,'01　WHO WE ARE','第1章　我々は何者か','From resource<br>to market.','三菱商事 金属資源グループとは','投資とトレーディングの両輪で、川上から川下までをつなぐ',size=30)
b+=BODY(L,yy+6,300,62)
# two-wheel value chain
vy=420; xs=[L+40,L+140,L+250,L+360,L+460]
st=[('x_vc_mine.jpg','Mine','資源開発・保有','50% 50%'),('_mr_project_06.png','Trade','トレーディング','50% 50%'),('x_vc_smelter.jpg','Smelt / Steel','製錬・製鉄','50% 40%'),('r-072.png','Trade','トレーディング','50% 50%'),('x_vc_ev.jpg','End use','最終製品・需要家','40% 50%')]
o=''
o+=f'<path d="M{xs[0]-L},{vy-30-300} Q{(xs[0]+xs[2])/2-L},{vy-110-300} {xs[2]-L},{vy-30-300}" fill="none"/>'
b+=svg(L,0,W,842,
  f'<path d="M{xs[0]-L},{vy-32} C{xs[0]-L+10},{vy-92} {xs[2]-L-10},{vy-92} {xs[2]-L},{vy-32}" fill="none" stroke="{GOLD}" stroke-width="1.1"/>'
  f'<path d="M{xs[0]-L},{vy+62} C{xs[0]-L+30},{vy+112} {xs[4]-L-30},{vy+112} {xs[4]-L},{vy+62}" fill="none" stroke="{BLUE}" stroke-width="1.1"/>'
  +''.join(f'<line x1="{xs[i]-L+30}" y1="{vy}" x2="{xs[i+1]-L-30}" y2="{vy}" stroke="{HAIR}" stroke-width=".8"/>' for i in range(4)))
for x,(f,e,j,p) in zip(xs,st):
    b+=CIRC(x,vy,52,f,p)+A(x-45,vy+34,e,90,'','text-align:center;font-size:7.2px;font-weight:400;letter-spacing:.3px')+A(x-45,vy+45,j,90,'sm','text-align:center')
b+=A(L+70,vy-108,'<b style="font-weight:500;color:'+GOLD+'">INVESTMENT</b>　資源投資｜鉄鋼原料本部・クリティカルミネラル本部',300,'sm')
b+=A(L+120,vy+104,'<b style="font-weight:500;color:'+BLUE+'">TRADING (RtM)</b>　トレーディング｜金属資源トレーディング本部',320,'sm')
# journey band
jy=596
b+=A(L,jy,'OUR JOURNEY',None,'lab')+A(L+86,jy,'時代を先読みし、事業モデルを変革してきた歩み',None,'sm')
b+=svg(L,jy+40,W,40,f'<line x1="0" y1="10" x2="{W}" y2="10" stroke="{GOLDL}" stroke-width=".8"/>'+''.join(f'<circle cx="{4+i*101}" cy="10" r="3" fill="{GOLD}"/>' for i in range(5)))
era=[('〜1990s','トレーディングに参入し、少数株主として出資'),('1990s','口銭モデルから投資モデルへ。JV運営の知見を蓄積'),('2000s','中国の成長を捉え、事業経営に関与（BHPと50:50）'),('2010s','原料炭偏重から脱却。資産価値の最大化へ'),('2020s〜','地域特化から、グローバルなトレーダーへ')]
for i,(y_,t) in enumerate(era):
    x=L+i*101; b+=A(x,jy+18,y_,None,'num','font-size:15px')+A(x,jy+60,t,92,'sm')
b+=A(L,jy+112,'Guided by the Three Corporate Principles of Mitsubishi Corporation — Corporate Responsibility to Society, Integrity and Fairness, Global Understanding through Business.',W,'bd','font-size:6.6px;color:'+MUTE)
b+=A(L,jy+132,'三綱領（所期奉公・処事光明・立業貿易）は一行で触れるに留め、図解しない',None,'memo')
# ---- P05 footprint
b2,yy=HEAD(R,52,'02　WHAT WE DO','第2章　独自価値','Where we work.','グローバル・フットプリント','多様な資源と地域で、事業と人の拠点を広げる',size=30)
b+=b2
MW=W+48; MH=MW*996/2600; my=262
b+=IMG(R-10,my,MW,MH,'v8/flat_std.png',fmt='PNG',light=.35,mx=1800)
P=lambda lon,lat:(R-10+(lon+170)/360*MW,my+(80-lat)/138*MH)
PRJ=[(-66.9,52.9),(-71.2,-28.5),(-70.6,-33.4),(148.3,-22.3),(-69.07,-24.27),(-70.5,-31.7),(-70.3,-33.15),(-77.05,-9.53),(-70.6,-17.1)]
DEV=[(-70.3,-22.9),(-110.9,31.9),(-128.9,58.5),(121.4,-30.7),(-94.0,51.6),(141.7,-13.3),(25.7,64.2),(-0.6,54.4)]
OFF=[(139.7,35.7),(103.8,1.3),(77.2,28.6),(-0.1,51.5),(-77.0,40.4),(55.3,25.2),(106.8,-6.2),(100.5,13.7),(-70.65,-33.45),(28.0,-26.2),(-58.4,-34.6),(-46.6,-23.5),(153.0,-27.5),(-77.0,-12.0),(-123.1,49.3),(121.5,31.2)]
o=''
for lo,la in OFF:
    x,y=P(lo,la); o+=f'<circle cx="{x-R+10:.1f}" cy="{y-my:.1f}" r="3.1" fill="{BLUE}" stroke="#fff" stroke-width=".8"/>'
for lo,la in DEV:
    x,y=P(lo,la); o+=f'<circle cx="{x-R+10:.1f}" cy="{y-my:.1f}" r="3.4" fill="#fff" stroke="{GOLD}" stroke-width="1.3"/>'
for lo,la in PRJ:
    x,y=P(lo,la); o+=f'<circle cx="{x-R+10:.1f}" cy="{y-my:.1f}" r="7" fill="{GOLD}" opacity=".18"/><circle cx="{x-R+10:.1f}" cy="{y-my:.1f}" r="3.4" fill="{GOLD}" stroke="#fff" stroke-width=".8"/>'
b+=svg(R-10,my,MW,MH,o)
ly=my+MH+8
b+=svg(R,ly,W,12,f'<circle cx="4" cy="5" r="3.4" fill="{GOLD}"/><circle cx="104" cy="5" r="3.4" fill="#fff" stroke="{GOLD}" stroke-width="1.3"/><circle cx="234" cy="5" r="3.1" fill="{BLUE}"/>')
b+=A(R+11,ly,'事業・資産',None,'sm')+A(R+111,ly,'開発・探鉱プロジェクト',None,'sm')+A(R+241,ly,'トレーディング拠点・金属資源の駐在',None,'sm')
# commodities
cy_=ly+40
b+=A(R,cy_,'OUR RESOURCES',None,'lab')
com=[('r-048.png','Metallurgical Coal','原料炭',1),('r-054.png','Copper','銅',1),('x_ironore.jpg','Iron Ore','鉄鉱石',0),('x_case_mine.jpg','Nickel','ニッケル',0),('x_lithium.jpg','Lithium','リチウム',0),('x_alu.jpg','Aluminium','アルミ・ボーキサイト',0),('r-074.png','Recycled','二次資源',0)]
x=R+20
for f,e,j,big in com:
    d=44 if big else 30; cx=x+d/2-10
    b+=CIRC(cx+10,cy_+48,d,f,ring=bool(big))+A(cx-20,cy_+76,e,60,'','text-align:center;font-size:6.2px;font-weight:'+('500' if big else '300'))+A(cx-20,cy_+86,j,60,'sm','text-align:center;font-size:5.8px')
    x+=d+(30 if big else 26)
b+=A(R+150,cy_+2,'主力の2事業（原料炭・銅）は次の見開きで詳しく',None,'sm','color:'+GOLD)
orb=''
pages.append(spread(b,4,5,'第1章を1ページに集約。「投資×トレーディングの両輪」を写真付きの流れ図1点で示し、歩みは年代5点の帯に。7グループ一覧・ポートフォリオ％・組織図は外す（落とし項目リスト参照）。','第2章の扉＝全体像。議事録「章の頭に全体像→主力2つ」に対応。拠点・駐在（青）を追加し、名称は入れない。開いたまま商談で使える“フットプリント”ページとして単体でも成立。',orb))

# =================== P06 Coal / P07 Copper (two pillars) ===================
hh=330
b=IMG(0,0,595,hh,'r-047.png','50% 45%',mx=1600)+IMG(595,0,595,hh,'r-054.png','50% 60%',mx=1600)
b+=A(0,hh-90,'',1190,'','height:90px;background:linear-gradient(180deg,rgba(255,255,255,0),rgba(255,255,255,.0))')
b+=A(L,40,'02　WHAT WE DO｜PILLAR 1',None,'lab','color:#fff;text-shadow:0 0 6px rgba(0,0,0,.35)')+A(R,40,'02　WHAT WE DO｜PILLAR 2',None,'lab','color:#fff;text-shadow:0 0 6px rgba(0,0,0,.35)')
b+=A(L,hh+30,'World-class<br>metallurgical coal.',W,'en','font-size:28px')
b+=A(L,hh+102,'',26,'',f'border-top:1px solid {RED}')+A(L,hh+112,'原料炭事業',None,'jt')+A(L,hh+129,'鉄の主原料“産業のコメ”を、世界最高品位で届ける',None,'js')
kp=[('~50<span style="font-size:16px">%</span>','一級強粘炭の供給に占める<br>BMAのシェア'),('~20<span style="font-size:16px">%</span>','原料炭の海上輸出市場<br>シェア'),('60<span style="font-size:16px">+ yrs</span>','炭鉱寿命。<br>港湾・鉄道まで自社保有')]
for i,(n,t) in enumerate(kp):
    x=L+i*168; b+=A(x,hh+170,'',150,'',f'border-top:.6px solid {GOLD}')+A(x,hh+182,n,None,'num','font-size:34px')+A(x,hh+224,t,150,'sm')
b+=BODY(L,hh+270,250,70)
# Bowen basin mini map
import landsvg
mx,my2,mw,mh=L+290,hh+262,200,150
mh=165
reg=landsvg.region(112,155,-44,-10,mw,mh)
bx=(148.3-112)/43*mw; by=(-10+22.3)/34*mh
b+=svg(mx,my2,mw,mh,f'<path d="{reg}" fill="#dfe7ef"/><circle cx="{bx:.1f}" cy="{by:.1f}" r="14" fill="{GOLD}" opacity=".18"/><circle cx="{bx:.1f}" cy="{by:.1f}" r="3.6" fill="{GOLD}"/>')
b+=A(mx+bx-62,my2+by-22,'Bowen Basin',None,'','font-size:6.4px;font-weight:500')+A(mx+bx-62,my2+by-12,'Queensland',None,'cap')
b+=A(mx,my2+mh+4,'BHPとの50:50合弁（BMA）。1968年 MDP設立／2001年 BMA組成',mw,'sm')
# copper right
b+=A(R,hh+30,'The world\'s largest<br>non-operating copper producer.',W+10,'en','font-size:28px')
b+=A(R,hh+102,'',26,'',f'border-top:1px solid {RED}')+A(R,hh+112,'銅事業',None,'jt')+A(R,hh+129,'自社操業を伴わずに、世界最大級の銅ポジションを築く',None,'js')
kp=[('No.1','ノンオペレーターとして<br>世界最大の銅生産者'),('5 / 5','参画する主要5鉱山すべてが<br>世界Top15'),('Top 25<span style="font-size:16px">%</span>','平均コストは世界の<br>上位25%に位置')]
for i,(n,t) in enumerate(kp):
    x=R+i*168; b+=A(x,hh+170,'',150,'',f'border-top:.6px solid {GOLD}')+A(x,hh+182,n,None,'num','font-size:34px')+A(x,hh+224,t,150,'sm')
# andes mini map with mines
mx,my2,mw,mh=R,hh+262,150,170
reg=landsvg.region(-84,-54,-37,-3,mw,mh)
PJ=lambda lo,la:((lo+84)/30*mw,(-3-la)/34*mh)
mines=[('Antamina',-77.05,-9.53),('Quellaveco',-70.6,-17.1),('Escondida',-69.07,-24.27),('Marimaca',-70.3,-22.9),('Los Pelambres',-70.5,-31.7),('Anglo American Sur',-70.3,-33.15)]
o=f'<path d="{reg}" fill="#dfe7ef"/>'
for n,lo,la in mines:
    x,y=PJ(lo,la); o+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{GOLD}" stroke="#fff" stroke-width=".7"/>'
b+=svg(mx,my2,mw,mh,o)+A(mx+mw-46,my2-2,'',50,'','height:'+str(mh+4)+'px;background:linear-gradient(90deg,rgba(255,255,255,0),#fff 85%)')+A(mx-2,my2+mh-30,'',mw+4,'','height:32px;background:linear-gradient(180deg,rgba(255,255,255,0),#fff 90%)')
for n,lo,la in mines:
    x,y=PJ(lo,la); b+=A(mx+x-6-len(n)*3.1,my2+y-4,n,None,'','font-size:5.6px;color:'+SUB+';white-space:nowrap')
b+=A(mx,my2+mh+4,'チリ・ペルーを中心に参画（ほか米国 Copper World）',200,'sm')
four=[('Tier 1 assets','規模で世界上位の優良鉱山に参画'),('Partnerships with majors','特定1社に偏らず、主要メジャーと協業'),('Trading relationships','販売を通じ、業界の幅広い関係を構築'),('New technology','業界のボトルネックに挑む技術へ投資')]
for i,(e,j) in enumerate(four):
    y=hh+268+i*42; b+=A(R+250,y,f'0{i+1}',None,'num','font-size:13px;color:'+GOLD)+A(R+272,y,e,None,'','font-size:8px;font-weight:400')+A(R+272,y+12,j,200,'sm')
pages.append(spread(b,6,7,'主力① 原料炭。上半分を写真、下半分を「数字3つ＋地図1点」に整理。出資構成図・生産量表は外し、数字は変動しにくいシェア・寿命に限定。','主力② 銅。鉱山一覧表を地図に置き換え、強みは4項目を1行ずつ。ランキング棒グラフは「No.1（ノンオペレーター）」の数字1点に集約。原料炭と見開きで対になるよう同じ型で組む。',''))

# =================== P08 RtM / P09 New technology ===================
b,yy=HEAD(L,52,'02　WHAT WE DO｜TRADING','第2章　独自価値','Resource to Market.','トレーディング事業（RtM）','一つの商品の中で、投資から販売までを一気通貫でつなぐ',size=30)
nb=[('15','industries','業界'),('50','countries','カ国'),('~1,000','customers','社の販売先')]
for i,(n,e,j) in enumerate(nb):
    x=L+i*150+(18 if i else 0); b+=A(x,yy+14,n,None,'num','font-size:38px')+A(x,yy+56,e.upper(),None,'cap')+A(x,yy+66,j,None,'sm')
    if i<2: b+=A(x+(110 if i==0 else 108),yy+24,'×',None,'','font-size:18px;font-weight:200;color:'+GOLD)
# functions ring
cx,cy=L+150,440; RR=92
o=f'<circle cx="{cx-L}" cy="{cy-340}" r="{RR}" fill="none" stroke="{GOLDL}" stroke-width=".8"/><circle cx="{cx-L}" cy="{cy-340}" r="40" fill="{GLASS}"/>'
b+=svg(L,340,300,220,o)
b+=A(cx-40,cy-12,'RtM',80,'','text-align:center;font-size:16px;font-weight:300;color:'+DEEP)+A(cx-40,cy+8,'Functions',80,'cap','text-align:center')
fn=[('Marketing &amp;<br>Procurement','販売・調達'),('Logistics','物流'),('Financing','ファイナンス'),('Risk<br>Management','リスク管理'),('Carbon<br>Reduction','脱炭素')]
for i,(e,j) in enumerate(fn):
    a=math.radians(-90+i*72); x=cx+RR*math.cos(a); y=cy+RR*math.sin(a)
    b+=f'<div class="a" style="left:{x-26}px;top:{y-26}px;width:52px;height:52px;border-radius:50%;background:#fff;border:.8px solid {GOLD};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center"><div style="font-size:5.8px;font-weight:400;line-height:1.2">{e}</div><div class="sm" style="font-size:5.4px">{j}</div></div>'
b+=A(L+80,575,'お客様に提供できる5つの機能',150,'smb','text-align:center')
# business model
bx=L+320; by=345
b+=A(bx,by,'BUSINESS MODEL',None,'lab')
bm=[('MC Assets ＋ Third-party','MC保有資産と第三者取引の両方を扱う'),('Stable supply','資源確保による安定供給'),('Market intelligence','市場・業界動向の発信と知見共有で、事業機会を発掘'),('Continuous value','トレーディング機能の強化で、付加価値を生み続ける')]
for i,(e,j) in enumerate(bm):
    y=by+22+i*52; b+=A(bx,y,'',180,'',f'border-top:.6px solid {HAIR}')+A(bx,y+8,e,180,'','font-size:8.4px;font-weight:300')+A(bx,y+22,j,180,'sm')
b+=svg(bx-14,by+22,10,200,f'<line x1="5" y1="0" x2="5" y2="200" stroke="{GOLD}" stroke-width=".8"/><path d="M1,194 L5,202 L9,194" fill="none" stroke="{GOLD}" stroke-width=".8"/>')
b+=A(L,640,'',W,'',f'border-top:.6px solid {HAIR}')+A(L,652,'グローバルネットワーク 10拠点：Singapore・Japan・India・China・USA・UK・UAE・Indonesia・Thailand・Chile',W,'sm','color:'+MUTE)
# ---- P09 new tech
b2,yy=HEAD(R,52,'02　WHAT WE DO｜NEW TECHNOLOGY','第2章　独自価値','Investing in<br>what\'s next.','新技術への取り組み','銅・クリティカルミネラルを中心に、原料炭まで。業界のボトルネックに挑む技術へ投資する',size=30)
b+=b2+BODY(R,yy+6,300,55)
# loop chain
cy=520; cx=R+235; rx,ry=190,92
b+=svg(R,cy-140,W,280,f'<ellipse cx="{cx-R}" cy="140" rx="{rx}" ry="{ry}" fill="none" stroke="{GOLDL}" stroke-width=".9"/>')
stg=[(180,'Mine','採掘'),(232,'Process','選鉱・浸出'),(308,'Smelt &amp; Refine','製錬・精製'),(0,'End use','電化・再エネ・AI/DC'),(110,'Recycle','リサイクル')]
for a,e,j in stg:
    t=math.radians(a); x=cx+rx*math.cos(t); y=cy+ry*math.sin(t)
    b+=f'<div class="a" style="left:{x-4}px;top:{y-4}px;width:8px;height:8px;border-radius:50%;background:{GOLD}"></div>'
    ox=-70 if math.cos(t)<-.3 else (8 if math.cos(t)>.3 else -30); oy=-24 if math.sin(t)<0 else 8
    b+=A(x+ox,y+oy,f'<b style="font-weight:400;font-size:7px;color:{INK}">{e}</b><br>{j}',80,'sm')
chips=[(cx-120,cy-48,'CiDRA','選鉱｜回収率・処理能力を向上','Copper'),(cx+20,cy-48,'Jetti','浸出｜触媒で硫化鉱から回収','Copper'),(cx-120,cy+14,'DESCycle','リサイクル｜電子スクラップから銅・貴金属を回収','Recycling'),(cx+20,cy+14,'〇〇〇〇','原料炭｜生産性・脱炭素の技術（MC様ご確認）','Coal')]
for x,y,n,d,t in chips:
    b+=A(x,y,f'<div style="font-size:5.4px;letter-spacing:1.2px;color:{GOLD}">{t.upper()}</div><div style="font-size:9px;font-weight:400">{n}</div><div class="sm" style="font-size:5.8px">{d}</div>',128,'',f'height:50px;padding:6px 8px;background:rgba(255,255,255,.9);border:.6px solid {HAIR};border-radius:3px')
b+=A(R,690,'CVCは「銅のバリューチェーン」に限定せず、「新技術への取り組み」として資源横断で示す（議事録対応）',W,'memo')
orb=''
pages.append(spread(b,8,9,'議事録対応：「1つから買って多数に売る」ハブ図は削除。営業視点で「何ができるか＝5つの機能」と「ビジネスモデル」に絞る。数字は15×50×1,000の1行で規模を伝える。','CVCを「新技術」の枠で再定義。銅中心＋原料炭・リサイクルにも触れる。循環する軌道線＝表紙の金の軌道と同じモチーフで、技術がつながりを生む姿を示す。',orb))

# =================== P10 Partner of Choice / P11 Vision ===================
b=IMG(0,0,595,300,'r-084.png','50% 35%',mx=1600)
b+=A(L,40,'03　WHY PARTNERS CHOOSE US',None,'lab','color:#fff;text-shadow:0 0 6px rgba(0,0,0,.4)')
b+=A(L,330,'Partner of choice.',W,'en','font-size:30px')
b+=A(L,374,'',26,'',f'border-top:1px solid {RED}')+A(L,384,'第3章　選ばれ続ける理由',None,'jt')+A(L,401,'資源業界に不可欠な存在として、世界のトッププレイヤーから選ばれ続ける',None,'js')
st4=[('Cultural affinity with the majors','資源メジャーとの企業文化的親和性'),('JV management capability','資源投資経験に裏打ちされたJV経営力'),('Sound financial base','事業ポートフォリオを活かした健全な財務基盤'),('Deep insight','マクロ環境とバリューチェーンに対する深い知見')]
for i,(e,j) in enumerate(st4):
    x=L+(i%2)*255; y=440+(i//2)*96
    b+=A(x,y,f'0{i+1}',None,'num','font-size:28px;color:'+GOLD)+A(x+44,y+2,e,200,'','font-size:9px;font-weight:400')+A(x+44,y+17,j,200,'sm')+BODY(x+44,y+32,196,22,'font-size:6.4px;line-height:1.6')
b+=A(L,650,'',W,'',f'border-top:.6px solid {HAIR}')
b+=A(L,662,'JOINT VENTURES WITH INDUSTRY LEADERS',None,'lab')+A(L,676,'業界最大手とのJV実績',None,'sm')
for i,n in enumerate(['BHP','Rio Tinto','Anglo American']):
    b+=A(L+230+i*92,666,n,None,'','font-size:13px;font-weight:300;letter-spacing:.3px')
b+=A(L,704,'単なる共同出資者に留まらず、人材派遣・ガバナンス参画・総合力でJVの事業価値を最大化',W,'sm')
# ---- P11 vision
b+=A(R,52,'04　OUR VISION',None,'lab')+A(R,63,'第4章　何を実現するか',None,'labj')
b+=A(R,86,'Building the future<br>of resources, together.',W,'en','font-size:30px')
b+=A(R,162,'',26,'',f'border-top:1px solid {RED}')+A(R,172,'共に、資源の未来を築く',None,'jt')+A(R,189,'クリティカルミネラルを取り巻く外部環境に、安定供給と効率的な供給の両面で応える',None,'js')
# three forces converging
cy=330; cxs=[R+80,R+250,R+420]
fz=[('Demand shift','産業構造の転換<br>人口増・電化による需要拡大'),('Supply constraints','供給制約の深刻化'),('Geopolitics','地政学リスクの常態化')]
for x,(e,j) in zip(cxs,fz):
    b+=f'<div class="a" style="left:{x-58}px;top:{cy-58}px;width:116px;height:116px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#fff 0%,{GLASS} 55%,#cfdce9 100%);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center"><div style="font-size:8.4px;font-weight:400">{e}</div><div class="sm" style="font-size:6px;margin-top:3px">{j}</div></div>'
b+=svg(R,cy+62,W,60,f'<path d="M80,0 Q250,46 250,46 M420,0 Q250,46 250,46" fill="none" stroke="{GOLD}" stroke-width=".8"/><circle cx="250" cy="46" r="3" fill="{GOLD}"/>')
b+=A(R,cy+114,'サプライチェーン確保の重要性と、川上資源への参入障壁が増大',W,'smb','text-align:center')
# mission
b+=A(R,500,'OUR COMMITMENT',None,'lab')
b+=A(R,518,'“To contribute to a better society by providing a stable supply of high-quality mineral resources that society needs, in a sustainable way.”',W-20,'en','font-size:15px;line-height:1.45;font-weight:200')
b+=A(R,586,'「社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する」',W,'sm')
b+=f'<img class="a" src="{uri(GLOBE_B,700,"PNG")}" style="left:{R+W-150}px;top:640px;width:150px;height:150px">'
b+=A(R,660,'CONTACT',None,'lab')+A(R,676,'Mitsubishi Corporation　Mineral Resources Group<br>2-3-1 Marunouchi, Chiyoda-ku, Tokyo 100-8086, Japan<br>www.mitsubishicorp.com',260,'','font-size:7px;line-height:1.7;font-weight:300;color:'+SUB)
b+=A(R,734,'お問い合わせ先は残す（議事録：要否は保留）。裏表紙へ移す案も可',None,'memo')
orb=orbit(1068,718,120,34,-14,(150,),GOLD,.7,.9)
pages.append(spread(b,10,11,'Partner of Choiceは1ページで完結。4つの強み＝本文、JV実績＝社名テキスト1行。前回の「評価される理由」（強みと重複）は削除。','外部環境→私たちの約束→連絡先、の3段。冒頭P.02の地球儀を小さく再登場させ、冊子を閉じる。',orb))

links=''.join(f'<link rel="stylesheet" href="f/nsjp/package/{w}.css">' for w in (300,400,500))
open('daiwari_v8.html','w').write('<!doctype html><meta charset=utf-8>'+links+'<style>'+CSS+'</style>'+''.join(pages))
