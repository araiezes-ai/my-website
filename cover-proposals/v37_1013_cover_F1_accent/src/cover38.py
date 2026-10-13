# F1 スチール3本のうち1本を赤／カッパーに。サンセリフ、タイトルの線は社名とタイトルの間（均等な行間）
exec(open('cover37.py').read().split('\nF1PTS=')[0])
def head(font,acc):
    return (f'<div class="a" style="left:48px;top:60px;font:400 14px/1 JO;letter-spacing:4.2px;color:{INK}">MITSUBISHI CORPORATION</div>'
            f'<div class="a" style="left:48px;top:88px;width:36px;border-top:1.4px solid {acc}"></div>'
            f'<div class="a" style="left:47px;top:102px;font:300 26px/1.0 JO;letter-spacing:5px;color:{INK}">MINERAL<br>RESOURCES</div>'
            f'<div class="a" style="left:48px;top:168px;font:400 14px/1 JO;letter-spacing:4.2px;color:#6b7178">CORPORATE PROFILE</div>')
ACCS={'red':('#3e040d','#a3122a','#e8485c'),'copper':('#6e3519','#c27a4a','#efc6a2')}
def lines3A(center_pts,acc,gid,x2,W=20,gap=22):
    x0=x2-595   # 光の位置は常に表紙の座標で決める（見開きでも表紙部分は表紙単体と同じ光）
    gr=(mgrad(gid+"s",STEEL,x0,842,x2,0)+mgrad(gid+"a",acc,x0,842,x2,0)).replace('<linearGradient ','<linearGradient spreadMethod="reflect" ')
    o=f'<defs>{gr}</defs>'
    for k in (-1,0,1):
        pl=offset_poly(center_pts,k*(W+gap))
        quads,U,D=miter_quads(pl,W); outline=U+D[::-1]
        d='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in outline)+'Z'
        g=gid+('a' if k==-1 else 's')          # 内側（先頭）の1本だけアクセント色
        o+=f'<path d="{d}" fill="url(#{g})"/>'+brushed(d,0,90+k,bbox=(-300,-300,1500,1100),op=.10)
    return o
F1PTS=[(-40,676),(250,676),(560,140),(640,1)]
css3=CSS2.replace('@page{size:210mm 297mm;margin:0}','@page{size:420mm 297mm;margin:0}')
for nm,acc in ACCS.items():
    fs=lines3A(F1PTS,acc,'fa',595)
    ss=lines3A([(-40,676)]+[(x+595,y) for x,y in F1PTS[1:]],acc,'fb',1190)
    RED_=acc[1]; fo=frontOnly(fs)
    open(f'cover38_{nm}_a.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS2+'</style>'+fo)
    open(f'cover38_{nm}_b.html','w').write('<!doctype html><meta charset=utf-8><style>'+css3+'</style>'+spread(ss,'JO',acc[1],True))
