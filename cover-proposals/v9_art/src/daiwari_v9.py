# 台割 v9 — 「金の軌道」が全ページを一本の糸として走る、アート寄りのB案デザイン
import base64, io, math, random
import numpy as np
from PIL import Image
import glassglobe2 as G
from common9 import *

_c = {}


def uri(f, mx=1400, fmt='JPEG', crop=None, light=0):
    k = (f, mx, fmt, crop, light)
    if k not in _c:
        im = Image.open(f if '/' in f else 'img/' + f)
        im = im.convert('RGBA' if fmt == 'PNG' else 'RGB')
        if crop:
            w, h = im.size; im = im.crop((int(crop[0] * w), int(crop[1] * h), int(crop[2] * w), int(crop[3] * h)))
        if light:
            wh = Image.new(im.mode, im.size, (255, 255, 255, 0) if fmt == 'PNG' else (255, 255, 255))
            a = im.split()[-1] if fmt == 'PNG' else None
            im = Image.blend(im, wh, light)
            if a: im.putalpha(a)
        im.thumbnail((mx, mx)); bf = io.BytesIO(); im.save(bf, fmt, **({'quality': 84} if fmt == 'JPEG' else {}))
        _c[k] = f'data:image/{fmt.lower()};base64,' + base64.b64encode(bf.getvalue()).decode()
    return _c[k]


CSS = font_css() + f"""
@page{{size:420mm 297mm;margin:0}}*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:NS,'Noto Sans JP',sans-serif;color:{INK};background:#fff}}
.sp{{position:relative;width:1190px;height:842px;overflow:hidden;background:#fff;page-break-after:always;zoom:1.3333}}
.a{{position:absolute}}
.lab{{font-size:6.6px;letter-spacing:2.4px;color:{GOLD};font-weight:400}}
.labj{{font-size:6.6px;letter-spacing:.6px;color:{MUTE};font-weight:300}}
.en{{font-weight:200;color:{INK};letter-spacing:-.2px;line-height:1.1}}
.jt{{font-family:'Noto Sans JP';font-weight:500;font-size:11px;letter-spacing:.8px;color:{INK}}}
.js{{font-family:'Noto Sans JP';font-weight:300;font-size:8.2px;letter-spacing:.4px;color:{SUB};line-height:1.6}}
.bd{{font-size:7.4px;line-height:1.75;color:#7b8188;font-weight:300;letter-spacing:.1px}}
.cap{{font-size:6px;letter-spacing:1.4px;color:{MUTE}}}
.num{{font-weight:200;color:{INK};line-height:1;letter-spacing:-.5px}}
.sm{{font-family:'Noto Sans JP';font-size:6.6px;line-height:1.55;color:{SUB};font-weight:300}}
.smb{{font-family:'Noto Sans JP';font-size:7.4px;line-height:1.45;color:{INK};font-weight:400}}
.memo{{font-family:'Noto Sans JP';font-size:5.6px;color:#a3a8ae;background:rgba(255,255,255,.85);padding:1px 3px;letter-spacing:.2px;line-height:1.5}}
.fo{{font-size:6.2px;letter-spacing:1.6px;color:{MUTE}}}
.ph{{object-fit:cover;display:block}}
.ghost{{font-weight:200;color:transparent;-webkit-text-stroke:.5px {GOLD_PALE};line-height:.8;letter-spacing:-4px}}
"""


def A(x, y, h, w=None, c='', s=''):
    return f'<div class="a {c}" style="left:{x}px;top:{y}px;{f"width:{w}px;" if w else ""}{s}">{h}</div>'


def IMG(x, y, w, h, f, pos='50% 50%', r=0, extra='', **k):
    return f'<img class="a ph" src="{uri(f, **k)}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-position:{pos};{f"border-radius:{r}px;" if r else ""}{extra}">'


def CIRC(cx, cy, d, f, pos='50% 50%', ring_=True, mx=600, crop=None):
    o = f'<img class="a ph" src="{uri(f, mx, crop=crop)}" style="left:{cx - d / 2}px;top:{cy - d / 2}px;width:{d}px;height:{d}px;border-radius:50%;object-position:{pos};box-shadow:0 6px 18px rgba(44,76,110,.16)">'
    if ring_: o += f'<div class="a" style="left:{cx - d / 2 - 4}px;top:{cy - d / 2 - 4}px;width:{d + 8}px;height:{d + 8}px;border-radius:50%;border:.6px solid {GOLD_PALE}"></div>'
    return o


def ORB(cx, cy, d, op=1):
    """small clear glass sphere (no continents) — used as a node / bubble"""
    S = d * G.PAD
    return f'<img class="a" src="{png("v9/orb.png")}" style="left:{cx - S / 2}px;top:{cy - S / 2}px;width:{S}px;height:{S}px;opacity:{op}">'


random.seed(4)
LO = 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua enim ad minim veniam quis nostrud exercitation ullamco laboris nisi aliquip ex ea commodo consequat duis aute irure in reprehenderit voluptate velit esse cillum fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt culpa qui officia deserunt mollit anim id est laborum'.split()


def lorem(n):
    w = [random.choice(LO) for _ in range(n)]; w[0] = w[0].capitalize(); s = ''
    for i, x in enumerate(w): s += x + ('. ' if i % 13 == 12 else ' ')
    return s.strip() + '.'


def BODY(x, y, w, n, s=''): return A(x, y, lorem(n), w, 'bd', s)


