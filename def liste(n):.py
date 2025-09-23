def liste(liste):
    for i in range(len(liste)-1):
        if liste [i]>liste[i + 1]:
            return False
    return True



def liste2(liste):
    if len(liste)==1:
        return True
    return (liste[0]<=(liste[1])) and (liste2(liste[1:]))


listea = [1,2,3,4,5,6,7,8,9]
listeb = [1,2,3,8,5,6,7,8,9]
print(liste(listea))
print(liste2(listeb))

