x = int(input("ingresa el numero: "))
suma = 0
i = 1
while i <= x:
    if x % i == 0:
        suma += i
    i += 1

dupla = x * 2

if suma > dupla:
    print("El numero es abundante")
else:
    print("El numero no es abundante")

