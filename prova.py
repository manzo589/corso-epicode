n = int(input("inserisci un numero per fare la somma delle sue cifre:  "))

somma = 0
while n > 0:
    somma += n % 10
    print(somma)
    n //= 10
print("il totale è: ", somma)
