i = int(input("ingresa el rango inicial"))
f = int(input("ingresa el rango final"))
ContPar = 0
ContImp = 0

for x in range(i, f+1):
    if x % 2 == 0:
        ContPar += 1
    else:
        ContImp += 1

print(f"hay {ContImp} impares y {ContPar} pares")
