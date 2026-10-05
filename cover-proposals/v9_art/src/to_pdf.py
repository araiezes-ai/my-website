import sys
from playwright.sync_api import sync_playwright
src,out,n=sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 0
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg=b.new_page(viewport={'width':1587,'height':1123},device_scale_factor=1)
    pg.goto('file://'+src); pg.wait_for_timeout(500)
    pg.pdf(path=out+'.pdf',width='420mm',height='297mm',print_background=True)
    b.close()
import pymupdf
d=pymupdf.open(out+'.pdf')
for i,pp in enumerate(d):
    pp.get_pixmap(dpi=int(sys.argv[4]) if len(sys.argv)>4 else 60).save(f'{out}_{i+1}.png')
print(len(d),'pages')
