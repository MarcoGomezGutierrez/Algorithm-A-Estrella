## Pathfinding, clase, que se encarga de recibir una matriz, con punto de inicio y fin ##
import pygame
from pygame.locals import *
from Algorithm.Casilla import Casilla

class Pathfinding:
    
    def __init__(self, matrix, startPoint, finalPoint, PANTALLA):
        self.map = matrix
        self.startPoint = startPoint
        self.finalPoint = finalPoint
        self.PANTALLA = PANTALLA
        #self.position = startPoint
        self.openList = list()
        self.closedList = list()
        self.result = list()
        self.finish = False
        
        ## Añadimos el punto inicial a OpenList ##
        self.openList.append(self.map[self.startPoint[0]][self.startPoint[1]])

    def algorithm(self):
        if not self.finish:
            ## Si openList no esta vacia... ##
            if (len(self.openList) > 0) :
                # Guardamos la primera posicion del Array #
                winner = 0
                for index in range(0, len(self.openList), 1):
                    # Si tiene una F más barata se guarda la posicion #
                    if self.openList[index].F < self.openList[winner].F:
                        winner = index
                        
                # Guardamos el ganador #
                # Borramos el ganador de OpenList #
                node = self.openList.pop(winner)
                # Lo metemos en ClosedList #
                self.closedList.append(node)
                
                # Si el nodo es el punto final terminamos #
                if node.x == self.finalPoint[0] and node.y == self.finalPoint[1]:
                    self.getResult()
                    self.finish = True
                # Sino continuamos calculando sus vecinos #
                else:
                    vecinos = self.getVecinos(node)
                    for vecino in vecinos:
                        ## Si no esta en la lista cerrada
                        if not vecino in self.closedList:
                            # Si no esta en la lista abierta, guardamos referencia del padre y calculamos la F #
                            if not vecino in self.openList:
                                vecino.padre = node
                                vecino.heuristica()
                                vecino.G = vecino.calculateG(node)
                                vecino.calculateF()
                                self.openList.append(vecino)
                            else: # Esta en OpenList luego se mira si mejora su G #
                                Gx = node.G + vecino.calculateG(node)
                                if (Gx < vecino.G):
                                    vecino.padre = node
                                    vecino.G = vecino.calculateG(node)
                                    vecino.calculateF()
                                    self.openList.insert(self.openList.index(vecino), vecino)
            else: ## Si se ha vaciado openList directamente no ha encontrado el camino ##
                print("No se ha encontrado solución")
                self.finish = True
        
            
    def getResult(self):
        node = self.closedList[-1]
        self.result.append(node)
        while node.x != self.startPoint[0] and node.y != self.startPoint[1]:
            node = node.padre
            self.result.append(node)
    
    def getVecinos(self, casilla):
        vecinos = list()
        for x in range(casilla.x - 1, casilla.x + 2, 1):
            for y in range(casilla.y - 1, casilla.y + 2, 1):
                ## Recorremos la matriz de vecinos y comprobamos que no sea un obstaculo y que no sea el mismo nodo
                if not self.map[x][y].obstaculo and (self.map[x][y].x != casilla.x or self.map[x][y].y != casilla.y):
                    vecinos.append(self.map[x][y])
        return vecinos
    
    def print(self, node, color):
        pygame.draw.rect(self.PANTALLA, color, (node.x * 10, node.y * 10, 10, 10))
    
        
                    
                    
            
        