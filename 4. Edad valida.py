while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        
        if edad < 0 or edad > 120:
            print("     Edad no valida, debe estar entre 0 y 120")
        else:
            print("     Edad valida")
            break  

    except:
        print("     Debes ingresar un numero entero")
