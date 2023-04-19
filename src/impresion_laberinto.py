import tkinter as tk
from tkinter import messagebox
from time import sleep
from os import system
import sys
from src.funciones_auxiliares import *

## Función para crear la ventana de impresión del laberinto
def crear_ventana_laberinto(laberinto):
    ventana = tk.Tk()
    ventana.title("Laberinto")

    ventana.eval('tk::PlaceWindow . center')

    celdas = []

    ## Recorremos todo el mapa pintando del color correspondiente cada celda
    for i, fila in enumerate(laberinto):
        fila_celdas = []
        for j, celda in enumerate(fila):
            caracter = laberinto[i][j]
            if caracter == '+':
                color='black'
            elif caracter == ' ':
                color='white'
            elif caracter == 'e':
                color='green'
            elif caracter == 's':
                color='red'
            elif caracter == '#':
                color='blue'
            elif caracter == '@':
                color='yellow'
            lbl_celda = tk.Label(ventana, width=2, height=1, bg=color, relief=tk.SUNKEN, borderwidth=1)
            lbl_celda.grid(row=i, column=j)
            fila_celdas.append(lbl_celda)
        celdas.append(fila_celdas)

    ventana.update()
    ventana.protocol("WM_DELETE_WINDOW", lambda: on_closing(ventana))

    return ventana, celdas


## Función para actualizar la ventana del laberinto, pintando cada celda de su color correspondiente 
def actualizar_pantalla(laberinto, ventana, celdas, color,i,j):

    celdas[i][j].config(bg=color)
    ventana.update()


## Función para resolver el mapa con el algoritmo, velocidad y mapa que reciba
def resolver_mapa_anchura(speed, laberinto, sol):
    SPEED = speed

    ventana, celdas = crear_ventana_laberinto(laberinto)


    while sol.estado_actual != sol.estado_final: # Se ejecuta el algoritmo hasta encontrar la salida
        

        resultado_comprobacion = sol.comprobar_estado()

        if resultado_comprobacion == -1:
            messagebox.showinfo(message="El laberinto no tiene solución", title="Titulo")
            ventana.destroy()
            return

        actualizar_pantalla(sol.laberinto, ventana, celdas,"blue",sol.estado_actual[0][1],sol.estado_actual[0][0])

        if resultado_comprobacion == True:
            break
        ventana.after(1000 // SPEED)


    state = sol.estado_final[0]

    while state != sol.estado_inicial[0]: # Se imprime la solución final paso a paso, marcando los movimientos realizados con el símbolo '@'
        actualizar_pantalla(laberinto, ventana, celdas,"yellow",state[1],state[0])
        state = sol.todos[state]
        ventana.after(1000 // SPEED)

    # Pinto la última casilla
    actualizar_pantalla(laberinto, ventana, celdas,"yellow",state[1],state[0])
    messagebox.showinfo(message="Haga click para continuar", title="AVISO")
    ventana.destroy()

    print("\nFIN FUNCION IMPRESION LABERINTO")

    return
