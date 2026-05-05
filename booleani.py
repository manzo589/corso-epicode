eta = int(input("quanti hanni hai?:  "))

patente = str (input ("hai la patente?: "))

guida  = (eta >= 18) and (patente == "si")

print (guida)


ritardo = "no"
premium = "si"

entrare = (ritardo == "si") or (premium == "si")

print (entrare)