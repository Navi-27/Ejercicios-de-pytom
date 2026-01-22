def generarLista():
    lista = []
    m = int(input("ingresa la longitud de la lista"))
    while m > 0:
        lista.append(int(input("ingresa el numero: ")))
        m -= 1

    n = int(input("ingresa las rotaciones a realizar: "))

    if n < len(lista):
        listAux = []

        x = (len(lista)) - (n)
        while x < (len(lista)):
            listAux.append(lista[x])
            x += 1





        c = 0
        while c < (len(lista))-(n):
            listAux.append(lista[c])
            c += 1       

        print(listAux)
    else:
        print("no se pudo realizar el cambio ya que el numero es mayor o igual a la longitud de la lista")


generarLista()