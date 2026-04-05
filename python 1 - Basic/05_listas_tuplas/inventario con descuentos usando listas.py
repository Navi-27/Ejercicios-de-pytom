import sys
ID = []
Nombre = []
Precio = []
Stock = []
Categoria = []
historial_ventas = []


def opcion_invalida():
    x = int(input("Opcion invalida\npara volver al menu principal ingresa 1 sino 2 para salir \n->"))
    if x == 1:
        menu()
    else:
        salir()

def validar_convertir_a_entero(x):
    try:
        x = int(x)
        return True
    except:
        return False

def validar_convertir_a_float(x):
    try:
        x = float(x)
        return True
    except:
        return False

def agregar_producto():

    print("--------Bienvenido al sistema de creacion de productos---------")
    id = input("ID del producto: ")
    if validar_convertir_a_entero(id):
        id = int(id)
        if id in ID:
            print("El id ingresado ya esta en uso, por favor seleciona otro id")
            agregar_producto()
        else:
                idTemp = int(id)
                NombreProduct = str(input("Nombre del producto: "))
                nombreTemp = NombreProduct
                PrecioProduct = (input("Precio del producto: "))
                if validar_convertir_a_float(PrecioProduct):
                    PrecioProduct = float(PrecioProduct)
                    if PrecioProduct > 0:
                        precioTemp = PrecioProduct
                        CantidadStock = int(input("Cantidad en stock: "))
                        if validar_convertir_a_float(CantidadStock):
                            CantidadStock = float(CantidadStock)
                            if CantidadStock >= 0:
                                cantidadTemp = CantidadStock
                                CategoriaProduct = (input("Categoria del producto: "))
                                if CategoriaProduct == "" or CategoriaProduct == int or CategoriaProduct == float:
                                    x = int(input("La categoria no puede quedar vacia y debe ser un texto, para volver a intentar ingresa 1 sino 2 para salir\n -> "))
                                    if x == 1:
                                        agregar_producto()
                                    else:
                                        salir()
                                else:
                                    CategoriaProductTemp = CategoriaProduct
                                    ID.append(idTemp)
                                    Nombre.append(nombreTemp)
                                    Precio.append(precioTemp)
                                    Stock.append(cantidadTemp)
                                    Categoria.append(CategoriaProductTemp)
                                    historial_ventas.append(0)
                                    x = int(input("Producto guardado con exito\n Si deseas agregar otro producto ingresa 1 sino 2 para volver al menu principal\n-> "))
                                    if x == 1:
                                        agregar_producto()
                                    else:
                                        menu()
                            else:
                                x = int(input("La cantidad debe ser un numero entero y no puede quedar vacio, por favor ingresa una cantidad valida, para volver a intentar ingresa 1 sino 2 para salir\n -> "))
                                if x == 1:
                                    agregar_producto()
                                else:
                                    salir()
                        else:
                            x = int(input("La cantidad debe ser un numero entero y no puede quedar vacio, por favor ingresa una cantidad valida, para volver a intentar ingresa 1 sino 2 para salir\n -> "))
                            if x == 1:
                                agregar_producto()
                            else:
                                salir()
                    else:
                        x = int(input("El Precio del procducto debe ser un numero mayor a 0, debe ser un numero entero o decimal y no puede quedar vacio, por favor ingresa un precio valido, para volver a intentar ingresa 1 sino 2 para salir\n -> "))
                        if x == 1:
                            agregar_producto()
                        else:
                            salir()
                    agregar_producto()
                else:
                    x = int(input("El Precio del procducto debe ser un numero mayor a 0, debe ser un numero entero o decimal y no puede quedar vacio, por favor ingresa un precio valido, para volver a intentar ingresa 1 sino 2 para salir\n -> "))
                    if x == 1:
                        agregar_producto()
                    else:
                        salir()
                    agregar_producto()
    else:
        x = int(input("El id deber se un numero entero, para volver a intentar ingresa 1 sino 2 para salir\n -> "))
        if x == 1:
            agregar_producto()
        else:
            salir()  

def buscar_por_id():
    id = int(input("Ingrese el ID del producto: "))
    if id in ID:
        posicion = ID.index(id)
        print(f"ID: {ID[posicion]}\nNombre: {Nombre[posicion]}\nPrecio: {Precio[posicion]}\nCantidad en stock: {Stock[posicion]}\nCategoria: {Categoria[posicion]}\nHistorial de venta es $ {historial_ventas[posicion]}")
        x = int(input("Para volver al menu principal ingresa 1 sino 2 para salir\n-> "))
        if x == 1:
            menu()
        else:
            salir()
    else:
        print("Producto no encontrado")
        x = int(input("Para volver a intentar ingresa 1 sino 2 para volver al menu principal\n-> "))
        if x == 1:
            buscar_por_id()
        else:
            menu()

def buscar_por_nombre():
    nombre = str(input("Ingresa el nombre del producto a buscar: "))
    if nombre in Nombre:
        posicion = Nombre.index(nombre)
        print(f"ID: {ID[posicion]}\nNombre: {Nombre[posicion]}\nPrecio: {Precio[posicion]}\nCantidad en stock: {Stock[posicion]}\nCategoria: {Categoria[posicion]}\nHistorial de venta es $ {historial_ventas[posicion]}")
        x = int(input("Para volver al menu principal ingresa 1 sino 2 para salir\n-> "))
        if x == 1:
            menu()
        else:
            salir()
    else:
        print("Producto no encontrado")
        x = int(input("Para volver a intentar ingresa 1 sino 2 para volver al menu principal\n-> "))
        if x == 1:
            buscar_por_nombre()
        else:
            menu()

