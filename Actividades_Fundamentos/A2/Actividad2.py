#Programa que calcula el perímetro i el área de un rectangulo dada su base i su altura

#Pediremos al usuario la base y la altura del rectangulo
base = int(input("Introduce la base del rectangulo: " ))
altura = int(input("Introduce la altura del rectangulo: "))

#Calcularemos el area
area = base * altura
#Calculamos perimetro (suma de todos sus lados) multiplicando por 2 el mismo valor anterior
perimetro = 2*base + 2*altura 

#Mostraremos por pantalla el area del rectangulo
print("Area del rectangulo es: " + str(area) + "cm")
print(f"El perimetro del rectangulo es: {perimetro} cm")