def HEAD(x, y, lab, labj, en, jt, js, w=440, size=30):
    o = A(x, y, lab, None, 'lab') + A(x, y + 11, labj, None, 'labj')
    o += A(x, y + 34, en, w, 'en', f'font-size:{size}px')
    lines = en.count('<br>') + 1; yy = y + 34 + lines * size * 1.1 + 12
    o += A(x, yy, '', 26, '', f'height:0;border-top:1px solid {RED}')
    o += A(x, yy + 10, jt, w, 'jt') + A(x, yy + 27, js, w, 'js')
    return o, yy + 27 + (js.count('<br>') + 1) * 13.5


def GHOST(x, y, t, size=150):
    """large outlined chapter numeral in pale gold — a quiet art element"""
    return A(x, y, t, None, 'ghost', f'font-size:{size}px')


def spread(under, body, over, l, r, memo_l, memo_r):
    o = '<div class="sp">' + svg(under) + body + svg(over)
    o += A(48, 806, f'{l:02d}', None, 'fo') + A(1130, 806, f'{r:02d}', None, 'fo')
    o += A(48, 818, '台割メモ｜' + memo_l, 480, 'memo') + A(643, 818, '台割メモ｜' + memo_r, 480, 'memo')
    return o + '<div class="a" style="left:595px;top:0;height:842px;border-left:.5px dashed #e3e6e9"></div></div>'


def thread(pts, seed, dots=(), sw=.6, n=70, twin=8):
    """the booklet's running gold thread: a main hairline + a paler twin + gold dust"""
    twin_pts = [(x, y + twin * math.sin(i * 1.3)) for i, (x, y) in enumerate(pts)]
    o = curve(twin_pts, sw * .55, GOLD_PALE, .9)
    o += curve(pts, sw, GOLD, .85, dots)
    o += dust(seed, sample_curve(pts, 500), n, 4)
    return o


L = 48; R = 643; W = 499
pages = []
V3 = (-28, -8, -10); FR = (-42, 6, -8); BK = (138, -14, 6)
GL_V3 = 'v9/gl_-28_-8_-10_1700.png'; GL_FR = 'v9/gl_-42_6_-8_1700.png'; GL_BK = 'v9/gl_138_-14_6_1100.png'
# thread hand-off heights between spreads (exit y of spread k == entry y of spread k+1)
HAND = [None, 520, 300, 470, 470]

# =================== P02-03  Opening ===================
gx, gy, D = 170, 560, 800
U = O = ''; pts_all = []; zs_all = []
for rr, tilt, yaw, sw, col, dots in [(1.08, -77, -14, .6, GOLD, ((300, 1), (20, 0))), (1.2, -70, 12, .45, GOLD, ((330, 0),)),
                                      (1.34, -80, -2, .32, GOLD_PALE, ()), (2.3, -87, 3.4, .6, GOLD, ((356, 1), (8, 0))),
                                      (2.5, -86, 2.6, .3, GOLD_PALE, ((4, 0),))]:
    u, o = ring(gx, gy, D / 2 * rr, tilt, yaw, occ=(gx, gy, D / 2), sw=sw, col=col, dots=dots); U += u; O += o
    p, z = ring_pts(gx, gy, D / 2 * rr, tilt, yaw); pts_all += p; zs_all += list(z)
b = wash(gx - 560, gy - 560, 1120, 1120, .45)
b += globe(gx, gy, D, GL_V3) + svg(G.graticule(V3, gx - D / 2, gy - D / 2, D, op=.26) + G.net(V3, gx - D / 2, gy - D / 2, D, seed=9, k=60))
b += flare(gx + 170, gy - 230, 150, .5)
b += A(L, 58, 'MITSUBISHI CORPORATION　MINERAL RESOURCES GROUP', None, 'lab')
b += A(R, 132, 'Strength to Hold.<br>Power to Connect.', 470, 'en', 'font-size:42px;line-height:1.08')
b += A(R, 240, '', 26, '', f'border-top:1px solid {RED}')
b += A(R, 254, 'コアメッセージ（英文主体・和文は確認用）', None, 'labj')
b += BODY(R, 274, 300, 80, 'font-size:8.2px;line-height:1.85;color:#6c7279')
toc = [('01', 'Who We Are', '我々は何者か｜三菱商事 金属資源グループ', '04'), ('02', 'What We Do', '独自価値｜フットプリント・原料炭・銅・トレーディング・新技術', '05'),
       ('03', 'Why Partners Choose Us', '選ばれ続ける理由｜Partner of Choice', '10'), ('04', 'Our Vision', '何を実現するか｜外部環境と私たちの約束', '11')]
b += A(R, 586, 'CONTENTS', None, 'lab')
for i, (n, e, j, p) in enumerate(toc):
    y = 606 + i * 44
    b += A(R, y, '', W - 40, '', f'border-top:.5px solid {HAIR}') + A(R, y + 9, n, None, 'num', f'font-size:18px;color:{GOLD}')
    b += A(R + 44, y + 8, e, None, '', 'font-size:11px;font-weight:300;letter-spacing:.2px') + A(R + 44, y + 24, j, None, 'sm') + A(R + W - 60, y + 10, 'P.' + p, None, 'fo')
O += dust(11, pts_all, 220, 4, zs_all)
pages.append(spread(U, b, O, 2, 3, '導入。表紙の地球儀を大きく扉に。軌道の輪がノドを越えて右ページへ伸び、コアメッセージと目次の間を通る（＝冊子を貫く「金の軌道」の起点）。',
                    'コアメッセージと目次のみ。軌道線は文字に掛からない高さで横断させ、右端から次の見開きへ抜ける。'))

