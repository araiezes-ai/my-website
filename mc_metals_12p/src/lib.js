// 描画ライブラリ：見開き座標(mm)で描き、A4スライド(左右)またはA3スライドへ振り分ける
const {execSync}=require('child_process'); const fs=require('fs'); const path=require('path');
const IN=v=>v/25.4;
const C={INK:'121519',G1:'3D4249',G2:'7D838A',G3:'CFD3D7',G4:'ECEDEE',G5:'E3E6E9',PAN:'F5F4F1',BR:'9C7442',BRL:'C9AD82',NV:'1F3A56',NVL:'9FB1C3',RED:'C8102E',CU:'A8622F',CUL:'E9D3C2',ST:'6E7A87',STD:'4A535D',W:'FFFFFF',OUT:'D9DDE1'};
const F={JP:'Noto Sans JP',EN:'Inter Tight',ENL:'Inter Tight Light',IN:'Inter'};
const SRC=__dirname, ASSET=path.join(SRC,'assets'), CACHE=path.join(SRC,'assets','_crop');
fs.mkdirSync(CACHE,{recursive:true});
const WARN=[];
class D {
  // tg: [{s:slide, ox:offset, lo, hi}]
  constructor(pptx,tg,name){this.p=pptx;this.tg=tg;this.name=name;}
  _route(x,w,kind,label){
    const hit=this.tg.filter(t=>x<t.hi-0.01 && x+w>t.lo+0.01);
    if(kind==='text' && hit.length>1){WARN.push(`${this.name}: text crosses gutter: "${String(label).slice(0,30)}"`);return [hit[0]];}
    return hit;
  }
  rect(x,y,w,h,o={}){ for(const t of this._route(x,w,'shape')) t.s.addShape(o.r?this.p.ShapeType.roundRect:this.p.ShapeType.rect,{x:IN(x-t.ox),y:IN(y),w:IN(w),h:IN(h),rectRadius:o.r?IN(o.r):undefined,rotate:o.rot||0,fill:o.fill?{color:o.fill,transparency:o.tr||0}:{type:'none'},line:o.line?{color:o.line,width:o.lw||0.75,dashType:o.dash||'solid'}:{type:'none'}}); return this;}
  ell(cx,cy,rx,ry,o={}){ry=ry||rx; for(const t of this._route(cx-rx,2*rx,'shape')) t.s.addShape(this.p.ShapeType.ellipse,{x:IN(cx-rx-t.ox),y:IN(cy-ry),w:IN(2*rx),h:IN(2*ry),fill:o.fill?{color:o.fill,transparency:o.tr||0}:{type:'none'},line:o.line?{color:o.line,width:o.lw||0.75,dashType:o.dash||'solid'}:{type:'none'}}); return this;}
  arc(cx,cy,r,a0,a1,th,o={}){ // ドーナツの扇形（角度：0=3時、時計回り）
    for(const t of this._route(cx-r,2*r,'shape')) t.s.addShape(this.p.ShapeType.blockArc,{x:IN(cx-r-t.ox),y:IN(cy-r),w:IN(2*r),h:IN(2*r),angleRange:[a0,a1],arcThicknessRatio:th,fill:o.fill?{color:o.fill,transparency:o.tr||0}:{type:'none'},line:o.line?{color:o.line,width:o.lw||0.75}:{type:'none'}});return this;}
  line(x1,y1,x2,y2,o={}){
    let beg=o.beg, end=o.end; if(x2<x1){[x1,y1,x2,y2]=[x2,y2,x1,y1];[beg,end]=[end,beg];}
    const flipV=y2<y1; const x=x1,y=Math.min(y1,y2),w=Math.max(x2-x1,0.001),h=Math.max(Math.abs(y2-y1),0.001);
    for(const t of this._route(x,w,'shape')) t.s.addShape(this.p.ShapeType.line,{x:IN(x-t.ox),y:IN(y),w:IN(w),h:IN(h),flipV,line:{color:o.c||C.INK,width:o.w||0.75,dashType:o.dash||'solid',beginArrowType:beg,endArrowType:end,transparency:o.tr||0}});
    return this;}
  // pts: [[x,y],...] 多角形 / segs: パス（{c:[x1,y1,x2,y2,x,y]}で3次ベジェ）
  path(pts,o={}){
    const xs=[],ys=[]; pts.forEach(p=>{const a=Array.isArray(p)?p:p.c; for(let i=0;i<a.length;i+=2){xs.push(a[i]);ys.push(a[i+1]);}});
    const minx=Math.min(...xs),miny=Math.min(...ys),maxx=Math.max(...xs),maxy=Math.max(...ys);
    for(const t of this._route(minx,maxx-minx,'shape')){
      const P=[]; pts.forEach((p,i)=>{ if(Array.isArray(p)) P.push(i===0?{x:IN(p[0]-minx),y:IN(p[1]-miny),moveTo:true}:{x:IN(p[0]-minx),y:IN(p[1]-miny)});
        else P.push({x:IN(p.c[4]-minx),y:IN(p.c[5]-miny),curve:{type:'cubic',x1:IN(p.c[0]-minx),y1:IN(p.c[1]-miny),x2:IN(p.c[2]-minx),y2:IN(p.c[3]-miny)}}); });
      if(o.close) P.push({close:true});
      t.s.addShape(this.p.ShapeType.custGeom,{x:IN(minx-t.ox),y:IN(miny),w:IN(Math.max(maxx-minx,0.01)),h:IN(Math.max(maxy-miny,0.01)),points:P,
        fill:o.fill?{color:o.fill,transparency:o.tr||0}:{type:'none'},line:o.line?{color:o.line,width:o.lw||0.75,dashType:o.dash||'solid',endArrowType:o.end,beginArrowType:o.beg}:{type:'none'}});
    } return this;}
  text(x,y,w,h,txt,o={}){
    const base={fontFace:o.f||F.JP,fontSize:o.s||8,color:o.c||C.G1,bold:!!o.b,align:o.al||'left',valign:o.va||'top',margin:0,
      lineSpacingMultiple:o.ls||(o.f&&o.f!==F.JP?1.0:1.45),charSpacing:o.cs||0,fit:'none',wrap:o.wrap===false?false:true,paraSpaceAfter:0};
    if(o.outline){base.outline={size:o.outline,color:o.oc||C.OUT};}
    const runs=Array.isArray(txt)?txt.map(r=>typeof r==='string'?{text:r,options:{}}:{text:r.t,options:{fontFace:r.f,fontSize:r.s,color:r.c,bold:r.b,breakLine:r.br,charSpacing:r.cs}}):txt;
    for(const t of this._route(x,w,'text',Array.isArray(txt)?txt.map(r=>r.t||r).join(''):txt)) t.s.addText(runs,{...base,x:IN(x-t.ox),y:IN(y),w:IN(w),h:IN(h)});
    return this;}
  img(file,x,y,w,h,fx=.5,fy=.5){
    const out=path.join(CACHE,`${path.parse(file).name}_${w.toFixed(1)}x${h.toFixed(1)}_${fx}_${fy}.jpg`);
    if(!fs.existsSync(out)) execSync(`python3 -I "${path.join(SRC,'crop.py')}" "${path.join(ASSET,file)}" "${out}" ${w} ${h} ${fx} ${fy}`);
    for(const t of this._route(x,w,'shape')) t.s.addImage({path:out,x:IN(x-t.ox),y:IN(y),w:IN(w),h:IN(h)});
    return this;}
}
// テキスト部品
const K=(d,x,y,en,jp,col=C.BR,w=120)=>{d.text(x,y,w,4,[{t:en,f:F.IN,s:6.5,b:true,c:col,cs:1.6},{t:jp?'　'+jp:'',f:F.JP,s:6.5,c:C.G2}],{ls:1});};
const H=(d,x,y,w,txt,s=40,o={})=>d.text(x,y,w,s*0.36*(txt.split('\n').length)+4,txt,{f:o.light?F.ENL:F.EN,b:!o.light,s,c:o.c||C.INK,ls:0.92,cs:o.cs||-0.6});
const LEAD=(d,x,y,w,txt,s=10.5)=>{d.rect(x,y,7,0.5,{fill:C.RED});d.text(x,y+3,w,s*0.36*1.6*Math.ceil(txt.length*s*0.353/w)+2,txt,{s,b:true,c:C.INK,ls:1.35});};
const BODY=(d,x,y,w,h,txt,s=7.8,o={})=>d.text(x,y,w,h,txt,{s,c:o.c||C.G1,ls:o.ls||1.65,al:o.al||'justify'});
const FOLIO=(d,n,side,ox=0)=>{ if(side==='L') d.text(ox+14,287,20,4,String(n).padStart(2,'0'),{f:F.IN,s:6.5,c:C.G2,cs:1.5}); else d.text(ox+176,287,20,4,String(n).padStart(2,'0'),{f:F.IN,s:6.5,c:C.G2,cs:1.5,al:'right'}); };
const BIGNUM=(d,x,y,t,s=190)=>d.text(x,y,s*0.42,s*0.38,t,{f:F.ENL,s,c:C.W,outline:0.6,ls:0.8,cs:-6});
const CAP=(d,x,y,w,t,dark=true)=>d.text(x,y,w,4,t,{f:F.JP,s:5.8,c:dark?C.W:C.G2,b:true,ls:1});
// 帯（中心線のオフセット多角形）
function offsetPoly(pts,s){const segs=[];for(let k=0;k<pts.length-1;k++){const [x0,y0]=pts[k],[x1,y1]=pts[k+1];const L=Math.hypot(x1-x0,y1-y0);const nx=-(y1-y0)/L*s,ny=(x1-x0)/L*s;segs.push([[x0+nx,y0+ny],[x1-x0,y1-y0]]);}
  const isect=(a,da,b,db)=>{const den=da[0]*db[1]-da[1]*db[0];const t=((b[0]-a[0])*db[1]-(b[1]-a[1])*db[0])/den;return [a[0]+t*da[0],a[1]+t*da[1]];};
  const P=[segs[0][0]];for(let k=0;k<segs.length-1;k++)P.push(isect(segs[k][0],segs[k][1],segs[k+1][0],segs[k+1][1]));const l=segs[segs.length-1];P.push([l[0][0]+l[1][0],l[0][1]+l[1][1]]);return P;}
function bandPoly(pts,w){const U=offsetPoly(pts,w/2),Dn=offsetPoly(pts,-w/2);return U.concat(Dn.reverse());}
module.exports={D,C,F,IN,K,H,LEAD,BODY,FOLIO,BIGNUM,CAP,bandPoly,offsetPoly,WARN};
// リング扇形（角度°：0=3時、時計回り）
function segPts(cx,cy,r0,r1,a0,a1,n=40){const P=[];for(let i=0;i<=n;i++){const a=(a0+(a1-a0)*i/n)*Math.PI/180;P.push([cx+r1*Math.cos(a),cy+r1*Math.sin(a)]);}
  for(let i=n;i>=0;i--){const a=(a0+(a1-a0)*i/n)*Math.PI/180;P.push([cx+r0*Math.cos(a),cy+r0*Math.sin(a)]);}return P;}
function arcPts(cx,cy,r,a0,a1,n=40){const P=[];for(let i=0;i<=n;i++){const a=(a0+(a1-a0)*i/n)*Math.PI/180;P.push([cx+r*Math.cos(a),cy+r*Math.sin(a)]);}return P;}
module.exports.segPts=segPts; module.exports.arcPts=arcPts;
