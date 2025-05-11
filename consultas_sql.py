import mysql.connector

def insertar_producto(conexion, nombre_producto, cantidad):
    """
    Inserta un nuevo producto y su cantidad en la tabla 'productos' de MySQL.

    Args:
        conexion: Objeto de conexión a la base de datos MySQL.
        nombre_producto (str): El nombre del producto a insertar.
        cantidad (int): La cantidad del producto a insertar.
    """
    cursor = conexion.cursor()
    sql = "INSERT INTO productos (nombre_producto, cantidad) VALUES (%s, %s)"
    valores = (nombre_producto, cantidad)
    try:
        cursor.execute(sql, valores)
        conexion.commit()
        print(f"Se insertó el producto '{nombre_producto}' con cantidad {cantidad}.")
    except mysql.connector.Error as err:
        print(f"Error al insertar el producto: {err}")
    finally:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()
            print("Conexión a la base de datos MySQL cerrada.")