import pygame
import sys
from pygame.locals import *
from Algorithm.Pathfinding import Pathfinding
from Algorithm.Casilla import Casilla
from Others.GeneratorMap import GeneratorMap
from Others.Interval import setInterval

pygame.init()


dimensions = 100
STEPS = 10
columnas = dimensions * STEPS
filas = dimensions * STEPS

FPS = 50

startPoint = [1 , 1]
finalPoint = [dimensions - 2, dimensions - 2]

## Generador de Mapas ##
generatorMap = GeneratorMap(dimensions, finalPoint)

## Mapa 1 con resultado sin obstaculo ##             
# map = generatorMap.createMap1()

## Mapa 2 con resultado con obstaculo ##
# map = generatorMap.createMap2()

## Mapa 3 sin resultado ##
# FPS = 500
# map = generatorMap.createMap3()

## Mapa 4 aleatorio ##
# map = generatorMap.createMap4()

## Mapa 5 con obstaculos con solucion ##
# map = generatorMap.createMap5()

## Mapa 6 imagen ##
map = generatorMap.createMap6()
columnas = generatorMap.column
filas = generatorMap.row

## Paleta de colores ##
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PINK = (255, 0, 128)


## Pantalla con sus dimensiones ##
PANTALLA = pygame.display.set_mode((columnas, filas))
## Nombre de la pantalla ##
pygame.display.set_caption('Algoritmo A*')


## Pintar de un solo color la pantalla
## PANTALLA.fill(BLANCO)

## DIBUJAR MATRIZ EN EL TABLERO ##
for list in map:
    for casilla in list:
        pygame.draw.rect(PANTALLA, casilla.color, (casilla.x * 10, casilla.y * 10, STEPS, STEPS))


## Posicion Inicial y Final del Algoritmo y pintarlas en rosa ##
pygame.draw.rect(PANTALLA, PINK, (startPoint[0] * 10, startPoint[1] * 10, STEPS, STEPS))          
pygame.draw.rect(PANTALLA, PINK, (finalPoint[0] * 10, finalPoint[1] * 10, STEPS, STEPS))

pathfanding = Pathfinding(map, startPoint, finalPoint, PANTALLA)

# Pintar el resultado del mapa ##
def printResult():
    for node in pathfanding.result:
        pygame.draw.rect(PANTALLA, BLUE, (node.x * 10, node.y * 10, STEPS, STEPS))


## Parametros para pintar un Rect: ventana donde se va a mostrar, color, (x, y, width, height)
# for col in range(0, columnas, STEPS):
#     for row in range(0, filas, STEPS):
#         pygame.draw.rect(PANTALLA, NEGRO, (col, row, STEPS, STEPS))

def app():
    pathfanding.algorithm()
    printOpenAndClosedList()
    if pathfanding.finish:
        interval.cancel()
        printResult()

def printOpenAndClosedList():
    for node in pathfanding.openList:
        pygame.draw.rect(PANTALLA, GREEN, (node.x * STEPS, node.y * STEPS, STEPS, STEPS))
    for node in pathfanding.closedList:
        pygame.draw.rect(PANTALLA, RED, (node.x * STEPS, node.y * STEPS, STEPS, STEPS))
        
interval = setInterval(1/FPS, app)

## Funcion para pintar constantemente la ventana ##
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            interval.cancel()
            pygame.quit()
            sys.exit()
    pygame.display.update()

