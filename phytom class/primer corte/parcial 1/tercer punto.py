dia = int(input("ingresa el numero de dias: "))
i = 2
alza = 0
dia1 = float(input("dia 1: "))
temp = 0
while i <= dia:
    diax = float(input(f"dia {i}: "))
    alza = (dia1 - diax)
    if alza < 0:
        alza = alza * -1
    if temp > alza:
        maximo = temp
    else:
        maximo = alza
    temp = alza 
    i += 1

print(f"el alza maximo es{maximo}")

