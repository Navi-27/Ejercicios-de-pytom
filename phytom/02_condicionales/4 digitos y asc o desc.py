number = input("ingresa 4 digitos: \n-> ")
r = number
n = len(number)

if n < 5 and n > 3:
    number = int(number)
    u = (number) % 10
    d = (number // 10) % 10
    c = (number // 100) % 10
    z = (number // 1000) 

    if (z < c < d < u):
        print("El numero cumple la condicion de 4 cifras, y es ascendente")
    else:
        if ( z > c > d > u):
            print("El numero cumple la condicion de 4 cifras, y es desendente")
        else:
            print("El numero cumple la condicion de 4 cifras, pero no esta ordenado ni ascendete ni descentemente")
else:
    print("Numero no valido, ingrese un numero de 4 digitos")