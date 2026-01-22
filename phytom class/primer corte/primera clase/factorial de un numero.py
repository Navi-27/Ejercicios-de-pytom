x = int(input("ingresa el numero a convertir a factorial: "))
y = 1
temp = x
while(x>1):
    y = y * x
    x -= 1
print(f"el factorial de {temp} es {y}")