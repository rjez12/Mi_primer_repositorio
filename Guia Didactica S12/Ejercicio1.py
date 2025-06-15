#Importar modulo datetime
from datetime import datetime

entrada = input("Ingresa tu entrada del diario:")
#Fecha y Hora
hora_fecha = datetime.now()
with open("diario.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{hora_fecha} - {entrada}\n")

print("Tu entrada fue guardada con exito en diario,txt")
