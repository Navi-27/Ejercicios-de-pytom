import random
lista = []
pares = []
impares = []
i = int(input("inicio"))
f = int(input("final"))

for x in range(i ,(f+1)):
    v = random.randint(i ,f)
    lista.append(v)

for x in lista:
    if (x % 2) == 0:
        pares.append(x)
    else:
        impares.append(x)

print(f"lista original {lista}")

print(f"lista de impare {impares}")
print(f"lista de pares {pares}")

buscar = int(input("ingresa el numero a buscar"))
contador = 0
if buscar in lista:
    print("numero encontrado")
else:
    print("numero no encontrado")

eliminar = int(input("ingresa el numero a eliminar"))

for x in lista:
    if eliminar in lista:
        lista.remove(eliminar)

print(lista)




