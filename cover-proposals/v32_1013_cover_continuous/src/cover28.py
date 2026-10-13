# 表紙 v28：L1フラット × 3色（赤／グラファイト／カッパー）
exec(open('cover27.py').read().split('P=[(front(UPC(False)')[0])
# (名前, 帯, 濃い縁, 帯に重ねる半透明の面, 不透明度, 合成, 背景の淡い面)
COLS=[('赤','#a3122a','#4e0510','#1f252c',.38,'multiply','#eceef1'),          # 赤×グラファイトの影。背景はクールグレー
      ('グラファイト','#2b323a','#0f1216','#6f8aa3',.55,'screen','#e6ebf0'),    # 黒鉄×スチールブルーの光。背景は青みのグレー
      ('カッパー','#b5561f','#4a1d07','#2a1a12',.34,'multiply','#f0ebe6')]       # 銅×ブロンズの影。背景は温かいグレー
P=[]
for nm,m,d,pa,po,pb,bg2 in COLS:
    MAIN,DARK,PA,PA_OP,PA_BL,PB=m,d,pa,po,pb,bg2
    P.append((front(UPC(False),m),f'L1_上昇_フラット_{nm}'))
open('cover28.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS2+'</style>'+''.join(p for p,_ in P))
import json; json.dump([n for _,n in P],open('cover28_names.json','w'),ensure_ascii=False)
