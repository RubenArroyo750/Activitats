# 20. Dissenyar un algorisme que ens digui els diners que tenim (en euros i cèntims) després de demanar-nos quantes monedes tenim (de 2 €, 1 €, 50 cèntims, 20 cèntims o 10 cèntims).

# Ingressar quantes monedes té l'usuari de cada tipus
monedes_2_euros = int(input("Quantes monedes de 2 € tens? "))
monedes_1_euro = int(input("Quantes monedes de 1 € tens? "))
monedes_50_centims = int(input("Quantes monedes de 50 cèntims tens? "))
monedes_20_centims = int(input("Quantes monedes de 20 cèntims tens? "))
monedes_10_centims = int(input("Quantes monedes de 10 cèntims tens? "))

# Calcular el total en cèntims
total_centims = (monedes_2_euros * 200 + 
                 monedes_1_euro * 100 + 
                 monedes_50_centims * 50 + 
                 monedes_20_centims * 20 + 
                 monedes_10_centims * 10)

# Convertir a euros i cèntims
euros = total_centims // 100
centims = total_centims % 100

# Mostrar el resultat
print(f"En total tens {euros} euros i {centims} cèntims.")