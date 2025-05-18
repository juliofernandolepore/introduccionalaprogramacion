import database, consultas_sql, bucles, main



# sub menu ingresar producto nuevo (opcion 1)
def ingresar_producto():
    # function para ingresar producto nuevo, y consultar su existencia en tabla previo a su registro
    producto = input("ingrese nuevo item o nuevo producto: ")
    str_validado = bucles.str_largo(producto, 3, 150)    
    cantidad = input("ingrese la cantidad o numero de items: ")
    cant_validada = bucles.limite_cantidad(cantidad, 1000)        
    # instanciar una conexion
    conexion = database.conectar_db("localhost", "fernandolepore", "12345678fer", "basededatos1")
    # efectuar INSERT en tabla productos
    booleano = consultas_sql.insertar_producto(conexion, str_validado, cant_validada)
    main.mostrar_menu()

def ver_todoslosproductos():
    # funcion para mostrar todos los productos almacenados, cantidad, fecha nombres
    conexion = database.conectar_db("localhost", "fernandolepore", "12345678fer", "basededatos1")
    lista = consultas_sql.obtener_productos(conexion)    
    if lista:
        print("-" * 60)
        print("{:<20} {:<10} {:<30}".format('Nombre', 'Cantidad', 'Fecha del registro'))
        print("-" * 60)
        for producto in lista:
            nombre = producto.get('nombre_item',)
            cantidad = producto.get('cantidad',)
            fecha_creacion = producto.get('fecha_creacion',)
            print("{:<20} {:<10} {:<30} ".format(nombre, cantidad, fecha_creacion))
            
        print("-" * 60)
    else:
        print("No se encontraron Proctos registrados")        
     
    
    
    
               