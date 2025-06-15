#Lista de compras
archivo = open("compras.txt", "w", encoding="utf-8")

print("Ingresa tus productos uno por uno. Pon 'fin' cuando termines.")    

while True:
   producto=input("Ingresar Producto: ")
   if producto.lower() == "fin":
    break

archivo.write(producto + "\n")

archivo.close()
print("Su lista de compras fue guardada en el archivo", archivo,".")