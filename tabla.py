import mysql.connector
from mysql.connector import errorcode

def crear_tabla_productos_si_no_existe(conexion):
    # Crear tabla productos si no existe aun en la DB
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
        print(f"Tabla '{tabla_productos}' creada exitosamente ya que la misma no existia en db MySQL.")
    except mysql.connector.Error as err:
        print(f"Error al crear la tabla '{tabla_productos}' en MySQL: {err}")