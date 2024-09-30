#Una botiga ofereix un descompte de l'15% sobre el total de la compra i
# un client vol saber quant haurà de pagar finalment per la seva compra.

#Pedimos al usuario que introduzca el total de su compra
descuento = 0.15
compra = float(input("Introduce el total de la compra: "))

#descuento = (compra) * 0.15 #Calculamos del total de la compra el 15% aplicado a ahorrar
CantidadDescuento = (compra * descuento)

#Mostramos por pantalla
print("Con el 15% te ahorraras: ", CantidadDescuento, "€")
print("El total de la compra con descuento aplicado es de: ", compra - CantidadDescuento, "€")