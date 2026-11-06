from PIL import Image
import os, glob

archivos = glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.png") + glob.glob("*.webp")
path = max(archivos, key=os.path.getmtime)
print(f"Usando: {path}")

img = Image.open(path).convert("RGBA")
img = img.resize((2048,2048), Image.LANCZOS)
w, h = img.size
pix = img.load()

for y in range(h):
    for x in range(w):
        r,g,b,a = pix[x,y]
        # Conservar solo rojo fuerte y plateado brillante
        is_red = r > 95 and r > g+15 and r > b+10
        is_silver = r > 150 and g > 150 and b > 150 and abs(r-g)<20 and abs(r-b)<20
        is_dark_red = r > 65 and r < 130 and g < 65 and b < 75 and r > g+15 # borde rojo oscuro de la estrella
        is_black_edge = r < 35 and g < 35 and b < 35
        
        if is_red or is_silver or is_dark_red or is_black_edge:
            # Dejar, pero el negro solo si está cerca del centro (no fondo)
            continue
        else:
            pix[x,y] = (0,0,0,0)

bbox = img.getbbox()
img = img.crop(bbox)
img = img.resize((1024,1024), Image.LANCZOS)
img.save("icon_star_only_final.png", "PNG")
img.save("icon_star_only_final.ico", sizes=[(256,256),(128,128),(64,64),(32,32),(16,16)])
print(">>> LISTO V2: solo estrella, sin circulo <<<")