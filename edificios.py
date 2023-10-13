def dibujarEdificioAlto(x,y,color,colorBorde):
    Rect(x,y,60,150, relleno=color),
    Rect(x+15,y+105,30,45,relleno='gainsboro',borde=colorBorde)
dibujarEdificioAlto(20,110,'azulOscuro','grisTurbio')
dibujarEdificioAlto(180,110,'caquiOscuro','rojoOscuro')
dibujarEdificioAlto(330,110,'grisPizarraClaro','blanco')

def crearVentanas(x,y):
    Rect(x+10,y+15,15,15, relleno='grisClaro',borde='negro')
    Rect(x+35,y+15,15,15, relleno='grisClaro',borde='negro')
    Rect(x+10,y+40,15,15, relleno='grisClaro',borde='negro')
    Rect(x+35,y+40,15,15, relleno='grisClaro',borde='negro')
    Rect(x+10,y+65,15,15, relleno='grisClaro',borde='negro')
    Rect(x+35,y+65,15,15, relleno='grisClaro',borde='negro')
crearVentanas(20,110)
crearVentanas(180,110)
crearVentanas(330,110)

def dibujarEdificioPequeño(x,y,color1,color2,valor):
    Rect(x,y,55,90, relleno=color1)
    Rect(x+12,y+50,30,40,relleno=color2, borde='negro')
    Rect(x+8,y+10,40,20, relleno='ruborLavanda')
    Rótulo(valor,x+28,y+20,tamaño=10,negrito=True)
dibujarEdificioPequeño(100,170,'rojoOscuro','marronCuero','STORE')
dibujarEdificioPequeño(260,170,'varillaDorada','marron','Shoes')

