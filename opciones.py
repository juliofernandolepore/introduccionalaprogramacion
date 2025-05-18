import database, consultas_sql, bucles, main
# funciones que se corresponden a las opciones del menu principal
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
        print("aun no hay registro de productos en el sistema")        
    main.mostrar_menu()

def actualizar_cantidad():
# function para actualizar las cantidades un producto por solicitud
    producto = input("ingrese producto al cual quiere modificar stock: ")
    str_validado = bucles.str_largo(producto, 3, 150)
# instanciar una conexion
    conexion = database.conectar_db("localhost", "fernandolepore", "12345678fer", "basededatos1")    
# llamar al model, o consulta sql para 1 producto para verificar su existencia antes del update
    booleano = consultas_sql.verificar_producto(conexion, str_validado)
    if booleano:   
        cantidad = input(f"ingrese el nuevo valor de stock para: {producto}")
        cant_validada = bucles.limite_cantidad(cantidad, 1000)        
        # llamar a la consulta update, ya que el producto es existente
        # actualizar cantidades (update)
    main.mostrar_menu()
    
    
               