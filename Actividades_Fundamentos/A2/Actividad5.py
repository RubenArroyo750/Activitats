#Programa que convierte un valor dado en grados Fahrenherit a grados Celsius.

#Pediremos al usuario un valor en grados Fahrenherit
f = float(input("Indica un valor en grados Fahrenherit: ")) #float representa datos positivos y negativos decimales

#Calculos de conversion
def Conversion(f): #Se crea una función con la variable F de Fahrenherit 
    c =  (f-32) * 5/9 #conversión de celsius i se calcula el valor restando 32 al valor f i el resultado se multiplica entre 5/9
    return c #retorna un resultado

#Mostramos por pantalla la conversion
print("La conversion a grados celsius es: " + str(Conversion(f)) + "")
