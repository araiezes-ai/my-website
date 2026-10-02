const pptxgen=require('pptxgenjs'); const fs=require('fs');
const d=JSON.parse(fs.readFileSync('layout2.json'));
const pres=new pptxgen();
const IN=v=>v/72;
pres.defineLayout({name:'A3L',width:IN(1190),height:IN(842)}); pres.layout='A3L';
pres.title='金属資源グループ 会社案内 台割 改善案';
const FONT='Yu Gothic';
pres.theme={headFontFace:FONT,bodyFontFace:FONT};
const names=['P02-03 導入（コアメッセージ・目次）','P04-05 第1章 WHO','P06-07 第2章 資産の強み・原料炭／銅','P08-09 第2章 トレーディング／事業一覧','P10-11 第3章 PROOF／第4章 VISION・締め'];
d.forEach((els,si)=>{
  const s=pres.addSlide();
  s.addNotes(names[si]+'（台割 改善案・構成確認用）');
  els.forEach((e,ei)=>{
    const x=IN(e.x),y=IN(e.y),w=IN(Math.max(e.w,0.5)),h=IN(Math.max(e.h,0.5));
    if(e.img){ s.addImage({data:e.img.data,x:IN(e.x),y:IN(e.y),w:IN(e.img.w),h:IN(e.img.h)}); return; }
    const hasBg=e.bg&&e.bg.a>0.02, full=e.bt>0&&e.bl>0&&e.bb>0&&e.br>0;
    const txt=e.runs.filter(r=>r.t!==undefined).map(r=>r.t).join('').trim();
    // single-side borders -> lines
    if(!full){
      if(e.bt>0) s.addShape(pres.shapes.LINE,{x,y,w:IN(e.w),h:0,line:{color:e.bcol.hex,width:e.bt,dashType:e.bstyle==='dashed'?'dash':'solid'}});
      if(e.bl>0&&!e.bt) s.addShape(pres.shapes.LINE,{x,y,w:0,h:IN(e.h),line:{color:e.blcol.hex,width:e.bl}});
    }
    const shapeOpt={};
    if(hasBg) {shapeOpt.fill={color:e.bg.hex,transparency:Math.round((1-e.bg.a)*100)};}
    if(full) shapeOpt.line={color:e.bcol.hex,width:e.bt,dashType:e.bstyle==='dashed'?'dash':'solid'};
    const round=e.rad>=Math.min(e.w,e.h)/2-0.5 && e.rad>0;
    const shp= round&&e.w===e.h? pres.shapes.OVAL : (e.rad>0? pres.shapes.ROUNDED_RECTANGLE: pres.shapes.RECTANGLE);
    if(!txt){
      if(hasBg||full) s.addShape(shp,{x,y,w,h,...shapeOpt,...(shp===pres.shapes.ROUNDED_RECTANGLE?{rectRadius:Math.min(0.5,IN(e.rad)/Math.min(w,h))}:{})});
      return;
    }
    const runs=[]; let cur=null;
    e.runs.forEach(r=>{
      if(r.br){ if(runs.length) runs[runs.length-1].options.breakLine=true; return; }
      runs.push({text:r.t,options:{fontSize:Math.max(r.fs,4),color:r.col?r.col.hex:'222222',bold:r.w>=500,charSpacing:r.ls||undefined}});
    });
    const lsp=e.lh? e.lh : e.fs*1.3;
    const opt={x,y:IN(e.y),w:IN(e.w*1.04+1),h:IN(Math.max(e.h,e.fs*1.4)),margin:0,valign:e.flex?'middle':'top',
      align:(e.align==='center'||(e.flex&&e.jc==='center'))?'center':(e.align==='right'?'right':'left'),
      fontFace:FONT,isTextBox:true,lineSpacing:lsp,fit:'none',wrap:!(e.h<=lsp*1.5 && !e.flex),objectName:'t'+si+'_'+ei,...shapeOpt};
    if(e.flex||hasBg||full){opt.w=w;}
    if(round||e.rad>0){opt.shape=e.rad>=e.h/2-0.5?pres.shapes.ROUNDED_RECTANGLE:pres.shapes.RECTANGLE; if(opt.shape===pres.shapes.ROUNDED_RECTANGLE) opt.rectRadius=0.5;}
    if(full||hasBg){opt.margin=[2,3,2,3];}
    if(e.bl>0&&!full){opt.margin=[0,0,0,8];}
    s.addText(runs,opt);
  });
  s.addShape(pres.shapes.LINE,{x:IN(595),y:0,w:0,h:IN(842),line:{color:'D5D8DB',width:0.75,dashType:'dash'}});
});
pres.writeFile({fileName:'daiwari_kaizen.pptx'}).then(f=>console.log('ok',f));
