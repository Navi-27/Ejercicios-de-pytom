num1 = int(input("ingresa el numero 1: "))
num2 = int(input("ingresa el numero 2: "))
num3 = int(input("ingresa el numero 3: "))

if num1<num2 and num1<num3:
    print(f"{num1}es el numero menor")
    if num2<num3:
        print(f"{num2}es el del medio {num3}es el mayo")
    else:
        print(f"{num3}es el del medio {num2}es el mayo")
elif num2<num3 and num2<num1:
    print(f"{num2}es el numero menor")
    if num1<num3:
        print(f"{num1}es el del medio {num2}es el mayo")
    else:
        print(f"{num3}es el del medio {num1}es el mayo")
elif num3<num1 and num3<num2:
    print(f"{num3}es el numero menor") 
    if num2<num1:
        print(f"{num2}es el del medio {num1}es el mayo")
    else:
        print(f"{num2}es el del medio {num1}es el mayo") 