class Animale:
    def __init__ (self, nome):
        self.nome = nome

    def Verso (self):
        print(f"{self.nome} fa un verso.")

class Cane (Animale):
    def Verso(self):
        print(f"{self.nome} fa Bau ")

class Gatto (Animale):
    def Verso(self):
        print(f"{self.nome} fa miao")


a = Cane("Fido")
a.Verso()

b = Gatto("Achille")
b.Verso()

c = Animale("Ugo")
c.Verso()