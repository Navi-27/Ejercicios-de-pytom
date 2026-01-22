matriz=[]

n = int(input("ingresa el tamaño de la matriz: "))

if n % 2 != 0 or n == 1:
    print("no se puede realizar la matriz")
else:
    u = 1
    i = 1
    while i < n:
        r = 1
        t = n
        while r <= t:
            if r < t or r > t:
                matriz.append(0)
            elif r == t:
                matriz.append(1)
                t -= u
            r += 1
        i += 1
        u +=1



print(matriz)