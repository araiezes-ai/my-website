# 表紙 v22：参考イメージ（斜めに上がる幅広の帯／片側の濃い縁＝厚み／半透明の面が重なりずれる）を白地・3本で
import math
exec(open('cover20.py').read().split('P=[(front(G1()')[0])
K=1/math.tan(math.radians(58))   # 傾き：高さ1あたりの水平移動
def para(xb,y0,y1,W):            # 上下が水平な平行四辺形
    xt=xb+(y0-y1)*K
    return f'M{xb:.1f},{y0} L{xb+W:.1f},{y0} L{xt+W:.1f},{y1} L{xt:.1f},{y1}Z'
CS={'steel':('#232a32','#55616e','#8c98a5'),'copper':('#5e2c15','#a9603a','#d08b62')}
CNT=[0]
def BANDS(cols):
    CNT[0]+=1; px=f'p{CNT[0]}'
    o='<defs>'
    for k,c in enumerate(cols):
        d,m,l=CS[c]
        o+=(f'<linearGradient id="{px}bd{k}" gradientUnits="userSpaceOnUse" x1="0" y1="842" x2="595" y2="100">'
            f'<stop offset="0" stop-color="{m}"/><stop offset=".6" stop-color="{l}"/><stop offset="1" stop-color="{m}"/></linearGradient>')
    o+='</defs>'
    spec=[(-70,900,430,118),(84,900,262,126),(238,900,-40,118)]   # (下端x, 下端y, 上端y, 幅)
    for k,((xb,y0,y1,W),c) in enumerate(zip(spec,cols)):
        d,m,l=CS[c]
        body=para(xb,y0,y1,W)
        o+=f'<path d="{body}" fill="url(#{px}bd{k})" opacity=".9"/>'+brushed(body,-58,200+k,bbox=(-300,-300,900,1100),op=.14)
        o+=f'<path d="{para(xb,y0,y1,16)}" fill="{d}" opacity=".95"/>'          # 片側の濃い縁＝厚み
        o+=f'<path d="{para(xb+(y0-(y1+46))*K,y1+46,y1,W)}" fill="{d}" opacity=".35"/>'  # 上端の影
    # 半透明の淡い面：帯の上をずれながら重なる
    o+=f'<path d="{para(20,700,300,92)}" fill="#eef0f2" opacity=".5"/>'
    o+=f'<path d="{para(250,560,150,70)}" fill="#eef0f2" opacity=".45"/>'
    return o
P=[(front(BANDS(['steel']*3),CS['steel'][1]),'J1_LAYERS_スチール'),
   (front(BANDS(['copper']*3),CS['copper'][1]),'J2_LAYERS_カッパー'),
   (front(BANDS(['steel','steel','copper']),CS['copper'][1]),'J3_LAYERS_スチール＋カッパー')]
open('cover22.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS2+'</style>'+''.join(p for p,_ in P))
import json; json.dump([n for _,n in P],open('cover22_names.json','w'),ensure_ascii=False)