# =================== P04  Who We Are / P05 Global Footprint ===================
U = O = ''
b, yy = HEAD(L, 52, '01　WHO WE ARE', '第1章　我々は何者か', 'From resource<br>to market.', '三菱商事 金属資源グループとは', '投資とトレーディングの両輪で、川上から川下までをつなぐ', size=30)
b = GHOST(L + 330, 30, '01', 170) + b
b += BODY(L, yy + 6, 300, 52)
# the two wheels drawn as two 3D orbits; five stations ride the front arc
cx, cy, RR = L + W / 2, 452, 238
ui, oi = ring(cx, cy - 4, RR, -78, 0, sw=.9, col=GOLD, op=(.25, .95), nseg=160)
ut, ot = ring(cx, cy + 6, RR * .96, -78, 180, sw=.9, col=BLUE, op=(.2, .8), nseg=160)
U += ui + ut; O += oi + ot
pts, zs = ring_pts(cx, cy - 4, RR, -78, 0, n=720)
CROP = {'x_vc_mine.jpg': (0, 0, .84, 1), 'x_vc_ev.jpg': (.18, 0, 1, 1)}
st = [('x_vc_mine.jpg', 'Mine', '資源開発・保有', '50% 50%'), ('_mr_project_06.png', 'Trade', 'トレーディング', '50% 50%'), ('x_vc_smelter.jpg', 'Smelt / Steel', '製錬・製鉄', '50% 40%'),
      ('r-072.jpeg', 'Trade', 'トレーディング', '50% 50%'), ('x_vc_ev.jpg', 'End use', '最終製品・需要家', '40% 50%')]
angs = [195, 233, 270, 307, 345]
for a, (f, e, j, p) in zip(angs, st):
    x, y = pts[int(a * 2) % 720]
    d = 56 if a == 270 else 48
    b += CIRC(x, y, d, f, p, crop=CROP.get(f)) + A(x - 45, y + d / 2 + 8, e, 90, '', 'text-align:center;font-size:7.2px;font-weight:400;letter-spacing:.3px') + A(x - 45, y + d / 2 + 19, j, 90, 'sm', 'text-align:center')
b += A(cx - 150, cy - 86, f'<b style="font-weight:500;color:{GOLD}">INVESTMENT</b>　資源投資｜鉄鋼原料本部・クリティカルミネラル本部', 300, 'sm', 'text-align:center')
b += A(cx - 160, cy + 128, f'<b style="font-weight:500;color:{BLUE}">TRADING (RtM)</b>　トレーディング｜金属資源トレーディング本部', 320, 'sm', 'text-align:center')
# journey: dates as beads on a hairline
jy = 612
b += A(L, jy, 'OUR JOURNEY', None, 'lab') + A(L + 90, jy, '時代を先読みし、事業モデルを変革してきた歩み', None, 'sm')
era = [('〜1990s', 'トレーディングに参入し、少数株主として出資'), ('1990s', '口銭モデルから投資モデルへ。JV運営の知見を蓄積'), ('2000s', '中国の成長を捉え、事業経営に関与（BHPと50:50）'),
       ('2010s', '原料炭偏重から脱却。資産価値の最大化へ'), ('2020s〜', '地域特化から、グローバルなトレーダーへ')]
for i, (y_, t) in enumerate(era):
    x = L + i * 101; b += A(x, jy + 18, y_, None, 'num', 'font-size:15px') + A(x, jy + 58, t, 92, 'sm')
    O += f'<circle cx="{x + 4}" cy="{jy + 46}" r="4.5" fill="{GOLD_HI}" opacity=".2"/><circle cx="{x + 4}" cy="{jy + 46}" r="1.6" fill="{GOLD}"/>'
b += A(L, jy + 110, 'Guided by the Three Corporate Principles of Mitsubishi Corporation — Corporate Responsibility to Society, Integrity and Fairness, Global Understanding through Business.', W, 'bd', f'font-size:6.6px;color:{MUTE}')
# ---- P05 footprint (crystal-glass map, same material as the globe)
b2, yy = HEAD(R, 52, '02　WHAT WE DO', '第2章　独自価値', 'Where we work.', 'グローバル・フットプリント', '多様な資源と地域で、事業と人の拠点を広げる', size=30)
b += GHOST(R + 330, 30, '02', 170) + b2
MW = W + 48; MH = MW * 138 / 360; my = 252
b += f'<div class="a" style="left:{R - 40}px;top:{my - 30}px;width:{MW + 80}px;height:{MH + 60}px;background:radial-gradient(closest-side,rgba(214,230,244,.55),rgba(255,255,255,0))"></div>'
b += f'<img class="a" src="{png("v9/flat_std.png", 1800)}" style="left:{R - 10}px;top:{my}px;width:{MW}px;height:{MH}px">'
Pm = lambda lo, la: (R - 10 + (lo + 170) / 360 * MW, my + (80 - la) / 138 * MH)
PRJ = [(-66.9, 52.9), (-71.2, -28.5), (-70.6, -33.4), (148.3, -22.3), (-69.07, -24.27), (-70.5, -31.7), (-70.3, -33.15), (-77.05, -9.53), (-70.6, -17.1)]
DEV = [(-70.3, -22.9), (-110.9, 31.9), (-128.9, 58.5), (121.4, -30.7), (-94.0, 51.6), (141.7, -13.3), (25.7, 64.2), (-0.6, 54.4)]
OFF = [(139.7, 35.7), (103.8, 1.3), (77.2, 28.6), (-0.1, 51.5), (-77.0, 40.4), (55.3, 25.2), (106.8, -6.2), (100.5, 13.7), (-70.65, -33.45), (28.0, -26.2), (-58.4, -34.6), (-46.6, -23.5), (153.0, -27.5), (-77.0, -12.0), (-123.1, 49.3), (121.5, 31.2)]
o = ''
tkx, tky = Pm(139.7, 35.7)
for lo, la in PRJ[:6]:     # faint gold routes from Tokyo to the main assets (wraps the right way)
    x, y = Pm(lo, la)
    if x < tkx - 300: x2 = x + MW;
    else: x2 = x
    mx_ = (tkx + x2) / 2; my_ = min(tky, y) - 40
    o += f'<path d="M{tkx:.1f},{tky:.1f} Q{mx_:.1f},{my_:.1f} {x2:.1f},{y:.1f}" fill="none" stroke="{GOLD}" stroke-width=".35" opacity=".45"/>' if x2 == x else ''
