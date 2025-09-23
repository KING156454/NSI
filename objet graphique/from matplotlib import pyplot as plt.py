from matplotlib import pyplot as plt

class Ligne:
    def __init__(self, a, b):    #Attention : double underscore __
        self.a = a     #Les attributs d'une instance de la classe Ligne s'appelleront toujours a et b
        self.b = b
        
    def affiche(self):
        abscisses = [self.a[0], self.b[0]]
        ordonnees = [self.a[1], self.b[1]]
        plt.plot(abscisses, ordonnees)
a = (7, 6)
b = (-1, -2)
ligne = Ligne(a, b)    #ligne.a et ligne.b sont initialisés à a et b
ligne.affiche()
plt.show()