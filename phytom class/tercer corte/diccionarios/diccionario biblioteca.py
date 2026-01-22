
libro = {}
genero = []

nombre = input("ingresa el nombre del libro: ")
autor = input("ingresa el nombre del autor: ")
anio = int(input("ingresa el anio de publicacion del libro: "))

c = int(input("ingresa la cantidad de generos que tiene el libro: "))

for i in range(1 ,c+1):
    gn = input(f"genero {i}: ")
    genero.append(gn)

libro = {
    "nombre" : nombre,
    "autor" : autor,
    "anio" : anio,
    "genero" : genero,
}

print(libro)


buscar = input("ingresa el genero a buscar: ")
if buscar in genero:
    print(f"el libro {nombre} tiene el genero {buscar}, por lo tanto fue eliminado de la biblioteca")
    genero.remove(buscar)
else:
    print(f"el libro {nombre} no tiene el genero {buscar}, por lo tanto no fue eliminado de la biblioteca")

libro["anio"] = int(input("ingresa el nuevo anio de publicacion del libro:"))


print(libro)
print("\nDirectorio:")
for clave, valor in libro.items():
    print(f"{clave.capitalize()}: {valor}")

