H=open('sheet11.py').read().split("'''")[1].replace('.cv img{width:190px;','.cv img{')
it=[('1','A-b 両輪の球','縦の線の球（事業投資）が背をまたいで裏表紙から表紙へ。表紙で横の線の球（トレーディング）と重なり、編み目の部分だけカッパーになる。','書体：セリフ'),
('2','A-2 二本の帯（ネイビー）','裏表紙では一本の帯だけが流れ、表紙でもう一本が加わって重なる。一本の流れに、もう一つの力が加わって両輪になる。','書体：サンセリフ'),
('3','A-2 二本の帯（カッパー）','同じ構成をカッパーで。金属資源グループらしさが最も強く、温かい。','書体：サンセリフ'),
('4','C-2 三本の帯','赤い一本が裏表紙から背をまたいで表紙へ通る。受け継いできた精神（裏）が、いまの事業（表の金属の帯）と並んで前へ進む。','書体：サンセリフ'),
('5a','届ける力（背で四分円）','波紋の中心を背の下端に置く。表紙・裏表紙それぞれ単体では1/4の円、見開くと半円になる。元の「四分円」の形を生かした案。','書体：セリフ'),('5b','届ける力（大きい円）','円を大きくして表紙に置き、直径の約1/4が背をまたいで裏表紙へかかる。円そのものがわかる案。','書体：セリフ')]
p='<div class="pg"><div class="a lb" style="left:40px;top:30px">COVER STUDY 07 ／ FRONT + BACK SPREADS</div><div class="a h1" style="left:40px;top:46px">表紙と裏表紙：見開いたときに一つの形になる</div>'
p+='<div class="a s" style="left:40px;top:80px;width:1110px">左が裏表紙、右が表紙。裏表紙には英文の所在地・URL（要確認）とロゴのみ。ロゴは表紙・裏表紙とも中央。広がる円の線は、源の近くは2.0pt、外へ行くほど0.55ptまで細く淡く（細すぎると遠目に形が消えるため）。形は背（中央）をまたいでつなげ、表紙単体でも成立するようにしている。</div>'
for i,(n,t,d,f) in enumerate(it):
    x=40+(i%3)*380; y=112+(i//3)*350
    p+=f'<div class="a cv" style="left:{x}px;top:{y}px;width:360px"><img src="s16/sp-{i+1}.png" style="width:360px;border:.5px solid #ccc"><div style="margin-top:6px"><span style="font-size:15px;font-weight:300;color:#B4693E">{n}</span> <span class="b t">{t}</span></div><div class="s">{d}</div><div class="s b" style="color:#24282d">{f}</div></div>'

p+='</div>'
open('sheet16.html','w').write(H+p)
