from liste_chaine import Liste_chaine


class Pile:
    def __init__(self):
        self.donnees = Liste_chainee()       
        
    def push(self, element):
        self.donnees.ajoute_debut(element)

    def pop(self):
        self.donnees.sup_cellule()
