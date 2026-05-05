x = str(input("scrivi un frase: "))

print(x)

print(x[::-1])

print (x.upper())

print (x.lower())

y = str(input("scrivi la lettera che vogliamo vedere qualte volte si ripete: "))

z = x.count(y)

print(f"la lettera '{y}' compare {z} volte")

w = int(input("indicami un numero che non sia maggiore delle lettere della tua frase:"))

print(x[:w])

r = int(input("quante volte ripetiamo queta parte di frase?"))

print(x[:w]*r)

input("Premi Invio per chiudere...")