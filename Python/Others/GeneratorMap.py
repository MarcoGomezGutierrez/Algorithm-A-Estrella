## Clase para Autogenerar un Mapa ##
from Algorithm.Casilla import Casilla
import random

class GeneratorMap:
    
    def __init__(self, DIMENSIONS, finalPoint):
        self.DIMENSIONS = DIMENSIONS
        self.finalPoint = finalPoint
    
    def createMap1(self):
        print("Mapa resultado en linea recta")
        map = list()
        for col in range(0, self.DIMENSIONS, 1):
            lista = list()
            for row in range(0, self.DIMENSIONS, 1):
                if row == 0 or row == self.DIMENSIONS-1 or col == 0 or col == self.DIMENSIONS-1:
                    lista.append(Casilla(col, row, True, self.finalPoint))
                else:
                    # lista.append(random.randint(0, 1))
                    lista.append(Casilla(col, row, False, self.finalPoint))
            map.append(lista)  
        return map

    ## Diagonales col -1, row + 1
    def createMap2(self):
        print("Mapa resultado con obstaculo en medio")
        map = list()
        for col in range(0, self.DIMENSIONS, 1):
            lista = list()
            for row in range(0, self.DIMENSIONS, 1):
                if row == 0 or row == self.DIMENSIONS-1 or col == 0 or col == self.DIMENSIONS-1:
                    lista.append(Casilla(col, row, True, self.finalPoint))
                else:
                    # lista.append(random.randint(0, 1))
                    lista.append(Casilla(col, row, False, self.finalPoint))
            map.append(lista)
        x = 15
        y = 35
        for i in range(0, 25, 1):
            map[x][y].obstaculo = True
            map[x][y].color = (0, 0, 0)
            x = x + 1
            y = y - 1
        x = 16
        y = 35
        for i in range(0, 25, 1):
            map[x][y].obstaculo = True
            map[x][y].color = (0, 0, 0)
            x = x + 1
            y = y - 1
        x = 15
        y = 36
        for i in range(0, 14, 1):
            map[x][y].obstaculo = True
            map[x][y].color = (0, 0, 0)
            y = y + 1
        return map
    
    def createMap3(self):
        print("Mapa sin resultado")
        map = list()
        for col in range(0, self.DIMENSIONS, 1):
            lista = list()
            for row in range(0, self.DIMENSIONS, 1):
                if row == 0 or row == self.DIMENSIONS-1 or col == 0 or col == self.DIMENSIONS-1:
                    lista.append(Casilla(col, row, True, self.finalPoint))
                else:
                    # lista.append(random.randint(0, 1))
                    lista.append(Casilla(col, row, False, self.finalPoint))
            map.append(lista)
        map[self.finalPoint[0] - 1][self.finalPoint[1] - 1].setObstaculo(True)
        map[self.finalPoint[0]][self.finalPoint[1] - 1].setObstaculo(True)
        map[self.finalPoint[0] - 1][self.finalPoint[1]].setObstaculo(True)
        return map
    
    def createMap4(self):
        print("Mapa aleatorio")
        map = list()
        for col in range(0, self.DIMENSIONS, 1):
            lista = list()
            for row in range(0, self.DIMENSIONS, 1):
                if row == 0 or row == self.DIMENSIONS-1 or col == 0 or col == self.DIMENSIONS-1:
                    lista.append(Casilla(col, row, True, self.finalPoint))
                else:
                    # lista.append(random.randint(0, 1))
                    num = random.randint(0,4)
                    if num == 0:
                        lista.append(Casilla(col, row, True, self.finalPoint))
                    else:
                        lista.append(Casilla(col, row, False, self.finalPoint))
            map.append(lista)  
        return map