from abc import ABC, abstractmethod

class Veicolo (ABC):
    @abstractmethod
    def muovi(self):
        pass
    

class Auto(Veicolo):
    def __init__(self, macchina):
        self.m = macchina

    def muovi(self):
        return (f"L'auto {self.m} si muove su strada")
    
class Aereo(Veicolo):
    def __init__(self, veivolo):
        self.v = veivolo

    def muovi(self):
        return (f"L'aereo {self.v} vola nel cielo")
    
def generico (Veicolo):
    return Veicolo.muovi()
    

x = Auto("Puma")

y = Aereo("F16")

print(x.muovi())

print(y.muovi())

print(generico(x))

print(generico(y))