import database

if __name__ == "__main__":
    # Establecer la conexión
    conexion = database.conectar_db()

    if conexion:
        # Ejemplo de inserción
        sql_insert = "INSERT INTO clientes (nombre, direccion) VALUES (%s, %s)"
        valores_insert = ("Carlos", "Calle Nueva 456")
        cursor_insert = database.ejecutar_consulta(conexion, sql_insert, valores_insert)
        if cursor_insert:
            database.guardar_cambios(conexion)
            print(f"Main: {cursor_insert.rowcount} registro insertado.")
            cursor_insert.close()

        # Ejemplo de selección
        sql_select = "SELECT * FROM clientes"
        cursor_select = database.ejecutar_consulta(conexion, sql_select)
        if cursor_select:
            resultados = database.obtener_resultados(cursor_select)
            print("\nMain: Lista de clientes:")
            for cliente in resultados:
                print(f"Main: {cliente}")
            cursor_select.close()

        # Cerrar la conexión
        database.cerrar_db(conexion)