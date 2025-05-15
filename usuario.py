import database, consultas_sql

def ingresar_producto():
    # function para ingresar producto nuevo, y consultar su existencia en tabla previo a su registro
    producto = input("ingrese nuevo item o nuevo producto: ")
    cantidad = input("ingrese la cantidad o numero de items: ")
    # instanciar una conexion
    conexion = database.conectar_db("localhost", "fernandolepore", "12345678fer", "basededatos1")
    # efectuar consulta sql para verificar que exista o no en tabla productos (devuelve un booleano)
    resultado = consultas_sql.verificar_producto(conexion, producto)
    # si resultado es falso continuo con el insertar
    resultado = consultas_sql.insertar_producto(conexion, producto, cantidad)
    # efectuar insert de valores no existentes en la base de datos y saneados
    consultas_sql.insertar_producto(conexion, producto, cantidad)