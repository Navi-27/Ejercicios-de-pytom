

from ast import mod
from nt import remove


numeros = []

ran = int(input("ingresa la longitud de la lista"))

for x in range(ran):
    num = int(input("numero: "))
    numeros.append(num)
print(numeros)

multiplo = int(input("multiplos de -> "))

x = 0
while x < len(numeros):
    if numeros[x] % multiplo == 0:
        eliminar = numeros[x]
        numeros.remove(eliminar)
        x -=1
    x += 1
    

print(numeros)
