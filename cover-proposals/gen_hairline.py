import math, base64, json, numpy as np
from global_land_mask import globe
from shapely.geometry import shape, Point
from shapely.prepared import prep
W,H=595,842
F='f/fontsource-shippori-mincho-5.3.0/package/files/'; G='f/fontsource-cormorant-garamond-5.3.0/package/files/'
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
css=f"""@font-face{{font-family:SM;src:url(data:font/woff2;base64,{b64(F+'shippori-mincho-japanese-400-normal.woff2')})}}
@font-face{{font-family:SM5;src:url(data:font/woff2;base64,{b64(F+'shippori-mincho-japanese-500-normal.woff2')})}}
@font-face{{font-family:CG;src:url(data:font/woff2;base64,{b64(G+'cormorant-garamond-latin-500-normal.woff2')})}}"""
J=prep(shape(json.load(open('japan.geojson'))['geometry']).buffer(0.3))
# Pacific-centred equirectangular map drawn with steel "hairline" strokes
LONC=170; SPAN=300; X0,X1=-20,W+20; Y0,Y1=292,575
LAT_TOP,LAT_BOT=74,-56
dy=1.75
lons=np.linspace(LONC-SPAN/2,LONC+SPAN/2,2200)
xs=X0+(lons-(LONC-SPAN/2))/SPAN*(X1-X0)
gray=[];red=[]
y=Y0
while y<=Y1:
    lat=LAT_TOP-(y-Y0)/(Y1-Y0)*(LAT_TOP-LAT_BOT)
    lw=((lons+180)%360)-180
    land=globe.is_land(np.full_like(lw,lat),lw)
    jp=land&(lw>128.6)&(lw<146.5)&(lat>30.5)&(lat<45.6)&~((lw<130.6)&(lat>34.2))&~((lw<139.7)&(lat>41.6))
    for mask,out in ((land&~jp,gray),(jp,red)):
        i=0;n=len(mask)
        while i<n:
            if mask[i]:
                j=i
                while j+1<n and mask[j+1]: j+=1
                if xs[j]-xs[i]>0.6: out.append(f'M{xs[i]:.1f},{y:.1f}H{xs[j]:.1f}')
                i=j+1
            else: i+=1
    y+=dy
def mark(x,y,s):
    o=''
    for th in (-90,30,150):
        p=lambda ang,d:(x+d*math.cos(math.radians(ang)),y+d*math.sin(math.radians(ang)))
        pts=[(x,y),p(th-30,s),p(th,s*math.sqrt(3)),p(th+30,s)]
        o+='<path d="M'+' L'.join(f'{a:.2f},{b:.2f}' for a,b in pts)+'Z" fill="#E60012"/>'
    return o
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs><linearGradient id="st" gradientUnits="userSpaceOnUse" x1="0" y1="292" x2="595" y2="575">
<stop offset="0" stop-color="#e3e5e7"/><stop offset=".3" stop-color="#8d9298"/><stop offset=".47" stop-color="#e6e8ea"/><stop offset=".64" stop-color="#7f848a"/><stop offset=".85" stop-color="#cfd2d5"/><stop offset="1" stop-color="#a3a7ac"/></linearGradient>
<linearGradient id="fd" x1="0" x2="1"><stop offset="0" stop-color="#000"/><stop offset=".14" stop-color="#fff"/><stop offset=".86" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient><mask id="m"><rect x="0" y="280" width="{W}" height="310" fill="url(#fd)"/></mask></defs>
<rect width="{W}" height="{H}" fill="#fff"/>
<text x="48" y="66" font-family="CG" font-size="9" letter-spacing="2.4" fill="#6b6b6b">MITSUBISHI CORPORATION  ·  MINERAL RESOURCES GROUP</text>
<text x="536" y="104" font-family="SM" font-size="14" fill="#2a2a2a" letter-spacing="6" style="writing-mode:vertical-rl">鉄で、世界をつなぐ。</text>
<g mask="url(#m)"><path d="{''.join(gray)}" stroke="url(#st)" stroke-width=".6" fill="none"/></g>
<path d="{''.join(red)}" stroke="#C8102E" stroke-width="1.5" fill="none"/>
<line x1="48" y1="604" x2="48" y2="690" stroke="#C8102E" stroke-width="1.6"/>
<text x="62" y="632" font-family="SM5" font-size="27" fill="#1c1c1c" letter-spacing="7">鉄鋼事業</text>
<text x="63" y="656" font-family="CG" font-size="11.5" letter-spacing="3.4" fill="#4a4a4a">STEEL BUSINESS</text>
<text x="63" y="682" font-family="SM" font-size="9.5" fill="#6d6d6d" letter-spacing="1">原料から鋼材まで、世界の鉄鋼サプライチェーンを担う。</text>
{mark(232,786,7.2)}
<text x="250" y="790" font-family="Liberation Serif" font-size="12.5" fill="#1a1a1a">Mitsubishi Corporation</text>
</svg>'''
open('wa2.html','w').write(f'<!doctype html><meta charset=utf-8><style>{css}@page{{size:A4;margin:0}}body{{margin:0}}svg{{width:210mm;height:297mm;display:block}}</style>{svg}')
