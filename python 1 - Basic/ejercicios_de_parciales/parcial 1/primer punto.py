x = int(input("Ingresa un numero: "))
i = 1
j = 1
contador = 0

while i < 7:
    j = 1
    while j < 7:
        r = i + j
        if r == x:
            contador +=1
        j += 1
    i += 1



print(f"hay {contador} combinaciones para obtener {x}")