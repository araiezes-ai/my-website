# 表紙 v15：A-b（両輪の球）と、ネイビー2案（二本の帯／三本の帯）＋書体提案
import math, base64
exec(open('cover11.py').read().split('pages=[]')[0])
exec(open('cover14.py').read().split('def W1')[0].split("exec(open('cover13.py')")[0]+open('cover14.py').read().split('def W1')[0].split("split('# 1 連なる半円')[0])")[1])
J='fnt/fontsource-jost-5.3.0/package/files/'; C='fnt/fontsource-cormorant-garamond-5.3.0/package/files/'
CSS2=CSS+f"""@font-face{{font-family:JO;font-weight:300;src:url(data:font/woff2;base64,{b64(J+'jost-latin-300-normal.woff2')})}}
@font-face{{font-family:JO;font-weight:400;src:url(data:font/woff2;base64,{b64(J+'jost-latin-400-normal.woff2')})}}
@font-face{{font-family:CG;font-weight:300;src:url(data:font/woff2;base64,{b64(C+'cormorant-garamond-latin-300-normal.woff2')})}}
@font-face{{font-family:CG;font-weight:500;src:url(data:font/woff2;base64,{b64(C+'cormorant-garamond-latin-500-normal.woff2')})}}
"""
CU='#B4693E'; GP='#2E3136'; NAVY='#1f2f4a'
def head(font,acc):
    if font=='JO':  # 幾何学サンセリフ（会社案内2026の系譜）
        return (f'<div class="a" style="left:48px;top:64px;font:400 9.5px JO;letter-spacing:3.6px;color:{INK}">MITSUBISHI CORPORATION</div>'
                f'<div class="a" style="left:48px;top:96px;width:40px;border-top:1.4px solid {acc}"></div>'
                f'<div class="a" style="left:48px;top:112px;font:300 31px/1.16 JO;letter-spacing:5.5px;color:{INK}">MINERAL<br>RESOURCES</div>'
                f'<div class="a" style="left:48px;top:196px;font:400 9.5px JO;letter-spacing:3.6px;color:#6b7178">CORPORATE PROFILE</div>')
    else:           # クラシックなセリフ大文字（統合報告書・Web英字見出しの系譜）
        return (f'<div class="a" style="left:48px;top:64px;font:500 10.5px CG;letter-spacing:3.4px;color:{INK}">MITSUBISHI CORPORATION</div>'
                f'<div class="a" style="left:48px;top:96px;width:40px;border-top:1.2px solid {acc}"></div>'
                f'<div class="a" style="left:46px;top:108px;font:300 38px/1.08 CG;letter-spacing:4.5px;color:{INK}">MINERAL<br>RESOURCES</div>'
                f'<div class="a" style="left:48px;top:200px;font:500 10.5px CG;letter-spacing:3.4px;color:#6b7178">CORPORATE PROFILE</div>')
def pg(svg,font,acc,bg=False):
    b=('<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff"/><stop offset=".55" stop-color="#fff"/><stop offset="1" stop-color="#eceef0"/></linearGradient></defs><rect width="595" height="842" fill="url(#bg)"/>') if bg else ''
    foot='<line x1="48" y1="784" x2="547" y2="784" stroke="#9aa0a6" stroke-width=".5"/>'+logo(400,806)
    return f'<div class="pg"><svg class="a" style="left:0;top:0" width="595" height="842" viewBox="0 0 595 842">{b}{svg}{foot}</svg>{head(font,acc)}</div>'
# A-b：両輪の球。二つの球の中心を紙面の光学的中心（やや上）へ、左右対称・紙幅の8割
def SPH(c1,c2):
    r=158; cy=508; a=(212,cy); b=(383,cy)
    o=sph_v(*a,r,c2)+sph_h(*b,r,c2)
    o+=f'<clipPath id="ov"><circle cx="{b[0]}" cy="{b[1]}" r="{r}"/></clipPath><clipPath id="ov2"><circle cx="{a[0]}" cy="{a[1]}" r="{r}"/></clipPath>'
    o+=f'<g clip-path="url(#ov)"><g clip-path="url(#ov2)"><rect x="0" y="0" width="595" height="842" fill="#fff"/>'+sph_v(*a,r,c1)+sph_h(*b,r,c1)+'</g></g>'
    return o
# 三本の帯（C-2を簡素化）：長さの違う三本。赤は細い一本だけ
def BARS3():
    T=CW['2']['t']; o='<defs>'; gs=[]
    for c in (T[0],T[1]):
        i,g=metal(c,0); o+=g; gs.append(i)
    o+='</defs>'
    rows=[(170,40,gs[0]),(96,40,gs[1])]
    y=566
    for x,h,g in rows:
        d=f'M{x},{y} L600,{y} L600,{y+h} L{x},{y+h}Z'
        o+=f'<path d="{d}" fill="url(#{g})"/>'+brushed(d,0,30+y,op=.28); y+=h+14
    o+=f'<rect x="300" y="{y+2}" width="300" height="7" fill="{RED}"/>'
    return o
pages=[(pg(SPH(CU,GP),'CG',CU),'A-b_両輪の球_セリフ'),(pg(SPH(CU,GP),'JO',CU),'A-b_両輪の球_サンセリフ'),
       (pg(M1('2'),'JO',RED,True),'A-2_二本の帯_サンセリフ'),(pg(M1('2'),'CG',RED,True),'A-2_二本の帯_セリフ'),
       (pg(BARS3(),'JO',RED,True),'C-2_三本の帯_サンセリフ'),(pg(BARS3(),'CG',RED,True),'C-2_三本の帯_セリフ')]
open('cover15.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS2+'</style>'+''.join(p for p,_ in pages))
import json; json.dump([n for _,n in pages],open('cover15_names.json','w'),ensure_ascii=False)
