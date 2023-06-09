## ---------------------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------------------
## ARCHIVO "COSTE_MIN.PY" CONTIENE LA CLASE Y MÉTODOS NECESARIOS PARA RESOLVER UN LABERINTO USANDO BÚSQUEDA COSTE MÍNIMO
## ---------------------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------------------

## -----------------Librerías-------------------------
from time import sleep
from os import system
import tkinter as tk 
from tkinter import messagebox
import sys
from queue import PriorityQueue

# Se define la clase 'COste_Min' para implementar el algoritmo de búsqueda coste mínimo
class Coste_Min:
    """
    Esta clase implementa el algoritmo de búsqueda de Coste Mínimo para
    encontrar el camino más corto en un laberinto desde la entrada hasta la salida, evitando obstáculos.

    Atributos:
        abierto (PriorityQueue): Cola de prioridad que contiene los estados abiertos (por explorar).
        cerrado (list): Lista que contiene los estados cerrados (explorados).
        todos (dict): Diccionario que mapea cada estado con su estado predecesor.
        laberinto (list): Representación del laberinto como una lista de strings.
        operadores (list): Lista de operadores para generar estados vecinos.
        operaciones (dict): Diccionario que mapea los operadores con sus respectivos desplazamientos en el laberinto.
        costes (dict): Diccionario que mapea los operadores con sus respectivos costes.
        estado_inicial (tuple): Coordenadas de la entrada del laberinto.
        estado_actual (tuple): Coordenadas del estado actual en el algoritmo de Coste Mínimo.
        estado_final (tuple): Coordenadas de la salida del laberinto.

    Métodos:
        obtener_indices(char): Retorna las coordenadas del caracter especificado en el laberinto.
        calcular_prioridad(estado, coste): Calcula la prioridad de un estado basado en el coste acumulado.
        abrir_estado(coste): Genera estados vecinos y los agrega a la cola de prioridad.
        comprobar_estado(): Verifica si el estado actual es el estado final, y si no lo es, actualiza el estado actual.
        imprime_laberinto(): Imprime el laberinto en la consola.
    """
    def __init__(self, laberinto): # Constructor de la clase Avara
        self.abierto = PriorityQueue()
        self.cerrado = []
        self.todos = {}
        self.laberinto = laberinto
        self.operadores = ['arriba', 'abajo', 'izquierda', 'derecha']
        self.operaciones = {
            'arriba': (0, -1),
            'abajo': (0, 1),
            'izquierda': (-1, 0),
            'derecha': (1, 0)
        }
        self.costes = {
            'arriba': 3,
            'abajo': 2,
            'izquierda': 4,
            'derecha': 1
        }

        self.estado_inicial = self.obtener_indices('e')
        self.estado_actual = self.estado_inicial
        self.estado_final = self.obtener_indices('s')

        if '$' in self.estado_inicial + self.estado_final:
            raise Exception('¡Debe haber una entrada "e" y una salida "s" en el laberinto!')

        self.abrir_estado(0)

    def obtener_indices(self, char):
        # Función para obtener las coordenadas del caracter especificado (entrada o salida)
        for idx, row in enumerate(self.laberinto):
            if char in row:
                return self.laberinto[idx].index(char), idx
        return '$', '$'

    def calcular_prioridad(self, coste):
        # Función para calcular la prioridad (coste) de un estado
        return coste

    def abrir_estado(self, coste):
        # Función para generar estados vecinos y agregarlos a la cola de prioridad
        for operador in self.operadores:
            x, y = self.operaciones[operador]
            nuevo_estado = (self.estado_actual[0] + x, self.estado_actual[1] + y)
            nuevo_coste = coste + self.costes[operador]
            try:
                if self.laberinto[nuevo_estado[1]][nuevo_estado[0]] != '+' and self.laberinto[nuevo_estado[1]][nuevo_estado[0]] != 'e' and nuevo_estado not in self.abierto.queue and nuevo_estado not in self.cerrado:
                    # En la cola de prioridad se almacena el estado y el coste para llegar al mismo.
                    self.abierto.put((self.calcular_prioridad(nuevo_coste), nuevo_estado, nuevo_coste))
                    self.todos[nuevo_estado] = self.estado_actual
            except Exception as e:
                pass

    def comprobar_estado(self):
        # Función para comprobar si el estado actual es el estado final
        if not self.abierto.empty():
            estado = self.abierto.get()
        else:
            print('\n¡El laberinto introducido no tiene solución!')
            return -1

        self.estado_actual = estado[1]
        self.abrir_estado(estado[2])
        self.cerrado.append(estado[1])

        if self.estado_actual == self.estado_final:
            return True

        if self.estado_actual != self.estado_inicial:
            self.laberinto[estado[1][1]] = self.laberinto[estado[1][1]][:estado[1][0]] + '#' + self.laberinto[estado[1][1]][estado[1][0] + 1:]

        return False
