aa = int(input("ingresa el año actual: "))
an = int(input("ingresa el año de nacimiento: "))

e = aa - an

print(f"tu edad actual es: {e}")

if e >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")