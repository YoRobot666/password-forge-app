from PIL import Image, ImageDraw

W=1024
img=Image.new('RGBA',(W,W),(0,0,0,255))
draw=ImageDraw.Draw(img)

# Craneo Punisher blanco hueso
# Cabeza
draw.ellipse([180,50,844,620], fill=(245,245,240), outline=(255,255,255), width=4)
# Ojos inclinados punisher
draw.polygon([(210,400),(450,480),(430,520),(200,480)], fill=(0,0,0))
draw.polygon([(814,400),(574,480),(594,520),(824,480)], fill=(0,0,0))
# Nariz
draw.polygon([(480,520),(510,520),(530,650),(500,680),(460,650)], fill=(0,0,0))
draw.polygon([(544,520),(514,520),(494,650),(524,680),(564,650)], fill=(0,0,0))

# Mandibula larga punisher
draw.rectangle([380,580,644,980], fill=(245,245,240))
# Dientes frontales
for i,x in enumerate([380,430,480,530,580]):
    if i==2: continue
    draw.rectangle([x,600,x+45,980], fill=(245,245,240), outline=(0,0,0), width=6)

# Colmillos largos
draw.polygon([(350,600),(380,600),(320,880)], fill=(245,245,240), outline=(0,0,0), width=5)
draw.polygon([(674,600),(644,600),(704,880)], fill=(245,245,240), outline=(0,0,0), width=5)

# Candado central (el que muerde)
draw.rounded_rectangle([420,680,604,890], radius=15, fill=(230,230,230), outline=(0,0,0), width=8)
# arco candado
draw.arc([440,620,584,740], 180, 0, fill=(230,230,230), width=18)
draw.arc([440,620,584,740], 180, 0, fill=(0,0,0), width=4)
# ojo cerradura
draw.ellipse([485,760,539,810], fill=(0,0,0))
draw.rectangle([495,800,529,860], fill=(0,0,0))

# Cicatrices tipo punisher
draw.line([(300,200),(380,280)], fill=(0,0,0), width=4)
draw.line([(320,190),(400,270)], fill=(0,0,0), width=4)

img.save('icon_punisher.ico', sizes=[(256,256),(128,128),(64,64),(32,32),(16,16)])
print("icon_punisher.ico PUNISHER creado - brutal")