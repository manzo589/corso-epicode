#creare lista da inserimento utente
print("Creiamo una lista di 5 nomi e indiciziamola")
for x in range(1,6):
    n = str(input(f"inserisci nome {x}: "))


#indicizzare lista
n1 ="fabio"
n2 ="federica"
n3 ="vittoria"
n4 ="achille"
n5 ="luna"

for indice, nome in enumerate([n1, n2, n3, n4, n5]):
    print(indice+1, nome)

#unione 2 liste
e1 = 10
e2 = 42
e3 = 2
e4 = 78
e5 = 20

for nome, eta in zip([n1 ,n2, n3, n4, n5],[e1, e2, e3, e4, e5]):
    print(f"{nome} ha {eta} anni")
