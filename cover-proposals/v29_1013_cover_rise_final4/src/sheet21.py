H=open('sheet11.py').read().split("'''")[1]
p='<div class="pg"><div class="a lb" style="left:40px;top:30px">COVER STUDY 12 ／ RISE — MEANING</div><div class="a h1" style="left:40px;top:46px">前へ、そして上へ：F1・G1の意味づけと、線画の2案</div>'
p+='<div class="a s" style="left:40px;top:80px;width:1110px">共通の読み方：水平に進む線＝トレーディング（世界をつなぎ、モノを前へ動かす力）。折れて上へ伸びる線＝事業投資（資産に深く入り、価値を上へ積み上げる力）。一点で向きを変える＝両輪が一つの流れとしてつながり、「推進」が「上昇」に変わる瞬間。</div>'
cols=[('s21/f1-3.png','F1　三本が、そろって向きを変える','同じ幅・同じ間隔の3本が、乱れずに並走し、同じ一点で上へ向きを変える。グループの数多くの事業と人が、一つの意思でそろって動く——これが総合商社の「総合力」。そろっているから、向きを変えるときも速く、強い。スチールの光沢は、鉄鋼を支える原料と、それを扱ってきた歴史の重み。'),
('s21/g1-1.png','G1　太さの違う三つの力が、同じ方向へ','太い1本＝事業投資（大きな資産と長い時間軸）。中の1本＝トレーディング（世界をつなぐ流れ）。細いカッパーの1本＝新しい価値づくり（銅・CVC・新技術）。役割も重さも違う三つが、同じ方向へ進み、いちばん細い線が内側＝先頭を走る。いまの強みの上に、次の一手を重ねていく姿。'),
('s21/h-1.png','H1　線画・同じ幅','F1を、球の線画と同じ0.6ptの細線の束で。水平に進むあいだはグラファイト、上へ向かうにつれてカッパーへ色づく＝流れの中で、資源が価値に変わっていく。'),
('s21/h-2.png','H2　線画・太さ違い','G1を細線の束で。太さは線の本数の違い（14本・7本・6本）で表す。重いものほど多くの線が束ねられている。カッパーの束が先頭を走る。')]
for i,(f,t,d) in enumerate(cols):
    x=40+i*282
    p+=f'<div class="a cv" style="left:{x}px;top:132px;width:262px"><img src="{f}" style="width:262px;border:.5px solid #ccc"><div class="b t" style="margin-top:6px">{t}</div><div class="s">{d}</div></div>'
p+='<div class="a s" style="left:40px;top:780px;width:1110px;color:#8a9096">書体：F1・G1はJost（会社案内2026の系譜）、H1・H2は細線と呼応するCormorant Garamond。</div></div>'
open('sheet21.html','w').write(H+p)
