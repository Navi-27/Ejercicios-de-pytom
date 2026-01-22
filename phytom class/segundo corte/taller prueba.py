Totales=[]



def conteo():
    unis = int(input("ingresa el numero de universidades -> "))

    contadorA = 0
    contadorR = 0
    contadorN = 0
    contadorNulo = 0
    ContadorAceptan = 0
    ContadorRechaza = 0
    ContadorEmpate = 0
    
    p = 1
    for p in range(unis):
        contadorA = 0
        contadorR = 0
        contadorB = 0
        contadorNulo = 0
        r = 2
        nomb = str(input("Universidad: "))
        while r > 1:
            voto = str(input("voto: "))
            if voto == "A" or voto == "a":
                contadorA += 1
            elif voto == "R" or voto == "r":
                contadorR += 1
            elif voto == "B" or voto == "b":
                contadorB += 1
            elif voto == "X" or voto == "x":
                r = 0
            else:
                contadorNulo += 1
            r += 1
        print(f"{nomb}: {contadorA} aceptan, {contadorR} rechazan, {contadorB} blancos, {contadorNulo} nulos.")
        if contadorA > contadorR:
            ContadorAceptan += 1
        elif contadorR > contadorA:
            ContadorRechaza +=1
        elif contadorA == contadorR:
            ContadorEmpate += 1
    Totales.append(ContadorAceptan)
    Totales.append(ContadorRechaza)
    Totales.append(ContadorEmpate)
    print(f"\nUniverdidades que aceptan: {Totales[0]}\nUniverdidades que Rechazan: {Totales[1]}\nUniversidades que Empatan: {Totales[2]}")


conteo()