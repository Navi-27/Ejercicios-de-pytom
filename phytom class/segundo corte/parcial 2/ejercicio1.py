lista = []
listamultiplicada = []

n = int(input("ingresa la longitud de la serie: "))

if n == 1:
    lista.append(0)
    print(f"Lista original = {lista}")
else:
    if n == 2:
        lista.append(0)
        lista.append(1)
        print(f"Lista original = {lista}")
    else:
        lista.append(0)
        lista.append(1)
        i = 1
        while i <= (n-2):
            temp = lista[i] + lista[i-1]
            lista.append(temp)
            i += 1
        print(f"Lista original = {lista}")

if n == 1:
    listamultiplicada.append(0)
    print(f"lista multiplicada = {listamultiplicada}")
else:
    for x in range(0, n):
        if x % 2 != 0:
            listamultiplicada.append(lista[x] * 3)
        else:
            listamultiplicada.append(lista[x] * 2)
    print(f"lista multiplicada = {listamultiplicada}")






