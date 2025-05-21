import mysql.connector
# consultas sql para usar y reutilizar en la app

def obtener_productos(conexion):
    # consulta sql para traer todos los registro de productos existentes
    cursor = conexion.cursor()
    consulta = "SELECT nombre_item, cantidad, fecha_creacion FROM productos"
    try:
        cursor.execute(consulta)
        columnas = cursor.column_names
        datos_productos = []
        for fila in cursor.fetchall():
            fila_dict = dict(zip(columnas,fila))
            if 'fecha_creacion' in fila_dict and fila_dict['fecha_creacion'] is not None:
                fila_dict['fecha_creacion'] = str(fila_dict["fecha_creacion"])
                datos_productos.append(fila_dict)
        return datos_productos
    except mysql.connector.Error as errot:
        print("error al efectuar la consulta")
        return None
    finally:
        if cursor:
            cursor.close()

def insertar_producto(conexion, nombre_producto, cantidad):
    # inserta un producto nuevo (nombre y cantidad), retorna un booleano
    cursor = conexion.cursor()
    sql = "INSERT INTO productos (nombre_item, cantidad) VALUES (%s, %s)"
    valores = (nombre_producto, cantidad)
    try:
        cursor.execute(sql, valores)
        conexion.commit()
        print(f"Se insertó el producto '{nombre_producto}' con la cantidad {cantidad}.")
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()
           
def verificar_producto(conexion, nombre_producto):
    # verifica la existencia de 1 solo producto
    cursor = conexion.cursor()
    consulta = "SELECT nombre_item FROM productos WHERE nombre_item = %s"
    valores = (nombre_producto,)
    try:
        cursor.execute(consulta, valores)
        resultado = cursor.fetchone()
        if resultado:
            nombre_encontrado = resultado[0]
            print(f"resultado de la busqueda: {nombre_encontrado}")            
            return True
        else:
            print("sin resultados")            
            return False
    except mysql.connector.Error as err:
        print(f"Error al consultar el producto: {nombre_producto}")
        print(err)
        return False
    finally:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()

def eliminar_todoslosproductos(conexion, nombre_producto):
    # consulta sql para eliminar item y sus cantidades
    return False

def modificar_cantidades(conexion, nombre_producto, cantidad):
    # consulta sql para modificar stock
    return False



                              