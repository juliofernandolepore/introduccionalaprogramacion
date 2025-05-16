import database, consultas_sql, bucles

# muestra el menu general al inicio de la carga
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
                print("opcion seleccionada: 1 - Ingresar producto nuevo")
                ingresar_producto()
            elif entero == 2:
                print("opcion seleccionada: 2")
                
            elif entero == 3:
                print("opcion seleccionada: 3")
                
            elif entero == 4:
                print("opcion seleccionada: 4")
                
            else:
                print("ha ingresado un valor no valido intente nuevamente")
        except ValueError:
            print("ha ingresado un valor no valido intente nuevamente")


# sub menu ingresar producto nuevo (opcion 1)
def ingresar_producto():
    # function para ingresar producto nuevo, y consultar su existencia en tabla previo a su registro
    producto = input("ingrese nuevo item o nuevo producto: ")
    str_validado = bucles.str_largo(producto, 2, 150)    
    cantidad = input("ingrese la cantidad o numero de items: ")
    cantidad_validada = bucles.limite_cantidad(cantidad, 100)    
    # instanciar una conexion
    conexion = database.conectar_db("localhost", "fernandolepore", "12345678fer", "basededatos1")
    # efectuar consulta sql para verificar que exista o no en tabla productos (devuelve un booleano)

    """
    resultado = consultas_sql.verificar_producto(conexion, str_validado)
    if resultado == False:
        print("el item no existe y puede ingresar como nuevo")
        # si resultado es falso continuo con el insertar
        
        if resultado:
            print("insertado exitosamente")
        else:
            print("no se pudo ingresar, error desconocido")    
    else:
        print("el producto ya existe, intente la opcion 3 del menu principal")    
    """
    resultado = consultas_sql.insertar_producto(conexion, str_validado, cantidad_validada)
    
               