import csv


class GestoreLibri:
    def __init__(self,file):
        self.file=file

    def leggi(self):
        with open (self.file,"r") as f:
            reader=csv.DictReader(f)
            for riga in reader:
                print(riga["titolo"])
        
    def autore(self):
        with open (self.file,"r") as f:
            reader=csv.DictReader(f)
            for riga in reader:
                if riga["autore"] == "fabio":
                    print (riga["titolo"])


gestione=GestoreLibri("libri.csv")

dati=gestione.leggi()
print("")
a1=gestione.autore()

