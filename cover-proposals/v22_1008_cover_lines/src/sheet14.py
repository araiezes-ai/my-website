H=open('sheet11.py').read().split("'''")[1]
it=[('A','両輪','縦の球 × 横の球','縦の線の球＝事業投資（資源の上流へ深く入る）。横の線の球＝トレーディング（世界へ横に広げる）。性格の違う二つが重なると、縦と横が編み目になる。両輪がかみ合うところに価値が生まれる。','a：右の球をカッパーに','b：重なった部分だけカッパー'),
('B','向きを変える力','流れの転換','横に流れてきた線が、一点で向きを変え、上へ伸びていく。資源の流れを、社会が必要とする方向へ向け直す。需給をつなぎ、流れを変えるのが総合商社の役割。紙の端から端まで断ち落として、流れが紙面の外へ続いていくように見せる。','a：カッパー一色','b：グラファイトからカッパーへ（原料が価値に変わる）')]
p='<div class="pg"><div class="a lb" style="left:40px;top:30px">COVER STUDY 05</div><div class="a h1" style="left:40px;top:46px">細い線の「両輪」と、向きを変える「流れ」</div>'
for i,(m,t,f,d,va,vb) in enumerate(it):
    x=40+i*575
    p+=f'<div class="a" style="left:{x}px;top:96px;width:540px"><span style="font-size:20px;font-weight:300;color:#B4693E">{m}</span> <span class="b t">{t}</span> <span class="s">／{f}</span><div class="s" style="margin-top:4px">{d}</div></div>'
    for j,v in enumerate((va,vb)):
        p+=f'<div class="a cv" style="left:{x+j*278}px;top:170px"><img src="s14/cv-{i*2+j+1}.png" style="width:268px"><div class="s" style="margin-top:6px">{v}</div></div>'
p+='</div>'
open('sheet14.html','w').write(H+p)