for lo, la in OFF:
    x, y = Pm(lo, la); o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="{BLUE}" stroke="#fff" stroke-width=".7"/>'
for lo, la in DEV:
    x, y = Pm(lo, la); o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.9" fill="#fff" stroke="{GOLD}" stroke-width="1.1"/>'
for lo, la in PRJ:
    x, y = Pm(lo, la); o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{GOLD_HI}" opacity=".22"/><circle cx="{x:.1f}" cy="{y:.1f}" r="2.9" fill="{GOLD}" stroke="#fff" stroke-width=".7"/>'
ly = my + MH + 10
o += f'<circle cx="{R + 4}" cy="{ly + 5}" r="2.9" fill="{GOLD}"/><circle cx="{R + 104}" cy="{ly + 5}" r="2.9" fill="#fff" stroke="{GOLD}" stroke-width="1.1"/><circle cx="{R + 234}" cy="{ly + 5}" r="2.6" fill="{BLUE}"/>'
b += A(R + 11, ly, '事業・資産', None, 'sm') + A(R + 111, ly, '開発・探鉱プロジェクト', None, 'sm') + A(R + 241, ly, 'トレーディング拠点・金属資源の駐在', None, 'sm')
# commodities as beads strung on an orbit arc
cy_ = ly + 44
b += A(R, cy_, 'OUR RESOURCES', None, 'lab') + A(R + 150, cy_ + 2, '主力の2事業（原料炭・銅）は次の見開きで詳しく', None, 'sm', f'color:{GOLD}')
com = [('r-048.jpeg', 'Metallurgical Coal', '原料炭', 1), ('r-054.jpeg', 'Copper', '銅', 1), ('x_ironore.jpg', 'Iron Ore', '鉄鉱石', 0), ('x_case_mine.jpg', 'Nickel', 'ニッケル', 0),
       ('x_lithium.jpg', 'Lithium', 'リチウム', 0), ('x_alu.jpg', 'Aluminium', 'アルミ・ボーキサイト', 0), ('r-074.jpeg', 'Recycled', '二次資源', 0)]
arc_y = cy_ + 54
o += f'<path d="M{R - 20},{arc_y + 14} Q{R + W / 2},{arc_y - 26} {R + W + 30},{arc_y + 14}" fill="none" stroke="{GOLD}" stroke-width=".55" opacity=".8"/>'
x = R + 20
for f, e, j, big in com:
    d = 44 if big else 30
    t = (x + d / 2 - R + 20) / (W + 50); yarc = (1 - t) ** 2 * (arc_y + 14) + 2 * (1 - t) * t * (arc_y - 26) + t * t * (arc_y + 14)
    b += CIRC(x + d / 2, yarc, d, f, ring_=bool(big)) + A(x + d / 2 - 30, yarc + d / 2 + 6, e, 60, '', 'text-align:center;font-size:6.2px;font-weight:' + ('500' if big else '300')) + A(x + d / 2 - 30, yarc + d / 2 + 16, j, 60, 'sm', 'text-align:center;font-size:5.8px')
    x += d + (30 if big else 26)
O += o
# the running thread: enters at the left edge, rides above the wheels, crosses the spine under the map
th = [(-10, HAND[1]), (40, 430), (140, 342), (330, 306), (595, 236), (760, 212), (1000, 232), (1200, HAND[2])]
O += thread(th, 21, dots=(3, 6))
pages.append(spread(U, b, O, 4, 5, '第1章を1ページに集約。「投資×トレーディングの両輪」を、地球を回る2本の軌道（金＝投資／青＝トレーディング）として描き、5つの段階をその上に載せる。',
                    '第2章の扉＝全体像。地図は表紙と同じ「結晶×ガラス」の質感。取扱資源は軌道の弧に連ねる。拠点・駐在（青）は名称なし・凡例のみ。'))

# =================== P06 Coal / P07 Copper — photos seen through one great lens ===================
U = O = ''
LC = (595, -2060, 2400)        # giant circle whose lower arc frames both photos
hh = 340
b = (f'<div class="a" style="left:0;top:0;width:1190px;height:{hh}px;clip-path:circle({LC[2]}px at {LC[0]}px {LC[1]}px);overflow:hidden">'
     + IMG(0, 0, 595, hh, 'r-047.jpeg', '50% 45%', mx=1600) + IMG(595, 0, 595, hh, 'r-054.jpeg', '50% 60%', mx=1600) + '</div>')
