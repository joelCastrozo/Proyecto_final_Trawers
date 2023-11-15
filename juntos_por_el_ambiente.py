# Proyecto final
from cmu_graphics import *
def papeles(x,y):
    papel = Group(Poligono(x,y,x-20,y+20,x-40,y+40,x-40,y+60,x-35,y+60,x-20,y+80,x,y+80,x+20,y+70,x+40,y+40,x+40,y+10, relleno='marfil',borde='negro'),
        Poligono(x+35,y+60,x+10,y+60,x,y+45,x+10,y+40,x+35,y+50, relleno='marfil',borde='negro'), Línea(x-20,y+20,x,y+30),
        Poligono(x-20,y+80,x+5,y+30,x-5,y+40,x-35,y+60, relleno='marfil', borde='negro'),Línea(x,y+30,x+10,y+25))

def enRatonPresionado(ratónX, ratónY):
    papeles(ratónX, ratónY)
cmu_graphics.run()