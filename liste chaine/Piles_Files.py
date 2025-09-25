from Liste_chaine import Liste_chainee

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
        return self.donnees.debut.valeur
        return None
    
    def pop(self):
        self.donnees.sup_cellule()
    
    def pop2(self):
        if not self.vide():
            self.donnees.sup_cellule()
        else:
            pritn("liste vide")

    def pop3(self):
        return
