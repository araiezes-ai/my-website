import re
s=open('daiwari_v14.py').read()
i=s.index("# ============ P02-03"); head,body=s[:i],s[i:]
M={'Cities':'都市','Steel · Copper · Aluminium':'鉄・銅・アルミ','Mobility':'モビリティ','Steel · Copper · Lithium':'鉄・銅・リチウム','Railways':'鉄道','Steel · Copper':'鉄・銅','Renewables':'再生可能エネルギー','Copper · Steel':'銅・鉄','Power grids':'送電網','Copper · Aluminium':'銅・アルミ','Devices':'デバイス','Copper · Lithium · Nickel':'銅・リチウム・ニッケル','Metals':'金属','The materials behind modern life':'現代の暮らしを支える素材','Smelting &amp; refining':'製錬・精製','Seaborne trade':'海上輸送','Copper cathodes':'銅地金',
'INTRODUCTION':'導入','DEMAND vs SUPPLY':'需要と供給','Demand':'需要','Supply':'供給','GAP':'ギャップ','Today':'現在','Future':'将来','CORE MESSAGE':'コアメッセージ',
'Who We Are':'我々は何者か','Our Strengths':'資産の強み','Coal &amp; Copper':'原料炭と銅','Resources to Value':'資源から価値へ','Partnerships':'パートナーシップ','Value Chain':'バリューチェーン','CONTENTS':'目次',
'01 · Who we are':'01｜我々は何者か','GROUP MISSION':'グループミッション','To contribute to a better society by providing a stable supply of high-quality mineral resources in a sustainable way.':'',
'ORGANIZATION':'組織','Steelmaking Raw Materials':'','Critical Minerals':'','Mineral Resources Trading':'','THREE CORPORATE PRINCIPLES':'三綱領',
'Corporate Responsibility to Society':'しょきほうこう','Integrity and Fairness':'しょじこうめい','Global Understanding through Business':'りつぎょうぼうえき',
'02 · Our strengths':'02｜資産の強み','Metallurgical Coal':'原料炭','Bowen Basin, Australia':'豪州 ボーエン・ベースン','Copper':'銅','Chile · Peru':'チリ・ペルー','USA':'米国','of 5':'5鉱山中','share':'シェア','years':'年以上',
'OUR JOURNEY｜FORESIGHT':'歩み｜先見性','02 · Metallurgical coal':'02｜原料炭','02 · Copper':'02｜銅','OWNERSHIP':'出資構成','Since':'設立','Location':'所在地','Assets':'保有資産','Mine life':'炭鉱寿命','Seaborne share':'海上輸出シェア',
'EARLY MOVER':'主要鉱山への参画','Chile':'チリ','Peru':'ペルー','Chile · 開発中':'チリ・開発中','USA · 開発中':'米国・開発中','COPPER PRODUCTION 2025':'会社別 世界銅生産量（2025年）','Mitsubishi Corp.':'三菱商事','Mitsubishi':'三菱商事',
'MARKET STRUCTURE':'市場構造','Metallurgical coal':'原料炭','03 · From resources to value':'03｜資源から価値へ',
'Iron Ore':'','Nickel':'','Lithium':'','Bauxite · Aluminium':'','Fertilizer':'','Recycled':'',
'NEW TECHNOLOGY ALONG THE COPPER CHAIN':'銅のバリューチェーンと新技術','Mine':'採掘','Concentrate':'銅精鉱','Cathode':'銅地金','End use':'最終用途','Recycle':'リサイクル',
'STARTUP｜選鉱':'スタートアップ｜選鉱','STARTUP｜浸出':'スタートアップ｜浸出','RECYCLING｜回収':'リサイクル｜回収','TRADING｜100%子会社':'トレーディング｜100%子会社','Copper mine':'銅鉱山',
'04 · Global partnerships':'04｜パートナーシップ','Cultural affinity':'','JV management':'','Financial strength':'','Deep insight':'','TRADING NETWORK':'販売網',
'Singapore（拠点集約）・Japan・India・China・USA・UK・UAE・Indonesia・Thailand・Chile':'シンガポール（拠点集約）・日本・インド・中国・米国・英国・UAE・インドネシア・タイ・チリ',
'JOINT VENTURES':'JV実績','WHY PARTNERS VALUE US':'パートナーに評価される理由','Long-term view':'','Risk sharing':'','Integrated strength':'','industries':'','countries':'','customers':'',
'05 · Integrated value chain':'05｜バリューチェーン全体像','UPSTREAM':'川上','MIDSTREAM':'川中','DOWNSTREAM':'川下','Steel':'','Non-ferrous':'','THE VIRTUOUS CYCLE':'好循環','Invest':'投資','⇄ Trade':'⇄ 販売','RtM FUNCTIONS':'RtMの機能',
'Marketing &amp; Procurement':'','Logistics':'','Financing':'','Risk Management':'','Carbon Reduction':'','Our commitment':'私たちの約束',
'Mitsubishi Corporation　Mineral Resources Group':'三菱商事　金属資源グループ','2-3-1 Marunouchi, Chiyoda-ku, Tokyo 100-8086, Japan　|　www.mitsubishicorp.com':'〒100-8086 東京都千代田区丸の内2-3-1｜www.mitsubishicorp.com',
'Port &amp; rail':'港湾・鉄道','Seaborne logistics':'海上輸送','Operations':'操業','Group CEO':'グループCEO'}
n=0
for k,v in M.items():
    q="'"+k+"'"
    if q in body: n+=body.count(q); body=body.replace(q,"'"+v+"'")
    else: print('miss:',k)
for a,b in [('>INVESTMENT<','>投資<'),('>TRADING (RtM)<','>トレーディング（RtM）<'),('"Investment" if i<2 else "Trading"','"投資" if i<2 else "トレーディング"'),('e or "TRADING · RtM"','e or "トレーディング（RtM）"'),('TRADING · RtM','トレーディング（RtM）')]:
    if a in body: body=body.replace(a,b)
    else: print('miss raw:',a)
open('daiwari_v14.py','w').write(head+body)
print('replaced',n)
