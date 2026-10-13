H=open('sheet11.py').read().split("'''")[1]
p='<div class="pg"><div class="a lb" style="left:40px;top:30px">COVER STUDY 11 ／ RISE, DIFFERENTIATED</div><div class="a h1" style="left:40px;top:46px">会社案内2026の文法は受け継ぎ、組み立てで独自性を出す</div>'
p+='<div class="a s" style="left:40px;top:80px;width:1110px">受け継ぐもの：図形は3つ／向き（前へ、そして上へ）／金属の質感。　変えたもの：①3本の役割（太さ違い・折れ位置のずれ）②1本だけカッパー＝金属資源グループの色　③つやのある光沢ではなく、ヘアライン加工のマットな金属＝素材そのものの表情。</div>'
cols=[('s20/cv-1.png','G1　太さ違い','太・中・細の3本。太い2本はスチール（事業投資・トレーディングの土台）、いちばん細い1本がカッパーで、いちばん内側＝先頭を走る。細くても先を行く新しい力（CVC・新技術）。'),
('s20/cv-2.png','G2　折れ位置ずらし','3本が順番に向きを変えて上がっていく。一斉にではなく、段階的に上昇する。中央の1本だけカッパー＝グループの核。3本の間隔が上がるほど開き、伸びやかに見える。'),
('s20/f1.png','参考：前回F1','同じ太さ・同じ間隔の3本と、つやのある光沢。会社案内2026と組み立てが近いため不採用。')]
for i,(f,t,d) in enumerate(cols):
    x=40+i*380
    p+=f'<div class="a cv" style="left:{x}px;top:138px;width:340px"><img src="{f}" style="width:{340 if i<2 else 250}px;border:.5px solid #ccc"><div class="b t" style="margin-top:6px">{t}</div><div class="s">{d}</div></div>'
p+='</div>'
open('sheet20.html','w').write(H+p)
