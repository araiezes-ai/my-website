import asyncio, json, os, base64
from playwright.async_api import async_playwright
JS=open('extract.py').read().split("JS=r'''")[1].split("'''")[0]
JS=JS.replace("els.push({x:r.left-r0.left","els.push({svg:el.tagName.toLowerCase()==='svg',x:r.left-r0.left")
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1300,'height':900},device_scale_factor=3)
        await pg.goto('file://'+os.path.abspath('daiwari_v4.html'))
        await pg.add_style_tag(content='.sp{zoom:1 !important}')
        await pg.wait_for_timeout(2500)
        data=await pg.evaluate(JS)
        await pg.add_style_tag(content='.sp > .a:not(svg){visibility:hidden !important} .sp{background:transparent !important} .sp:after{display:none} body{background:transparent !important}')
        svgs=await pg.query_selector_all('.sp > svg.a')
        shots=[]
        for s in svgs:
            shots.append(base64.b64encode(await s.screenshot(omit_background=True)).decode())
        k=0
        for sl in data:
            for e in sl:
                if e.get('svg'):
                    e['img']={'data':'image/png;base64,'+shots[k],'w':e['w'],'h':e['h'],'fit':'fill','png':True}; k+=1
        print(len(shots),k)
        json.dump(data,open('layout.json','w'))
        await b.close()
asyncio.run(main())
