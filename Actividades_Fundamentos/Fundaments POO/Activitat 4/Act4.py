#4. Afegeix un mèdote a la classe Persona anomenat saluda(nom), que rebi per paràmetre un nom i el saludi. 
#El nom li preguntarem al usuari per teclat.  " Hola xxxx, soc el Manel."

#Clase Persona con atributo nombre 
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    #Creamos método saludar para que salude al nombre de la clase persona
    def saludar(self, otro_nombre):
        #Se muestra por pantalla el nombre registrado en el método saludando al de la clase
        print(f"Hola {otro_nombre}, soy el {self.nombre}!")

otro_nombre = input("Introduce tu nombre: ")

#Objeto tipo persona indicando el nombre asignado
persona1 = Persona("Manel")

#Objeto tipo persona de método saludar donde el usuario introduce su nombre
persona1.saludar(otro_nombre)
