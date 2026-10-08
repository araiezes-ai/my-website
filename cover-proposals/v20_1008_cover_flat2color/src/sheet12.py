H=open('sheet11.py').read().split("'''")[1]
mot=[('A','両輪','面の半円＝「持つ」（事業投資）、線の半円＝「動かす」（トレーディング）。同じ地面に並ぶ二つで一つの力。'),
('B','循環','四つの四分円が回る。投資→事業運営→トレーディング→CVC。色が違う一枚は「いま動いている一手」。'),
('C','つなぐ','線の束が両側（資源の出し手と使い手）を結び、その間に価値（点）が生まれる。'),
('D','バリューチェーン','左の四角（原石）が、右へ進むほど角が取れて円（製品・価値）になる。上流から下流へ。'),
('E','持つ力','器（資産・事業基盤）が資源を抱えて支える。長く持ち続ける力。'),
('F','前へ','並んで進む矢の中で、一つだけ色が違う＝常に一手先を行く。会社案内の山形とも地続き。')]
pairs=[('1','カッパー × グラファイト'),('2','朱 × グラファイト'),('3','朱 × カッパー')]
p='<div class="pg"><div class="a lb" style="left:40px;top:30px">COVER STUDY 03 ／ 6 MOTIFS × 3 COLOUR PAIRS</div><div class="a h1" style="left:40px;top:46px">白地＋2色のフラットな幾何学。形ひとつに意味をひとつ</div>'
p+='<div class="a s" style="left:40px;top:78px;width:1110px">ルール：①白地に2色まで ②形は面か、線の「束」で面をつくる（線幅は2.5〜3.5pt。1本で見せるヘアラインは使わない）③一つの形に一つの意味。ホワイトボードで手描きできる単純さ ④地図・地球・鉱山・大きな中央の円・スリーダイヤの引用はしない</div>'
cw=150; gx=178
for i,(m,n,d) in enumerate(mot):
    x=gx+i*(cw+12)
    p+=f'<div class="a" style="left:{x}px;top:108px;width:{cw}px"><span style="font-size:16px;font-weight:300">{m}</span> <span class="b t">{n}</span><div class="s" style="height:56px">{d}</div></div>'
for j,(k,pn) in enumerate(pairs):
    y=178+j*218
    p+=f'<div class="a" style="left:40px;top:{y+80}px;width:126px"><span class="b t" style="color:#D24A2B">{k}</span> <span class="b t">{pn}</span></div>'
    for i in range(6):
        p+=f'<div class="a cv" style="left:{gx+i*(cw+12)}px;top:{y}px"><img src="s12/cv-{j*6+i+1:02d}.png" style="width:{cw}px"></div>'
p+='</div>'
open('sheet12.html','w').write(H+p)
