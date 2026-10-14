#!/bin/sh
# PPTX → PDF（LibreOffice）→ PNG、見開き合成
set -e
D=$(cd "$(dirname "$0")/../deliverables" && pwd); W=$(mktemp -d)
cp "$D/MC_Metals_12P_JP_Editable.pptx" $W/main.pptx; cp "$D/MC_Metals_Design_Alternatives.pptx" $W/alt.pptx
(cd $W && soffice --headless --convert-to pdf main.pptx >/dev/null 2>&1 && soffice --headless --convert-to pdf alt.pptx >/dev/null 2>&1)
cp $W/main.pdf "$D/MC_Metals_12P_Proof.pdf"; cp $W/alt.pdf "$D/MC_Metals_Design_Alternatives.pdf"
mkdir -p "$D/../src/_render"; rm -f "$D/../src/_render"/*.png
pdftoppm -r ${1:-60} -png "$D/MC_Metals_12P_Proof.pdf" "$D/../src/_render/p"
pdftoppm -r ${2:-40} -png "$D/MC_Metals_Design_Alternatives.pdf" "$D/../src/_render/alt"
echo rendered
