# Un alumne vol saber quin serà el seu qualificació final en la matèria de Algorismes.
#55% de la mitjana dels seus tres qualificacions parcials.
#30% de la qualificació de l'examen final.
#15% de la qualificació d'un treball final.
pesPercials = 0.55
pesExamenFinal = 0.3
pesTreballFinal = 0.15


parcial1 = float(input("Nota Parcial 1: "))
parcial2 = float(input("Nota Parcial 2: "))
parcial3 = float(input("Nota Parcial 3: "))
examenFinal = float(input("Nota Examen Final: "))
treballFinal = float(input("Nota Treball Final: "))

mitjanaParcials = ((parcial1 + parcial2 + parcial3) /3) * pesPercials
notaExamenFinal = mitjanaParcials + (examenFinal * pesExamenFinal) + (treballFinal * pesTreballFinal)


