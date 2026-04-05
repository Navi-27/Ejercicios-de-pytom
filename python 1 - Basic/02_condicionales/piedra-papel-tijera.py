import random

print("Elige una de las siguientes opciones \n 1. Piedra \n 2. Papel \n 3. Tijera")
x = int(input("Elige una opcion: "))

maq = random.randint(1, 3)

if x == maq:
    print(f"Empate la maquina eligio {maq}")
elif (x == 1 and maq == 3) or (x == 2 and maq == 1) or ( x == 3 and maq == 2):
    print(f"Ganaste la maquina eligio {maq}")
else:
    print(f"Perdiste la maquina eligio {maq}")