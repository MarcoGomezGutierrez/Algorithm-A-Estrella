### Esto es la clase del Algoritmo ###

class Casilla:
    def __init__(self, x, y, obst, finalPoint):
        self.x = x
        self.y = y
        
        self.F = 0 ## Suma de G + H ##
        self.G = 0 ## Pasos de una casilla a otra, 10 Horizontales o Verticales y 14 Diagonales ##
        self.H = 0 ## Heuristica (Si vamos de A(esta casilla) a B(pto final), es abs(A.x - B.x) + abs(A.y - B.y) ##
        
        self.finalPoint = finalPoint
        
        ## Calculamos que el rgb de la casilla sea menor a 40 para saber si es un obstáculo o no ##
        self.obstaculo = obst
        if obst:
            self.color = (0,0,0)
        else:
            self.color = (255,255,255)
            
        ## Guardar la posicion del padre ##
        self.padre = None
    
    def setObstaculo(self, obstaculo):
        self.obstaculo = obstaculo
        if obstaculo:
            self.color = [0, 0, 0]
        else: 
            self.color = [255, 255, 255]
    
    def heuristica(self):
        x = abs(self.x - self.finalPoint[0])
        y = abs(self.y - self.finalPoint[1])
        
        self.H = (x + y) * 10
        return self.H
    
    def calculateG(self, node):
        if node.x + 1 == self.x and node.y + 1 == self.y:
            return 14
        elif node.x - 1 == self.x and node.y + 1 == self.y:
            return 14
        elif node.x + 1 == self.x and node.y - 1 == self.y:
            return 14
        elif node.x - 1 == self.x and node.y - 1 == self.y:
            return 14
        else:
            return 10
    
    def calculateF(self):
        self.F = self.G + self.H
        return self.F
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
        