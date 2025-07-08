#Modulo de generacio de factura

from Productos import Productos, Cantidades, Precios

def GenerarFactura(ResumenArchivo="factura.txt"):


    total=0 #Variable acumuladora
    
    with open(ResumenArchivo, "w") as f:
         f.write(" ------FACTURA---------\n") 
         f.write("{:<15} {:<10} {:<10} {:<10}\n".format("Producto", "Cantidad", "Precio", "Subtotal")) #se utilizan los formatos de cadena para alinear las columnas
         f.write("--===============================--\n") #se utiliza .format para alinear las columnas 
         for i in range(len(Productos)):
            subtotal = Cantidades[i] * Precios[i]
            total += subtotal
            f.write("{:<15} {:<10} {:<10.2f} {:<10.2f}\n".format(Productos[i], Cantidades[i], Precios[i], subtotal))
            f.write("\nTotal: C${:.2f}\n".format(total))
            f.write("--===============================--\n")
    print(f"Factura guardada en {ResumenArchivo}")