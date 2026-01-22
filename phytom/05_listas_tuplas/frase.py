oracion = []
temp = []
final = []


frase = str(input("ingresa la frase a comprobar: \n"))
palabra = ""

for letra in frase:
    if letra != " ":
        palabra += letra
    else:
        oracion.append(palabra)
        palabra = ""
oracion.append(palabra)

for i in range(len(oracion)):
    if oracion[i] not in temp:
        temp.append(oracion[i])
        

radio = len(temp)

for x in range(len(temp)):
    contador = 0
    for j in range(len(oracion)):
        if temp[x] == oracion[j]:
            contador += 1
    final.append(f"{temp[x]}: {contador}")

print(final)
