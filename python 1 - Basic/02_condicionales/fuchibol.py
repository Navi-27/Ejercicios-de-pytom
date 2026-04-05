import random

print("Elige que seras \n1.Arquero \n2.Pateador")
user = int(input("-> "))

if user == 1:
    print("Tu seras el Arquero Elige a donde atajaras \n 1 2 3\n 4 5 6\n 7 8 9")
    opcion = int(input("-> "))
    maq = random.randint(1, 9)
    if opcion == maq:
        print(f"Atajaste el balon la maquina pateo a {maq}")
    else:
        print(f"Gol la maquina pateo a {maq}")
else:
    print("Tu seras el Pateador Elige a donde Patearas \n 1 2 3\n 4 5 6\n 7 8 9")
    opcion = int(input("-> "))
    maq = random.randint(1, 9)
    if opcion == maq:
        print(f"La maquina te tiro hacia el {maq} y atajo tu tiro")
    elif opcion >10 or opcion <1:
        print("votaste el panel")
    else:
        print(f"Goooool la maquina se lanzo {maq} y no atajo tu penal")
    