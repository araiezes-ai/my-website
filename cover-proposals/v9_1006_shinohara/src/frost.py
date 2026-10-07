import numpy as np
from PIL import Image, ImageFilter
def fbm(n,seed=1,oct=6):
    rng=np.random.default_rng(seed); out=np.zeros((n,n)); amp=1; tot=0
    for o in range(oct):
        s=max(2,2**(o+2)); g=rng.random((s,s))
        im=Image.fromarray((g*255).astype(np.uint8)).resize((n,n),Image.BICUBIC)
        out+=np.asarray(im)/255*amp; tot+=amp; amp*=.55
    out/=tot; return (out-out.min())/(out.max()-out.min())
def sphere(N=900,seed=3):
    y,x=np.mgrid[0:N,0:N]; u=(x+.5)/N*2-1; v=1-(y+.5)/N*2; r2=u*u+v*v; ins=r2<1
    z=np.sqrt(np.clip(1-r2,0,1)); L=np.array([-.5,.6,.62]); L/=np.linalg.norm(L)
    d=np.clip(u*L[0]+v*L[1]+z*L[2],0,1)
    base=np.stack([np.full_like(u,c) for c in (150,186,218)],-1)
    lite=np.array([236,244,250.]); col=base*(1-d[...,None]*.55)+lite*d[...,None]*.55
    col=col*(1-(1-z)[...,None]**2*.25)+np.array([120,156,192.])*(1-z)[...,None]**2*.25
    nz=fbm(N,seed); cl=np.clip((nz-.36)*2.6,0,1)**.8
    col=col*(1-cl[...,None]*.88)+252*cl[...,None]*.88
    rim=np.clip((r2-.94)/.06,0,1); col=col*(1-rim[...,None]*.6)+np.array([240,246,252.])*rim[...,None]*.6
    a=np.clip((1-np.sqrt(r2))*N*.5,0,1)*255
    img=np.dstack([np.clip(col,0,255),a]).astype(np.uint8)
    return Image.fromarray(img,'RGBA').filter(ImageFilter.GaussianBlur(.6))
def frost_globe(path,seed=5,k=.55):
    im=Image.open(path).convert('RGBA'); a=np.asarray(im).astype(float); N=a.shape[0]
    nz=fbm(N,seed); cl=np.clip((nz-.35)*1.8,0,1)*k+.18
    rgb=a[...,:3]; rgb=rgb*(1-cl[...,None])+255*cl[...,None]
    # cool tint
    rgb=rgb*np.array([.97,.99,1.0])
    out=np.dstack([np.clip(rgb,0,255),a[...,3]]).astype(np.uint8)
    return Image.fromarray(out,'RGBA')
if __name__=='__main__':
    sphere(900,3).save('v9/sph1.png'); sphere(900,8).save('v9/sph2.png'); sphere(900,13).save('v9/sph3.png')
    frost_globe('v8/gl_-28_-8_-10_1700_0.34.png',5,.7).save('v9/fg_front.png')
    frost_globe('v8/gl_138_-14_6_1700_0.2.png',7,.6).save('v9/fg_back.png')
    from PIL import Image as I
    s=I.new('RGB',(1800,600),'white')
    for i,f in enumerate(['v9/sph1.png','v9/fg_front.png','v9/fg_back.png']):
        t=I.open(f); t.thumbnail((580,580)); s.paste(t,(i*600,0),t)
    s.save('v9/frost_chk.png')
