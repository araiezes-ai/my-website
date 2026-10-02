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
.lb{{font-size:6.8px;color:#666;letter-spacing:.8px}}
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

# ===== P04-05 v2 =====
b=hd(L,'第1章　WHO｜我々は何者か　—　三菱商事・金属資源グループとは','理解')
b+=T(L,60,'三菱商事とは','三綱領に基づき、経済価値・環境価値・社会価値の同時実現を志す総合商社')
b+=XC(L,112,250,110)
b+=ph(L,210,150,66,'r-000.png',None,'contain')+A(L,280,'三綱領（所期奉公・処事光明・立業貿易）',None,'lb')
b+=FIG(L+270,112,229,76,'ref_mc.png','現状の図：三綱領と3つの価値（金属資源G_P46）')+FIG(L+270,206,229,76,'ref_groups.png','全7グループの構成（三菱商事公式サイト）')
b+=nt(L,300,'三綱領と「3つの価値の同時実現」を示す（PwC様レビューNo.3）。グループ数は7グループ（同No.4）')
b+=rule(L,326,W)
b+=T(L,338,'金属資源グループの位置付け・役割','三菱商事の中で、金属資源グループが担う位置付けと役割')
b+=XC(L,388,250,90)
b+=FIG(L+270,388,229,72,'ref_portfolio.png','現状の図：ポートフォリオ構成（Investor Day P6）')
b+=A(L,470,'グループミッション',None,'lb',"font-weight:400;color:#444")
b+=A(L,484,'「社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する」',W,'',"font-size:9px;font-weight:300;line-height:1.6")
b+=nt(L,518,'収益面は事実・実績ベースで表示し、誇示する表現は避ける。ミッション文言は金属資源G_P2の正式表記を要確認',W)
b+=A(L,548,'組織図・事業体制',None,'',"font-size:11px;font-weight:400")+TAG(L+92,550,'改善① 移動')
b+=A(L,564,'投資を担う2本部と、トレーディングを担う1本部',None,'t2')
o=A(L+190,588,'グループCEO',120,'bx',"height:20px")+A(L+380,588,'グループCEOオフィス',110,'bx',"height:20px;border-style:dashed")
o+=A(L+249,608,'',1,'',"height:12px;border-left:.6px solid #888")+rule(L+80,620,340,'#888')
for i,(n,k) in enumerate([('鉄鋼原料本部','投資'),('クリティカルミネラル本部','投資'),('金属資源トレーディング本部','トレーディング')]):
    x=L+10+i*170; o+=A(x+75,620,'',1,'',"height:10px;border-left:.6px solid #888")+A(x,630,n+f'<span style="color:#888;font-size:6.2px">（{k}）</span>',150,'bx',"height:28px")
o+=lbl(L,672,'主要関係会社')
for i,(n,d) in enumerate([('MDP','原料炭'),('MCI','南米の銅・鉄鉱石'),('MCIP','ペルーの銅'),('RtM','トレーディング'),('Triland Metals','金属取引（ブローカー・ヘッジ）')]):
    o+=A(L+i*100,686,f'<b style="font-weight:400">{n}</b><span style="color:#888;font-size:5.8px;line-height:1.3">{d}</span>',94,'bx',"height:34px")
b+=o+nt(L,728,'本部長名などの個人名は記載しない。PwC資料の分類どおり「位置付け・役割」の中で示す（組織図＝役割の具体化）',W)
# right
b+=hd(R,'第1章　WHO｜我々は何者か','理解')
b+=T(R,60,'金属資源グループの事業と機能の変遷','時代の変化を先読みし、事業モデルを変革してきた歩み')+TAG(R+330,66,'改善② 拡大')
b+=XC(R,108,W,60)
b+=FIG(R,148,262,197,'ref_hensen.png','現状の図：主要金属資源権益の参画経緯（金属資源G_P30）')
tl=[('1980年代〜','日本の需要を捉え、資源を日本へ運ぶトレーディングに参入'),('〜2000年頃','少数株主として資源権益に出資'),('2000年〜','大型案件に参画し、BHPと50:50のJV運営へ'),('2010年代〜','銅の権益を拡大。マーケティングをRtM（シンガポール）に集約'),('現在','〇〇（現在の姿を記載）')]
b+=A(R+284,150,'',1,'',"height:192px;border-left:.6px solid #888")
for i,(e,t) in enumerate(tl):
    y=150+i*40; b+=A(R+280,y+2,'',8,'',"height:8px;border-radius:4px;background:#888")+A(R+294,y,e,200,'',"font-size:8.4px;font-weight:400")+A(R+294,y+12,t,205,'',"font-size:6.8px;line-height:1.4;color:#444")+X(R+294,y+24,205,26,6,1.4)
b+=nt(R,362,'案件の詳細には立ち入らず、一級資産への早期参画を「幸運ではなく、熟慮の上で先手を打った結果＝先見性」として前向きに表現。図は現状の図を仮置き（デザイン未確定）',W)
b+=rule(R,392,W)
b+=T(R,404,'バリューチェーン全体像','投資と販売の両輪で、川上から川下までに関わる')
b+=FIG(R,452,262,197,'ref_vc.png','現状の図：金属資源のバリューチェーンと事業領域（金属資源G_P3）')
vc=[('川上','資源開発・保有','投資'),('川中','製鉄・製錬','投資'),('中間流通','トレーディング（RtM）','販売'),('川下','最終製品・需要家','')]
for i,(a,t,k) in enumerate(vc):
    y=454+i*40; b+=A(R+280,y,f'{a}　<b style="font-weight:400">{t}</b>',150,'bx',"height:28px")+(A(R+436,y+8,k,60,'',"font-size:7px;border-left:1.4px solid #555;padding-left:5px") if k else '')
    if i<3: b+=A(R+350,y+28,'↓',None,'',"font-size:8px;color:#888")
b+=XC(R+280,620,219,40,6.8,1.6)
b+=nt(R,676,'「投資と販売の両輪」が軸（PwC様レビューNo.7）。デザイン確定までは現状の図を仮置き。規模には言及しない。鋼材販売のメタルワンは別グループである旨を注記。第2章の前提として第1章の最後に置く',W)
pages.append(spread(b,4,5))


# ===== P06-07 : 第2章 資産の強み・原料炭 / 銅 =====
b=hd(L,'第2章　HOW/WHAT｜独自価値　—　機能・強み','納得')
b+=T(L,60,'わが社資産の強み','バリューチェーンの起点で、一級資産を保有する')
b+=XC(L,108,W,90)
kf=[('原料炭','5鉱山','高品位の鉱山に厳選して保有'),('銅','日本最大','持分生産量（世界第20位）'),('銅','世界上位15','に入る優良鉱山に複数参画')]
for i,(c,n,d) in enumerate(kf):
    x=L+i*168; b+=rule(x,150,156,'#888')+A(x,156,c,None,'lb')+A(x,168,n,156,'kf')+A(x,194,d,156,'lb')
b+=FIG(L,212,150,80,'ref_assets.png','現状の図（金属資源G_P6）')+XC(L+166,212,333,90,6.8,1.6)
b+=nt(L,314,'第2章の起点（PwC様レビューNo.12）。数値は事実ベースで表示し、誇示する表現は避ける',W)
b+=rule(L,334,W)
b+=T(L,346,'原料炭事業','鉄の主原料“産業のコメ”を、世界最高品位で届ける')
b+=A(L,394,'BHPと50:50の合弁（BMA）で、原料炭の一級資産に参画',W,'',"font-size:10px;font-weight:400")
steps=['世界最高品位の<br>原料炭を保有','原料炭は鉄の主原料<br>＝“産業のコメ”','鉄は今後も<br>底堅く必要とされる','ゆえに<br>社会に不可欠']
for i,s in enumerate(steps):
    x=L+i*126; b+=A(x,418,f'<span style="color:#888">{i+1}</span><br>{s}',112,'bx',"height:52px")
    if i<3: b+=A(x+114,438,'→',None,'',"font-size:10px;color:#888")
for i in range(4): b+=X(L+i*126,476,112,36,6.8,1.6)
b+=ph(L,540,240,170,'r-047.png','写真：BMAの鉱山（流用：粗原稿）')
b+=FIG(L+259,540,240,170,'ref_coal.png','現状の図：原料炭事業（金属資源G_P7）※他社ロゴは本制作で使用しない')
b+=nt(L,730,'社会における必要性の文脈を主に訴求。川上の代表例として銅・トレーディングより前に配置。BMAロゴは「他社ロゴ不使用」の方針に照らし扱い要確認',W)
b+=hd(R,'第2章　HOW/WHAT｜独自価値','納得')
b+=T(R,60,'銅事業','自社操業を伴わずに、世界最大級の銅ポジションを築く')
b+=ph(R+259,60,240,170,'_mr_project_02.png','写真：銅鉱山（流用：三菱商事サイト）')
b+=A(R,108,'ノンオペレーターとして世界最大の銅生産者',240,'',"font-size:10.5px;font-weight:400")+XC(R,128,240,110)
b+=rule(R,256,W)
pts=[('Tier1アセットの保有','規模で世界上位の優良鉱山に参画'),('主要メジャー各社との協業','特定1社に偏らず、ほぼすべてのメジャーと共同事業・取引'),('トレーディングによる関係構築','販売を通じて業界内の幅広いリレーションを形成'),('新技術・スタートアップへの投資','業界のボトルネックに挑む技術に投資')]
for i,(t,d) in enumerate(pts):
    x=R+(i%2)*256; y=272+(i//2)*120
    b+=A(x,y,t,240,'',"font-size:10px;font-weight:400")+A(x,y+16,d,240,'lb')+XC(x,y+32,240,60)
b+=FIG(R,520,W,170,'ref_copper.png','現状の図：銅事業（金属資源G_P8）')
b+=nt(R,706,'★自社操業なしで世界最大級の銅ポジション（ノンオペレーターとして世界最大）を明示し、「声がかかる存在」として訴求（PwC様レビューNo.14）。Green Copperは削除。他社ロゴは使用しない',W)
pages.append(spread(b,6,7))

# ===== P08-09 : トレーディング / 事業一覧 =====
b=hd(L,'第2章　HOW/WHAT｜独自価値','納得')
b+=T(L,60,'トレーディング事業','15業界×50カ国×約1,000社の販売網で、市場をつなぐ')
b+=A(L,112,'15<span style="font-size:8px">業界</span> × 50<span style="font-size:8px">カ国</span> × 約1,000<span style="font-size:8px">社</span>',260,'kf','font-size:19px;white-space:nowrap')
b+=XC(L,148,250,100)
b+=FIG(L+270,112,229,140,'ref_rtm.png','現状の図：RtM＝Resource to Market（金属資源G_P37）')
b+=lbl(L,272,'多様な取引機能')
for i,t in enumerate(['取扱商品の広さ','在庫','輸送手配','ヘッジ']):
    x=L+i*126; b+=A(x,288,t,112,'bx',"height:24px")+X(x,318,112,30,6.8,1.6)
b+=lbl(L,364,'投資（本体）とトレーディング（RtM）の連携')
fl=[('資源投資<br>（三菱商事本体）'),('RtM<br>ヘッジ・在庫・物流を付加'),('顧客<br>欧州・シンガポール・米州')]
for i,t in enumerate(fl):
    x=L+i*170; b+=A(x,380,t,150,'bx',"height:34px")
    if i<2: b+=A(x+153,382,'オフテイク →' if i==0 else '販売 →',None,'',"font-size:6px;color:#666")
b+=A(L+40,420,'← 市場の生きた情報を還元し、事業機会を発掘（好循環）',420,'',"font-size:7px;color:#555;border-top:.6px dashed #888;padding-top:3px")
b+=nt(L,440,'販売顧客に「投資目的の主体」と誤認されない表現に。RtMの追加資料（PwC様より別途共有）を反映予定',W)
b+=rule(L,466,W)
b+=T(L,478,'トレーディング事業の事例（銅）','一つの商品の中で、投資から販売まで一気通貫でつなぐ')
b+=gb(L,526,W,170,'事例図：銅の投資から販売までの一気通貫／複数地域・多機能にわたる展開<br>※PwCにて情報収集中')
b+=XC(L,704,W,120)
b+=hd(R,'第2章　HOW/WHAT｜独自価値','納得')
b+=T(R,60,'事業・プロジェクト一覧','鉄鉱石から電池資源・肥料・アルミまで、世界に広がる事業領域')
b+=FIG(R,108,W,200,'ref_map.png','現状の図：事業・プロジェクト一覧（金属資源G_P10）')
items=[('鉄鉱石','x_ironore.jpg'),('電池資源（ニッケル）','r-073.png'),('電池資源（リチウム）','x_lithium.jpg'),('肥料資源',None),('アルミ・ボーキサイト','r-055.png'),('二次資源','r-074.png')]
for i,(t,f) in enumerate(items):
    x=R+i*84; y=322
    b+=(ph(x,y,78,62,f,None,'contain') if f else gb(x,y,78,62,'写真：〇〇'))+A(x,y+66,t,80,'',"font-size:7.6px;font-weight:400")+X(x,y+80,78,30,6.4,1.55)
b+=nt(R,452,'鉄鉱石は主力3商品の一角だが、銅・原料炭と同格には押し出さず一覧の先頭に配置。原料炭・銅はP.06–07で紹介',W)
b+=rule(R,476,W)
b+=T(R,488,'新技術への投資（CVC）','銅のバリューチェーン全体に、新技術の網を張る')
vc2=['川上｜採掘','精鉱','川中｜製錬','川下｜製品']
for i,t in enumerate(vc2):
    x=R+i*126; b+=A(x,538,t,112,'bx',"height:22px")
    if i<3: b+=A(x+114,542,'→',None,'',"font-size:10px;color:#888")
for i,(n,p) in enumerate([('JETTI','川上'),('CiDRA','川上'),('Triland Metals','流通')]):
    b+=A(R+i*170,572,f'{n}<br><span class="lb">（{p}）</span>',150,'',"font-size:8px;border-left:2px solid #888;padding-left:6px")
b+=XC(R,612,W,110)
b+=FIG(R,652,150,90,'ref_cvc.png','現状の図：Copper Value Chain（P41）')+X(R+166,652,333,60,6.6,1.6)
b+=nt(R,766,'「CVC」の定義（コーポレート・ベンチャー・キャピタル／銅バリューチェーン）と、各投資先のバリューチェーン上の位置を要確認。新技術の把握が既存事業の高度化・将来価値に還元される点を訴求',W)
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
    y=126+i*32; b+=A(R+130,y,t,360,'',"font-size:7.6px;font-weight:400;border-left:1.4px solid #555;padding-left:6px")+X(R+137,y+12,360,24,6.2,1.4)
b+=A(R,226,'サプライチェーン確保の重要性・川上資源への参入障壁が増大',W,'bx',"height:20px;font-size:7.6px")
b+=A(R,252,'当社の取り組み',None,'lb',"font-weight:400;color:#444")
b+=A(R,266,'① 安定供給（安定的な資源確保）<br><span style="font-size:6.4px;color:#777">資源投資</span>',215,'bx',"height:30px;border-color:#444")+A(R+219,272,'⇄ 連携',60,'',"font-size:7px;text-align:center;color:#555")+A(R+284,266,'② 効率的な供給<br><span style="font-size:6.4px;color:#777">トレーディング</span>',215,'bx',"height:30px;border-color:#444")
b+=X(R,300,215,40,6.2,1.4)+X(R+284,300,215,40,6.2,1.4)
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
open('daiwari_v3.html','w').write(f'<!doctype html><meta charset=utf-8>{links}<style>{CSS}</style>'+''.join(pages))
