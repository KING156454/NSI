from matplotlib import pyplot as plt

class Ligne:
    def __init__(self, a, b):    #Attention : double underscore __
        self.a = a     #Les attributs d'une instance de la classe Ligne s'appelleront toujours a et b
        self.b = b
        
    def affiche(self):
        abscisses = [self.a[0], self.b[0]]
        ordonnees = [self.a[1], self.b[1]]
        plt.plot(abscisses, ordonnees)

    def affiche_milieu(self):
        abscisse = (a[0] + b[0])/2
    ordonnee = (a[1] +  b[1])/2
    plt.plot(abscisse, ordonnee,'o')

    def calcule_longueur(self):
        longueur = sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
        return longueur


plt.show()