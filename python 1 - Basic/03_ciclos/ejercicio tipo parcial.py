suma = []
n = int(input("ingrese los elementos de la lista: "))
m = int(input("ingrese la cantidad de listas: "))

general = []

k = 1
for i in range(m):
    temp = []

    for r in range(1,n+1):
        temp.append(r**k)
    k += 1
    suma.append(sum(temp))
    general.append(temp)

print(general)
print(f"La sumatoria de cada lista es \n{suma}")