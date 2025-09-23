def somme(n):
    S= 0
    for i in range(1 , n+1):
        S += i
    print(S)
#somme(3)

def somme2(n):
    if n == 0:
        return 0
    return n + somme2(n - 1)

print(somme2(3))