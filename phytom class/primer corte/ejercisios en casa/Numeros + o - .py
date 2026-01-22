#Ejercicio
#Escribe un programa que solicite números hasta que el usuario ingrese el número cero, y muestra cuántos números positivos fueron introducidos.

contadorPositivos = 0
ContadorNegativos = 0 
contador = 1
print("INSTRUCCIONES\nIngresa numeros positivos o negativos tanto como quieras.\npara salir del programa ingresa 0")
while contador != 0:
    contador = int(input("-> "))
    if contador > 0 :
        contadorPositivos += 1
    elif contador < 0 :
        ContadorNegativos += 1
    else:
        contador = 0

print(f"El numero total de numeros positivos ingresador es de {contadorPositivos}, y el numero total de numeros negativos ingresados es de {ContadorNegativos}")
