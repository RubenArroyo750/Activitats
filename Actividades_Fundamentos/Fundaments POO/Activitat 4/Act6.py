#6. Crea una classe Producte amb atributs nom, preu i descompte. Afegeix un mètode que mostri el preu amb un descompte. 
#Demana a l'usuari el nom i el preu i descompte, i mostra el nom amb el preu amb descompte.

#Clase producto con atributos nombre, precio y descuento
class Producto:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento
    #Metodo donde se calcula el descuento inputado al precio
    def calcularDescuento(self):
        descuentoPrecio = precio - (precio * descuento / 100)
        #Resultado por pantalla
        print(f"El producto {self.nombre} tiene un valor de {self.precio} €, con un descuento aplicado del {self.descuento} %.")
        print(f"Equivale a un total de: {descuentoPrecio} €")

#Consultamos al usuario los atributos del producto y los registramos
nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
descuento = float(input("Introduce el descuento que se aplicará: "))

#Objeto producto1 vinculado al constructor producto donde pedimos los atributos
producto1 = Producto(nombre, precio, descuento)

#Objeto producto1 vinculado al método del calculo del descuento
producto1.calcularDescuento()
