
def lista1():
    x = int(input("ingresa cuantos numeros vas a ingresar"))
    lista = []
    while x > 0:
        lista.append(int(input("ingresa el numero: ")))
        x -= 1
    
    contador = 0
    
    for c in range(len(lista)):
        if lista[c] < 10:
            lista[c] = 0
        elif lista[c] > 20:
            lista[c] = 1
        else:
            contador += 1 
    print(f"{lista} y {contador} no se cambiaron")
            
lista1()