elementos = int(input("ingresa la cantidad de valores que tendra la lista \n-> "))
lista=[]
impares=[]
pares=[]


for x in range(elementos):
    v = int(input(f"ingresa el numero: "))
    lista.append(v)

for x in lista:
    if (x % 2) == 0:
        pares.append(x)
    else:
        impares.append(x)
print(f"lista original {lista}")

print(f"lista de impare {impares}")
print(f"lista de pares {pares}")

    
