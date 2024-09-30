#Realitza un programa que rebi una quantitat de minuts i mostri per pantalla a quantes hores i minuts correspon.
#Per exemple: 1000 minuts són 16 hores i 40 minuts.

datos = int(input("Introduce una cantidad de minutos: ")) #Se introduce la cantidad de minutos

hora = datos//60 #División entera de la hora con los datos introducidos entre 60 minutos de una hora

minutos1 = datos - (hora * 60) #Se calcula los datos de la hora multiplicado por 60 y se restan los datos introducidos por el usuario

#Mostrar mensaje por pantalla
print("La cantidad de minutos " + str(datos) + " corresponde a: " + str(hora) + " horas y "+ str(minutos1) + " minutos")