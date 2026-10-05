"""Glass globe renderer: faceted champagne-gold / graphite continents inside a translucent glass sphere.
render(N, lon0, lat0, roll) -> RGBA PIL image (N x N), plus orbit(...) -> SVG paths in the same pixel space."""
import numpy as np, math
from PIL import Image, ImageFilter
from global_land_mask import globe
from scipy.spatial import cKDTree

def _v(lat, lon):
    la, lo = np.radians(lat), np.radians(lon)
    return np.stack([np.cos(la)*np.cos(lo), np.cos(la)*np.sin(lo), np.sin(la)], -1)

def _basis(lon0, lat0, roll=0):
    c = _v(lat0, lon0)
    e = np.array([-math.sin(math.radians(lon0)), math.cos(math.radians(lon0)), 0.])
    n = np.cross(c, e)
    r = math.radians(roll)
    e, n = e*math.cos(r) + n*math.sin(r), -e*math.sin(r) + n*math.cos(r)
    return c, e, n

# facet seeds (fibonacci sphere) – crystal / mineral texture
M = 42000
i = np.arange(M) + .5
phi = np.arccos(1 - 2*i/M); th = math.pi*(1+5**.5)*i
SEEDS = np.stack([np.cos(th)*np.sin(phi), np.sin(th)*np.sin(phi), np.cos(phi)], -1)
rng = np.random.default_rng(7)
SEEDS += rng.normal(0, .006, SEEDS.shape); SEEDS /= np.linalg.norm(SEEDS, axis=1)[:, None]
TREE = cKDTree(SEEDS)
CELL_R = rng.random(M); CELL_S = rng.random(M)
CELL_N = rng.normal(0, .30, (M, 3))
SPACING = math.sqrt(4*math.pi/M)
TREE_F = cKDTree(SEEDS[::3])

# resource hot spots (lat, lon, weight, sigma deg)  – South America, Australia first; then N. America, Africa, Europe
HOT = [(-23, -69, 1.0, 9), (-14, -73, .9, 8), (-7, -50, .55, 9), (-30, -70, .7, 7),
       (-22, 148, 1.0, 8), (-23, 119, .85, 9), (-31, 122, .5, 9),
       (33, -111, .65, 8), (52, -120, .55, 10), (47, -90, .3, 10),
       (-26, 28, .7, 8), (-12, 27, .55, 7), (12, -10, .25, 10),
       (51, 0, .45, 8), (50, 10, .35, 8), (60, 15, .25, 8)]
COLD = [(35, 105, 1.0, 22), (60, 95, 1.0, 30)]   # China / Russia kept quiet (graphite)
JAPAN = (35.7, 139.7)

def _gold(P):
    w = np.zeros(P.shape[:-1])
    for la, lo, k, s in HOT:
        d = np.degrees(np.arccos(np.clip(P @ _v(la, lo), -1, 1)))
        w += k*np.exp(-(d/s)**2)
    for la, lo, k, s in COLD:
        d = np.degrees(np.arccos(np.clip(P @ _v(la, lo), -1, 1)))
        w -= .6*k*np.exp(-(d/s)**2)
    return np.clip(w, 0, 1)

def _latlon(P):
    return np.degrees(np.arcsin(np.clip(P[..., 2], -1, 1))), np.degrees(np.arctan2(P[..., 1], P[..., 0]))

def _land(P):
    la, lo = _latlon(P)
    return globe.is_land(la, lo)

def mix(a, b, t):
    t = t[..., None] if np.ndim(t) else t
    return np.asarray(a)*(1-t) + np.asarray(b)*t

GOLD_D = np.array([140, 104, 50.]); GOLD_L = np.array([244, 220, 166.])
GRAPH_D = np.array([46, 52, 60.]); GRAPH_L = np.array([186, 192, 200.])
LIGHT = np.array([-.55, .62, .56]); LIGHT /= np.linalg.norm(LIGHT)

