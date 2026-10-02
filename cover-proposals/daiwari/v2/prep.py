import json, base64, io
from PIL import Image
d=json.load(open('layout.json'))
for sl in d:
    for e in sl:
        im=e.get('img')
        if not im: continue
        raw=base64.b64decode(im['src'].split(',',1)[1]); pic=Image.open(io.BytesIO(raw)).convert('RGB')
        W,H=max(1,round(im['w']*3)),max(1,round(im['h']*3))
        if im['fit']=='contain':
            pic.thumbnail((W,H)); can=Image.new('RGB',(W,H),'white'); can.paste(pic,((W-pic.width)//2,(H-pic.height)//2)); pic=can
        else:
            r=max(W/pic.width,H/pic.height); pic=pic.resize((max(W,int(pic.width*r)+1),max(H,int(pic.height*r)+1)))
            l=(pic.width-W)//2; t=(pic.height-H)//2; pic=pic.crop((l,t,l+W,t+H))
        bf=io.BytesIO(); pic.save(bf,'JPEG',quality=85)
        im['data']='image/jpeg;base64,'+base64.b64encode(bf.getvalue()).decode(); del im['src']
json.dump(d,open('layout2.json','w'))
