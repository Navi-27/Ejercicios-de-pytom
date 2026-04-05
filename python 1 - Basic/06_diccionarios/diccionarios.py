# Diccionario vacío
diccionario_vacio = {}

# Diccionario con elementos
diccionario = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'Madrid'
    }

# Usando la función dict()
diccionario = dict(nombre="Juan", edad=30, ciudad="Madrid")
# Acceder a un valor usando la clave
nombre = diccionario['nombre']  # 'Juan'

# Usando el método get()
edad = diccionario.get('edad')  # 30

# Usando get() con valor predeterminado
telefono = diccionario.get('telefono', 'No disponible')  # 'No disponible'
print(diccionario)
print(nombre)
print(edad)
print(telefono)

# Agregar un nuevo par clave-valor
diccionario['telefono'] = '123456789'

# Modificar un valor existente
diccionario['edad'] = 31
edad = diccionario.get('edad') 
telefono = diccionario.get('telefono', 'No disponible')
print(nombre)
print(edad)
print(telefono)
print(diccionario)
# Eliminar un par clave-valor usando del
del diccionario['ciudad']

# Eliminar y obtener un valor usando pop()
telefono = diccionario.pop('telefono')  # '123456789'
print(telefono)
print("iterar: ")
# Iterar sobre las claves
for clave in diccionario:
    print(clave)

# Iterar sobre los valores
for valor in diccionario.values():
    print(valor)
     

# Iterar sobre los pares clave-valor
for clave, valor in diccionario.items():
   print(clave, valor)
   




# Diccionario con elementos
diccionario = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'Madrid'
}

# Capturar valores desde el input
diccionario['nombre'] = input("Ingresa el nombre: ")
diccionario['edad'] = int(input("Ingresa la edad: "))
diccionario['ciudad'] = input("Ingresa la ciudad: ")

# Imprimir los valores del diccionario
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

print(diccionario)

# Diccionario para almacenar varios nombres con sus datos
diccionario_personas = {}

# Bucle para agregar personas
for x in range(2):
    nombre = input("Ingresa el nombre: ")
    
    
    # Capturar otros datos
    edad = int(input(f"Ingresa la edad de {nombre}: "))
    ciudad = input(f"Ingresa la ciudad de {nombre}: ")

    # Agregar los datos de la persona al diccionario
    diccionario_personas[nombre] = {
        'edad': edad,
        'ciudad': ciudad
    }

# Imprimir los datos de todas las personas
print("\nDatos de las personas:")
for nombre, datos in diccionario_personas.items():
    print(f"Nombre: {nombre}")
    for clave, valor in datos.items():
        print(f"  {clave.capitalize()}: {valor}")