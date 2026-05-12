def media (*args):
    """media dei numeri"""
    return sum(args) / len(args)

def chiedi_num():
   """chiede ad utende il numero da inserire"""
   return int(input("Scrivi numero per media: "))

def stringa_corretta():
    """domanda se lista scritta correttamente"""
    return str(input("La lista che hai inserito è corretta?(si/no) "))

numeri = []

print ("Facciamo la media dei numeri.")

num_med = int(input("Di quanti numeri vuoi fare la media? "))

for x in range(0,num_med):
    num = chiedi_num()
    numeri.append(num)
print("la tua lista è:" ,numeri)

corretto = stringa_corretta()

while corretto == "no" :
    print("inseirsci di nuovo la lista!")
    numeri.clear()
    for x in range(0,num_med):
        num = chiedi_num()
        numeri.append(num)
    print("la tua lista è:" ,numeri)
    corretto = stringa_corretta()

print(f"La media dei {num_med} numeri è: " ,media(*numeri))
 
input("Premi Invio per chiudere...")