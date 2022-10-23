
# Para crear un array de objetos array = {my_obj1, my_obj2}
# Para acceder a los elementos array{1}.propiedad devuelve
# la variable propiedad de my_obj1

classdef casilla

  properties
    x
    y
    F # Suma de G + H
    G # Pasos de una casilla a otra, 10 Horizontales o Verticales y 14 Diagonales
    H # Heuristica (Si vamos de A(esta casilla) a B(pto final), es (A.x - B.x) + (A.y - B.y)
    obstaculo
    padre
  endproperties

  methods
    function obj = casilla(x, y, rgbSum)
      obj.x = x;
      obj.y = y;
      if (rgbSum <= 40)
        obj.obstaculo = true;
      else
        obj.obstaculo = false;
      endif
    endfunction
  endmethods

endclassdef

