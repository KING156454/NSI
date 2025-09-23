class Colis():
    def __init__(self, nom, poids, nb_article):
        self.nom = nom
        self.poids = poids
        self.nb_article = nb_article

    def __repr__(self):
        affichage = "colis nomme{self.nom} qui pese {self.poids}kg avec {self.nb_article}article dedans"
        return affichage
    
    def get_nom(self):
        return self.nom
    
    def modif_poids(self,n):
        self.poids += n

    def poids_total(self):
        poids_total = self.nb_article * self.poids
        return poids_total
    
    def liste_colis(self ,liste):
        ensemble = 0
        for i in liste :
            ensemble += poids_total(i)
        return ensemble

colis1 = Colis(biere,20,5)
colis2 = Colis(pain, 200 , 1000)
