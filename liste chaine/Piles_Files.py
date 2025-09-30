from liste_chaine import Liste_chainee

class Pile:
    def __init__(self):
        self.donnees = Liste_chainee()       
        
    def push(self, element):
        self.donnees.ajoute_debut(element)

    def vide(self):
        if self.donnees.debut is None:
            return True
        return False

    def top(self):
        if not self.vide():
            return self.donnees.debut.valeur
        else:
            return None
    
    def pop(self):
        self.donnees.sup_debut()
    
    def pop2(self):
        if not self.vide():
            self.donnees.sup_debut()
        else:
            print("liste vide")

    def pop3(self):
        return

class File:
    def __init__(self):
        self.donnees = Liste_chainee()
        
    def entrer(self, valeur):
        self.donnees.ajoute_fin()
        
    def sortir(self):
        if self.donnees.debut is None:
            return None
        valeur = self.donnes.debut.valeur
        self.donnees.sup_valeur()
        return valeur
        
    def vide(self):
        if self.debut == None :
            return True

def taille(pile):
    l = 0
    while not pile.vide():
        valeur = pile.pop()
        l += 1
    return l

def taille2(pile):
    l = 0
    pile_aux = Pile()
    while not pile.vide():
        pile_aux.push(pile.pop())
        l += 1
    while not pile_aux.vide():
        pile.push(pile_aux.pop())
    return l
pile = Pile()
for i in range(10):
    pile.push(i)
print(pile.donnees)
print(taille(pile))
print(pile.donnees)