
nombres = []

while True:

    nombre_usuario = input("Ingresa tu nombre: ").strip()


    if nombre_usuario == "":
        print("   El nombre no puede estar vacio")
        continue


    nombres.append(nombre_usuario)


    otra_respuesta = input("Deseas agregar otro nombre? (si/no): ").lower().strip()
    

    while otra_respuesta not in ['si', 'no']:
        print("     Responde con 'si' o 'no'.")
        otra_respuesta = input("Deseas agregar otro nombre? (si/no): ").lower().strip()
    

    if otra_respuesta == 'no':
        break

print("\n Lista final de nombres:\n")
for i, nombre in enumerate(nombres, start=1):
    print(f"{i}. {nombre.title()}")

       
