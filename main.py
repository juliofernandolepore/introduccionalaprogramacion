import database, tabla, opciones

if __name__ == "__main__":
    print("bienvenido al menu general")
    # seccion de app con el usuario
    opciones.mostrar_menu()
    # Establecer la conexión
    conexion = database.conectar_db("localhost", "fernandolepore", "12345678fer", "basededatos1")
    # Crear tabla productos si no existe aun en la DB
    tabla.crear_tabla_productos_si_no_existe(conexion)    
    # Cerrar la conexión
    database.cerrar_db(conexion)