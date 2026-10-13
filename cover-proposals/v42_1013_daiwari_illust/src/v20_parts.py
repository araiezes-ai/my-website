# 台割 v19（10/13 PwC FB反映）— 案②（帯・アウトライン数字）のデザインで、全12P構成に再編
exec(open('v19_head.py').read())
import math
CU='#a8622f'   # 銅（金属資源グループのハイライト）
def kick(x,y,en,jp,col=BR): return T(x,y,en,None,'k',f'color:{col}')+T(x,y+11,jp,None,'kj')
def lead(x,y,t,w=None,size=11.5): return A(x,y,'',22,'',f'border-top:1.4px solid {RED}')+T(x,y+10,t,w,'h',f'font-size:{size}px')
def arrow(x1,y1,x2,y2,col=INK,sw=.8):
    a=math.atan2(y2-y1,x2-x1); h=4
    p1=(x2-h*math.cos(a-.5),y2-h*math.sin(a-.5)); p2=(x2-h*math.cos(a+.5),y2-h*math.sin(a+.5))
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{sw}"/><path d="M{p1[0]:.1f},{p1[1]:.1f} L{x2},{y2} L{p2[0]:.1f},{p2[1]:.1f}" fill="none" stroke="{col}" stroke-width="{sw}"/>'
def chev(cx,y,w=34,col=RED): return f'<path d="M{cx-w/2},{y} L{cx},{y+9} L{cx+w/2},{y}" fill="none" stroke="{col}" stroke-width="1.2"/>'
def badge(x,y,t,col=BR,d=16): return A(x,y,f'<div style="font-family:IT;font-weight:600;font-size:{d*.55}px;color:#fff">{t}</div>',d,'',f'height:{d}px;border-radius:50%;background:{col};display:flex;align-items:center;justify-content:center')
def msq(x,y,w,rows):
    o=''
    for i,(k_,v,d_) in enumerate(rows):
        yy=y+i*34; o+=rule(x,yy,w,INK if i==0 else G3,1 if i==0 else .6)
        o+=T(x,yy+7,k_,None,'l','font-size:5.8px;letter-spacing:1.4px;color:'+G2)+T(x+58,yy+5,v,w-58,'hs','font-size:9px;font-weight:700')+T(x+58,yy+19,d_,w-58,'s','font-size:6.2px')
    return o

#P23
  CORE MESSAGE / CONTENTS =================
b=tile(0,0,330,250,'r-022.png','50% 60%','都市','鉄・銅・アルミ')
b+=tile(334,0,261,123,'x_vc_ev.jpg','50% 55%','モビリティ','鉄・銅・リチウム')
b+=ptile(334,127,261,123,'鉄道','鉄・銅','鉄道の写真（ストック）')
b+=tile(0,254,163,146,'x_vc_wind.jpg','50% 30%','再生可能エネルギー','銅・鉄')
b+=tile(167,254,163,146,'x_case_pylon.jpg','50% 50%','送電網','銅・アルミ')
b+=ptile(334,254,261,146,'デバイス','銅・リチウム・ニッケル','スマートフォン・データセンターの写真（ストック）')
b+=tile(599,0,330,264,'mr_03_01@2x.webp','50% 50%','金属素材','暮らしを形づくる鉄・銅・アルミ',2000)
b+=tile(933,0,257,264,'x_vc_smelter.jpg','50% 50%','製錬・精製','')
b+=tile(599,268,257,132,'r-023.png','50% 60%','海上輸送','')
b+=tile(860,268,330,132,'r-054.png','50% 55%','銅地金','')
b+=kick(L,438,'コアメッセージ','私たちの存在意義')
b+=T(L,466,'Strength to Hold.<br>Power to Connect.',W,'dl','font-size:46px')
b+=lead(L,570,'持つ力と、つなぐ力。',None,15)
b+=para(L,604,300,'資源は、そこに「ある」だけでは、まだ価値ではありません。誰かが見出し、育て、必要とする場所へ届けて、はじめて力になる。私たちは、世界有数の資産に関わり、投資とトレーディングの両輪で川上から川下までをつなぎます。フェアな立場だからこそ、埋められる隙間がある。多様なパートナーと使い手の間に立ち、その時々の最適解を導く。世界に眠る価値を、社会の力へ。')
b+=kick(R,438,'目次','Contents')
toc=[('01','我々は何者か','三菱商事とは／金属資源グループとは','04'),('02','独自価値','投資とトレーディングの両輪／原料炭・銅・トレーディング・新技術','06'),('03','選ばれ続ける理由','Partner of Choice','10'),('04','何を実現するか','社会課題への取り組み','11')]
for i,(n,e,j,p) in enumerate(toc):
    y=466+i*72
    b+=rule(R,y,W,INK if i==0 else G3,1 if i==0 else .6)+T(R,y+10,n,None,'n','font-size:40px;color:'+BR)+T(R+84,y+14,e,None,'h','font-size:14px')+T(R+84,y+36,j,320,'s','font-size:7.2px')+T(R+W-34,y+16,'P.'+p,None,'fo')
b+=BAND(0,824,1190,18)
pages.append(spread(b,2,3,'',''))

