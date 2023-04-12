from time import sleep
from os import system

SPEED = 100

#maze = 'maze_small.txt' # Descomentar el seleccionado
maze =  'maze_big.txt'   # Descomentar el seleccionado
with open(maze,'r') as f:
    laberinto = f.read().split('\n')

class Anchura:
    abierto = []
    cerrado = []
    laberinto = None
    estado_inicial  = (None,None)
    estado_actual   = (None,None)
    estado_final    = (None,None)
    operadores = ['arriba','abajo','izquierda','derecha']
    operaciones = {
            'arriba'    : (0,-1),
            'abajo'     : (0, 1),
            'izquierda' : (-1,0),
            'derecha'   : (1 ,0)
        }
    
    def __init__(self,laberinto) -> None:
        self.laberinto = laberinto
        
        self.estado_inicial = self.obtener_indices('e')
        self.estado_actual = self.estado_inicial
        self.estado_final = self.obtener_indices('s')
        if '$' in self.estado_inicial + self.estado_final:
            raise Exception('¡Debe haber una entrada "e" y una salida "s" en el laberinto!')
        
        self.abrir_estado()
        
    def obtener_indices(self,char):
        for idx, row in enumerate(self.laberinto):
            if char in row:
                return self.laberinto[idx].index(char), idx
        return '$','$'
    
    
    def abrir_estado(self):
        for operador in self.operadores:
            x, y = self.operaciones[operador]
            nuevo_estado = (self.estado_actual[0] + x, self.estado_actual[1] + y)
            try:
                if self.laberinto[nuevo_estado[1]][nuevo_estado[0]] != '+' and nuevo_estado not in self.abierto and nuevo_estado not in self.cerrado:
                        self.abierto.append(nuevo_estado)
            except:
                pass


    def comprobar_estado(self):
        try:
            estado = self.abierto.pop(0)
        except:
            print('¡El laberinto introducido no tiene solución!')
            exit()
        self.estado_actual = estado
        self.abrir_estado()
        self.cerrado.append(estado)
        if self.estado_actual == self.estado_final:
            return True
        if self.estado_actual != self.estado_inicial:
            self.laberinto[estado[1]] = self.laberinto[estado[1]][:estado[0]]+'#'+self.laberinto[estado[1]][estado[0]+1:]
        return False
        
        
    def imprime_laberinto(self):
        for row in self.laberinto:
            print(row)


sol = Anchura(laberinto)

while sol.estado_actual != sol.estado_final:
    if sol.comprobar_estado():
        sol.imprime_laberinto()
        break
    sol.imprime_laberinto()
    sleep(1/SPEED)
    system('clear')
