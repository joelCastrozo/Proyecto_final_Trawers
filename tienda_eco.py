from cmu_graphics import *
tienda_q = Grupo()

def tienda():
    tienda_q.agregar(Oval(200,265,340,20, relleno='gris', opacidad=40),
    Polygon(50,260,50,60,200,45,350,60,350,260, relleno=gradient('azulCielo', 'azulOscuro', inicio='inferior-izquierda'), borde='negro'))
    for i in range(12):
        tienda_q.agregar(Rect(52, 60 + 17 * i, 296, 4, relleno='azulClaro', anchuraDeBorde=0.3))
    tienda_q.agregar(Polygon(40,70,35,60,40,50,200,25,360,50,370,60,360,70,200,50, relleno=gradient('gris', 'grisOscuro', 'azulCadete', 'azulPizarra', inicio='inferior'), borde='negro'),    Rect(200-75,160,150,100, relleno='gris', borde='negro'),
    Rect(200-60,100,120,40, relleno='grisTurbio', borde='negro'),
    Label('WAREHOUSE',200,120, tamaño=14, relleno='azulMedianoche', negrito=True),
    Line(40,262,360,262, relleno='gris', anchuraDeLínea=4))
    for i in range(2):
        tienda_q.agregar(Circle(147+106*i, 110, 2, relleno='azulMedianoche'), Circle(147+106*i, 110+20*i, 2, relleno='azulMedianoche'),
        Circle(147+106*i, 130, 2, relleno='azulMedianoche'))
    tienda_q.agregar(Rect(155,160,60,100, relleno='grisOscuro'))
    for i in range(4):
        tienda_q.agregar(Rect(125, 160 + 9 * i, 150, 9, relleno=rgb(119 + 10 * i, 136 + 4 * i, 153 + 6 * i), borde='negro', anchuraDeBorde=0.3))
    for i in range(3):
        tienda_q.agregar(Rect(127+ 40 * i, 220, 40, 40, relleno='caqui', borde='negro', anchuraDeBorde=0.3),
        Rect(143+40*i,220,10,15, relleno='rojo', borde='negro', anchuraDeBorde=0.2),
        Rect(133+40*i,240,7,2, relleno='marron'),
        Rect(133+40*i,245,30,2, relleno='marron'),
        Rect(133+40*i,250,15,2, relleno='marron'))

def eliminar_tienda():
    tienda_q.centroX = 90000

cmu_graphics.run()