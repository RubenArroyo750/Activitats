#15. Donades dues variables numèriques A i B, que l'usuari ha de teclejar, es demana realitzar un algoritme que intercanviï els valors de 
#les dues variables i mostri que fa valen a al final les dues variables.

a = int(input("Valor A: "))
b = int(input("Valor B: "))

print("Valor A: " + str(a) + ", Valor B: " + str(b))

#Valor auxiliar para hacer el intercambio
aux = b
b = a
a = b
print("Intercambio:")
print(f"1: {a}, 2: {b}")