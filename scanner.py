import random
import string

contrasena = input("Escribe una contraseña para analizar: ")
puntaje = 0

print("\n--- Análisis ---")

# Análisis que ya tienes
if len(contrasena) >= 8:
    puntaje += 2
    if len(contrasena) >= 12: puntaje += 2
if contrasena.lower() != contrasena: puntaje += 2
if any(c.isdigit() for c in contrasena): puntaje += 2
if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for c in contrasena): puntaje += 2

print(f"Calificación: {puntaje}/10")

# Nivel 3: Estimación
combinaciones = 0
if puntaje <= 4:
    print("⏱️ Tiempo para hackearla: < 1 hora")
else:
    print("⏱️ Tiempo para hackearla: Días / Años (depende)")

# Generador
print("\n--- Sugerencia segura generada para ti ---")
chars = string.ascii_letters + string.digits + "!@#$%"
sugerida = ''.join(random.choice(chars) for _ in range(14))
print(f"Usa algo así: {sugerida}")
print("Tip: Guarda esa en tu gestor de contraseñas, no en notepad.")