def render(N, lon0, lat0, roll=0, back=True, back_a=.20, glow=1.0, ss=2, japan=True, ocean=(226, 236, 245), deep=(92, 126, 166)):
    S = N*ss
    c, e, n = _basis(lon0, lat0, roll)
    y, x = np.mgrid[0:S, 0:S]
    u = (x+.5)/S*2-1; v = 1-(y+.5)/S*2
    r2 = u*u+v*v; inside = r2 < 1
    z = np.sqrt(np.clip(1-r2, 0, 1))
    uu, vv, zz = u[inside], v[inside], z[inside]
    Pf = uu[:, None]*e + vv[:, None]*n + zz[:, None]*c
    Pb = uu[:, None]*e + vv[:, None]*n - zz[:, None]*c
    Nv = np.stack([uu, vv, zz], -1)                       # normal in view space
    # --- ocean / glass
    fres = (1-zz)**1.4
    sph = np.clip(Nv @ LIGHT, 0, 1)
    col = mix(ocean, deep, np.clip(fres*1.25 + (1-sph)*.35, 0, 1))
    # far side continents seen through the glass
    if back:
        lb = _land(Pb)
        db, ib = TREE.query(Pb, k=1)
        gb = _gold(Pb)
        tb = mix(np.array([150, 166, 184.]), np.array([196, 178, 140.]), gb*.8)
        a = back_a*lb*(1-.6*fres)
        col = col*(1-a[:, None]) + tb*a[:, None]
    # --- front land
    lf = _land(Pf)
    d, idx = TREE.query(Pf, k=2)
    edge = np.clip(1-(d[:, 1]-d[:, 0])/(SPACING*.09), 0, 1)
    g = _gold(Pf)
    nrm = Nv + CELL_N[idx[:, 0]]*.9
    nrm /= np.linalg.norm(nrm, axis=1)[:, None]
    diff = np.clip(nrm @ LIGHT, 0, 1)
    shade = .18 + .86*diff + (CELL_R[idx[:, 0]]-.5)*.16
    base_g = mix(GRAPH_D, GRAPH_L, np.clip(shade, 0, 1))
    base_o = mix(GOLD_D, GOLD_L, np.clip(shade, 0, 1))
    tl = mix(base_g, base_o, np.clip(g*1.15, 0, 1))
    # sparkles: warm points of light in resource regions
    sp = (CELL_S[idx[:, 0]] > .86)*g*glow
    tl = tl + sp[:, None]*np.array([90, 70, 30.])
    tl = tl*(1-.18*edge[:, None]) + edge[:, None]*.18*np.array([250, 240, 220.])
    # limb darkening on land
    tl = tl*(.78+.22*zz[:, None])
    col = np.where(lf[:, None], tl, col)
    # --- specular + soft sheen + rim
    H = LIGHT + np.array([0, 0, 1.]); H /= np.linalg.norm(H)
    nh = np.clip(Nv @ H, 0, 1)
    spec = nh**140*1.0 + nh**18*.22 + nh**4*.06
    col = col + spec[:, None]*np.array([255, 255, 255.])*(.85 - .35*lf[:, None])
    cd = (uu-.42)**2 + (vv+.48)**2
    caus = np.exp(-cd/.05)*.22*(1-lf)
    col = col + caus[:, None]*np.array([255, 250, 236.])
    rim = np.clip((r2[inside]-.93)/.07, 0, 1)**2
    col = col*(1-rim[:, None]*.55) + rim[:, None]*.55*np.array([246, 250, 255.])
    img = np.zeros((S, S, 4)); img[inside, :3] = np.clip(col, 0, 255); img[inside, 3] = 255
    if japan:
        jx, jy, jz = _v(*JAPAN) @ e, _v(*JAPAN) @ n, _v(*JAPAN) @ c
        if jz > 0:
            px, py = (jx+1)/2*S, (1-jy)/2*S
            rr = np.hypot(x-px, y-py)
            a = np.clip(1-(rr/(S*.0055)), 0, 1)
            halo = np.exp(-(rr/(S*.016))**2)*.35
            t = np.clip(a + halo, 0, 1)*(img[..., 3] > 0)
            for k, cv in enumerate((214, 24, 48)):
                img[..., k] = img[..., k]*(1-t) + cv*t
    im = Image.fromarray(img.astype(np.uint8), 'RGBA')
    return im.resize((N, N), Image.LANCZOS)

def proj(lat, lon, N, lon0, lat0, roll=0):
    c, e, n = _basis(lon0, lat0, roll); p = _v(lat, lon)
    return (p@e+1)/2*N, (1-p@n)/2*N, p@c

