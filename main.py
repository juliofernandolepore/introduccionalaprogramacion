import database

if __name__ == "__main__":
    print("bienvenido al menu general")
    # Establecer la conexión
    conexion = database.conectar_db("localhost", "fernandolepore", "12345678fer", "basededatos1")
    # Cerrar la conexión
    database.cerrar_db(conexion)