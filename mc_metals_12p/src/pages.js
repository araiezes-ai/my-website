// 各ページ／見開きのデザイン（座標はmm。見開きは0–420、ノド=210）
const {C,F,K,H,LEAD,BODY,FOLIO,BIGNUM,CAP,bandPoly,segPts,arcPts}=require('./lib');
const L=14, R=222, W=184, NODO=210;
const chip=(d,x,y,w,h,t,o={})=>{d.rect(x,y,w,h,{fill:o.fill||C.W,line:o.line||C.G3,lw:o.lw||0.6,r:o.r===undefined?h/2:o.r});d.text(x,y+(h-3.2)/2-0.2,w,h,t,{s:o.s||7,c:o.c||C.INK,b:o.b!==false,al:'center',ls:1});};
const dot=(d,x,y,r,col)=>d.ell(x,y,r,r,{fill:col,line:C.W,lw:0.8});
const badge=(d,x,y,t,col,r=3.2)=>{d.ell(x,y,r,r,{fill:col});d.text(x-r,y-2,2*r,4,t,{f:F.IN,s:6.5,b:true,c:C.W,al:'center',ls:1});};

// ---------------- COVER ----------------
function cover(d,dx=0,variant='A'){
  const X=v=>v+dx;
  d.rect(X(0),0,210,297,{fill:C.W});
  if(variant==='A'){ // 3本のライン：前へ進み、一点で上へ
    const cl=[[-6,238.6],[88.2,238.6],[197.6,49.4],[225.9,0.3]];
    const offs=[-14.8,0,14.8], cols=[C.CU,C.ST,C.STD];
    offs.forEach((o,k)=>{const P=require('./lib').offsetPoly(cl,o);d.path(bandPoly(P.map(p=>[X(p[0]),p[1]]),7.1),{fill:cols[k],close:true});
      d.path(P.map(p=>[X(p[0]),p[1]-1.2]),{line:C.W,lw:0.4});});
  } else { // 3本の帯が交差して上へ抜ける（赤）
    const band=(p0,p1,w,col,tr)=>{const dxv=p1[0]-p0[0],dyv=p1[1]-p0[1],Ln=Math.hypot(dxv,dyv),nx=-dyv/Ln*w/2,ny=dxv/Ln*w/2;
      d.path([[X(p0[0]+nx),p0[1]+ny],[X(p1[0]+nx),p1[1]+ny],[X(p1[0]-nx),p1[1]-ny],[X(p0[0]-nx),p0[1]-ny]],{fill:col,tr,close:true});};
    band([-20,262],[240,198],32,C.G1,25); band([-20,226],[240,138],25,'A3122A',15); band([106,300],[240,116],34,'7D1424',20);
    d.rect(X(0),266,210,31,{fill:C.W});
  }
  d.text(X(17),24,150,5,'MITSUBISHI CORPORATION',{f:F.IN,s:10,c:C.INK,cs:3.5,ls:1});
  d.rect(X(17),33,12,0.6,{fill:C.RED});
  d.text(X(17),39,170,40,'METAL\nRESOURCES\nGROUP',{f:F.ENL,s:30,c:C.INK,cs:3,ls:0.98});
  d.text(X(17),78,170,6,'CORPORATE PROFILE',{f:F.IN,s:9,c:C.G2,cs:3.2,ls:1});
  d.text(X(17),86,170,6,'Strength to Hold. Power to Connect.',{f:F.ENL,s:10,c:C.G1,ls:1});
  d.rect(X(17),272,176,0.25,{fill:C.G3});
  d.text(X(17),277,176,5,'Mitsubishi Corporation',{f:F.IN,s:8,c:C.INK,al:'center',cs:1.2,ls:1});
}
function back(d,dx=0){
  const X=v=>v+dx; d.rect(X(0),0,210,297,{fill:C.W});
  [-14.8,0,14.8].forEach((o,k)=>{const y=238.6+o; d.rect(X(0),y-3.55,210,7.1,{fill:[C.CU,C.ST,C.STD][k]}); d.rect(X(0),y-3.55+1.2,210,0.15,{fill:C.W,tr:30});});
  d.text(X(17),24,176,5,'MITSUBISHI CORPORATION',{f:F.IN,s:8,c:C.INK,cs:3,ls:1});
  d.text(X(17),31,176,5,'Metal Resources Group',{f:F.ENL,s:10,c:C.G1,ls:1});
  d.text(X(17),268,176,12,'三菱商事株式会社　金属資源グループ\n〒100-8086 東京都千代田区丸の内2-3-1　｜　www.mitsubishicorp.com',{s:7,c:C.G1,ls:1.6});
}

