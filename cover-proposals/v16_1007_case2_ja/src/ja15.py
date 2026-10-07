s=open('daiwari_v15.py').read()
JB=['資源は、そこに「ある」だけでは、まだ価値ではありません。誰かが見出し、育て、必要とする場所へ届けて、はじめて力になる。私たちは、世界有数の資産に関わり、投資とトレーディングの両輪で川上から川下までをつなぎます。フェアな立場だからこそ、埋められる隙間がある。多様なパートナーと使い手の間に立ち、その時々の最適解を導く。世界に眠る価値を、社会の力へ。',
'三菱商事は、三綱領に基づき、経済価値・環境価値・社会価値の同時実現を目指す総合商社です。そのなかで金属資源グループは、社会に不可欠な金属資源を世界から確保し、安定的に届ける役割を担っています。資源投資を担う2本部と、トレーディングを担う1本部の両輪で、川上の鉱山から川下の需要家までをつないでいます。',
'原料炭と銅を中核に、鉄鉱石、電池資源、アルミ、肥料、二次資源へと事業領域を広げています。資産を保有する地域だけでなく、世界各地にトレーディング拠点と金属資源の担当者を置き、新しい事業機会を探っています。鉄鉱石を先頭に、世界に広がる事業と人の拠点を一覧で示します。',
'BHPと50:50の合弁であるBMAを通じ、豪州クイーンズランド州ボーエン・ベースンで世界最高品位の原料炭事業に参画しています。炭鉱に加えて港湾と鉄道も保有し、山から港まで全体最適で運営しています。',
'特定の1社に偏らず、主要メジャーのほぼすべてと共同事業・取引を行っています。販売を通じた幅広い関係と長年の実績が、新しい案件での信頼につながっています。',
'出資案件から得られるオフテイクをRtMが引き受け、ヘッジ・在庫・物流などの機能を付加して世界の顧客に届けます。顧客との接点から得た市場の生きた情報は、資源投資の判断へと還元されます。',
'新技術の把握は、既存事業の高度化と将来価値の創出に還元されます。鉱石品位の低下、回収率、リサイクルといった業界のボトルネックに挑むスタートアップへの投資を通じ、川上から川下までに網を張っています。',
'資源業界では、良い案件があっても単独では規模が大きすぎることが少なくありません。そのとき「三菱に声をかけよう」と思われる存在であること。業界最大手とJVを組み、人材派遣・ガバナンス参画・総合力で事業価値の最大化に貢献してきました。']
s=s.replace("pages=[]","_JB=iter(__JB__)\ndef BODY(x,y,w,n,s=''): return A(x,y,next(_JB),w,'bd','font-family:\"Noto Sans JP\";text-align:justify;'+s)\npages=[]",1).replace("__JB__",repr(JB))
M={"'MITSUBISHI CORPORATION　MINERAL RESOURCES GROUP'":"'三菱商事　金属資源グループ'",
"'Who We Are'":"'我々は何者か'","'What We Do'":"'独自価値'","'Why Partners Choose Us'":"'選ばれ続ける理由'","'Our Vision'":"'何を実現するか'","'CONTENTS'":"'目次'",
"'選ばれ続ける理由｜Partner of Choice'":"'Partner of Choice'",
"'01　WHO WE ARE'":"'01｜我々は何者か'","'Value chain'":"'バリューチェーン'",
"'Mine','資源開発・保有'":"'採掘','資源開発・保有'","'Trade','トレーディング'":"'流通','トレーディング'","'Smelt / Steel','製錬・製鉄'":"'加工','製錬・製鉄'","'End use','最終製品":"'需要家','最終製品",
"'OUR JOURNEY'":"'歩み'","'Guided by the Three Corporate Principles of Mitsubishi Corporation.'":"'三菱商事の三綱領（所期奉公・処事光明・立業貿易）を企業理念とする'",
"'02　WHAT WE DO'":"'02｜独自価値'","'OUR RESOURCES'":"'取扱資源'","'Metallurgical Coal','原料炭'":"'原料炭',''","'Copper','銅'":"'銅',''",
"'Iron Ore','鉄鉱石'":"'鉄鉱石',''","'Nickel','ニッケル'":"'ニッケル',''","'Lithium','リチウム'":"'リチウム',''","'Aluminium','アルミ・ボーキサイト'":"'アルミ・ボーキサイト',''","'Recycled','二次資源'":"'二次資源',''","'Fertilizer','肥料資源'":"'肥料資源',''",
"'TRADING HUB'":"'販売網'",
"'02　WHAT WE DO｜PILLAR 1'":"'02｜独自価値　原料炭'","'02　WHAT WE DO｜PILLAR 2'":"'02｜独自価値　銅'","'OWNERSHIP'":"'出資構成'","'Mitsubishi Corp.'":"'三菱商事'",
"'Queensland'":"'豪州クイーンズランド州'",
"'Tier 1 assets'":"''","'Partnerships with majors'":"''","'Trading relationships'":"''","'New technology'":"''",
"'02　WHAT WE DO｜TRADING'":"'02｜独自価値　トレーディング'","'industries'":"''","'countries'":"''","'customers'":"''","'Functions'":"'5つの機能'",
"'Marketing &amp;<br>Procurement'":"'販売・調達'","'Carbon<br>Reduction'":"'脱炭素'","'Risk<br>Management'":"'リスク管理'","'Financing'":"'ファイナンス'","'Logistics'":"'物流'",
"'BUSINESS MODEL'":"'ビジネスモデル'","'MC Assets ＋ Third-party'":"''","'Stable supply'":"''","'Market intelligence'":"''","'Continuous value'":"''",
"'TRADING EXAMPLE'":"'トレーディング事業例'","'トレーディング事業例｜Copper Value Chain'":"'銅のバリューチェーン'","'Mining'":"''","'Smelting'":"''",
"'Base Demand'":"'基礎需要'","'Energy Transition'":"'エネルギー転換'","'AI &amp; Data Centers'":"'AI・データセンター'",
"'02　WHAT WE DO｜NEW TECHNOLOGY'":"'02｜独自価値　新技術'","'Mine','採掘'":"'','採掘'","'Process','選鉱・浸出'":"'','選鉱・浸出'","'Smelt &amp; Refine','製錬・精製'":"'','製錬・精製'","'End use','電化":"'','電化","'Recycle','リサイクル'":"'','リサイクル'",
"'COPPER｜STARTUP'":"'銅｜スタートアップ'","'RECYCLING'":"'リサイクル'",
"'03　WHY PARTNERS CHOOSE US'":"'03｜選ばれ続ける理由'",
"'Cultural affinity with the majors'":"''","'JV management capability'":"''","'Sound financial base'":"''","'Deep insight'":"''",
"'JOINT VENTURES WITH INDUSTRY LEADERS'":"'業界最大手とのJV実績'","'WHY PARTNERS VALUE US'":"'パートナーに評価される理由'",
"'Long-term perspective'":"''","'Risk sharing'":"''","'Integrated strength'":"''",
"'04　OUR VISION'":"'04｜何を実現するか'","'Demand shift'":"'需要の拡大'","'Supply constraints'":"'供給制約'","'Geopolitics'":"'地政学リスク'",
"'OUR COMMITMENT'":"'私たちの約束'","'“To contribute to a better society by providing a stable supply of high-quality mineral resources that society needs, in a sustainable way.”'":"''",
"'CONTACT'":"'お問い合わせ'","'Mitsubishi Corporation　Mineral Resources Group<br>2-3-1 Marunouchi, Chiyoda-ku, Tokyo 100-8086, Japan<br>www.mitsubishicorp.com'":"'三菱商事　金属資源グループ<br>〒100-8086 東京都千代田区丸の内2-3-1<br>www.mitsubishicorp.com'"}
for k,v in M.items():
    if k in s: s=s.replace(k,v)
    else: print('miss',k[:50])
s=s.replace("open('daiwari_v9.html','w')","open('daiwari_v15.html','w')")
open('daiwari_v15.py','w').write(s)
