"""Glass globe v9 — closer to the original B-option image: a bright, near-white glass sphere that lets the page show
through, silvery crystal continents with warm gold light, soft atmosphere halo, and hairline gold orbits.

render(N, lon0, lat0, roll) -> RGBA PIL image of N x N px (sphere diameter = N/PAD), transparent outside the halo.
net(...) / graticule(...) / orbit(...) -> SVG fragments in the same pixel space, drawn over the raster."""
import math
import numpy as np
from PIL import Image
from scipy.spatial import cKDTree
from glassglobe import _v, _basis, _gold, _land, SEEDS, JAPAN, mix

# coarser crystal facets than v8 (larger, more legible planes like the original image)
_M = 24000
_i = np.arange(_M) + .5
_phi = np.arccos(1 - 2 * _i / _M); _th = math.pi * (1 + 5 ** .5) * _i
FSEEDS = np.stack([np.cos(_th) * np.sin(_phi), np.sin(_th) * np.sin(_phi), np.cos(_phi)], -1)
_r = np.random.default_rng(5)
FSEEDS += _r.normal(0, .012, FSEEDS.shape); FSEEDS /= np.linalg.norm(FSEEDS, axis=1)[:, None]
TREE = cKDTree(FSEEDS)
CELL_N = _r.normal(0, .27, (_M, 3)); CELL_R = _r.random(_M); CELL_S = _r.random(_M)
SPACING = math.sqrt(4 * math.pi / _M)

PAD = 1.18                                   # image side / sphere diameter (room for the halo)
LIGHT = np.array([.50, .62, .60]); LIGHT /= np.linalg.norm(LIGHT)   # from upper right, like the original

_rng = np.random.default_rng(11)
_F = _rng.normal(0, 1, (48, 3)) * np.repeat([2.5, 5, 9, 16, 30, 52], 8)[:, None]
_PH = _rng.random(48) * 6.283
_AMP = np.repeat([1, .6, .38, .24, .14, .08], 8)


def _noise(P):
    """cheap fractal noise on the sphere, roughly in [-1, 1]"""
    return (np.sin(P @ _F.T + _PH) * _AMP).sum(-1) / 2.2


def _wisps(P):
    """streaky white cloud / frost wisps (anisotropic: stretched along longitude)"""
    Q = P * np.array([1.0, 1.0, 3.2])
    n = _noise(Q * 1.4) + .5 * _noise(Q * 3.1 + 2)
    return np.clip((n - .35) * 1.6, 0, 1)


SILVER_D = np.array([58, 76, 100.]); SILVER_L = np.array([228, 236, 244.])
GOLD_D = np.array([150, 112, 58.]); GOLD_L = np.array([255, 232, 182.])
SKY_C = np.array([238, 245, 251.]); SKY_M = np.array([184, 210, 234.]); SKY_E = np.array([96, 140, 190.])


