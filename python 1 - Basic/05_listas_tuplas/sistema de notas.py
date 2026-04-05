materias=[]

numMaterias = int(input("ingresa el numero de materias a digitar"))

for j in range(numMaterias):
    temp = str(input(f"ingresa el nombre de la materia "))
    nota = float(input(f"ingresa la nota de la materia {temp} "))
    if nota < 3:
        materias.append(temp)

print(f"materias reprobadas: {materias}")