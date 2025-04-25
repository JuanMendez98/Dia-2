numeros = [10, 25, 42, 7, 56]

while True:
        
    while True:

        try:
            numero_usuario = float(input("Ingresa un numero: "))
            break
        except:
            print("     Ingresa un numero valido.")

    if numero_usuario in numeros:
            print(f"     El numero{numero_usuario: .0f} esta en la lista.")
    else:
        print(f"     El numero{numero_usuario: .0f} no esta en la lista.")

    while True:
        otro_intento = input("Desea intentar con otro numero? (si/no): ").lower().strip()
        if otro_intento == 'si':
            break 
        elif otro_intento == 'no':
            print("    Adios")
            break 
        else:
            print("Responde con 'si' o 'no'.")

    if otro_intento == 'no':
        break