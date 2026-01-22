## este archivo calcula la nota necesaria que debes sacar en el tercer corte para pasar la materia

def nota_necesaria(pon1, pon2, nota_final):

    pon1 = float(input("Ingresa la nota del primer corte: "))
    pon2 = float(input("Ingresa la nota del primer corte: "))

    nota = 3 - ((pon1 * 0.3) +(pon2 * 0.3))

    if nota <= 0:
        print("tu ponderada es 3 por lo tanto no necesitas mas nota para pasar la materia")
    else:
        nota_final = nota / 0.4
        print(f"Necesitas sacar al menos:  {round(nota_final, 2)} en el tercer corte para pasar la materia en 3")

nota_necesaria(0, 0, 3)