#3.Escriu un programa que generi una hora específica a l'atzar (per exemple, les 10:30:00) 
#i mostri quanta estona ha passat fins ara, en hores, minuts i segons.

#Importamos random y datetime
import random
import datetime

#Generar hora al azar
hora_aleatoria = random.randint(00, 24) #Hora aleatoria entre 00 y 24h.
minutos_aleatorios = random.randint(0, 59) #Minutos aleatorios entre 0 y 59m.

hora_str = datetime.strptime(hora_aleatoria, minutos_aleatorios, "%H:%M:%S")
print(hora_str)

