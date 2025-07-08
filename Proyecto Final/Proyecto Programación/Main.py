#Modulo principal
from Productos import AgregarProducto, ActualizarProducto, EliminaProducto, VerInventario, VenderProducto, ValorTotal
from Factura import GenerarFactura
from Usuario import INICIO, agregar_usuario
from Menu import  MostrarMenu

while True:
    print("1. Iniciar sesión")
    print("2. Registrar nuevo usuario")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        if INICIO():
            while True:
                MostrarMenu()
                Opcion = input("Seleccione una opcion: ")

                if Opcion == "1":
                    AgregarProducto()
                elif Opcion == "2":
                    ActualizarProducto()
                elif Opcion == "3":
                    VerInventario()
                elif Opcion == "4":
                    EliminaProducto()
                elif Opcion == "5":
                    ValorTotal()
                elif Opcion == "6":
                    GenerarFactura()
                elif Opcion == "7":
                    VenderProducto()
                elif Opcion == "8":
                    print("-Saliendo del programa-")
                    break
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")
            break
    elif opcion == "2":
        usuario = input("Nuevo usuario: ")
        clave = input("Nueva contraseña: ")
        agregar_usuario(usuario, clave)
        print("Usuario registrado correctamente.\n")
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")