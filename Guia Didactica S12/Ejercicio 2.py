#Solicite ingresar el nombre del archivo
archivo = input("Ingresar el nombre del archivo: ")

try:
   with open(archivo, "r", encoding="utf-8") as f:
       lineas = f.readlines()
   print("El archivo tiene", len(lineas), "lineas")
except FileNotFoundError:
 print(f"Error, el archivo", archivo, "no existe.")
