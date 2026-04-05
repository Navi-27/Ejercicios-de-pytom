import random
lista = []
lista2 = []
iguales = []
noPrimera = []
noSegunda = []
m = int(input("ingresa el numero de elementos de la lista: "))
t =1
for i in range(m):
    lista.append(random.randint(1, m))
    lista2.append(random.randint(1, m))

for r in lista:
    for p in lista2: 
        if p in iguales:
            t += 1
        else:
            if r == p:
                iguales.append(p)


for p in lista2: 
    if p in noPrimera:
        rasdasa = 1
    else: 
        if p in iguales:
            t += 1
        else:
            noPrimera.append(p)


for p in lista: 
    if p in noSegunda:
        temporti = 1
    else:
        if p in iguales:
            t += 1
        else:
            noSegunda.append(p)


print(lista)
print(lista2)
print(f"Lista de numeros que aparecen en las dos listas {iguales}")
print(f"numeros que aparece en la Primera pero no en la Segunda {noSegunda}")
print(f"numeros que aparece en la Segunda pero no en la Primera {noPrimera}")
