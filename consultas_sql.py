import mysql.connector

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
    # funcion para consultar en la db si existe o no un producto, retorna booleano
    cursor = conexion.cursor()
    sql = "SELECT nombre_item FROM productos WHERE nombre_item = %s"
    valores = (nombre_producto,)
    try:
        cursor.execute(sql, valores)
        resultado = cursor.fetchone()
        if resultado:            
            return True
        else:            
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

def ejecutar_consulta(conexion, sql, valores=None):
    """
    Ejecuta una consulta SQL en la base de datos.

    Argumentos:
        conexion (mysql.connector.MySQLConnection): El objeto de conexión.
        sql (str): La consulta SQL a ejecutar.
        valores (tuple, optional): Los valores para la consulta (para consultas preparadas).
                                   Defaults to None.

    Return:
        mysql.connector.cursor.MySQLCursor: El objeto cursor si la consulta se ejecuta con éxito,
                                            None en caso de error.
    """
    cursor = None
    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            if valores:
                cursor.execute(sql, valores)
            else:
                cursor.execute(sql)
            return cursor
        else:
            print("Database: No hay conexión a la base de datos para ejecutar la consulta.")
            return None
    except mysql.connector.Error as err:
        print(f"Database: Error al ejecutar la consulta: {err}")
        if cursor:
            cursor.close()
        return None

def obtener_resultados(cursor):
    """
    Obtiene todos los resultados de un cursor.

    Args:
        cursor (mysql.connector.cursor.MySQLCursor): El objeto cursor.

    Returns:
        list: Una lista de los resultados obtenidos.
    """
    if cursor:
        return cursor.fetchall()
    else:
        return []

                              