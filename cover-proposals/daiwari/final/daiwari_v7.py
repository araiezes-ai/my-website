import base64, io
from PIL import Image
N='f/ns/package/files/'
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
_c={}
def uri(f,fit=None):
    if f not in _c:
        im=Image.open('img/'+f).convert('RGB'); im.thumbnail((1200,1200)); bf=io.BytesIO(); im.save(bf,'JPEG',quality=82)
        _c[f]='data:image/jpeg;base64,'+base64.b64encode(bf.getvalue()).decode()
    return _c[f]
CSS=f"""@font-face{{font-family:NS;font-weight:300;src:url(data:font/woff2;base64,{b64(N+'noto-sans-latin-300-normal.woff2')})}}
@font-face{{font-family:NS;font-weight:400;src:url(data:font/woff2;base64,{b64(N+'noto-sans-latin-400-normal.woff2')})}}
@page{{size:420mm 297mm;margin:0}}*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:NS,'Noto Sans JP',sans-serif;color:#222;background:#fff}}
.sp{{position:relative;width:1190px;height:842px;overflow:hidden;background:#fff;page-break-after:always;zoom:1.3333}}
.sp:after{{content:"";position:absolute;left:595px;top:0;bottom:0;border-left:1px dashed #d5d8db}}
.a{{position:absolute}}
.hd{{font-size:7.4px;letter-spacing:1.2px;color:#555;font-weight:400}}
.ps{{font-size:6.6px;color:#777;border:.5px solid #aaa;border-radius:8px;padding:1px 7px;letter-spacing:.5px}}
.t1{{font-size:18px;font-weight:300;line-height:1.4;letter-spacing:.8px}}
.t2{{font-size:10px;font-weight:400;line-height:1.55;color:#444;letter-spacing:.3px}}
.lb{{font-size:6px;color:#666;letter-spacing:.6px}}
.x{{font-family:'Noto Sans JP';font-weight:300;color:#9aa0a6;word-break:break-all;line-break:anywhere}}
.cnt{{font-size:5.8px;color:#b0b4b8;letter-spacing:.3px}}
.gb{{background:#eef0f2;border:.6px dashed #b6bbc0;display:flex;align-items:center;justify-content:center;text-align:center;padding:6px}}
.gb span{{font-size:7px;color:#6a7076;line-height:1.5}}
.nt{{font-size:6.2px;color:#9a5a60;line-height:1.5}}
.kf{{font-size:20px;font-weight:300;line-height:1.1}}
.bx{{border:.6px solid #9aa0a6;font-size:7.4px;text-align:center;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1.35;padding:3px}}
.fo{{font-size:6.6px;letter-spacing:1.4px;color:#999}}
"""
def A(x,y,h,w=None,c='',s=''):
    return f'<div class="a {c}" style="left:{x}px;top:{y}px;{f"width:{w}px;" if w else ""}{s}">{h}</div>'
def FIG(x,y,w,h,f,cap):
    return ph(x,y,w,h,f,None,'contain')+A(x,y,'',w,'',f'height:{h}px;border:.6px solid #c9cdd1')+A(x,y+h+3,cap,w,'lb','font-size:6.2px;color:#666')
def TAG(x,y,t): return A(x,y,t,None,'',"font-size:6.2px;color:#fff;background:#2a6fb0;padding:1px 5px;border-radius:2px;letter-spacing:.3px")
def TAG0(x,y,t): return A(x,y,t,None,'',"font-size:6.2px;color:#fff;background:#2a6fb0;padding:1px 5px;border-radius:2px")
def X(x,y,w,n,size=7.8,lh=1.75,tag='本文'):
    return A(x,y,'Ｘ'*n,w,'x',f'font-size:{size}px;line-height:{lh}')+''
