class Studente:
    def __init__(self, nome, eta):
        if eta <= 0:
            raise ErroreScuola("Età inserita errata!")
        self.nome=nome
        self.eta=eta

    def Stampa(self):
        return f"Lo studente si chiama {self.nome} ed ha {self.eta} anni"

class ErroreScuola(Exception):
    pass

class EtaNonValidaError(ErroreScuola):
    def __init__(self, eta):
        super().__init__(f"Età inserita {eta} non valida")
        self.eta=eta

x = str(input("Inserici Nome studente: "))

z = 0
while z == 0:
    try:
        y = int(input("inserisci Età Studente: "))
        s1 = Studente(x, y)
        print(s1.Stampa())
        z = y

    except ErroreScuola as e:
        print("Valore eta inserito non conforme!")