segundos = int(input("ingresa los segundos a calcular: "))
minutos = 0
while segundos >= 0:
    segundos = segundos-60
    if segundos >= 0:
        minutos += 1

print(f"le faltan {segundos*-1} para convertirse en 1 min ")
print(f"y tienes {minutos}")