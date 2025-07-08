#Funcion para agregar u caargar un usuario para acceder al programa
import os
import pwinput

def agregar_usuario(usuario, clave):
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{usuario},{clave}\n")

def cargar_usuarios():
    if not os.path.exists("usuarios.txt"):
        return {}
    with open("usuarios.txt", "r") as archivo:
        lineas = archivo.readlines()
    usuarios = {}
    for linea in lineas:
        usuario, clave = linea.strip().split(",")
        usuarios[usuario] = clave
    return usuarios

def INICIO():
    try:
        print(" INICIO DE SESIÓN")
        usuarios = cargar_usuarios()
        intentos = 0
        while intentos < 3:
            usuario = input("Usuarios: ")
            clave_ingresada = pwinput.pwinput(prompt="Contraseña: ", mask="*")
            if usuario in usuarios and usuarios[usuario] == clave_ingresada:
                print(" Acceso permitido.\n")
                return True
            else:
                print("Usuario o contraseña no encontrados.\n")
                intentos += 1
        print("Demasiados intentos fallidos. Saliendo del programa.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

    