
libro = {}
genero = []

nombre = input("ingresa el nombre del libro: ")
autor = input("ingresa el nombre del autor: ")

c = int(input("ingresa la cantidad de generos que tiene el libro: "))

for i in range(c):
    gn = input(f"genero {i}: ")
    genero.append(gn)

libro = {
    "nombre" : nombre,
    "autor" : autor,
    "genero" : genero,
}

print(libro)