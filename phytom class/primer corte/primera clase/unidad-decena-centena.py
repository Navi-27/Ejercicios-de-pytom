x = int(input("ingresa el numero \n-> "))

u = x % 10
d = (x // 10) % 10
c = (x // 100) %10
z = (x // 1000) 


print(f"Unidad: {u} \nDecena: {d} \nCentena: {c} {z}")