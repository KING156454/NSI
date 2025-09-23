def presence(n,liste):
    for i in range(len(liste)):
        if n == liste[i]:
            return True
    return False



def presence2(n , liste):
    if len(liste) ==0 :
        return False
    return (liste[0] == n) or (presence2(n,liste[1:]))

listea = [1,2,3,4,5,6,7,8,9]

print(presence(5,listea))
print(presence2(10,listea))