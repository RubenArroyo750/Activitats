# 4. Escriu un programa que generi cinc números decimals aleatoris entre 0 i 1,
# i els mostri en la mateixa línia, separats per guions, no es poden utilitzar llistes.
import random

#Generamos cinco numeros decimales aleatorios
num1 = random.random()
num2 = random.random()
num3 = random.random()
num4 = random.random()
num5 = random.random()

#Mostramos los numeros separados por guiones
print(f"{num1} - {num2} - {num3} - {num4} - {num5}")

#Mostramos los numeros separados por guiones con sep
print(num1, num2, num3, num4, num5, sep=" - ")