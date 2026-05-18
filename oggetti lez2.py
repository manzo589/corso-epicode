class studente :
    scuola = "Liceo classico"
    
    def __init__(self, nome):
        self.nome = nome
   

    def presentazione(self):
        print(f"Sono {self.nome} e frequento la scuola {studente.scuola}")
      
    @classmethod
    def cambio_scuola (cls, cambio_scuola):
        cls.scuola = cambio_scuola

s1 = studente ("fabio")

s2 = studente ("federica")

s1.presentazione()

s2.presentazione()

studente.cambio_scuola("Liceo scentifico")

s1.presentazione()

s2.presentazione()
