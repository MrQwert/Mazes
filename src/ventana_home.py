import tkinter as tk
from src import *

def crear_home():
	ventana = tk.Tk()

	ventana.title("UFV - INCO - Problema de búsqueda en laberintos - Grupo 4")

	# Negamos la posibilidad de redimensionar la ventana
	#ventana.resizable(False,False)

	# Definimos la anchura y altura de nuestra ventana
	anchura_ventana = 1300
	altura_ventana = 800 

	# Obtenemos la información de la pantalla del PC que ejecuta el programa 
	anchura_pantalla_PC = ventana.winfo_screenwidth()  
	altura_pantalla_PC = ventana.winfo_screenheight() 
	 
	# Calculamos las coordenadas para que la ventana aparezca en el medio del PC
	x = (anchura_pantalla_PC/2) - (anchura_ventana/2)
	y = (altura_pantalla_PC/2) - (altura_ventana/2)
	 
	# Indicamos las características de la ventana (anchura, altura y posición) 
	ventana.geometry('%dx%d+%d+%d' % (anchura_ventana, altura_ventana, x, y))


	# Creamos una etiqueta
	etiqueta = tk.Label(ventana, text = "- Programa de resolución de laberintos -\nPor favor, selecciona entre "\
		"las distintas opciones y después presiona el botón 'Ejecutar búsqueda'",font=("Arial", 16))
	etiqueta.grid(row = 0, column = 0, columnspan = 3, padx = 25, pady= 25)

	etiqueta = tk.Label(ventana, text = "Tipo de mapa:                   ",font=("Arial", 16))
	etiqueta.grid(row = 1, column = 0, padx = 25, pady= 10)

	etiqueta = tk.Label(ventana, text = "Algoritmo de búsqueda:",font=("Arial", 16))
	etiqueta.grid(row = 1, column = 1, padx = 25, pady= 10)

	etiqueta = tk.Label(ventana, text = "Velocidad de impresión:",font=("Arial", 16))
	etiqueta.grid(row = 1, column = 2, padx = 25, pady= 10)


	# Variable que almacena la opcion seleccionada por el radiobutton
	mapa_seleccionado = tk.IntVar()
	radio_mapa = tk.Radiobutton(ventana, text="Mapa 1 (pequeño)",font=("Arial", 14), value=1, variable=mapa_seleccionado).grid(row = 2, column = 0,sticky = "W", padx = 40)
	radio_mapa = tk.Radiobutton(ventana, text="Mapa 2 (mediano)",font=("Arial", 14), value=2, variable=mapa_seleccionado).grid(row = 3, column = 0,sticky = "W", padx = 40)
	radio_mapa = tk.Radiobutton(ventana, text="Mapa 3 (grande)",font=("Arial", 14), value=3, variable=mapa_seleccionado).grid(row = 4, column = 0,sticky = "W", padx = 40)

	# Variable que almacena la opcion seleccionada por el radiobutton
	algoritmo_seleccionado = tk.IntVar()
	radio_algoritmo = tk.Radiobutton(ventana, text="Anchura",font=("Arial", 14), value=1, variable=algoritmo_seleccionado).grid(row = 2, column = 1,sticky = "W", padx = 40)
	radio_algoritmo = tk.Radiobutton(ventana, text="Profundidad",font=("Arial", 14), value=2, variable=algoritmo_seleccionado).grid(row = 3, column = 1,sticky = "W", padx = 40)
	radio_algoritmo = tk.Radiobutton(ventana, text="A*",font=("Arial", 14), value=3, variable=algoritmo_seleccionado).grid(row = 4, column = 1,sticky = "W", padx = 40)
	radio_algoritmo = tk.Radiobutton(ventana, text="MinMax",font=("Arial", 14), value=4, variable=algoritmo_seleccionado).grid(row = 5, column = 1,sticky = "W", padx = 40)

	# Variable que almacena la opcion seleccionada por el radiobutton
	velocidad_seleccionada = tk.IntVar()
	radio_velocidad = tk.Radiobutton(ventana, text="Velocidad baja",font=("Arial", 14), value=1, variable=velocidad_seleccionada).grid(row = 2, column = 2,sticky = "W", padx = 40)
	radio_velocidad = tk.Radiobutton(ventana, text="Velocidad media",font=("Arial", 14), value=2, variable=velocidad_seleccionada).grid(row = 3, column = 2,sticky = "W", padx = 40)
	radio_velocidad = tk.Radiobutton(ventana, text="Velocidad alta",font=("Arial", 14), value=3, variable=velocidad_seleccionada).grid(row = 4, column = 2,sticky = "W", padx = 40)


	# Creamos un botón, importante pasar la función a ejecutar en "command" sin paréntesis
	# Si queremos pasar parámetros hay que usar lambda --> "command = lambda: funcion(argumentos)"
	botonEjecutar = tk.Button(ventana, width = 15, height = 3, text = "Ejecutar búsqueda",font=("Arial", 14), command = lambda: opcionesSeleccionadas(ventana,etiqueta_error,mapa_seleccionado,algoritmo_seleccionado,velocidad_seleccionada))
	botonEjecutar.grid(row = 6, column = 1, padx = 25, pady= 80)

	# Creamos un botón, importante pasar la función a ejecutar en "command" sin paréntesis
	# Si queremos pasar parámetros hay que usar lambda --> "command = lambda: funcion(argumentos)"
	botonSalir = tk.Button(ventana, width = 15, height = 3, text = "Cerrar programa",font=("Arial", 14), command = lambda: cerrarPrograma(ventana))
	botonSalir.grid(row = 7, column = 1, padx = 25, pady= 0)



	# Creamos una etiqueta
	etiqueta_error = tk.Label(ventana,font=("Arial", 14))
	etiqueta_error.grid(row = 8, column = 1,padx = 25, pady= 20)

	# Loop principal de nuestra ventana
	ventana.mainloop()

	return mapa_seleccionado.get(), algoritmo_seleccionado.get(), velocidad_seleccionada.get()