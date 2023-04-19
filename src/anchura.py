## ---------------------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------------------
## ARCHIVO "ANCHURA.PY" CONTIENE LA CLASE Y MÉTODOS NECESARIOS PARA RESOLVER UN LABERINTO USANDO BÚSQUEDA EN ANCHURA
## ---------------------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------------------

## -----------------Librerías-------------------------
from time import sleep
from os import system
import tkinter as tk 
from tkinter import messagebox
import sys
from src.impresion_laberinto import *

# Se define la clase 'Anchura' para implementar el algoritmo de búsqueda en anchura
class Anchura:
    """
    Esta clase contiene varios atributos y métodos:

    - Atributos: almacenar información como el laberinto, los estados abiertos, cerrados, iniciales, actuales y finales, y las operaciones posibles.
    - Métodos: para inicializar el objeto, obtener índices de caracteres específicos, abrir un estado, comprobar el estado actual, e imprimir el laberinto.
    """
    
    

    operadores = ['arriba','abajo','izquierda','derecha']
    operaciones = { # Se codifican las operaciones
            'arriba'    : (0,-1),
            'abajo'     : (0, 1),
            'izquierda' : (-1,0),
            'derecha'   : (1 ,0)
        }
    
    def __init__(self,laberinto) -> None: # Constructor de la clase.
        self.abierto = []#
        self.cerrado = []#
        self.estados = []#
        self.todos = {}#
        self.estado_inicial  = ((None,None),(None,None))#
        self.estado_actual   = ((None,None),(None,None))#
        self.estado_final    = ((None,None),(None,None))#
        self.laberinto = laberinto
        
        self.estado_inicial = self.obtener_indices('e') # Obtenemos la posición de la entrada al laberinto.
        self.estado_actual = self.estado_inicial # La entrada será el estado actual.
        self.estado_final = self.obtener_indices('s') # Obtenemos la posición de la salida del laberinto.
        if '$' in self.estado_inicial + self.estado_final: # Comprobamos que exista tanto entrada como salida.
            raise Exception('¡Debe haber una entrada "e" y una salida "s" en el laberinto!')
        
        self.abrir_estado()
        
    def obtener_indices(self,char):
        """
         Función para buscar la posición del caracter 'char'. Si no lo encuentra, devuelve ($,$). 
        """
        for idx, row in enumerate(self.laberinto):
            if char in row:
                return ((self.laberinto[idx].index(char), idx),(None,None))
        return '$','$'
    
    
    def abrir_estado(self):
        """
        Esta función se utiliza para expandir los nodos adyacentes al estado actual en el laberinto. El propósito principal de esta función es agregar todos los estados accesibles y válidos a la lista de estados abiertos (nodos por explorar) y actualizar el diccionario todos con la relación entre el estado actual y sus estados adyacentes.
        """
        for operador in self.operadores: # Se recorren todos los operadores disponibles
            x, y = self.operaciones[operador]
            nuevo_estado = (self.estado_actual[0][0] + x, self.estado_actual[0][1] + y) # Se calcula el nuevo estado sumando las coordenadas del estado actual con las coordenadas correspondientes al operador
            try:
                if self.laberinto[nuevo_estado[1]][nuevo_estado[0]] != '+' and self.laberinto[nuevo_estado[1]][nuevo_estado[0]] != 'e' and nuevo_estado not in self.estados and nuevo_estado not in self.cerrado: #  se verifica si el nuevo estado es accesible y válido, es decir, si no es una pared ('+') y si no está en las listas de estados ya visitados (estados y cerrados). Si se cumplen las condiciones, se agrega el nuevo estado a la lista de estados abiertos y se actualiza el diccionario todos.
                        self.abierto.append((nuevo_estado,self.estado_actual[0]))
                        self.estados.append(nuevo_estado)
                        self.todos[nuevo_estado] = self.estado_actual[0]
            except:
                pass


    def comprobar_estado(self):
        """
        Esta función se utiliza para comprobar si se ha alcanzado el estado final (la salida del laberinto) y actualizar el estado actual. La función devuelve True si se alcanza el estado final y False en caso contrario.
        """
        try:
            estado = self.abierto.pop(0) # Se intenta obtener el siguiente estado de la lista de estados abiertos (FIFO)
        except: # Si no hay más estados abiertos, se considera que el laberinto no tiene solución y se termina la ejecución del programa.
            print('¡El laberinto introducido no tiene solución!')
            return -1
        self.estado_actual = estado # Se actualiza el estado actual con el estado obtenido de la lista de estados abiertos
        self.abrir_estado() # Se llama a la función abrir_estado() para expandir los nodos adyacentes al estado actual
        self.cerrado.append(estado) # Se agrega el estado actual a la lista de estados cerrados (nodos ya explorados)
        if self.estado_actual[0] == self.estado_final[0]: # Se comprueba si el estado actual es igual al estado final
            return True
        if self.estado_actual[0] != self.estado_inicial[0]: # Si el estado actual no es el estado final ni el estado inicial, se actualiza el laberinto con el símbolo '#' para marcar la posición actual
            self.laberinto[estado[0][1]] = self.laberinto[estado[0][1]][:estado[0][0]]+'#'+self.laberinto[estado[0][1]][estado[0][0]+1:]
        return False


## Función para resolver el mapa con el algoritmo, velocidad y mapa que reciba
def resolver_mapa_anchura(milisegundos, laberinto, sol):


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
        sleep(milisegundos/1000)


    state = sol.estado_final[0]

    while state != sol.estado_inicial[0]: # Se imprime la solución final paso a paso, marcando los movimientos realizados con el símbolo '@'
        actualizar_pantalla(laberinto, ventana, celdas,"yellow",state[1],state[0])
        state = sol.todos[state]
        sleep(milisegundos/1000)


    messagebox.showinfo(message="Haga click para continuar", title="AVISO")
    ventana.destroy()

    return
