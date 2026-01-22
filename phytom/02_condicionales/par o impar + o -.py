num1 = float(input("ingresa el primer numero: "))
if num1 == 0:
    print("el numero es 0 y es un numero neutro")
else:
    resulado = num1 % 2
    if resulado == 0:
        print("el numero es par")
        if num1 >= 0:
            print("el numero es positivo")
        else:
            print("el numero es negativo")
    else:
        print("el numero es impar")
        if num1 >= 0:
            print("el numero es positivo")
        else:
            print("el numero es negativo")