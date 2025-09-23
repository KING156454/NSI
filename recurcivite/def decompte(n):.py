def decompte(n):
    for i in range(3 ,-1 ,-1):
        print(i)
decompte(3)

def decompte2(n):
    if n < 0:
        return
    print(n)
    decompte2(n-1)
decompte2(3)