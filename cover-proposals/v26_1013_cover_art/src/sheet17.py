H=open('sheet11.py').read().split("'''")[1]
it=[('A','FOLD ／ 一枚の帯','一枚の銅の帯が、裏表紙の下から背をまたいで上がり、表紙で一度だけ折れて、上へ抜けていく。折り目で帯の表と裏が入れ替わる——事業投資とトレーディングは別々の二つではなく、一枚の帯の表と裏。折れる一点は、新しい段階へ向きを変える転換点でもある。',
'①一つ（一枚の帯）②面：帯幅は紙幅の約9%　③裏表紙の下端と表紙の上端で断ち落とし　④上へ　⑤奥行きは折り目の明暗と金属のヘアライン　⑥カッパー'),
('B','ARC ／ 二つの弧','半径の違う二つの銅の弧が、裏表紙の下から同じ方向へ立ち上がり、表紙の上で交わって右へ抜けていく。大きな金属彫刻の曲面のように、線ではなく「面の弧」で見せる。二つの軌道＝事業投資とトレーディング。交わるところが最も深い色になる＝両輪がかみ合うところに価値が生まれる。',
'①一つ（二本で一組の弧）②面：帯幅は紙幅の約7〜9%　③下端と右端で断ち落とし　④上へ、前へ　⑤半透明の重なり＋旋盤の挽き目のような同心の筋　⑥カッパー')]
p='<div class="pg"><div class="a lb" style="left:40px;top:30px">COVER STUDY 08 ／ ART × SIMPLE</div><div class="a h1" style="left:40px;top:46px">アートとしての一枚、シンプルな一つの形：2案</div>'
p+='<div class="a s" style="left:40px;top:80px;width:1110px">COVER STUDY 02でまとめた三菱商事の6つの文法（モチーフは一つ／主役は面／断ち落とし／向き／重なりと質感／色は一つ）に厳密に沿って作った。色はカッパー一色、書体はJost（会社案内2026の系譜）。左が裏表紙、右が表紙。</div>'
for i,(k,t,d,r) in enumerate(it):
    x=40+i*565
    p+=f'<div class="a cv" style="left:{x}px;top:112px;width:545px"><img src="s17/sp-{i+1}.png" style="width:545px;border:.5px solid #ccc"><div style="margin-top:8px"><span style="font-size:20px;font-weight:300;color:#B4693E">{k}</span> <span class="b t">{t}</span></div><div class="s" style="margin-top:3px">{d}</div><div class="s" style="margin-top:6px;color:#24282d"><span class="b">6つの文法</span>　{r}</div></div>'
p+='</div>'
open('sheet17.html','w').write(H+p)
