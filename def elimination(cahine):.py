def elimination(chaine):
    resultat = ""
    for i in chaine :
        if i != " " :
            resultat += i
    return resultat
print(elimination("a a a"))

chaine_caractere = [",","?","."," ",";","/",":","!","'","-","_"]
def elimination2(chaine):
    if chaine == "":
        return ""
    c = chaine[0]
    if c in chaine_caractere:
        return elimination2(chaine[1:])
    else :
        return c + elimination2(chaine[1:])
print(elimination2("j'aime les patates_douce ,?;:!/::!"))