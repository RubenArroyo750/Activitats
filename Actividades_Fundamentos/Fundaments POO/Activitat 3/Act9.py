# 9. Escriu un programa que mesuri quant temps triga en executar-se una operació,
# com per exemple calcular l'arrel quadrada de 3 números diferents.
# Utilitza datetime.now() per obtenir el temps abans i després de l'operació,
# i resta’ls per calcular el temps total d'execució.
from datetime import datetime
import math, time

# Definim tres números per calcular l'arrel quadrada
num1 = 16
num2 = 25
num3 = 36

# Obtenim el temps abans de l'operació
temps_inicial = datetime.now()

# Càlcul de l'arrel quadrada dels tres números
arrel1 = math.sqrt(num1)
arrel2 = math.sqrt(num2)
arrel3 = math.sqrt(num3)
time.sleep(3) # Sleep for 3 seconds

# Obtenim el temps després de l'operació
temps_final = datetime.now()

# Calculem el temps total d'execució
temps_total = temps_final - temps_inicial

# Mostrem els resultats
print(f"L'arrel quadrada de {num1} és: {arrel1}")
print(f"L'arrel quadrada de {num2} és: {arrel2}")
print(f"L'arrel quadrada de {num3} és: {arrel3}")
print(f"El temps total d'execució és: {temps_total.total_seconds()} segons")