b += A(L, 40, '02　WHAT WE DO｜PILLAR 1', None, 'lab', 'color:#fff;text-shadow:0 0 6px rgba(0,0,0,.35)') + A(R, 40, '02　WHAT WE DO｜PILLAR 2', None, 'lab', 'color:#fff;text-shadow:0 0 6px rgba(0,0,0,.35)')
O += f'<circle cx="{LC[0]}" cy="{LC[1]}" r="{LC[2] + 9}" fill="none" stroke="{GOLD}" stroke-width=".6" opacity=".85"/>'
O += f'<circle cx="{LC[0] + 30}" cy="{LC[1] - 6}" r="{LC[2] + 22}" fill="none" stroke="{GOLD_PALE}" stroke-width=".4" opacity=".9"/>'
# thread enters, dives under the lens edge and comes out on the right
th = [(-10, HAND[2]), (120, 300), (300, 352), (595, 352), (900, 336), (1080, 360), (1200, HAND[3])]
O += thread(th, 31, dots=(2, 4), twin=5)
top = hh + 40
b += A(L, top, 'World-class<br>metallurgical coal.', W, 'en', 'font-size:28px')
b += A(L, top + 72, '', 26, '', f'border-top:1px solid {RED}') + A(L, top + 82, '原料炭事業', None, 'jt') + A(L, top + 99, '鉄の主原料“産業のコメ”を、世界最高品位で届ける', None, 'js')
kp = [('~50<span style="font-size:16px">%</span>', '一級強粘炭の供給に占める<br>BMAのシェア'), ('~20<span style="font-size:16px">%</span>', '原料炭の海上輸出市場<br>シェア'), ('60<span style="font-size:16px">+ yrs</span>', '炭鉱寿命。<br>港湾・鉄道まで自社保有')]
for i, (n, t) in enumerate(kp):
    x = L + i * 168; b += A(x, top + 136, '', 150, '', f'border-top:.6px solid {GOLD}') + A(x, top + 148, n, None, 'num', 'font-size:34px') + A(x, top + 190, t, 150, 'sm')
    O += f'<circle cx="{x}" cy="{top + 136.3}" r="1.6" fill="{GOLD}"/>'
b += BODY(L, top + 236, 250, 62)
# Bowen basin: crystal mini map + a small orbit round the basin
mx, my2, mw = L + 292, top + 222, 200; mh = mw * 34 / 43
b += f'<img class="a" src="{png("v9/aus.png", 900)}" style="left:{mx}px;top:{my2}px;width:{mw}px;height:{mh}px">'
bx = mx + (148.3 - 112) / 43 * mw; by = my2 + (-10 + 22.3) / 34 * mh
u, o = ring(bx, by, 26, -70, -20, sw=.5, dots=((60, 0),)); U += u; O += o + f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="2.8" fill="{GOLD}" stroke="#fff" stroke-width=".7"/>'
b += A(bx - 92, by - 6, 'Bowen Basin', None, '', 'font-size:6.4px;font-weight:500') + A(bx - 92, by + 4, 'Queensland', None, 'cap')
b += A(mx, my2 + mh + 4, 'BHPとの50:50合弁（BMA）。1968年 MDP設立／2001年 BMA組成', mw, 'sm')
# copper (right)
b += A(R, top, 'The world\'s largest<br>non-operating copper producer.', W + 10, 'en', 'font-size:28px')
b += A(R, top + 72, '', 26, '', f'border-top:1px solid {RED}') + A(R, top + 82, '銅事業', None, 'jt') + A(R, top + 99, '自社操業を伴わずに、世界最大級の銅ポジションを築く', None, 'js')
kp = [('No.1', 'ノンオペレーターとして<br>世界最大の銅生産者'), ('5 / 5', '参画する主要5鉱山すべてが<br>世界Top15'), ('Top 25<span style="font-size:16px">%</span>', '平均コストは世界の<br>上位25%に位置')]
for i, (n, t) in enumerate(kp):
    x = R + i * 168; b += A(x, top + 136, '', 150, '', f'border-top:.6px solid {GOLD}') + A(x, top + 148, n, None, 'num', 'font-size:34px') + A(x, top + 190, t, 150, 'sm')
    O += f'<circle cx="{x}" cy="{top + 136.3}" r="1.6" fill="{GOLD}"/>'
mx, my2, mw = R, top + 224, 150; mh = mw * 34 / 30
b += f'<img class="a" src="{png("v9/andes.png", 700)}" style="left:{mx}px;top:{my2}px;width:{mw}px;height:{mh}px">'
PJ = lambda lo, la: (mx + (lo + 84) / 30 * mw, my2 + (-3 - la) / 34 * mh)
mines = [('Antamina', -77.05, -9.53), ('Quellaveco', -70.6, -17.1), ('Escondida', -69.07, -24.27), ('Marimaca', -70.3, -22.9), ('Los Pelambres', -70.5, -31.7), ('Anglo American Sur', -70.3, -33.15)]
mp = [PJ(lo, la) for _, lo, la in mines]
O += curve(mp, .45, GOLD, .7)
for (n, lo, la), (x, y) in zip(mines, mp):
    O += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{GOLD_HI}" opacity=".22"/><circle cx="{x:.1f}" cy="{y:.1f}" r="2.3" fill="{GOLD}" stroke="#fff" stroke-width=".6"/>'
    b += A(x - 8 - len(n) * 3.1, y - 4, n, None, '', f'font-size:5.6px;color:{SUB};white-space:nowrap')
