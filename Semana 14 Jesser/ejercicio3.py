#Escriba varias lineas de texto
#Funcion que ingrese datos en un archivo .txt
def guardar_notas():
#Abrir archivo en modo  escritura
    with open("notas.txt", "w", encoding="utf-8") as archivo:
        print("Ingrese varias lineas de texto. Ingrese una linea vacia para terminar")
#Bucle para saber cuando se termina de ingresar inf
        while True:
            linea=input()
            if linea=="":
                break
#Guardar los datos en el archivo.txt
            archivo.write(linea +"\n")
    print("Las lineas de texto fueron guardadas en 'notas.txt'.")

#Llamar a la funcion
guardar_notas()