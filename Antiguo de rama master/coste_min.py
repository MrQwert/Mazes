from queue import PriorityQueue
from time import sleep
from os import system

SPEED = 100

# maze = 'maze_small.txt' # Descomentar el seleccionado
maze = 'maze_big.txt'  # Descomentar el seleccionado
with open(maze, 'r') as f:
    laberinto = f.read().split('\n')


class Coste_Min:
    abierto = PriorityQueue()
    cerrado = []
    laberinto = None
    estado_inicial = (None, None)
    estado_actual = (None, None)
    estado_final = (None, None)
    operadores = ['arriba', 'abajo', 'izquierda', 'derecha']
    operaciones = {
        'arriba': (0, -1),
        'abajo': (0, 1),
        'izquierda': (-1, 0),
        'derecha': (1, 0)
    }
    costes = {
        'arriba': 3,
        'abajo': 2,
        'izquierda': 4,
        'derecha': 1
    }

    def __init__(self, laberinto) -> None:
        self.laberinto = laberinto
        self.estado_inicial = self.obtener_indices('e')
        self.estado_actual = self.estado_inicial
        self.estado_final = self.obtener_indices('s')
        if '$' in self.estado_inicial + self.estado_final:
            raise Exception('¡Debe haber una entrada "e" y una salida "s" en el laberinto!')

        self.abrir_estado(0)

    def obtener_indices(self, char):
        for idx, row in enumerate(self.laberinto):
            if char in row:
                return self.laberinto[idx].index(char), idx
        return '$', '$'

    def calcular_prioridad(self, coste):
        return coste

    def abrir_estado(self, coste):
        for operador in self.operadores:
            x, y = self.operaciones[operador]
            nuevo_estado = (self.estado_actual[0] + x, self.estado_actual[1] + y)
            nuevo_coste = coste + self.costes[operador]
            try:
                if self.laberinto[nuevo_estado[1]][nuevo_estado[0]] != '+' and \
                        nuevo_estado not in self.abierto.queue and nuevo_estado not in self.cerrado:
                    self.abierto.put((self.calcular_prioridad(nuevo_coste), nuevo_estado, nuevo_coste))
            except Exception as e:
                pass

    def comprobar_estado(self):
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
            self.laberinto[estado[1][1]] = self.laberinto[estado[1][1]][:estado[1][0]] + \
                                           '#' + self.laberinto[estado[1][1]][estado[1][0] + 1:]
        return False

    def imprime_laberinto(self):
        for row in self.laberinto:
            print(row)


sol = Coste_Min(laberinto)

while sol.estado_actual != sol.estado_final:
    if sol.comprobar_estado():
        sol.imprime_laberinto()
        break
    sol.imprime_laberinto()
    sleep(1 / SPEED)
    system('cls')
