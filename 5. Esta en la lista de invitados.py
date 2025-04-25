invitados = ["ana", "luis", "sofía"]

while True:

    nombre = input("Ingresa tu nombre: ").strip().lower()

    if not nombre:
        print("     No ingresaste ningún nombre")
        continue


    if nombre in invitados:
        print("     Estas en la lista de invitados")
    else:
        print("     No esta en la lista de invitados")


    while True:
        respuesta = input("Quieres verificar otro nombre? (si/no): ").strip().lower()

        if respuesta == "si":
            break  
        elif respuesta == "no":
            print("     Adios")
            exit()
        else:
            print("     Escribe solo 'si' o 'no'")


