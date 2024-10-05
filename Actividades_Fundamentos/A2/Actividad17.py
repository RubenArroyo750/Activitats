# 17. Un ciclista part d'una ciutat A a les HH hores, MM minuts i SS segons. El temps de viatge fins arribar a una altra ciutat B és de T segons. Escriure un algoritme que determini l'hora d'arribada a la ciutat B.
# Ingressar les dades
# Ingressar les dades
HH = int(input("Hora de partida (HH): "))
MM = int(input("Minuts de partida (MM): "))
SS = int(input("Segons de partida (SS): "))
T = int(input("Temps de viatge en segons (T): "))

# Convertir l'hora de partida a segons totals
temps_partida_en_segons = HH * 3600 + MM * 60 + SS

# Sumar el temps de viatge
temps_arribada_en_segons = temps_partida_en_segons + T

# Convertir els segons totals a hores, minuts i segons
hores_arribada = (temps_arribada_en_segons // 3600) % 24
minuts_arribada = (temps_arribada_en_segons % 3600) // 60
segons_arribada = temps_arribada_en_segons % 60

# Mostrar el resultat
print(f"L'hora d'arribada a la ciutat B és {hores_arribada:02}:{minuts_arribada:02}:{segons_arribada:02}")