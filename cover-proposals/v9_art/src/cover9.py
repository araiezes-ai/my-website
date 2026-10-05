# 表紙 v9 — B案改良をアート寄りに: 透明なガラスの地球儀 + 表裏を貫く金の軌道群
import math
import glassglobe2 as G
from common9 import *

CSS = font_css() + f"""
@page{{size:420mm 297mm;margin:0}}*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#fff}}
.sp{{position:relative;width:1190px;height:842px;overflow:hidden;background:#fff;page-break-after:always;zoom:1.3333;font-family:NS}}
.a{{position:absolute}}
.ttl{{font-weight:200;font-size:22px;line-height:1.36;color:#2b2f34;letter-spacing:.4px}}
.cap{{font-size:6.4px;letter-spacing:1.8px;color:#8a8f95}}
.ver{{font-size:6px;letter-spacing:3.2px;color:{GOLD};writing-mode:vertical-rl}}
"""
FR = (-42, 6, -8); BK = (138, -14, 6); V3 = (-28, -8, -10)
P_FR = 'v9/gl_-42_6_-8_1700.png'; P_BK = 'v9/gl_138_-14_6_1100.png'; P_V3 = 'v9/gl_-28_-8_-10_1700.png'


def title(x, y):
    return (f'<div class="a ttl" style="left:{x}px;top:{y}px">Mitsubishi Corporation<br>Mineral Resources Group<br>Corporate Profile</div>'
            f'<div class="a" style="left:{x}px;top:{y + 104}px;width:58px;border-top:1px solid {RED}"></div>')


def back_info(x=56, y=742):
    return (svg(logo(x + 6, y, 5.4, 10.5)) + f'<div class="a cap" style="left:{x}px;top:{y + 20}px;line-height:1.7">MINERAL RESOURCES GROUP<br>'
            '2-3-1 Marunouchi, Chiyoda-ku, Tokyo 100-8086, Japan<br>www.mitsubishicorp.com</div>')


def fold(): return '<div class="a" style="left:595px;top:0;height:842px;border-left:.5px dashed #e3e6e9"></div>'


def overlays(view, cx, cy, D, seed=3):
    gx, gy = cx - D / 2, cy - D / 2
    return G.graticule(view, gx, gy, D, op=.28) + G.net(view, gx, gy, D, seed=seed, k=60)


def rings(cx, cy, D, spec, seed=1):
    """spec: list of (rr, tilt, yaw, sw, col, dots). returns under, over, dust"""
    U = O = ''; pts = []; zs = []
    for rr, tilt, yaw, sw, col, dots in spec:
        u, o = ring(cx, cy, D / 2 * rr, tilt, yaw, occ=(cx, cy, D / 2), sw=sw, col=col, dots=dots)
        U += u; O += o
        p, z = ring_pts(cx, cy, D / 2 * rr, tilt, yaw); pts += p; zs += list(z)
    return U, O, dust(seed, pts, n=150, spread=4, zs=zs)


pages = []

# ---------------- B-1  二つの半球（表裏で世界一周）
cx1, cy1, D1 = 1000, 478, 560
cx2, cy2, D2 = 250, 372, 250
spec1 = [(1.10, -76, -12, .6, GOLD, ((205, 1), (330, 0))),
         (1.22, -70, 14, .45, GOLD, ((150, 0), (262, 1))),
         (1.38, -80, -4, .35, GOLD_PALE, ((290, 0),)),
         (2.55, -79, -6, .55, GOLD, ((178, 1), (196, 0))),     # the long ring that crosses the spine to the back globe
         (2.85, -77, -9, .3, GOLD_PALE, ((200, 0),))]
u1, o1, d1 = rings(cx1, cy1, D1, spec1, 1)
spec2 = [(1.18, -74, -10, .45, GOLD, ((40, 1),)), (1.36, -78, 6, .3, GOLD_PALE, ())]
u2, o2, d2 = rings(cx2, cy2, D2, spec2, 2)
b = wash(cx1 - 520, cy1 - 470, 1040, 940, .42) + wash(cx2 - 230, cy2 - 210, 460, 420, .35)
b += svg(u1 + u2) + shadow(cx1, cy1 + D1 / 2 + 46, D1 * .34, 16) + shadow(cx2, cy2 + D2 / 2 + 26, D2 * .32, 8, .12)
b += globe(cx1, cy1, D1, P_FR) + globe(cx2, cy2, D2, P_BK)
b += svg(overlays(FR, cx1, cy1, D1, 3) + overlays(BK, cx2, cy2, D2, 4) + o1 + o2 + d1 + d2)
b += flare(cx1 + 150, cy1 - 170, 120, .55)
b += title(595 + 48, 92) + svg(logo(595 + 232, 800)) + back_info()
b += f'<div class="a cap" style="left:56px;top:640px;line-height:1.8">METALLURGICAL COAL&nbsp;&nbsp;·&nbsp;&nbsp;COPPER&nbsp;&nbsp;·&nbsp;&nbsp;IRON ORE&nbsp;&nbsp;·&nbsp;&nbsp;CRITICAL MINERALS&nbsp;&nbsp;·&nbsp;&nbsp;TRADING</div>'
pages.append(('B-1', f'<div class="sp">{b}{fold()}</div>'))