// ---------------- P2–3 ----------------
function sp23(d){
  d.img('r-022.png',0,0,128,86,.5,.55); d.img('mr_03_01@2x.webp',130,0,80,86,.4,.5);
  d.img('r-023.png',0,88,82,46,.5,.6); d.img('r-054.png',84,88,62,46,.5,.5); d.img('_mr_project_06.png',148,88,62,46,.6,.5);
  d.img('_mr_project_04.png'===''?'':'r-046.png',212,0,208,134,.5,.45);
  [[3,'都市・インフラ'],[133,'金属素材'],[3,'海上輸送',88],[87,'銅地金',88],[151,'トレーディング',88],[215,'鉱山',0]].forEach(([x,t,y])=>CAP(d,x,(y||0)+(y===88?40:80),50,t));
  d.rect(0,140,420,0.5,{fill:C.CU});
  // P2
  K(d,L,148,'INTRODUCTION','社会と金属');
  H(d,L,155,120,'Metals shape\nthe way we live.',30);
  LEAD(d,L,182,110,'暮らしのすべてに、金属がある。');
  BODY(d,L,193,96,60,'ビル、鉄道、自動車、送電網、再生可能エネルギー、データセンター。私たちの暮らしと産業は、鉄や銅をはじめとする金属に支えられています。人口の増加と新興国の発展、そして社会の電化によって、金属の需要はこれからも高まっていきます。一方で、良質な資源の開発は年々難しくなり、資源を確保し、必要な場所へ確実に届けることの重要性が増しています。');
  // Where metals work（インフォグラフィック）
  const gx=122; K(d,gx,148,'WHERE METALS WORK','暮らしを支える金属',C.BR,76);
  const rows=[['都市・インフラ','建物・鉄道・橋',['Fe','Cu','Al']],['モビリティ','自動車・EV・船舶',['Fe','Cu','Li','Ni']],['電力・再エネ','送電網・風力・太陽光',['Cu','Al','Fe']],['デジタル','通信・データセンター',['Cu','Al']]];
  rows.forEach(([a,b,els],i)=>{const y=158+i*21; d.rect(gx,y,76,0.3,{fill:i?C.G3:C.INK});
    d.text(gx,y+3,40,5,a,{s:8,b:true,c:C.INK,ls:1}); d.text(gx,y+8.5,40,4,b,{s:6.2,c:C.G2,ls:1});
    els.forEach((e,j)=>{const cx=gx+45+j*8.2, cy=y+9; const cu=e==='Cu'; d.ell(cx,cy,3.6,3.6,{fill:cu?C.CU:C.W,line:cu?C.CU:C.G2,lw:0.6}); d.text(cx-3.6,cy-1.9,7.2,4,e,{f:F.IN,s:6.4,b:true,c:cu?C.W:C.G1,al:'center',ls:1});});});
  d.rect(gx,242,76,0.3,{fill:C.G3});
  d.text(gx,245,76,10,'Fe 鉄　Cu 銅　Al アルミ　Li リチウム　Ni ニッケル',{s:6,c:C.G2,ls:1.5});
  // 需給ギャップ
  const bx=L, by=252; d.text(bx,by,96,4,'需要と供給',{s:6.5,b:true,c:C.G1,ls:1});
  const X0=bx, Y0=by+30, Wc=96;
  d.path([[X0,Y0],{c:[X0+40,Y0-4,X0+70,Y0-14,X0+Wc,Y0-25]}],{line:C.INK,lw:1.6});
  d.path([[X0,Y0],{c:[X0+40,Y0-8,X0+70,Y0-11,X0+Wc,Y0-13]}],{line:C.G2,lw:1.2,dash:'dash'});
  d.rect(X0,Y0+0.6,Wc,0.3,{fill:C.G3});
  d.text(X0+Wc-30,Y0-31,30,4,'需要｜電化・人口増',{s:5.8,c:C.INK,al:'right',ls:1}); d.text(X0+Wc-30,Y0-19.5,30,4,'供給｜開発の難化',{s:5.8,c:C.G2,al:'right',ls:1});
  d.text(X0+Wc-46,Y0-25,26,4,'GAP',{f:F.IN,s:7,b:true,c:C.BR,ls:1});
  // P3
  K(d,R,148,'CORE MESSAGE','私たちの存在意義');
  H(d,R,155,184,'Strength to Hold.\nPower to Connect.',30,{light:true});
  LEAD(d,R,182,150,'持つ力と、つなぐ力。');
  BODY(d,R,193,112,40,'資源は、そこに「ある」だけでは、まだ価値ではありません。誰かが見出し、育て、必要とする場所へ届けて、はじめて社会の力になる。私たちは、世界有数の資産に関わり、投資とトレーディングの両輪で、川上から川下までをつなぎます。');
  [['HOLD','持つ力','世界有数の資源に投資し、長く育てる',C.BR],['CONNECT','つなぐ力','資源と市場をつなぎ、必要な場所へ届ける',C.NV]].forEach(([e,j,t,col],i)=>{const x=342,y=193+i*20; d.rect(x,y,2,15,{fill:col}); d.text(x+5,y,60,4,e,{f:F.IN,s:7,b:true,c:col,cs:1.5,ls:1}); d.text(x+5,y+4.5,60,5,j,{s:8.5,b:true,c:C.INK,ls:1}); d.text(x+5,y+10,60,4,t,{s:5.8,c:C.G2,ls:1.2});});
  K(d,R,240,'CONTENTS','目次');
  const toc=[['01','Who We Are','我々は何者か','04'],['02','Our Distinctive Strength','独自価値','06'],['03','Our Businesses & Innovation','主力事業と新技術','08'],['04','Partner of Choice','選ばれ続ける理由','10'],['05','Supporting Society','社会課題への取り組み','11']];
  toc.forEach(([n,e,j,p],i)=>{const x=R+i*37.2,y=248; d.rect(x,y,34,0.4,{fill:C.INK}); d.text(x,y+2,34,10,n,{f:F.ENL,s:20,c:C.BR,ls:1}); d.text(x,y+12,34,9,e,{f:F.EN,s:7.4,b:true,c:C.INK,ls:1.05}); d.text(x,y+21,34,4,j,{s:6,c:C.G2,ls:1}); d.text(x,y+26,34,4,'P.'+p,{f:F.IN,s:6,c:C.G2,ls:1});});
  FOLIO(d,2,'L'); FOLIO(d,3,'R',210);
}

