#6. Calcular la mitjana de tres nombres entrats per teclat.

#Se introducen los numeros
numeroA = int(input("Introduce el primer numero para calcular la media: "))
numeroB = int(input("Introduce el segundo numero para calcular la media: "))
numeroC = int(input("Introduce el tercer numero para calcular la media: "))

#O se puede hacer de esta manera:
# n1, n2, n3 = int(input("N1: ")), int(input("N2: ")), int(input("N3: "))

media = (numeroA+numeroB+numeroC)/3 #Se suman los tres numeros y se divide entre 3 para hacer la media

#Muestra por pantalla
print("La media de los tres numeros es: " + str(media) + "")


