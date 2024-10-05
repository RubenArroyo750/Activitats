#18. Demanar el nom i els dos cognoms d'una persona i mostrar les inicials.

nom = input("nom: ")
cognom1 = input("cognom1: ")
cognom2 = input("cognom2: ")

# Els stirngs es poden recorrer i accedir per posició com si fossin llistes
i1 = nom[0].upper()
i2 = cognom1[0].upper()
i3 = cognom2[0].upper()

print(i1,i2,i3, sep=".", end=".")