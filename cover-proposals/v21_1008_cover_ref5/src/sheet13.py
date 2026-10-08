H=open('sheet11.py').read().split("'''")[1]
mot=[('1','つなぐ力','連なる半円','大きな半円が、形を小さく変えながら次へとつながっていく。掘る、運ぶ、加工する、届ける。最後の一つ（色）が需要家に届く価値。白地を広く残し、静かに見せる。'),
('2','持つ力','器と資源','器（資産・事業基盤）に円（資源）が半分沈んでいる。色の下半分は「いま持っている資源」、線だけの上半分は「これから持つ資源」。参考ポスターから構図を作り直したオリジナル。'),
('3','届ける力','四分円の同心線','角の一点（源＝鉱山・権益）から、線が波紋のように広がる。世界中の需要家へ届く供給網を、地図を使わずに表現する。'),
('4','両輪','二つのU','二つの大きなU（事業投資とトレーディング）が、一本一本の線で途切れずに結ばれている。真ん中の点は、両輪がかみ合うところで生まれる価値。'),
('5','積み重ねる力','積み石','細い線で描いた三つの石。下の二段は数十年かけて築いた権益と信頼、色を変えた最上段は、その上にこれから積む次の一段（新技術・CVC）。')]
p='<div class="pg"><div class="a lb" style="left:40px;top:30px">COVER STUDY 04 ／ 5 PATTERNS × 2 COLOUR PAIRS</div><div class="a h1" style="left:40px;top:46px">参考ポスター5型を、金属資源グループの「力」として意味づける</div>'
p+='<div class="a s" style="left:40px;top:78px;width:1110px">白地に2色（上段：カッパー × グラファイト／下段：朱 × グラファイト）。線は1本で見せず、束ねて面にする（線幅2.4〜6.6pt）。形は大きく、要素は少なく、白地を広く残して「大人っぽいシンプル」に寄せた。</div>'
cw=196; gx=40
for i,(n,t,f,d) in enumerate(mot):
    x=gx+i*(cw+26)
    p+=f'<div class="a" style="left:{x}px;top:116px;width:{cw+10}px"><span style="font-size:18px;font-weight:300;color:#B4693E">{n}</span> <span class="b t">{t}</span> <span class="s">／{f}</span><div class="s" style="margin-top:3px">{d}</div></div>'
    for j in range(2):
        p+=f'<div class="a cv" style="left:{x}px;top:{212+j*300}px"><img src="s13/cv-{i*2+j+1:02d}.png" style="width:{cw}px"></div>'
p+='</div>'
open('sheet13.html','w').write(H+p)
