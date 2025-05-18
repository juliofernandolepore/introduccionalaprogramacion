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
    # validar que solo ingrese un numero entero
    while int(cantidad) > max:
        print(f" la {cantidad} supera el maximo permitido de caracteres {max} ")
        cantidad = int(input("intente nuevamente con un numero inferior: "))
    while int(cantidad) < 1:
        print("el minimo a ingresar es 1")
        cantidad = int(input("intente nuevamente: "))
    return int(cantidad)