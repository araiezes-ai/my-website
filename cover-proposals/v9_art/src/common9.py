"""shared helpers for v9 (cover + 台割): fonts, logo, page-space orbits, gold dust, light."""
import base64, io, math
import numpy as np
from PIL import Image
import glassglobe2 as G

FONTS = 'f/ns/package/files/'
GOLD = '#b8924f'; GOLD_HI = '#e2c78f'; GOLD_PALE = '#e9dcc0'; SILVER = '#c9d3dd'
INK = '#23272c'; SUB = '#5d636a'; MUTE = '#9aa0a6'; RED = '#C8102E'; HAIR = '#dde1e5'; GLASS = '#e8f0f7'; BLUE = '#5b84ad'; DEEP = '#2c4c6e'


def b64(p): return base64.b64encode(open(p, 'rb').read()).decode()


_cache = {}


def png(path_or_im, mx=None):
    key = (path_or_im if isinstance(path_or_im, str) else id(path_or_im), mx)
    if key not in _cache:
        im = Image.open(path_or_im) if isinstance(path_or_im, str) else path_or_im
        if mx: im = im.copy(); im.thumbnail((mx, mx), Image.LANCZOS)
        bf = io.BytesIO(); im.save(bf, 'PNG', optimize=True)
        _cache[key] = 'data:image/png;base64,' + base64.b64encode(bf.getvalue()).decode()
    return _cache[key]


def font_css():
    o = ''
    for w in (200, 300, 400, 500):
        o += f"@font-face{{font-family:NS;font-weight:{w};src:url(data:font/woff2;base64,{b64(FONTS + f'noto-sans-latin-{w}-normal.woff2')})}}"
    return o


def mark(x, y, s=6.6):
    o = ''
    for th in (-90, 30, 150):
        p = lambda a, d: (x + d * math.cos(math.radians(a)), y + d * math.sin(math.radians(a)))
        q = [(x, y), p(th - 30, s), p(th, s * math.sqrt(3)), p(th + 30, s)]
        o += '<path d="M' + ' L'.join(f'{a:.2f},{b:.2f}' for a, b in q) + 'Z" fill="#E60012"/>'
    return o


def logo(x, y, s=6.6, fs=12.5, col='#1a1a1a'):
    return mark(x, y, s) + f'<text x="{x + 18 * s / 6.6}" y="{y + 4 * s / 6.6}" font-family="Liberation Serif" font-size="{fs}" fill="{col}">Mitsubishi Corporation</text>'


def svg(inner, x=0, y=0, w=1190, h=842):
    return f'<svg class="a" style="left:{x}px;top:{y}px;overflow:visible" width="{w}" height="{h}">{inner}</svg>'


def img(x, y, w, h, uri, extra=''):
    return f'<img class="a" src="{uri}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}">'


def globe(cx, cy, D, path, extra=''):
    """place a rendered glass globe (sphere diameter D, centred at cx,cy); the png carries the halo padding"""
    S = D * G.PAD
    return img(cx - S / 2, cy - S / 2, S, S, png(path), extra)


def ring(cx, cy, R, tilt=-74, yaw=0, squash=1.0, occ=None, sw=.55, col=GOLD, dots=(), op=(.18, .95), nseg=120, dash=None):
    """hairline 3D ring of radius R (px) centred at cx,cy, seen with tilt/yaw.
    occ=(ox,oy,orad): a sphere/photo-disc that hides the far half of the ring (the far half is still drawn faintly:
    the glass is transparent). returns (under_svg, over_svg)."""
    q = G.ring3d(tilt, yaw, 1.0, squash, n=nseg * 6)
    X = cx + q[:, 0] * R; Y = cy - q[:, 1] * R; Z = q[:, 2]
    m = len(q); step = m // nseg
    under = over = ''
    zr = max(Z.max() - Z.min(), 1e-6)
    da = f' stroke-dasharray="{dash}"' if dash else ''
    for s in range(nseg):
        ks = [(s * step + k) % m for k in range(step + 1)]
        z = Z[ks].mean(); depth = (z - Z.min()) / zr
        d = 'M' + 'L'.join(f'{X[k]:.1f},{Y[k]:.1f}' for k in ks)
        hidden = False
        if occ is not None and z < 0:
            ox, oy, orr = occ
            hidden = np.hypot(X[ks] - ox, Y[ks] - oy).mean() < orr
        if hidden:
            under += f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw * .8:.2f}" opacity="{op[0]:.2f}"{da}/>'
        else:
            o_ = op[0] + .1 + (op[1] - op[0] - .1) * depth
            seg = f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw * (.7 + .55 * depth):.2f}" opacity="{o_:.2f}"{da}/>'
            if z >= 0: over += seg
            else: under += seg
    for ang, big in dots:
        k = int(ang / 360 * m) % m
        x, y = X[k], Y[k]
        r_ = 1.6 if big else 1.05
        dot = (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r_ * 4.4:.1f}" fill="{GOLD_HI}" opacity=".18"/>'
               f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r_:.2f}" fill="{GOLD}"/>')
        if Z[k] >= 0: over += dot
        elif occ is None or np.hypot(x - occ[0], y - occ[1]) > occ[2]: under += dot
    return under, over


