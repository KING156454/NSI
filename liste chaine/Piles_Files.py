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
        if self.donnees.debut is None:
            return
        val = self.donnees.debut.valeur
        self.donnees.sup_debut()
        return val
    
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
        self.donnees.ajoute_fin(valeur)
        
    def sortir(self):
        if self.donnees.debut is None:
            return None
        valeur = self.donnees.debut.valeur
        self.donnees.sup_debut()
        return valeur
        
    def vide(self):
        if self.donnees.debut is None:
            return True
        return False

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

def pre_el_pile(pile):
    if pile.vide():
        return None
    val = None
    while not pile.vide():
        val = pile.pop()
    return val

def pre_el_pile2(pile):
    if pile.vide():
        return None
    pile_aux = Pile()
    val = None
    while not pile.vide():
        val = pile.pop()
        pile_aux.push(val)
    while not pile_aux.vide():
        pile.push(pile_aux.pop())

def plus_grand_pile(pile):
    if pile.vide():
        return None
    pile_aux = Pile()
    max_val = None
    while not pile.vide():
        val = pile.pop()
        if max_val is None or val > max_val:
            max_val = val
        pile_aux.push(val)
        
def plus_grand_pile2(pile):
    if pile.vide():
        return None
    pile_aux = Pile()
    max_val = None
    while not pile.vide():
        val = pile.pop()
        if max_val is None or val > max_val:
            max_val = val
        pile_aux.push(val)
    while not pile_aux.vide():
        pile.push(pile_aux.pop())

def tot_el_pile(pile):
    if pile.vide():
        return None
    tot = 0
    pile_aux = Pile()
    while not pile.vide():
        val = pile.pop()
        tot += val
        pile_aux.push(val)
        
def tot_el_pile2(pile):
    if pile.vide():
        return None
    tot = 0
    pile_aux = Pile()
    while not pile.vide():
        val = pile.pop()
        tot += val
        pile_aux.push(val)
    while not pile_aux.vide():
        pile.push(pile_aux.pop())

def renverse_pile(pile):
    if pile.vide():
        return None
    pile_aux = Pile()
    while not pile.vide():
        pile_aux.push(pile.pop())
    return pile_aux

def echange_pile(pile1, pile2):
    if pile1.vide() or pile2.vide():
        return None
    pile_aux = Pile()
    while not pile1.vide():
        pile_aux.push(pile1.pop())
    while not pile2.vide():
        pile1.push(pile2.pop())
    while not pile_aux.vide():
        pile2.push(pile_aux.pop())
    return pile1, pile2

def dernier_el_entre_file():
    file = File()
    for i in range(10):
        file.entrer(i)
    val = None
    while not file.vide():
        val = file.sortir()
    return val

def dernier_el_entre_file2():
    file = File()
    for i in range(10):
        file.entrer(i)
    file_aux = File()
    val = None
    while not file.vide():
        val = file.sortir()
        file_aux.entrer(val)
    while not file_aux.vide():
        file.entrer(file_aux.sortir())
    return val

def taille_file(file):
    l = 0
    while not file.vide():
        file.sortir()
        l += 1
    return l

def taille_file2(file):
    l = 0
    file_aux = File()
    while not file.vide():
        val = file.sortir()
        file_aux.entrer(val)
        l += 1
    while not file_aux.vide():
        file.entrer(file_aux.sortir())
    return l

def plus_petit_file(F):
    if F.vide():
        return None
    mini = F.sortir()
    while not F.vide():
        x = F.sortir()
        if x < mini:
            mini = x
    return mini

def plus_petit_file2(F):
    if F.vide():
        return None
    temp = File()
    mini = F.sortir()
    temp.entrer(mini)
    while not F.vide():
        x = F.sortir()
        if x < mini:
            mini = x
        temp.entrer(x)
    while not temp.vide():
        F.entrer(temp.sortir())
    return mini

def renverser_file(F):
    P = Pile()
    while not F.vide():
        P.push(F.sortir())
    while not P.vide():
        F.entrer(P.pop())

def moyenne_file(F):
    if F.vide():
        return 0
    somme = 0
    n = 0
    while not F.vide():
        x = F.sortir()
        somme += x
        n += 1
    return somme / n

def moyenne_file2(F):
    if F.vide():
        return 0
    temp = File()
    somme = 0
    n = 0
    while not F.vide():
        x = F.sortir()
        somme += x
        n += 1
        temp.entrer(x)
    while not temp.vide():
        F.entrer(temp.sortir())
    return somme / n

def echanger_files(F1, F2):
    temp = File()
    while not F1.vide():
        temp.entrer(F1.sortir())
    while not F2.vide():
        F1.entrer(F2.sortir())
    while not temp.vide():
        F2.entrer(temp.sortir())

def echanger_pile_file(P, F):
    tempP = Pile()
    tempF = File()
    while not P.vide():
        tempF.entrer(P.pop())
    while not F.vide():
        tempP.push(F.sortir())
    while not tempP.vide():
        P.push(tempP.pop())
    while not tempF.vide():
        F.entrer(tempF.sortir())

def elimine_pairs_pile(P):
    temp = Pile()
    while not P.vide():
        x = P.pop()
        if x % 2 != 0:
            temp.push(x)
    while not temp.vide():
        P.push(temp.pop())
    
def doubler_file(F):
    temp = File()
    while not F.vide():
        x = F.sortir()
        temp.entrer(2 * x)
    while not temp.vide():
        F.entrer(temp.sortir())

def elimine_doublons_consecutifs_pile(P):
    temp = Pile()
    precedent = None
    while not P.vide():
        x = P.pop()
        if x != precedent:
            temp.push(x)
        precedent = x
    while not temp.vide():
        P.push(temp.pop())

