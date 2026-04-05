lista =[]
abundante = []

n = int(input("ingresa la longitud de la lista: "))
i = 1
while i <= n:
    temp = int(input(f"numero {i}: "))
    lista.append(temp)
    i+=1

for v in lista:
    r = 1
    divisores = []
    if v < 0:
        v = v * -1
        if v == 0:
            p = "No"
            abundante.append(p)
        else:
            while r <= v:
                if v % r == 0:
                    divisores.append(r)
                r += 1
            temp = sum(divisores)
            if temp > (v * 2):
                p = "Si"
                abundante.append(p)
            else:
                p = "No"
                abundante.append(p)
    else:
        if v == 0:
            p = "No"
            abundante.append(p)
        else:
            while r <= v:
                if v % r == 0:
                    divisores.append(r)
                r += 1
            temp = sum(divisores)
            if temp > (v * 2):
                p = "Si"
                abundante.append(p)
            else:
                p = "No"
                abundante.append(p)

print(lista)
print(abundante)