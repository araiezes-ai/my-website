H=open('sheet11.py').read().split("'''")[1]
p='<div class="pg"><div class="a lb" style="left:40px;top:30px">COVER STUDY 13 ／ LAYERS</div><div class="a h1" style="left:40px;top:46px">斜めに上がる3本の帯と、重なりずれる面</div>'
p+='''<div class="a s" style="left:40px;top:80px;width:1110px"><span class="b">形の意味</span>　①3本の帯が、段々に高くなりながら右上へ抜けていく＝上昇・推進。3本＝事業投資・トレーディング・新しい価値づくり（CVC・新技術）。
②帯の片側の濃い縁＝厚み。紙の上の模様ではなく、実体のある金属の板＝実物資産を持ち、現場を動かしている重み。
③帯の上を半透明の淡い面がずれながら重なる＝三つの機能が重なり合い、互いに作用しながら回っていく（投資→事業→トレーディング→CVCの循環）。重なりの奥行きで、線を増やさずに上質さを出す。</div>'''
cols=[('J1　スチール','鉄鋼・金属の色。最も硬質で、重厚。'),('J2　カッパー','金属資源グループの色として。温かく、他の冊子と並べても識別しやすい。'),('J3　スチール＋カッパー','2本のスチール（いまの事業の土台）の先に、カッパーの1本（次の成長）。最も高い位置へ抜ける帯を銅にした。')]
for i,(t,d) in enumerate(cols):
    x=40+i*380
    p+=f'<div class="a cv" style="left:{x}px;top:172px;width:340px"><img src="s22/cv-{i+1}.png" style="width:340px;border:.5px solid #ccc"><div class="b t" style="margin-top:6px">{t}</div><div class="s">{d}</div></div>'
p+='</div>'
open('sheet22.html','w').write(H+p)
