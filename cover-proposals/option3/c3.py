import base64, io
from PIL import Image, ImageEnhance
N='f/ns/package/files/'
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
def uri(f,sat=.85,con=1.06,crop=None):
    im=Image.open('img/'+f).convert('RGB')
    if crop: w,h=im.size; im=im.crop((int(crop[0]*w),int(crop[1]*h),int(crop[2]*w),int(crop[3]*h)))
    im=ImageEnhance.Color(im).enhance(sat); im=ImageEnhance.Contrast(im).enhance(con)
    bf=io.BytesIO(); im.save(bf,'JPEG',quality=90); return 'data:image/jpeg;base64,'+base64.b64encode(bf.getvalue()).decode()
W,H=595,842; G=3
cells=[ # x,y,w,h,image,crop,sat
(0,0,372,392,'r-046.png',(.05,.05,.75,.95),.8),
(372+G,0,W-372-G,196,'r-054.png',(.2,.25,.8,.75),.95),
(372+G,196+G,W-372-G,196-G,'r-048.png',(.1,.1,.9,.9),.6),
(0,392+G,236,208,'r-075.png',(.35,.2,.75,.95),.9),
(236+G,392+G,W-236-G,208,'r-053.png',(.0,.1,1,.9),.8),
]
body=''
for x,y,w,h,f,cr,sat in cells:
    body+=f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:url({uri(f,sat,1.08,cr)}) center/cover"></div>'
# modern-art accent: one small solid red square inside the grid
body+=f'<div style="position:absolute;left:{372+G}px;top:{392+G-0}px;width:0;height:0"></div>'
body+='<div style="position:absolute;left:212px;top:368px;width:48px;height:48px;background:#C8102E"></div>'
mark=''
import math
for th in (-90,30,150):
    p=lambda a,d:(7.2*0+232+d*math.cos(math.radians(a)),792+d*math.sin(math.radians(a)))
    s=6.6; q=[(232,792),p(th-30,s),p(th,s*math.sqrt(3)),p(th+30,s)]
    mark+='<path d="M'+' L'.join(f'{a:.2f},{b:.2f}' for a,b in q)+'Z" fill="#E60012"/>'
html=f'''<!doctype html><meta charset=utf-8><style>
@font-face{{font-family:NS;font-weight:300;src:url(data:font/woff2;base64,{b64(N+'noto-sans-latin-300-normal.woff2')})}}
@font-face{{font-family:NS;font-weight:400;src:url(data:font/woff2;base64,{b64(N+'noto-sans-latin-400-normal.woff2')})}}
@page{{size:210mm 297mm;margin:0}}body{{margin:0}}
.pg{{position:relative;width:595px;height:842px;overflow:hidden;background:#fff;zoom:1.3333;font-family:NS}}
</style><div class="pg">{body}
<div style="position:absolute;left:48px;top:640px;font-weight:300;font-size:17px;line-height:1.42;color:#24272b;letter-spacing:.3px">Mitsubishi Corporation<br>Mineral Resources Group<br>Corporate Profile</div>
<div style="position:absolute;left:48px;top:722px;width:30px;height:1px;background:#C8102E"></div>
<svg style="position:absolute;left:0;top:0" width="595" height="842">{mark}<text x="250" y="796" font-family="Liberation Serif" font-size="12.5" fill="#1a1a1a">Mitsubishi Corporation</text></svg>
</div>'''
open('c3.html','w').write(html)
