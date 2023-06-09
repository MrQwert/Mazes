## ---------------------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------------------
## ARCHIVO "MAIN.PY" CONTIENE EL BUCLE PRINCIPAL DEL PROGRAMA, EL CUAL PERMITE AL USUARIO ESCOGER UNA SERIE DE OPCIONES,
## Y DADA SU SELECCIÓN, IMPRIME DE FORMA VISUAL LA RESOLUCIÓN DEL LABERINTO
## ---------------------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------------------


## -----------------Librerías-------------------------
import tkinter as tk
import gc
from src import *


## -----------------Comienza el programa-----------------

## Diccionarios con las distintas opciones que puede devolver el usuario cuando la ventana "home" finaliza
dic_seleccion_laberinto = dict({1:"maze_pequenio.txt",2:"laberinto_roberto.txt",3:"maze_grande.txt",4:"maze_custom.txt"})

dic_seleccion_algoritmo = dict({1:"Anchura",2:"Profundidad",3:"A*",4:"Avara",5:"CosteMin",6:"MiniMax"})

dic_seleccion_heuristica = dict({1:"Manhattan",2:"Euclidea",3:"Chebyshev"})

## Indica los milisegundos que el programa espera entre cada movimiento de búsqueda en el laberinto 
## EJ: "1:350" --> La opción 1, la lenta, esperaría 350ms
dic_seleccion_velocidad = dict({1:350,2:50,3:10})

## Bucle principal del programa, mostrar al usuario la ventana "home", que escoja, imprimir visualmente
## su elección, y vuelta a empezar
while (True):
    tipo_laberinto, algoritmo_busqueda, tipo_heuristica, velocidad_impresion = crear_home()

    ## Prints para comprobar que hemos recogido correctamente las elecciones introducidas por el usuario
    print("\nDatos recibidos de la ventana home:")
    print("tipo_laberinto = "+dic_seleccion_laberinto[tipo_laberinto])
    print("algoritmo_busqueda = "+dic_seleccion_algoritmo[algoritmo_busqueda])
    print("tipo_heuristica = "+dic_seleccion_heuristica[tipo_heuristica])
    print("velocidad_impresion = "+str(dic_seleccion_velocidad[velocidad_impresion])+"\n")


    if(dic_seleccion_algoritmo[algoritmo_busqueda] == "MiniMax"):
        ## Ejecutamos al minimax por terminal
        main_minimax()

    else:
        with open("Laberintos/"+dic_seleccion_laberinto[tipo_laberinto],'r') as f:
            laberinto = f.read().split('\n')

        ## Seleccionamos el algoritmo que haya indicado el usuario
        ## (FALTA MINIMAX)
        if(dic_seleccion_algoritmo[algoritmo_busqueda] == "Anchura"):
            algoritmo = Anchura(laberinto)
            tiene_tupla = True
        elif(dic_seleccion_algoritmo[algoritmo_busqueda] == "Profundidad"):
            algoritmo = Profundidad(laberinto)
            tiene_tupla = True
        elif(dic_seleccion_algoritmo[algoritmo_busqueda] == "A*"):
            ## Este algoritmo hace uso de la heurística seleccionada por el usuario
            algoritmo = A_Star(laberinto,dic_seleccion_heuristica[tipo_heuristica])
            tiene_tupla = False
        elif(dic_seleccion_algoritmo[algoritmo_busqueda] == "Avara"):
            ## Este algoritmo hace uso de la heurística seleccionada por el usuario
            algoritmo = Avara(laberinto,dic_seleccion_heuristica[tipo_heuristica])
            tiene_tupla = False
        elif(dic_seleccion_algoritmo[algoritmo_busqueda] == "CosteMin"):
            algoritmo = Coste_Min(laberinto)
            tiene_tupla = False


        ## Resolvemos el laberinto
        resolver_mapa_algoritmo(dic_seleccion_velocidad[velocidad_impresion], laberinto,algoritmo,tiene_tupla)

        ## Borrar de memoria restos
        del(algoritmo)
        del(laberinto)
        gc.collect()