def ring_pts(cx, cy, R, tilt=-74, yaw=0, squash=1.0, n=360):
    q = G.ring3d(tilt, yaw, 1.0, squash, n=n)
    return list(zip(cx + q[:, 0] * R, cy - q[:, 1] * R)), q[:, 2]


def dust(seed, pts, n=60, spread=5, zs=None, col=GOLD_HI, box=(0, 0, 1190, 842)):
    rng = np.random.default_rng(seed)
    o = ''
    for _ in range(n):
        k = rng.integers(len(pts)); x, y = pts[k]
        if zs is not None and zs[k] < -.2 and rng.random() < .7: continue
        x += rng.normal(0, spread); y += rng.normal(0, spread)
        if not (box[0] <= x <= box[2] and box[1] <= y <= box[3]): continue
        r = .22 + rng.random() ** 2 * .9
        o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" fill="{col}" opacity="{.25 + rng.random() * .65:.2f}"/>'
    return o


def path_pts(d_pts):
    return d_pts


def curve(pts, sw=.6, col=GOLD, op=.9, dots=(), dash=None):
    """smooth Catmull-Rom curve through page points (for the thread that runs through the booklet)"""
    p = [pts[0]] + list(pts) + [pts[-1]]
    d = f'M{p[1][0]:.1f},{p[1][1]:.1f}'
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f' C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}'
    da = f' stroke-dasharray="{dash}"' if dash else ''
    o = f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}" opacity="{op}"{da}/>'
    for i in dots:
        x, y = pts[i]
        o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{GOLD_HI}" opacity=".18"/><circle cx="{x:.1f}" cy="{y:.1f}" r="1.6" fill="{GOLD}"/>'
    return o


def sample_curve(pts, n=400):
    """approximate points along curve() for dust placement"""
    p = [pts[0]] + list(pts) + [pts[-1]]
    out = []
    per = max(2, n // max(1, len(pts) - 1))
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = map(np.array, (p[i - 1], p[i], p[i + 1], p[i + 2]))
        for t in np.linspace(0, 1, per, endpoint=False):
            t2, t3 = t * t, t * t * t
            out.append(tuple(.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 + (-p0 + 3 * p1 - 3 * p2 + p3) * t3)))
    return out


def flare(cx, cy, r, op=.7):
    """soft white light bloom (for art direction: light caught on the glass)"""
    return f'<div class="a" style="left:{cx - r}px;top:{cy - r}px;width:{2 * r}px;height:{2 * r}px;border-radius:50%;background:radial-gradient(closest-side,rgba(255,255,255,{op}),rgba(236,244,251,{op * .35}) 45%,rgba(255,255,255,0));pointer-events:none"></div>'


def wash(x, y, w, h, op=.55):
    """very pale sky-glass wash, used behind globes / at page edges"""
    return f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:50%;background:radial-gradient(closest-side,rgba(214,230,244,{op}),rgba(236,243,250,{op * .4}) 55%,rgba(255,255,255,0))"></div>'


def shadow(cx, cy, rx, ry, op=.16):
    return f'<div class="a" style="left:{cx - rx}px;top:{cy - ry}px;width:{2 * rx}px;height:{2 * ry}px;border-radius:50%;background:radial-gradient(closest-side,rgba(70,96,124,{op}),rgba(70,96,124,0))"></div>'
