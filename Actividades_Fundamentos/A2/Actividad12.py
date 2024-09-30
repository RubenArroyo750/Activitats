#Demana a l'usuari dos parells de nombres x1, y1 i x2, y2, que representin dos punts en el pla. 
#Calcula i mostra la distància entre ells.

x1 = int(input("Introduce el numero x1: "))
y1 = int(input("Introduce el numero y1: "))
x2 = int(input("Introduce el numero x2: "))
y2 = int(input("Introduce el numero y2: "))

pareja1 = (x1 - x2) **2
pareja2 = (y1 - y2) **2

print(pareja1)
print(pareja2)