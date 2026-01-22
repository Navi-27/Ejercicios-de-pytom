

print("Bienvenido al sistema de notas")
CantEstudiantes = int(input("ingresa la cantidad de estudiantes: "))
definitiva = 0

for i in range(1, CantEstudiantes+1):
    print("Ingrese el nombre del estudiante")
    nombre = input()
    CantMaterias = int(input(f"ingresa la cantidad de materias de {nombre}: "))
    for j in range(1, CantMaterias+1):
        print(f"ingresa el nombre de la materia {j}: ")
        materia = input("-> ")
        CantNotas = int(input(f"ingresa la cantidad de notas de {materia}: "))
        definitiva = 0
        for k in range(1, CantNotas+1):
            nota = float(input(f"ingresa la nota {k}: "))
            definitiva = definitiva + nota
        definitiva = definitiva / CantNotas
        if definitiva < 3:
            print(f"la nota definitiva de {materia} es: {round(definitiva,2)} por lo tanto perdio")
        else:
            print(f"la nota definitiva de {materia} es: {round(definitiva,2)} por lo tanto paso")    


# print("Bienvenido al sistema de notas")
# CantEstudiantes = int(input("ingresa la cantidad de estudiantes: "))
# definitiva = 0
# x = 1

# while(x <= CantEstudiantes):
#     print("Ingrese el nombre del estudiante")
#     nombre = input()
#     CantMaterias = int(input(f"ingresa la cantidad de materias de {nombre}: "))
#     x += 1
#     y = 1
#     while(y <= CantMaterias):
#         print(f"ingresa el nombre de la materia {y}: ")
#         materia = input("-> ")
#         CantNotas = int(input(f"ingresa la cantidad de notas de {materia}: "))
#         y += 1
#         k = 1
#         while(k <= CantNotas):
#             nota = float(input(f"ingresa la nota {k}: "))
#             definitiva = definitiva + nota
#             k += 1
#         definitiva = definitiva / CantNotas
#         print(f"la nota definitiva de {materia} es: {definitiva}")