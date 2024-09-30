#Programa que dado dos nombres, muestra la suma, resta, división y multiplicación de los dos

#Le preguntamos al usuario que indique dos nombres
numero1 = int(input("Escribe un numero: "))
numero2 = int(input("Escribe un segundo numero: "))

#Calculos de los nombres
suma = numero1 + numero2
resta = numero1 - numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2

#Mostraremos por pantalla los calculos
print("La suma de los dos nombres es: " + str(suma) +"!")
print("La resta de los dos nombres es: " + str(resta) + "!")
print("La division de los dos nombres es: " + str(division) + "!")
print("La multiplicación de los dos nombres es: " + str(multiplicacion) + "!")

print("Las operaciones son " + str(suma), str(resta), str(division), str(multiplicacion), sep= ", ") #Opcion 2
