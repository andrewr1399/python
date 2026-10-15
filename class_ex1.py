####Classi

class Bottiglia:
    
    def __init__ (self, capacita, contenuto):
        self.capacita = capacita
        self.contenuto = contenuto
        
    def bere(self, bev):
        
        if bev > self.contenuto:
            print("Hai bevuto troppa acqua!")
            self.contenuto = 0
        
        else:
            self.contenuto = self.contenuto - bev
        
            
    def riempi(self, agg):
        
        if agg > (self.capacita - self.contenuto):
            print("Troppa acqua, ora è piena!")
            self.contenuto = self.capacita
            
        else:
            self.contenuto = self.contenuto + agg
    
    def vuota(self):
        return self.contenuto <= 0
    
    def __str__(self):
        return f"bottiglia da {self.capacita}L ({self.contenuto}L dentro)"
        

b1 = Bottiglia(1, 0.7)

b1.bere(float(input("Quanto hai bevuto?: ")))
b1.riempi(float(input("Riempi?: ")))

print(b1)
