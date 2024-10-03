#3. Afegeix un mètode la classe Persona anomenat presenta() per a que respongui "Hola em dic Manel i tinc 19 anys."

#Clase Persona con atributos nombre y edad
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #Creamos método presenta para que responda una frase
    def presenta(self):
        #Muestra por pantalla los valores nombre y edad la persona registrada
        print (f"Hola em dic {self.nombre} i tinc {self.edad} anys")

#Objeto tipo persona 
persona1 = Persona("Manel", 19)
#Se llama al método presenta
persona1.presenta()