def render(N, lon0, lat0, roll=0, ss=2, back_a=.16, gold=1.0, japan=True, warm=1.0, land_on=True):
    S = int(N * ss)
    c, e, n = _basis(lon0, lat0, roll)
    y, x = np.mgrid[0:S, 0:S]
    u = ((x + .5) / S * 2 - 1) * PAD
    v = (1 - (y + .5) / S * 2) * PAD
    r2 = u * u + v * v
    r = np.sqrt(r2)
    inside = r2 < 1
    out = np.zeros((S, S, 4))
    # ---------- outer atmosphere halo (white -> pale blue, fades into the page)
    halo = np.exp(-((r - 1) / .03) ** 2) * (r >= 1) * .75 + np.exp(-((r - 1) / .12) ** 2) * (r >= 1) * .28
    out[..., :3] = np.array([214, 230, 246.])
    out[..., 3] = np.clip(halo, 0, 1) * 255

    uu, vv = u[inside], v[inside]
    zz = np.sqrt(np.clip(1 - uu * uu - vv * vv, 0, 1))
    Nv = np.stack([uu, vv, zz], -1)
    Pf = uu[:, None] * e + vv[:, None] * n + zz[:, None] * c
    Pb = uu[:, None] * e + vv[:, None] * n - zz[:, None] * c
    fres = (1 - zz) ** 1.6
    sph = np.clip(Nv @ LIGHT, 0, 1)

    # ---------- glass body: near white in the light, sky blue towards the shaded limb
    t_mid = np.clip(fres * 1.35 + (1 - sph) * .85 - .10, 0, 1)
    col = mix(SKY_C, SKY_M, t_mid)
    col = mix(col, SKY_E, np.clip((fres - .35) * 1.2 * (1 - sph * .8), 0, 1) * .75)
    # internal watery texture
    wn = _noise(Pf * 1.7)
    col = col + wn[:, None] * np.array([10, 9, 6.]) * (1 - fres[:, None])
    # far-side continents faintly through the glass (mirror image, very soft)
    lb = _land(Pb).astype(float) * land_on
    gb = _gold(Pb)
    tb = mix(np.array([150, 172, 196.]), np.array([214, 190, 150.]), gb * .8)
    a = back_a * lb * (1 - .5 * fres)
    col = col * (1 - a[:, None]) + tb * a[:, None]

    # ---------- front continents: silvery crystal facets, light and airy
    lf = _land(Pf) & land_on
    d, idx = TREE.query(Pf, k=2)
    edge = np.clip(1 - (d[:, 1] - d[:, 0]) / (SPACING * .045), 0, 1)
    nrm = Nv + CELL_N[idx[:, 0]] * 1.1
    nrm /= np.linalg.norm(nrm, axis=1)[:, None]
    diff = np.clip(nrm @ LIGHT, 0, 1)
    smooth = np.clip(Nv @ LIGHT, 0, 1)
    shade = .16 + .55 * diff ** .9 + .40 * smooth + (CELL_R[idx[:, 0]] - .5) * .10
    shade = np.clip(shade, 0, 1)
    land = mix(SILVER_D, SILVER_L, shade)
    # snowy / frosted highlights on high-latitude & highlighted facets
    la = np.degrees(np.arcsin(np.clip(Pf[:, 2], -1, 1)))
    snow = np.clip((np.abs(la) - 55) / 18, 0, 1) * .5 + _wisps(Pf) * .22
    land = mix(land, np.array([246, 249, 252.]), np.clip(snow, 0, .8))
    # gold: lit facets inside resource regions become warm champagne, plus a soft glow
    g = _gold(Pf) * gold
    land_g = mix(GOLD_D, GOLD_L, shade)
    land = mix(land, land_g, np.clip(g * 1.05, 0, .92))
    sp = (CELL_S[idx[:, 0]] > .80) * g
    land = land + sp[:, None] * np.array([80, 62, 24.])
    land = land * (1 - .22 * edge[:, None]) + edge[:, None] * .22 * np.array([255, 250, 236.])
    # continents sit *inside* the glass: veil them towards the limb and let the glass colour through
    veil = np.clip(.04 + fres * .55, 0, .7)
    land = land * (1 - veil[:, None]) + col * veil[:, None]
    col = np.where(lf[:, None], land, col)
    # warm under-glow spilling over coasts/sea from the golden regions
    glow = _gold(Pf) * gold * warm
    col = col + (glow ** 1.4)[:, None] * np.array([58, 38, 4.]) * (1 - fres[:, None])

    # ---------- light: broad bloom + crisp highlight + white wisps + inner caustic + bright rim
    H = LIGHT + np.array([0, 0, 1.]); H /= np.linalg.norm(H)
    nh = np.clip(Nv @ H, 0, 1)
    bloom = nh ** 9 * .30 + nh ** 40 * .30 + nh ** 400 * .9
    bloom = bloom * np.where(lf, .55, 1.0)
    col = col * (1 - bloom[:, None]) + 255 * bloom[:, None]
    wisp = _wisps(Pf * 1.0 + .3) * (1 - fres) * .22
    col = col * (1 - wisp[:, None]) + 255 * wisp[:, None]
    cd = (uu + .40) ** 2 + (vv + .52) ** 2
    caus = np.exp(-cd / .035) * .45
    col = col * (1 - caus[:, None]) + np.array([255, 252, 244.]) * caus[:, None]
    rr = np.sqrt(uu * uu + vv * vv)
    rim = np.exp(-((1 - rr) / .008) ** 2) * .8 + np.exp(-((1 - rr) / .05) ** 2) * .30
    col = col * (1 - rim[:, None]) + np.array([250, 253, 255.]) * rim[:, None]
    # gentle transparency: the glass is slightly see-through, the land less so
    alpha = np.where(lf, .97, .88 + .10 * fres)
    alpha = np.clip(alpha + rim * .1, 0, 1)
    # antialias the silhouette
    edge_aa = np.clip((1 - rr) * S / PAD / 1.2, 0, 1)
    alpha = alpha * edge_aa

    oc = out[inside]
    a0 = oc[:, 3] / 255
    a_tot = alpha + a0 * (1 - alpha)
    rgb = (np.clip(col, 0, 255) * alpha[:, None] + oc[:, :3] * (a0 * (1 - alpha))[:, None]) / np.maximum(a_tot, 1e-6)[:, None]
    out[inside, :3] = rgb
    out[inside, 3] = a_tot * 255

    if japan:
        jp = _v(*JAPAN)
        if jp @ c > .05:
            px = ((jp @ e) / PAD + 1) / 2 * S; py = (1 - (jp @ n) / PAD) / 2 * S
            d2 = np.hypot(x - px, y - py)
            t = np.clip(1 - d2 / (S * .0045), 0, 1) + np.exp(-(d2 / (S * .012)) ** 2) * .25
            t = np.clip(t, 0, 1) * (out[..., 3] > 0)
            out[..., :3] = out[..., :3] * (1 - t[..., None]) + np.array([214, 24, 48.]) * t[..., None]
    im = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), 'RGBA')
    return im.resize((N, N), Image.LANCZOS)


