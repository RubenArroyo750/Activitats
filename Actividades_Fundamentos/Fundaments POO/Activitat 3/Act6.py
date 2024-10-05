#6. Escriu un programa que generi una cadena de 3 caràcters que inclogui lletres (majúscules i minúscules) i números aleatoris.
import random
import string

#Creamos conjunto de carácteres que incluya letras y digitos
caracteres = string.ascii_letters + string.digits

#Generamos una cadena aleatoria de 8 carácteres
caracter1 = random.choice(caracteres)
caracter2 = random.choice(caracteres)
caracter3 = random.choice(caracteres)

#Unimos carácteres en una cadena
cadena_aleatoria = caracter1 + caracter2 + caracter3

#Mostramos la cadena generada
print(f"Cadena aleatòria: {cadena_aleatoria}")

