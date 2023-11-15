from cmu_graphics import *
camión = Grupo(
    Poligono(182,160,150,160,130,185,110,195,110,220,107,220,107,230,182,230,relleno='azulAcero'),
    Rect(182,210,88,18,relleno='grisPizarraOscuro'),
    Rect(185,177,106,30,relleno='gris'),
    Linea(285,208,285,220,relleno='grisPizarraOscuro'),
    Linea(205,208,287,208,relleno='grisTurbio',anchuraDeLinea=4),
    Circulo(135,225,15),
    Circulo(135,225,10,relleno='grisTurbio'),
    Circulo(135,225,5,relleno='gris'),
    Circulo(244,225,15),
    Circulo(244,225,10,relleno='grisTurbio'),
    Circulo(244,225,5,relleno='gris'),
    Linea(110,200,110,209,relleno='oro',anchuraDeLinea=3),
    Linea(117,205,123,205,relleno='oro',anchuraDeLinea=3),
    Rect(185,215,20,15,relleno='azulAcero'),
    Rect(155,165,20,25,relleno='azulAceroClaro',opacidad=50),
    Poligono(150,165,135,185,135,190,150,190,relleno='azulAceroClaro',opacidad=50),
    Linea(165,200,173,200,relleno='azulAceroClaro'))

camión.inferior = 355
camión.centroX = 110
camión.ancho -= 10
def modulo_de_camion():
    camión.centroX = 2000

cmu_graphics.run()