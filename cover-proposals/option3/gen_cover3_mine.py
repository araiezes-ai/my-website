exec(open('c3b.py').read().split("# --- A:")[0])
def sliced(src,box,name,offs=(38,10,62,24,0,48,18),sq=(340,604),sat=1.0,con=1.08):
    im=Image.open(D+src).convert('RGB').crop(box)
    im=ImageEnhance.Contrast(ImageEnhance.Color(im).enhance(sat)).enhance(con)
    w0,h0=im.size; h=int(h0*595/w0); im=im.resize((595,h),Image.LANCZOS)
    top=max(0,(h-600)//2); im=im.crop((0,top,595,top+600))
    n=7; sw=595/n; inner=''
    for i in range(n):
        x=int(i*sw); w=int((i+1)*sw)-x
        inner+=f'<img src="{enc(im.crop((x,0,x+w,600)),92)}" style="position:absolute;left:{x}px;top:{offs[i]}px;width:{w-1}px;height:600px;display:block">'
    inner+=f'<div style="position:absolute;left:{sq[0]}px;top:{sq[1]}px;width:28px;height:28px;background:#C8102E"></div>'
    page(inner,name,title_y=668)
sliced('_mr_project_03.png',(380,0,1200,884),'c3m1')          # open-pit bowl
sliced('_mr_project_04.png',(150,0,970,884),'c3m2')            # terraced pit wall
sliced('mr_02_01@2x.webp',(500,0,1440,1428),'c3m3')            # pit + concentrator, wide context
