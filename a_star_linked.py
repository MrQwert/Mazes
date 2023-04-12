from queue import PriorityQueue
from time import sleep
from os import system

SPEED = 100

maze = 'maze_big.txt'  # Descomentar el seleccionado
with open(maze, 'r') as f:
    laberinto = f.read().split('\n')

clear_maze = laberinto.copy()


class A_Star:
    def __init__(self, laberinto):
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

    def calcular_prioridad(self, estado, coste):
        h_manhattan = abs(self.estado_final[0] - estado[0]) + abs(self.estado_final[1] - estado[1])
        return h_manhattan + coste

    def abrir_estado(self, coste):
        for operador in self.operadores:
            x, y = self.operaciones[operador]
            nuevo_estado = (self.estado_actual[0] + x, self.estado_actual[1] + y)
            try:
                if self.laberinto[nuevo_estado[1]][nuevo_estado[0]] != '+' and nuevo_estado not in self.abierto.queue and nuevo_estado not in self.cerrado:
                    self.abierto.put((self.calcular_prioridad(nuevo_estado, coste + 1), nuevo_estado, coste + 1))
                    self.todos[nuevo_estado] = self.estado_actual
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
            self.laberinto[estado[1][1]] = self.laberinto[estado[1][1]][:estado[1][0]] + '#' + self.laberinto[estado[1][1]][estado[1][0] + 1:]

        return False

    def imprime_laberinto(self):
        for row in self.laberinto:
            print(row)


def print_laberinto(l):
    for row in l:
        print(row)


sol = A_Star(laberinto)

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
        system('clear')
