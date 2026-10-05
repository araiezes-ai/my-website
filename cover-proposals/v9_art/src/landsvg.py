import json
from shapely.geometry import shape, box
from shapely import affinity
g=shape(json.load(open('land.geojson'))['features'][0]['geometry'] if 'features' in json.load(open('land.geojson')) else json.load(open('land.geojson'))['geometry'])
g=g.simplify(0.35).buffer(0)
L0,L1,B0,B1=-25,335,-56,76
a=g.intersection(box(-25,B0,180,B1)); b=affinity.translate(g.intersection(box(-180,B0,-25,B1)),360,0)
def path(geom,w,h):
    sx=w/(L1-L0); sy=h/(B1-B0); d=[]
    geoms=getattr(geom,'geoms',[geom])
    for p in geoms:
        if p.geom_type!='Polygon' or p.area<0.3: continue
        d.append('M'+'L'.join(f'{(x-L0)*sx:.1f},{(B1-y)*sy:.1f}' for x,y in p.exterior.coords)+'Z')
    return ''.join(d)
def land(w,h): return path(a,w,h)+path(b,w,h)
def proj(lon,lat,w,h):
    if lon<L0: lon+=360
    return (lon-L0)*w/(L1-L0),(B1-lat)*h/(B1-B0)
def region(l0,l1,b0,b1,w,h):
    gg=g.intersection(box(l0,b0,l1,b1)); sx=w/(l1-l0); sy=h/(b1-b0); d=[]
    for p in getattr(gg,'geoms',[gg]):
        if p.geom_type!='Polygon' or p.area<0.05: continue
        d.append('M'+'L'.join(f'{(x-l0)*sx:.1f},{(b1-y)*sy:.1f}' for x,y in p.exterior.coords)+'Z')
    return ''.join(d)
