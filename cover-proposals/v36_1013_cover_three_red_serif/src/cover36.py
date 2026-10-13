# 三本の帯（赤）・セリフ：①表紙のみ（単体で完結）②表裏がつながる見開き
exec(open('cover34.py').read().split('\nP=[]\n')[0])
def frontOnly(svg):
    foot=('<rect x="0" y="772" width="600" height="90" fill="#fff"/><line x1="48" y1="784" x2="547" y2="784" stroke="#9aa0a6" stroke-width=".5"/>'+logo(297.5-66,808))
    bg=('<defs><linearGradient id="bgf" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff"/><stop offset=".6" stop-color="#fff"/><stop offset="1" stop-color="#eceef0"/></linearGradient></defs><rect width="595" height="842" fill="url(#bgf)"/>')
    return f'<div class="pg"><svg class="a" style="left:0;top:0" width="595" height="842" viewBox="0 0 595 842">{bg}{svg}{foot}</svg>{head("CG",RED_)}</div>'
T=TONES['グラファイト']; RED_='#5f6c7a'
css4=CSS2
open('cover36a.html','w').write('<!doctype html><meta charset=utf-8><style>'+css4+'</style>'+frontOnly(THREE(T)))
css3=CSS2.replace('@page{size:210mm 297mm;margin:0}','@page{size:420mm 297mm;margin:0}')
open('cover36b.html','w').write('<!doctype html><meta charset=utf-8><style>'+css3+'</style>'+spread(THREE_S(T),'CG',RED_,True))
