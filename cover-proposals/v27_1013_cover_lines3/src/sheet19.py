H=open('sheet11.py').read().split("'''")[1]
p='<div class="pg"><div class="a lb" style="left:40px;top:30px">COVER STUDY 10 ／ THREE METAL LINES</div><div class="a h1" style="left:40px;top:46px">会社案内2026の「赤い3本」の強さを、金属の色で</div>'
p+='<div class="a s" style="left:40px;top:80px;width:1110px">会社案内2026の山形は、太い3本の線・紙の端で断ち落とし・明暗が流れる金属の光沢、の三つで強さを出している。この組み立てはそのままに、形の向きと色を金属資源グループのものに置き換えた（表紙のみ）。</div>'
cap=[('E','UP ／ 上を向く3本','頂点が上を向く3本の山形。下端で断ち落とし、紙面の下から上へ押し上げる。会社案内の「前へ」に対し、こちらは「上へ」＝成長・上昇。'),
('F','RISE ／ 前へ、そして上へ','左から水平に進んできた3本が、一点で向きを変えて右上へ抜けていく。トレーディングで前へ進む力が、事業投資で上へ伸びる力に変わる＝推進から上昇へ。')]
for i,(k,t,d) in enumerate(cap):
    x=40+i*565
    p+=f'<div class="a" style="left:{x}px;top:118px;width:545px"><span style="font-size:20px;font-weight:300;color:#5f6c7a">{k}</span> <span class="b t">{t}</span><div class="s" style="margin-top:3px">{d}</div></div>'
    for j,lab in enumerate(['スチール（鉄鋼・金属の色）','カッパー']):
        p+=f'<div class="a cv" style="left:{x+j*278}px;top:186px"><img src="s19/cv-{i*2+j+1}.png" style="width:262px;border:.5px solid #ccc"><div class="s" style="margin-top:4px">{k}{j+1}　{lab}</div></div>'
p+='</div>'
open('sheet19.html','w').write(H+p)
