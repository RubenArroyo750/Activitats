# 11. Demana a l'usuari dos nombres i mostra la "distància" entre ells (el valor absolut de la seva diferència, de manera que el resultat sigui sempre positiu).

#Usuario input
num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))

#Se resta la distancia entre el numero1 y 2 restandolos
distancia = num1 - num2

#Se calcula el valor absoluto de la diferencia para que el resultado sea positivo
absoluto = abs(distancia)

#Muestra por pantalla
print(absoluto)