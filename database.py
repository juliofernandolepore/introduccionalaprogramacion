import mysql.connector

def conectar_db(host="localhost", user="usuario", password="contraseña", database="basededatos"):  
    # Establecer la conexión y retorna: mysql.connector.MySQLConnection: El objeto de conexión si la conexión es exitosa
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
    # Cierra la conexión a la base de datos MySQL.

    if conexion and conexion.is_connected():
        conexion.close()
        
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