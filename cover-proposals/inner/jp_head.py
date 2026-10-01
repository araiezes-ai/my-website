import base64, math
from hl import hairmap
N='f/ns/package/files/'
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
CSS=f"""
@font-face{{font-family:NS;font-weight:300;src:url(data:font/woff2;base64,{b64(N+'noto-sans-latin-300-normal.woff2')})}}
@font-face{{font-family:NS;font-weight:400;src:url(data:font/woff2;base64,{b64(N+'noto-sans-latin-400-normal.woff2')})}}
@font-face{{font-family:NS;font-weight:500;src:url(data:font/woff2;base64,{b64(N+'noto-sans-latin-500-normal.woff2')})}}
@page{{size:420mm 297mm;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:NS,'Noto Sans JP',sans-serif;color:#2e3135;background:#fff}}
.sp{{position:relative;width:1190px;height:842px;overflow:hidden;background:#fff;page-break-after:always;zoom:1.3333}}
.sp:after{{content:"";position:absolute;left:595px;top:0;bottom:0;border-left:1px dashed #e4e6e8}}
.a{{position:absolute}}
.lab{{font-size:7.2px;letter-spacing:2.2px;color:#6b7076;font-weight:400;text-transform:uppercase;white-space:nowrap}}
.lab b{{display:inline-block;width:14px;height:1px;background:#C8102E;vertical-align:middle;margin-right:8px}}
.h1{{font-weight:300;font-size:25px;line-height:1.28;letter-spacing:.1px;color:#24272b}}
.h2{{font-weight:400;font-size:10.5px;letter-spacing:.3px;color:#2e3135}}
.h2:before{{content:"";display:block;width:16px;height:1px;background:#2e3135;margin-bottom:7px}}
.cap{{font-size:6.6px;letter-spacing:1.6px;color:#7a7f85;text-transform:uppercase}}
.num{{font-weight:300;color:#24272b;letter-spacing:-.3px;line-height:1}}
.body{{font-weight:300;font-size:8.6px;line-height:1.62;color:#45494e}}
.note{{font-family:'Noto Sans JP';font-weight:400;font-size:6.4px;color:#9a6a6f}}
.ph{{background-color:#f6f7f8;background-image:repeating-linear-gradient(90deg,#dfe2e5 0 .55px,transparent .55px 2.3px);display:flex;align-items:center;justify-content:center}}
.ph span{{font-family:'Noto Sans JP';font-size:7px;color:#8a8f95;background:#f6f7f8;padding:2px 6px}}
.bar{{height:2.4px;background:#e1e4e7;margin-bottom:6.4px}}
.rule{{position:absolute;height:0;border-top:.6px solid #cdd0d4}}
.vrule{{position:absolute;width:0;border-left:.6px solid #cdd0d4}}
.fol{{font-size:7px;letter-spacing:1.6px;color:#8a8f95}}
"""
def A(x,y,html,w=None,cls='',style=''):
    ws=f'width:{w}px;' if w else ''
    return f'<div class="a {cls}" style="left:{x}px;top:{y}px;{ws}{style}">{html}</div>'
from PIL import Image as _I
import io as _io
IMG={'画像：三綱領':('r-000.png','contain'),
'写真：鉱山（上流）':'x_vc_mine.jpg','写真：製錬所（中流）':'x_vc_smelter.jpg','写真：洋上風力（用途）':'x_vc_wind.jpg','写真：EV（需要家）':'x_vc_ev.jpg',
'写真：BMA鉱山・重機':'r-047.png','写真：原料炭':'r-048.png','写真：港湾・鉄道':'r-023.png','写真：パートナー':'r-051.png',
'写真：銅鉱山':'r-053.png','写真：低炭素銅の取り組み':'r-046.png','写真：安定的な供給基盤':'r-054.png','写真：長期的な価値創造':'r-052.png',
'写真：積出港・銅カソード':'r-072.png','写真：鉱山':'c_94ce967e-016.png','写真：製錬':'c_a5a586a7-010.png','写真：最終製品':'r-022.png',
'写真：夜空と鉱山車両':'r-075.png',
'写真：鉄鉱石':('x_ironore.jpg','contain'),'写真：ニッケル':('r-073.png','contain'),'写真：リチウム':('x_lithium.jpg','contain'),'写真：アルミ':('x_alu.jpg','contain'),'写真：ボーキサイト':('r-055.png','contain'),'写真：二次資源':'r-074.png',
'写真：現場で働く人々':'r-082.png','写真：植生調査・環境':'r-084.png','写真：都市・人口':'x_ch076.jpg','写真：鉱山開発':'x_ch078.jpg','写真：港湾・物流':'x_ch080.jpg'}
_cache={}
def _uri(f):
    if f not in _cache:
        im=_I.open('img/'+f).convert('RGB'); im.thumbnail((1400,1400)); bf=_io.BytesIO(); im.save(bf,'JPEG',quality=86)
        _cache[f]='data:image/jpeg;base64,'+base64.b64encode(bf.getvalue()).decode()
    return _cache[f]
def ph(x,y,w,h,label):
    v=IMG.get(label)
    if v:
        f,fit=(v if isinstance(v,tuple) else (v,'cover'))
        return f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:#fff;overflow:hidden"><img src="{_uri(f)}" style="width:100%;height:100%;object-fit:{fit};display:block"></div>'
    return f'<div class="a ph" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><span>{label}</span></div>'
def bars(x,y,w,n,last=.55):
    s=''.join(f'<div class="bar" style="width:{(last if i==n-1 else 1)*100:.0f}%"></div>' for i in range(n))
    return A(x,y,s,w)
def rule(x,y,w): return f'<div class="rule" style="left:{x}px;top:{y}px;width:{w}px"></div>'
def vrule(x,y,h): return f'<div class="vrule" style="left:{x}px;top:{y}px;height:{h}px"></div>'
def lab(x,y,t): return A(x,y,f'<b></b>{t}',cls='lab')
def h2(x,y,t,w=None): return A(x,y,t,w,'h2')
def note(x,y,t,w=None): return A(x,y,'※'+t,w,'note')
def folio(n,left):
    t=f'{n:02d}'
    if left: return A(48,806,f'{t}&nbsp;&nbsp;&nbsp;&nbsp;MITSUBISHI CORPORATION&nbsp;&nbsp;·&nbsp;&nbsp;MINERAL RESOURCES GROUP',cls='fol')
    return A(1190-48-20,806,t,cls='fol')
def svg(x,y,w,h,inner): return f'<svg class="a" style="left:{x}px;top:{y}px;overflow:visible" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{inner}</svg>'
def hairbar(x,y,w,h,shade=90,step=1.5,sw=.4):
    c=f'rgb({shade},{shade+3},{shade+7})'
    d=''.join(f'M{x+i*step:.1f},{y}v{h}' for i in range(int(w/step)+1))
    return f'<path d="{d}" stroke="{c}" stroke-width="{sw}"/>'
def spread(body,l,r): return f'<div class="sp">{body}{folio(l,True)}{folio(r,False)}</div>'
