# Heurísticas:

import math

def calcular_euclidea(self, estado):
    dx = abs(self.estado_final[0] - estado[0])
    dy = abs(self.estado_final[1] - estado[1])
    return math.sqrt(dx * dx + dy * dy)

def calcular_chebyshev(self, estado):
    dx = abs(self.estado_final[0] - estado[0])
    dy = abs(self.estado_final[1] - estado[1])
    return max(dx, dy)

def calcular_manhattan(self, estado):
    h_manhattan = abs(self.estado_final[0] - estado[0]) + abs(self.estado_final[1] - estado[1])
    return h_manhattan