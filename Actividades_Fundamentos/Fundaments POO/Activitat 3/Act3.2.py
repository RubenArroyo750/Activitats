# 3. Escriu un programa que generi una hora específica a l'atzar (per exemple, les 10:30:00)
# i mostri quanta estona ha passat fins ara, en hores, minuts i segons.
from datetime import datetime
import random

#Generamos hora, minutos y segundos aleatorios
hores = random.randint(0,23)
minuts = random.randint(0,59)
segons = random.randint(0,59)

#Creamos objeto datetime con la hora aleatoria
hora_aleatoria = datetime.now().replace(hour=hores, minute=minuts, second=segons, microsecond=0)

#Obtenemos hora actual
ara = datetime.now()

#Calculamos la diferencia en segundos
diferencia = (ara - hora_aleatoria).total_seconds()

#Convertimos la diferencia a horas, minutos y segundos
hores_passades = int(diferencia // 3600)
minuts_passats = int((diferencia % 3600) // 60)
segons_passats = int(diferencia % 60)

# Mostrem els resultats
print(f"Hora aleatòria generada: {hores:02}:{minuts:02}:{segons:02}")
print(f"Diferència fins ara: {hores_passades} hores, {minuts_passats} minuts i {segons_passats} segons.")