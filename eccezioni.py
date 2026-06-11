class Divisione:
    def __init__(self, a , b):
        self.a = a
        self.b = b

    def risultato(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return ("Impossibile dividere per 0")

x = int(input("Inserisci il denominatore: "))

y = int(input("Inserisci il divisore: "))

d1 = Divisione(x , y)

print (d1.risultato())






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

try: # dando l'errore direttamente nella creazione della persona p1 va inserita nel try
    p1 = Persona (s , d)
    p1.stampa()
except ValueError:
    print ("L'età inserita è errata")







class SaldoInsufficenteError(Exception):
    pass

class Banca:
    def __init__(self, saldo):
        self.saldo = saldo

    def preleva (self, importo):
        if importo > self.saldo:
            raise SaldoInsufficenteError("Saldo indufficente!")
        self.saldo -= importo
        return f"Il tuo nuovo saldo è: €{self.saldo}"

y = int(input("Quanto vuoi depositare?:€ "))

b1 = Banca(y)

x = int(input("Quanto vuoi prelevare?:€ "))

try: #dando l'errore nella fase di prelievo solo la sottrazione va inserita nel try
    print(b1.preleva(x)) 
except SaldoInsufficenteError:
    print("Saldo Insufficente!")