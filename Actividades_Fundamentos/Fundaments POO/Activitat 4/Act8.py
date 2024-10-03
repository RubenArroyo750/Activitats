#8. Crea una classe Dau que simuli el llençament d'un dau. Afegeix un mètode estàtic que retorni un número aleatori entre 1 i 6. 
#Genera 4 llençaments aleatoris i mostra el resultat per pantalla en una sola linia separada per espais.

#Importamos modulo random
import random

#Clase dado que simula su lanzamiento de un Dado
class Dado:
    #Metodo estático
    @staticmethod
    def NumeroAleatorio():
        #Variable aleatorio con el generador de numeros aleatorios del 1 - 6
        aleatorio = random.randint(1, 6)
        #Devolvemos la variable 
        return aleatorio

#Generamos 4 lanzamientos de Dados
Dado1 = Dado.NumeroAleatorio()
Dado2 = Dado.NumeroAleatorio()
Dado3 = Dado.NumeroAleatorio()
Dado4 = Dado.NumeroAleatorio()

#Dados = (Dado1, Dado2, Dado3, Dado4)

#Llamamos al constructor Dado donde pedimos el método creado
Dado.NumeroAleatorio()

#Resultado de los numeros aleatorios separados por espacios
print("Los resultados de los lanzamientos aleatorios son:", Dado1, Dado2, Dado3, Dado4, sep=" ")


