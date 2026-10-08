H='''<!doctype html><meta charset=utf-8><link rel="stylesheet" href="f/nsjp/package/300.css"><link rel="stylesheet" href="f/nsjp/package/400.css"><link rel="stylesheet" href="f/nsjp/package/700.css"><style>
@page{size:420mm 297mm;margin:0}*{margin:0;padding:0;box-sizing:border-box}
.pg{position:relative;width:1190px;height:842px;overflow:hidden;background:#fff;page-break-after:always;zoom:1.3333;font-family:'Noto Sans JP';color:#24282d}
.a{position:absolute}.h1{font-size:21px;font-weight:400;letter-spacing:1px}.lb{font-size:9px;letter-spacing:2.4px;color:#8a9096;font-weight:400}
.t{font-size:10.2px;line-height:1.75;font-weight:400}.s{font-size:8.6px;line-height:1.6;color:#555b62}.b{font-weight:700}
.ref img{height:150px;border:.5px solid #ddd;display:block}.ref .s{margin-top:6px}
.num{font-size:22px;font-weight:300;color:#C8102E;width:30px;display:inline-block;vertical-align:top}
.pt{display:inline-block;width:470px;vertical-align:top}
.cv img{width:190px;border:.5px solid #ccc;display:block}
.rl{border-top:.5px solid #9aa0a6}
</style>'''
refs=[('ref_cg.png','会社案内 Corporate Brochure 2026','赤の太い山形を3本。左端で断ち落とし、白地に大きな余白。'),
('ref_ar.png','統合報告書 2026「INTEGRATED STRENGTH」','半透明の山形が2025→2026→2027と前進。銀の金属面から虹色へ。細線は年号の軸だけ。'),
('ref_iday.png','Investor Day 2026（MCSV Creation Forum）','半透明の斜めの柱が段々に上がっていく。重なりで奥行きを出す。'),
('ref_sus.png','サステナビリティレポート 2025','緑〜紺の矢形が重なりながら上へ。'),
('ref_kab.png','株主通信（70周年号）','赤い太い帯が一本、紙面を横切る。')]
p1='<div class="pg"><div class="a lb" style="left:56px;top:44px">COVER STUDY 02 ／ 社内検討用</div>'
p1+='<div class="a h1" style="left:56px;top:62px">三菱商事のクリエイティブにおける「シンプル」と「幾何学」</div>'
p1+='<div class="a s" style="left:56px;top:96px;width:1060px">会社案内、統合報告書、IR、サステナビリティの各表紙（三菱商事Webサイト掲載、2025–2026年）を横に並べて見ると、先方の言う「シンプル」は「線が細い・要素が少ない」ではなく、「一つの太い形で言い切る」ことだとわかる。</div>'
x=56
for f,t,c in refs:
    from PIL import Image
    w,h=Image.open('s11/'+f).size; iw=int(150*w/h); cwid=max(iw,170)
    p1+=f'<div class="a ref" style="left:{x}px;top:132px;width:{cwid}px"><img src="s11/{f}"><div class="s"><span class="b">{t}</span><br>{c}</div></div>'
    x+=cwid+24
p1+='<div class="a rl" style="left:56px;top:362px;width:1078px"></div>'
p1+='<div class="a lb" style="left:56px;top:378px">FINDINGS ／ 共通する文法</div>'
pts=[('モチーフは一つだけ','地図・地球・建物のような説明的な絵は一冊も使っていない。抽象形を一つ置き、その意味は本文やコピーで語る。'),
('主役は「線」ではなく「面（帯）」','主役の形の幅は紙面幅の3〜10%。0.5pt前後の細線は、年号の軸や下部の罫線など「構造」にしか使っていない。'),
('断ち落として、中央で閉じない','形は紙の端から外へ続いていく。真ん中に閉じた図形を置かない（先方の「真ん中に大きな丸はNG」と同じ考え方）。'),
('向きがある：前へ、上へ','山形は前へ、柱と矢は上へ向かう。「成長」「前進」を、言葉を使わずに形だけで伝えている。'),
('奥行きは本数ではなく、重なりと質感で出す','線を増やすのではなく、半透明の重なりや金属的なグラデーション（銀、赤のメタリック）で上質さを出している。'),
('色は冊子ごとに一つ選ぶ','赤、銀〜スペクトル、青緑、緑紺と、媒体ごとに主役の色が違う。だから金属資源グループが自分の色を持つことは、三菱商事のルールの内側にある。')]
for k,(a,b) in enumerate(pts):
    col=k%2; row=k//2
    p1+=f'<div class="a" style="left:{56+col*540}px;top:{402+row*62}px"><span class="num">0{k+1}</span><span class="pt"><span class="b t">{a}</span><br><span class="s">{b}</span></span></div>'
