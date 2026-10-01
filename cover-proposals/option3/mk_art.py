src=open('inner_jp.py').read()
OVR=r'''
from PIL import Image as _PI
GOLD='#8a8f95'; BLUE='#C8102E'
CSS+=""".jh1:after{content:"";display:block;width:34px;height:1px;background:#C8102E;margin-top:12px}"""
IMG.update({'写真：銅鉱山':'_mr_project_02.png','写真：低炭素銅の取り組み':'_mr_project_04.png','写真：積出港・銅カソード':'mr_01_01@2x.webp',
 '写真：現場で働く人々':'_mr_project_01.png','写真：パートナー':'_mr_project_01.png','写真：BMA鉱山・重機':'r-047.png'})
def _enc(im):
    bf=_io.BytesIO(); im.convert('RGB').save(bf,'JPEG',quality=88); return 'data:image/jpeg;base64,'+base64.b64encode(bf.getvalue()).decode()
def strips(x,y,w,h,f,n=4,offs=(22,0,34,10),sq=True):
    im=_PI.open('img/'+f).convert('RGB'); H=h+max(offs); W0,H0=im.size
    r=max(w/W0,H/H0); im=im.resize((int(W0*r)+1,int(H0*r)+1)); l=(im.width-w)//2; t=(im.height-H)//2; im=im.crop((l,t,l+w,t+H))
    o=''; sw=w/n
    for i in range(n):
        a=int(i*sw); b_=int((i+1)*sw); hh=h+offs[i%len(offs)]
        o+=f'<img class="a" src="{_enc(im.crop((a,0,b_,hh)))}" style="left:{x+a}px;top:{y}px;width:{b_-a-1}px;height:{hh}px">'
    if sq:
        k=min(range(n),key=lambda i:offs[i%len(offs)]); o+=f'<div class="a" style="left:{x+int(k*sw)+int(sw)-9}px;top:{y+h+offs[k%len(offs)]-9 if False else y+h-9}px;width:18px;height:18px;background:#C8102E"></div>'
    return o
_ph0=ph
def ph(x,y,w,h,label):
    v=IMG.get(label)
    if v and w==249 and y==150:
        f=v if isinstance(v,str) else v[0]
        edge=595 if x<595 else 1190
        return strips(x,0,edge-x,150+h-34,f)
    return _ph0(x,y,w,h,label)
'''
src=src.replace("exec(open('jp_head.py').read())","exec(open('jp_head.py').read())"+OVR,1)
src=src.replace("b+=note(L,388,'コアメッセージ","b+=strips(400,0,195,330,'_mr_project_03.png',n=3,offs=(30,0,48))\nb+=note(L,388,'コアメッセージ",1)
src=src.replace("open('inner_jp.html','w').write(html)","open('inner_art.html','w').write(html)")

p5=open('blocks_p05.txt').read().replace("b+=bars(R,194,440,3)","b+=bars(R,194,220,3)\nb+=strips(R+292,0,1190-R-292,170,'mr_02_01@2x.webp')")
_a=src.index("# right\nb+=chap(R,52,'第1章','HOW WE WORK（仮）')"); _b=src.index("pages.append(spread(b,4,5))")+len("pages.append(spread(b,4,5))")
src=src[:_a]+p5+src[_b:]
_a=src.index("b+=chap(R,52,'第4章'"); _b=src.index("pages.append(spread(b,10,11))")+len("pages.append(spread(b,10,11))")
src=src[:_a]+open('blocks_p11.txt').read().replace('<br>より良い','より良い').replace('font-size:14.5px;font-weight:300;line-height:1.65;letter-spacing:.8px','font-size:13.5px;font-weight:300;line-height:1.65;letter-spacing:.6px')+src[_b:]
src=src.replace("b+=bars(L,170,440,4)","b+=bars(L,170,220,4)\nb+=strips(L+250,0,595-L-250,170,'_mr_project_05.png' if False else '_mr_project_03.png')",1)
open('inner_art.py','w').write(src)