b += A(mx, my2 + mh + 4, 'チリ・ペルーを中心に参画（ほか米国 Copper World）', 200, 'sm')
four = [('Tier 1 assets', '規模で世界上位の優良鉱山に参画'), ('Partnerships with majors', '特定1社に偏らず、主要メジャーと協業'), ('Trading relationships', '販売を通じ、業界の幅広い関係を構築'), ('New technology', '業界のボトルネックに挑む技術へ投資')]
for i, (e, j) in enumerate(four):
    y = top + 232 + i * 42; b += A(R + 250, y, f'0{i + 1}', None, 'num', f'font-size:13px;color:{GOLD}') + A(R + 272, y, e, None, '', 'font-size:8px;font-weight:400') + A(R + 272, y + 12, j, 200, 'sm')
pages.append(spread(U, b, O, 6, 7, '主力① 原料炭。2枚の写真を「一つの大きなレンズ（地球の弧）」で切り取り、その縁を金の軌道がなぞる。数字3つ＋結晶質感の地図。',
                    '主力② 銅。原料炭と同じ型で対に。鉱山は地図上を金の線でつなぎ、アンデスに連なる「軌道」として見せる。'))

# =================== P08 RtM / P09 New technology ===================
U = O = ''
b, yy = HEAD(L, 52, '02　WHAT WE DO｜TRADING', '第2章　独自価値', 'Resource to Market.', 'トレーディング事業（RtM）', '一つの商品の中で、投資から販売までを一気通貫でつなぐ', size=30)
b = GHOST(L + 330, 30, '02', 170) + b
nb = [('15', 'industries', '業界'), ('50', 'countries', 'カ国'), ('~1,000', 'customers', '社の販売先')]
for i, (n, e, j) in enumerate(nb):
    x = L + i * 150 + (18 if i else 0); b += A(x, yy + 14, n, None, 'num', 'font-size:38px') + A(x, yy + 56, e.upper(), None, 'cap') + A(x, yy + 66, j, None, 'sm')
    if i < 2: b += A(x + (110 if i == 0 else 108), yy + 24, '×', None, '', f'font-size:18px;font-weight:200;color:{GOLD}')
# five functions orbiting a glass sphere
cx, cy = L + 150, 470
b += wash(cx - 150, cy - 130, 300, 260, .5) + ORB(cx, cy, 86)
b += A(cx - 40, cy - 12, 'RtM', 80, '', f'text-align:center;font-size:16px;font-weight:300;color:{DEEP}') + A(cx - 40, cy + 8, 'Functions', 80, 'cap', 'text-align:center')
u, o = ring(cx, cy, 128, -66, -8, occ=(cx, cy, 43), sw=.7, op=(.25, .95)); U += u; O += o
u, o = ring(cx, cy, 142, -72, 14, occ=(cx, cy, 43), sw=.4, col=GOLD_PALE); U += u; O += o
pts, zs = ring_pts(cx, cy, 128, -66, -8, n=360)
fn = [('Marketing &amp;<br>Procurement', '販売・調達'), ('Logistics', '物流'), ('Financing', 'ファイナンス'), ('Risk<br>Management', 'リスク管理'), ('Carbon<br>Reduction', '脱炭素')]
for i, (e, j) in enumerate(fn):
    k = int((200 + i * 72) % 360); x, y = pts[k]; z = zs[k]
    s = 48 + 8 * z
    b += f'<div class="a" style="left:{x - s / 2}px;top:{y - s / 2}px;width:{s}px;height:{s}px;border-radius:50%;background:rgba(255,255,255,.94);border:.7px solid {GOLD};box-shadow:0 4px 12px rgba(44,76,110,.12);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center"><div style="font-size:5.8px;font-weight:400;line-height:1.2">{e}</div><div class="sm" style="font-size:5.4px">{j}</div></div>'
b += A(cx - 75, 608, 'お客様に提供できる5つの機能', 150, 'smb', 'text-align:center')
bx = L + 330; by = 360
b += A(bx, by, 'BUSINESS MODEL', None, 'lab')
bm = [('MC Assets ＋ Third-party', 'MC保有資産と第三者取引の両方を扱う'), ('Stable supply', '資源確保による安定供給'), ('Market intelligence', '市場・業界動向の発信と知見共有で、事業機会を発掘'), ('Continuous value', 'トレーディング機能の強化で、付加価値を生み続ける')]
for i, (e, j) in enumerate(bm):
    y = by + 22 + i * 52; b += A(bx, y, '', 170, '', f'border-top:.6px solid {HAIR}') + A(bx, y + 8, e, 170, '', 'font-size:8.4px;font-weight:300') + A(bx, y + 22, j, 170, 'sm')
