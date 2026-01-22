a = float(input("ingresa la varianle a diferente de 0:" ))

if a == 0:
    print("la variable a no puede ser 0")
else:
    b = float(input("ingresa la varianle b: " ))
    c = float(input("ingresa la varianle c: " ))
    if ((b**2 - 4*a*c)**0.5) < 0:
        print("al calcular la raiz da como resultado una raiz negativa, y la raiz no puede ser negativa")
    else:
        x1 = (-b + ((b**2 - 4*a*c)**0.5))/(2*a)
        x2 = (-b - ((b**2 - 4*a*c)**0.5))/(2*a)
        print(f"el resultado es: {x1} y {x2}")

