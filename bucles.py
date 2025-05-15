def str_largo(nombre, min, max):
    nombre_ingresado = nombre.Lower() 
    if len(nombre_ingresado) > 150:
        return nombre+" supera el maximo permitido de caracteres "+ max
    elif len(nombre_ingresado) < 2:
        return nombre+" supera el maximo permitido de caracteres "+ min
    else: 
        return nombre_ingresado
    
def limite_cantidad(cantidad, max):
    entero = int(cantidad)
    # validar que solo ingrese un numero entero
    if entero > max:
        print(entero+" supera el maximo permitido de caracteres "+ max)
    elif entero < 1:
        print("el minimo a ingresar es 1")
    else: 
        return entero