#2. Escriu un programa que generi tres números aleatoris entre 1 i 100, els mostri i després en mostri la seva suma.

import random

#Generar 3 numeros aleatorios entre 1 i 100
#Primer numero
numero_aleatorio1 = random.randint(1, 100)
print("Numero aleatorio 1: ", numero_aleatorio1)
#Segundo numero
numero_aleatorio2 = random.randint(1, 100)
print("Numero aleatorio 2: ", numero_aleatorio2)
#Tercer numero
numero_aleatorio3 = random.randint(1, 100)
print("Numero aleatorio 3: ", numero_aleatorio3)

#Sumar total numeros aleatorios
suma_aleatorios = numero_aleatorio1 + numero_aleatorio2 + numero_aleatorio3
#Muestra por pantalla del resultado
print("La suma total de los numeros aleatorios es de: ", suma_aleatorios)
