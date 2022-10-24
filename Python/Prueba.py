from Algorithm.Casilla import Casilla
from Others.GeneratorMap import GeneratorMap

cas1 = Casilla(1,1,True,[2,2])
cas2 = Casilla(3,3,False,[2,2])

lista =  list()
lista.append(1)
lista.append(6)
lista.append(5)
lista.append(2)
print(lista)
print("El elemento 2 deberia ser 5: ")
print(lista.pop(2))
print(lista[-1])
lista.append(10)
lista.append(60)
lista.append(50)
lista.append(20)
print(lista)

for index in range(0, len(lista), 1):
    print(lista[index])

print("-------------------")

l = list()
l.append(cas1)
l.append(Casilla(2,2,True,[2,2]))
l.append(Casilla(3,3,True,[2,2]))
if cas2 in l:
    print("El elemento esta en la lista")
else:
    print("No esta en la lista")
    
print(l[1].x)
print(l.index(cas2))
l.insert(1, cas1)
cas1.x = 100
print(l[1].x)


print("-------------------")
if (cas1 == cas2): print("Son iguales")
else: print("No son iguales")

generatorMap = GeneratorMap(100, 1, [100-1,100-1])
map = generatorMap.createMap6()

print(len(map))
print(len(map[301]))