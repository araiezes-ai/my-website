# 三本の帯（赤）：帯が裏表紙へ突き抜ける見開き × 書体2種
exec(open('cover32.py').read().split('def frontF')[0])
def THREE_S(T):
    o='<defs>'; gs=[]
    for c in T:
        i,g=metal(c,-60); o+=g; gs.append(i)
    o+='</defs>'
    def ext(p0,p1,x):  # 直線を左へ延長
        k=(p1[1]-p0[1])/(p1[0]-p0[0]); return (x,p0[1]+(x-p0[0])*k)
    # 見開き座標。2本は裏表紙の左下から入り、背をまたいで表紙の右上へ抜ける
    specs=[((-40,830),(1290,520),92,1,.80),((-40,760),(1290,380),70,0,.82),((895,900),(1275,330),96,2,.84)]
    for k,(q0,q1,w,gi,op) in enumerate(specs):
        d,a=band(q0,q1,w)
        o+=f'<path d="{d}" fill="url(#{gs[gi]})" opacity="{op}" style="mix-blend-mode:multiply"/>'+brushedW(d,a,500+k)
    return o
P=[]
for font,nm in (('JO','サンセリフ_Jost'),('CG','セリフ_CormorantGaramond')):
    P.append((spread(THREE_S(T),font,RED_,True),nm))
css=CSS2.replace('@page{size:210mm 297mm;margin:0}','@page{size:420mm 297mm;margin:0}')
open('cover33.html','w').write('<!doctype html><meta charset=utf-8><style>'+css+'</style>'+''.join(p for p,_ in P))
import json; json.dump([n for _,n in P],open('cover33_names.json','w'),ensure_ascii=False)
