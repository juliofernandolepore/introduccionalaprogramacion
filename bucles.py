def str_largo(nombre, min, max):
    while True:
        nombre_ingresado = nombre.lower()
        largo = len(nombre_ingresado) 
        if largo > max:
            print(f"el maximo es :{max}")
            print(f"ingresaste: {largo} caracteres")
            nombre_ingresado = input("ingresa un nombre mas corto").lower()
            return
        elif largo < min:
            print(f"el minimo es: {min} caracteres")
            print(f"ingresaste: {largo} caracteres")
            return
        else: 
            return nombre_ingresado
    
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