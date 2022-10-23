clear;clc all;
## Leer la imagen del escenario ##

## FUNCIONES ##
function map = printBordesMapa(map, filas, columnas)
  map(:,1,:) = 0;
  map(1,:,:) = 0;
  map(columnas,:,:) = 0;
  map(:,filas,:) = 0;
endfunction

function map = printPoint(map, x, y, rgb1, rgb2, rgb3)
  map(x, y, 1) = rgb1;
  map(x, y, 2) = rgb2;
  map(x, y, 3) = rgb3;
endfunction

## Añadir al final de la lista una coleccion o objeto ##
function list = append(list, coleccion)
  list{end+1} = coleccion;
endfunction

## Obtener la casilla de la matriz por su posicion ##
function nodo = getCasilla(escenario, posicion)
  nodo = escenario{posicion(1), posicion(2)};
endfunction

## Funcion borrar posicion de una lista ##
function list = delete(list, posicion)
  try ## Si hay más de un elemento borro la posicion ##
    list(posicion) = [];
  catch ## Si solo hay un elemento devuelvo un array vacio ##
    list = {};
  end_try_catch
endfunction

function index = getIndexOf(list, elemento)
  try
    index = 0;
    for i=1:numel(list)
      if (list{i}.x == elemento.x && list{i}.y == elemento.y)
        index = i;
        break
      endif
    endfor
  catch
    index = 0;
    for i=1:numel(list)
      if (list{i}.x == elemento(1) && list{i}.y == elemento(2))
        index = i;
        break
      endif
    endfor
  end_try_catch

endfunction

## Comprobar que dos casillas son las posiciones iguales ##
function cumple = equals(casilla1, casilla2)
  cumple = false;
  type1 = typeinfo(casilla1);
  type2 = typeinfo(casilla2);
  if (type1 == "object" && type2 == "object")
    if (casilla1.x == casilla2.x && casilla1.y == casilla2.y)
      cumple = true;
    endif
  elseif (type1 == "object" && type2 == "matrix")
    if (casilla1.x == casilla2(1) && casilla1.y == casilla2(2))
      cumple = true;
    endif
  elseif (type1 == "matrix" && type2 == "object")
    if (casilla1(1) == casilla2.x && casilla1(1) == casilla2.y)
      cumple = true;
    endif
  elseif (casilla1(1) == casilla2(1) && casilla1(1) == casilla2(2))
    "Casilla1(1)"
    casilla1(1)
    "Casilla2(1)"
    casilla2(1)
    "Casilla1(2)"
    casilla1(2)
    "Casilla2(2)"
    casilla2(2)
    cumple = true;
  endif
endfunction

## Comprobar si una Casilla ya esta dentro de una coleccion ##
function cumple = isInCollection(coleccion, nodo)
  cumple = 0; ## Si la coleccion esta vacia no esta en la coleccion ##
  if numel(coleccion) != 0
    for i=1:numel(coleccion)
      if (equals(coleccion{i},nodo) == 1) ## Si son iguales esta en la coleccion ##
        cumple = 1;
        break
      endif
    endfor
  endif
endfunction

function heuristica = getHeuristica(posicion1, posicion2)
  x = abs(posicion1.x - posicion2(1));
  y = abs(posicion1.y - posicion2(2));
  heuristica = (x + y) * 10;
endfunction

function vecinos = getVecinos(escenario, nodo)
  vecinos = {};
  for x = nodo.x-1:nodo.x+1
    for y = nodo.y-1:nodo.y+1
      obj = escenario{x,y};

      ## Si no es el nodo principal, y su vecino no es un obstaculo ##
      if (obj.obstaculo == 0 && (x != nodo.x || y != nodo.y))
        vecinos = append(vecinos, obj);
      endif
    endfor
  endfor
endfunction

## Devuelve 14 si es una diagonal, si es horizontal devuelve 10 ##
## Nodo (posicion central de la matriz)
## Vecino (es la posicion del vecino para calcular su G,
## si es una diagonal o no)
function G = getG(nodo, vecino)
  if nodo.x + 1 == vecino.x && nodo.y + 1 == vecino.y
    G = 14;
  elseif nodo.x - 1 == vecino.x && nodo.y + 1 == vecino.y
    G = 14;
  elseif nodo.x + 1 == vecino.x && nodo.y - 1 == vecino.y
    G = 14;
  elseif nodo.x - 1 == vecino.x && nodo.y - 1 == vecino.y
    G = 14;
  else
    G = 10;
  endif
endfunction

## ---------- ##

## Guardar la imagen en una matriz ##

## Es muy pero que muy pesada y mi programa tarda más de 1 hora en calcularlo,
## todavía no he tenido paciencia como para que lo termine ##
##map = imread("mapa2.jpg");

## Autogeneracion de Matriz de Pruebas ##
map = [];
for i=1:10
  for y=1:10
    map(i,y,1) = 255;
    map(i,y,2) = 255;
    map(i,y,3) = 255;
  endfor
endfor

y = 3;
x = 6;

for i=1:4
  map(x,y,1) = 0;
  map(x,y,2) = 0;
  map(x,y,3) = 0;
  x = x - 1;
  y = y + 1;
