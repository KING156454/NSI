from graphviz import Graph

class Arbre_binaire:
    def __init__(self, nom):
        self.nom = nom
        self.fils_gauche = None
        self.fils_droit = None
  
    def liste_aretes(self):
        liste = []
        if self.fils_gauche != None:
            liste.append((str(self.nom), str(self.fils_gauche.nom)))
            liste = liste + self.fils_gauche.liste_aretes()
        if self.fils_droit != None:
            liste.append((str(self.nom), str(self.fils_droit.nom)))
            liste = liste + self.fils_droit.liste_aretes()
        return liste

    def affiche(self):
        graph = Graph()
        liste = self.liste_aretes()
        graph.edges(liste)
        graph.render(view=True, format='png')
    
    def set_fils_gauche(self, arbre):
        self.fils_gauche = arbre
        
    def set_fils_droit(self, arbre):
        self.fils_droit = arbre
        
    #root = Arbre_binaire('root')
    #a = Arbre_binaire('a')
    #b = Arbre_binaire('b')
    #c = Arbre_binaire('c')
    #d = Arbre_binaire('d')
    #e = Arbre_binaire('e')
    #f = Arbre_binaire('f')
    #g = Arbre_binaire('g')
    #root.set_fils_gauche(a)
    #a.set_fils_gauche(c)
    #a.set_fils_droit(d)
    #root.set_fils_droit(b)
    #b.set_fils_gauche(e)
    ##b.set_fils_droit(f)
    #e.set_fils_gauche(g)
    #root.affiche()

def branche_gauche(nb):
    a = Arbre_binaire('0')

    return a.affiche()
        
1 = Arbre_binaire('a')
a.affichage()