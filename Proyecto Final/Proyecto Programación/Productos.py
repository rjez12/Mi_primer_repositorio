#Modulo de ingreso de datos generales (Producto,Cantidad y precio)
#Funciones de actualizacion y eliminacion mediante ubicacion por codigo
Productos = []
Cantidades = []
Precios = []

def AgregarProducto():
    try:
        nombre = input("Ingrese el nombre del producto: ")
        
        while True:
            cantidad = int(input("Cantidad: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente de nuevo.")
            else:
                break

        while True:
            precio = float(input("Ingrese el precio unitario: C$"))
            if precio < 0:
                print("El precio no puede ser negativo. Intente de nuevo.")
            else:
                break

        Productos.append(nombre)
        Cantidades.append(cantidad)
        Precios.append(precio)
        print("Datos ingresados correctamente.")
    except ValueError:
        print("Error: Ingrese valores válidos para cantidad y precio.")
        return 

def ActualizarProducto():
    VerInventario()
    try:
        codigo = int(input("Ingrese el codigo a actualizar: ")) #valor inicial comienza en 0=1 1=2....
        if 0 <= codigo < len(Productos):
            Productos[codigo] = input("Nuevo nombre del producto: ")
            
            while True:
                cantidad = int(input("Nueva cantidad: "))
                if cantidad < 0:
                    print("La cantidad no puede ser negativa. Intente de nuevo.")
                else:
                    break
            Cantidades[codigo] = cantidad

            while True:
                precio = float(input("Nuevo precio: C$"))
                if precio < 0:
                    print("El precio no puede ser negativo. Intente de nuevo.")
                else:
                    break
            Precios[codigo] = precio

            print("Producto actualizado")
        else:
            print("Codigo invalido")
    except ValueError:
        print("Error: Ingrese valores válidos para código, cantidad y precio.")
        return

def EliminaProducto():
    VerInventario()
    try:
        codigo = int(input("Código a eliminar: "))
        if 0 <= codigo < len(Productos):
            Productos.pop(codigo)
            Cantidades.pop(codigo)
            Precios.pop(codigo)
            print("Producto eliminado.")
        else:
            print("Código inválido.")
    except ValueError:
        print("Error: Ingrese un valor válido para el código.")

def VenderProducto():
    VerInventario()
    try:
        codigo = int(input("Ingrese el código del producto a vender: "))
        if 0 <= codigo < len(Productos):
            print(f"Producto seleccionado: {Productos[codigo]}")
            cantidad_vender = int(input("Cantidad a vender: "))
            if 0 < cantidad_vender <= Cantidades[codigo]:
                total = cantidad_vender * Precios[codigo]
                Cantidades[codigo] -= cantidad_vender

                # Generar una factura en base a la venta en un archivo de texto .txt
                with open("facturaVenta.txt", "w", encoding="utf-8") as facturaVenta:
                    facturaVenta.write("--- FACTURA DE VENTA ---\n")
                    facturaVenta.write(f"Producto: {Productos[codigo]}\n")
                    facturaVenta.write(f"Cantidad vendida: {cantidad_vender}\n")
                    facturaVenta.write(f"Precio unitario: C${Precios[codigo]:.2f}\n")
                    facturaVenta.write(f"Total a pagar: C${total:.2f}\n")
                    facturaVenta.write("------------------------\n")

                print("Venta realizada y stock actualizado.")
                print("Factura generada en el archivo 'facturaVenta.txt'.")
            else:
                print("Cantidad no válida o insuficiente en inventario.")
        else:
            print("Código de producto inválido.")
    except ValueError:
        print("Error: Ingrese valores válidos para código y cantidad.")

def VerInventario():
    print("\n ---- INVENTARIO ---- " )
    for i in range (len(Productos)):
        print(f"Codigo: {i} | Producto: {Productos[i]} | Cantidades: {Cantidades[i]} | Precio: ${Precios[i]:.2f}")

def ValorTotal():
    total= 0
    for i in range (len(Productos)):
        total += Cantidades[i] * Precios[i]
    print(f"\nEl valor total del inventario es de: C${total:.2f}")