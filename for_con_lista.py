
print("Creiamo una lista di 5 nomi e indiciziamola")
lista_nomi = []
contatore = 0


for x in range(1,6):
    n = str(input(f"inserisci nome {x}: "))
    lista_nomi.insert(x-1, n)
print(lista_nomi)

for i, y in enumerate(lista_nomi, start=0):
    print(i+1, y)

input("Premi Invio per chiudere...")