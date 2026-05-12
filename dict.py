#creazione dizionario
studente ={"nome":"fabio", "eta":30, "corso":"python"}
print(studente)

#modifica chiave 
studente["eta"] = 37
print(studente)

#aggiunta chiave
studente["matricola"] = "1234"
print(studente)

#stampa valore chiave
nome = studente.get("nome","non specificata")
print(nome)

 #stampa coppia chiave/valore
for nome, corso in studente.items():
    print(nome, corso)

#eliminare chiave
studente.pop("eta")
print(studente)