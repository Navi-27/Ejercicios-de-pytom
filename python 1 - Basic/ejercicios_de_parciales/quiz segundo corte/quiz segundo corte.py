lista = []

n = int(input("ingresa la longitud de la serie: "))

if n == 1:
    lista.append(0)
    print(lista)
else:
    if n == 2:
        lista.append(0)
        lista.append(1)
        print(lista)
    else:
        lista.append(0)
        lista.append(1)
        i = 1
        while i <= (n-2):
            temp = lista[i] + lista[i-1]
            lista.append(temp)
            i += 1
        print(lista)