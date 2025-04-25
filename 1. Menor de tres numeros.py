while True:
    print("     Ingresa tres numeros para encontrar el menor")
    
    while True:
        try:
            numero1 = float(input("Ingresa el primer numero: "))
            break  
        except:
            print("     Ingresa un numero valido")
    
    while True:
        try:
            numero2 = float(input("Ingresa el segundo numero: "))
            break  
        except:
            print("     Ingresa un numero valido")
    
    while True:
        try:
            numero3 = float(input("Ingresa el tercer numero: "))
            break  
        except:
            print("     Ingresa un numero valido")
    
    if numero1 < numero2 and numero1 < numero3:
        print(f"     El numero menor es: {numero1}")
    elif numero2 < numero1 and numero2 < numero3:
        print(f"     El numero menor es: {numero2}")
    else:
        print(f"     El numero menor es: {numero3}")
    
    while True:
        otra_vez = input("Quieres volver a hacerlo? (si/no): ").lower().strip()
        if otra_vez == 'si':
            break  
        elif otra_vez == 'no':
            print("     Adios")
            break  
        else:
            print("     Responde con 'si' o 'no'")
    
    if otra_vez == 'no':
        break  