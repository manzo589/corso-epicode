class studente:
    def __init__(self, nome, corso):
        self.nome = nome
        self.corso = corso
        pass

studente1 = studente("Giulia", "Informatica")
print(f"Ciao, sono {studente1.nome} e frequento il corso di {studente1.corso}")


class persona :
    def __init__(self, nome):
        self.__nome = nome

    def presentati (self):
        print (f"Ciao mi chiamo {self.__nome}") 

class studente (persona):
    def __init__(self, nome, corso):
        persona.__init__(self, nome)
        self.corso = corso

    def presentati_2 (self):
        print(f"e frequento il corso di {self.corso}")



s1 = studente ("Fabio", "python")



s1.presentati()

s1.presentati_2()


class studenti :
    scuola = "Liceo classico"
    
    def __init__(self, nome):
        self.nome = nome

    def presentazione(self)
        print(f"Sono {self.nome} e frequento la scuola {scuola})
              
s2 = studenti ("fabio")

s2.presentazione()
