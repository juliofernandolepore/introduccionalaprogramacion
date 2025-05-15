def mostrar_menu():
    while True:
        print("                                        *********************************")
        print("                                          bienvenido al menu general")
        print("                 ************************************************************************")
        print("                  la siguiente es una app de manejo de stock para una verduleria por ejemplo")
        print("                 ************************************************************************")
        print("                                       seleccione la opcion deseada")
        print("                  ************************************************************************")
        print("                         1. Ingresar Producto Nuevo - Nueva verdura")
        print("                         2. Ver stock de todos los productos / cantidades almacenadas")
        print("                         3. Ingresar mas unidades del producto existente")
        print("                         4. Ver cantidades de un Producto (item) en especifico")
        opcion = input("ingrese su opcion: ")
        try:
            entero = int(opcion)
            if entero == 1:
                print("opcion seleccionada: 1")
                return 1
            elif entero == 2:
                print("opcion seleccionada: 2")
                return 2
            elif entero == 3:
                print("opcion seleccionada: 3")
                return 3
            elif entero == 4:
                print("opcion seleccionada: 4")
                return 4
            else:
                print("ha ingresado un valor no valido intente nuevamente")
        except ValueError:
            print("ha ingresado un valor no valido intente nuevamente")
                