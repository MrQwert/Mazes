## ---------------------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------------------
## ARCHIVO "IMPRESION_LABERINTO.PY" CONTIENE LAS FUNCIONES NECESARIAS PARA MOSTRAR DE MANERA VISUAL, EN UNA VENTANA DE
## TKINTER, LA BÚSQUEDA QUE REALIZA UN ALGORITMO EN UN LABERINTO
## ---------------------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------------------

## -----------------Librerías-------------------------
import tkinter as tk
from tkinter import messagebox
from time import sleep
from os import system
import sys
from src.funciones_auxiliares import *


## -----------------Comienzan las funciones-----------------

## Función para crear la ventana de impresión del laberinto
def crear_ventana_laberinto(laberinto):

    ## Creamos la ventana
    ventana = tk.Tk()
    ventana.title("Laberinto")

    ## La posicionamos centrada
    ventana.eval('tk::PlaceWindow . center')

    ## Celdas de la ventana, cada una contendrá una posición del mapa, que se representará como un pequeño cuadrado
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
            elif caracter == 'X':
                color='purple'
            ## Creamos la celda y la posicionamos en el grid
            lbl_celda = tk.Label(ventana, width=2, height=1, bg=color, relief=tk.SUNKEN, borderwidth=1)
            lbl_celda.grid(row=i, column=j)
            fila_celdas.append(lbl_celda)
        celdas.append(fila_celdas)

    ventana.update()

    ## Controlar que el usuario cierre la ventana durante la impresión
    ventana.protocol("WM_DELETE_WINDOW", lambda: on_closing(ventana))

    return ventana, celdas


## Función para actualizar la ventana del laberinto, pintando cada celda de su color correspondiente 
def actualizar_pantalla(laberinto, ventana, celdas, color,i,j):

    try:
        celdas[i][j].config(bg=color)
        ventana.update()
    except:
        print("\nEl usuario ha cerrado la ventana durante la impresion, cerrando programa...")
        sys.exit()


## Función para resolver el mapa con el algoritmo, velocidad y mapa que reciba
def resolver_mapa_algoritmo(milisegundos, laberinto, algoritmo, tiene_tupla):


    ventana, celdas = crear_ventana_laberinto(laberinto)


    while algoritmo.estado_actual != algoritmo.estado_final: # Se ejecuta el algoritmo hasta encontrar la salida
        

        resultado_comprobacion = algoritmo.comprobar_estado()

        if resultado_comprobacion == -1:
            messagebox.showinfo(message="El laberinto no tiene solución", title="Titulo")
            ventana.destroy()
            return

        if(tiene_tupla == True):
            actualizar_pantalla(algoritmo.laberinto, ventana, celdas,"blue",algoritmo.estado_actual[0][1],algoritmo.estado_actual[0][0])
        else:
            actualizar_pantalla(algoritmo.laberinto, ventana, celdas,"blue",algoritmo.estado_actual[1],algoritmo.estado_actual[0])
        if resultado_comprobacion == True:
            break
        sleep(milisegundos/1000)


    if(tiene_tupla == True):
        state = algoritmo.estado_final[0]
        while state != algoritmo.estado_inicial[0]: # Se imprime la solución final paso a paso, marcando los movimientos realizados con el símbolo '@'
            actualizar_pantalla(laberinto, ventana, celdas,"yellow",state[1],state[0])
            state = algoritmo.todos[state]
            sleep(milisegundos/1000)
    else:
        state = algoritmo.estado_final
        while state != algoritmo.estado_inicial: # Se imprime la solución final paso a paso, marcando los movimientos realizados con el símbolo '@'
            actualizar_pantalla(laberinto, ventana, celdas,"yellow",state[1],state[0])
            state = algoritmo.todos[state]
            sleep(milisegundos/1000)
    

    messagebox.showinfo(message="Haga click para continuar", title="AVISO")

    ventana.destroy()

    return