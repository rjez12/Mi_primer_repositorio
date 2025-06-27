#Ejercicio leyendo y añadiendo datos a un archivo csv
#Ingresando datos como: fecha, producto, cantidad, precio
#El programa debe calcular el total de ingresos generados y unidades vendidas de cada prodcuto
producto_buscar = input("Ingrese el nombre del producto a analizar: ").lower()

total_ingresos = 0
total_unidades = 0

try:
    with open("ventas.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            fecha, producto, cantidad, precio = linea.strip().split(",")
            if producto.lower() == producto_buscar:
                cantidad = int(cantidad)
                precio = float(precio)
                total_unidades += cantidad
                total_ingresos += cantidad * precio

    print(f"\nProducto: {producto_buscar}")
    print(f"Total de unidades vendidas: {total_unidades}")
    print(f"Total de ingresos generados: ${total_ingresos:.2f}")

except FileNotFoundError:
    print(" Error: El archivo 'ventas.csv' no fue encontrado.")
except Exception as e:
    print(f" Ocurrió un error: {e}")