number = input("ingresa 4 digitos: \n-> ")
r = int(number)
n = len(number)
lista = []

if r % 2 ==0:
    for x in number:
        lista.append(x)

    repite = 0
    numero = 0

    for t in lista:
        contador = lista.count(t)
        if contador > 1:
            repite = 1
            numero = t
            break

    if repite < 0:
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
    else:
        print(f"el numero no es valido porque el numero {numero} se repite mas de una vez")  
else:
    print("ingresa numeros pares")