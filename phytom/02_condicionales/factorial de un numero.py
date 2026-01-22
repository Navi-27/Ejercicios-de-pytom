#Haz un programa para calcular el factorial de un número ingresado por el usuario usando while.
num = int(input("ingresa el numero no mayor a 100: "))
temp = num * (num-1)
i = num -2
if num <= 100:
    while i > 0 :
        temp = temp * i
        i = i - 1
    print(temp)
else:
    print("el numero es mayor a 100")

    



