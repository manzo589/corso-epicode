class Studente:
    def __init__(self, nome, eta, corso):
        self.nome = nome
        self.eta = eta
        self.corso = corso

    @classmethod
    def studente_da_stringa(cls, studente):
        nome,eta,corso =studente.split("-")
        return cls(nome, int(eta), corso)

    @property
    def anno_nascita(self):
        return 2026-self.eta

    @property
    def eta(self):
        return self._eta
    
    @eta.setter
    def eta(self, nuova_eta):
        if nuova_eta >= 0 :
            self._eta = nuova_eta
        else:
            print("Eta errata")

x = input("Inserisci nome-eta-corso dello studente separati dal trattino: ")
s = Studente.studente_da_stringa(x)

print(s.nome,s.eta,s.corso)
print(s.anno_nascita)

y = int(input ("Modifica l'eta: "))
s.eta = y
print(s.nome,s.eta,s.corso)
print(s.anno_nascita)