# ---------------- B-2  パノラマ（平面×質感のハイブリッド）
LA, LB, LT, LBt = 50, 410, 80, -58
W2 = 1190; H2 = int(W2 * (LT - LBt) / (LB - LA)); my = 268
P = lambda la, lo: ((((lo - LA) % 360) / (LB - LA)) * W2, (LT - la) / (LT - LBt) * H2 + my)
b = f'<div class="a" style="left:0;top:{my - 70}px;width:1190px;height:{H2 + 140}px;background:linear-gradient(180deg,rgba(255,255,255,0),rgba(220,233,245,.55) 30%,rgba(206,224,240,.7) 55%,rgba(226,236,246,.45) 82%,rgba(255,255,255,0))"></div>'
b += flare(250, my + 120, 260, .8) + flare(930, my + 60, 200, .6)
# three great sweeping orbits behind and in front of the sheet
U = O = ''; pts = []; zs = []
for R_, tilt, yaw, sw, col, dots in [(700, -82, -5, .55, GOLD, ((150, 1), (32, 0))), (760, -80, 3, .35, GOLD_PALE, ((210, 0),)), (640, -84, -9, .45, GOLD, ((330, 1),))]:
    u, o = ring(620, my + H2 * .5, R_, tilt, yaw, sw=sw, col=col, dots=dots); U += u; O += o
    p, z = ring_pts(620, my + H2 * .5, R_, tilt, yaw); pts += p; zs += list(z)
b += svg(U) + img(0, my, W2, H2, png('v9/flat_wide.png'))
tk = P(35.7, 139.7); arcs = ''
for la, lo in [(-23, -69), (-14, -73), (-22, 148), (-23, 119), (-26, 28), (33, -111), (51, 0), (-6, -50), (52, -120)]:
    x, y = P(la, lo); x0, y0 = tk
    mx = (x0 + x) / 2; myy = min(y0, y) - abs(x - x0) * .18 - 14
    arcs += f'<path d="M{x0:.1f},{y0:.1f} Q{mx:.1f},{myy:.1f} {x:.1f},{y:.1f}" fill="none" stroke="{GOLD}" stroke-width=".45" opacity=".75"/>'
    arcs += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{GOLD_HI}" opacity=".2"/><circle cx="{x:.1f}" cy="{y:.1f}" r="1.3" fill="{GOLD}"/>'
arcs += f'<circle cx="{tk[0]:.1f}" cy="{tk[1]:.1f}" r="2.3" fill="{RED}"/>'
b += svg(arcs + O + dust(5, pts, 160, 4, zs))
b += title(595 + 48, 92) + svg(logo(595 + 232, 800)) + back_info()
pages.append(('B-2', f'<div class="sp">{b}{fold()}</div>'))

# ---------------- B-3  透ける地球（表表紙に一つ、裏へ軌道が抜ける）
cx3, cy3, D3 = 595 + 300, 500, 470
spec3 = [(1.12, -78, -12, .6, GOLD, ((205, 1), (330, 0))),
         (1.26, -71, 16, .45, GOLD, ((160, 0), (250, 1))),
         (1.42, -75, 4, .35, GOLD_PALE, ((290, 0),)),
         (2.9, -81, -3, .5, GOLD, ((186, 1), (171, 0))),
         (3.3, -80, -6, .3, GOLD_PALE, ((193, 0),))]
u3, o3, d3 = rings(cx3, cy3, D3, spec3, 6)
b = wash(cx3 - 430, cy3 - 400, 860, 800, .45) + svg(u3) + shadow(cx3, cy3 + D3 / 2 + 44, D3 * .34, 14)
b += globe(cx3, cy3, D3, P_V3) + svg(overlays(V3, cx3, cy3, D3, 7) + o3 + d3) + flare(cx3 + 110, cy3 - 130, 95, .5)
b += title(595 + 48, 92) + svg(logo(595 + 232, 800)) + back_info()
pages.append(('B-3', f'<div class="sp">{b}{fold()}</div>'))

html = '<!doctype html><meta charset=utf-8><style>' + CSS + '</style>' + ''.join(p for _, p in pages)
open('v9/covers9.html', 'w').write(html)
print('ok')