p1+='<div class="a rl" style="left:56px;top:598px;width:1078px"></div>'
p1+='<div class="a lb" style="left:56px;top:614px">SO, THIN LINES? ／ 細い線は正しいか</div>'
p1+='''<div class="a t" style="left:56px;top:636px;width:520px">前回の5案（A〜E）は、主役を0.5pt前後のヘアラインだけで描いていた。上品ではあるが、三菱商事の「シンプル」が持つ<span class="b">太さと言い切る強さ</span>が足りず、遠くからは何が描かれているか分からない。<span class="b">主役を細線にするのは誤りだった</span>と判断した。</div>'''
p1+='''<div class="a t" style="left:610px;top:636px;width:524px">今回は主役を太い面（帯）に戻す。細線は二か所だけに残す。<br>① <span class="b">帯の内側の「筋目」</span>：金属のヘアライン加工の表情。細い線を「金属という素材の質感」として使う理由がここにある。<br>② <span class="b">下部の罫線</span>：会社案内と同じく、紙面の構造を示す線として使う。<br>つまり<span class="b">形は太く、質感は細く</span>。三菱商事の文法に乗りつつ、金属資源グループの冊子だとわかる表情にする。</div>'''
p1+='<div class="a s" style="left:56px;top:790px;width:1078px;color:#8a9096">出典：三菱商事Webサイト「会社案内」「統合報告書」「IRライブラリー」各ページ掲載の表紙画像（2026年10月8日閲覧）。社内検討用の参考として縮小掲載。</div></div>'
cap={'A':('両輪','投資（事業投資）とトレーディング、二本の帯が同じ方向へ向かって重なっていく。重なった部分が一番濃い＝両輪がかみ合うところに価値が生まれる。'),
'B':('循環上昇','一本の帯が向きを変えながら上へ進む。投資→事業運営→トレーディング→CVCの「ぐるぐる」を横から見たらせん。回るたびに一段上がる。'),
'C':('積層','長さの違う帯が右へ流れ出る。鉱床の地層であり、上流から下流へと価値が積み上がるバリューチェーンでもある。')}
cw=[('1','銅アクセント','グループの主力である銅の色。温かく、他の冊子と並べても埋もれない。'),
('2','ネイビー×グラファイト＋赤一点','最も「三菱商事らしい」配色。赤はコーポレートカラーとして一か所だけに使う。'),
('3','メタリック・ディープゴールド','最も格調が高い。ただし豪華に寄りすぎないよう、彩度を抑えた金にしている。')]
p2='<div class="pg"><div class="a lb" style="left:56px;top:40px">COVER STUDY 02 ／ 3 MOTIFS × 3 COLOURS</div><div class="a h1" style="left:56px;top:56px">表紙案：形は太く、質感は細く</div>'
for j,(n,nm,ds) in enumerate(cw):
    p2+=f'<div class="a" style="left:{312+j*206}px;top:96px;width:196px"><span class="b t" style="color:#C8102E">{n}</span> <span class="b t">{nm}</span><div class="s">{ds}</div></div>'
# covers: 3 rows would be too tall; layout = rows of motifs, each cover 190w x 269h → use smaller 170w
for i,m in enumerate('ABC'):
    y=146+i*228
    p2+=f'<div class="a" style="left:56px;top:{y}px;width:236px"><span class="b" style="font-size:18px;font-weight:300">{m}</span> <span class="b t">{cap[m][0]}</span><div class="s" style="margin-top:4px">{cap[m][1]}</div></div>'
    for j in range(3):
        p2+=f'<div class="a cv" style="left:{312+j*206}px;top:{y}px"><img src="s11/cv-{i*3+j+1}.png" style="width:152px"></div>'
p2+='''<div class="a" style="left:960px;top:146px;width:178px"><div class="lb">RECOMMENDATION</div>
<div class="t" style="margin-top:8px"><span class="b">本命：B × 1</span><br><span class="s">「ぐるぐる」と「つなぐ」を一つの形で言える唯一の案。銅は金属資源グループの顔として、全社の他の冊子と並べたときに一番識別しやすい。</span></div>
<div class="t" style="margin-top:12px"><span class="b">対抗：A × 2</span><br><span class="s">「両輪」が最もストレートに伝わる。配色は三菱商事の他の冊子と最も地続きにできる。</span></div>
<div class="t" style="margin-top:12px"><span class="b">15日の打ち合わせでは</span><br><span class="s">形（A/B/C）と色（1/2/3）を分けて選んでもらう。ホワイトボードで「意味」を描きながら決められるよう、形はどれも手で描けるくらい単純にしてある。</span></div>
<div class="t" style="margin-top:12px"><span class="b">中面への展開</span><br><span class="s">帯の一部を各章扉や見出しの帯として、そのまま切り出して使える（案③で使ってきた横の帯と同じ文法）。</span></div></div>'''
p2+='</div>'
open('sheet11.html','w').write(H+p1+p2)