// ---------------- P4–5  A ----------------
function journey(d,x0,y,w,o={}){
  const eras=[['1980–90s','日本の産業に、資源を。','日本の製造業を支えるため、トレーディングで資源に関わり、少数出資から事業へ。'],
    ['1990s','仲介から、担い手へ。','口銭収入に頼らず、資産を持つ投資モデルへ転換。JV運営の知見を蓄える。'],
    ['2000s','一級資産に、早くから。','需要の拡大を先読みし、BHPとの折半出資でBMAを組成。事業経営に参画。'],
    ['2010s','次の柱を、先回りして。','原料炭に続く柱として銅へ領域を拡大。販売機能をRtMに集約。'],
    ['2020s–','投資と販売を、一つの力に。','両輪を一体で動かし、世界の市場と産業をつなぐ事業者へ。']];
  const cw=w/5;
  eras.forEach(([yr,h,t],i)=>{const x=x0+i*cw; d.text(x,y-11,cw,6,yr,{f:F.EN,s:10.5,b:true,c:C.INK,ls:1}); dot(d,x+1.6,y,1.6,(i===2||i===3)?C.CU:C.INK);
    d.text(x,y+4,cw-3,9,h,{s:7.6,b:true,c:C.INK,ls:1.3}); d.text(x,y+13,cw-3.5,16,t,{s:6.3,c:C.G1,ls:1.5});});
}
function ring7(d,cx,cy,r0,r1,o={}){
  const n=7, seg=360/n, gap=1.4;
  for(let i=0;i<n;i++){const a0=-seg/2+i*seg+gap/2,a1=a0+seg-gap; d.path(segPts(cx,cy,r0,r1,a0,a1),{fill:i===0?C.CU:C.G5,close:true});}
  d.ell(cx,cy,r0-3,r0-3,{fill:C.PAN});
}
function sp45A(d){
  BIGNUM(d,104,-6,'01');
  K(d,L,16,'CHAPTER 01','我々は何者か｜三菱商事とは');
  H(d,L,23,150,'Who We Are',42);
  LEAD(d,L,42,150,'三綱領を精神の根幹に、「総合力」で価値を生む。');
  BODY(d,L,53,104,30,'三菱商事は、三綱領を企業理念とし、事業を通じて経済価値・社会価値・環境価値の同時実現を目指しています。幅広い産業と地域にまたがる事業と人のつながり。その「総合力」こそが、三菱商事の強みです。');
  // 7グループの輪 → 金属資源グループ
  const cx=92, cy=150, r0=38, r1=60;
  d.ell(cx,cy,r1+9,r1+9,{line:C.G3,lw:0.4}); d.ell(cx,cy,r1+13,r1+13,{line:C.G4,lw:0.4});
  ring7(d,cx,cy,r0,r1);
  for(let i=1;i<7;i++){const a=(i*360/7)*Math.PI/180; dot(d,cx+(r0+r1)/2*Math.cos(a),cy+(r0+r1)/2*Math.sin(a),1.1,C.W);}
  d.text(cx-28,cy-13,56,6,'三菱商事',{s:13,b:true,c:C.INK,al:'center',ls:1});
  d.text(cx-28,cy-4,56,4,'総合力',{s:8,b:true,c:C.BR,al:'center',ls:1});
  d.text(cx-28,cy+3,56,10,'多様な産業 × 地域 × 機能',{s:6,c:C.G2,al:'center',ls:1});
  d.text(cx-28,cy+9,56,4,'7つの営業グループ',{s:6,c:C.G1,al:'center',ls:1});
  d.text(cx+r0+1,cy-6,r1-r0-2,14,'金属資源\nグループ',{s:7.4,b:true,c:C.W,al:'center',ls:1.2});
  d.text(cx-75,cy-r1-14,150,4,'7 BUSINESS GROUPS',{f:F.IN,s:6,b:true,c:C.G2,cs:2.4,al:'center',ls:1});
  // 接続ライン（ノドを越えて右ページのミッションへ）
  d.line(cx+r1+0.5,cy,240,cy,{c:C.CU,w:1.4}); dot(d,cx+r1+13,cy,1.6,C.CU); dot(d,240,cy,2.2,C.CU);
  d.text(L,221,140,10,'7つの営業グループのうち、長年三菱商事を支えてきた中核グループの一つ。',{s:8.4,b:true,c:C.INK,ls:1.45});
  // 三綱領
  d.rect(L,238,184,0.4,{fill:C.INK}); K(d,L,241,'PRINCIPLES','三綱領｜三菱商事の企業理念');
  [['所期奉公','しょきほうこう','事業を通じ、物心共に豊かな社会の実現に努力すると同時に、かけがえのない地球環境の維持にも貢献する'],['処事光明','しょじこうめい','公明正大で品格のある行動を旨とし、活動の公開性、透明性を堅持する'],['立業貿易','りつぎょうぼうえき','全世界的、宇宙的視野に立脚した事業展開を図る']].forEach(([a,r,t],i)=>{const x=L+i*62;
    d.text(x,249,58,7,a,{s:13,b:true,c:C.INK,ls:1}); d.text(x,257,58,4,r,{s:5.8,c:C.BR,ls:1}); d.text(x,262,56,18,t,{s:6.3,c:C.G1,ls:1.55});});
  FOLIO(d,4,'L');
  // P5
  K(d,R,16,'CHAPTER 01','我々は何者か｜金属資源グループとは');
  H(d,R,23,184,'The core that\nhas carried us.',30);
  LEAD(d,R,48,184,'三綱領を事業で体現する、中核グループとして。');
  BODY(d,R,59,110,30,'社会に不可欠な金属資源を世界から確保し、安定的に届けてきました。市況の波を越えて事業に関わり続け、長年にわたり全社の利益を支える屋台骨となっています。');
  d.img('_mr_project_03.png',338,56,68,40,.5,.5);
  d.rect(R,104,184,0.4,{fill:C.INK}); K(d,R,107,'CONTRIBUTION','長年の貢献');
  d.text(R,113,110,12,'市況の波を越えて、全社の利益を長く支えてきた。',{s:10,b:true,c:C.INK,ls:1.35});
  d.rect(240,128,166,44,{fill:C.INK});
  d.text(250,134,150,4,[{t:'GROUP MISSION',f:F.IN,s:6.5,b:true,c:'E9D6AC',cs:1.6},{t:'　グループミッション',s:6.5,c:'C9CED3'}],{ls:1});
  d.text(250,142,148,24,'社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する',{s:11,b:true,c:C.W,ls:1.5});
  K(d,R,182,'OUR JOURNEY','先見性をもって、先手を打ってきた歩み');
  d.line(R,210,420,210,{c:C.CU,w:1.2});
  journey(d,R,210,184);
  d.rect(R,250,184,0.3,{fill:C.G3}); K(d,R,254,'PORTFOLIO','事業領域');
  ['原料炭','銅','鉄鉱石','ニッケル','リチウム','アルミ・ボーキサイト','肥料資源','二次資源'].forEach((t,i,a)=>{const ws=[16,12,16,18,18,30,18,18]; let x=R; for(let k=0;k<i;k++) x+=ws[k]+2.5; chip(d,x,261,ws[i],7,t,{fill:i<2?C.CU:C.W,line:i<2?C.CU:C.G3,c:i<2?C.W:C.G1,s:6.4});});
  d.text(R,271,184,4,'原料炭と銅を中核に、世界に事業を広げる。',{s:6.3,c:C.G2,ls:1});
  FOLIO(d,5,'R',210);
}
// ---------------- P4–5  B（総合力の構造図にミッションと歩みを重ねる） ----------------
function sp45B(d){
  BIGNUM(d,104,-6,'01');
  K(d,L,16,'CHAPTER 01','我々は何者か');
  H(d,L,23,150,'Who We Are',42);
  LEAD(d,L,42,180,'三綱領を精神の根幹に。その総合力の中核を担う、金属資源グループ。');
  const cx=96, cy=176, r0=46, r1=78;
  d.path([[cx+r1*Math.cos(-22*Math.PI/180),cy+r1*Math.sin(-22*Math.PI/180)],[420,64],[420,262],[cx+r1*Math.cos(22*Math.PI/180),cy+r1*Math.sin(22*Math.PI/180)]],{fill:C.CU,tr:90,close:true});
  d.ell(cx,cy,r1+10,r1+10,{line:C.G3,lw:0.4});
  ring7(d,cx,cy,r0,r1);
  d.ell(cx,cy,30,30,{fill:C.W,line:C.BRL,lw:0.5,dash:'dash'});
  d.text(cx-30,cy-38,60,6,'三菱商事｜総合力',{s:9.5,b:true,c:C.INK,al:'center',ls:1});
  d.text(cx-26,cy-12,52,4,'三綱領',{s:7,b:true,c:C.BR,al:'center',ls:1});
  d.text(cx-26,cy-5,52,16,'所期奉公\n処事光明\n立業貿易',{s:7.6,b:true,c:C.INK,al:'center',ls:1.4});
  d.text(cx+r0+2,cy-7,r1-r0-4,14,'金属資源\nグループ',{s:8,b:true,c:C.W,al:'center',ls:1.2});
  d.text(L,262,170,10,'7つの営業グループのうち、長年三菱商事を支えてきた中核グループの一つ。',{s:8.4,b:true,c:C.INK,ls:1.45});
  d.text(L,272,170,8,'三綱領を企業理念とし、幅広い産業と地域にまたがる事業と人のつながり＝「総合力」で価値を生み出しています。',{s:6.5,c:C.G1,ls:1.5});
  FOLIO(d,4,'L');
  d.text(R+8,72,170,4,[{t:'GROUP MISSION',f:F.IN,s:6.5,b:true,c:C.CU,cs:1.6},{t:'　グループミッション',s:6.5,c:C.G2}],{ls:1});
  d.text(R+8,80,170,20,'社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する',{s:11.5,b:true,c:C.INK,ls:1.5});
  K(d,R+8,112,'OUR JOURNEY','先見性をもって、先手を打ってきた歩み');
  const eras=[['1980–90s','日本の産業に、資源を。','トレーディングで資源に関わり、少数出資から事業へ。'],['1990s','仲介から、担い手へ。','資産を持つ投資モデルへ転換し、JV運営の知見を蓄える。'],['2000s','一級資産に、早くから。','BHPとの折半出資でBMAを組成し、事業経営に参画。'],['2010s','次の柱を、先回りして。','銅へ領域を拡大。販売機能をRtMに集約。'],['2020s–','投資と販売を、一つの力に。','両輪を一体で動かす、グローバルな事業者へ。']];
  d.line(R+12,124,R+12,250,{c:C.CU,w:1});
  eras.forEach(([y,h,t],i)=>{const yy=124+i*26; dot(d,R+12,yy+2,1.8,(i===2||i===3)?C.CU:C.INK); d.text(R+20,yy-1,30,6,y,{f:F.EN,s:10,b:true,c:C.INK,ls:1}); d.text(R+52,yy-1,60,5,h,{s:8,b:true,c:C.INK,ls:1.2}); d.text(R+52,yy+5,110,10,t,{s:6.4,c:C.G1,ls:1.45});});
  d.text(R+8,262,170,8,'市況の波を越えて事業に関わり続け、長年にわたり全社の利益を支える屋台骨に。',{s:8.4,b:true,c:C.INK,ls:1.4});
  FOLIO(d,5,'R',210);
}

