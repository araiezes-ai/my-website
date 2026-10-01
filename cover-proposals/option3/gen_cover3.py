import base64, io, math, random
from PIL import Image, ImageEnhance
N='f/ns/package/files/'; D='mc/dl/'
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
def enc(im,q=90):
    bf=io.BytesIO(); im.convert('RGB').save(bf,'JPEG',quality=q); return 'data:image/jpeg;base64,'+base64.b64encode(bf.getvalue()).decode()
def mark(x,y,s=6.6):
    o=''
    for th in (-90,30,150):
        p=lambda a,d:(x+d*math.cos(math.radians(a)),y+d*math.sin(math.radians(a)))
        q=[(x,y),p(th-30,s),p(th,s*math.sqrt(3)),p(th+30,s)]
        o+='<path d="M'+' L'.join(f'{a:.2f},{b:.2f}' for a,b in q)+'Z" fill="#E60012"/>'
    return o
FONT=f"""@font-face{{font-family:NS;font-weight:300;src:url(data:font/woff2;base64,{b64(N+'noto-sans-latin-300-normal.woff2')})}}"""
def page(inner,name,title_y=652,title_color='#24272b',logo_dark=True):
    html=f'''<!doctype html><meta charset=utf-8><style>{FONT}@page{{size:210mm 297mm;margin:0}}body{{margin:0}}
.pg{{position:relative;width:595px;height:842px;overflow:hidden;background:#fff;zoom:1.3333;font-family:NS}}</style><div class="pg">{inner}
<div style="position:absolute;left:48px;top:{title_y}px;font-weight:300;font-size:17px;line-height:1.42;color:{title_color};letter-spacing:.3px">Mitsubishi Corporation<br>Mineral Resources Group<br>Corporate Profile</div>
<div style="position:absolute;left:48px;top:{title_y+82}px;width:30px;height:1px;background:#C8102E"></div>
<svg style="position:absolute;left:0;top:0" width="595" height="842">{mark(232,792)}<text x="250" y="796" font-family="Liberation Serif" font-size="12.5" fill="{'#1a1a1a' if logo_dark else '#fff'}">Mitsubishi Corporation</text></svg></div>'''
    open(name+'.html','w').write(html)

# --- A: sliced jetty (staggered vertical strips) ---
im=Image.open(D+'mr_01_01@2x.webp').convert('RGB').crop((1000,0,2300,1922))
im=ImageEnhance.Contrast(im).enhance(1.05)
sc=595/1300; im=im.resize((595,int(1922*sc))); im=im.crop((0,250,595,850))
n=7; sw=595/n; offs=[38,10,62,24,0,48,18]; inner=''
for i in range(n):
    x=int(i*sw); w=int((i+1)*sw)-x
    strip=im.crop((x,0,x+w,600))
    inner+=f'<img src="{enc(strip)}" style="position:absolute;left:{x}px;top:{offs[i]}px;width:{w-1}px;height:600px;display:block">'
inner+='<div style="position:absolute;left:340px;top:604px;width:28px;height:28px;background:#C8102E"></div>'
page(inner,'c3a',title_y=668)

# --- B: diptych colour field: sea + pit terraces, red square at the joint ---
sea=Image.open(D+'mr_01_01@2x.webp').convert('RGB'); pit=Image.open(D+'_mr_project_04.png').convert('RGB')
s1=sea.crop((1480,200,2560,1922)).resize((380,606)).crop((0,0,380,600))
s2=pit.crop((180,120,980,884)); s2=pit.crop((300,100,700,884)); s2=ImageEnhance.Color(s2).enhance(.35).resize((212,415)).crop((0,0,212,401))
inner=f'<img src="{enc(s1)}" style="position:absolute;left:0;top:0;width:380px;height:600px">'
inner+=f'<img src="{enc(s2)}" style="position:absolute;left:383px;top:0;width:212px;height:401px;object-fit:cover">'
cu=Image.open(D+'mr_03_01@2x.webp').convert('RGB').crop((380,0,900,540))
inner+=f'<img src="{enc(cu)}" style="position:absolute;left:383px;top:404px;width:212px;height:196px;object-fit:cover">'
inner+='<div style="position:absolute;left:352px;top:572px;width:56px;height:56px;background:#C8102E"></div>'
page(inner,'c3b',title_y=652)
