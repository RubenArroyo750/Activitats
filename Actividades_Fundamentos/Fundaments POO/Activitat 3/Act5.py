#5. Escriu un programa que demani a l'usuari una cadena i mostri el primer i l'últim caràcter, els dos en majúscules.

#Pedimos al usuario que genere una cadena
cadena = input("Introduce una cadena: ")

#Obtenemos el primer y último carácter para convertirlo en mayúsculas
primera = cadena[0].upper()
ultima = cadena[-1].upper()

#Mostramos los carácteres en mayúsculas
print("El primer carácter en mayúsculas es: ", primera)
print("El último carácter en mayúsculas es: ", ultima)

