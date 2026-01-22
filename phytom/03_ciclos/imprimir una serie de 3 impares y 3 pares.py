n = int(input("¿Cuántos números quieres imprimir en la serie? "))

contador = 0
impar = 1
par = 2

while contador < n:
    # Imprime 3 impares
    impares_print = 0
    while impares_print < 3 and contador < n:
        print(impar, end=", " if contador < n - 1 else "")
        impar += 2
        contador += 1
        impares_print += 1
    # Imprime 3 pares
    pares_print = 0
    while pares_print < 3 and contador < n:
        print(par, end=", " if contador < n - 1 else "")
        par += 2
        contador += 1
        pares_print += 1




