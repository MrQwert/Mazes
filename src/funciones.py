import tkinter as tk
from time import sleep
from os import system
import sys

def cerrarPrograma(ventana):
	ventana.destroy()
	sys.exit()

def opcionesSeleccionadas(ventana,etiqueta_error,mapa_seleccionado,algoritmo_seleccionado,velocidad_seleccionada):
	
	if(mapa_seleccionado.get()==0 or algoritmo_seleccionado.get()==0  or velocidad_seleccionada.get()==0):
		etiqueta_error.config(text = "¡Error!\nSeleccione todas las opciones")
	else:
		## Correcto, se acaba esta pantalla
		ventana.destroy()

