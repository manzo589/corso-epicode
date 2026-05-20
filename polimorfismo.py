class Forma:
    def area(self):
        pass
        

class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area (self):
        return self.base * self.altezza

class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return 3.14 * (self.raggio)**2
    

forme = [ Rettangolo(5, 8), Cerchio(3), Cerchio(12), Rettangolo(12, 25)]

for x in forme:
    print (x.area())