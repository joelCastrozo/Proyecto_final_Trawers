from cmu_graphics import *

Poligono(172,302,176,294,186,300,180,309,172,302,relleno='verde',borde='verdeOscuro',visible=True)

Rect(32,323,14,15,relleno='naranja',borde='rojoNaranja',anchuraDeBorde=1,visible=True)
Línea(32,323,47,337,relleno='rojo',visible=True),
Linea(30,337,47,337,relleno='madera',anchuraDeLinea=3,visible=True)

Rect(30,264,13,12,relleno='gris',borde='grisOscuro',visible=True)
Línea(28,275,45,275,relleno='azulReal',anchuraDeLinea=1,visible=True)

cmu_graphics.run()