// MC_Metals_12P_JP_Editable.pptx（A4縦12枚）と MC_Metals_Design_Alternatives.pptx（A3横）を生成
const pptxgen=require('pptxgenjs'); const path=require('path'); const Lb=require('./lib'); const P=require('./pages');
const OUT=path.join(__dirname,'..','deliverables');
async function main(){
  const p=new pptxgen(); p.defineLayout({name:'A4P',width:8.268,height:11.693}); p.layout='A4P'; p.title='三菱商事 金属資源グループ 会社案内 12P';
  const S=[]; for(let i=0;i<12;i++){const s=p.addSlide(); s.background={color:'FFFFFF'}; S.push(s);}
  const pg=(i)=>({s:S[i],ox:0,lo:0,hi:210});
  const sp=(i,name)=>new Lb.D(p,[{s:S[i],ox:0,lo:0,hi:210},{s:S[i+1],ox:210,lo:210,hi:420}],name);
  P.cover(new Lb.D(p,[pg(0)],'P01'),0,'A');
  P.sp23(sp(1,'P02-03')); P.sp45A(sp(3,'P04-05')); P.sp67A(sp(5,'P06-07')); P.sp89(sp(7,'P08-09')); P.sp1011(sp(9,'P10-11'));
  P.back(new Lb.D(p,[pg(11)],'P12'),0);
  const notes=['P01 Cover','P02 Introduction','P03 Core Message & Contents','P04 Who We Are｜三菱商事とは','P05 Who We Are｜金属資源グループとは','P06 Our Distinctive Strength','P07 Our Distinctive Strength','P08 Our Businesses & Innovation','P09 Our Businesses & Innovation','P10 Partner of Choice','P11 Supporting Society','P12 Back Cover'];
  S.forEach((s,i)=>s.addNotes(notes[i]+'｜詳細は content_and_factcheck.md'));
  await p.writeFile({fileName:path.join(OUT,'MC_Metals_12P_JP_Editable.pptx')});
  // 比較案（A3横・ネイティブ図形）
  const a=new pptxgen(); a.defineLayout({name:'A3L',width:16.535,height:11.693}); a.layout='A3L';
  const add=(fn,label,arg)=>{const s=a.addSlide(); const d=new Lb.D(a,[{s,ox:0,lo:0,hi:420}],label); fn(d,arg);
    s.addText(label,{x:0.15,y:11.35,w:8,h:0.25,fontFace:'Noto Sans JP',fontSize:8,color:'9AA0A6',margin:0}); return s;};
  add((d)=>{P.cover(d,0,'A'); P.cover(d,210,'B'); d.rect(209.8,0,0.4,297,{fill:'D5DADE'});},'表紙 比較｜左：案A 3本のライン（前へ進み、一点で上へ）／右：案B 3本の帯が交差して上へ抜ける');
  add(P.sp45A,'P4–5 案A｜企業全体から対象グループへ線がつながる構成（本体採用）');
  add(P.sp45B,'P4–5 案B｜総合力の構造図にミッションと歩みを重ねる構成');
  add(P.sp67A,'P6–7 案A｜バリューチェーン横軸＋投資／販売の2本のライン＋市場情報の戻り（本体採用）');
  add(P.sp67B,'P6–7 案B｜価値循環のループ＋各事業への接続');
  await a.writeFile({fileName:path.join(OUT,'MC_Metals_Design_Alternatives.pptx')});
  if(Lb.WARN.length) console.log('WARN\n'+Lb.WARN.join('\n')); console.log('built');
}
main();
