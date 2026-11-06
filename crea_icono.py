from PIL import Image, ImageDraw
import math
size=1024
img=Image.new("RGBA",(size,size),(0,0,0,0))
draw=ImageDraw.Draw(img)
cx,cy=size//2,size//2
def star(cx,cy,r):
    pts=[]
    for i in range(10):
        ang=math.radians(-90+i*36)
        rad=r if i%2==0 else r*0.4
        pts.append((cx+math.cos(ang)*rad, cy+math.sin(ang)*rad))
    return pts
draw.polygon(star(cx,cy,480), fill=(0,0,0,255))
draw.polygon(star(cx,cy,462), fill=(200,200,200,255))
draw.polygon(star(cx,cy,435), fill=(235,235,235,255))
draw.polygon(star(cx,cy,395), fill=(0,0,0,255))
draw.polygon(star(cx,cy,280), fill=(230,0,0,255))
img.save("icon_star_only_final.ico", sizes=[(256,256),(128,128),(64,64),(32,32),(16,16)])
print("ICO CREADO")
