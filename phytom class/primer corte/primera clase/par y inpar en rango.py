rangoInicial = int(input("ingresa el rango inicial: "))
rangoFinal = int(input("ingresa el rango final: "))
temp1 = rangoInicial
temp2 = rangoFinal
contador = 0
pares = ""
impares = ""
while(rangoInicial <= rangoFinal):
    if(rangoInicial % 2 == 0):
        contador += 1
        pares = pares + str(rangoInicial)+", " 
    rangoInicial += 1
print(f"la cantidad de numeros pares entre {temp1} y {temp2} es: {contador} \nlos numeros pares son: {pares}")

contador = 0
rangoInicial = temp1
rangoFinal = temp2
while(rangoInicial <= rangoFinal):
    if(rangoInicial % 2 != 0):
        contador += 1
        impares = impares + str(rangoInicial)+", " 
    rangoInicial += 1
print(f"la cantidad de numeros impares entre {temp1} y {temp2} es: {contador} \nlos numeros impares son: {impares}")
  

