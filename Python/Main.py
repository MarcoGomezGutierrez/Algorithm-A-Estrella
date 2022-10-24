import pygame
import sys
from pygame.locals import *
from Algorithm.Pathfinding import Pathfinding
from Algorithm.Casilla import Casilla
from Others.GeneratorMap import GeneratorMap
from Others.Interval import setInterval

pygame.init()


dimensions = 100
steps = 10
columnas = dimensions * steps
filas = dimensions * steps

FPS = 1000

startPoint = [1 , 1]
finalPoint = [columnas / steps - 2, filas / steps - 2]

## Generador de Mapas ##
generatorMap = GeneratorMap(dimensions, steps, finalPoint)

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
steps = 2
generatorMap.steps = steps
map = generatorMap.createMap6()
columnas = generatorMap.column
filas = generatorMap.row
finalPoint = generatorMap.finalPoint

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
        pygame.draw.rect(PANTALLA, casilla.color, (casilla.x * steps, casilla.y * steps, steps, steps))


## Posicion Inicial y Final del Algoritmo y pintarlas en rosa ##
pygame.draw.rect(PANTALLA, PINK, (startPoint[0] * steps, startPoint[1] * steps, steps, steps))          
pygame.draw.rect(PANTALLA, PINK, (finalPoint[0] * steps, finalPoint[1] * steps, steps, steps))

pathfanding = Pathfinding(map, startPoint, finalPoint, PANTALLA)

# Pintar el resultado del mapa ##
def printResult():
    for node in pathfanding.result:
        pygame.draw.rect(PANTALLA, BLUE, (node.x * steps, node.y * steps, steps, steps))


## Parametros para pintar un Rect: ventana donde se va a mostrar, color, (x, y, width, height)
# for col in range(0, columnas, steps):
#     for row in range(0, filas, steps):
#         pygame.draw.rect(PANTALLA, NEGRO, (col, row, steps, steps))

def app():
    pathfanding.algorithm()
    printOpenAndClosedList()
    if pathfanding.finish:
        interval.cancel()
        printResult()

def printOpenAndClosedList():
    for node in pathfanding.openList:
        pygame.draw.rect(PANTALLA, GREEN, (node.x * steps, node.y * steps, steps, steps))
    for node in pathfanding.closedList:
        pygame.draw.rect(PANTALLA, RED, (node.x * steps, node.y * steps, steps, steps))
        
interval = setInterval(1/FPS, app)
# interval = setInterval(0, app)

## Funcion para pintar constantemente la ventana ##
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            interval.cancel()
            pygame.quit()
            sys.exit()
    pygame.display.update()

