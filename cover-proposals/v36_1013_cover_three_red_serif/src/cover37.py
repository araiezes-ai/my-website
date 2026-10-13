# F1（スチール3本・前へ、そして上へ）× セリフ・均等行間のタイトル：①表紙のみ ②表裏見開き
exec(open('cover35.py').read().split('\ncss4=CSS2')[0])
ACC='#5f6c7a'
def lines3W(center_pts,c,gid,x2,W=20,gap=22):
    o=f'<defs>{mgrad(gid,c,0,842,x2,0)}</defs>'
    for k in (-1,0,1):
        pl=offset_poly(center_pts,k*(W+gap))
        quads,U,D=miter_quads(pl,W); outline=U+D[::-1]
        d='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in outline)+'Z'
        o+=f'<path d="{d}" fill="url(#{gid})"/>'+brushed(d,0,90+k,bbox=(-300,-300,1500,1100),op=.10)
    return o
F1PTS=[(-40,676),(250,676),(560,140),(640,1)]
front_svg=lines3W(F1PTS,STEEL,'fa',595)
spread_svg=lines3W([(-40,676)]+[(x+595,y) for x,y in F1PTS[1:]],STEEL,'fb',1190)
def frontOnly2(svg):
    return frontOnly(svg).replace(f'border-top:1.2px solid {RED_}',f'border-top:1.2px solid {ACC}')
open('cover37a.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS2+'</style>'+frontOnly2(front_svg))
css3=CSS2.replace('@page{size:210mm 297mm;margin:0}','@page{size:420mm 297mm;margin:0}')
open('cover37b.html','w').write('<!doctype html><meta charset=utf-8><style>'+css3+'</style>'+spread(spread_svg,'CG',ACC,True))
