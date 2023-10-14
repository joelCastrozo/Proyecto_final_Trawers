from cmu_graphics import *

def crearVentanas(x,y):
    ventanas = Group(
        Rect(x+10,y+15,15,15, relleno='grisClaro',borde='negro'),
        Rect(x+35,y+15,15,15, relleno='grisClaro',borde='negro'),
        Rect(x+10,y+40,15,15, relleno='grisClaro',borde='negro'),
        Rect(x+35,y+40,15,15, relleno='grisClaro',borde='negro'),
        Rect(x+10,y+65,15,15, relleno='grisClaro',borde='negro'),
        Rect(x+35,y+65,15,15, relleno='grisClaro',borde='negro')
    )
    return ventanas

def dibujarEdificioAlto(x,y,color,colorBorde):
    edificio = Grupo(
        Rect(x,y,60,150, relleno=color),
        Rect(x+15,y+105,30,45,relleno='gainsboro',borde=colorBorde)
    )
    crearVentanas(x,y)
    return edificio

edificio_1 = dibujarEdificioAlto(20,110,'azulOscuro','grisTurbio')
edificio_2 = dibujarEdificioAlto(180,110,'caquiOscuro','rojoOscuro')
edificio_3 = dibujarEdificioAlto(330,110,'grisPizarraClaro','blanco')

def dibujarEdificioPequeño(x,y,color1,color2,valor):
    edificio_pequeño = Grupo(
        Rect(x,y,55,90, relleno=color1),
        Rect(x+12,y+50,30,40,relleno=color2, borde='negro'),
        Rect(x+8,y+10,40,20, relleno='ruborLavanda'),
        Rótulo(valor,x+28,y+20,tamaño=10,negrito=True)
    )
    return edificio_pequeño

edificio_4 = dibujarEdificioPequeño(100,170,'rojoOscuro','marronCuero','STORE')
edificio_5 = dibujarEdificioPequeño(260,170,'varillaDorada','marron','Shoes')

cmu_graphics.run()