def orbit(N, lon0, lat0, roll, tilt, yaw, rr=1.3, dots=(), squash=1.0, cx=0, cy=0, scale=1.0):
    """3D circle of radius rr around the globe; returns (front_path, back_path, dots[(x,y,front)]) in px."""
    c, e, n = _basis(lon0, lat0, roll)
    t = np.radians(np.arange(0, 360.5, .5))
    p = np.stack([np.cos(t), np.sin(t)*squash, np.zeros_like(t)], -1)*rr
    a, b = math.radians(tilt), math.radians(yaw)
    Rx = np.array([[1, 0, 0], [0, math.cos(a), -math.sin(a)], [0, math.sin(a), math.cos(a)]])
    Rz = np.array([[math.cos(b), -math.sin(b), 0], [math.sin(b), math.cos(b), 0], [0, 0, 1]])
    q = p @ Rx.T @ Rz.T                                   # view space directly (x right, y up, z to viewer)
    X = cx + (q[:, 0]+1)/2*N*scale; Y = cy + (1-q[:, 1])/2*N*scale
    hidden = (q[:, 2] < 0) & (q[:, 0]**2+q[:, 1]**2 < 1)
    fr, bk = [], []
    for k in range(len(t)):
        (bk if hidden[k] else fr).append((X[k], Y[k], k))
    def segs(pts):
        out = ''; prev = None
        for x, y, k in pts:
            out += ('L' if prev is not None and k == prev+1 else 'M') + f'{x:.1f},{y:.1f}'; prev = k
        return out
    ds = []
    for ang in dots:
        k = int(ang*2) % len(t); ds.append((X[k], Y[k], not hidden[k]))
    return segs(fr), segs(bk), ds

def render_flat(W, H, lon_a, lon_b, lat_top, lat_bot, ss=2, ocean_glass=True):
    """Equirectangular panorama with the same faceted mineral texture; ocean = transparent (alpha) glass tint."""
    Sw, Sh = W*ss, H*ss
    y, x = np.mgrid[0:Sh, 0:Sw]
    lon = lon_a + (x+.5)/Sw*(lon_b-lon_a); lat = lat_top - (y+.5)/Sh*(lat_top-lat_bot)
    lon = (lon+180) % 360 - 180
    P = _v(lat, lon).reshape(-1, 3)
    lf = globe.is_land(lat, lon).reshape(-1)
    d, idx = TREE_F.query(P, k=2); idx = idx*3
    edge = np.clip(1-(d[:, 1]-d[:, 0])/(SPACING*1.7*.09), 0, 1)
    g = _gold(P)
    # gentle cylinder: surface normal turns left/right across the sheet -> dynamism
    t = ((x+.5)/Sw).reshape(-1); cyl = (t-.5)*1.3
    nv = np.stack([np.sin(cyl)*.6, np.full_like(t, .25), np.cos(cyl)], -1)
    nrm = nv + CELL_N[idx[:, 0]]*.9; nrm /= np.linalg.norm(nrm, axis=1)[:, None]
    diff = np.clip(nrm @ LIGHT, 0, 1)
    shade = .18 + .86*diff + (CELL_R[idx[:, 0]]-.5)*.16
    tl = mix(mix(GRAPH_D, GRAPH_L, np.clip(shade, 0, 1)), mix(GOLD_D, GOLD_L, np.clip(shade, 0, 1)), np.clip(g*1.15, 0, 1))
    sp = (CELL_S[idx[:, 0]] > .86)*g
    tl = tl + sp[:, None]*np.array([90, 70, 30.])
    tl = tl*(1-.18*edge[:, None]) + edge[:, None]*.18*np.array([250, 240, 220.])
    img = np.zeros((Sh*Sw, 4))
    img[:, :3] = np.clip(tl, 0, 255); img[:, 3] = lf*255
    im = Image.fromarray(img.reshape(Sh, Sw, 4).astype(np.uint8), 'RGBA')
    return im.resize((W, H), Image.LANCZOS)

def flat_xy(lat, lon, W, H, lon_a, lon_b, lat_top, lat_bot):
    while lon < lon_a: lon += 360
    return (lon-lon_a)/(lon_b-lon_a)*W, (lat_top-lat)/(lat_top-lat_bot)*H
