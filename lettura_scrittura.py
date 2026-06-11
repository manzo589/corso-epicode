class Appunti:
    def __init__ (self):
        self.file="lettura_scrittura.txt"
        
    def scrivi(self):
        self.nota=input("Scrivi una nota da aggiungere al tuo diario: ")
        with open("lettura_scrittura.txt","a") as f:
            f.write(self.nota + "\n")

    def aggiungere_nota(self):
        z =input("Vuoi aggiungere un'altra nota?(si/no): ").lower()
        while z == "si":
            with open("lettura_scrittura.txt","a") as f:
                self.nota=input("Scrivi nota: ")
                f.write(self.nota + "\n") 
                z =input("Vuoi aggiungere un'altra nota?(si/no): ").lower()
                
    def stampa(self):
        with open ("lettura_scrittura.txt","r") as f:
            return f.read()
        
    def cancella(self):
        with open ("lettura_scrittura.txt","w") as f:
            f.write("")
            print("File svuotato")

a1 = Appunti()

z = 0

while z == 0:
    x = input("Cosa vuoi fare? \n"
    "1)Scivere nota \n"
    "2)Leggere diario \n"
    "3)Cancellare il diario \n"
    "4)Chiudere il diario \n"
    "Inserire la proprio scelta: ").lower()

    if x in ["1", "scrivere nota"]:
        a1.scrivi()
        a1.aggiungere_nota()

    elif x in ["2", "leggere diario"]:
        print(a1.stampa())

    elif x in ["3", "cancellare il diario"]:
        a1.cancella()

    elif x in ["4", "chiudere il diario"]:
        input("Diario chiuso con successo!")
        z = 1

    else:
        print("Selezione errata!")