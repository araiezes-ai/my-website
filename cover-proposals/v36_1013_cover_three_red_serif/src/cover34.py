# 三本の帯（赤）：タイトル周りを一つのブロックに（均等な行間・タイトル縮小）。表裏は切り離して提示
exec(open('cover33.py').read().split('P=[]')[0])
def head(font,acc):
    if font=='JO':
        return (f'<div class="a" style="left:48px;top:52px;width:36px;border-top:1.4px solid {acc}"></div>'
                f'<div class="a" style="left:48px;top:66px;font:400 14px/1 JO;letter-spacing:4.2px;color:{INK}">MITSUBISHI CORPORATION</div>'
                f'<div class="a" style="left:47px;top:92px;font:300 26px/1.0 JO;letter-spacing:5px;color:{INK}">MINERAL<br>RESOURCES</div>'
                f'<div class="a" style="left:48px;top:156px;font:400 14px/1 JO;letter-spacing:4.2px;color:#6b7178">CORPORATE PROFILE</div>')
    return (f'<div class="a" style="left:48px;top:58px;font:500 15px/1 CG;letter-spacing:3.8px;color:{INK}">MITSUBISHI CORPORATION</div>'
            f'<div class="a" style="left:48px;top:80px;width:36px;border-top:1.2px solid {acc}"></div>'
            f'<div class="a" style="left:46px;top:93px;font:300 32px/0.98 CG;letter-spacing:4.2px;color:{INK}">MINERAL<br>RESOURCES</div>'
            f'<div class="a" style="left:48px;top:168px;font:500 15px/1 CG;letter-spacing:3.8px;color:#6b7178">CORPORATE PROFILE</div>')
P=[]
for font,nm in (('JO','サンセリフ_Jost'),('CG','セリフ_CormorantGaramond')):
    P.append((spread(THREE_S(T),font,RED_,True),nm))
css=CSS2.replace('@page{size:210mm 297mm;margin:0}','@page{size:420mm 297mm;margin:0}')
open('cover34.html','w').write('<!doctype html><meta charset=utf-8><style>'+css+'</style>'+''.join(p for p,_ in P))
import json; json.dump([n for _,n in P],open('cover34_names.json','w'),ensure_ascii=False)