// ---------------- P6–7  A（バリューチェーン横軸＋2本のライン＋情報の戻り） ----------------
function sp67A(d){
  BIGNUM(d,124,-6,'02');
  K(d,L,16,'CHAPTER 02','独自価値');
  H(d,L,23,184,'Our Distinctive\nStrength',36);
  LEAD(d,L,52,180,'投資とトレーディングの両輪で、資源の流れ全体に関わる。');
  H(d,R,21,184,'Not a miner.\nNot just a trader.',18,{light:true,c:C.G1});
  BODY(d,R,38,184,24,'資源に投資して育てる力と、市場へ届ける力。その両方を持ち、互いを強め合いながら長い時間をかけて積み重ねてきたこと。それが、鉱山会社でも純粋なトレーダーでもない、金属資源グループならではの強さです。');
  const S=[[14,86,'UPSTREAM','鉱山・資源開発','_mr_project_03.png'],[112,86,'PROCESSING','選鉱・製錬・製鉄','mr_02_01@2x.webp'],[222,86,'LOGISTICS & SALES','調達・物流・販売','r-023.png'],[320,86,'CUSTOMERS','産業の需要家','r-022.png']];
  const top=86;
  // 市場情報の戻り（B）：需要家 → 投資
  d.path([[363,top-1],[363,76],[30,76],[30,top+0.5]],{line:C.NV,lw:1,dash:'dash',end:'triangle'});
  d.rect(96,73.5,92,5,{fill:C.W}); d.text(96,74,92,4,'B　市場の情報を、次の投資判断へ',{s:6.8,b:true,c:C.NV,al:'center',ls:1});
  S.forEach(([x,w,e,j,img])=>{d.text(x,top,w,4,e,{f:F.IN,s:6.3,b:true,c:C.G2,cs:1.6,ls:1}); d.text(x,top+4.5,w,5,j,{s:9,b:true,c:C.INK,ls:1}); d.img(img,x,top+11,w,30,.5,.5);});
  // HOLD ライン
  const hy=132; d.rect(14,hy,184,2.2,{fill:C.BR});
  d.text(30,hy+3.5,168,5,[{t:'HOLD',f:F.IN,s:7.5,b:true,c:C.BR,cs:1.6},{t:'　資源投資｜鉱山・製錬への出資　',s:7,b:true,c:C.INK},{t:'鉄鋼原料本部・クリティカルミネラル本部',s:6,c:C.G2}],{ls:1});
  // 2つの素材レーン（鉄鋼原料／銅）
  const lanes=[[150,'鉄鋼原料',['原料炭・鉄鉱石','製鉄所｜鋼材','建設・自動車・インフラ']],[167,'銅',['銅鉱石','選鉱・製錬｜銅地金','電線・電力・データセンター']]];
  lanes.forEach(([y,tag,cells])=>{
    d.text(14,y+1.8,14,4,tag,{s:6,b:true,c:C.G2,ls:1});
    chip(d,30,y,68,9,cells[0],{s:7.4}); chip(d,112,y,86,9,cells[1],{s:7.4}); chip(d,320,y,86,9,cells[2],{s:7.4});
    d.line(98.5,y+4.5,111.5,y+4.5,{c:C.G2,w:0.8,end:'triangle'});
    d.line(198.5,y+4.5,221,y+4.5,{c:C.G2,w:0.8});
    d.line(308.5,y+4.5,319.5,y+4.5,{c:C.G2,w:0.8,end:'triangle'});
  });
  // 物流・販売セル（両レーンにまたがる）
  d.rect(222,148,86,22.5,{fill:'EEF2F6',line:C.NVL,lw:0.6,r:3}); d.line(221,154.5,222,154.5,{c:C.G2,w:0.8,end:'triangle'}); d.line(221,171.5,222,171.5,{c:C.G2,w:0.8,end:'triangle'});
  d.text(222,151.5,86,5,'RtM｜資源と市場をつなぐ',{s:7.6,b:true,c:C.NV,al:'center',ls:1});
  d.text(222,158,86,10,'鉱石・精鉱の段階から、地金・製品の段階まで\n物流・在庫・ヘッジ・販売を担う',{s:6,c:C.G1,al:'center',ls:1.45});
  // CONNECT ライン
  const cyl=184; d.rect(14,cyl,388,2.2,{fill:C.NV}); d.path([[402,cyl-2],[406,cyl+1.1],[402,cyl+4.2]],{fill:C.NV,close:true});
  d.text(30,cyl+3.8,168,5,[{t:'CONNECT',f:F.IN,s:7.5,b:true,c:C.NV,cs:1.6},{t:'　トレーディング（RtM）｜資源と市場をつなぐ　',s:7,b:true,c:C.INK},{t:'金属資源トレーディング本部',s:6,c:C.G2}],{ls:1});
  // A マーカー
  badge(d,22,hy+6,'A',C.BR); badge(d,22,cyl+6,'A',C.NV);
  // C 新技術ピン
  [[176,167,'選鉱・浸出'],[396,167,'リサイクル']].forEach(([x,y,t])=>{badge(d,x,y-1.5,'C',C.CU,2.8);});
  d.text(320,177,86,5,'C　新技術がボトルネックを改善 → P.08',{s:6,b:true,c:C.CU,ls:1});
  // D 長期の積み重ね
  const ty=204; d.line(14,ty,404,ty,{c:C.G3,w:3,end:'triangle'});
  ['1980s','1990s','2000s','2010s','2020s'].forEach((t,i)=>{const x=[40,100,160,270,350][i]; d.text(x-10,ty+3,20,4,t,{f:F.IN,s:6,c:C.G2,al:'center',ls:1});});
  badge(d,14,ty,'D',C.INK);
  d.text(22,ty-6.5,180,4,'D　市況に左右されず、流れに関わり続けてきた積み重ね',{s:6.4,b:true,c:C.INK,ls:1});
  // E 結果としての主力3事業
  d.rect(300,214,106,26,{fill:C.INK});
  d.text(306,218,96,4,[{t:'E',f:F.IN,s:7,b:true,c:'E9D6AC'},{t:'　その結果としての、いまの主力事業',s:6.6,b:true,c:C.W}],{ls:1});
  ['原料炭','銅','トレーディング'].forEach((t,i)=>chip(d,306+i*31,226,i==2?34:28,8,t,{fill:C.INK,line:'8A9096',c:C.W,s:6.6}));
  d.text(372,235.5,30,4,'→ P.08',{f:F.IN,s:6,c:'C9CED3',al:'right',ls:1});
  // 凡例（A–E）
  const LG=[['A','持つ力・つなぐ力','投資とトレーディングの両輪で事業を行う。鉱山会社でも純粋なトレーダーでもない立ち位置。',C.BR],
    ['B','互いを強め合う','市場の情報を投資判断に生かし、投資で得た資源を市場へ届ける好循環。',C.NV],
    ['C','流れ全体を進化させる','業界の課題に挑む新技術に投資し、知見を両輪に還元する。',C.CU],
    ['D','長い時間をかけて','流れに関わり続けた積み重ねが、先手を打つ力（先見性）に。',C.INK],
    ['E','その結果としての、いま','原料炭・銅・トレーディングは、強みの「結果」である。',C.RED]];
  const pos=[14,76,138,222,320], wd=[56,56,56,86,86];
  LG.forEach(([k,t,s,col],i)=>{const x=pos[i]; d.rect(x,248,wd[i],0.4,{fill:C.INK}); badge(d,x+3,254,k,col,2.8); d.text(x+8,251.8,wd[i]-8,5,t,{s:7.6,b:true,c:C.INK,ls:1}); d.text(x,259,wd[i]-2,20,s,{s:6.3,c:C.G1,ls:1.55});});
  FOLIO(d,6,'L'); FOLIO(d,7,'R',210);
}
// ---------------- P6–7  B（価値循環ループ＋各事業） ----------------
function sp67B(d){
  BIGNUM(d,124,-6,'02');
  K(d,L,16,'CHAPTER 02','独自価値');
  H(d,L,23,184,'Our Distinctive\nStrength',36);
  LEAD(d,L,52,180,'投資とトレーディングが互いを強め合い、価値が循環する。');
  const cx=105, cy=170, r=52;
  d.ell(cx,cy,r+16,r+16,{line:C.G3,lw:0.5,dash:'dash'});
  d.path(segPts(cx,cy,r-14,r,180,360),{fill:C.BR,close:true}); d.path(segPts(cx,cy,r-14,r,0,180),{fill:C.NV,close:true});
  d.path([[cx+r+5,cy-6],[cx+r-7,cy-6],[cx+r-1,cy+4]],{fill:C.BR,close:true}); d.path([[cx-r-5,cy+6],[cx-r+7,cy+6],[cx-r+1,cy-4]],{fill:C.NV,close:true});
  d.ell(cx,cy,r-18,r-18,{fill:C.PAN});
  d.text(cx-30,cy-10,60,6,'Strength to Hold.',{f:F.EN,s:9,b:true,c:C.BR,al:'center',ls:1}); d.text(cx-30,cy+2,60,6,'Power to Connect.',{f:F.EN,s:9,b:true,c:C.NV,al:'center',ls:1});
  d.text(cx-40,cy-r-12,80,5,'HOLD｜資源投資',{s:8.5,b:true,c:C.BR,al:'center',ls:1}); d.text(cx-50,cy-r-6.5,100,4,'投資で得た資源を、市場へ届ける',{s:6.2,c:C.G1,al:'center',ls:1});
  d.text(cx-40,cy+r+3,80,5,'CONNECT｜トレーディング',{s:8.5,b:true,c:C.NV,al:'center',ls:1}); d.text(cx-50,cy+r+9,100,4,'市場の情報を、投資判断へ返す',{s:6.2,c:C.G1,al:'center',ls:1});
  badge(d,cx-r-12,cy-r+4,'A',C.BR); badge(d,cx+r+10,cy+r-4,'B',C.NV);
  // 新技術の注入
  d.line(cx+r+16,cy-30,232,104,{c:C.CU,w:1,dash:'dash',beg:'triangle'}); badge(d,cx+r+22,cy-40,'C',C.CU);
  d.text(L,250,180,5,'D　この循環に、長い時間をかけて関わり続けてきた。',{s:8.4,b:true,c:C.INK,ls:1});
  d.text(L,258,180,10,'市況の浮き沈みに左右されず関わり続けた積み重ねが、先を見据えて手を打つ力（先見性）になっています。',{s:6.5,c:C.G1,ls:1.5});
  FOLIO(d,6,'L');
  // 右：新技術＋3事業
  d.rect(232,92,174,26,{fill:C.CUL});
  d.text(240,97,160,5,'C　NEW TECHNOLOGY｜流れ全体を進化させる',{s:8,b:true,c:C.CU,ls:1}); d.text(240,104,160,10,'業界のボトルネック（選鉱・浸出・リサイクル）に挑む技術へ投資し、知見を両輪に還元する。',{s:6.6,c:C.G1,ls:1.5});
  K(d,R,130,'RESULT','E　その結果としての、いまの主力事業');
  [['METALLURGICAL COAL','原料炭','高品位の一級資産を、長期のコミットメントで育てる','r-047.png'],['COPPER','銅','世界上位の優良鉱山に、早くから参画','_mr_project_02.png'],['TRADING','トレーディング','自社と第三者の資源を、世界の需要家へ','r-023.png']].forEach(([e,j,t,img],i)=>{const y=140+i*40;
    d.img(img,R,y,52,34,.5,.5); d.text(R+58,y+2,120,5,e,{f:F.EN,s:10,b:true,c:C.INK,ls:1}); d.text(R+58,y+9,120,5,j,{s:8,b:true,c:C.BR,ls:1}); d.text(R+58,y+16,120,10,t,{s:6.8,c:C.G1,ls:1.45});
    d.line(cx+r+16,cy,R-2,y+17,{c:C.G3,w:0.6}); });
  d.text(R,264,184,5,'→ 詳しくは P.08　Our Businesses & Innovation',{s:6.6,b:true,c:C.CU,ls:1});
  FOLIO(d,7,'R',210);
}