O += f'<line x1="{bx - 9}" y1="{by + 22}" x2="{bx - 9}" y2="{by + 222}" stroke="{GOLD}" stroke-width=".7"/><path d="M{bx - 13},{by + 216} L{bx - 9},{by + 224} L{bx - 5},{by + 216}" fill="none" stroke="{GOLD}" stroke-width=".7"/>'
b += A(L, 660, '', W, '', f'border-top:.6px solid {HAIR}') + A(L, 672, 'グローバルネットワーク 10拠点：Singapore・Japan・India・China・USA・UK・UAE・Indonesia・Thailand・Chile', W, 'sm', f'color:{MUTE}')
# ---- P09 new tech: the resource loop as an orbit round a glass sphere
b2, yy = HEAD(R, 52, '02　WHAT WE DO｜NEW TECHNOLOGY', '第2章　独自価値', 'Investing in<br>what\'s next.', '新技術への取り組み', '銅・クリティカルミネラルを中心に、原料炭まで。業界のボトルネックに挑む技術へ投資する', size=30)
b += b2 + BODY(R, yy + 6, 300, 48)
cx, cy = R + W / 2, 540
b += wash(cx - 260, cy - 170, 520, 340, .5) + ORB(cx, cy, 120, .95)
u, o = ring(cx, cy, 205, -72, 0, occ=(cx, cy, 60), sw=.9, op=(.25, .95), nseg=160); U += u; O += o
u, o = ring(cx, cy, 228, -76, 6, occ=(cx, cy, 60), sw=.4, col=GOLD_PALE, nseg=160); U += u; O += o
pts, zs = ring_pts(cx, cy, 205, -72, 0, n=360)
stg = [(180, 'Mine', '採掘'), (225, 'Process', '選鉱・浸出'), (290, 'Smelt &amp; Refine', '製錬・精製'), (355, 'End use', '電化・再エネ・AI/DC'), (90, 'Recycle', 'リサイクル')]
for a, e, j in stg:
    x, y = pts[a % 360]; z = zs[a % 360]
    O += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{GOLD_HI}" opacity=".22"/><circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="{GOLD}"/>'
    ox = -74 if x < cx - 60 else (10 if x > cx + 60 else -30); oy = -26 if y < cy else 8
    b += A(x + ox, y + oy, f'<b style="font-weight:400;font-size:7px;color:{INK}">{e}</b><br>{j}', 80, 'sm')
chips = [(cx - 146, cy - 50, 'CiDRA', '選鉱｜回収率・処理能力を向上', 'Copper'), (cx + 18, cy - 50, 'Jetti', '浸出｜触媒で硫化鉱から回収', 'Copper'),
         (cx - 146, cy + 8, 'DESCycle', 'リサイクル｜電子スクラップから銅・貴金属を回収', 'Recycling'), (cx + 18, cy + 8, '〇〇〇〇', '原料炭｜生産性・脱炭素の技術（MC様ご確認）', 'Coal')]
for x, y, n, d, t in chips:
    b += A(x, y, f'<div style="font-size:5.4px;letter-spacing:1.2px;color:{GOLD}">{t.upper()}</div><div style="font-size:9px;font-weight:400">{n}</div><div class="sm" style="font-size:5.8px">{d}</div>', 128, '',
           f'height:48px;padding:6px 8px;background:rgba(255,255,255,.82);border:.6px solid {GOLD_PALE};border-radius:24px;backdrop-filter:blur(2px)')
b += A(R, 712, 'CVCは「銅のバリューチェーン」に限定せず、「新技術への取り組み」として資源横断で示す（議事録対応）', W, 'memo')
th = [(-10, HAND[3]), (50, 430), (160, 345), (330, 318), (595, 318), (800, 360), (1000, 410), (1200, HAND[4])]
O += thread(th, 41, dots=(3,), twin=6)
pages.append(spread(U, b, O, 8, 9, 'ハブ図は削除。RtMの「5つの機能」を、ガラスの球を回る軌道上の衛星として配置（＝表紙の地球儀と同じ世界観）。数字は15×50×1,000の1行。',
                    'CVCを「新技術」の枠で。資源の循環を、ガラスの球を一周する金の軌道として描き、技術事例を内側に置く。'))

# =================== P10 Partner of Choice / P11 Vision ===================
U = O = ''
pc = (240, 105, 272)    # photo seen through a round lens, bleeding top-left
b = f'<div class="a" style="left:{pc[0] - pc[2]}px;top:{pc[1] - pc[2]}px;width:{2 * pc[2]}px;height:{2 * pc[2]}px;border-radius:50%;overflow:hidden">' + IMG(0, 0, 2 * pc[2], 2 * pc[2], 'r-084.jpeg', '50% 30%', mx=1600) + '</div>'
b += f'<div class="a" style="left:{pc[0] - pc[2]}px;top:{pc[1] - pc[2]}px;width:{2 * pc[2]}px;height:{2 * pc[2]}px;border-radius:50%;background:radial-gradient(circle at 70% 75%,rgba(255,255,255,.0) 55%,rgba(255,255,255,.35) 85%,rgba(255,255,255,.7) 100%)"></div>'
for rr, tilt, yaw, sw, col, dots in [(1.06, -74, -18, .65, GOLD, ((320, 1), (20, 0))), (1.18, -70, 10, .4, GOLD_PALE, ((350, 0),))]:
    u, o = ring(pc[0], pc[1], pc[2] * rr, tilt, yaw, occ=(pc[0], pc[1], pc[2]), sw=sw, col=col, dots=dots); U += u; O += o
