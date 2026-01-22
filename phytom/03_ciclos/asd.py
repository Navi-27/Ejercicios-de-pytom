dias = int(input("ingresa el numero de dias: "))
contador = 1
ValMax = 0
ValAnterior = 0

while(contador <= dias):
    numActual = float(input(f"Dia {contador}: "))
    if contador > 1:
        if numActual > ValAnterior:
            resultado = (ValAnterior-numActual)*-1
            if(resultado > ValMax):
                ValMax = resultado
    contador += 1
    ValAnterior = numActual

print(f"La mayor alza fue de: {round(ValMax)}")