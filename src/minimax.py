# BASADA EN LA IMPLEMENTACIÓN DEL TRES EN RALLA (TIC-TAC-TOE) DE:
# Russell, S., & Norvig, P. (2010). Artificial Intelligence A Modern Approach Third Edition.
# In Pearson. https://doi.org/10.1017/S0269888900007724

import random
import math
import functools
import copy
from time import sleep

cache = functools.lru_cache(10 ** 6)

PLAYER_MAX = "e"
PLAYER_MIN = "s"
PARED = "+"
CAMINO = "."
TESORO = "X"


class Competicion:
    """Un juego es similar a un problema, pero tiene una prueba terminal en lugar 
    de una prueba de objetivo y una utilidad para cada estado terminal. Para crear 
    un juego, se debe crear una subclase de esta clase e implementar acciones, resultado,
    es_terminal y utilidad. También es necesario establecer el atributo .initial en el
    estado inicial; esto puede hacerse en el constructor."""


class Minimax:
    """Clase para implementar el algoritmo de búsqueda Minimax
    en un laberinto, necesitando que el jugador 's' llegue a uno de los premios 'X' 
    antes que su oponente para ganar. 's' mueve primero."""
    operadores = ['arriba', 'abajo', 'izquierda', 'derecha']
    operaciones = {  # Se codifican las operaciones
        'arriba': (0, -1),
        'abajo': (0, 1),
        'izquierda': (-1, 0),
        'derecha': (1, 0)
    }

    def __init__(self):
        maze = 'maze_adv.txt'
        # Se lee el fichero seleccionado y se almacena en la variable laberinto.
        with open(maze, 'r') as f:
            l = f.read().split('\n')
            l = [list(row) for row in l]
        self.initial = Laberinto(laberinto=l, to_move=PLAYER_MAX, utilidad=0)
        self.laberinto = Laberinto(laberinto=l.copy(), to_move=PLAYER_MAX, utilidad=0)
        self.estados_finales = self.laberinto.obtener_indices(TESORO)

    def actions(self, laberinto):
        """Busca todas las acciones legales para un determinado jugador. 
        La función devuelve todas las posiciones a las que un jugador puede moverse
        tras aplicar todos los operadores legales en un determinado estado."""
        acciones = []
        _jugador = laberinto.to_move
        pos = laberinto.obtener_indices(_jugador)
        for operador in self.operadores:  # Se recorren todos los operadores disponibles
            x, y = self.operaciones[operador]
            nuevo_estado = (pos[0] + x, pos[1] + y)  # Se calcula el nuevo estado
            if 0 <= nuevo_estado[0] < laberinto.width and 0 <= nuevo_estado[1] < laberinto.height \
                    and laberinto[nuevo_estado] not in [PARED, CAMINO, PLAYER_MAX, PLAYER_MIN]:
                acciones.append(nuevo_estado)

        # Si un jugador se queda sin acciones (ha llegado a un callejón sin salida), la utilidad
        # de ese estado para el jugador es inferior a aquella de perder una partida contra su
        # oponente (su oponente llega rimero a un premio).
        if not acciones:
            laberinto.utilidad = (-2 if _jugador == PLAYER_MAX else +2)
        # Ordena las acciones a tomar en función de la menor distancia de Manhattan
        # a cualquiera de los premios del laberinto
        manhattan_distance = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
        acciones = sorted(acciones, key=lambda estado: min(manhattan_distance(estado, tesoro)
                                                           for tesoro in self.estados_finales))
        return acciones

    def result(self, laberinto, pos):
        """Se calcula el laberinto resultante de mover un determinado jugador a
        una posición específica en el laberinto. Esto incluye la utilidad
        para el nuevo estado y si éste es un estado terminal o no."""
        _jugador = laberinto.to_move
        laberinto = laberinto.new(player=_jugador, nueva_pos=pos,
                                  to_move=(PLAYER_MIN if _jugador == PLAYER_MAX else PLAYER_MAX))
        win = self.tesoro_encontrado(laberinto, _jugador)
        laberinto.utilidad = (0 if not win else +1 if _jugador == PLAYER_MAX else -1)
        return laberinto

    @staticmethod
    def utilidad(laberinto, _jugador):
        """Calcula la utilidad para un determinado jugador para
        una determinada configuración del laberinto (signo de la
        utilidad depende de si el jugador es MIN o MAX)"""
        return laberinto.utilidad if _jugador == PLAYER_MAX else -laberinto.utilidad

    def es_terminal(self, laberinto):
        """Una determinada configuración de un laberinto es terminal
        si uno de los jugadores ha llegado a una de las casillas con
        premio o uno de los jugadores no tiene acciones disponibles."""
        return laberinto.utilidad != 0 or len(self.actions(laberinto)) == 0

    @staticmethod
    def display(laberinto):
        print(laberinto)

    def tesoro_encontrado(self, laberinto, _jugador):
        """Función que comprueba si un jugador se encuentra en una
        de las posiciones con premio."""
        pos = laberinto.obtener_indices(_jugador)
        return True if pos in self.estados_finales else False


