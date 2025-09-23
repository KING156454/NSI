def compte(n):
    for i in range(1, n+1):
        print(i)
#compte(3)

def compte2(n):
    if n>0:
        compte2(n-1)
        print(n)

compte2(3)