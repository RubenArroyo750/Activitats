#2. Afegeix a la classe anterior un mètode per a que mostri el nom i 
#l'edat de la persona en aquest format " Nom: Manel, Edat: 19".

#Clase Persona con atributos nombre y edad
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #Registramos frase que mostrará en pantalla con los valores objeto
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

#Objeto tipo persona 
persona1 = Persona("Manel", 19)
#Muestra por pantalla en los valores nombre y edad la persona registrada
print(persona1)