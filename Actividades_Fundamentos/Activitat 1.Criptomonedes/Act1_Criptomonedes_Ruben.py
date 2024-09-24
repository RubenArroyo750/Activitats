#Activitat Criptomonedes Ruben Arroyo

#Variables de la quantitat i preu de compra de cada criptomoneda amb el càlcul total de la inversió
#Bitcoin
QuantitatBTC = 0.5 
PreuBTC = 27000 

ValorBTC = QuantitatBTC * PreuBTC 

#Ethereum
QuantitatETH = 2 
PreuETH = 1800

ValorETH = QuantitatETH * PreuETH 

#Ripple
QuantitatXRP = 1000
PreuXRP = 0.50

ValorXRP = QuantitatXRP * PreuXRP 

#Càlcul del valor total de la inversió
TotalInversio = ValorBTC + ValorETH + ValorXRP

#Càlcul del valor de cada criptomoneda
PercentatgeBTC = ValorBTC / TotalInversio * 100

#Càlcul del valor de cada criptomoneda
PercentatgeETH = ValorETH / TotalInversio * 100

#Càlcul del valor de cada criptomoneda
PercentatgeXRP = ValorXRP / TotalInversio * 100

#Càlcul ROI amb inversió inicial de 15,000 euros
cost_total_inicial = 15000
valorROI = ((TotalInversio - cost_total_inicial) / cost_total_inicial) * 100

#Mostra per pantalla del valor total de la inversió de cada criptomoneda
print("Valor de Bitcoin: ", format(ValorBTC,"1.1f"),"euros")
print("Valor d'Ethereum: ", format(ValorETH,"1.1f"), "euros")
print("Valor de Ripple: ", format(ValorXRP, "1.1f"), "euros")

#Mostra per pantalla del total de la inversió
print("Valor total de la inversió: ", format(TotalInversio,"1.1f"), "euros")

#Mostra el porcentatge del valor de cada criptomoneda
print("Percentatge de Bitcoin: ", format(PercentatgeBTC,"1.2f"),"%")

#Mostra el porcentatge del valor de cada criptomoneda
print("Percentatge de Ethereum: ", format(PercentatgeETH,"1.2f"),"%")

#Mostra el porcentatge del valor de cada criptomoneda
print("Percentatge de Ripple: ", format(PercentatgeXRP,"1.2f"),"%")

#Mostra el rendiment de la inversió (ROI)
print("Rendiment de la inversió ROI: ", format(valorROI,"1.2f"),"%")