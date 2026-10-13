# 表紙 v22：参考イメージ（斜めに上がる幅広の帯／片側の濃い縁＝厚み／半透明の面が重なりずれる）を白地・3本で
import math
exec(open('cover20.py').read().split('P=[(front(G1()')[0])
K=1/math.tan(math.radians(58))   # 傾き：高さ1あたりの水平移動
def para(xb,y0,y1,W):            # 上下が水平な平行四辺形
    xt=xb+(y0-y1)*K
    return f'M{xb:.1f},{y0} L{xb+W:.1f},{y0} L{xt+W:.1f},{y1} L{xt:.1f},{y1}Z'
CS={'wine':('#5a0a13','#8f2230','#a8323f'),'mcred':('#7a0a1b','#be0f2c','#d42a43'),'steel':('#232a32','#55616e','#8c98a5'),'copper':('#5e2c15','#a9603a','#d08b62')}
CNT=[0]
def BANDS(cols):
    CNT[0]+=1; px=f'p{CNT[0]}'
    o='<defs>'
    for k,c in enumerate(cols):
        d,m,l=CS[c]
        o+=(f'<linearGradient id="{px}bd{k}" gradientUnits="userSpaceOnUse" x1="0" y1="842" x2="595" y2="100">'
            f'<stop offset="0" stop-color="{m}"/><stop offset=".6" stop-color="{l}"/><stop offset="1" stop-color="{m}"/></linearGradient>')
    o+='</defs>'
    spec=[(30,900,-60,86),(134,900,-60,86),(238,900,-60,86)]   # 3本とも下端から上端・右端へ突き抜ける。間隔18   # (下端x, 下端y, 上端y, 幅)
    for k,((xb,y0,y1,W),c) in enumerate(zip(spec,cols)):
        d,m,l=CS[c]
        body=para(xb,y0,y1,W)
        o+=f'<path d="{body}" fill="url(#{px}bd{k})" opacity=".96"/>'+brushed(body,-58,200+k,bbox=(-300,-300,900,1100),op=.07)
        o+=f'<path d="{para(xb,y0,y1,12)}" fill="{d}" opacity=".95"/>'          # 片側の濃い縁＝厚み
    # 半透明の淡い面：帯の上をずれながら重なる
    o+=f'<path d="{para(-90,900,380,64)}" fill="#eef0f2" opacity=".55"/>'
    o+=f'<path d="{para(196,640,250,52)}" fill="#eef0f2" opacity=".45"/>'
    return o
P=[(front(BANDS(['wine']*3),CS['wine'][1]),'K1_LAYERS_ワインレッド_突き抜け')]
open('cover24.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS2+'</style>'+''.join(p for p,_ in P))
import json; json.dump([n for _,n in P],open('cover24_names.json','w'),ensure_ascii=False)
