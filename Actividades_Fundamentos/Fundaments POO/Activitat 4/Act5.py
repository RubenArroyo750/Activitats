#5. Crea una classe Cercle amb un atribut radi. Afegeix un mètode que calculi l'àrea del cercle. 
#Demana a l'usuari que introdueixi el radi i mostra l'àrea.

#Importar modulo math
import math


#Clase circulo con atributo radio
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    #Metodo donde se calcula el area del circulo
    def calcularArea(self):
        area = math.pi * self.radio **2
        #Se redondea a dos decimales el resultado por pantalla
        areaResultado = round(area, 2)
        #Mostramos al usuario el resultado del area
        print(f"El area del circulo es de: {areaResultado}")
    
#Preguntamos al usuario que introduzca el radio
radio = float(input("Introduce el radio del circulo: "))

#Creamos objeto circulo vinculado al constructor donde pedimos el input del radio
circulo1 = Circulo(radio)

#Insertamos el mismo objeto donde llamaremos a la función calcularArea sin parámetros ya que solo tenemos self "comprensión"
circulo1.calcularArea()


        