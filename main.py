import database, tabla, opciones

if __name__ == "__main__":
    print("                                    *********************************")    
    conexion = database.conectar_db("localhost", "fernandolepore", "12345678fer", "basededatos1")    
    tabla.crear_tabla_productos_si_no_existe(conexion)
    database.cerrar_db(conexion)    
    # seccion de app con el usuario
    valor = opciones.mostrar_menu()
    
    