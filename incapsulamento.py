class ContoBancario:
    def __init__ (self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    
    def set_deposito(self,aggiungi_soldi):
        if aggiungi_soldi >= 0:
            self.__saldo = aggiungi_soldi + self.__saldo

    def set_preleva(self, preleva_soldi):
        if preleva_soldi >= 0:
            if preleva_soldi <= self.__saldo:
                self.__saldo = self.__saldo - preleva_soldi
            else:
                print("Fondi insufficenti per il prelievo")

print("Benvenuto in Banca di Credito di Manzo")
conto1 = ContoBancario( 1000 )

z = "si"

while z == "si":
    x = input("Vuoi fare un deposito o un prelievo? ")
    
    while x not in ("deposito","prelievo"):
        print("Errore di digitazione riprovare")
        x = input("Vuoi fare un deposito o un prelievo? ")

    if x == "deposito":
        y = int(input("Quanti soldi vuoi depositare? €"))
        conto1.set_deposito( y )
        print(f"Nuovo saldo {conto1.get_saldo()}")
    
    elif  x == "prelievo":
        y = int(input("Quanti soldi vuoi prelevare? €"))
        conto1.set_preleva( y )
        print(f"Nuovo saldo {conto1.get_saldo()}")

    z = input("Vuoi procedere con un'altra operazione?(si/no) ")

print("Grazie per averci scelto!")
input("Premi Invio per chiudere...")