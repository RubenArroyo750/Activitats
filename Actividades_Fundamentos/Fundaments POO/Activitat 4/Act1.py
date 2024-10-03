#1. Crea una classe Persona amb atributs nom i edat. Crea un objecte de tipus 
#Persona amb nom = "Manel" i edat = 19 . Imprimex l'objecte, que veus?

#Clase Persona con atributos nombre y edad
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #Registramos frase que mostrará en pantalla con los valores objeto
    def __str__(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

#Objeto tipo persona 
persona1 = Persona("Manel", 19)
#Muestra por pantalla en los valores nombre y edad la persona registrada
print(persona1)