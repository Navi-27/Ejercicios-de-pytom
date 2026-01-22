import random
lista = []
i = int(input("inicio: "))
f = int(input("final: "))

for x in range(i ,(f+1)):
    v = random.randint(i ,f)
    lista.append(v)
print(lista)

b = int(input("ingresa el valor a buscar: "))
contador = 0
if b in lista:
    for x in lista:
        if x == b:
            contador += 1
    if contador > 1:
        print(f"el numero {b} aparece {contador} veces en la lista")
    else:
        print(f"el numero {b} aparece {contador} vez en la lista")
else:
    print("el numero no parece en la lista")