class Laberinto:
    """Un laberinto se define como una clase cuyo atributo más importante
    es una lista de listas las cuales representan la configuración de un laberinto
    en un instante de tiempo t."""

    def __init__(self, laberinto, to_move=None, utilidad=0):
        self.laberinto = laberinto
        self.width = len(laberinto[0])
        self.height = len(laberinto)
        self.to_move = to_move
        self.utilidad = utilidad

    def __setitem__(self, pos, data):
        self.laberinto[pos[1]][pos[0]] = data

    def __getitem__(self, pos):
        return self.laberinto[pos[1]][pos[0]]

    def new(self, player, nueva_pos, to_move) -> 'Laberinto':
        """Devuelve un nuevo laberinto en el que se actualiza el estado del mismo
        en función de la acción tomada por el jugador del cual fuese el turno."""
        laberinto = Laberinto(
            laberinto=self.laberinto.copy(),
            to_move=to_move,
            utilidad=self.utilidad)

        pos = laberinto.obtener_indices(player)
        laberinto[pos] = CAMINO
        laberinto[nueva_pos] = player
        return laberinto

    def obtener_indices(self, char):
        """
         Función para buscar la(s) posición(es) del caracter 'char'. Si no lo encuentra, devuelve ($,$).
        """
        posiciones = []
        for idx, row in enumerate(self.laberinto):
            if char in row:
                posiciones.append((self.laberinto[idx].index(char), idx))
        if len(posiciones) == 0:
            return '$', '$'
        elif len(posiciones) == 1:
            return posiciones[0]
        else:
            return posiciones

    def __hash__(self):
        return hash(self.laberinto) + hash(self.to_move)

    def __repr__(self):
        def row(y): return ''.join(self[x, y] for x in range(self.width))

        return '\n'.join(map(row, range(self.height))) + '\n'


def minmax_alphabeta(laberinto, estado_inicial):
    """Realiza una búsqueda empleando el algoritmo de búsqueda minimax para determinar
    la mejor acción para un jugador desde un determinado estado. Para optimizar
    la complejidad del algoritmo, se emplea alfa-beta prunning para reducir
    el número de ramas del árbol de estados las cuales se explorarán.
    No hay 'iterative deepening'."""

    infinito = math.inf
    _jugador = estado_inicial.to_move

    def valor_max(_estado, alpha, beta, d):
        print(_estado)
        sleep(0.5)
        if laberinto.es_terminal(_estado):
            return laberinto.utilidad(_estado, _jugador), None
        v, movimiento = -infinito, None
        acciones_posibles = laberinto.actions(_estado)
        for a in acciones_posibles:
            print(d, 'e', a)
            v2, _ = valor_min(laberinto.result(copy.deepcopy(_estado), a), alpha, beta, d + 1)
            if v2 > v:
                v, movimiento = v2, a
                alpha = max(alpha, v)
            if v >= beta:
                return v, movimiento
        return v, movimiento

    def valor_min(_estado, alpha, beta, d):
        print(_estado)
        sleep(0.5)
        if laberinto.es_terminal(_estado):
            return laberinto.utilidad(_estado, _jugador), None
        v, move = +infinito, None
        acciones_posibles = laberinto.actions(_estado)
        for a in acciones_posibles:
            print(d, 's', a)
            v2, _ = valor_max(laberinto.result(copy.deepcopy(_estado), a), alpha, beta, d + 1)
            if v2 < v:
                v, move = v2, a
                beta = min(beta, v)
            if v <= alpha:
                return v, move
        return v, move

    return valor_max(estado_inicial, -infinito, +infinito, 0)


def jugador(algoritmo):
    """Implementa a un jugador que sigue una determinada estrategia de juego."""
    return lambda game, state: algoritmo(game, state)[1]

def jugar(competicion, strategies: dict, verbose=False):
    """Juega a un juego hasta que éste finaliza."""
    estado = competicion.initial
    while not competicion.es_terminal(estado):
        _jugador = estado.to_move
        move = strategies[_jugador](competicion, estado)
        estado = competicion.result(estado, move)
        if verbose:
            print('Player', _jugador, 'move:', move)
            print(estado)
    return estado


def main():
    competicion_laberinto = Minimax()

    estado = jugar(competicion=competicion_laberinto,
                   strategies={PLAYER_MAX: jugador(minmax_alphabeta), PLAYER_MIN: jugador(minmax_alphabeta)},
                   verbose=True)
    print(estado)
    print(estado.utilidad)
    if estado.utilidad == 1:
        print("¡El jugador MAX ha encontrado la solución óptima! ¡Va a ganar el juego siempre! (Abusón...)")
    else:
        print("El jugador MAX no puede ganar este juego si MIN es un jugador óptimo :(")


if __name__ == "__main__":
    main()