b += A(L, 40, '03　WHY PARTNERS CHOOSE US', None, 'lab', 'color:#fff;text-shadow:0 0 6px rgba(0,0,0,.4)')
b += GHOST(L + 360, 360, '03', 130)
b += A(L, 396, 'Partner of choice.', W, 'en', 'font-size:30px')
b += A(L, 440, '', 26, '', f'border-top:1px solid {RED}') + A(L, 450, '第3章　選ばれ続ける理由', None, 'jt') + A(L, 467, '資源業界に不可欠な存在として、世界のトッププレイヤーから選ばれ続ける', None, 'js')
st4 = [('Cultural affinity with the majors', '資源メジャーとの企業文化的親和性'), ('JV management capability', '資源投資経験に裏打ちされたJV経営力'), ('Sound financial base', '事業ポートフォリオを活かした健全な財務基盤'), ('Deep insight', 'マクロ環境とバリューチェーンに対する深い知見')]
for i, (e, j) in enumerate(st4):
    x = L + (i % 2) * 255; y = 500 + (i // 2) * 80
    b += A(x, y, f'0{i + 1}', None, 'num', f'font-size:28px;color:{GOLD}') + A(x + 44, y + 2, e, 200, '', 'font-size:9px;font-weight:400') + A(x + 44, y + 17, j, 200, 'sm') + BODY(x + 44, y + 32, 196, 20, 'font-size:6.4px;line-height:1.6')
b += A(L, 668, '', W, '', f'border-top:.6px solid {HAIR}')
b += A(L, 678, 'JOINT VENTURES WITH INDUSTRY LEADERS', None, 'lab') + A(L, 686, '業界最大手とのJV実績', None, 'sm')
for i, n in enumerate(['BHP', 'Rio Tinto', 'Anglo American']):
    b += A(L + 230 + i * 92, 676, n, None, '', 'font-size:13px;font-weight:300;letter-spacing:.3px')
b += A(L, 716, '単なる共同出資者に留まらず、人材派遣・ガバナンス参画・総合力でJVの事業価値を最大化', W, 'sm')
# ---- P11 vision
b += A(R, 52, '04　OUR VISION', None, 'lab') + A(R, 63, '第4章　何を実現するか', None, 'labj')
b += GHOST(R + 330, 30, '04', 170)
b += A(R, 86, 'Building the future<br>of resources, together.', W, 'en', 'font-size:30px')
b += A(R, 160, '', 26, '', f'border-top:1px solid {RED}') + A(R, 170, '共に、資源の未来を築く', None, 'jt') + A(R, 187, 'クリティカルミネラルを取り巻く外部環境に、安定供給と効率的な供給の両面で応える', None, 'js')
cy = 316; cxs = [R + 80, R + 250, R + 420]
fz = [('Demand shift', '産業構造の転換<br>人口増・電化による需要拡大'), ('Supply constraints', '供給制約の深刻化'), ('Geopolitics', '地政学リスクの常態化')]
for x, (e, j) in zip(cxs, fz):
    b += ORB(x, cy, 112)
    b += A(x - 56, cy - 30, f'<div style="font-size:8.4px;font-weight:400">{e}</div><div class="sm" style="font-size:6px;margin-top:3px">{j}</div>', 112, '', 'text-align:center')
    u, o = ring(x, cy, 70, -76, -10, occ=(x, cy, 56), sw=.45, dots=((330, 0),)); U += u; O += o
O += f'<path d="M{cxs[0]},{cy + 64} Q{cxs[1]},{cy + 118} {cxs[1]},{cy + 118} M{cxs[2]},{cy + 64} Q{cxs[1]},{cy + 118} {cxs[1]},{cy + 118}" fill="none" stroke="{GOLD}" stroke-width=".7"/><circle cx="{cxs[1]}" cy="{cy + 118}" r="5" fill="{GOLD_HI}" opacity=".25"/><circle cx="{cxs[1]}" cy="{cy + 118}" r="2" fill="{GOLD}"/>'
b += A(R, cy + 128, 'サプライチェーン確保の重要性と、川上資源への参入障壁が増大', W, 'smb', 'text-align:center')
b += A(R, 500, 'OUR COMMITMENT', None, 'lab')
b += A(R, 518, '“To contribute to a better society by providing a stable supply of high-quality mineral resources that society needs, in a sustainable way.”', W - 20, 'en', 'font-size:15px;line-height:1.45;font-weight:200')
b += A(R, 586, '「社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する」', W, 'sm')
# closing globe (Asia–Oceania side, Japan) — its orbit runs off the page towards the back cover
gcx, gcy, gD = R + W - 40, 724, 190
b += wash(gcx - 180, gcy - 160, 360, 320, .45) + globe(gcx, gcy, gD, GL_BK)
for rr, tilt, yaw, sw, col, dots in [(1.16, -76, -12, .55, GOLD, ((40, 1),)), (2.4, -80, -6, .5, GOLD, ((200, 0),)), (1.32, -72, 10, .32, GOLD_PALE, ())]:
    u, o = ring(gcx, gcy, gD / 2 * rr, tilt, yaw, occ=(gcx, gcy, gD / 2), sw=sw, col=col, dots=dots); U += u; O += o
O += G.net(BK, gcx - gD / 2, gcy - gD / 2, gD, seed=12, k=24)
b += A(R, 660, 'CONTACT', None, 'lab') + A(R, 676, 'Mitsubishi Corporation　Mineral Resources Group<br>2-3-1 Marunouchi, Chiyoda-ku, Tokyo 100-8086, Japan<br>www.mitsubishicorp.com', 260, '', f'font-size:7px;line-height:1.7;font-weight:300;color:{SUB}')
b += A(R, 734, 'お問い合わせ先は残す（議事録：要否は保留）。裏表紙へ移す案も可', None, 'memo')
th = [(-10, HAND[4]), (24, 430), (110, 392), (300, 378), (470, 330), (595, 252), (800, 236), (1000, 240), (1200, 222)]
O += thread(th, 51, dots=(2, 4), twin=6)
pages.append(spread(U, b, O, 10, 11, '写真を丸い「レンズ」で切り抜き、金の軌道が周回。4つの強み＝本文、JV実績＝社名1行。',
                    '外部環境の3つの変化を3つのガラス球に。最後に日本側の地球儀が現れ、軌道が裏表紙へ抜けて冊子を閉じる（＝表紙の軌道と一周してつながる）。'))

links = ''.join(f'<link rel="stylesheet" href="f/nsjp/package/{w}.css">' for w in (300, 400, 500))
open('daiwari_v9.html', 'w').write('<!doctype html><meta charset=utf-8>' + links + '<style>' + CSS + '</style>' + ''.join(pages))
print('ok')
