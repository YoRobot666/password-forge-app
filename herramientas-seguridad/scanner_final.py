# scanner_final.py - Tu primer programa de ciberseguridad
import random
import string

print("=== SCANNER DE CONTRASEÑAS v2.0 ===")

# 1. ENTRADA
contrasena = input("Escribe una contraseña de prueba: ")

# 2. LOGICA - Aquí es donde piensa
puntaje = 0
fallas = []

if len(contrasena) >= 8:
    puntaje += 2
else:
    fallas.append("Muy corta (menos de 8)")

if len(contrasena) >= 12:
    puntaje += 2

if contrasena.lower() != contrasena:
    puntaje += 2
else:
    fallas.append("Sin mayúsculas")

if any(c.isdigit() for c in contrasena):
    puntaje += 2
else:
    fallas.append("Sin números")

if any(c in "!@#$%*_-" for c in contrasena):
    puntaje += 2
else:
    fallas.append("Sin símbolos")

# 3. SALIDA
print(f"\nTu calificación: {puntaje}/10")

if fallas:
    print("Para mejorar:", ", ".join(fallas))

# Extra: te genera una segura
segura = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%") for _ in range(16))
print(f"\nUna contraseña 10/10 sería algo como: {segura}")
print("Guárdala en tu gestor, no en un post-it.")