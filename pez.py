from cmu_graphics import *

# Pez muerto
fotoDePezMuerto = Grupo(
    Ovalo(90,210,200,150,relleno=gradiente('gris','grisTurbio', inicio='izquierda')),
    Ovalo(120,150,160,190,relleno=gradiente('gris','grisTurbio', inicio='inferior')),
    Ovalo(230,160,150,150,relleno=gradiente('gris','grisTurbio', inicio='inferior')),
    Ovalo(300,210,150,110,relleno=gradiente('gris','grisTurbio', inicio='izquierda')),

    Poligono(122,193, 143,172, 168,157, 200,146, 236,149, 240,165, 245,191, 
    246,214, 245,233, 221,238, 200,240, 179,232, 158,222, 137,208, 123,194, relleno=gradiente('plateado','azulAceroClaro', inicio='superior'), borde='negro'),
    Poligono (106,216, 122,193, 137,208, 158,222, 179,232,200,240,
    176,238, 151,234, 127,225, 106,216, relleno='azulAceroClaro', borde='negro'),

    Ovalo(120,270,160,110,relleno=gradiente('gris','grisTurbio', inicio='superior')),
    Ovalo(230,280,165,110,relleno=gradiente('gris','grisTurbio', inicio='superior')),

    Poligono(199,186,214,170,221,193,220,200,210,205,204,202,199,186, relleno='coralClaro'),
    Linea (236,149,199,186),
    Linea (151,199,190,193),
    Linea (173,177,171,211),
    Linea (207,177,211,192))
   
fotoDePezMuerto.centroX = 55
fotoDePezMuerto.centroY = 365
fotoDePezMuerto.ancho = 50
fotoDePezMuerto.altura = 50

def vaciar():
    fotoDePezMuerto.vaciar()
cmu_graphics.run()