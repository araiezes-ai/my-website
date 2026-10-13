# 表紙 v28：L1フラット × 3色（赤／グラファイト／カッパー）
exec(open('cover27.py').read().split('P=[(front(UPC(False)')[0])
COLS=[('赤','#a01d30','#5e0a14'),('グラファイト','#3b4249','#1b1f24'),('カッパー','#a85a33','#5a2a13')]
P=[]
for nm,m,d in COLS:
    MAIN,DARK=m,d
    P.append((front(UPC(False),m),f'L1_上昇_フラット_{nm}'))
open('cover28.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS2+'</style>'+''.join(p for p,_ in P))
import json; json.dump([n for _,n in P],open('cover28_names.json','w'),ensure_ascii=False)
