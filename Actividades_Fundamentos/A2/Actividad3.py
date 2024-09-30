#Programa que calcula la hipotenusa de un triangulo rectangulo

#Introducimos los valores de los catetos del triangulo rectangulo
CatetoA = int(input("Introduce el cateto A del triangulo-reactangulo: "))
CatetoB = int(input("Introduce el cateto B del triangulo-reactangulo: "))
#import math

#hipotenusa = math.sqrt((CatetoA *2) + (CatetoB *2))
hipotenusa = ((CatetoA **2) + (CatetoB **2))** 0,5

print("La hipotenusa es: " + str(hipotenusa) +"")
