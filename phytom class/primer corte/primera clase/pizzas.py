
cp = int(input("cuantas personas son? \n-> "))
pp = int(input("cuantas porciones se come cada una? \n-> "))
ppi = int(input("cuantas porciones trae la pizza? \n-> "))

total_porciones = cp * pp
pizzas_necesarias = (total_porciones + ppi - 1) // ppi
total = (pizzas_necesarias * ppi) - total_porciones


print(f"las personas se comeran {total_porciones} porciones,necesitamos {pizzas_necesarias} pizzas y sobran {total} porciones")