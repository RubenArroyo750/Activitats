class Persona:
    def __init__(self, nomPersona, edat):
        self.nom = nomPersona
        self.edat = edat
        self.saldoInicial = 1000
    
    def __str__(self):
        return f"Hola, em dic {self.nom} i tinc {self.edat} anys i un saldo de {self.saldoInicial} euros."

edatJoan = 44
p1 = Persona("Joan", edatJoan)
p2 = Persona("Jose", 25)
print(p2)
