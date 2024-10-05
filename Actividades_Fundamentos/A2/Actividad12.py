#Demana a l'usuari dos parells de nombres x1, y1 i x2, y2, que representin dos punts en el pla. 
#Calcula i mostra la distància entre ells.

x1 = int(input("Introduce el numero x1: "))
y1 = int(input("Introduce el numero y1: "))

x2 = int(input("Introduce el numero x2: "))
y2 = int(input("Introduce el numero y2: "))

#Calculamos catetos
cateto1 = (x2 - x1) 
cateto2 = (y2 - y1) 

#Calculamos hipotenusa
hipotenusa = (cateto1 **2 + cateto2 **2) **0.5

#Muestra pantalla
print(hipotenusa)
