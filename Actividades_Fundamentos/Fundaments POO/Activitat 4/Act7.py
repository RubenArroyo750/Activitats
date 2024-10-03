#7. Crea una classe Calculadora amb mètodes estàtics per sumar, restar, multiplicar i dividir. 
#Després, demana dos números a l'usuari i mostra el resultat de les 4 operacions amb aquests numeros.

#Clase calculadora con métodos estáticos
class Calculadora:
    #Se genera el método estático
    @staticmethod
    #suma de dos valores y se devuelven 
    def sumar(a, b):
        return a + b
    #Resta de dos valores y se devuelven 
    def restar(a, b):
        return a - b
    #Multiplicación de dos valores y se devuelven 
    def multiplicar(a, b):
        return a * b
    #Division de dos valores y se devuelven 
    def dividir(a, b):
        return a / b

#Se pide al usuario que introduzca los dos valores
a = int(input("Introduce un numero: "))
b = int(input("Introduce otro numero: "))

#Mostramos por pantalla los resultados de las operaciones redondeando los resultados con 2 decimales
resultado = Calculadora.sumar(a, b)
print("La suma total de los numeros es de: ",round(resultado, 2))

resultado = Calculadora.restar(a, b)
print("La resta total de los numeros es de: ",round(resultado, 2))

resultado = Calculadora.multiplicar(a, b)
print("La multiplicación total de los numeros es de: ",round(resultado, 2))

resultado = Calculadora.dividir(a, b)
print("La división total de los numeros es de: ",round(resultado, 2))

