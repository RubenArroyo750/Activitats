#16. Dos vehicles viatgen a diferents velocitats (v1 i v2) i estan distanciats per una distància d. 
#El que està darrere viatja a una velocitat més gran. Es demana fer un algoritme per ingressar la distància entre els dos vehicles (km) i les seves respectives velocitats (km / h) i amb això determinar i mostrar en què temps (minuts) arribarà el vehicle més ràpid a l'altre.
# Ingressar dades
d = float(input("Distància entre els vehicles (en km): "))
v1 = float(input("Velocitat del vehicle més lent (en km/h): "))
v2 = float(input("Velocitat del vehicle més ràpid (en km/h): "))

# Calcular el temps en hores
t_horas = d / (v2 - v1)

# Convertir el temps a minuts
t_minuts = t_horas * 60

# Mostrar el resultat
print(f"El vehicle més ràpid arribarà al vehicle més lent en {t_minuts:.2f} minuts.")