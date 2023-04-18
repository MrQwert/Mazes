import tkinter as tk
from tkinter import messagebox
from time import sleep
from os import system
import sys

## Función para el boton "Cerrar programa" de la ventana de home
def cerrarPrograma(ventana):
    ventana.destroy()
    sys.exit()


## Función para el boton "Ejecutar búsqueda" de la ventana de home
def opcionesSeleccionadas(ventana,etiqueta_error,laberinto_seleccionado,heuristica_seleccionada,algoritmo_seleccionado,velocidad_seleccionada):
    
    if(laberinto_seleccionado.get()==0 or heuristica_seleccionada.get()==0 or algoritmo_seleccionado.get()==0 or velocidad_seleccionada.get()==0):
        ## Incorrecto, avisamos al usuario
        etiqueta_error.config(text = "¡Error!\nSeleccione todas las opciones")
    else:
        ## Correcto, se acaba esta pantalla
        ventana.destroy()


## Función para detectar cuando el usuario cierra una ventana manualmente
def on_closing(ventana):
    if(messagebox.askokcancel("AVISO", "¿Quieres cerrar el programa?") == True):
        print("\nDestruyendo ventana y cerrando programa...\n")
        ventana.destroy()
        sys.exit()
    else:
        print("\nCierre abortado\n")
