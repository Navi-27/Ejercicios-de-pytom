lista = []
longitud = int(input("ingresa la longitud de la lista "))

def mayor_a_2():
    lista.append(1)
    lista.append(1)

    temp = 1
    k = 1
    for i in range(longitud - 2):
        temp = temp + k
        lista.append(temp)
        k += 1
        i += 1
    print(lista)

def igual_a_2():
    lista.append(1)
    lista.append(1)
    print(lista)

def igual_a_1():
    lista.append(1)
    print(lista)

if longitud == 1:
    igual_a_1()
elif longitud == 2:
    igual_a_2()
else:
    mayor_a_2()


