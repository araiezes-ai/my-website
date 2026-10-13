# 表紙 v17：アート×シンプル 2案（FOLD／ARC）。三菱商事の6つの文法に厳密に沿う
import math, random
exec(open('cover16.py').read().split('S=[')[0])
COP=CW['1']['t']
def miter_quads(pts,w):
    def off(p0,p1,s):
        dx,dy=p1[0]-p0[0],p1[1]-p0[1]; L=math.hypot(dx,dy); return (-dy/L*s,dx/L*s)
    def isect(a,da,b,db):
        den=da[0]*db[1]-da[1]*db[0]; t=((b[0]-a[0])*db[1]-(b[1]-a[1])*db[0])/den; return (a[0]+t*da[0],a[1]+t*da[1])
    n=len(pts)-1
    def side(sg):
        segs=[]
        for k in range(n):
            o=off(pts[k],pts[k+1],sg*w/2); segs.append(((pts[k][0]+o[0],pts[k][1]+o[1]),(pts[k+1][0]-pts[k][0],pts[k+1][1]-pts[k][1])))
        P=[segs[0][0]]+[isect(segs[k][0],segs[k][1],segs[k+1][0],segs[k+1][1]) for k in range(n-1)]
        P.append((segs[-1][0][0]+segs[-1][1][0],segs[-1][0][1]+segs[-1][1][1])); return P
    U,D=side(1),side(-1)
    return [[U[k],U[k+1],D[k+1],D[k]] for k in range(n)],U,D
def FOLD():
    pts=[(-80,792),(905,418),(1072,-60)]
    quads,U,D=miter_quads(pts,56)
    o='<defs>'; i1,g1=metal(COP[1],-20); i2,g2=metal(COP[0],70); o+=g1+g2+'</defs>'
    for k,q in enumerate(quads):
        d='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in q)+'Z'
        a=math.degrees(math.atan2(pts[k+1][1]-pts[k][1],pts[k+1][0]-pts[k][0]))
        o+=f'<path d="{d}" fill="url(#{[i1,i2][k]})"/>'+brushedW(d,a,40+k,op=.3)
    o+=f'<line x1="{U[1][0]:.1f}" y1="{U[1][1]:.1f}" x2="{D[1][0]:.1f}" y2="{D[1][1]:.1f}" stroke="#fff" stroke-width=".9" opacity=".85"/>'
    # 折り目の影（裏面に落ちる薄い影）
    q=quads[1]; d='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in q)+'Z'
    o+=f'<defs><linearGradient id="fs" gradientUnits="userSpaceOnUse" x1="{pts[1][0]}" y1="{pts[1][1]}" x2="{pts[1][0]+40}" y2="{pts[1][1]-110}"><stop offset="0" stop-color="#000" stop-opacity=".35"/><stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient></defs><path d="{d}" fill="url(#fs)"/>'
    return o
def arcband(C,r,w,t0,t1,grad,seed,op=.86):
    P=lambda rr,t:(C[0]+rr*math.cos(math.radians(t)),C[1]+rr*math.sin(math.radians(t)))
    ro,ri=r+w/2,r-w/2; a,b,c,d=P(ro,t0),P(ro,t1),P(ri,t1),P(ri,t0)
    path=f'M{a[0]:.1f},{a[1]:.1f} A{ro},{ro} 0 0 1 {b[0]:.1f},{b[1]:.1f} L{c[0]:.1f},{c[1]:.1f} A{ri},{ri} 0 0 0 {d[0]:.1f},{d[1]:.1f}Z'
    UID[0]+=1; cid=f'ac{UID[0]}'; random.seed(seed)
    o=f'<path d="{path}" fill="url(#{grad})" opacity="{op}" style="mix-blend-mode:multiply"/><clipPath id="{cid}"><path d="{path}"/></clipPath><g clip-path="url(#{cid})">'
    rr=ri
    while rr<ro:   # 旋盤の挽き目のような同心の筋
        al=random.random()**2*.3; col='#fff' if random.random()<.55 else '#000'
        p1,p2=P(rr,t0),P(rr,t1)
        o+=f'<path d="M{p1[0]:.1f},{p1[1]:.1f} A{rr:.1f},{rr:.1f} 0 0 1 {p2[0]:.1f},{p2[1]:.1f}" fill="none" stroke="{col}" stroke-width="{random.choice((.35,.5,.7))}" opacity="{al:.3f}"/>'
        rr+=random.uniform(1.1,2.4)
    return o+'</g>'
def ARC():
    o='<defs>'; i1,g1=metal(COP[1],-30); i2,g2=metal(COP[0],-30); o+=g1+g2+'</defs>'
    o+=arcband((1000,1350),1000,40,200,290,i2,7,op=.9)
    o+=arcband((1300,1180),900,54,195,275,i1,8,op=.85)
    return o
ACC=COP[0][1]
S=[(spread(FOLD(),'JO',ACC,True),'A_FOLD_一枚の帯'),(spread(ARC(),'JO',ACC,True),'B_ARC_二つの弧')]
css=CSS2.replace('@page{size:210mm 297mm;margin:0}','@page{size:420mm 297mm;margin:0}')
open('cover17.html','w').write('<!doctype html><meta charset=utf-8><style>'+css+'</style>'+''.join(p for p,_ in S))
import json; json.dump([n for _,n in S],open('cover17_names.json','w'),ensure_ascii=False)
