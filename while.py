n = int(input("inserisci un numero per fare la somma delle sue cifre:  "))

somma = 0
while n > 0:
    somma += n % 10
    print(somma)
    n //= 10
print("il totale è: ", somma)


#trova il nome nascosto
nome = "fabio"
indovinare = str(input("Inserisci il nome da indovinare: "))

while indovinare != nome:
    indovinare = str(input("prova di nuovo: "))
print("Indovinato!")