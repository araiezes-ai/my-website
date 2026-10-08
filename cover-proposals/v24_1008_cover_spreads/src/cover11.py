# 表紙 v11：三菱商事の既存クリエイティブ文法（太い面・断ち落とし・方向性・透明の重なり・金属の質感）に合わせた3モチーフ×3配色
import base64, math, random
N_='f/ns/package/files/'
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
INK='#24282d'; RED='#C8102E'
CW={ # 配色：各3トーン（濃・中・淡）＋金属ハイライト
 '1':dict(name='銅アクセント',t=[('#5e2c17','#a65a33','#d99a6c'),('#7b3a1e','#c27a4a','#ecc19b'),('#9c5a36','#dca27a','#f4dcc6')],sub='#4a4f56',acc=None),
 '2':dict(name='ネイビー×グラファイト＋赤一点',t=[('#16233a','#2c4466','#5d7896'),('#30363e','#59616b','#9aa2ab'),('#5d7896','#93a6ba','#d3dbe3')],sub='#30363e',acc=RED),
 '3':dict(name='メタリック・ディープゴールド',t=[('#4e3b17','#8f6d34','#c9a868'),('#6b5226','#ad8a4c','#e2cc98'),('#8f7444','#cdb27c','#f1e5c6')],sub='#4a4f56',acc=None),
}
def mark(x,y,s=6.6):
    o=''
    for th in (-90,30,150):
        p=lambda a,d:(x+d*math.cos(math.radians(a)),y+d*math.sin(math.radians(a)))
        q=[(x,y),p(th-30,s),p(th,s*math.sqrt(3)),p(th+30,s)]
        o+='<path d="M'+' L'.join(f'{a:.2f},{b:.2f}' for a,b in q)+'Z" fill="#E60012"/>'
    return o
def logo(x,y,s=6.2,fs=11.8):
    return mark(x,y,s)+f'<text x="{x+17*s/6.6}" y="{y+4*s/6.6}" font-family="Liberation Serif" font-size="{fs}" fill="#1a1a1a">Mitsubishi Corporation</text>'
CSS=f"""@font-face{{font-family:NS;font-weight:300;src:url(data:font/woff2;base64,{b64(N_+'noto-sans-latin-300-normal.woff2')})}}
@font-face{{font-family:NS;font-weight:500;src:url(data:font/woff2;base64,{b64(N_+'noto-sans-latin-500-normal.woff2')})}}
@page{{size:210mm 297mm;margin:0}}*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#fff}}
.pg{{position:relative;width:595px;height:842px;overflow:hidden;background:#fff;page-break-after:always;zoom:1.3333;font-family:NS}}
.a{{position:absolute}}
.k1{{font-weight:500;font-size:10px;letter-spacing:3.2px;color:{INK}}}
.ttl{{font-weight:300;font-size:30px;line-height:1.18;letter-spacing:4px;color:{INK}}}
.k2{{font-weight:300;font-size:10px;letter-spacing:3px;color:#6b7178}}
"""
def page(svg,cw):
    acc=CW[cw]['acc'] or CW[cw]['t'][0][1]
    t=(f'<div class="a k1" style="left:48px;top:74px">MITSUBISHI CORPORATION</div>'
       f'<div class="a" style="left:48px;top:104px;width:3px;height:74px;background:{acc}"></div>'
       f'<div class="a ttl" style="left:62px;top:102px">MINERAL<br>RESOURCES</div>'
       f'<div class="a k2" style="left:62px;top:192px">CORPORATE PROFILE</div>')
    bg=('<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".55" stop-color="#ffffff"/><stop offset="1" stop-color="#eceef0"/></linearGradient></defs>'
        '<rect width="595" height="842" fill="url(#bg)"/>')
    foot=f'<line x1="48" y1="784" x2="547" y2="784" stroke="#9aa0a6" stroke-width=".5"/>'+logo(400,806)
    return f'<div class="pg"><svg class="a" style="left:0;top:0" width="595" height="842" viewBox="0 0 595 842">{bg}{svg}{foot}</svg>{t}</div>'
UID=[0]
def metal(c,ang=0):
    """金属グラデ（濃→中→ハイライト→中→濃）"""
    UID[0]+=1; i=f'm{UID[0]}'; d,m,l=c
    r=math.radians(ang); x2=.5+.5*math.cos(r); y2=.5+.5*math.sin(r)
    g=(f'<linearGradient id="{i}" x1="{1-x2:.2f}" y1="{1-y2:.2f}" x2="{x2:.2f}" y2="{y2:.2f}">'
       f'<stop offset="0" stop-color="{d}"/><stop offset=".38" stop-color="{m}"/><stop offset=".56" stop-color="{l}"/><stop offset=".72" stop-color="{m}"/><stop offset="1" stop-color="{d}"/></linearGradient>')
    return i,g
