import asyncio, json, os, base64, sys
from playwright.async_api import async_playwright
HTML=sys.argv[1]; OUT=sys.argv[2]
JS=r'''
() => {
 const out=[];
 const isBlock=el=>{const d=getComputedStyle(el).display; return !(d==='inline'||d==='inline-block'&&false)};
 document.querySelectorAll('.sp').forEach(sp=>{
  const r0=sp.getBoundingClientRect(); const items=[];
  const blocks=[];
  sp.querySelectorAll('*').forEach(el=>{
    if(el.closest('svg')||el.tagName==='IMG'||el.classList.contains('big')) return;
    if(getComputedStyle(el).display==='inline') return;
    // has direct text or inline children with text
    let has=false;
    el.childNodes.forEach(n=>{ if(n.nodeType===3&&n.textContent.trim()) has=true;
      if(n.nodeType===1&&getComputedStyle(n).display==='inline'&&n.textContent.trim()) has=true;});
    if(has) blocks.push(el);
  });
  blocks.forEach(el=>{
    const runs=[]; let lastTop=null, prevRight=-1e9; let x0=1e9,y0=1e9,x1=-1e9,y1=-1e9, ch=0;
    const rg=document.createRange();
    const walk=(node)=>{
      node.childNodes.forEach(n=>{
        if(n.nodeType===3){
          const cs=getComputedStyle(n.parentElement);
          const st={fs:parseFloat(cs.fontSize),fw:cs.fontWeight,c:cs.color,ls:cs.letterSpacing,ff:cs.fontFamily};
          const txt=n.textContent; let cur='';
          for(let i=0;i<txt.length;i++){
            rg.setStart(n,i); rg.setEnd(n,i+1);
            const rs=rg.getClientRects(); if(!rs.length){continue;}
            const q=rs[0];
            if(/[ \t\n\r]/.test(txt[i])&&q.width<0.01) continue;
            const nl=(lastTop!==null && q.left<prevRight-3 && q.top>lastTop+2);
            if(nl){ if(cur) runs.push(Object.assign({t:cur},st)); cur=''; runs.push({br:1}); }
            if(lastTop===null||nl) lastTop=q.top;
            prevRight=q.right;
            if(q.width>0.01){x0=Math.min(x0,q.left);y0=Math.min(y0,q.top);x1=Math.max(x1,q.right);y1=Math.max(y1,q.bottom); ch=Math.max(ch,q.height);}
            cur+=txt[i];
          }
          if(cur) runs.push(Object.assign({t:cur},st));
        } else if(n.nodeType===1){
          if(n.tagName==='BR'){return;}
          if(getComputedStyle(n).display==='inline') walk(n);
        }
      });
    };
    walk(el);
    // clean whitespace
    const rr=[]; runs.forEach(r=>{ if(r.br){ if(rr.length&&!rr[rr.length-1].br) rr.push(r); return;} r.t=r.t.replace(/[ \t\n\r]+/g,' '); if(!rr.length||rr[rr.length-1].br) r.t=r.t.replace(/^ /,''); if(r.t) rr.push(r);});
    while(rr.length&&rr[rr.length-1].br) rr.pop();
    if(!rr.length) return;
    if(x1<0) return;
    const cs=getComputedStyle(el);
    const nl=rr.filter(r=>r.br).length+1;
    const lh=cs.lineHeight==='normal'?ch:parseFloat(cs.lineHeight);
    items.push({x:x0-r0.left,y:y0-r0.top,w:x1-x0,h:y1-y0,ch:ch,lh:lh,lines:nl,align:cs.textAlign,runs:rr});
  });
  out.push(items);
 });
 return out;
}
'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1190,'height':842},device_scale_factor=2.6)
        await pg.goto('file://'+os.path.abspath(HTML))
        await pg.add_style_tag(content='.sp{zoom:1 !important;margin:0} body{margin:0}')
        await pg.wait_for_timeout(3000)
        data=await pg.evaluate(JS)
        await pg.add_style_tag(content='.sp *:not(.big){color:transparent !important;text-shadow:none !important} .sp > div[style*="border-left:.5px dashed"]{display:none !important}')
        await pg.wait_for_timeout(500)
        sps=await pg.query_selector_all('.sp')
        bgs=[]
        for i,s in enumerate(sps):
            f=f'pptx9/bg{i+1}.jpg'; await s.screenshot(path=f,type='jpeg',quality=90); bgs.append(f)
        json.dump({'slides':data,'bgs':bgs},open(OUT,'w'),ensure_ascii=False)
        print([len(s) for s in data])
        await b.close()
asyncio.run(main())
