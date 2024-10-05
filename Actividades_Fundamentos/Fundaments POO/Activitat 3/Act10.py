# 10. Escriu un programa que mostri el directori de treball actual del teu ordinador
# (on s'està executant el programa).
import os

# Obtenim el directori de treball actual
directori_actual = os.getcwd()

# Mostrem el directori actual
print(f"El directori de treball actual és: {directori_actual}")