def brushed(clip_d,ang,seed,bbox=(-200,-200,1000,1200),op=.22):
    """面の内側だけに走る細い筋目（ヘアライン＝金属の質感として使う）"""
    UID[0]+=1; cid=f'c{UID[0]}'; random.seed(seed)
    o=f'<clipPath id="{cid}"><path d="{clip_d}"/></clipPath><g clip-path="url(#{cid})"><g transform="rotate({ang} 300 420)">'
    y=bbox[1]
    while y<bbox[3]:
        a=random.random()**2*op; col='#ffffff' if random.random()<.55 else '#000000'
        o+=f'<line x1="{bbox[0]}" y1="{y:.1f}" x2="{bbox[2]}" y2="{y:.1f}" stroke="{col}" stroke-width="{random.choice((.35,.5,.7))}" opacity="{a:.3f}"/>'
        y+=random.uniform(1.1,2.6)
    return o+'</g></g>'
def band(p0,p1,w):
    dx,dy=p1[0]-p0[0],p1[1]-p0[1]; L=math.hypot(dx,dy); nx,ny=-dy/L*w/2,dx/L*w/2
    q=[(p0[0]+nx,p0[1]+ny),(p1[0]+nx,p1[1]+ny),(p1[0]-nx,p1[1]-ny),(p0[0]-nx,p0[1]-ny)]
    return 'M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in q)+'Z', math.degrees(math.atan2(dy,dx))

def M1(cw):  # 両輪：二つの帯が一つの方向へ重なっていく
    T=CW[cw]['t']; o='<defs>'; gs=[]
    for k,c in enumerate(T[:2]):
        i,g=metal(c,-60); o+=g; gs.append(i)
    o+='</defs>'
    dA,aA=band((-60,905),(680,470),118)
    dB,aB=band((-60,640),(680,545),118)
    o+=f'<path d="{dB}" fill="url(#{gs[1]})" opacity=".78"/>'+brushed(dB,aB,1)
    o+=f'<path d="{dA}" fill="url(#{gs[0]})" opacity=".82" style="mix-blend-mode:multiply"/>'+brushed(dA,aA,2)
    return o
def M2(cw):  # 循環上昇：一本の帯が向きを変えながら上へ（ぐるぐるを横から見たらせん）
    T=CW[cw]['t']; o='<defs>'; gs=[]
    for c in (T[0],T[1],T[0]):
        i,g=metal(c,-70); o+=g; gs.append(i)
    o+='</defs>'
    pts=[(-60,800),(470,700),(170,575),(680,470)]
    W=[64,64,64]
    def off(p0,p1,w):
        dx,dy=p1[0]-p0[0],p1[1]-p0[1]; L=math.hypot(dx,dy); return (-dy/L*w,dx/L*w)
    def isect(a,da,b,db):
        den=da[0]*db[1]-da[1]*db[0]; t=((b[0]-a[0])*db[1]-(b[1]-a[1])*db[0])/den; return (a[0]+t*da[0],a[1]+t*da[1])
    def side(sg):
        segs=[]
        for k in range(3):
            n=off(pts[k],pts[k+1],sg*32); segs.append(((pts[k][0]+n[0],pts[k][1]+n[1]),(pts[k+1][0]-pts[k][0],pts[k+1][1]-pts[k][1])))
        P=[segs[0][0]]
        for k in range(2): P.append(isect(segs[k][0],segs[k][1],segs[k+1][0],segs[k+1][1]))
        P.append((segs[2][0][0]+segs[2][1][0],segs[2][0][1]+segs[2][1][1])); return P
    U,Dn=side(1),side(-1)
    for k in range(3):
        q=[U[k],U[k+1],Dn[k+1],Dn[k]]; d='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in q)+'Z'
        a=math.degrees(math.atan2(pts[k+1][1]-pts[k][1],pts[k+1][0]-pts[k][0]))
        fill=f'url(#{gs[k]})'
        if CW[cw]['acc'] and k==1: fill=RED
        o+=f'<path d="{d}" fill="{fill}"/>'+brushed(d,a,10+k)
    # 折り目（稜線）
    for k in (1,2): o+=f'<line x1="{U[k][0]:.1f}" y1="{U[k][1]:.1f}" x2="{Dn[k][0]:.1f}" y2="{Dn[k][1]:.1f}" stroke="#ffffff" stroke-width=".8" opacity=".7"/>'
    return o
def M3(cw):  # 積層：上流から下流へ、資源が価値になっていく層（鉱床の地層とバリューチェーン）
    T=CW[cw]['t']; o='<defs>'; gs=[]
    flat=[T[0],T[0],T[1],T[1],T[2],T[2]]
    for c in flat:
        i,g=metal(c,0); o+=g; gs.append(i)
    o+='</defs>'
    rows=[(250,34),(196,34),(150,34),(318,34),(232,34),(110,34)]
    y=504
    for k,(x,h) in enumerate(rows):
        d=f'M{x},{y} L600,{y} L600,{y+h} L{x},{y+h}Z'
        fill=f'url(#{gs[k]})'
        if CW[cw]['acc'] and k==3: fill=RED
        o+=f'<path d="{d}" fill="{fill}"/>'+brushed(d,0,20+k,op=.28)
        y+=h+9
    return o
pages=[]
for mk,mf,mn in [('A',M1,'両輪'),('B',M2,'循環上昇'),('C',M3,'積層')]:
    for cw in '123':
        pages.append((mk,cw,mn,page(mf(cw),cw)))
open('cover11.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS+'</style>'+''.join(p for *_,p in pages))
import json; json.dump([(a,b,c) for a,b,c,_ in pages],open('cover11_idx.json','w'),ensure_ascii=False)
