# 再生成手順
1. `npm i pptxgenjs@4` （node_modules）
2. `node build.js` → deliverables/MC_Metals_12P_JP_Editable.pptx・MC_Metals_Design_Alternatives.pptx
3. `./render.sh 150 90` → Proof PDF／比較案PDF／PNG（LibreOffice）
4. `python3 review.py` → A3見開き俯瞰版、`python3 storyboard.py` → 台割サムネイル
- lib.js：見開き座標(mm)で描き、A4左右スライドへ振り分ける描画ライブラリ
- pages.js：各ページのデザイン（P4–5／P6–7はA・B案）
- crop.py：写真の切り抜き（assets/ → assets/_crop/）
