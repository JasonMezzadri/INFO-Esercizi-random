import math


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcola_distanza_origine(self):
        distanza = math.sqrt(self.x**2 + self.y**2) #**2 --> alla seconda
        return distanza
    
    def calcola_distanza_altro_punto(self, altro_punto: "Punto"):
        differenza = math.sqrt(abs(self.y - altro_punto.y)**2 + abs(self.x - altro_punto.x)**2) # abs = valore assoluto
        return differenza
    
    def visualizza(self):
        print(f"({self.x}, {self.y})")

punto1 = Punto(3, 4)
punto2 = Punto(6, 8)

punto1.visualizza()
punto2.visualizza()

calcola_distanza = punto1.calcola_distanza_altro_punto(punto2)  # calcola la distanza tra i due punti
print(f"La distanza tra i due punti è {calcola_distanza}")