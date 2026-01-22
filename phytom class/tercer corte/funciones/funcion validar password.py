
n = input("ingresa tu contraseña: ")

password = []
especiales = []

l = "@#$%&*!"


for x in n:
    password.append(x)

for x in l:
    especiales.append(x)

print(password)
print(especiales)

def validarLongitud(n):
    if len(n) >= 8:
        validar = 1
    else:
        validar = 0
    return validar

def validarMayusculaInicial(password):
    if password[0] >= "0" and password[0] <= "9":
        validar = 0
    elif password[0] >= "A" or password[0] <= "Z" or password[0] >= "a" or password[0] <= "z":
        validar = 1
    else:
        validar = 1
    return validar

def validarMayusculaYEspacial(password):
    mayuscula = 0
    minuscula = 0
    Especiales = 0
    for x in password:
        if x >= "A" and x <= "Z":
            mayuscula += 1
        if x >= "a" and x <= "z":
            minuscula += 1
        if x in especiales:
            Especiales += 1
    if mayuscula > 0 and minuscula > 0 and Especiales > 0:
        validar = 1
    else:
        validar = 0
    for x in password:
        if x == " ":
            validar = 0
    return validar



m = validarMayusculaInicial(password)
z = validarLongitud(n)
u = validarMayusculaYEspacial(password)
validacion = m + z + u


if validacion == 3:
    print("contraseña valida")
else:
    print("contraseña invalida")