# 8. Escriu un programa que generi un color aleatori en format RGB.
# Cada component (R, G, B) ha de ser un valor entre 0 i 255.
import random

#Generamos valores aleatorios para cada componente de color
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

#Mostramos el color generado
print(f"El color RGB generado es: ({r}, {g}, {b})")
