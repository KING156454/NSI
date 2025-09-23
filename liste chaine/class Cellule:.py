class Cellule:
    def __init__(self, valeur, successeur):
        'Initialise la cellule '
        self.valeur = valeur
        self.successeur = successeur  # Un autre objet du type Cellule
    

class Liste_chainee:
    def __init__(self):
        self.debut = None
        self.longueur = 0
        
    def ajoute_debut(self, valeur):
        cell = Cellule(valeur, self.debut) #Le successeur de cell est l'actuel selfdebut
        self.debut = cell    #self.debut est remplacée par cell
    
    def __repr__(self):
        affichage = ""
        cellule_courante = self.debut
        while cellule_courante != None:
            affichage += str(cellule_courante.valeur) + ' '
            cellule_courante = cellule_courante.successeur
        return affichage

    def ajoute_fin(self,valeur):
        if self.debut == None :
            self.ajoute_debut(valeur)
        Cellule_courrante = self.debut
        while Cellule_courrante.successeur != None :
            Cellule_courrante = Cellule_courrante.successeur
        nouvelle_cellule = Cellule(valeur, None)
        Cellule_courrante.successeur = nouvelle_cellule
        self.longueur += 1

    def sup_cellule(self,nom):
        if self.debut == None :
            return
        else:
            self.debut = self.debut.successeur
        self.longueur -= 1

    def sup_cellule_fin(self):
        if self.debut is None:
            return None
        if self.debut.successeur is None:
            self.debut = None
            return None
        cellule = self.debut
        while cellule.successeur.successeur is not None:
            cellule = cellule.successeur

        cellule.successeur = None

    def complexite(self) :
        return








    def taille(self):
        if self.debut is None :
            return 0
        compteur = 0
        cc = self.debut
        while cc is not None :
            compteur += 1
            cc = cc.successeur
        return compteur
    
    def recherche_cellule_index(self,index) :
        if index < 0 or index > self.longueur:
            print("erreur index")
            return
        cellule_courante = self.debut
        cc = self.debut
        for i in range(index):
            cc = cc.successeur
        return cc.valeur
    
    def recherche_cellule_valeur(self,valeur):
        if self.debut == None :
            return None
        cc = self.debut
        compteur = 0
        while cc.valeur != valeur and cc.successeur is not None :
            cc = cc.successeur
            compteur += 1
        if cc.valeur == valeur :
            return compteur
        else :
            return None
    
liste = Liste_chainee()
liste.ajoute_debut('a')
liste.ajoute_debut('b')
print(liste)
print(liste.debut.valeur)
print(liste.debut.successeur)
print(liste.debut.successeur.valeur)