# ---------------------------------------------------------------- vector overlays (page px)
def _to_px(q, gx, gy, D):
    """view-space (x,y in sphere radii) -> page px for a globe drawn with sphere diameter D whose top-left is gx,gy"""
    return gx + (q[..., 0] + 1) / 2 * D, gy + (1 - q[..., 1]) / 2 * D


def proj(lat, lon, view):
    c, e, n = _basis(*view)
    p = _v(lat, lon)
    return np.stack([p @ e, p @ n, p @ c], -1)


def net(view, gx, gy, D, seed=3, k=70, col='#c9a35e'):
    """fine golden network of light points + short links over the resource regions (front hemisphere only)"""
    rng = np.random.default_rng(seed)
    idx = rng.choice(len(SEEDS), 30000, replace=False)
    P = SEEDS[idx]
    g = _gold(P)
    keep = (rng.random(len(P)) < g ** 1.6 * .6) & _land(P)
    P = P[keep][:k * 6]
    c, e, n = _basis(*view)
    q = np.stack([P @ e, P @ n, P @ c], -1)
    P, q = P[q[:, 2] > .18], q[q[:, 2] > .18]
    X, Y = _to_px(q, gx, gy, D)
    o = ''
    pts = list(zip(X, Y, q[:, 2]))
    for i, (x, y, z) in enumerate(pts):
        dd = [(math.hypot(x - x2, y - y2), j) for j, (x2, y2, _) in enumerate(pts) if j != i]
        dd.sort()
        for dist, j in dd[:2]:
            if j > i and dist < D * .07:
                o += f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{pts[j][0]:.1f}" y2="{pts[j][1]:.1f}" stroke="{col}" stroke-width=".28" opacity="{.25 + .45 * z:.2f}"/>'
        rr = .45 + .55 * rng.random()
        o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rr * 1.9:.2f}" fill="#ffe7b0" opacity="{.18 * z:.2f}"/><circle cx="{x:.1f}" cy="{y:.1f}" r="{rr * .55:.2f}" fill="#fff6dc" opacity="{.5 + .5 * z:.2f}"/>'
    return o


def graticule(view, gx, gy, D, col='#ffffff', op=.35, sw=.25):
    """a few white meridians / parallels, like light caught in the glass"""
    c, e, n = _basis(*view)
    o = ''
    lines = [('lat', a) for a in (-40, -10, 20, 50)] + [('lon', a) for a in range(-180, 180, 40)]
    for kind, a in lines:
        t = np.arange(-180, 181, 2.) if kind == 'lat' else np.arange(-85, 86, 2.)
        P = _v(np.full_like(t, a), t) if kind == 'lat' else _v(t, np.full_like(t, a))
        q = np.stack([P @ e, P @ n, P @ c], -1)
        X, Y = _to_px(q, gx, gy, D)
        seg = ''
        for k in range(len(t)):
            if q[k, 2] > .02:
                seg += ('L' if seg and q[k - 1, 2] > .02 else 'M') + f'{X[k]:.1f},{Y[k]:.1f}'
        if seg:
            o += f'<path d="{seg}" fill="none" stroke="{col}" stroke-width="{sw}" opacity="{op}"/>'
    return o


def ring3d(tilt, yaw, rr=1.3, squash=1.0, n=720):
    t = np.radians(np.linspace(0, 360, n, endpoint=False))
    p = np.stack([np.cos(t), np.sin(t) * squash, np.zeros_like(t)], -1) * rr
    a, b = math.radians(tilt), math.radians(yaw)
    Rx = np.array([[1, 0, 0], [0, math.cos(a), -math.sin(a)], [0, math.sin(a), math.cos(a)]])
    Rz = np.array([[math.cos(b), -math.sin(b), 0], [math.sin(b), math.cos(b), 0], [0, 0, 1]])
    return p @ Rx.T @ Rz.T


GOLD = '#b8924f'; GOLD_HI = '#e2c78f'; GOLD_PALE = '#e7d8b8'


