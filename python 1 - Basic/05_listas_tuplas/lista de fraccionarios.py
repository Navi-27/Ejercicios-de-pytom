fraccion = []


fraccion.append(1)

n = int(input("ingresa la logitud de la lista a imprimir"))
impar = 3
i = 1
if n >= 2:
    while i <= n-1:
        if i % 2 == 0:
            temp = f"-{i}/{impar}"
            fraccion.append(temp)
        elif i % 2 == 1:
            temp = f"{i}/{impar}"
            fraccion.append(temp)
        i += 1
        impar += 2

print(fraccion)



        

    