def minimum(liste):
    minimum = liste[0]
    for i in liste:
        if i <= minimum:
            minimum= i
    return minimum

listea = [1,2,3,4,5,6,0,8,9]
print(minimum(listea))

def minimum2(liste):
    if len(liste) == 1 :
        return liste[0]
    nb = minimum2(liste[1:])
    return min(liste[0],nb)
print(minimum2(listea))