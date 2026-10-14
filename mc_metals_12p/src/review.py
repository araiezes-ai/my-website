# A3横の見開き俯瞰版（P1単独／5見開き／P12単独＝7ビュー）と、12P台割ストーリーボードを生成
import glob, os, subprocess
from PIL import Image, ImageDraw, ImageFont
R=os.path.join(os.path.dirname(__file__),'_render'); D=os.path.join(os.path.dirname(__file__),'..','deliverables')
pg=[Image.open(f).convert('RGB') for f in sorted(glob.glob(R+'/p-*.png'))]; w,h=pg[0].size
font=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',int(h*0.016))
def sheet(left,right,label):
    S=Image.new('RGB',(w*2,h),'white'); d=ImageDraw.Draw(S)
    if left is not None: S.paste(left,(0,0))
    else: d.rectangle((0,0,w,h),fill='#eceeef')
    if right is not None: S.paste(right,(w,0))
    else: d.rectangle((w,0,2*w,h),fill='#eceeef')
    d.line((w,0,w,h),fill='#c9ced3',width=2)
    d.text((int(w*0.02),int(h*0.965)),label,fill='#7d838a',font=font)
    return S
views=[sheet(None,pg[0],'P1 表紙（単独ページ）')]
for a,b,t in [(1,2,'P2–3 Core Message & Contents'),(3,4,'P4–5 Who We Are'),(5,6,'P6–7 Our Distinctive Strength'),(7,8,'P8–9 Our Businesses & Innovation'),(9,10,'P10–11 Partner of Choice ／ Supporting Society')]:
    views.append(sheet(pg[a],pg[b],t))
views.append(sheet(pg[11],None,'P12 裏表紙（単独ページ）'))
views[0].save(D+'/MC_Metals_Spread_Review.pdf',save_all=True,append_images=views[1:],resolution=w/ (210/25.4))
print('review',len(views))
