## ---------------------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------------------
## ARCHIVO "MAIN.PY" CONTIENE EL BUCLE PRINCIPAL DEL PROGRAMA, EL CUAL PERMITE AL USUARIO ESCOGER UNA SERIE DE OPCIONES,
## Y DADA SU SELECCIÓN, IMPRIME DE FORMA VISUAL LA RESOLUCIÓN DEL LABERINTO
## ---------------------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------------------


## -----------------Librerías-------------------------
import tkinter as tk
from src import *


## -----------------Comienza el programa-----------------

## Diccionarios con las distintas opciones que puede devolver el usuario cuando la ventana "home" finaliza
dic_seleccion_laberinto = dict({1:"maze_pequenio.txt",2:"maze_mediano.txt",3:"maze_grande.txt",4:"maze_custom.txt"})

dic_seleccion_algoritmo = dict({1:"Anchura",2:"Profundidad",3:"A*",4:"MinMax"})

dic_seleccion_heuristica = dict({1:"Manhattan",2:"Euclidea",3:"Chebyshev"})

## Indica los milisegundos que el programa espera entre cada movimiento de búsqueda en el laberinto 
## EJ: "1:350" --> La opción 1, la lenta, esperaría 350ms
dic_seleccion_velocidad = dict({1:350,2:50,3:10})

## Bucle principal del programa, mostrar al usuario la ventana "home", que escoja, imprimir visualmente
## su elección, y vuelta a empezar
while (True):
    tipo_laberinto, algoritmo_busqueda, tipo_heuristica, velocidad_impresion = crear_home()

    ## Prints temporales para comprobar que hemos recogido correctamente las elecciones introducidas por el usuario
    print("\nDatos recibidos de la ventana home:")
    print("tipo_laberinto = "+dic_seleccion_laberinto[tipo_laberinto])
    print("algoritmo_busqueda = "+dic_seleccion_algoritmo[algoritmo_busqueda])
    print("tipo_heuristica = "+dic_seleccion_heuristica[tipo_heuristica])
    print("velocidad_impresion = "+str(dic_seleccion_velocidad[velocidad_impresion])+"\n")

    ## Se lee el fichero seleccionado y se almacena en la variable laberinto.
    with open("Laberintos/"+dic_seleccion_laberinto[tipo_laberinto],'r') as f:
        laberinto = f.read().split('\n')

    ## Seleccionamos el algoritmo que haya indicado el usuario
    ## (EN CONSTRUCCIÓN)
    if(dic_seleccion_algoritmo[algoritmo_busqueda] == "Anchura"):
        algoritmo = Anchura(laberinto) 
    elif(dic_seleccion_algoritmo[algoritmo_busqueda] == "Profundidad"):
        algoritmo = Profundidad(laberinto)
    else:
        algoritmo = Anchura(laberinto) 

    ## Resolvemos el laberinto
    resolver_mapa_algoritmo(dic_seleccion_velocidad[velocidad_impresion], laberinto,algoritmo)
    del(algoritmo)
