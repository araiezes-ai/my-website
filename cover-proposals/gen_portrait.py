import math, base64, random, numpy as np
from global_land_mask import globe
random.seed(11)
W,H=595,842
F='f/fontsource-shippori-mincho-5.3.0/package/files/'; N='f/ns/package/files/'
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
css=f"""@font-face{{font-family:NS;font-weight:300;src:url(data:font/woff2;base64,{b64(N+'noto-sans-latin-300-normal.woff2')})}}
@font-face{{font-family:NS;font-weight:400;src:url(data:font/woff2;base64,{b64(N+'noto-sans-latin-400-normal.woff2')})}}
@font-face{{font-family:NS;font-weight:500;src:url(data:font/woff2;base64,{b64(N+'noto-sans-latin-500-normal.woff2')})}}"""
# Pacific-centred equirectangular world, land drawn with VERTICAL steel hairlines
LONC=155; SC=W/360; LAT_TOP,LAT_BOT=76,-56; Y0=548
def px(lon,lat): return ((lon-(LONC-180))%360)*SC, Y0+(LAT_TOP-lat)*SC
Y1=Y0+(LAT_TOP-LAT_BOT)*SC
lats=np.linspace(LAT_TOP,LAT_BOT,900); ys=Y0+(LAT_TOP-lats)*SC
gray=[];red=[];x=0.6
while x<W:
    lon=((x/SC+(LONC-180))+180)%360-180
    land=globe.is_land(lats,np.full_like(lats,lon))
    jp=land&(128.6<lon<146.5)&(lats>30.5)&(lats<45.6)&~((lon<130.6)&(lats>34.2))&~((lon<139.7)&(lats>41.6))
    for mask,out in ((land&~jp,gray),(jp,red)):
        i=0;n=len(mask)
        while i<n:
            if mask[i]:
                j=i
                while j+1<n and mask[j+1]: j+=1
                if ys[j]-ys[i]>0.3: out.append(f'M{x:.1f},{ys[i]:.1f}V{ys[j]:.1f}')
                i=j+1
            else: i+=1
    x+=1.55
# Sites as shown on rough P.09 (business map)
SITES=[('Triland Metals / RtM Europe',-0.1,51.5),('Arctial',13.2,65.8),('RtM Bharat',77.2,28.6),('RtM International',103.8,1.3),
('Goongarrie Hub',121.4,-30.0),('Aurukun',141.7,-13.3),('BMA',148.3,-22.3),('MDP',153.0,-27.5),
('Turnagain',-128.9,58.5),('PAK Lithium',-94.0,51.6),('Elemental USA',-96.0,33.0),('RtM Americas',-77.0,40.4),('IOC',-66.9,52.9),
('Antamina',-77.05,-9.53),('MCIP',-77.0,-12.0),('Quellaveco',-70.6,-17.1),('Marimaca',-70.3,-22.9),('Escondida',-69.07,-24.27),
('CAP / CMP',-70.9,-28.6),('Los Pelambres',-70.5,-31.7),('MCI',-70.65,-33.45),('Anglo American Sur',-70.3,-33.15)]
risers='';tops=''
used=[]
for name,lon,lat in SITES:
    x,y=px(lon,lat)
    while any(abs(x-u)<1.6 for u in used): x+=1.7
    used.append(x)
    top=random.uniform(250,430)
    risers+=f'<path d="M{x:.1f},{y:.1f}V{top:.1f}"/>'
    tops+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.3"/>'
tx,ty=px(139.7,35.7)
def mark(x,y,s):
    o=''
    for th in (-90,30,150):
        p=lambda ang,d:(x+d*math.cos(math.radians(ang)),y+d*math.sin(math.radians(ang)))
        q=[(x,y),p(th-30,s),p(th,s*math.sqrt(3)),p(th+30,s)]
        o+='<path d="M'+' L'.join(f'{a:.2f},{b:.2f}' for a,b in q)+'Z" fill="#E60012"/>'
    return o
BIZ=['Metallurgical Coal','Copper','Iron Ore','Nickel','Lithium','Aluminium &amp; Bauxite','Recycled Resources','Trading']
biz=''.join(f'<text x="48" y="{222+i*14.5}">{b}</text>' for i,b in enumerate(BIZ))
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs><linearGradient id="st" gradientUnits="userSpaceOnUse" x1="0" y1="{Y0}" x2="{W}" y2="{Y1}">
<stop offset="0" stop-color="#c9ccd0"/><stop offset=".3" stop-color="#868b91"/><stop offset=".5" stop-color="#d8dbde"/><stop offset=".7" stop-color="#7d8288"/><stop offset="1" stop-color="#b9bdc1"/></linearGradient>
<linearGradient id="rs" gradientUnits="userSpaceOnUse" x1="0" y1="{Y1}" x2="0" y2="250"><stop offset="0" stop-color="#4f545a"/><stop offset=".45" stop-color="#5d6268" stop-opacity=".7"/><stop offset="1" stop-color="#5d6268" stop-opacity="0"/></linearGradient><linearGradient id="rr" gradientUnits="userSpaceOnUse" x1="0" y1="{Y1}" x2="0" y2="200"><stop offset="0" stop-color="#C8102E"/><stop offset=".5" stop-color="#C8102E" stop-opacity=".8"/><stop offset="1" stop-color="#C8102E" stop-opacity="0"/></linearGradient></defs>
<rect width="{W}" height="{H}" fill="#fff"/>
<g font-family="NS" font-weight="300" font-size="17.5" fill="#3d4044"><text x="46" y="118">Mitsubishi Corporation</text><text x="46" y="142">Mineral Resources Group</text><text x="46" y="166">Brochure</text></g>
<line x1="48" y1="196" x2="70" y2="196" stroke="#C8102E" stroke-width="1"/>
<g font-family="NS" font-weight="400" font-size="7.6" letter-spacing="1.6" fill="#6c7075" style="text-transform:uppercase">{biz}</g>
<path d="{''.join(gray)}" stroke="url(#st)" stroke-width=".6" fill="none"/>
<path d="{''.join(red)}" stroke="#C8102E" stroke-width="1.1" fill="none"/>
<g stroke="url(#rs)" stroke-width=".45" fill="none">{risers}</g>
<g fill="#4a4e53">{tops}</g>
<path d="M{tx:.1f},{ty:.1f}V200" stroke="url(#rr)" stroke-width=".7"/><circle cx="{tx:.1f}" cy="{ty:.1f}" r="2" fill="#C8102E"/>
{mark(232,800,7.2)}
<text x="250" y="804" font-family="Liberation Serif" font-size="12.5" fill="#1a1a1a">Mitsubishi Corporation</text>
</svg>'''
open('wa4.html','w').write(f'<!doctype html><meta charset=utf-8><style>{css}@page{{size:A4;margin:0}}body{{margin:0}}svg{{width:210mm;height:297mm;display:block}}</style>{svg}')