def orbit(gx, gy, D, tilt, yaw, rr=1.3, squash=1.0, dots=(), sw=.5, col=GOLD, back_op=.22, front_op=.95, nseg=90):
    """hairline 3D orbit. returns (behind_svg, front_svg). opacity follows depth so the ring reads as going round
    the globe; behind the glass it stays faintly visible (the glass is transparent)."""
    q = ring3d(tilt, yaw, rr, squash)
    X, Y = _to_px(q, gx, gy, D)
    m = len(q)
    hidden = (q[:, 2] < 0) & (q[:, 0] ** 2 + q[:, 1] ** 2 < 1)
    zmin, zmax = q[:, 2].min(), q[:, 2].max()
    bk = fr = ''
    step = m // nseg
    for s in range(nseg):
        ks = list(range(s * step, min((s + 1) * step + 1, m + 1)))
        ks = [k % m for k in ks]
        zm = q[ks, 2].mean()
        depth = (zm - zmin) / max(zmax - zmin, 1e-6)
        d = 'M' + 'L'.join(f'{X[k]:.1f},{Y[k]:.1f}' for k in ks)
        if hidden[ks].mean() > .5:
            bk += f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw * .8:.2f}" opacity="{back_op:.2f}"/>'
        else:
            op = .30 + (front_op - .30) * depth
            tgt = 'fr' if zm >= 0 or not ((q[ks, 0] ** 2 + q[ks, 1] ** 2) < 1).any() else 'bk'
            seg = f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw * (.75 + .5 * depth):.2f}" opacity="{op:.2f}"/>'
            if tgt == 'fr': fr += seg
            else: bk += seg
    for ang, big in dots:
        k = int(ang / 360 * m) % m
        if hidden[k]: continue
        x, y = X[k], Y[k]
        rr_ = 1.5 if big else 1.0
        fr += (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rr_ * 4.2:.1f}" fill="{GOLD_HI}" opacity=".16"/>'
               f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rr_:.1f}" fill="{GOLD}"/>')
    return bk, fr


def dust(rng, path_pts, n=40, spread=6, col=GOLD_HI):
    """scatter of tiny gold particles along a list of (x, y) points"""
    o = ''
    for _ in range(n):
        x, y = path_pts[rng.integers(len(path_pts))]
        x += rng.normal(0, spread); y += rng.normal(0, spread)
        o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{.25 + rng.random() * .6:.2f}" fill="{col}" opacity="{.25 + rng.random() * .6:.2f}"/>'
    return o


def render_flat(W, H, lon_a, lon_b, lat_top, lat_bot, ss=2, gold=1.0):
    """equirectangular sheet in the same silvery-crystal language; sea is transparent"""
    Sw, Sh = int(W * ss), int(H * ss)
    y, x = np.mgrid[0:Sh, 0:Sw]
    lon = lon_a + (x + .5) / Sw * (lon_b - lon_a); lat = lat_top - (y + .5) / Sh * (lat_top - lat_bot)
    lon = (lon + 180) % 360 - 180
    P = _v(lat, lon).reshape(-1, 3)
    lf = _land(P)
    d, idx = TREE.query(P, k=2)
    edge = np.clip(1 - (d[:, 1] - d[:, 0]) / (SPACING * .045), 0, 1)
    t = ((x + .5) / Sw).reshape(-1)
    base = np.stack([(t - .5) * .9, np.full_like(t, .2), np.ones_like(t)], -1)
    base /= np.linalg.norm(base, axis=1)[:, None]
    nrm = base + CELL_N[idx[:, 0]]; nrm /= np.linalg.norm(nrm, axis=1)[:, None]
    diff = np.clip(nrm @ LIGHT, 0, 1)
    shade = np.clip(.12 + .62 * diff ** .9 + .30 * np.clip(base @ LIGHT, 0, 1) + (CELL_R[idx[:, 0]] - .5) * .16, 0, 1)
    land = mix(SILVER_D, SILVER_L, shade)
    land = mix(land, np.array([246, 249, 252.]), np.clip(_wisps(P) * .25, 0, .6))
    g = _gold(P) * gold
    land = mix(land, mix(GOLD_D, GOLD_L, shade), np.clip(g * 1.05, 0, .92))
    sp = (CELL_S[idx[:, 0]] > .80) * g
    land = land + sp[:, None] * np.array([80, 62, 24.])
    land = land * (1 - .22 * edge[:, None]) + edge[:, None] * .22 * np.array([255, 250, 236.])
    land = mix(land, np.array([214, 228, 242.]), .18)
    img = np.zeros((Sh * Sw, 4)); img[:, :3] = np.clip(land, 0, 255); img[:, 3] = lf * 235
    im = Image.fromarray(img.reshape(Sh, Sw, 4).astype(np.uint8), 'RGBA')
    return im.resize((W, H), Image.LANCZOS)
