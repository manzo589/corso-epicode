class Libro:
    numero_pagine = 200
    def __init__(self,titolo,autore):
        self.titolo = titolo
        self.autore = autore

    def __str__(self):
        return f"Il libro {self.titolo} è stato scritto da {self.autore} ed ha {self.numero_pagine} pagine"
    
L1 = Libro("one piece", "eichiro oda")

print(str(L1))

lista_libri = []

n = int(input("Quanti libri vuoi caricare? "))

for x in range(n):
    y = input("Inserisci il titolo del libro da inserie: ")
    z = input("Inserisci autore del libro: ")
    L2 = Libro (y, z)
    lista_libri.append (L2)
    print(str(L2))
    

for libro in lista_libri:
    print (libro)
