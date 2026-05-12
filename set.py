corso_a = {"fabio", "federica", "vittoria"}
corso_b = {"achelle", "luna","fabio", "federica"}

print("Entrambi i corsi sono seguitida: ",corso_a | corso_b)

print("Frequenta solo il corso A: ", corso_a - corso_b)

print("Frequenta solo il corso B: ", corso_b - corso_a)

print("Frequentano solo un corso: ",corso_a ^ corso_b)

x = len(corso_a ^ corso_b)

print("Il numero di studenti unici nei corsi è: ", x)
