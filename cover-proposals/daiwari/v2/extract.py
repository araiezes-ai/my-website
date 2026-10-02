import asyncio, json
from playwright.async_api import async_playwright
JS=r'''
() => {
 const out=[];
 const rgb=s=>{const m=s.match(/rgba?\(([^)]+)\)/); if(!m) return null; const p=m[1].split(',').map(x=>parseFloat(x)); return {hex:p.slice(0,3).map(v=>Math.round(v).toString(16).padStart(2,'0')).join(''), a:p.length>3?p[3]:1};};
 document.querySelectorAll('.sp').forEach((sp,si)=>{
   const r0=sp.getBoundingClientRect(); const els=[];
   sp.querySelectorAll(':scope > .a').forEach(el=>{
     const r=el.getBoundingClientRect(), cs=getComputedStyle(el);
     const img=el.querySelector('img');
     const runs=[]; let pend=false;
     const walk=(n)=>{
       if(n.nodeType===3){let t=n.textContent.replace(/[ \t\n\r]+/g,' '); if(!t.trim()&&!t.includes('　')) {if(t===' '&&runs.length) runs.push({t:' ',...st(n.parentElement)}); return;} if(pend&&runs.length){runs.push({br:1});} pend=false; runs.push({t,...st(n.parentElement)}); return;}
       if(n.nodeType!==1) return;
       if(n.tagName==='BR'){runs.push({br:1}); return;}
       if(n.tagName==='IMG') return;
       const blk=getComputedStyle(n).display==='block' && n!==el;
       if(blk&&runs.length) pend=true;
       n.childNodes.forEach(walk);
       if(blk) pend=true;
     };
     const st=(e)=>{const c=getComputedStyle(e); return {fs:parseFloat(c.fontSize), col:rgb(c.color), w:parseInt(c.fontWeight), ls:parseFloat(c.letterSpacing)||0};};
     walk(el);
     const bt=parseFloat(cs.borderTopWidth), bl=parseFloat(cs.borderLeftWidth), bb=parseFloat(cs.borderBottomWidth), br=parseFloat(cs.borderRightWidth);
     els.push({x:r.left-r0.left,y:r.top-r0.top,w:r.width,h:r.height,
       bg:rgb(cs.backgroundColor), bt,bl,bb,br, bcol:rgb(cs.borderTopColor), blcol:rgb(cs.borderLeftColor), bstyle:cs.borderTopStyle,
       rad:parseFloat(cs.borderTopLeftRadius)||0, align:cs.textAlign, flex:cs.display==='flex', jc:cs.justifyContent,
       lh:parseFloat(cs.lineHeight)||0, fs:parseFloat(cs.fontSize),
       img: img? {src:img.src, fit:getComputedStyle(img).objectFit, w:img.getBoundingClientRect().width, h:img.getBoundingClientRect().height}:null,
       runs});
   });
   out.push(els);
 });
 return out;
}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1300,'height':900})
        import os
        await pg.goto('file://'+os.path.abspath('daiwari_v2.html'))
        await pg.add_style_tag(content='.sp{zoom:1 !important}')
        await pg.wait_for_timeout(2500)
        data=await pg.evaluate(JS)
        json.dump(data,open('layout.json','w'))
        print([len(s) for s in data])
        await b.close()
asyncio.run(main())
