"""
El presente código resuelve laberintos utilizando el algoritmo Avaro.
"""
from queue import PriorityQueue
from time import sleep
from os import system

# Importamos las librerías necesarias para el algoritmo Avaro y la visualización en consola


SPEED = 100 # Se establece la velocidad a la que se imprimirá el proceso de búsqueda.
CON_COSTES = True  # Se establece si al algoritmo implementado trabajará con coste uniforme o no.

# Leemos el archivo del laberinto y copiamos su contenido a una variable para luego imprimir la solución
maze = 'maze_big.txt'  # Descomentar el seleccionado
with open(maze, 'r') as f:
    laberinto = f.read().split('\n')

clear_maze = laberinto.copy()


class Avara:
    """
    Esta clase implementa el algoritmo de búsqueda Avara para encontrar el camino
    más corto en un laberinto desde la entrada hasta la salida, evitando obstáculos.

    Atributos:
        abierto (PriorityQueue): Cola de prioridad que contiene los estados abiertos (por explorar).
        cerrado (list): Lista que contiene los estados cerrados (explorados).
        todos (dict): Diccionario que mapea cada estado con su estado predecesor.
        laberinto (list): Representación del laberinto como una lista de strings.
        operadores (list): Lista de operadores para generar estados vecinos.
        operaciones (dict): Diccionario que mapea los operadores con sus respectivos desplazamientos en el laberinto.
        costes (dict): Diccionario que mapea los operadores con sus respectivos costes.
        estado_inicial (tuple): Coordenadas de la entrada del laberinto.
        estado_actual (tuple): Coordenadas del estado actual en el algoritmo avaro.
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

    def calcular_prioridad(self, estado):
        # Función para calcular la prioridad (distancia de Manhattan) de un estado
        h_manhattan = abs(self.estado_final[0] - estado[0]) + abs(self.estado_final[1] - estado[1])
        return h_manhattan

    def abrir_estado(self, coste):
        # Función para generar estados vecinos y agregarlos a la cola de prioridad
        for operador in self.operadores:
            x, y = self.operaciones[operador]
            nuevo_estado = (self.estado_actual[0] + x, self.estado_actual[1] + y)
            if CON_COSTES:
                nuevo_coste = coste + self.costes[operador]
            else:
                nuevo_coste = coste + 1
            try:
                if self.laberinto[nuevo_estado[1]][nuevo_estado[0]] != '+' and nuevo_estado not in self.abierto.queue and nuevo_estado not in self.cerrado:
                    # En la cola de prioridad se almacena el estado y el coste para llegar al mismo.
                    self.abierto.put((self.calcular_prioridad(nuevo_estado), nuevo_estado, nuevo_coste))
                    self.todos[nuevo_estado] = self.estado_actual
            except Exception as e:
                pass

    def comprobar_estado(self):
        # Función para comprobar si el estado actual es el estado final
        if not self.abierto.empty():
            estado = self.abierto.get()
        else:
            print('¡El laberinto introducido no tiene solución!')
            exit()

        self.estado_actual = estado[1]
        self.abrir_estado(estado[2])
        self.cerrado.append(estado[1])

        if self.estado_actual == self.estado_final:
            return True

        if self.estado_actual != self.estado_inicial:
            self.laberinto[estado[1][1]] = self.laberinto[estado[1][1]][:estado[1][0]] \
                                           + '#' + self.laberinto[estado[1][1]][estado[1][0] + 1:]

        return False

    def imprime_laberinto(self):
        for row in self.laberinto:
            print(row)


def print_laberinto(l):
    for row in l:
        print(row)


sol = Avara(laberinto)

while sol.estado_actual != sol.estado_final:
    if sol.comprobar_estado():
        sol.imprime_laberinto()
        break
    sol.imprime_laberinto()
    sleep(1 / SPEED)
    system('clear')


state = sol.estado_final
while state != sol.estado_inicial:
    state = sol.todos[state]
    clear_maze[state[1]] = clear_maze[state[1]][:state[0]] + '@' + clear_maze[state[1]][state[0] + 1:]
    print_laberinto(clear_maze)
    sleep(1 / SPEED)
    if state != sol.estado_inicial:
        system('cls')
