import random

n = int(input("ingresa la longitud de la lista: "))

lista = []
x = 1
while x < (n*100):
    lista.append(x)
    x += 1


def primos(lista):
    listaPrimos = []
    contador2 = 0
    for x in lista:
        t = 1
        contador = 0
        while t <= x:
            if x % t == 0 :
                contador += 1
            t += 1
        if contador == 2:
            listaPrimos.append(x)
            contador2 +=1
        if contador2 == n:
            break
    return listaPrimos

listaFinal = []

x = primos(lista)

temp = 0
for p in x:
    temp += p
    listaFinal.append(temp)
    
print(listaFinal)