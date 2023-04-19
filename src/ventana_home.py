## ---------------------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------------------
## ARCHIVO "VENTANA_HOME.PY" CONTIENE LA FUNCIÓN PARA CREAR LA PÁGINA PRINCIPAL DEL PROGRAMA, DONDE EL USUARIO
## ELIGIRÁ QUÉ LABERINTO EJECUTA, QUE ALGORITMO USA, QUE HEURÍSTICA USA Y QUE VELOCIDAD DE IMPRESIÓN QUIERE
## VENTANA HECHA CON LA LA BIBLIOTECA GRÁFICA "TKINTER"
## ---------------------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------------------

import tkinter as tk
from src.funciones_auxiliares import *

def crear_home():
	# Creamos la ventana
	ventana = tk.Tk()

	ventana.title("UFV - INCO - Problema de búsqueda en laberintos - Grupo 4")

	# Protocolo en caso de cierre de ventana
	ventana.protocol("WM_DELETE_WINDOW", lambda: on_closing(ventana))

	# Negamos la posibilidad de redimensionar la ventana
	#ventana.resizable(False,False)

	# Definimos la anchura y altura de nuestra ventana
	anchura_ventana = 1285
	altura_ventana = 800 

	# Obtenemos la información de la pantalla del PC que ejecuta el programa 
	anchura_pantalla_PC = ventana.winfo_screenwidth()  
	altura_pantalla_PC = ventana.winfo_screenheight() 
	 
	# Calculamos las coordenadas para que la ventana aparezca en el medio del PC
	x = (anchura_pantalla_PC/2) - (anchura_ventana/2)
	y = (altura_pantalla_PC/2) - (altura_ventana/2)
	 
	# Indicamos las características de la ventana (anchura, altura y posición) 
	ventana.geometry('%dx%d+%d+%d' % (anchura_ventana, altura_ventana, x, y))

	# Creamos la etiqueta del mensaje de información
	etiqueta = tk.Label(ventana, text = "- Programa de resolución de laberintos -\nPor favor, selecciona entre "\
		"las distintas opciones y después presiona el botón 'Ejecutar búsqueda'",font=("Arial", 16))
	etiqueta.grid(row = 0, column = 0, columnspan = 4, padx = 25, pady= 25)

	# Creamos la etiqueta del tipo de laberinto a elegir y la posicionamos en el grid
	etiqueta = tk.Label(ventana, text = "Tipo de laberinto:     ",font=("Arial", 16))  #17
	etiqueta.grid(row = 1, column = 0, padx = 25, pady= 10)

	# Creamos la etiqueta del tipo de algoritmo a elegir y la posicionamos en el grid
	etiqueta = tk.Label(ventana, text = "Algoritmo de búsqueda: ",font=("Arial", 16)) #21
	etiqueta.grid(row = 1, column = 1, padx = 25, pady= 10)

	# Creamos la etiqueta del tipo de heurística a elegir y la posicionamos en el grid
	etiqueta = tk.Label(ventana, text = "Tipo de heurística:    ",font=("Arial", 16))  #18
	etiqueta.grid(row = 1, column = 2, padx = 25, pady= 10)

	# Creamos la etiqueta de la velocidad de impresión a elegir y la posicionamos en el grid
	etiqueta = tk.Label(ventana, text = "Velocidad de impresión:",font=("Arial", 16)) #22
	etiqueta.grid(row = 1, column = 3, padx = 25, pady= 10)


	# Padding horizontal a aplicar en los radiobutton
	padding_x_radio = 13

	# Variable que almacena la opcion seleccionada por el radiobutton del laberinto, así como las opciones del mismo y su posición en el grid
	laberinto_seleccionado = tk.IntVar()
	radio_mapa = tk.Radiobutton(ventana, text="Pequeño",font=("Arial", 14), value=1, variable=laberinto_seleccionado).grid(row = 2, column = 0,sticky = "W", padx = padding_x_radio)
	radio_mapa = tk.Radiobutton(ventana, text="Mediano",font=("Arial", 14), value=2, variable=laberinto_seleccionado).grid(row = 3, column = 0,sticky = "W", padx = padding_x_radio)
	radio_mapa = tk.Radiobutton(ventana, text="Grande",font=("Arial", 14), value=3, variable=laberinto_seleccionado).grid(row = 4, column = 0,sticky = "W", padx = padding_x_radio)
	radio_mapa = tk.Radiobutton(ventana, text="Custom",font=("Arial", 14), value=4, variable=laberinto_seleccionado).grid(row = 5, column = 0,sticky = "W", padx = padding_x_radio)

	# Variable que almacena la opcion seleccionada por el radiobutton del algoritmo, así como las opciones del mismo y su posición en el grid
	algoritmo_seleccionado = tk.IntVar()
	radio_algoritmo = tk.Radiobutton(ventana, text="Anchura",font=("Arial", 14), value=1, variable=algoritmo_seleccionado).grid(row = 2, column = 1,sticky = "W", padx = padding_x_radio)
	radio_algoritmo = tk.Radiobutton(ventana, text="Profundidad",font=("Arial", 14), value=2, variable=algoritmo_seleccionado).grid(row = 3, column = 1,sticky = "W", padx = padding_x_radio)
	radio_algoritmo = tk.Radiobutton(ventana, text="A*",font=("Arial", 14), value=3, variable=algoritmo_seleccionado).grid(row = 4, column = 1,sticky = "W", padx = padding_x_radio)
	radio_algoritmo = tk.Radiobutton(ventana, text="MinMax",font=("Arial", 14), value=4, variable=algoritmo_seleccionado).grid(row = 5, column = 1,sticky = "W", padx = padding_x_radio)

	# Variable que almacena la opcion seleccionada por el radiobutton de la heurística, así como las opciones del mismo y su posición en el grid
	heuristica_seleccionada = tk.IntVar()
	radio_heuristica = tk.Radiobutton(ventana, text="Manhattan",font=("Arial", 14), value=1, variable=heuristica_seleccionada).grid(row = 2, column = 2,sticky = "W", padx = padding_x_radio)
	radio_heuristica = tk.Radiobutton(ventana, text="Euclidea",font=("Arial", 14), value=2, variable=heuristica_seleccionada).grid(row = 3, column = 2,sticky = "W", padx = padding_x_radio)
	radio_heuristica = tk.Radiobutton(ventana, text="Chebyshev",font=("Arial", 14), value=3, variable=heuristica_seleccionada).grid(row = 4, column = 2,sticky = "W", padx = padding_x_radio)

	# Variable que almacena la opcion seleccionada por el radiobutton de la velocidad, así como las opciones del mismo y su posición en el grid
	velocidad_seleccionada = tk.IntVar()
	radio_velocidad = tk.Radiobutton(ventana, text="Velocidad baja",font=("Arial", 14), value=1, variable=velocidad_seleccionada).grid(row = 2, column = 3,sticky = "W", padx = padding_x_radio)
	radio_velocidad = tk.Radiobutton(ventana, text="Velocidad media",font=("Arial", 14), value=2, variable=velocidad_seleccionada).grid(row = 3, column = 3,sticky = "W", padx = padding_x_radio)
	radio_velocidad = tk.Radiobutton(ventana, text="Velocidad alta",font=("Arial", 14), value=3, variable=velocidad_seleccionada).grid(row = 4, column = 3,sticky = "W", padx = padding_x_radio)


	# Creamos un botón, importante pasar la función a ejecutar en "command" sin paréntesis. Ejemplo: "command = funcion"
	# Si queremos pasar argumentos a la función hay que usar lambda. Ejemplo: "command = lambda: funcion(argumentos)"
	botonEjecutar = tk.Button(ventana, width = 15, height = 3, text = "Ejecutar búsqueda",font=("Arial", 14), command = lambda: opcionesSeleccionadas(ventana,etiqueta_error,laberinto_seleccionado,heuristica_seleccionada,algoritmo_seleccionado,velocidad_seleccionada))
	botonEjecutar.grid(row = 6, column = 1, columnspan = 2, padx = 25, pady= 80)

	# Creamos un botón, importante pasar la función a ejecutar en "command" sin paréntesis
	# Si queremos pasar parámetros hay que usar lambda --> "command = lambda: funcion(argumentos)"
	botonSalir = tk.Button(ventana, width = 15, height = 3, text = "Cerrar programa",font=("Arial", 14), command = lambda: cerrarPrograma(ventana))
	botonSalir.grid(row = 7, column = 1, columnspan = 2, padx = 25, pady= 0)


	# Creamos una etiqueta de error por si el usuario trata de ejecutar sin haber seleccionado todas las opciones
	etiqueta_error = tk.Label(ventana,font=("Arial", 14),fg='#FF0000')
	etiqueta_error.grid(row = 8, column = 1, columnspan = 2,padx = 25, pady= 20)

	ventana.mainloop()

	# Cuando se presiona el botón de ejecutar, se cierra la ventana y devolvemos las selecciones del usuario
	return laberinto_seleccionado.get(), algoritmo_seleccionado.get(), heuristica_seleccionada.get(),velocidad_seleccionada.get()