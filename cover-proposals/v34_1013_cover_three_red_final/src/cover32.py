# 表紙 v32：三本の帯（赤）× 書体2種、裏表紙はそれぞれ独立したデザイン
exec(open('cover31.py').read().split('P=[(front(THREE')[0])
T=TONES['赤']; RED_='#a3122a'
def frontF(svg,font):
    foot=('<rect x="0" y="772" width="600" height="90" fill="#fff"/><line x1="48" y1="784" x2="547" y2="784" stroke="#9aa0a6" stroke-width=".5"/>'+logo(297.5-66,808))
    bg=('<defs><linearGradient id="bgf" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff"/><stop offset=".6" stop-color="#fff"/><stop offset="1" stop-color="#eceef0"/></linearGradient></defs><rect width="595" height="842" fill="url(#bgf)"/>')
    return f'<div class="pg"><svg class="a" style="left:0;top:0" width="595" height="842" viewBox="0 0 595 842">{bg}{svg}{foot}</svg>{head(font,RED_)}</div>'
def back(font):
    ff='JO' if font=='JO' else 'CG'; fz='8.5px' if font=='JO' else '10px'
    i,g=metal(T[0],0)
    svg=(f'<defs>{g}</defs><rect width="595" height="842" fill="#fff"/>'
         f'<rect x="277.5" y="700" width="40" height="3" fill="url(#{i})"/>'          # 表紙の帯を受ける、短い赤のメタリック
         +logo(297.5-66,742))
    txt=(f'<div class="a" style="left:0;width:595px;text-align:center;top:770px;font:400 {fz} {ff};letter-spacing:1.6px;color:#6b7178;line-height:1.9">'
         'Mitsubishi Corporation　Mineral Resources Group<br>2-3-1 Marunouchi, Chiyoda-ku, Tokyo 100-8086, Japan<br>www.mitsubishicorp.com</div>')
    return f'<div class="pg"><svg class="a" style="left:0;top:0" width="595" height="842" viewBox="0 0 595 842">{svg}</svg>{txt}</div>'
P=[]
for font,nm in (('JO','サンセリフ_Jost'),('CG','セリフ_CormorantGaramond')):
    P.append((frontF(THREE(T),font),f'表紙_{nm}'))
    P.append((back(font),f'裏表紙_{nm}'))
open('cover32.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS2+'</style>'+''.join(p for p,_ in P))
import json; json.dump([n for _,n in P],open('cover32_names.json','w'),ensure_ascii=False)
