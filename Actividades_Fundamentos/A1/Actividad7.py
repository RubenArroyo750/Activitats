#Programa que muestra una frase en una sola línea

#Crearemos cada palabra y la guardaremos en varias variables
Palabra1 = "La"
Palabra2 = "Casa"
Palabra3 = "Blanca"
Palabra4 = "guarda"
Palabra5 = "un"
Palabra6 = "secret"

#Mostraremos por pantalla la frase completa con espacios separados en blanco
print(Palabra1, Palabra2, Palabra3, Palabra4, Palabra5, Palabra6, sep=" ")



#V2 CORRECIÓN
cadena1 =  "La casa blanca"
cadena2 = "guarda un secret"

print(cadena1, cadena2)           # Separador per defecte, " "
print(cadena1, cadena2, sep="/")  # Canviem el separador
print(cadena1, cadena2, end=".")  # Canviem el caràcter final