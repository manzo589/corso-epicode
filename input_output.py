class Studente:
    def __init__(self):
        self.nome = input("Inserisci il nome dello studente: ")
        self.eta = int(input("Inserisci l'eta dello studente: "))

    def __str__(self):
        return f"{self.nome},{self.eta}"
    

    def presentati (self):
        return f"Il Nuovo studente si chiama {self.nome} e ha {self.eta} anni."
    
class Diario:
#-----------creazione della variabile file con il nome del file da creare---------    
    def __init__(self):
        self.file = "input_output.txt"

#------------scrivere su un file-----------
    def scrivi_file(self, nota):
        with open(self.file, "a") as f:
            f.write(nota +"\n")

#-------------leggere da file--------------
    def leggi(self):
        with open (self.file,"r") as f:
            return f.read()

s1 = Studente()

print(s1.presentati())

print(s1)

d1 = Diario()

nota = input("Scrivi una nota su di te: ")

d1.scrivi_file(nota)

print(d1.leggi())