totales = []
primos = []

n = int(input("ingresa la longitud de la lista: "))

for i in range(n):
    num = int(input(f"numero: "))
    totales.append(num)

for x in totales:
    t = 1
    contador = 0
    while t <= x:
        if x % t == 0 :
            contador += 1
        t += 1
    if contador == 2:
        primos.append(x)


print(primos)

# print(totales)