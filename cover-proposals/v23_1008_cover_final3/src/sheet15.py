H=open('sheet11.py').read().split("'''")[1]
p='<div class="pg"><div class="a lb" style="left:40px;top:30px">COVER STUDY 06 ／ 3 DESIGNS × 2 TYPEFACES</div><div class="a h1" style="left:40px;top:46px">残す3案と、三菱商事の過去のクリエイティブから選んだ書体</div>'
p+='''<div class="a s" style="left:40px;top:80px;width:1110px"><span class="b">書体の根拠</span>　三菱商事の英字は2系統。①<span class="b">クラシックなセリフの大文字＋広い字間</span>：統合報告書2026「INTEGRATED STRENGTH」、Webの英字見出し（PHILOSOPHY AND PRINCIPLES／COMPANY ほか）。②<span class="b">幾何学的なサンセリフの大文字＋広い字間</span>：会社案内2026「CORPORATE BROCHURE 2026」。どちらも細めのウエイトで、字間を大きく取るのが共通点。<br>
今回は ①に <span class="b">Cormorant Garamond Light</span>、②に <span class="b">Jost Light</span>（Futura系）をあてた。いずれもオープンライセンスで、本番ではモリサワ等の同系統書体（例：①Trajan／Adobe Garamond、②Futura PT）への差し替えも可能。</div>'''
cols=[('A-b','両輪の球','縦の線の球＝事業投資（深さ）、横の線の球＝トレーディング（広がり）。重なりが編み目になり、そこだけカッパー。円の位置は紙面中央・やや上に揃え、左右の余白を等しくした。','推奨：セリフ。細い線と、セリフの細い先端が呼応する。理知的で静か。'),
('A-2','二本の帯','事業投資とトレーディングの二本の帯が、同じ方向へ重なっていく。重なった部分が最も深い色。ネイビー×グラファイトの金属質。','推奨：サンセリフ。幾何学的な帯と、幾何学的な文字が揃う。会社案内2026と地続き。'),
('C-2','三本の帯','帯を三本まで減らした。長さの違う二本の金属の帯と、細い赤の一本。読み方は二通り：投資・トレーディング・CVCの三つの機能、あるいは三綱領。説明しすぎない余白を残す。','推奨：サンセリフ。要素が少ない分、文字も直線的に。セリフ版はより格調高く。')]
for i,(k,t,d,f) in enumerate(cols):
    x=40+i*380
    p+=f'<div class="a" style="left:{x}px;top:150px;width:360px"><span style="font-size:18px;font-weight:300;color:#B4693E">{k}</span> <span class="b t">{t}</span><div class="s" style="margin-top:3px;height:54px">{d}</div><div class="s b" style="color:#24282d">{f}</div></div>'
    for j in range(2):
        lab=['セリフ（Cormorant Garamond）','サンセリフ（Jost）'] if i==0 else ['サンセリフ（Jost）','セリフ（Cormorant Garamond）']
        wd=[256,96][j]; lx=[x,x+266][j]
        p+=f'<div class="a cv" style="left:{lx}px;top:258px;width:{wd}px"><img src="s15/cv-{i*2+j+1}.png" style="width:{wd}px"><div class="s" style="margin-top:4px">{lab[j]}{"（推奨）" if j==0 else ""}</div></div>'
p+='</div>'
open('sheet15.html','w').write(H+p)
