def doublement(chaine):
    resultat = ""
    for c in chaine :
        resultat += 2*c
    return resultat
print(doublement("robot"))


def doublement2(chaine) :
    if len(chaine) == 0:
        return chaine
    return chaine[0]*2 + doublement2(chaine[1:])
print(doublement2("robot"))