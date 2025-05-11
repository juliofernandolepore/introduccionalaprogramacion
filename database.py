import mysql.connector

def conectar_db(host="localhost", user="tu_usuario", password="tu_contraseña", database="tu_basededatos"):
    """
    Establece una conexión a la base de datos MySQL.

    Argumentos:
        host (str): La dirección del servidor MySQL.
        user (str): El nombre de usuario de MySQL.
        password (str): La contraseña del usuario de MySQL.
        database (str): El nombre de la base de datos.

    Return:
        mysql.connector.MySQLConnection: El objeto de conexión si la conexión es exitosa,
                                         None en caso de error.
    """
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Database: ¡Conexión exitosa a db!")
        return mydb
    except mysql.connector.Error as err:
        print(f"Database: Error al conectar a bd: {err}")
        return None

def cerrar_db(conexion):
    """
    Cierra la conexión a la base de datos MySQL.

    Argumentos:
        conexion (mysql.connector.MySQLConnection): El objeto de conexión a cerrar.
    """
    if conexion and conexion.is_connected():
        conexion.close()
        print("Database: Conexión a db cerrada.")

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

def guardar_cambios(conexion):
    """
    Guarda los cambios en la base de datos (commit).

    Args:
        conexion (mysql.connector.MySQLConnection): El objeto de conexión.
    """
    if conexion and conexion.is_connected():
        conexion.commit()
    else:
        print("Database: No hay conexión a la base de datos para guardar los cambios.")