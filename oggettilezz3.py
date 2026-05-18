class Studente:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def presentati(self):
        print(f"Ciao sono {self.nome} ed ho {self.eta} anni")

s1 = Studente ("Fabio", 37)
s2 = Studente ("Federica", 36)

s1.presentati()
s2.presentati()


s1.corso = "Matematica"
s2.corso = "Fisica aerospaziale"

print("Ciao sono",s1.nome,"ed ho",s1.eta,"anni e frequento il corso di", s1.corso)
print("Ciao sono",s2.nome,"ed ho",s2.eta,"anni e frequento il corso di", s2.corso)
