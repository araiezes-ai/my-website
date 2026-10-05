import sys; sys.path.insert(0,'/home/user/my-website/cover-proposals/v9_art/src')
import glassglobe2 as G
job=sys.argv[1]
if job=='flatwide': G.render_flat(3200,int(3200*138/360),50,410,80,-58,ss=1.4).save('v9/flat_wide.png')
elif job=='flatstd': G.render_flat(2600,int(2600*138/360),-170,190,80,-58,ss=1.4).save('v9/flat_std.png')
elif job=='orb': G.render(500,0,0,0,land_on=False,japan=False).save('v9/orb.png')
elif '_' in job:
    lon,lat,roll,N=map(float,job.split('_')); G.render(int(N),lon,lat,roll,ss=1.5 if N>1200 else 2).save(f'v9/gl_{job}.png')
if job=='aus': G.render_flat(800,int(800*34/43),112,155,-10,-44,ss=2).save('v9/aus.png')
if job=='andes': G.render_flat(600,int(600*34/30),-84,-54,-3,-37,ss=2).save('v9/andes.png')
