class Automobile:
    ruote = 4
    def __init__(self, marca):
        self.marca = marca

    def __str__(self):
        return f"{self.marca} ha {self.ruote} ruote"


a1 = Automobile("Ford")

a2 = Automobile("Fiat")

print (a1)
print (a2)
