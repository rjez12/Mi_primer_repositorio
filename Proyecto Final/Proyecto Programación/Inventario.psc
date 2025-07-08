Algoritmo Inventario
	Definir codigo, cantidad, limite, i, ingresado, c, b, m, modificar como entero
	Definir descripcion Como Caracter
	Definir precio Como real
	Definir entrada, entrada02 como logico
	Definir resp como texto
	
	limite = 1000
	ingresado = 1
	entrada02 = Verdadero
	
	Dimension codigo[limite]
	Dimension descripcion[limite]
	Dimension cantidad[limite]
	Dimension precio[limite]
	
	Repetir
		Limpiar Pantalla
		Escribir "==== Men� de Inventario ===="
		Escribir "1. Agregar nuevo producto"
		Escribir "2. Actualizar producto"
		Escribir "3. Buscar producto"
		Escribir "4. Ver total del inventario"
		Escribir "Ingrese una opci�n:"
		Leer opc
		
		Segun opc Hacer
			
			1: // Agregar producto
				Limpiar Pantalla
				i = ingresado
				entrada = Falso
				
				Si i <= limite Entonces
					Escribir "Ingrese un c�digo num�rico:"
					Leer codigo[i]
					
					Para c = 1 Hasta ingresado - 1 Con Paso 1 Hacer
						Si codigo[c] = codigo[i] Entonces
							entrada = Verdadero
						FinSi
					FinPara
					
					Si entrada = Verdadero Entonces
						Escribir "Error: El c�digo ya existe"
					Sino
						Escribir "Ingrese descripci�n del producto:"
						Leer descripcion[i]
						
						Escribir "Ingrese cantidad en stock:"
						Leer cantidad[i]
						
						Escribir "Ingrese precio unitario:"
						Leer precio[i]
						
						Escribir "Registro exitoso."
						ingresado = ingresado + 1
					FinSi
				Sino
					Escribir "�L�mite m�ximo alcanzado!"
				FinSi
				
			2: // Modificar producto
				Limpiar Pantalla
				Escribir "Ingrese el c�digo del producto que desea actualizar:"
				Leer modificar
				entrada = Falso
				
				Para m = 1 Hasta ingresado - 1 Con Paso 1 Hacer
					Si codigo[m] = modificar Entonces
						Escribir "Ingrese nueva cantidad de stock:"
						Leer cantidad[m]
						Escribir "Ingrese nuevo precio unitario:"
						Leer precio[m]
						Escribir "Producto actualizado con �xito."
						entrada = Verdadero
						Escribir "C�digo", "     ", "Descripci�n", "     ", "Cantidad", "    ", "Precio"
						Escribir codigo[m], "       ", descripcion[m], "     ", cantidad[m], "     ", "C$ ", precio[m];
					FinSi
				FinPara
				
				Si entrada = Falso Entonces
					Escribir "C�digo no encontrado."
				FinSi
				
			3: // Buscar producto
				Limpiar Pantalla
				Escribir "Ingrese el c�digo del producto a buscar:"
				Leer modificar
				entrada = Falso
				
				Para m = 1 Hasta ingresado - 1 Con Paso 1 Hacer
					Si codigo[m] = modificar Entonces
						Escribir "Producto encontrado:"
						Escribir "C�digo", "     ", "Descripci�n", "     ", "Cantidad", "    ", "Precio"
						Escribir codigo[m], "       ", descripcion[m], "     ", cantidad[m], "     ", "C$ ", precio[m]
						entrada = Verdadero
					FinSi
				FinPara
				
				Si entrada = Falso Entonces
					Escribir "Producto no encontrado."
				FinSi
				
			4: // Mostrar todo el inventario
				Limpiar Pantalla
				Si ingresado > 1 Entonces
					Escribir "Inventario actual:"
					Escribir "C�digo", "     ", "Descripci�n", "     ", "Cantidad", "    ", "Precio"
					Para i = 1 Hasta ingresado - 1 Con Paso 1 Hacer
						Escribir codigo[i], "       ", descripcion[i], "     ", cantidad[i], "     ", "C$ ", precio[i]
					FinPara
				Sino
					Escribir "No hay productos registrados a�n."
				FinSi
				
			De Otro Modo:
				Escribir "Opci�n inv�lida. Intente de nuevo."
				
		FinSegun
		
		Escribir ""
		Escribir "�Desea realizar otra operaci�n? (S/N):"
		Leer resp
		Si Mayusculas(resp) = "N" Entonces
			entrada02 = Falso
		FinSi
		
	Hasta Que entrada02 = Falso
	
FinAlgoritmo
