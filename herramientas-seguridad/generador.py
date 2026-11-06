# generador.py - Tu generador personal
import random
import string

print("=== GENERADOR DE CONTRASEÑAS ===")

# TÚ eliges la longitud
try:
    longitud = int(input("¿De cuántos caracteres la quieres? (ej: 12, 16, 20): "))
except:
    print("Pon un número, bro. Usaré 16 por defecto.")
    longitud = 16

if longitud < 8:
    print("⚠️ Muy corta, la subo a 8 mínimo por seguridad.")
    longitud = 8

# Preguntas extras (opcional pero queda pro)
usar_mayus = input("¿Con mayúsculas? (s/n): ").lower() != 'n'
usar_numeros = input("¿Con números? (s/n): ").lower() != 'n'
usar_simbolos = input("¿Con símbolos? (s/n): ").lower() != 'n'

# Armamos el alfabeto
caracteres = string.ascii_lowercase
if usar_mayus:
    caracteres += string.ascii_uppercase
if usar_numeros:
    caracteres += string.digits
if usar_simbolos:
    caracteres += "!@#$%*_-+"

# Generamos
contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))

print("\n------------------------------")
print(f"Tu contraseña de {longitud} caracteres:")
print(f"👉 {contrasena}")
print("------------------------------")
print("Copia esa y guárdala en tu gestor.")