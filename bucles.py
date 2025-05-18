def str_largo(nombre, min, max):
    while len(nombre) > max:
            print(f"el maximo es :{max}")
            print(f"ingresaste: {len(nombre)} caracteres")
            nombre = input("ingresa un nombre mas corto: ")
            
    while len(nombre) < min:
            print(f"el minimo es: {min} caracteres")
            print(f"ingresaste: {len(nombre)} caracteres")
            nombre = input("ingresa un nombre mas largo: ")               
    return nombre.lower()
    
def limite_cantidad(cantidad, max):
    entero = int(cantidad)
    # validar que solo ingrese un numero entero
    if entero > max:
        print(entero+" supera el maximo permitido de caracteres "+ max)
        return
    elif entero < 1:
        print("el minimo a ingresar es 1")
        return
    else: 
        return entero