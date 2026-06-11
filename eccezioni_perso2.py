class Magazzino:
    def __init__(self, prodotto, quantita):
        self.prodotto=prodotto
        self.quantita=quantita

    def rimuovi_prodotto(self, rimosso):
        if rimosso > self.quantita:
            raise ProdottoEsauritoError(self.prodotto, self.quantita)
        self.quantita -= rimosso

    def nuova_quantita(self):
        return f"La nuova giacenza del prodotto {self.prodotto} è {self.quantita}"


class ErroreMagazzino(Exception):
    pass

class ProdottoEsauritoError(ErroreMagazzino):
    def __init__(self, prodotto, quantita):
        super().__init__(f"Il prodotto {prodotto} è terminato")
        self.prodotto=prodotto
        self.quantita=quantita

try:
    p1 = Magazzino("Sapone", 10)
    p1.rimuovi_prodotto(11)
    print(p1.nuova_quantita())
except ProdottoEsauritoError as e:
    print(f"Prodotto non sufficente, la giacenza è di {p1.quantita}")