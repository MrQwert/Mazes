import tkinter as tk
from src import *

print("\nHola mundo!\n")


while (True):
	tipo_mapa, algoritmo_busqueda, velocidad_impresion = crear_home()

	print("tipo_mapa = "+str(tipo_mapa))
	print("algoritmo_busqueda = "+str(algoritmo_busqueda))
	print("velocidad_impresion = "+str(velocidad_impresion))

	resolver_mapa_anchura(35, "maze_extra_small.txt")

	print("\nAdios mundo!\n")