def buscar_por_categoria():
    categoria = str(input("ingresa la categoria a buscar: "))
    if categoria in Categoria:
        for x in range(len(Categoria)):
            if Categoria[x] == categoria:
                print(f"ID: {ID[x]}\nNombre: {Nombre[x]}\nPrecio: {Precio[x]}\nCantidad en stock: {Stock[x]}\nCategoria: {Categoria[x]}\nHistorial de venta es $ {historial_ventas[x]}")
    else:
        print("Categoria no encontrada")
        l = int(input("Para volver a intentar ingresa 1 sino 2 para volver al menu principal\n-> "))
        if l == 1:
            buscar_por_categoria()
        else:
            menu()
    i = int(input("Para volver al menu principal ingresa 1 o si quieres buscar otra categoria ingresa 2\n-> "))
    if i == 1:
        menu()
    elif i == 2:
        buscar_por_categoria()
    else:
        opcion_invalida()

def buscar_producto():
    dependencia = int(input("Bienvenido al sistema de busqueda de productos\n1. Buscar por ID\n2. Buscar por nombre\n3. Buscar por categoria\n4. Volver al menu principal\n-> "))
    if dependencia == 1:
        buscar_por_id()
    elif dependencia == 2:
        buscar_por_nombre()
    elif dependencia == 3:
        buscar_por_categoria()
    elif dependencia == 4:
        menu()
    else:
        opcion_invalida() 

def comprar():
    print(ID)
    id = int(input("ingresa el id a comprar: "))
    if id in ID:
        encontrado = False
        for i in range(len(ID)):
            if id == ID[i]:
                encontrado = True
                print(f"Producto encontrado\nID: {ID[i]}\nNombre: {Nombre[i]}\nPrecio: {Precio[i]}\nCantidad en stock: {Stock[i]}\nCategoria: {Categoria[i]}")
                cantidadCompra = int(input("Ingresa la cantidad a comprar\n-> "))
                if cantidadCompra > Stock[i]:
                    b = int(input(f"Cantidad insuficiente de productos, en el momento solo hay {Stock[i]} disponibles\n para vovler a comprar digita 1 sino 2: "))
                    if b == 1:
                        comprar()
                    else:
                        salir()
                else:
                    PrecioProducto = Precio[i]
                    PrecioTotal = cantidadCompra * PrecioProducto
                    if cantidadCompra > 5 and PrecioTotal >100:
                        PrecioDescuento = PrecioTotal - (PrecioTotal*0.15)
                        b = int(input(f"el total a pagar es de {PrecioDescuento}\n quiers confirmar la compra?\n1. si\n2. no\n->"))
                        if b == 1:
                            CantidadTemp = Stock[i]
                            temp = CantidadTemp - cantidadCompra
                            Stock[i] = temp
                            historial_ventas[i] = PrecioTotal
                            x =int(input("Compra Exitosa\nCantidad de inventario actualizada\npara volver al menu inserta 1 sino 2: "))
                            if x == 1:
                                menu()
                            else:
                                salir()
                        else: 
                            salir()
                    elif cantidadCompra > 5 and PrecioTotal <100:
                        PrecioDescuento = PrecioTotal - (PrecioTotal*0.1)
                        b = int(input(f"el total a pagar es de {PrecioDescuento}\nquiers confirmar la compra?\n1. si\n2. no\n->"))
                        if b == 1:
                            CantidadTemp = Stock[i]
                            temp = CantidadTemp - cantidadCompra
                            Stock[i] = temp
                            historial_ventas[i] = PrecioTotal
                            x =int(input("Compra Exitosa\nCantidad de inventario actualizada\npara volver al menu inserta 1 sino 2: "))
                            if x == 1:
                                menu()
                            else:
                                salir()
                        else:
                            salir()
                    elif cantidadCompra <5 and PrecioTotal > 100:
                        PrecioDescuento = PrecioTotal - (PrecioTotal*0.5)
                        b = int(input(f"el total a pagar es de {PrecioDescuento}\nquiers confirmar la compra?\n1. si\n2. no\n->"))
                        if b == 1:
                            CantidadTemp = Stock[i]
                            temp = CantidadTemp - cantidadCompra
                            Stock[i] = temp
                            historial_ventas[i] = PrecioTotal
                            x =int(input("Compra Exitosa\nCantidad de inventario actualizada\npara volver al menu inserta 1 sino 2: "))
                            if x == 1:
                                menu()
                            else:
                                salir()
                        else:
                            salir()
                return
        if not encontrado:
            x = int(input("Articulo no encontrado\nsi deseas comprar otro articulo ingresa 1 sino 2: "))
            if x == 1:
                comprar()
            else:
                salir()
    else:
        x = int(input("Articulo no encontrado\nsi deseas comprar otro articulo ingresa 1 sino 2: "))
        if x == 1:
            comprar()
        else:
            salir()

def salir():
    print("Gracias por usar nuestros servicios")
    sys.exit() 

def menu():
    Opcion_Menu = int(input("--------MENU--------\n1. Agregar un producto \n2. Buscar un producto\n3. Comprar\n4. Salir\n-> "))
    if Opcion_Menu == 1:
        agregar_producto()
    elif Opcion_Menu == 2:
        buscar_producto()
    elif Opcion_Menu == 3:
        comprar()
    elif Opcion_Menu == 4:
        salir()
    else:
        opcion_invalida()

menu()

 
