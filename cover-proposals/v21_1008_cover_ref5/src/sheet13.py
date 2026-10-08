H=open('sheet11.py').read().split("'''")[1]
mot=[('1','つなぐ力','連なる半円','大きな半円が、形を小さく変えながら次へとつながっていく。資源を掘り、運び、加工し、届ける。役割を受け渡していくバリューチェーンの連なり。'),
('2','持つ力','傾いた四角と円','重い四角（資産・事業基盤）が、円（資源）をしっかり抱えている。わずかな傾きは、止まらずに動き続ける姿勢。隅の点は、そこから生まれる新しい価値（CVC・新技術）。'),
('3','届ける力','四分円の同心線','角の一点（源＝鉱山・権益）から、線が波紋のように広がる。世界中の需要家へ届く供給網を、地図を使わずに表現する。'),
('4','両輪','二つのU','二つの大きなU（事業投資とトレーディング）が、一本一本の線で途切れずに結ばれている。真ん中の点は、両輪がかみ合うところで生まれる価値。'),
('5','積み重ねる力','積み石','形の違う三つの石が、ずれずに積み上がっている。数十年かけて築いてきた権益と信頼、そしてその上にさらに積む次の一段。')]
p='<div class="pg"><div class="a lb" style="left:40px;top:30px">COVER STUDY 04 ／ 5 PATTERNS × 2 COLOUR PAIRS</div><div class="a h1" style="left:40px;top:46px">参考ポスター5型を、金属資源グループの「力」として意味づける</div>'
p+='<div class="a s" style="left:40px;top:78px;width:1110px">白地に2色（上段：カッパー × グラファイト／下段：朱 × グラファイト）。線は1本で見せず、束ねて面にする（線幅2.4〜6.6pt）。形は紙面の6〜7割まで大きくし、端で断ち落とす。前回の案が負けていた「大きさ」「線の密度」「傾きの緊張感」を取り戻した。</div>'
cw=196; gx=40
for i,(n,t,f,d) in enumerate(mot):
    x=gx+i*(cw+26)
    p+=f'<div class="a" style="left:{x}px;top:116px;width:{cw+10}px"><span style="font-size:18px;font-weight:300;color:#B4693E">{n}</span> <span class="b t">{t}</span> <span class="s">／{f}</span><div class="s" style="margin-top:3px">{d}</div></div>'
    for j in range(2):
        p+=f'<div class="a cv" style="left:{x}px;top:{196+j*300}px"><img src="s13/cv-{i*2+j+1:02d}.png" style="width:{cw}px"></div>'
p+='</div>'
open('sheet13.html','w').write(H+p)
