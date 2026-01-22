


def salario():
    sueldo = int(input("ingresa el salario del empleado"))
    if sueldo % 5 == 0 :
        contador100 = 0
        contador20 = 0
        contador50 = 0
        contador5 = 0
        while sueldo > 0:
            if sueldo >= 100:
                sueldo -= 100
                contador100 += 1
            elif sueldo >= 50:
                sueldo -= 50
                contador50 += 1
            elif sueldo >= 20:
                sueldo -= 20
                contador20 += 1
            elif sueldo >= 5:
                sueldo -= 5
                contador5 += 1
        print(f"se necesitan {contador100} billetes de 100")
        print(f"se necesitan {contador50} billetes de 50")
        print(f"se necesitan {contador20} billetes de 20")
        print(f"se necesitan {contador5} billetes de 5")
    else:
        print("ingresa un valor multiplo de 5")

salario()