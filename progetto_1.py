#------------------- Parte 1 -------------------
titolo = "il signore degli anelli"
copie = 5
prezzo = 9.95
disponibile = True

print("Titolo del libro:", titolo)
print("Copie disponibili:", copie)
print("Prezzo medio:", prezzo)
print("Disponibile:", disponibile)

print("")
#------------------- Parte 2 -------------------
lista_libri = ["il signore degli anelli" , "cars" , "zootropolis" , "la cariaca dei 101" , "oceania"]

dizionario_libri = \
{"il signore degli anelli" : 5 ,
"cars" : 4 ,
"zootropolis" : 3 ,
"la cariaca dei 101" : 2 ,
"oceania" : 1 }

utenti = {"fabio" , "federica" , "vittoria" , "achille" , "luna" }

print("")
#------------------- Parte 3 -------------------
class Libro:
    def __init__(self, titolo1 , autore , anno , copie_disponibili):
        self.titolo1 = titolo1
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info (self):
        return f"Il libro {self.titolo1} è stato scritto da {self.autore} nell'anno {self.anno} e ci sono disponibili {self.copie_disponibili} copie."

class Utente:
    def __init__(self , nome , eta , id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        return f"{self.nome} ha {self.eta} anni e il suo id è {self.id_utente}"

class Prestito:
    def __init__(self , libro , utente , giorni_prestito):
        self.libro = libro
        self.utente = utente
        self.giorni_prestito = giorni_prestito

    def dettagli(self):       
        return f"Il Libro {self.libro.titolo1} è stato preso da {self.utente.id_utente} per {self.giorni_prestito} giorni"

#------------------- Parte 4 -------------------
def presta_libro(utente , libro , giorni):
    if libro.copie_disponibili > 0:
        libro.copie_disponibili -= 1
        return Prestito(libro, utente, giorni)

    else:
        print(f"Il libro {libro.titolo1} non è disponibile")


    
# Creo 3 Libri
L1 = Libro("Gli aristogatti" , "Vittoria" , "1990" , 10 )
L2 = Libro("cars" , "Fabio" , "2000" , 0 )
L3 = Libro("La sirenetta" , "Federica" , "1996" , 3 )

#Creo 3 utenti
U1 = Utente("Fabio" , 37 , "Manzo89")
U2 = Utente("Federica" , 36 , "Fede90")
U3 = Utente("Vittoria" , 3 , "Vitto23")

P1 = Prestito(L1, U1, 5)

print(L1.info())
print(U1.scheda())
print(P1.dettagli())
print("")
#Creo 3 prestiti
P1 = presta_libro(U1, L1, 5)
P2 = presta_libro(U2, L2, 3)
P3 = presta_libro(U3, L3, 10)


print("")
#Stampo nuove disponibilita
for libro in [L1, L2, L3]:
    print(f"{libro.titolo1}: {libro.copie_disponibili}")

print("")
#Stampo dettaglio prestito
for prestito in [P1, P2, P3]:
    if prestito:
        print(prestito.dettagli())