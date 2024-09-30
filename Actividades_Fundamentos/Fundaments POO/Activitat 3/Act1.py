#Escriu un programa que demani a l'usuari dues dates específiques en format YYYY-MM-D. 
#Mostra la diferència en dies entre aquestes dues dates.

#Importem llibreria datetime
from datetime import datetime

#Demanem a l'usuari que introdueixi les dates
data1_str = input("Introduce una fecha en el formato (YYYY-MM-D): ")
data2_str = input("Introduce otra fecha en el formato (YYYY-MM-D): ")

#Conversió de les dades de cadena a objecte datetime
data1 = datetime.strptime(data1_str, "%Y-%m-%d")
data2 = datetime.strptime(data2_str, "%Y-%m-%d")

#Calcul diferencia en dies
diferencia = abs((data2 - data1).days)
print("La diferència entre les dues dates és de ", diferencia, " dies.")


