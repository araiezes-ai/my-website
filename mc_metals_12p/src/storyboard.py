# 全12ページのサムネイル・ページ番号・英語見出し・1行メッセージ（A3横）
import os, base64, glob, subprocess, sys
R=os.path.join(os.path.dirname(__file__),'_render'); D=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','deliverables'))
fs=sorted(glob.glob(R+'/thumb/t-*.png'))
rows=[('P1','METAL RESOURCES GROUP','表紙。3本のライン（投資・トレーディング・新技術）が前へ進み、一点で上へ伸びる。'),
('P2','Metals shape the way we live.','暮らしと産業を支える金属。需要は高まり、供給は難しくなっている。'),
('P3','Strength to Hold. Power to Connect.','持つ力とつなぐ力。存在意義と目次（P4／6／8／10／11）。'),
('P4','Who We Are','三綱領と総合力。7つの営業グループの中で、金属資源グループへ線がつながる。'),
('P5','The core that has carried us.','中核グループとしてのミッション、長年の貢献、先見性の歩み。'),
('P6','Our Distinctive Strength','川上から需要家までのバリューチェーンに、投資（HOLD）とトレーディング（CONNECT）が重なる。'),
('P7','Our Distinctive Strength','市場情報の戻り・新技術・長期の積み重ね。その結果が主力3事業（→P8）。'),
('P8','Our Businesses & Innovation','原料炭（50:50のBMA・高品位への厳選）と銅（世界上位鉱山への早期参画）。'),
('P9','Our Businesses & Innovation','トレーディング（RtMが資源と市場をつなぐ）と、新技術（銅バリューチェーン上のCiDRA／Jetti／DESCycle）。'),
('P10','Partner of Choice','4つの強みがパートナーの価値に変わり、協業が次の協業を生む。'),
('P11','Supporting Society with the Resources It Needs','社会の課題 → 私たちのアクション → 持続可能で豊かな社会。'),
('P12','Back Cover','表紙のラインを受ける裏表紙。名称・所在地・URL（要確認）。')]
cells=''
for f,(n,e,m) in zip(fs,rows):
    b=base64.b64encode(open(f,'rb').read()).decode()
    cells+=f'<div class="c"><img src="data:image/png;base64,{b}"><div class="n">{n}</div><div class="e">{e}</div><div class="m">{m}</div></div>'
html=f'''<!doctype html><meta charset=utf-8><style>@page{{size:420mm 297mm;margin:0}}body{{margin:0;font-family:"Noto Sans CJK JP";color:#121519}}
.pg{{width:420mm;height:297mm;padding:12mm 14mm;box-sizing:border-box}}h1{{font:600 20pt "Inter Tight";margin:0 0 1mm}}.s{{font-size:8pt;color:#7d838a;margin-bottom:5mm}}
.g{{display:grid;grid-template-columns:repeat(6,1fr);gap:5mm 6mm}}.c img{{width:100%;border:.3mm solid #cfd3d7;display:block}}
.n{{font:600 9pt "Inter";color:#9c7442;margin-top:1.5mm}}.e{{font:600 8pt "Inter Tight";margin-top:.5mm}}.m{{font-size:6.6pt;color:#3d4249;line-height:1.5;margin-top:.8mm}}</style>
<div class="pg"><h1>MC Metal Resources Group — 12P Storyboard</h1><div class="s">三菱商事 金属資源グループ 会社案内（日本語版・A4縦12ページ）｜大見出しは英語、本文は日本語</div><div class="g">{cells}</div></div>'''
open(D+'/_sb.html','w').write(html)
subprocess.run(['/opt/pw-browsers/chromium-1194/chrome-linux/chrome','--headless','--no-sandbox','--no-pdf-header-footer','--print-to-pdf='+D+'/MC_Metals_12P_Storyboard.pdf',D+'/_sb.html'],stderr=subprocess.DEVNULL)
os.remove(D+'/_sb.html'); print('storyboard')
