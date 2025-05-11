import mysql.connector
from mysql.connector import errorcode

def crear_tabla_productos_si_no_existe(conexion):
    """
    Crea la tabla 'productos' en la base de datos MySQL si no existe.
    La tabla tendrá los campos:
        - cantidad: INT (entero)
        - nombre_item: VARCHAR(150) (cadena de texto de hasta 150 caracteres)
    """
    tabla_productos = 'productos'
    cantidad = 'cantidad INT, nombre_item VARCHAR(150)'
    cursor = conexion.cursor()
    try:
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {tabla_productos} (
                {cantidad}
            )
        """)
        conexion.commit()
        print(f"Tabla '{tabla_productos}' creada exitosamente (si no existía) en db MySQL.")
    except mysql.connector.Error as err:
        print(f"Error al crear la tabla '{tabla_productos}' en MySQL: {err}")