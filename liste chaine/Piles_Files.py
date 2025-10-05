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

def 
pile = Pile()
pile_aux = Pile()
for i in range(10):
    pile.push(i)
print(pile.donnees)
print(taille2(pile))
print(pile.donnees)
print(pre_el_pile())
print(plus_grand_pile2())
print(tot_el_pile2())
