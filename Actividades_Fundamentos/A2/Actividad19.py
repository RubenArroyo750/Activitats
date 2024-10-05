# 19. Escriure un algoritme per calcular la nota final d'un estudiant, considerant que: per cada resposta correcta 5 punts, per una incorrecta -1 i per respostes en blanc 0. Imprimeix el resultat obtingut per l'estudiant.

respCorrecte = int(input("Correctes: "))
respIncorrecte = int(input("Incorrectes: "))
respBlanc = int(input("Blanc: "))

nota = respCorrecte * 5 + respIncorrecte * (-1) 
print(nota)