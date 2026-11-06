from PIL import Image, ImageDraw
import os
print("Iniciando...")
print("Carpeta:", os.getcwd())

img = Image.new('RGBA', (1024,1024), (10,10,11,255))
draw = ImageDraw.Draw(img)
draw.rectangle([50,50,974,974], outline=(0,229,255), width=8)
draw.rectangle([100,100,924,924], outline=(255,0,255), width=3)
draw.ellipse([200,150,824,750], fill=(40,40,50), outline=(0,229,255), width=12)
draw.ellipse([300,350,450,450], fill=(0,229,255))
draw.ellipse([574,350,724,450], fill=(0,229,255))
draw.rectangle([400,500,624,800], fill=(0,229,255))

ruta = os.path.join(os.getcwd(), "icon_epic.ico")
img.save(ruta, sizes=[(256,256),(128,128),(64,64),(32,32),(16,16)])
print(f"¡Listo! Creado: {ruta}")