// ---------------- P8–9 主力3事業＋新技術 ----------------
function sp89(d){
  K(d,L,12,'CHAPTER 03','独自価値｜主力事業と新技術');
  H(d,L,17,184,'Our Businesses & Innovation',24);
  d.text(R,17,184,10,'原料炭・銅・トレーディング。3つの主力事業と、業界の課題に挑む新技術。',{s:8.5,b:true,c:C.INK,ls:1.4});
  const cols=[[14,120],[146,128],[286,120]];
  d.img('r-047.png',14,36,120,24,.5,.62); d.img('_mr_project_02.png',146,36,128,24,.5,.5); d.img('r-023.png',286,36,120,24,.5,.6);
  const head=(x,w,e,j)=>{d.text(x,63,w,6,e,{f:F.EN,s:13,b:true,c:C.INK,cs:0.3,ls:1}); d.rect(x,70.5,8,0.5,{fill:C.RED}); d.text(x,72.5,w,9,j,{s:7.6,b:true,c:C.INK,ls:1.35});};
  const msq=(x,y,w,rows)=>{rows.forEach(([k,v,s],i)=>{const yy=y+i*9; d.rect(x,yy,w,0.3,{fill:i?C.G3:C.INK}); d.text(x,yy+2.2,18,4,k,{f:F.IN,s:5.4,b:true,c:C.G2,cs:1,ls:1}); d.text(x+18,yy+1.6,w-18,4,v,{s:7,b:true,c:C.INK,ls:1}); d.text(x+18,yy+5.3,w-18,4,s,{s:5.6,c:C.G2,ls:1});});};
  // A 原料炭
  let [x,w]=cols[0];
  head(x,w,'METALLURGICAL COAL','社会に不可欠な高品位原料炭の一級資産を、長期のコミットメントで育ててきた。');
  d.text(x,84,50,12,'50:50',{f:F.ENL,s:26,c:C.INK,ls:1}); d.text(x,95,52,8,'BHPとの合弁 BMA\n（BHP Mitsubishi Alliance）',{s:5.8,c:C.G1,ls:1.35});
  // JV図
  const jb=(bx,by,bw,t,s2,col)=>{d.rect(bx,by,bw,8,{fill:C.W,line:col,lw:0.7}); d.text(bx,by+1.2,bw,4,t,{f:F.IN,s:6.6,b:true,c:C.INK,al:'center',ls:1}); if(s2) d.text(bx,by+4.6,bw,3,s2,{s:4.6,c:C.G2,al:'center',ls:1});};
  jb(x+62,84,26,'三菱商事','',C.INK); jb(x+62,98,26,'MDP','三菱商事100%',C.INK); jb(x+93,98,24,'BHP','',C.G2);
  d.rect(x+62,112,55,9,{fill:C.INK}); d.text(x+62,113.5,55,4,'BMA',{f:F.IN,s:7.4,b:true,c:C.W,al:'center',ls:1}); d.text(x+62,117.2,55,3,'豪州クイーンズランド州 ボーエン・ベースン',{s:4.8,c:'C9CED3',al:'center',ls:1});
  d.line(x+75,92,x+75,97.5,{c:C.INK,w:0.6,end:'triangle'}); d.line(x+75,106,x+75,111.5,{c:C.INK,w:0.6,end:'triangle'}); d.line(x+105,106,x+105,111.5,{c:C.G2,w:0.6,end:'triangle'});
  d.text(x+76.5,107.2,10,3,'50%',{f:F.IN,s:5,c:C.G1,ls:1}); d.text(x+106.5,107.2,10,3,'50%',{f:F.IN,s:5,c:C.G1,ls:1});
  // 7→5
  d.text(x,107,56,4,'高品位への厳選',{s:6.4,b:true,c:C.INK,ls:1});
  for(let i=0;i<7;i++){const keep=i<5; d.ell(x+3+i*6.4,116,2.4,2.4,{fill:keep?C.BR:C.W,line:keep?C.BR:C.G3,lw:0.7});}
  d.text(x,120.5,58,4,'7炭鉱 → 高品位の5炭鉱へ',{s:5.6,c:C.G1,ls:1});
  msq(x,126,w,[['MARKET','上位5社で約80%','寡占度が高く、供給は漸減'],['SCALE','一級強粘炭の世界供給の約50%','BMAが占めるシェア'],['QUALITY','炭鉱から港湾・鉄道まで保有','山から港まで一体で運営']]);
  // B 銅（ノドを避けて左右に分割）
  [x,w]=cols[1];
  head(x,57,'COPPER','電化と成長を支える銅。世界上位の優良鉱山に早くから参画。');
  d.text(x,84,57,12,'Top 15',{f:F.ENL,s:24,c:C.INK,ls:1}); d.text(x,95,57,10,'操業中の主要5鉱山すべてが、鉱山別生産量で世界トップ15',{s:5.8,c:C.G1,ls:1.35});
  msq(x,108,57,[['MARKET','上位5社で約25%','寡占化が進まず、再編の機運'],['SCALE','日本最大の銅生産者','持分生産量ベース'],['PARTNERS','主要メジャーの多くと協業','特定の1社に偏らない']]);
  d.rect(x,135,57,0.3,{fill:C.G3});
  const tx=217, tw=57;
  d.text(tx,63,tw,4,'EARLY ENTRY',{f:F.IN,s:6.3,b:true,c:C.BR,cs:1.6,ls:1}); d.text(tx,67.5,tw,4,'主要銅鉱山への参画年と世界順位',{s:6,c:C.G2,ls:1});
  const mines=[[1988,'Escondida','チリ','1'],[1997,'Los Pelambres','チリ','12'],[1999,'Antamina','ペルー','4'],[2011,'Anglo American Sur','チリ','10'],[2011,'Quellaveco','ペルー','15'],[2023,'Marimaca','チリ',null],[2025,'Copper World','米国',null]];
  d.line(tx+12,76,tx+12,76+6*9.2,{c:C.G3,w:0.8});
  mines.forEach(([yr,n,c,rk],i)=>{const y=76+i*9.2; d.text(tx,y-1.6,10,4,String(yr),{f:F.IN,s:5.8,c:C.G1,ls:1});
    if(rk){d.ell(tx+12,y,3,3,{fill:C.CU}); d.text(tx+9,y-1.6,6,4,rk,{f:F.IN,s:5.4,b:true,c:C.W,al:'center',ls:1});}
    else {d.ell(tx+12,y,2.6,2.6,{fill:C.W,line:C.CU,lw:0.8});}
    d.text(tx+17,y-2.3,42,4,n,{f:F.IN,s:6.4,b:true,c:C.INK,ls:1}); d.text(tx+17,y+1.4,42,3,c+(rk?'':'｜開発中'),{s:5,c:rk?C.G2:C.CU,b:!rk,ls:1});});
  d.text(tx,139,tw,8,'●内の数字＝鉱山別生産量の世界順位\n○＝開発中（順位対象外）',{s:4.8,c:C.G2,ls:1.4});
  // C トレーディング
  [x,w]=cols[2];
  head(x,w,'TRADING','自社アセットに限らず第三者の資源も扱い、資源と市場をつなぐ。');
  [['15','業界'],['50','カ国'],['約1,000','社の販売先']].forEach(([n,t],i)=>{const xx=x+i*36; d.text(xx,84,36,10,n,{f:F.ENL,s:i==2?19:24,c:C.INK,ls:1}); d.text(xx,95,36,4,t,{s:5.8,c:C.G1,ls:1});});
  // フロー
  const fy=103;
  const fb=(bx,by,bw,bh,t,col,fill,tc)=>{d.rect(bx,by,bw,bh,{fill:fill||C.W,line:col,lw:0.7,r:1.2}); d.text(bx,by+bh/2-2.2,bw,5,t,{s:6.3,b:true,c:tc||C.INK,al:'center',ls:1.2});};
  fb(x,fy,30,9,'自社の保有資産',C.BR); fb(x,fy+12,30,9,'第三者の資源',C.G2);
  d.rect(x+40,fy+3,32,15,{fill:C.NV,r:1.5}); d.text(x+40,fy+6,32,5,'RtM',{f:F.EN,s:10,b:true,c:C.W,al:'center',ls:1}); d.text(x+40,fy+12,32,4,'Resource to Market',{f:F.IN,s:4.6,c:'C9D6E3',al:'center',ls:1});
  fb(x+82,fy+3,38,15,'世界の顧客\n15業界・50カ国',C.INK);
  d.line(x+30.5,fy+4.5,x+39.5,fy+8,{c:C.NV,w:0.7,end:'triangle'}); d.line(x+30.5,fy+16.5,x+39.5,fy+13,{c:C.NV,w:0.7,end:'triangle'}); d.line(x+72.5,fy+10.5,x+81.5,fy+10.5,{c:C.NV,w:0.7,end:'triangle'});
  d.path([[x+101,fy+18.5],[x+101,fy+26],[x+15,fy+26],[x+15,fy+9.5]],{line:C.BR,lw:0.8,dash:'dash',end:'triangle'});
  d.text(x+34,fy+27,60,4,'市場の情報を、投資の判断へ',{s:5.6,b:true,c:C.BR,al:'center',ls:1});
  d.text(x,135,w,4,'FUNCTIONS｜多様な取引機能',{s:6,b:true,c:C.NV,ls:1});
  ['物流','在庫','ヘッジ','リスク管理'].forEach((t,i)=>chip(d,x+i*30.5,140,28,7.5,t,{fill:'EEF2F6',line:C.NVL,c:C.NV,s:6.4,r:1}));
  // NEW TECHNOLOGY 帯
  const ny=156; d.rect(0,ny,420,141,{fill:C.PAN});
  K(d,L,ny+8,'NEW TECHNOLOGY','新技術',C.CU);
  H(d,L,ny+14,70,"Investing in\nwhat's next.",19);
  d.rect(L,ny+31,8,0.5,{fill:C.RED});
  d.text(L,ny+34,66,12,'業界のボトルネックに挑む技術へ投資し、現場へ届ける。',{s:7.6,b:true,c:C.INK,ls:1.4});
  BODY(d,L,ny+48,62,50,'資源の流れの中で、業界の課題になっている工程を見極め、課題を解く技術を持つスタートアップに出資しています。トレーディングや業界とのつながりを生かして技術を現場に取り入れ、得られた知見を既存事業の高度化に還元しています。',6.6);
  // 銅のバリューチェーン（形の変化）
  const sy=ny+40, xs=[92,138,182,250,304];
  const st=[['鉱石','ORE'],['選鉱｜銅精鉱','CONCENTRATE'],['製錬｜銅地金','CATHODE'],['用途','END USE'],['回収・リサイクル','RECYCLING']];
  d.text(80,ny+10,120,4,'COPPER VALUE CHAIN｜銅が姿を変えていく流れ',{f:F.IN,s:6.4,b:true,c:C.G1,cs:1.2,ls:1});
  // 形
  d.path([[xs[0]-11,sy+6],[xs[0]-6,sy-6],[xs[0]+3,sy-9],[xs[0]+11,sy-3],[xs[0]+9,sy+7],[xs[0]-2,sy+9]],{fill:'5A6068',close:true});
  [[-4,-2],[3,1],[-1,5],[5,-5]].forEach(([a,b])=>d.ell(xs[0]+a,sy+b,1,1,{fill:C.CU}));
  d.path([[xs[1]-12,sy+8],[xs[1]-6,sy-2],[xs[1]-1,sy-6],[xs[1]+5,sy-3],[xs[1]+12,sy+8]],{fill:'8C5A3A',close:true});
  for(let k=0;k<6;k++) d.ell(xs[1]-8+k*3.2,sy+5-(k%2)*2,0.6,0.6,{fill:C.CUL});
  for(let k=0;k<3;k++) d.rect(xs[2]-10+k*2.2,sy-8+k*1.6,18,14,{fill:[C.CU,'B8723F','C88752'][k],line:'8C4E24',lw:0.4});
  d.ell(xs[3],sy,9,9,{line:C.CU,lw:2.2}); d.ell(xs[3],sy,5,5,{line:C.CU,lw:2.2}); d.ell(xs[3],sy,1.6,1.6,{fill:C.CU});
  d.path(arcPts(xs[4],sy,8,200,520-40),{line:C.CU,lw:2}); d.path([[xs[4]+6.5,sy-9.5],[xs[4]+9.5,sy-4.8],[xs[4]+3.8,sy-4.2]],{fill:C.CU,close:true});
  // 流れ矢印
  [[0,1],[1,2],[3,4]].forEach(([a,b])=>d.line(xs[a]+14,sy,xs[b]-14,sy,{c:C.G1,w:0.9,end:'triangle'}));
  d.line(xs[2]+14,sy,xs[3]-14,sy,{c:C.G1,w:0.9,end:'triangle'});
  st.forEach(([j,e],i)=>{d.text(xs[i]-22,sy+12,44,4,e,{f:F.IN,s:5.4,b:true,c:C.G2,al:'center',cs:1,ls:1}); d.text(xs[i]-22,sy+16.5,44,5,j,{s:7.4,b:true,c:C.INK,al:'center',ls:1});});
  // 浸出の分岐
  const lx=124, ly=sy+36;
  d.path([[xs[0],sy+22],[xs[0],ly],[lx-12,ly]],{line:C.G1,lw:0.8,end:'triangle'});
  d.rect(lx-12,ly-5,34,10,{fill:C.W,line:C.G1,lw:0.6,r:5}); d.text(lx-12,ly-2.2,34,5,'浸出（リーチング）',{s:6.4,b:true,c:C.INK,al:'center',ls:1});
  d.path([[lx+22,ly],[xs[2],ly],[xs[2],sy+22]],{line:C.G1,lw:0.8,end:'triangle'});
  d.text(lx+24,ly-4.5,36,4,'電解採取で銅地金へ',{s:5,c:C.G2,ls:1});
  // リサイクルの戻り
  d.path([[xs[4],sy+22],{c:[xs[4],sy+48,xs[2]+30,sy+52,xs[2]+16,sy+26]}],{line:C.CU,lw:0.9,dash:'dash',end:'triangle'});
  d.text(256,sy+49,40,4,'再び供給へ',{s:5.6,b:true,c:C.CU,ls:1});
  // 技術ピン
  const pin=(px,py,ty,n,t,s,bx)=>{d.line(px,py,px,ty-0.5,{c:C.CU,w:0.8}); dot(d,px,py,1.8,C.CU);
    d.rect(bx,ty,48,22,{fill:C.W,line:C.CU,lw:0.8}); d.rect(bx,ty,48,1.2,{fill:C.CU});
    d.text(bx+3,ty+3,42,4,n,{f:F.EN,s:9,b:true,c:C.INK,ls:1}); d.text(bx+3,ty+8.5,42,4,t,{s:6,b:true,c:C.CU,ls:1}); d.text(bx+3,ty+13,43,8,s,{s:5.4,c:C.G1,ls:1.35});};
  pin(xs[1]+4,sy+22,ny+92,'CiDRA','選鉱の高度化','浮遊選鉱を高度化し、銅の回収率と処理能力を高める',xs[1]+1);
  pin(lx-6,ly+5,ny+107,'Jetti','浸出による銅回収','触媒を用いた浸出で、硫化銅鉱から銅を回収する',lx-52);
  pin(xs[4],sy+22,ny+92,'DESCycle','資源の回収','電子スクラップから銅・貴金属を回収する',xs[4]-24);
  // Jetti ケース
  const jx=330, jw=76; d.rect(jx,ny+8,jw,125,{fill:C.W});
  d.text(jx+5,ny+13,jw-10,4,'CASE｜取り組み事例',{s:6,b:true,c:C.CU,ls:1});
  d.text(jx+5,ny+18,jw-10,7,'Jetti × 三菱商事',{f:F.EN,s:11,b:true,c:C.INK,ls:1});
  const stp=[['01','BOTTLENECK','課題','低品位・難処理の硫化銅鉱は、従来の方法では銅を回収しにくい。'],['02','TECHNOLOGY','技術が変える工程','触媒を用いた浸出（リーチング）で、硫化銅鉱から銅を回収する。'],['03','VALUE','期待する価値','これまで活用しにくかった鉱石の活用と、環境価値の高い銅地金の供給。']];
  stp.forEach(([n,e,j,t],i)=>{const y=ny+30+i*28; d.text(jx+5,y,10,6,n,{f:F.ENL,s:13,c:C.CU,ls:1}); d.text(jx+17,y,jw-22,4,e,{f:F.IN,s:5.6,b:true,c:C.G2,cs:1,ls:1}); d.text(jx+17,y+4,jw-22,4,j,{s:7,b:true,c:C.INK,ls:1}); d.text(jx+17,y+9.5,jw-21,14,t,{s:5.9,c:C.G1,ls:1.45});
    if(i<2) d.line(jx+10,y+8,jx+10,y+25,{c:C.CUL,w:1.2});});
  d.rect(jx+5,ny+113,jw-10,0.3,{fill:C.G3});
  d.text(jx+5,ny+115,jw-10,16,'三菱商事の役割：出資による事業拡大の支援、同社技術で生産された銅地金の販売、鉱山への技術導入の共同検討。',{s:5.6,c:C.G1,ls:1.45});
  FOLIO(d,8,'L'); FOLIO(d,9,'R',210);
}

