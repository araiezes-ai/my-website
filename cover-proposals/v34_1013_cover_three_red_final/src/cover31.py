# 表紙 v31：A-2（二本の帯・半透明の金属が交差）の文法で3本。表紙のみ
exec(open('cover20.py').read().split('P=[(front(G1()')[0])
TONES={
 'ネイビー':[('#16233a','#2c4466','#5d7896'),('#30363e','#59616b','#9aa2ab'),('#1f2f4a','#3d5878','#8fa6be')],
 '赤':[('#3e040d','#a3122a','#e8485c'),('#30363e','#59616b','#9aa2ab'),('#5a0a16','#8f1a2c','#d0606e')],
 'グラファイト':[('#1d242c','#5f6c7a','#e3e8ee'),('#30363e','#59616b','#9aa2ab'),('#0e1115','#2f363e','#8f9aa6')]}
def THREE(T):
    o='<defs>'; gs=[]
    for c in T:
        i,g=metal(c,-60); o+=g; gs.append(i)
    o+='</defs>'
    specs=[((-60,742),(680,560),92,1,.80),   # 長く緩やかな帯（土台）
           ((-60,640),(680,392),70,0,.82),   # もう一本、少し急に
           ((300,900),(680,330),96,2,.84)]   # 急角度で交差して上へ抜ける帯
    for k,(p0,p1,w,gi,op) in enumerate(specs):
        d,a=band(p0,p1,w)
        o+=f'<path d="{d}" fill="url(#{gs[gi]})" opacity="{op}" style="mix-blend-mode:multiply"/>'+brushed(d,a,500+k)
    return o
P=[(front(THREE(TONES[n]),TONES[n][0][1] if n!='赤' else '#a3122a'),f'M_三本の帯_{n}') for n in ('ネイビー','赤','グラファイト')]
open('cover31.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS2+'</style>'+''.join(p for p,_ in P))
import json; json.dump([n for _,n in P],open('cover31_names.json','w'),ensure_ascii=False)