endfor

y = 4;
x = 6;

for i=1:3
  map(x,y,1) = 0;
  map(x,y,2) = 0;
  map(x,y,3) = 0;
  x = x - 1;
  y = y + 1;
endfor
y = 5;
x = 6;
map(x,y,1) = 0;
map(x,y,2) = 0;
map(x,y,3) = 0;

y = 7;
x = 2;
map(x,y,1) = 0;
map(x,y,2) = 0;
map(x,y,3) = 0;

y = 6;
x = 2;
map(x,y,1) = 0;
map(x,y,2) = 0;
map(x,y,3) = 0;

##y = 7;
##x = 8;
##map(x,y,1) = 0;
##map(x,y,2) = 0;
##map(x,y,3) = 0;

y = 8;
x = 8;
map(x,y,1) = 0;
map(x,y,2) = 0;
map(x,y,3) = 0;

##------------------------------------ ##

dimensiones = size(map); %Dimensiones del tablero

columnas = dimensiones(1);
filas = dimensiones(2);


## Pintar borde del mapa ##
map = printBordesMapa(map, filas, columnas);

## Establecer el principio y el fin ##
principio = [2,2];
fin = [dimensiones(1)-1, dimensiones(2)-1];

## Pintar punto de Inicio en Azul ##
map = printPoint(map, principio(1), principio(2), 0, 0, 255);
## Pintar el punto Final en Naranja ##
map = printPoint(map, fin(1), fin(2), 255, 128, 0);

escenario = {}; # Escenario con las Casillas #
openList = {}; # La lista abierta #
closedList = {}; # Lista cerrada #
posicionActual = principio; #Posicion a evaluar de las casillas del tablero

## Copiarme en una matriz con el objeto Casilla todo el mapa ##
for columna=1:dimensiones(1)
  for fila=1:dimensiones(2)
    escenario(columna,fila) = {casilla(
      columna,
      fila,
      sum(map(columna, fila, :))
    )};
  endfor
endfor

## Añadimos a OpenList la posicion actual ##
nodo = getCasilla(escenario, posicionActual);
openList = append(openList, nodo);

##iterador = 0;

## Bucle del algoritmo ##
while equals(nodo, fin) == 0
  ## Saber que indice de openList es el que tiene mejor F
  indexWithLowF = 0;
  F = 0;
  for i=1:numel(openList)
    if (F == 0)
      indexWithLowF = i;
      F = openList{i}.F;
    elseif openList{i}.F < F
      indexWithLowF = i;
      F = openList{i}.F;
    endif
  endfor

  ## Guardamos el ganador
  nodo = openList{indexWithLowF};
  ## Borramos de openList
  openList = delete(openList, indexWithLowF);
  ## Le metemos en closedList
  closedList = append(closedList, nodo);

  posicionActual = [nodo.x, nodo.y];

##  "------------"
##  nodo.x
##  nodo.y

  ## Si el nodo ganador ya es el punto final salimos del bucle ##
  if equals(nodo, fin)
    break
  endif

  ## Calculamos todos los vecinos ##
  vecinos = getVecinos(escenario, nodo);

  ## Obtener las F de los vecinos o mejorarla en caso de menos pasos
  for i=1:numel(vecinos)
    if (equals(vecinos{i}, fin))
      vecinos{i}.padre = [nodo.x, nodo.y];
      openList = append(openList, vecinos{i});
      break
    endif
    ## Si no esta en la lista cerrada y no esta en la lista abierta
    if (isInCollection(closedList, vecinos{i}) == 0)
      if (isInCollection(openList, vecinos{i}) == 0)
        ## Guardo la referencia del padre y calculo su F ##
        vecinos{i}.padre = [nodo.x, nodo.y];
        vecinos{i}.H = getHeuristica(vecinos{i}, fin);
        vecinos{i}.G = nodo.G + getG(nodo, vecinos{i});
        vecinos{i}.F = vecinos{i}.H + vecinos{i}.G;
        openList = append(openList, vecinos{i});
      else
        ## Si esta en openList se comprueba si mejora su G ##
        index = getIndexOf(openList, vecinos{i});
        Gx = nodo.G + getG(nodo, openList{index});
        ## Sí mejora, se recalcula su F y se cambia su padre ##
        if (Gx < vecinos{i}.G)
          openList{index}.padre = [nodo.x, nodo.y];
          openList{index}.G = nodo.G + getG(nodo, openList{index});
          openList{index}.F = openList{index}.H + openList{index}.G;
        endif
      endif
    endif
  endfor

  if (numel(openList) == 0)
    "No se encontro ningun camino"
    break
  endif

endwhile

nodo = closedList{end};
map = printPoint(map, nodo.x, nodo.y, 0, 255, 0);
map = printPoint(map, nodo.padre(1), nodo.padre(2), 0, 255, 0);
while !equals(nodo, principio)
  index = getIndexOf(closedList, nodo.padre);
  nodo = closedList{index};
  map = printPoint(map, nodo.x, nodo.y, 0, 255, 0);
endwhile


## Pintar el escenario ##
imshow(map)
## ----- ##

