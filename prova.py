class Persona:
    def __init__(self, nome , eta):
        if eta < 0:
            raise ValueError ("L'età non può essere inferiore a 0!")
        self.nome = nome
        self.eta = eta

    def stampa (self):
        print (f"{self.nome} ha {self.eta} anni")

s = str(input("Inserisci un Nome: "))
d = int(input("Inserisci Età: "))

try:
    p1 = Persona (s , d)
    p1.stampa()
except ValueError:
    print ("L'età inserita è errata")