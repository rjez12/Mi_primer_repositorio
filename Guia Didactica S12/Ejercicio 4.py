#Abrir archivo CSV en modo lectura
with open('listado.csv','r', encoding="utf-8") as archivo:
  
  for linea in archivo:
      linea = linea.strip()
      datos = [d.strip() for d in linea.split(',')]
  
      if len(datos) == 3:
         nombre = datos[0]
         precio = datos[1]
         cantidad = datos[2]

         print(f"Producto: {nombre} | Precio: ${precio}| Cantidad: {cantidad}")