def XC(x,y,w,n,size=7.8,lh=1.75,tag='本文'):
    per=max(1,int(w//size)); lines=-(-n//per)
    return X(x,y,w,n,size,lh)+A(x,y+lines*size*lh+1,f'▸{tag} {n}字／英語 約{round(n*0.55)}語',None,'cnt')
def T(x,y,title,sub,w=480):
    return A(x,y,title,w,'t1')+A(x,y+28+(title.count('<br>')*25),sub,w,'t2')
def gb(x,y,w,h,label): return A(x,y,f'<span>{label}</span>',w,'gb',f'height:{h}px')
def ph(x,y,w,h,f,cap=None,fit='cover'):
    o=A(x,y,f'<img src="{uri(f)}" style="width:{w}px;height:{h}px;object-fit:{fit};display:block">',w)
    if cap: o+=A(x,y+h+3,cap,w,'lb')
    return o
def rule(x,y,w,c='#cfd2d5'): return f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;border-top:.6px solid {c}"></div>'
def nt(x,y,t,w=480): return A(x,y,'※'+t,w,'nt')
def hd(x,chap,psy): return A(x,34,chap,None,'hd')+A(x+430,32,'読み手の心理：'+psy,None,'ps')
def lbl(x,y,t): return A(x,y,t,None,'lb',"font-weight:400;color:#444")
def spread(b,l,r):
    return f'<div class="sp">{b}'+A(48,808,f'{l:02d}',None,'fo')+A(1123,808,f'{r:02d}',None,'fo')+A(300,808,'台割 完成版（構成確認用・PwC様レビュー10/2反映）— 青ラベル＝改善点／本文は日本語字数、英語語数は目安',None,'fo','letter-spacing:.5px;background:#fff;padding:1px 4px')+'</div>'
L=48; R=643; W=499
pages=[]
A1="資源は、そこに「ある」だけでは、まだ価値ではありません。誰かが見出し、育て、必要とする場所へ届けて、はじめて力になる。私たちは、世界有数の資産に関わり、投資とトレーディングの両輪で川上から川下までをつなぎます。フェアな立場だからこそ、埋められる隙間がある。多様なパートナーと使い手の間に立ち、その時々の最適解を導く。世界に眠る価値を、社会の力へ。"

# ===== P02-03 : 導入（コアメッセージ＋目次）=====
b=A(0,0,'',1190,'',"height:842px;background:#e6e8eb")+A(40,360,'<b style="font-size:13px;font-weight:400">見開きビジュアル（イラスト／写真）</b><br>選定された表紙案の表現に合わせて決定',560,'',"font-size:8px;color:#555;line-height:1.7")+A(40,410,'表紙案①の場合：鋼のヘアライン（細い線）で描いた世界地図・拠点から立ち上がる線<br>表紙案②の場合：ガラスの地球儀と金色の軌道線<br>表紙案③の場合：鉱山写真を短冊状に再構成したビジュアル',560,'',"font-size:7.6px;color:#555;line-height:1.9")+A(40,470,'※台割は表紙3案のいずれにも寄せないため、ここではグレーの枠のみ。構成（コアメッセージ・ビジュアル・目次を1見開きに置くこと）はPwC様の台割ver.0（P1–P2）に準拠',560,'nt')
b+=A(36,40,'',440,'',"height:290px;background:#fff")
b+=A(56,58,'導入｜コアメッセージ',None,'hd')+A(56+330,56,'読み手の心理：興味',None,'ps')
b+=A(56,80,'Strength to Hold.<br>Power to Connect.',400,'t1','font-size:26px;line-height:1.2;font-weight:300')
b+=A(56,146,'参考訳：持つ力と、つなぐ力。',None,'lb')+TAG0(190,146,'英文を主に')
b+=A(56,164,"Xxxxxxxxx, xx xxxxx xxx, xx xxx xxxx xxxxx. Xx xxxxx xxxxxxx xx xxxxxxxx xxxx, xxxxxxx xxxx, xxx xxxxxxx xxxx xx xxxxx xxxx'xx xxxxxx. Xxxx xxxx xx xxxx xxxxxx xxxx xxxxx. Xx xxxxxx xxxx xxxxx-xxxxx xxxxxx, xxxxxxxxxx xxx xxxxx xxxxx xxxx xxxxxxxx xx xxxxxxxxxx xxxxxxx xxxxxxxxxx xxx xxxxxxx. Xxxxxxx xx xxxxx xx xxxx xxxxxx, xx xxx xxxxxx xxxx xxxxxx xxxxxx. Xxxxxxx xx xxxxx xxxxxxx xxxxxxx xxxxxxxx xxx xxxxx, xx xxxx xxx xxxxx xxxxxx xxx xxxxx xxxxxx. Xxxxxxx xx xxxx xxx xxxxxx, xx xxxx xxx xxxxx xxxxxxx xx xxx xxxxx xxxx xxxxx xxx xxxxxxx.",400,'x','font-family:NS;font-size:8.6px;line-height:1.7;word-break:normal;line-break:auto')
b+=A(56,262,'▸コアメッセージ本文（英文）92語／547字（A-1案と同量）',None,'cnt')
b+=nt(56,278,'最新版のコアメッセージに差し替え予定（PwC様レビューNo.2）。現在はA-1ブラッシュアップ案を仮置き。英語版冊子のため英文を主とし、和文は社内確認用の参考訳',400)
b+=A(700,26,'',430,'',"height:20px")
b+=A(56+620,460,'',470,'',"height:340px;background:#fff")
b+=A(696,478,'目次',None,'t1')
toc=[('導入','コアメッセージ','02'),('第1章','WHO｜我々は何者か　—　三菱商事・金属資源グループとは：全体像・歩み','04'),('第2章','HOW/WHAT｜独自価値　—　機能・強み','06'),('第3章','PROOF｜選ばれ続ける理由　—　実績・関係・評価','10'),('第4章','VISION｜何を実現するか　—　社会課題への取り組み','11')]
for i,(c,t,p) in enumerate(toc):
    y=520+i*44; b+=rule(696,y,420)+A(696,y+8,c,None,'lb')+A(746,y+7,t,330,'',"font-size:9.5px;font-weight:300;line-height:1.4")+A(1096,y+8,p,None,'fo')
pages.append(spread(b,2,3))

# ===== helpers v4 =====
import math as _m, landsvg
def svg(x,y,w,h,inner): return f'<svg class="a" style="left:{x}px;top:{y}px;overflow:visible" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{inner}</svg>'
def BX(x,y,w,h,html,s=''): return A(x,y,html,w,'bx',f'height:{h}px;{s}')
def VL(x,y,h,c='#888',wd=.8): return f'<div class="a" style="left:{x}px;top:{y}px;height:{h}px;border-left:{wd}px solid {c}"></div>'
def HL(x,y,w,c='#888',wd=.8): return f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;border-top:{wd}px solid {c}"></div>'
def SM(x,y,t,w=None,s=''): return A(x,y,t,w,'',"font-size:6.4px;color:#555;line-height:1.45;"+s)
def H3(x,y,t,w=None): return A(x,y,t,w,'',"font-size:9px;font-weight:400;color:#222")
def XS(x,y,w,n): return X(x,y,w,n,5.6,1.5)
def SRC(x,y,t,w=W): return A(x,y,'図の出典・簡略化元：'+t,w,'',"font-size:5.6px;color:#888")
DK='#3c4045'; MD='#8a9096'; LT='#d6d9dd'; BG='#f1f2f4'

# ===== P04-05 v4 =====
b=hd(L,'第1章　WHO｜我々は何者か　—　三菱商事・金属資源グループとは','理解')
b+=T(L,60,'三菱商事とは','三綱領に基づき、経済価値・環境価値・社会価値の同時実現を志す総合商社')
b+=XC(L,108,230,90)
# three values triangle
cx,cy=L+372,166
o=''
for (dx,dy) in [(0,-36),(-50,24),(50,24)]:
    o+=f'<circle cx="{cx-L-250+dx:.0f}" cy="{cy-104+dy:.0f}" r="23" fill="{BG}" stroke="{MD}" stroke-width=".6"/>'
b+=svg(L+250,104,249,120,o)
for (dx,dy,t) in [(0,-36,'経済価値'),(-50,24,'環境価値'),(50,24,'社会価値')]:
    b+=A(cx+dx-30,cy+dy-5,t,60,'',"font-size:7.6px;text-align:center;font-weight:400")
b+=A(cx-34,cy-4,'3つの価値の<br>同時実現',68,'',"font-size:6.4px;text-align:center;color:#555;line-height:1.3")
b+=SRC(L+264,240,'金属資源G_P46（Core Principles &amp; Vision）',235)
b+=ph(L,212,86,46,'r-000.png',None,'contain')
for i,(k,r,m) in enumerate([('所期奉公','しょきほうこう','事業を通じ、社会に貢献する'),('処事光明','しょじこうめい','公明正大で品格ある行動'),('立業貿易','りつぎょうぼうえき','グローバルな視野で事業を展開')]):
    x=L+104+i*48
b+=SM(L,262,'三綱領',96)
for i,(k,m) in enumerate([('所期奉公','事業を通じ、社会に貢献する'),('処事光明','公明正大で品格ある行動'),('立業貿易','グローバルな視野で事業を展開')]):
    x=L+104+i*48
for i,(k,m) in enumerate([('所期奉公','社会への貢献'),('処事光明','公明正大'),('立業貿易','グローバルな視野')]):
    b+=BX(L+92+i*56,212,52,46,f'<b style="font-weight:400;font-size:7px">{k}</b><span style="font-size:5.6px;color:#777">{m}</span>')
b+=nt(L,240+0,'',1) if False else ''
b+=A(L,280,'全社の事業グループ（7グループ）',None,'',"font-size:7.6px;font-weight:400")
G7=['エネルギー&amp;パワー<br>ソリューション','マテリアル<br>ソリューション','金属資源','社会インフラ','モビリティ','食品産業','S.L.C.']
for i,g in enumerate(G7):
    hl=(g=='金属資源')
    b+=BX(L+i*71.3,296,68,30,g,f"font-size:6px;line-height:1.25;{'background:'+DK+';color:#fff;border-color:'+DK if hl else ''}")
b+=nt(L,332,'三綱領と「3つの価値の同時実現」を示す（PwC様レビューNo.3）。グループ構成は三菱商事公式サイトの7グループ（同No.4）。金属資源Gのみ濃色で示し、他は等価に並べる',W)
b+=rule(L,354,W)
b+=T(L,364,'金属資源グループの位置付け・役割','三菱商事の中で、金属資源グループが担う位置付けと役割')
b+=XC(L,410,230,80)
# donut
seg=[('金属資源',20,DK),('食料資源',10,'#b9bec4'),('C to B VC',10,'#a5abb2'),('基盤事業',30,'#c9cdd2'),('エネルギーVC',30,'#dcdfe2')]
o=''; a0=-90; R1,R2=48,30; cxx,cyy=60,62
for n,v,c in seg:
    a1=a0+v*3.6; la=1 if v*3.6>180 else 0
    p=lambda r,a:(cxx+r*_m.cos(_m.radians(a)),cyy+r*_m.sin(_m.radians(a)))
    x1,y1=p(R1,a0); x2,y2=p(R1,a1); x3,y3=p(R2,a1); x4,y4=p(R2,a0)
    o+=f'<path d="M{x1:.1f},{y1:.1f} A{R1},{R1} 0 {la} 1 {x2:.1f},{y2:.1f} L{x3:.1f},{y3:.1f} A{R2},{R2} 0 {la} 0 {x4:.1f},{y4:.1f}Z" fill="{c}" stroke="#fff" stroke-width="1"/>'
    a0=a1
b+=svg(L+250,404,124,124,o)
b+=A(L+250+60-28,404+52,'約14兆円',56,'',"font-size:7.4px;text-align:center;font-weight:400")+A(L+250+60-28,404+64,'投融資残高',56,'',"font-size:5.4px;text-align:center;color:#777")
for i,(n,v,c) in enumerate(seg):
    y=414+i*20
    b+=A(L+384,y+2,'',8,'',f"height:8px;background:{c}")+A(L+396,y,f'{n}　約{v}%',110,'',f"font-size:7px;{'font-weight:500' if i==0 else 'color:#555'}")
b+=SRC(L+250,532,'Investor Day P6（ポートフォリオ構成・2026年度見通し）',249)
b+=A(L,500,'グループミッション',None,'',"font-size:7.6px;font-weight:400")
b+=A(L,514,'「社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する」',230,'',"font-size:8.2px;font-weight:300;line-height:1.6")
b+=nt(L,548,'収益面は事実ベースで表示し、誇示する表現は避ける（PwC様レビューNo.4）',W)
b+=A(L,572,'組織図・事業体制',None,'',"font-size:10px;font-weight:400")+TAG(L+84,574,'改善① 移動')
b+=A(L,588,'投資を担う2本部と、トレーディングを担う1本部',None,'t2','font-size:8.4px')
b+=BX(L+190,606,120,18,'グループCEO')+BX(L+380,606,110,18,'グループCEOオフィス','border-style:dashed')
b+=VL(L+250,624,8)+HL(L+85,632,340)
for i,(n,k) in enumerate([('鉄鋼原料本部','投資'),('クリティカルミネラル本部','投資'),('金属資源トレーディング本部','トレーディング')]):
    x=L+10+i*170; b+=VL(x+75,632,8)+BX(x,640,150,26,f'{n}<span style="color:#888;font-size:5.8px">（{k}）</span>')
b+=A(L,676,'主要関係会社',None,'',"font-size:7px;color:#444")
for i,(n,d) in enumerate([('MDP','原料炭'),('MCI','南米の銅・鉄鉱石'),('MCIP','ペルーの銅'),('RtM','トレーディング'),('Triland Metals','金属取引（ブローカー・ヘッジ）')]):
    b+=BX(L+i*100,690,94,30,f'<b style="font-weight:400">{n}</b><span style="color:#888;font-size:5.6px">{d}</span>')
b+=nt(L,728,'本部長名などの個人名は記載しない（PwC様レビューNo.5）',W)

# ---- P05 ----
b+=hd(R,'第1章　WHO｜我々は何者か','理解')
b+=T(R,60,'金属資源グループの事業と機能の変遷','時代の変化を先読みし、事業モデルを変革してきた歩み')+TAG(R+330,66,'改善② 拡大')
b+=XC(R,108,W,60)
# simplified chart: years 1990-2025 across W
Y0,Y1=1988,2026; CW_=W; CH=62; top=150
X_=lambda y:(y-Y0)/(Y1-Y0)*CW_
coal=[(1990,52),(1995,50),(2000,42),(2003,52),(2005,120),(2007,100),(2008,300),(2009,128),(2011,290),(2013,140),(2015,90),(2017,190),(2019,170),(2020,120),(2021,215),(2022,365),(2024,250),(2025,190)]
cu=[(1990,110),(1995,120),(2000,80),(2003,80),(2006,300),(2007,320),(2009,234),(2011,400),(2013,330),(2016,220),(2018,290),(2020,280),(2021,423),(2023,390),(2025,450)]
pc=' '.join(f'{X_(y):.1f},{CH-v/420*CH:.1f}' for y,v in coal); pu=' '.join(f'{X_(y):.1f},{CH-v/480*CH:.1f}' for y,v in cu)
o=f'<polyline points="{pu}" fill="none" stroke="#b5bac0" stroke-width="1.2"/><polyline points="{pc}" fill="none" stroke="{DK}" stroke-width="1.2"/>'
o+=f'<line x1="0" y1="{CH}" x2="{CW_}" y2="{CH}" stroke="#aaa" stroke-width=".5"/>'
for yr in range(1990,2026,5): o+=f'<text x="{X_(yr):.1f}" y="{CH+8}" font-size="5.4" fill="#888" text-anchor="middle">{yr}</text>'
b+=svg(R,top+16,W,CH+10,o)
b+=A(R+330,top-12,'<span style="color:#3c4045">━</span> 原料炭価格　<span style="color:#b5bac0">━</span> 銅価格（推移の概形）',None,'',"font-size:5.8px;color:#666")
ev=[(1991,'冷戦終結・<br>日本が需要牽引'),(1999,'業界再編'),(2004.5,'中国台頭'),(2009,'世界金融危機'),(2016,'中国危機'),(2022,'脱炭素・地政学')]
for yr,t in ev: b+=A(R+X_(yr)-32,top+2,t,64,'',"font-size:5.6px;color:#777;text-align:center;line-height:1.3")
# milestones
ty=top+CH+38
b+=HL(R,ty,W,DK,1)
ms=[(1988,"'88 MEL<br>'97 MLP／'99 CMA参画"),(1992,"'92 IOC参画"),(2000,"'00 BMA組成"),(2011.5,"'11/12 AAQ・AAS参画<br>'12 RtM設立"),(2018,"'18 AAQ買増")]
for yr,t in ms:
    x=R+X_(yr); b+=A(x-3,ty-3,'',6,'',f"height:6px;border-radius:3px;background:{DK}")+A(x-2,ty+6,t,90,'',"font-size:6px;line-height:1.35;font-weight:400")
# eras
eras=[('〜1990年代','トレーディングに参入し、少数株主として出資'),('1990年代','口銭モデルから投資モデルへ。JV運営の知見を蓄積'),('2000年代','中国の成長を捉え、事業経営に関与（BHPと50:50）'),('2010年代','原料炭偏重から脱却。共同出資者に留まらず資産価値を最大化'),('2020年代〜','地域特化から、グローバルなトレーダーへ')]
ey=ty+34
for i,(e,t) in enumerate(eras):
    x=R+i*100.5; b+=A(x,ey,e,96,'',f"font-size:7px;font-weight:400;border-top:1.2px solid {DK};padding-top:3px")+SM(x,ey+16,t,94)+XS(x,ey+44,94,30)
b+=SRC(R,ey+72,'金属資源G_P30（主要金属資源権益の参画経緯）。価格推移は概形、案件・思惑は要点のみ抜粋')
b+=nt(R,ey+82,'案件の詳細には立ち入らず、一級資産への早期参画を「先見性」として前向きに表現（PwC様レビューNo.6）',W)
# value chain
vy=ey+104
b+=rule(R,vy-6,W)
b+=T(R,vy,'バリューチェーン全体像','投資と販売の両輪で、川上から川下までに関わる')
gy=vy+44
cols=[('鉱山',0,100),('トレーディング',104,64),('製鉄／製錬',172,110),('トレーディング',286,64),('最終製品／需要家',354,145)]
for n,x,w in cols:
    tr='トレ' in n
    b+=A(R+x,gy,n,w,'',f"height:16px;line-height:16px;text-align:center;font-size:7px;color:#fff;background:{MD if tr else DK}")
ry1,ry2,rh=gy+20,gy+20+74,70
rows=[(ry1,'鉱山会社','原料炭・鉄鉱石','鉄鋼原料本部','製鉄会社','鋼材','',('メタルワン','別グループ'),'建材・自動車用鋼板'),
      (ry2,'鉱山会社','銅鉱石・ボーキサイト','クリティカルミネラル本部','製錬会社','銅地金・アルミ地金','クリティカルミネラル本部',('RtM','金属資源トレーディング本部'),'電線・再エネ発電・EV内配線／モーター')]
for i,(y,a1,a2,a3,c1,c2,c3,(t1,t2),e) in enumerate(rows):
    b+=A(R-12,y+20,'鉄鋼' if i==0 else '非鉄金属',10,'',"font-size:6px;color:#555;line-height:1.2")
    b+=BX(R,y,100,rh,f'<b style="font-weight:400">{a1}</b><span style="font-size:6px">{a2}</span><span style="font-size:5.6px;color:#777">{a3}</span>','background:'+BG)
    b+=BX(R+172,y,110,rh,f'<b style="font-weight:400">{c1}</b><span style="font-size:6px">{c2}</span><span style="font-size:5.6px;color:#777">{c3}</span>','background:'+BG)
    b+=BX(R+286,y,64,rh,f'<b style="font-weight:400">{t1}</b><span style="font-size:5.4px;color:#777">{t2}</span>','border-style:dashed' if i==0 else '')
    b+=BX(R+354,y,145,rh,f'<span style="font-size:6px;color:#777">主な最終用途</span><span style="font-size:6.6px">{e}</span>')
b+=BX(R+104,ry1,64,rh*2+4,'<b style="font-weight:400">RtM</b><span style="font-size:5.4px;color:#777">金属資源<br>トレーディング本部</span>')
by=ry2+rh+8
b+=A(R,by,'資源投資（鉱山・製鉄／製錬）',282,'',f"border-top:2.4px solid {DK};font-size:7px;text-align:center;padding-top:2px")+A(R+104,by+18,'トレーディング（RtM）',246,'',f"border-top:2.4px solid {MD};font-size:7px;text-align:center;padding-top:2px")
b+=A(R+360,by+6,'＝ 投資と販売の<br>「両輪」',139,'',"font-size:9px;font-weight:500;text-align:center;line-height:1.4")
# 川上〜川下 boxes below
ky=by+50
for i,(a,t) in enumerate([('川上','資源開発・保有'),('川中','製鉄・製錬'),('中間流通','トレーディング（RtM）'),('川下','最終製品・需要家')]):
    x=R+i*126; b+=BX(x,ky,112,24,f'{a}｜{t}','font-size:6.8px')
    if i<3: b+=A(x+114,ky+5,'→',None,'',"font-size:9px;color:#888")
b+=SRC(R,ky+30,'金属資源G_P3（金属資源のバリューチェーンと事業領域）。写真は省略')
b+=nt(R,ky+40,'「投資と販売の両輪」を軸に表現（PwC様レビューNo.7）。規模には言及しない。鋼材販売のメタルワンは別グループ',W)
pages.append(spread(b,4,5))

# ===== P06-07 v4 =====
b=hd(L,'第2章　HOW/WHAT｜独自価値　—　機能・強み','納得')
b+=T(L,60,'わが社資産の強み','バリューチェーンの起点で、一級資産を保有する')
b+=XC(L,108,W,60)
for j,(c,h,items) in enumerate([('原料炭','世界最大級の原料炭事業',[('Market','上位5社で約80%','寡占度が高く、供給は漸減'),('Scale','BMAで約50%','一級強粘炭供給に占めるシェア'),('Quality','高品位に集約','港湾・鉄道も自社保有し全体最適')]),
                                ('銅','世界トップクラスの資産',[('Market','上位5社で約25%','寡占化が進まず、再編の機運'),('Scale','ノンオペレーターとして世界最大','持分生産量 世界20位・本邦首位'),('Quality','5鉱山すべて世界Top15','平均コストは世界上位25%')])]):
    x=L+j*256; b+=A(x,140,f'{c}<span style="font-size:7px;color:#666;font-weight:300">　{h}</span>',243,'',f"font-size:10px;font-weight:500;border-bottom:1.2px solid {DK};padding-bottom:3px")
    for i,(k,n,d) in enumerate(items):
        y=164+i*40; b+=A(x,y,k,50,'',"font-size:6.4px;color:#777;letter-spacing:.8px")+A(x+52,y-2,n,190,'',"font-size:10.5px;font-weight:300;line-height:1.2")+SM(x+52,y+15,d,190)
b+=SRC(L,286,'金属資源G_P6（わが社資産の強み）。Market／Scale／Quality の要点のみ抽出')
b+=nt(L,298,'第2章の起点（PwC様レビューNo.12）。数値は事実ベースで表示し、誇示する表現は避ける',W)
b+=rule(L,320,W)
b+=T(L,332,'原料炭事業','鉄の主原料“産業のコメ”を、世界最高品位で届ける')
b+=A(L,378,'BHPと50:50の合弁（BMA）で、原料炭の一級資産に参画',W,'',"font-size:9.6px;font-weight:400")
for i,s_ in enumerate(['世界最高品位の<br>原料炭を保有','原料炭は鉄の主原料<br>＝“産業のコメ”','鉄は今後も<br>底堅く必要とされる','ゆえに<br>社会に不可欠']):
    x=L+i*126; b+=BX(x,398,112,40,f'<span style="color:#888">{i+1}</span>{s_}')
    if i<3: b+=A(x+114,410,'→',None,'',"font-size:10px;color:#888")
for i in range(4): b+=XS(L+i*126,442,112,36)
# BMA simplified
by=490
b+=ph(L,by,150,200,'r-047.png')+SM(L,by+202,'写真：BMAの鉱山（流用：粗原稿）',150)
b+=A(L+164,by,'出資構成',None,'',"font-size:7.4px;font-weight:400")
b+=BX(L+164,by+14,80,20,'三菱商事')+VL(L+204,by+34,10)+SM(L+208,by+35,'100%')
b+=BX(L+164,by+44,80,20,'MDP')+BX(L+254,by+44,62,20,'BHP')
b+=VL(L+204,by+64,12)+VL(L+285,by+64,12)+SM(L+208,by+66,'50%')+SM(L+289,by+66,'50%')
b+=BX(L+164,by+76,152,26,'<b style="font-weight:400">BMA</b><span style="font-size:5.6px;color:#777">BHP Mitsubishi Alliance</span>','background:'+BG)
facts=[('参画','1968年 MDP設立／2001年 BMA組成（持分50%）'),('拠点','豪州クイーンズランド州 Bowen Basin'),('保有資産','炭鉱（露天掘4・坑内掘1）・港・鉄道'),('生産量','39百万t（当社持分20百万t）2026年度見通し'),('特記','炭鉱寿命60年以上／海上輸出市場シェア約20%')]
for i,(k,v) in enumerate(facts):
    y=by+116+i*15; b+=A(L+164,y,k,40,'',"font-size:6.4px;color:#777")+A(L+206,y,v,293,'',"font-size:6.8px")
b+=svg(L+330,by,169,104,f'<path d="{landsvg.region(112,155,-44,-9,169,104)}" fill="#e3e6e9"/><rect x="{(146-112)/43*169:.0f}" y="{(9+19)/35*104:.0f}" width="{4/43*169:.0f}" height="{8/35*104:.0f}" fill="none" stroke="#3c4045" stroke-width="1"/>')+A(L+330+(150.5-112)/43*169,by+(9+17)/35*104,'Bowen Basin<br>（クイーンズランド州）',70,'',"font-size:5.8px;line-height:1.3")
b+=SRC(L+164,by+196,'金属資源G_P7（原料炭事業）。表・出資構成・地図を簡略化',335)
b+=nt(L,by+222,'①〜④の文脈で、社会における必要性を中心に訴求（PwC様レビューNo.13）。他社ロゴ（BHP・BMA）は使用せずテキスト表記',W)
# ---- P07 copper ----
b+=hd(R,'第2章　HOW/WHAT｜独自価値','納得')
b+=T(R,60,'銅事業','自社操業を伴わずに、世界最大級の銅ポジションを築く')
b+=A(R,108,'ノンオペレーターとして世界最大の銅生産者',240,'',"font-size:10.5px;font-weight:400")
b+=XC(R,128,240,100)
b+=ph(R+259,60,240,160,'_mr_project_02.png')+SM(R+259,223,'写真：銅鉱山（流用：三菱商事サイト）',240)
pts=[('Tier1アセットの保有','規模で世界上位の優良鉱山に参画'),('主要メジャー各社との協業','特定1社に偏らず、ほぼすべてのメジャーと共同事業・取引'),('トレーディングによる関係構築','販売を通じて業界内の幅広いリレーションを形成'),('新技術・スタートアップへの投資','業界のボトルネックに挑む技術に投資')]
for i,(t,d) in enumerate(pts):
    x=R+(i%2)*256; y=246+(i//2)*58
    b+=A(x,y,t,240,'',"font-size:9px;font-weight:400")+SM(x,y+13,d,240)+XS(x,y+26,240,50)
b+=rule(R,368,W)
# fig 1 table
b+=A(R,380,'保有案件（主要鉱山）',None,'',"font-size:8.4px;font-weight:400")
hdr=['鉱山','所在国','鉱山別生産量','出資比率','参画時期']; cw=[78,34,48,36,44]
tb=[('Escondida','チリ','1位','8.25%','1988年'),('Los Pelambres','チリ','12位','5%','1997年'),('Anglo American Sur','チリ','10位*','20.44%','2011年'),('Marimaca','チリ','開発中','5%','2023年'),('Antamina','ペルー','4位','10%','1999年'),('Quellaveco','ペルー','15位','40%','2011年'),('Copper World','米国','開発中','30%','2025年')]
y=400; x=R
for j,h in enumerate(hdr): b+=A(x+sum(cw[:j]),y,h,cw[j],'',f"font-size:6px;color:#fff;background:{DK};padding:3px 3px")
for i,r in enumerate(tb):
    yy=y+18+i*24
    for j,v in enumerate(r): b+=A(x+sum(cw[:j]),yy,v,cw[j],'',f"font-size:7.2px;padding:6px 3px;height:24px;{'background:'+BG if i%2==0 else ''}")
b+=SM(R,y+18+7*24+4,'* 隣接鉱山との一体操業後の体制',240)
# fig 2 ranking bars
rk=[('1','BHP',1501),('2','Codelco',1432),('3','Freeport',1099),('4','Southern Copper',948),('5','Zijin Mining',850),('6','Glencore',812),('7','Rio Tinto',740),('8','China Moly',558),('9','KGHM',538),('10','Anglo American',496),('11','Antofagasta',453),('17','Teck',363),('20','三菱商事',326)]
rx=R+262; b+=A(rx,380,'会社別 世界銅生産量ランキング（2025年・kt）',None,'',"font-size:8.4px;font-weight:400")
for i,(n,c,v) in enumerate(rk):
    yy=402+i*18.5; me=(c=='三菱商事')
    b+=A(rx,yy,f'{n}.',14,'',"font-size:6px;color:#777;text-align:right")+A(rx+18,yy,c,70,'',f"font-size:6.2px;{'font-weight:500' if me else ''}")
    b+=A(rx+90,yy+1,'',v/1501*110,'',f"height:11px;background:{DK if me else LT}")+A(rx+92+v/1501*110,yy,f'{v:,}',30,'',"font-size:5.8px;color:#666")
b+=A(rx+90,402+12*18.5+16,'ノンオペレーターとして世界最大',140,'',"font-size:6.6px;font-weight:500;border:.8px solid #3c4045;padding:1px 4px")
b+=SRC(R,668,'金属資源G_P8（銅事業）を2つの図に分けて簡略化。他社ロゴは使用せず社名をテキスト表記')
b+=nt(R,680,'★ノンオペレーターとして世界最大を明示し、「声がかかる存在」として訴求（PwC様レビューNo.14）。Green Copperは削除',W)
pages.append(spread(b,6,7))

# ===== P08-09 v7 =====
b=hd(L,'第2章　HOW/WHAT｜独自価値','納得')
b+=T(L,60,'トレーディング事業','15業界×50カ国×約1,000社の販売網で、市場をつなぐ')
b+=A(L,106,'15<span style="font-size:8px">業界</span> × 50<span style="font-size:8px">カ国</span> × 約1,000<span style="font-size:8px">社</span>',250,'kf','font-size:19px;white-space:nowrap')+A(L+262,108,'グローバルネットワーク　10拠点',None,'',"font-size:8px;font-weight:400")+SM(L+262,120,'シンガポール・日本・インド・中国・米国・英国・UAE・インドネシア・タイ・チリ',237)
b+=XC(L,140,W,60)
# --- RtM hub (compact)
hy=170; b+=A(L,hy,'RtM ＝ Resource to Market',None,'',"font-size:8.4px;font-weight:400")+SM(L+150,hy+2,'調達（左）と販売（右）をシンガポールのRtMIが結ぶ')
sup=[('投資先','鉄鉱石・貴金属・ニッケル・リチウム'),('投資先','鉄鉱石・銅'),('他サプライヤー','一般炭・鉄鉱石・銅・貴金属'),('他サプライヤー','アルミ・貴金属')]
for i,(n,d) in enumerate(sup):
    y=hy+16+i*30; b+=BX(L,y,110,24,f'<b style="font-weight:400">{n}</b><span style="font-size:5.4px;color:#666">{d}</span>','background:'+BG)
mk=[('RtME','欧州市場'),('RtMB','インド市場'),('RtMJ','日本市場'),('RtMA','北米市場'),('中東・ASEAN','市場'),('中南米・ブラジル','市場')]
for i,(n,d) in enumerate(mk):
    y=hy+14+i*21; b+=BX(L+392,y,107,18,f'<b style="font-weight:400">{n}</b><span style="font-size:5.2px;color:#666">{d}</span>')
hcy=76
b+=BX(L+205,hy+hcy-20,90,40,'<b style="font-weight:500;font-size:9px">RtMI</b><span style="font-size:5.6px">シンガポール</span>',f'border-radius:20px;border:1.2px solid {DK}')
ln=''
for i in range(4): ln+=f'<line x1="112" y1="{28+i*30}" x2="203" y2="{hcy}" stroke="#8a9096" stroke-width=".8"/>'
for i in range(6):
    y2=14+i*21+9; ln+=f'<line x1="297" y1="{hcy}" x2="388" y2="{y2}" stroke="#3c4045" stroke-width=".8"/><path d="M383,{y2-3} L389,{y2} L383,{y2+3}" fill="none" stroke="#3c4045" stroke-width=".8"/>'
b=svg(L,hy,499,150,ln)+b
b+=A(L,hy+142,'取扱商品例：石炭・銅（銅精鉱／銅地金）・鉄鉱石・貴金属・リチウム・アルミ',W,'',"font-size:6.2px;color:#444")+SRC(L,hy+152,'金属資源G_P37（RtM＝Resource to Market）。地図を拠点の関係図に簡略化')
b+=rule(L,334,W)
# --- ① RtM business model
b+=T(L,342,'RtM事業のビジネスモデル（仮）','一つの商品の中で、投資から販売まで一気通貫でつなぐ')+TAG(L+300,348,'PwC様FB①')
b+=XC(L,388,W,100)
dx=L+128; dw=243; dy=430
b+=BX(dx,dy,dw,18,'<b style="font-weight:500">Mitsubishi Corporation</b>')
b+=BX(dx+4,dy+22,52,14,'第三者取引','font-size:5.8px')+BX(dx+58,dy+22,56,14,'MC保有資産','font-size:5.8px;background:'+BG)
arr=f'<path d="M30,0 V36 M26,31 L30,36 L34,31" fill="none" stroke="{DK}" stroke-width="1.4"/><path d="M{dw-30},36 V0 M{dw-34},5 L{dw-30},0 L{dw-26},5" fill="none" stroke="{MD}" stroke-width="1.4"/>'
b+=svg(dx,dy+39,dw,38,arr)+svg(dx,dy+100,dw,38,arr)
b+=A(dx+40,dy+44,'資源確保による<br><b style="font-weight:500">安定供給</b>',80,'',"font-size:6.2px;line-height:1.4")
b+=A(dx+126,dy+40,'市場・業界動向の発信・知見共有による<b style="font-weight:500">事業機会の発掘</b>',84,'',"font-size:6.2px;line-height:1.4;text-align:right")
b+=BX(dx,dy+77,dw,22,'<b style="font-weight:500;font-size:9px">RtM</b>',f'border:1.2px solid {DK}')
b+=A(dx+40,dy+106,'トレーディング機能強化による<b style="font-weight:500">継続的な付加価値創出</b>',80,'',"font-size:6.2px;line-height:1.4")
b+=A(dx+126,dy+102,'広い産業接地面を活かした<b style="font-weight:500">インテリジェンス機能の発揮</b>',84,'',"font-size:6.2px;line-height:1.4;text-align:right")
b+=BX(dx,dy+138,dw,18,'<b style="font-weight:500">顧客基盤</b>')
cards=[('Sustainability','世界の資産とパートナーシップを基盤に、最適な供給とファイナンスを提供',L,dy),
       ('Professionalism','業界の専門性と総合商社の伝統による、信頼性の高いサービス',L,dy+80),
       ('Market Intelligence','実績と詳細な市場分析に基づく、顧客ごとの市場情報',L+379,dy),
       ('Global Network','90カ国以上の拠点網で、市場情報と迅速な解決策を提供',L+379,dy+80)]
for t,d,x,y in cards:
    b+=gb(x,y,120,26,'写真：〇〇')+A(x,y+29,t,120,'',"font-size:7.4px;font-weight:500")+SM(x,y+40,d,120)+XS(x,y+60,120,12)
b+=SRC(L,dy+162,'金属資源G_P9（RtM事業のビジネスモデル）、Resource to Market（RtM紹介資料）。左右のカードは顧客への提供価値')
b+=nt(L,dy+172,'PwC様フィードバック①：RtMの事業ビジネスモデルを中心にした内容に差し替え。「トレーディング事業の事例（銅）」の枠は、このビジネスモデルと下記②の説明文（銅の事例）に統合',W)
b+=rule(L,dy+196,W)
# --- ② RtM functions
fy=dy+202
b+=T(L,fy,'RtMの多様な機能','調達から販売まで、取引に付加価値を加える5つの機能')+TAG(L+170,fy+6,'PwC様FB②')
b+=XC(L,fy+46,W,80)
fns=[('Risk Management','市場リスク・信用リスク・品質管理'),('Logistics','用船・委託販売・在庫運用・ジャストインタイム納入'),('Financing','オフテイク契約・貿易金融'),('Marketing and Procurement','市場分析・マーケティング戦略・調達先の多様化'),('Carbon Reduction','カーボンオフセット・低炭素素材')]
for i,(n,d) in enumerate(fns):
    x=L+i*100.6; y=fy+88
    b+=A(x,y,str(i+1),14,'',f"height:14px;line-height:14px;border-radius:7px;border:1px solid {DK};font-size:7px;text-align:center")+A(x+18,y+1,n,76,'',"font-size:7px;font-weight:500;line-height:1.25")+SM(x,y+22,d,94)+XS(x,y+44,94,14)
b+=nt(L,fy+142,'PwC様フィードバック②：見出しを「RtMの多様な機能」とし、機能一覧を5項目に差し替え。本文は銅の事例を交えた説明文を想定（参照：RtM Group Main Products and Business Solutions）',W)
# ---- P09 ----
b+=hd(R,'第2章　HOW/WHAT｜独自価値','納得')
b+=T(R,60,'事業・プロジェクト一覧','鉄鉱石から電池資源・肥料・アルミまで、世界に広がる事業領域')
MW,MH=W,183; my=104
b+=svg(R,my,MW,MH,f'<path d="{landsvg.land(MW,MH)}" fill="#e3e6e9"/>')
PRJ=[('IOC',-66.9,52.9,'鉄鉱石','○'),('CMP',-71.2,-28.5,'鉄鉱石','○'),('CAP',-70.6,-33.4,'鉄鉱石','○'),('BMA',148.3,-22.3,'原料炭','○'),
('Escondida',-69.07,-24.27,'銅','○'),('Los Pelambres',-70.5,-31.7,'銅','○'),('Anglo American Sur',-70.3,-33.15,'銅','○'),('Antamina',-77.05,-9.53,'銅','○'),('Quellaveco',-70.6,-17.1,'銅','○'),('Marimaca',-70.3,-22.9,'銅','☆'),('Copper World',-110.9,31.9,'銅','☆'),
('Turnagain',-128.9,58.5,'ニッケル','☆'),('Kalgoorlie Nickel',121.4,-30.7,'ニッケル','☆'),('PAK Lithium',-94.0,51.6,'リチウム','☆'),('Aurukun',141.7,-13.3,'ボーキサイト','☆'),('Arctial',25.7,64.2,'低炭素アルミ','☆'),('Woodsmith',-0.6,54.4,'肥料資源','☆'),
('RtM Europe／Triland Metals',-0.1,51.5,'トレーディング','□'),('RtM Bharat',77.2,28.6,'トレーディング','□'),('RtM International',103.8,1.3,'トレーディング','□'),('RtM Japan',139.7,35.7,'トレーディング','□'),('RtM Americas',-77.0,40.4,'トレーディング','□')]
CAT=['鉄鉱石','原料炭','銅','ニッケル','リチウム','ボーキサイト','低炭素アルミ','肥料資源','トレーディング']
SH={'鉄鉱石':'#2f3337','原料炭':'#555b61','銅':'#7a8087','ニッケル':'#9aa0a6','リチウム':'#9aa0a6','ボーキサイト':'#b0b5ba','低炭素アルミ':'#b0b5ba','肥料資源':'#b0b5ba','トレーディング':'#ffffff'}
for n,lo,la,c,k in PRJ:
    x,y=landsvg.proj(lo,la,MW,MH); col=SH[c]
    shape_='border-radius:4px' if k=='○' else ('border-radius:0;transform:rotate(45deg)' if k=='☆' else 'border-radius:0')
    b+=A(R+x-3,my+y-3,'',6,'',f"height:6px;background:{col};border:.6px solid #2f3337;{shape_}")
lab=[('IOC',-66.9,52.9,6,-4),('BMA',148.3,-22.3,6,-4),('Chile・Peru（銅・鉄鉱石）',-72,-22,8,-2),('Copper World',-110.9,31.9,-60,-8),('Turnagain',-128.9,58.5,-48,-8),('PAK Lithium',-94.0,51.6,-12,-14),('Arctial',25.7,64.2,6,-6),('Woodsmith',-0.6,54.4,-40,-12),('Aurukun',141.7,-13.3,6,-6),('Kalgoorlie',121.4,-30.7,-40,4),('RtM Japan',139.7,35.7,6,-4),('RtM International',103.8,1.3,-40,6),('RtM Bharat',77.2,28.6,-44,-4),('RtM Europe・Triland',-0.1,51.5,6,2),('RtM Americas',-77.0,40.4,6,-2)]
for n,lo,la,dx,dy in lab:
    x,y=landsvg.proj(lo,la,MW,MH); b+=A(R+x+dx,my+y+dy,n,None,'',"font-size:5.4px;color:#333;white-space:nowrap")
ly=my+MH+4
leg='　'.join((f'<span style="color:{SH[c]}">■</span>' if c!='トレーディング' else '□')+c for c in CAT)
b+=A(R,ly,leg,W,'',"font-size:5.8px;white-space:nowrap")
b+=A(R,ly+11,'○既存プロジェクト　◇探査・探鉱・開発プロジェクト　□トレーディング拠点',W,'',"font-size:5.8px;color:#555")
b+=SRC(R,ly+22,'金属資源G_P10（事業・プロジェクト一覧）。凡例の色分けは台割用のグレー階調')
items=[('鉄鉱石','x_ironore.jpg'),('電池資源（ニッケル）','r-073.png'),('電池資源（リチウム）','x_lithium.jpg'),('肥料資源',None),('アルミ・ボーキサイト','r-055.png'),('二次資源','r-074.png')]
for i,(t,f) in enumerate(items):
    x=R+i*84; y=ly+36
    b+=(ph(x,y,78,40,f,None,'contain') if f else gb(x,y,78,40,'写真：〇〇'))+A(x,y+42,t,82,'',"font-size:6.6px;font-weight:400")+XS(x,y+52,78,24)
b+=nt(R,ly+112,'鉄鉱石を先頭に配置し、銅・原料炭と同格には押し出さない（PwC様レビューNo.15）',W)
cy0=ly+134
b+=rule(R,cy0-6,W)
b+=T(R,cy0,'新技術への投資（CVC）','銅のバリューチェーン全体に、新技術の網を張る')
fy=cy0+46
LX=R+58; cw2=[96,96,96,135]; cx2=[LX,LX+100,LX+200,LX+300]
st=[('採掘','鉱石','Cu 約1%'),('選鉱・浸出','銅精鉱','Cu 20〜30%'),('製錬・精製','銅地金','Cu 99.99%'),('最終用途','基礎需要・エネルギー転換・AI／DC','')]
for i,(n,p,g) in enumerate(st):
    x=cx2[i]; b+=A(x,fy,n,cw2[i],'',f"height:16px;line-height:16px;text-align:center;font-size:7px;color:#fff;background:{DK}")
    b+=A(x,fy+18,f'{p}<span style="color:#888">　{g}</span>' if g else p,cw2[i],'',"font-size:6px;text-align:center")
    if i<3: b+=A(x+cw2[i]-1,fy+1,'›',None,'',"font-size:10px;color:#888")
def chip(x,y,w,h,t,kind):
    st_={'投資':f'background:{DK};color:#fff','トレーディング':f'background:{MD};color:#fff','CVC':f'border:1px solid {DK};background:#fff'}[kind]
    return A(x,y,t,w,'',f"height:{h}px;font-size:6.2px;padding:3px 4px;line-height:1.35;{st_}")
lanes=[('資源投資',fy+34,28),('トレーディング',fy+66,28),('新技術投資<br>（CVC）',fy+98,60)]
for n,y,h in lanes:
    b+=A(R,y,n,52,'',f"height:{h}px;font-size:6.4px;font-weight:400;display:flex;align-items:center;border-top:.6px solid #ccc")+HL(LX,y,W-58,'#e0e2e5',.6)
b+=chip(cx2[0],fy+36,cw2[0],24,'鉱山への出資<br>Escondida・Quellaveco ほか','投資')
b+=chip(cx2[1],fy+68,196,24,'RtM：銅精鉱・銅地金のトレーディング','トレーディング')
b+=chip(cx2[3],fy+68,cw2[3],24,'Triland Metals：LME・CMEでのブローカー／ヘッジ','トレーディング')
b+=chip(cx2[1],fy+100,cw2[1],26,'<b style="font-weight:500">CiDRA</b>（選鉱）<br>回収率・処理能力を向上','CVC')
b+=chip(cx2[1],fy+130,cw2[1],26,'<b style="font-weight:500">Jetti</b>（浸出）<br>触媒で硫化鉱から回収','CVC')
b+=chip(cx2[3],fy+100,cw2[3],26,'<b style="font-weight:500">DESCycle</b>（リサイクル）<br>電子スクラップから銅・貴金属を回収','CVC')
b+=A(cx2[3],fy+132,'↺ リサイクルで再び供給へ',cw2[3],'',"font-size:6px;color:#555")
iy=fy+44
lg='<span style="color:#3c4045">■</span> 資源投資　<span style="color:#8a9096">■</span> トレーディング　□ 新技術投資（CVC）'
b+=A(R,iy+118,lg,W,'',"font-size:6px")
b+=SRC(R,iy+130,'金属資源G_P41（Copper Value Chain）、統合報告書P19。インフォグラフィックに再構成')
b+=nt(R,iy+140,'CVC＝コーポレート・ベンチャー・キャピタル（新技術スタートアップへの投資）。新技術の把握が既存事業の高度化・将来価値に還元される点を訴求（PwC様レビューNo.15）',W)
pages.append(spread(b,8,9))

# ===== P10-11 v2 =====
b=hd(L,'第3章　PROOF｜選ばれ続ける理由　—　実績・関係・評価','安心')
b+=T(L,60,'Partner of Choice','資源業界に不可欠な存在として、選ばれ続ける')+TAG(L+160,66,'改善③ 1ページ化')
b+=XC(L,108,240,120)
b+=ph(L+259,108,240,150,'_mr_project_01.png','写真：現場の人々（流用：三菱商事サイト）')
fn=['資源メジャーとの<br>企業文化的親和性','資源投資経験に裏打ちされた<br>JV経営力','事業ポートフォリオを活かした<br>健全な財務基盤','マクロ環境とバリューチェーンに<br>対する深い知見']
for i,t in enumerate(fn):
    x=L+(i%2)*256; y=290+(i//2)*92
    b+=A(x,y,f'<span style="color:#888">0{i+1}</span>　'+t,240,'',"font-size:9.5px;font-weight:400;line-height:1.45")+XC(x,y+32,240,60,6.8,1.6)
b+=rule(L,476,W)
b+=lbl(L,486,'業界最大手とのJV実績')
for i,n in enumerate(['BHP','Rio Tinto','Anglo American']):
    b+=A(L+i*168,500,n,156,'bx',"height:22px")
b+=lbl(L,534,'単なる共同出資者に留まらない、JVへの貢献')
for i,t in enumerate(['人材派遣','ガバナンス参画','三菱の総合力による<br>事業価値の最大化']):
    x=L+i*168; b+=A(x,548,t,156,'bx',"height:30px")+X(x,584,156,36,6.6,1.6)
b+=rule(L,628,W)
b+=lbl(L,638,'パートナーに評価される理由')
for i,t in enumerate(['中長期的な視座','リスクシェアリング','総合力']):
    x=L+i*168; b+=A(x,654,t,156,'',"font-size:9px;font-weight:400")+X(x,670,156,48,6.6,1.6)
b+=nt(L,728,'他社ロゴは使用しない（社名はテキスト表記）。財務貢献だけを強調すると「資金提供に留まる」と受け取られるため、JV経営への関与と総合力を併せて示し、PEファンド等との違いを明確にする（PwC様レビューNo.19／参照：金属資源G資料 P38の2ページ後）',W)
# right page : 第4章 + 締め
b+=hd(R,'第4章　VISION｜何を実現するか　—　社会課題への取り組み','期待')
b+=T(R,60,'外部環境と社会課題','クリティカルミネラルを取り巻く外部環境に、安定供給と効率的な供給の両面で応える')
b+=A(R,112,'外部環境',None,'lb',"font-weight:400;color:#444")
b+=A(R+20,128,'クリティカル<br>ミネラル',90,'bx',"height:90px;border-radius:45px;font-size:8.4px")
for i,t in enumerate(['産業構造の転換（人口増・電化による需要の拡大）','供給制約の深刻化','地政学リスクの常態化']):
    y=128+i*30; b+=VL(R+126,y,24,'#555',1.4)+A(R+134,y,t,360,'',"font-size:7.6px;font-weight:400")+XS(R+134,y+13,360,40)
b+=A(R,226,'サプライチェーン確保の重要性・川上資源への参入障壁が増大',W,'bx',"height:20px;font-size:7.6px")
b+=A(R,252,'当社の取り組み',None,'lb',"font-weight:400;color:#444")
b+=A(R,266,'① 安定供給（安定的な資源確保）<br><span style="font-size:6.4px;color:#777">資源投資</span>',215,'bx',"height:30px;border-color:#444")+A(R+219,272,'⇄ 連携',60,'',"font-size:7px;text-align:center;color:#555")+A(R+284,266,'② 効率的な供給<br><span style="font-size:6.4px;color:#777">トレーディング</span>',215,'bx',"height:30px;border-color:#444")
b+=XS(R,300,215,40)+XS(R+284,300,215,40)
b+=nt(R,322,'現状の図（金属資源G_P38「クリティカルミネラルを取り巻く外部環境と当社の取り組み」）を踏襲（PwC様レビューNo.20）。①②と資源投資・トレーディングの対応は要確認。短期的な潮流（脱炭素・生成AI等）は前面化しない',W)
b+=A(595,352,'',595,'',"height:490px;background:#e6e8eb")+A(R+20,360,'締めのビジュアル（選定された表紙案の表現に合わせて決定）',None,'lb')
b+=A(R+10,378,'',480,'',"height:412px;background:#fff")
b+=A(R+30,392,'締め｜ビジョン共感×協業への誘い',None,'hd')+TAG(R+200,390,'PwC様レビューNo.21')
b+=A(R+30,410,'共に、資源の未来を築く（仮）',430,'t1')
b+=A(R+30,436,'目指す未来像への共感から、関係構築へとつなぐ締め',430,'t2')
b+=A(R+30,462,'目指す未来像',None,'',"font-size:9px;font-weight:400")+A(R+30,476,'社会に必要な資源を、長期にわたって支え続ける',200,'lb')+XC(R+30,490,200,60,6.8,1.6)
b+=A(R+250,462,'協業への誘い',None,'',"font-size:9px;font-weight:400")+A(R+250,476,'この相手と共に築きたい、と感じてもらう',200,'lb')+XC(R+250,490,200,60,6.8,1.6)
b+=A(R+30,552,'コアメッセージ／グループミッションに帰結（冒頭P.02と呼応）',430,'',"font-size:8px;border:.6px solid #9aa0a6;padding:5px;text-align:center")
b+=nt(R+30,578,'直接的な営業色は抑える。具体的な表現手段は後続検討。グループミッションはP.04（位置付け・役割）に置き、ここではその言葉に帰結させる（PwC様レビューNo.21）',430)
b+=rule(R+30,608,430)
b+=A(R+30,618,'お問い合わせ先',None,'',"font-size:9px;font-weight:400")+TAG(R+110,620,'改善⑤')
b+=X(R+30,636,280,60,6.8,1.6)+A(R+30,680,'部署名・所在地・メール／Webサイト',280,'lb')
b+=gb(R+380,626,80,80,'QRコード<br>（Webサイト）')
b+=nt(R+30,724,'商談で手渡す冊子のため、問い合わせ先とWebサイトへの導線を控えめに設ける（裏表紙に置く案も可）',430)
pages.append(spread(b,10,11))



links=''.join(f'<link rel="stylesheet" href="f/nsjp/package/{w}.css">' for w in (300,400,500))
open('daiwari_v7.html','w').write(f'<!doctype html><meta charset=utf-8>{links}<style>{CSS}</style>'+''.join(pages))
