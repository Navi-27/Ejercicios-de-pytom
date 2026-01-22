
directorio = {}
cant = int(input("cuantas personas tiene el directorio?: "))


for i in range(cant):
    nombre = input("nombre: ")
    direccion = input("direccion: ")
    ciudad = input("ciudad: ")
    v = 0
    v = int(input(f"ingresa la cantidad de telefonos de {nombre}: "))
    telefonos = []
    for j in range(v):
        telefono = int(input(f"telefono de {nombre}: "))
        telefonos.append(telefono)

    directorio[nombre] = {
        "ciudad" : ciudad,
        "direccion" : direccion,
        "telefonos" : telefonos,
    }
    
print(directorio)
print("\nDirectorio:")
for nombre, datos in directorio.items():
    print(f"Nombre: {nombre}")
    for clave, valor in datos.items():
        print(f"{clave.capitalize()}: {valor}")



    