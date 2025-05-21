import database, tabla, opciones

# muestra el menu general al inicio de la carga
def intro():
    print("                 ************************************************************************")
    print("                                 app Manejo de stock en una verduleria de barrio")
    print("                 ************************************************************************")
    print("                                       seleccione la opcion deseada")
    print("                  ************************************************************************")

def muestra_opciones():
    print("                  ************************************************************************") 
    print("                         1. Ingresar Producto Nuevo - Nueva verdura")
    print("                         2. Ver stock de todos los productos / cantidades almacenadas")
    print("                         3. Ingresar mas unidades del producto existente")
    print("                         4. Ver cantidades de un Producto (item) en especifico")
    print("                         5. Eliminar todos los productos de un item especifico")
    print("                         6. Salir de la app")
    print("                  ************************************************************************")

def mostrar_menu():
        muestra_opciones()
        opcion = input("ingrese su opcion: ")
        try:
            if int(opcion) == 1:
                print("opcion seleccionada: 1 - Ingresar producto nuevo")
                opciones.ingresar_producto()
            elif int(opcion) == 2:
                print("opcion seleccionada: 2")
                opciones.ver_todoslosproductos()                
            elif int(opcion) == 3:
                print("opcion seleccionada: 3")
                opciones.actualizar_cantidad()                
            elif int(opcion) == 4:
                print("opcion seleccionada: 4")
            elif int(opcion) == 5:
                print("opcion seleccionada: 5")     
            elif int(opcion) == 6:
                print("opcion seleccionada: 6, usted ha salido de la aplicacion")
                return                
        except ValueError:
            print("ERROR inesperado en el menu principal")


if __name__ == "__main__":    
    conexion = database.conectar_db("localhost", "fernandolepore", "12345678fer", "basededatos1")    
    tabla.crear_tabla_productos_si_no_existe(conexion)
    database.cerrar_db(conexion)    
    # seccion de app con el usuario
    intro()
    mostrar_menu()
    
    