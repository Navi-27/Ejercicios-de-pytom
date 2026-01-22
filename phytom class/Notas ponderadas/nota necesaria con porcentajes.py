## este archivo calcula la nota necesaria que debes sacar en el tercer corte para pasar la materia

def nota_necesaria(pon1, pon2, nota_objetivo):

    pon1 = float(input("Ingresa la nota del primer corte: "))
    pon2 = float(input("Ingresa la nota del primer corte: "))

    temp1 = pon1 * 0.3
    temp2 = pon2 * 0.3

    notatemp = temp1 + temp2

    if notatemp == 3:
        print("tu ponderada es 3 por lo tanto no necesitas mas nota para pasar la materia")
        return
    else:
        x = int(input("ingresa cuantas notas se tomaron en el tercer corte: "))
        lista_notas_indicativo = []
        lista_notas_porcentaje = []
        lista_notas_final = []

        print("primero catalogamos las notas del tercer corte dejando el parcial al final y su respectivo porcentaje")
        for i in range(x):
            lista_notas_indicativo.append(input(f"Nombre de la nota {i+1}: "))

        print("ahora ingresa el porcentaje de cada nota (en decimal)")
        for i in range(x):
            lista_notas_porcentaje.append(float(input(f"Porcentaje de {lista_notas_indicativo[i]}: ")))

        print("ahora ingresa la nota que sacaste en cada una a excepcion del parcial")
        for i in range(x-1):
            nota = float(input(f"Nota obtenida en {lista_notas_indicativo[i]}: "))
            lista_notas_final.append(nota * lista_notas_porcentaje[i])

        suma_componentes_tercer_corte = sum(lista_notas_final)

        ponderado12 = (pon1 * 0.3) + (pon2 * 0.3)
        contrib_tercer_corte_actual = suma_componentes_tercer_corte * 0.4

        falta = nota_objetivo - (ponderado12 + contrib_tercer_corte_actual)

        if falta <= 0:
            print("Con tus notas actuales ya tienes una ponderada de 3, no necesitas mas nota para pasar la materia")
        else:
            porcentaje_parcial_interno = lista_notas_porcentaje[-1]
            aporte_parcial_en_final = 0.4 * porcentaje_parcial_interno
            nota_requerida = falta / aporte_parcial_en_final
            print(f"Necesitas sacar al menos {round(nota_requerida, 2)} en {lista_notas_indicativo[-1]} para pasar con {nota_objetivo}")
        

nota_necesaria(0, 0, 3)