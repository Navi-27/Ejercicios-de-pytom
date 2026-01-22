import random

n = int(input("ingresa la longitud de la lista: "))

lista = []

for x in range(n):
    v = random.randint(1, n)
    lista.append(v)

def primos(lista):
    listaPrimos = []
    for x in lista:
        t = 1
        contador = 0
        while t <= x:
            if x % t == 0 :
                contador += 1
            t += 1
        if contador == 2:
            listaPrimos.append(x)
    return listaPrimos

print(lista)
print(primos(lista))