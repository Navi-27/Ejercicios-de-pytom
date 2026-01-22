lista = []
listaFactorial = []
listaSuma = []

n = int(input("ingresa la longitud de la serie"))

for x in range(1 ,(n*2)+2):
    if x % 2 == 0:
        lista.append(x)
    else:
        t = 1
print(lista)

for p in lista:
    y = 1
    t = p
    while(t>1):
        y = y * t
        t -= 1
    listaFactorial.append(y)

print(listaFactorial)

for k in listaFactorial:
    suma = 0
    p = str(k)
    for l in p:
        b = int(l)
        suma += b
    listaSuma.append(suma)
    

print(listaSuma)
    

    