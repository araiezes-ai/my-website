const pptxgen=require('pptxgenjs'); const fs=require('fs');
const [,,LAY,OUT,MODE]=process.argv;
const d=JSON.parse(fs.readFileSync(LAY));
const p=new pptxgen(); const SW=16.535, SH=11.693, K=SW/1190;
p.defineLayout({name:'A3L',width:SW,height:SH}); p.layout='A3L';
const hex=c=>{const m=c.match(/[\d.]+/g); if(!m) return '000000'; return m.slice(0,3).map(v=>(+v|0).toString(16).padStart(2,'0')).join('').toUpperCase();};
const alpha=c=>{const m=c.match(/[\d.]+/g); return m&&m.length>3?+m[3]:1;};
const cjk=t=>/[　-鿿＀-￯]/.test(t);
const face=(r)=>{const w=+r.fw; const jp=cjk(r.t)||/Noto Sans JP/.test(r.ff.split(',')[0]);
  if(jp) return w>=500?'Noto Sans JP Medium':(w<=300?'Noto Sans JP Light':'Noto Sans JP');
  return w<=200?'Noto Sans ExtraLight':w<=300?'Noto Sans Light':w>=500?'Noto Sans Medium':'Noto Sans';};
d.slides.forEach((items,i)=>{
  const s=p.addSlide();
  s.background={path:d.bgs[i]};
  if(MODE==='image') return;
  items.forEach(it=>{
    const runs=[];
    it.runs.forEach((r,k)=>{
      if(r.br){ if(runs.length) runs[runs.length-1].options.breakLine=true; return;}
      const ls=parseFloat(r.ls)||0;
      runs.push({text:r.t,options:{fontFace:face(r),fontSize:r.fs,color:hex(r.c),transparency:Math.round((1-alpha(r.c))*100),charSpacing:ls?ls:undefined}});
    });
    if(!runs.length) return;
    const lh=it.lh; const pad=(lh-it.ch)/2;
    const al=it.align==='center'?'center':(it.align==='right'||it.align==='end')?'right':'left';
    let w=it.w*1.10+4, x=it.x;
    if(al==='center') x=it.x-(w-it.w)/2; else if(al==='right') x=it.x-(w-it.w);
    s.addText(runs,{x:x*K,y:(it.y-pad)*K,w:w*K,h:(it.lines*lh)*K,margin:0,valign:'top',align:al,wrap:false,lineSpacing:lh,paraSpaceBefore:0,paraSpaceAfter:0,fit:'none'});
  });
});
p.writeFile({fileName:OUT}).then(f=>console.log('ok',f));
