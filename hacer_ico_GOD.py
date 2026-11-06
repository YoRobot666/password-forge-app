from PIL import Image, ImageDraw
import math

W = 1024
img = Image.new('RGBA', (W,W), (8,8,10,255))
draw = ImageDraw.Draw(img)

# Fondo glow magenta
for r in range(400, 100, -20):
    alpha = int((400-r)*0.3)
    draw.ellipse([W//2-r, W//2-r+100, W//2+r, W//2+r+300], outline=(255,0,180, alpha), width=3)

# Craneo base
draw.ellipse([150,80,874,700], fill=(15,30,40), outline=(0,229,255), width=10)
draw.ellipse([120,200,300,450], fill=(5,5,8)) # hueco lateral
draw.ellipse([724,200,904,450], fill=(5,5,8))

# Ojos plasma
draw.ellipse([220,380,460,580], fill=(0,0,0), outline=(255,0,200), width=6)
draw.ellipse([564,380,804,580], fill=(0,0,0), outline=(255,0,200), width=6)
# brillo interno ojos
draw.ellipse([280,430,400,530], fill=(0,255,255))
draw.ellipse([624,430,744,530], fill=(0,255,255))
draw.ellipse([300,450,380,510], fill=(255,255,255))
draw.ellipse([644,450,724,510], fill=(255,255,255))

# Circuit lines
for i in range(200, 800, 60):
    draw.line([(i,120),(i,350)], fill=(0,229,255,120), width=2)
    draw.rectangle([i-15,100,i+15,130], outline=(0,229,255), width=2)

# Dientes / mandibula
draw.ellipse([200,550,824,950], fill=(10,25,35), outline=(0,229,255), width=8)
# dientes
for x in range(260, 770, 50):
    draw.rectangle([x,700,x+30,800], fill=(180,220,230), outline=(0,229,255), width=2)

# CANDADO GIGANTE MAGENTA (el que muerde)
# cuerpo candado
draw.rounded_rectangle([380,780,644,970], radius=20, fill=(40,0,40), outline=(255,0,200), width=8)
# arco
draw.arc([400,680,624,850], 180, 0, fill=(255,0,200), width=12)
# ojo cerradura
draw.ellipse([470,850,554,920], fill=(0,0,0), outline=(0,255,255), width=4)
draw.rectangle([490,910,534,950], fill=(0,255,255))

img.save('icon_god.ico', sizes=[(256,256),(128,128),(64,64),(32,32),(16,16)])
print("icon_god.ico GOD creado")