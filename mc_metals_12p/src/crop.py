# crop.py SRC OUT W_MM H_MM FX FY  — 指定比率で切り抜き、JPEG化（300dpi相当まで）
import sys
from PIL import Image
src,out,w,h,fx,fy=sys.argv[1],sys.argv[2],float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6])
im=Image.open(src).convert('RGB'); W,H=im.size; ar=w/h
if W/H>ar: cw,ch=int(H*ar),H
else: cw,ch=W,int(W/ar)
x=int(max(0,min(W-cw,fx*W-cw/2))); y=int(max(0,min(H-ch,fy*H-ch/2)))
im=im.crop((x,y,x+cw,y+ch))
mx=int(w/25.4*300)
if im.size[0]>mx: im=im.resize((mx,int(mx/ar)),Image.LANCZOS)
im.save(out,'JPEG',quality=86)
