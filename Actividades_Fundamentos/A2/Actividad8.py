#Un venedor rep un sou base més un 10% extra per comissió de les seves vendes, 
#el venedor vol saber quants diners obtindrà per concepte de comissions per les tres vendes que realitza en el mes i el total 
#que rebrà al mes tenint en compte el seu sou base i comissions.

sueldoBase = float(input("Introduce el sueldo: ")) #Se introduce el sueldo

#Introducción del valor de cada venta
venta1 = float(input("Introduce el total de la primera venta: "))
venta2 = float(input("Introduce el total de la segunda venta: "))
venta3 = float(input("Introduce el total de la tercera venta: "))

#Suma de la comisión (se suman las tres ventas) y se multiplica por el 10%
comision = (venta1 + venta2 + venta3) * 0.1 
total = sueldoBase + comision

#Muestra por pantalla del resultado
print("El sueldo del vendedor es:", sueldoBase,"€")
print("La comision total del mes por las tres ventas es de: ", comision,"€")
print("El sueldo total con la comision incluida del vendedor corresponde a : ", total,"€")