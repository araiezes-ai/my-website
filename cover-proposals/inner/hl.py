import math, random, json, numpy as np, shapely
from global_land_mask import globe
from shapely.geometry import shape
JP=shape(json.load(open('japan.geojson'))['geometry'])
def hairmap(w, lon0, lon1, lat0, lat1, step=1.1, sw=.45, sites=(), japan=True, seed=3, dark=70, light=0xd2, site_r=1.6):
    """Equirectangular land drawn with vertical steel hairlines. lon range may cross 180 (lon1>180)."""
    rnd=random.Random(seed)
    sc=w/(lon1-lon0); h=(lat1-lat0)*sc
    lats=np.linspace(lat1,lat0,int(h*2.5)); ys=(lat1-lats)*sc
    def px(lon,lat):
        l=lon
        while l<lon0: l+=360
        return (l-lon0)*sc,(lat1-lat)*sc
    groups={}
    x=0.4
    while x<w:
        lon=((lon0+x/sc)+180)%360-180
        m=globe.is_land(lats,np.full_like(lats,lon))
        t=x/w; s=0.5+0.28*math.cos(2*math.pi*(t*1.6-0.12))+0.16*math.cos(2*math.pi*(t*4.3+0.3))
        k=round(min(1,max(0,s+rnd.uniform(-.07,.07)))*16)
        segs=groups.setdefault(k,[])
        i=0;n=len(m)
        while i<n:
            if m[i]:
                j=i
                while j+1<n and m[j+1]: j+=1
                if ys[j]-ys[i]>0.3: segs.append(f'M{x:.1f},{ys[i]:.1f}V{ys[j]:.1f}')
                i=j+1
            else: i+=1
        x+=step
    def tone(k): c=int(dark+(light-dark)*k/16); return f'rgb({c},{c+3},{c+7})'
    out=''.join(f'<path d="{"".join(v)}" stroke="{tone(k)}"/>' for k,v in groups.items() if v)
    svg=f'<g stroke-width="{sw}" fill="none">{out}</g>'
    if japan:
        gs=JP.geoms if JP.geom_type=='MultiPolygon' else [JP]
        d=''.join('M'+'L'.join(f'{px(a,b)[0]:.2f},{px(a,b)[1]:.2f}' for a,b in g.exterior.coords)+'Z' for g in gs)
        svg+=f'<path d="{d}" fill="#C8102E"/>'
    for s in sites:
        lon,lat=s[0],s[1]; col=s[2] if len(s)>2 else '#3b3f44'
        x,y=px(lon,lat); svg+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{site_r}" fill="{col}"/>'
    return svg,w,h,px