// ---------------- P10–11 ----------------
function sp1011(d){
  d.img('r-084.png',0,0,210,80,.5,.3); d.img('r-075.png',210,0,210,80,.5,.6);
  CAP(d,4,74,80,'パートナーシップ（写真は要差し替え）'); CAP(d,214,74,80,'社会を支える資源');
  // P10
  BIGNUM(d,120,78,'04',150);
  K(d,L,88,'CHAPTER 04','選ばれ続ける理由');
  H(d,L,94,184,'Partner of Choice',32);
  LEAD(d,L,110,184,'資源業界に不可欠な存在として、選ばれ続ける。');
  BODY(d,L,121,184,10,'資源メジャーをはじめとするパートナーと長期にわたり事業を共に育て、単なる共同出資者にとどまらない貢献を重ねてきました。');
  K(d,L,134,'WHY US → VALUE','4つの強みが、パートナーの価値に変わる');
  const rs=[['01','中長期の視座と文化的親和性','資源メジャーと同じ時間軸で事業に向き合う','長期にわたる、安定したパートナーシップ'],
            ['02','JV経営・現場への貢献','人材派遣・ガバナンス参画で経営と操業を支える','事業価値の最大化'],
            ['03','健全な財務基盤とリスクシェア','事業ポートフォリオを生かした資金力','大型案件のリスク分担'],
            ['04','マクロ環境とバリューチェーンの知見','幅広い産業接点から得る市場の理解','市場と産業の知見の提供']];
  rs.forEach(([n,t,s,v],i)=>{const y=142+i*21; d.rect(L,y,104,0.3,{fill:i?C.G3:C.INK});
    d.text(L,y+2,12,8,n,{f:F.ENL,s:15,c:C.BR,ls:1}); d.text(L+13,y+2.5,92,5,t,{s:7.8,b:true,c:C.INK,ls:1}); d.text(L+13,y+8.5,92,5,s,{s:6.1,c:C.G2,ls:1});
    d.line(L+106,y+8,L+117,y+8,{c:C.BR,w:0.8,end:'triangle'});
    d.rect(L+118,y+2.5,66,11,{fill:C.PAN,line:C.BRL,lw:0.5,r:1.5}); d.text(L+118,y+5.4,66,5,v,{s:7,b:true,c:C.INK,al:'center',ls:1});});
  d.text(L+118,137.5,66,4,'パートナーにもたらす価値',{s:6,b:true,c:C.BR,al:'center',ls:1});
  // 協業の循環
  K(d,L,232,'CYCLE OF COLLABORATION','協業が、次の協業を生む');
  const nodes=[['会社対会社の関係へ',L],['新たな協業が生まれる',L+64],['強み・知見・信頼が蓄積',L+128]];
  nodes.forEach(([t,x],i)=>{d.rect(x,240,56,12,{fill:i===0?C.INK:C.W,line:C.INK,lw:0.7,r:6}); d.text(x,243.4,56,5,t,{s:7,b:true,c:i===0?C.W:C.INK,al:'center',ls:1}); if(i<2) d.line(x+56.5,246,x+63.5,246,{c:C.INK,w:0.8,end:'triangle'});});
  d.path([[L+184,246],{c:[L+192,246,L+192,262,L+150,262]},[L+34,262],{c:[L+20,262,L+20,256,L+28,252.5]}],{line:C.BR,lw:0.9,dash:'dash',end:'triangle'});
  d.text(L,268,184,10,'主なJVパートナー　BHP　／　Rio Tinto　／　Anglo American　ほか',{s:7,b:true,c:C.G1,ls:1});
  FOLIO(d,10,'L');
  // P11
  BIGNUM(d,330,78,'05',150);
  K(d,R,88,'CHAPTER 05','何を実現するか');
  H(d,R,94,184,'Supporting Society with\nthe Resources It Needs',22);
  LEAD(d,R,112,184,'取り組みを通じて資源の安定供給を支え、パートナーと共に未来をつくる。');
  const tier=(y,en,jp)=>{d.text(R,y,60,4,en,{f:F.IN,s:6.3,b:true,c:C.G2,cs:1.6,ls:1}); d.text(R+40,y,100,4,jp,{s:6.3,c:C.G2,ls:1});};
  tier(126,'CHALLENGES','社会の課題');
  [['需要の拡大','電化・AI・データセンターで、基幹素材の需要が高まる'],['供給の制約','良質な資源の開発が、より難しく時間を要するように'],['地政学リスク','資源の囲い込みが、供給網に影響を与える']].forEach(([t,s],i)=>{const x=R+i*62; d.rect(x,131,58,20,{fill:C.PAN}); d.rect(x,131,58,0.6,{fill:C.INK}); d.text(x+3,134,52,5,t,{s:7.8,b:true,c:C.INK,ls:1}); d.text(x+3,140,52,10,s,{s:5.8,c:C.G1,ls:1.4});});
  const chv=(y)=>d.path([[R+86,y],[R+92,y+4],[R+98,y]],{line:C.RED,lw:1});
  chv(154);
  d.rect(R,161,184,9,{fill:C.INK}); d.text(R,163.2,184,5,'クリティカルミネラルの供給網を確保する重要性が、かつてなく高まっている',{s:7,b:true,c:C.W,al:'center',ls:1});
  chv(173);
  tier(181,'OUR ACTIONS','私たちのアクション');
  [['安定的な資源確保','資源投資','大規模資産の持分を確保し、成長領域に早くから参画する',C.BR],['バリューチェーン全体の効率化','トレーディング','権益の引き取りと外部調達で、必要な場所へ確実に届ける',C.NV]].forEach(([t,k,s,col],i)=>{const x=R+i*102; d.rect(x,186,82,24,{fill:C.W,line:col,lw:0.8}); d.rect(x,186,82,1.4,{fill:col}); d.text(x+4,190,74,4,k,{s:6,b:true,c:col,ls:1}); d.text(x+4,195,74,5,t,{s:8.2,b:true,c:C.INK,ls:1}); d.text(x+4,201.5,74,8,s,{s:5.9,c:C.G1,ls:1.4});});
  d.line(R+84,195,R+100,195,{c:C.G1,w:0.8,end:'triangle'}); d.line(R+100,201,R+84,201,{c:C.G1,w:0.8,end:'triangle'}); d.text(R+82,203,20,4,'連携',{s:5.8,b:true,c:C.G1,al:'center',ls:1});
  chv(214);
  tier(222,'VALUE','社会への価値');
  d.rect(R,227,184,48,{fill:C.INK});
  d.text(R+8,232,168,8,'持続可能で豊かな社会を、パートナーと共に。',{s:11,b:true,c:C.W,ls:1.2});
  d.text(R+8,242,168,12,'社会が必要とする良質な金属資源を、持続可能な形で安定供給することで、より良い社会の実現に寄与する。',{s:7.4,c:'DCE0E4',ls:1.5});
  d.text(R+8,256,168,14,'To contribute to a better society by providing a stable supply of high-quality mineral resources that society needs, in a sustainable way.',{f:F.IN,s:6.4,c:'9AA1A8',ls:1.3});
  FOLIO(d,11,'R',210);
}
module.exports={cover,back,sp23,sp45A,sp45B,sp67A,sp67B,sp89,sp1011};
