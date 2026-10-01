import math, base64, numpy as np
from global_land_mask import globe
W,H=595,842
F='f/fontsource-shippori-mincho-5.3.0/package/files/'; G='f/fontsource-cormorant-garamond-5.3.0/package/files/'
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
css=f"""@font-face{{font-family:SM;src:url(data:font/woff2;base64,{b64(F+'shippori-mincho-japanese-400-normal.woff2')})}}
@font-face{{font-family:CG;font-weight:500;src:url(data:font/woff2;base64,{b64(G+'cormorant-garamond-latin-500-normal.woff2')})}}
@font-face{{font-family:CG;font-weight:400;src:url(data:font/woff2;base64,{b64(G+'cormorant-garamond-latin-400-normal.woff2')})}}
@font-face{{font-family:CG;font-weight:300;src:url(data:font/woff2;base64,{b64(G+'cormorant-garamond-latin-300-normal.woff2')})}}"""
# Pacific-centred equirectangular, full 360, steel hairlines
LONC=160; X0,X1=-8,W+8; Y0=318; LAT_TOP,LAT_BOT=76,-56
SC=(X1-X0)/360; Y1=Y0+(LAT_TOP-LAT_BOT)*SC
def px(lon,lat):
    l=(lon-(LONC-180))%360
    return X0+l*SC, Y0+(LAT_TOP-lat)*SC
lons=np.linspace(LONC-180,LONC+180,2400); xs=X0+(lons-(LONC-180))*SC
gray=[];red=[];y=Y0;dy=1.6
while y<=Y1:
    lat=LAT_TOP-(y-Y0)/SC
    lw=((lons+180)%360)-180
    land=globe.is_land(np.full_like(lw,lat),lw)
    jp=land&(lw>128.6)&(lw<146.5)&(lat>30.5)&(lat<45.6)&~((lw<130.6)&(lat>34.2))&~((lw<139.7)&(lat>41.6))
    for mask,out in ((land&~jp,gray),(jp,red)):
        i=0;n=len(mask)
        while i<n:
            if mask[i]:
                j=i
                while j+1<n and mask[j+1]: j+=1
                if xs[j]-xs[i]>0.4: out.append(f'M{xs[i]:.1f},{y:.1f}H{xs[j]:.1f}')
                i=j+1
            else: i+=1
    y+=dy
# Locations taken from rough p.06-09 (illustrative)
TOKYO=(139.7,35.7)
sites=[(148.5,-22.5),(-69.1,-24.3),(-77.1,-9.5),(-70.6,-33.4),(-66.9,52.9),(103.8,1.3),(-0.1,51.5),(72.9,19.1),(55.3,25.2),(121.5,31.2),(100.5,13.7),(106.8,-6.2)]
tx,ty=px(*TOKYO); arcs=''; pts=''
for lon,lat in sites:
    x,y=px(lon,lat)
    # shortest horizontal path on this pacific-centred map is the straight one; lift as a gentle curve
    mx,my=(tx+x)/2,(ty+y)/2-abs(x-tx)*0.18-12
    arcs+=f'<path d="M{tx:.1f},{ty:.1f}Q{mx:.1f},{my:.1f} {x:.1f},{y:.1f}"/>'
    pts+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.7"/>'
def mark(x,y,s):
    o=''
    for th in (-90,30,150):
        p=lambda ang,d:(x+d*math.cos(math.radians(ang)),y+d*math.sin(math.radians(ang)))
        q=[(x,y),p(th-30,s),p(th,s*math.sqrt(3)),p(th+30,s)]
        o+='<path d="M'+' L'.join(f'{a:.2f},{b:.2f}' for a,b in q)+'Z" fill="#E60012"/>'
    return o
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs><linearGradient id="st" gradientUnits="userSpaceOnUse" x1="0" y1="{Y0}" x2="595" y2="{Y1}">
<stop offset="0" stop-color="#d7dadd"/><stop offset=".3" stop-color="#8b9096"/><stop offset=".47" stop-color="#e2e4e6"/><stop offset=".64" stop-color="#7c8187"/><stop offset=".85" stop-color="#c9ccd0"/><stop offset="1" stop-color="#9fa3a8"/></linearGradient>
<linearGradient id="fd" x1="0" x2="1"><stop offset="0" stop-color="#000"/><stop offset=".05" stop-color="#fff"/><stop offset=".95" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>
<mask id="m"><rect x="0" y="{Y0-10}" width="{W}" height="{Y1-Y0+20}" fill="url(#fd)"/></mask></defs>
<rect width="{W}" height="{H}" fill="#fff"/>
<text x="48" y="66" font-family="CG" font-weight="500" font-size="9" letter-spacing="2.6" fill="#555">MITSUBISHI CORPORATION</text>
<text x="48" y="80" font-family="CG" font-weight="500" font-size="9" letter-spacing="2.6" fill="#555">MINERAL RESOURCES GROUP</text>
<text x="545" y="58" font-family="SM" font-size="8.5" letter-spacing="3" fill="#777" style="writing-mode:vertical-rl">三菱商事　金属資源グループ</text>
<text x="46" y="182" font-family="CG" font-weight="300" font-size="40" fill="#1e1e1e" letter-spacing=".3">Strength to Hold.</text>
<text x="46" y="228" font-family="CG" font-weight="300" font-size="40" fill="#1e1e1e" letter-spacing=".3">Power to Connect.</text>
<line x1="48" y1="256" x2="76" y2="256" stroke="#C8102E" stroke-width="1"/>
<g mask="url(#m)"><path d="{''.join(gray)}" stroke="url(#st)" stroke-width=".55" fill="none"/></g>
<path d="{''.join(red)}" stroke="#C8102E" stroke-width="1.3" fill="none"/>
<g fill="none" stroke="#3a3d40" stroke-width=".35" stroke-opacity=".75">{arcs}</g>
<g fill="#3a3d40">{pts}</g>
<circle cx="{tx:.1f}" cy="{ty:.1f}" r="2.6" fill="#C8102E"/><circle cx="{tx:.1f}" cy="{ty:.1f}" r="5.5" fill="none" stroke="#C8102E" stroke-width=".5"/>
<text x="48" y="656" font-family="CG" font-weight="500" font-size="15" letter-spacing="1.2" fill="#2a2a2a">Group Profile</text>
<text x="48" y="678" font-family="CG" font-weight="500" font-size="8.5" letter-spacing="2.2" fill="#6a6a6a">METALLURGICAL COAL · COPPER · IRON ORE · TRADING · FUTURE MATERIALS</text>
{mark(232,786,7.2)}
<text x="250" y="790" font-family="Liberation Serif" font-size="12.5" fill="#1a1a1a">Mitsubishi Corporation</text>
</svg>'''
open('wa3.html','w').write(f'<!doctype html><meta charset=utf-8><style>{css}@page{{size:A4;margin:0}}body{{margin:0}}svg{{width:210mm;height:297mm;display:block}}</style>{svg}')
