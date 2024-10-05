# Un alumne vol saber quin serà el seu qualificació final en la matèria de Algorismes.
#55% de la mitjana dels seus tres qualificacions parcials.
#30% de la qualificació de l'examen final.
#15% de la qualificació d'un treball final.

#Usuario introduce sus qualificaciones
parcial1 = int(input("Nota Parcial 1: "))
parcial2 = int(input("Nota Parcial 2: "))
parcial3 = int(input("Nota Parcial 3: "))

examenFinal = int(input("Nota Examen Final: "))

treballFinal = int(input("Nota Treball Final: "))

#Se suma los imputs de los parciales y se divide entre los 3
nParciales = (parcial1 + parcial2 + parcial3) / 3

#Se calcula el porcentaje indicado en cada qualificación
total = (nParciales * 0.30) + (examenFinal * 0.55) + (treballFinal * 0.15)

print("La nota final es de: ", total) #Muestra por pantalla del resultado


