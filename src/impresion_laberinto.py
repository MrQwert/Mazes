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
def actualizar_pantalla(estado_actual,laberinto, ventana, celdas, color):

    # try:
    #     i = estado_actual[0][1]
    #     j = estado_actual[0][0]
    #     celda = laberinto[i][j]
    #     if celda == '+':
    #         celdas[i][j].config(bg='black')
    #     elif celda == ' ':
    #         celdas[i][j].config(bg='white')
    #     elif celda == 'e':
    #         celdas[i][j].config(bg='green')
    #     elif celda == 's':
    #         celdas[i][j].config(bg='red')
    #     elif celda == '#':
    #         celdas[i][j].config(bg='blue')
    #     elif celda == '@':
    #         celdas[i][j].config(bg='yellow')
    # except:
    #     print("\nHan cerrado la ventana de impresión del laberinto y cerramos el programa...\n")
    #     sys.exit()


    i = estado_actual[0][1]
    j = estado_actual[0][0]
    print("\ni="+str(i)+" j="+str(j))
    print(laberinto[i][j])
    celdas[i][j].config(bg=color)

    ventana.update()


## Función para actualizar la ventana del laberinto, pintando cada celda de su color correspondiente 
def actualizar_pantalla_2(estado_actual,laberinto, ventana, celdas, color):

    # try:
    #     i = estado_actual[0][1]
    #     j = estado_actual[0][0]
    #     celda = laberinto[i][j]
    #     if celda == '+':
    #         celdas[i][j].config(bg='black')
    #     elif celda == ' ':
    #         celdas[i][j].config(bg='white')
    #     elif celda == 'e':
    #         celdas[i][j].config(bg='green')
    #     elif celda == 's':
    #         celdas[i][j].config(bg='red')
    #     elif celda == '#':
    #         celdas[i][j].config(bg='blue')
    #     elif celda == '@':
    #         celdas[i][j].config(bg='yellow')
    # except:
    #     print("\nHan cerrado la ventana de impresión del laberinto y cerramos el programa...\n")
    #     sys.exit()


    i = estado_actual[1]
    j = estado_actual[0]
    print("\ni="+str(i)+" j="+str(j))
    print(laberinto[i][j])
    celdas[i][j].config(bg=color)

    ventana.update()


## Función para resolver el mapa con el algoritmo, velocidad y mapa que reciba
def resolver_mapa_anchura(speed, laberinto, sol):
    SPEED = speed


    # Se crea una copia que luego utilizaremos para mostrar la solución.
    clear_maze = laberinto.copy()

    ventana, celdas = crear_ventana_laberinto(laberinto)


    #sleep(100)

    while sol.estado_actual != sol.estado_final: # Se ejecuta el algoritmo hasta encontrar la salida
        
        #sleep(1)

        resultado_comprobacion = sol.comprobar_estado()

        if resultado_comprobacion == -1:
            messagebox.showinfo(message="El laberinto no tiene solución", title="Titulo")
            ventana.destroy()
            return

        actualizar_pantalla(sol.estado_actual,sol.laberinto, ventana, celdas,"blue")

        if resultado_comprobacion == True:
            break
        ventana.after(1000 // SPEED)


    system('clear')
    state = sol.estado_final[0]

    while state != sol.estado_inicial[0]: # Se imprime la solución final paso a paso, marcando los movimientos realizados con el símbolo '@'
        state = sol.todos[state]
        clear_maze[state[1]] = clear_maze[state[1]][:state[0]]+'@'+clear_maze[state[1]][state[0]+1:]
        print("\nSTATE\n")
        print(state)
        #sleep(100)
        actualizar_pantalla_2(state,clear_maze, ventana, celdas,"yellow")
        ventana.after(1000 // SPEED)
        if state != sol.estado_inicial[0]:
            system('clear')


    messagebox.showinfo(message="Haga click para continuar", title="AVISO")
    ventana.destroy()

    return



# ## Función para imprimir el recorrido de la solución del laberinto
# def print_laberinto(l):
#         for row in l:
#             print(row)