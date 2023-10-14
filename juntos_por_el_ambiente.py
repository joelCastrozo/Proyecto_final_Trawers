# Proyecto final
from cmu_graphics import *
import time
import random

# Portada
# Elementos para todas las escenas
app.fondo = 'azulCieloProfundo'
sol = Estrella(200,0,100,100, relleno=None)
suelo = Rect(0,260,400,140, relleno='azulCieloProfundo')
time.sleep(3)
# Escena 01 - La ciudad, principal medio de destrucción
carretera = Rect(-20,320,440,80, relleno='grisOscuro', borde='gris', anchuraDeBorde=5)
división_de_carretera = Linea(0,360,410,360, relleno=gradiente('negro', 'grisOscuro', 'negro'), anchuraDeLinea=4, guion=(5,6))
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

def dibujarEdificioPequeño(x,y,color1,color2,valor):
    edificio_pequeño = Grupo(
        Rect(x,y,55,90, relleno=color1),
        Rect(x+12,y+50,30,40,relleno=color2, borde='negro'),
        Rect(x+8,y+10,40,20, relleno='ruborLavanda'),
        Rótulo(valor,x+28,y+20,tamaño=10,negrito=True)
    )
    return edificio_pequeño
    
def crearAutos(color, partida, direccion):
    base = Rect(partida, direccion-30, 70, 30, relleno=color)
    capo = Rect(partida+10, direccion-50, 50, 20, relleno=color)
    ruedaIzq = Círculo(partida+15, direccion, 10)
    ruedaDer = Círculo(partida+55, direccion, 10)
    carro = Grupo(capo, base, ruedaIzq, ruedaDer)
    return carro

app.contadorDeBasura = 0
def dibujarBasura():
    while app.contadorDeBasura < 35:
        app.contadorDeBasura += 1
        centroX_de_basura, centroY_de_basura = random.randint(40,360), random.randint(270,310)
        cantidad = random.randint(3,7)
        Estrella(centroX_de_basura-9, centroY_de_basura+5, 3, cantidad, relleno='marron')
        Rect(centroX_de_basura+18, centroY_de_basura-4, 3, 13, relleno='azulClaro')
        Ovalo(centroX_de_basura+30, centroY_de_basura+3, 2, 4, relleno=gradiente('gris', 'blanco'))

def dibujarEscenaDeCiudad():
    app.fondo = gradiente('azulCieloProfundo','azulCieloClaro', inicio='superior')
    sol.relleno = gradiente('oro', 'amarillo', 'caqui')
    edificio_1 = dibujarEdificioAlto(20,110,'azulOscuro','grisTurbio')
    edificio_2 = dibujarEdificioAlto(180,110,'caquiOscuro','rojoOscuro')
    edificio_3 = dibujarEdificioAlto(330,110,'grisPizarraClaro','blanco')
    edificio_4 = dibujarEdificioPequeño(100,170,'rojoOscuro','marronCuero','STORE')
    edificio_5 = dibujarEdificioPequeño(260,170,'varillaDorada','marron','Shoes')
    suelo.relleno = gradiente('gris', 'gainsboro', inicio='inferior')
    carretera.alFrente()
    división_de_carretera.alFrente()
    dibujarBasura()

dibujarEscenaDeCiudad()

carro_1 = crearAutos(gradiente('azulReal', 'azulGandul', inicio='inferior'), 440, 320)
carro_2 = crearAutos(gradiente('violetaRojoMedio', 'violeta', inicio='inferior'), 540, 320)
carro_3 = crearAutos(gradiente('grisOscuro', 'grisClaro', inicio='inferior'), 690, 320)
carro_4 = crearAutos(gradiente('verde', 'limaVerde', inicio='inferior'), -40, 360)
carro_5 = crearAutos(gradiente('rojo', 'carmesi', inicio='inferior'), -240, 360)
carro_6 = crearAutos(gradiente('naranja', 'oro', inicio='inferior'), -440, 360)
# Escena 2 - Los bosques, el problema del mal oxigeno
def dibujarArbolesSecos(x,y):
    Polígono(x, y, x+5, y-15, x-5, y-15, x+5, y-30, x, y-40, x-5, y-65, x+5, y-85, x, y-45, x+5, y-50, x+10, y-50, x+5, y-40, x+10, y-10, x+15, y, relleno=gradiente(rgb(180,160,140), 'negro', inicio='inferior'))
def dibujarBrotes(x,y):
    Linea(x,y,x-3,y-10, relleno=gradiente('verde', 'limaVerde', inicio='superior'))
    Linea(x,y,x+3,y-10, relleno=gradiente('verde', 'verdeBosque', inicio='superior'))
    Ovalo(x,y,10,6, relleno='tierra')
    
app.cuentaDeArbolesSecos = 0
app.cuentaDeArbolesVerdes = 0
def crearArboles(x, y):
    Árbol = Group(
            Circle (x+5,y-43,15, relleno='verde'),
            Circle (x+30,y-43,15, relleno='verde'),
            Circle (x+20,y+19,15, relleno='verde'),
            Circle (x+7,y+19,15, relleno='verde'),
            Circle (x-23,y,25, relleno=gradiente('verde', 'limaVerde', inicio='izquierda')),
            Circle (x-23,y,25, relleno=gradiente('verde', 'limaVerde', inicio='derecha')),
            Rect (x-8,y+7,16,80, relleno=gradiente('tierra','granate', inicio='superior')),
            Óvalo(x,y+85,15,10, relleno='granate'),
            Circle (x,y+7,25, relleno='verdeBosque')
    )

def crearEscenaDelBosque(estáSembrado, estáArdiendo, estáSeco, estáCrecido):
    sol.alFrente()
    suelo.relleno = gradiente('verdeBosque', 'verde', inicio='inferior')
    carretera.visible = False
    if estáSembrado == True:
        Rect(0,0,400,400, relleno=gradiente('azulCielo', 'azulCielo', 'verde', inicio='superior'))
        sol.alFrente()
        suelo.alFrente()
        Rect(230,280,40,70, relleno=gradiente('salmonClaro', 'tierra', 'salmonOscuro', inicio='superior'), borde='negro')
        Rect(280,280,40,70, relleno=gradiente('salmonClaro', 'tierra', 'salmonOscuro', inicio='superior'), borde='negro')
        Rect(330,280,40,70, relleno=gradiente('salmonClaro', 'tierra', 'salmonOscuro', inicio='superior'), borde='negro')
        Rect(230,355,140,40, relleno=gradiente('salmonClaro', 'tierra', 'salmonOscuro', inicio='superior'), borde='negro')
        dibujarBrotes(250,290), dibujarBrotes(250,310), dibujarBrotes(250,330), dibujarBrotes(250,370)
        dibujarBrotes(300,290), dibujarBrotes(300,310), dibujarBrotes(300,330), dibujarBrotes(300,370)
        dibujarBrotes(350,290), dibujarBrotes(350,310), dibujarBrotes(350,330), dibujarBrotes(350,370)
        dibujarBrotes(270,380), dibujarBrotes(330,380)
    if estáArdiendo == True:
        suelo.relleno = gradiente('gris', 'naranja', 'gainsboro', inicio='inferior')
        carretera.relleno = 'grisOscuro'
        sol.relleno=gradiente('oro', 'amarillo', 'amarillo', 'rojo', 'rojo', 'amarillo')
    if estáSeco == True:
        Rect(0,0,400,400, relleno=gradiente('azulCielo', 'azulCielo', 'verde', inicio='superior'))
        sol.alFrente()
        suelo.relleno = gradiente('salmonClaro', 'negro', 'salmonClaro', 'negro', inicio='superior')
        suelo.alFrente()
        while app.cuentaDeArbolesSecos < 99:
            posicion_x_de_arbol = random.randint(10,390)
            posicion_y_de_arbol = random.randint(320,385)
            app.cuentaDeArbolesSecos += 1
            dibujarArbolesSecos(posicion_x_de_arbol,posicion_y_de_arbol)
    if estáCrecido == True:
        sol.alFrente()
        Rect(0,0,400,400, relleno=gradiente('azulCielo', 'azulCielo', 'verde', inicio='superior'))
        sol.relleno = gradiente('oro', 'amarillo', 'caqui')
        suelo.alFrente()
        suelo.relleno = 'verdeBosque'
        sol.relleno=gradiente('oro', 'amarillo', 'amarillo', 'rojo', 'rojo', 'amarillo')
        app.cuentas = 0
        while app.cuentaDeArbolesVerdes < 99:
            posicion_x_de_arbol_2 = random.randint(20,380)
            posicion_y_de_arbol_2 = random.randint(260,385)
            app.cuentaDeArbolesVerdes += 1
            crearArboles(posicion_x_de_arbol_2,posicion_y_de_arbol_2)

cenizas = Group()
app.cenizas_totales = 0
app.probarFuego = False
esBosque = False
# Escena 3 - Rio contaminado
fotoDePezMuerto = Grupo(
        Rect(0,0,400,400, relleno=gradiente('grisTurbio','azulMediaNoche','grisTurbio', inicio='derecha')),
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
        Linea (236,149,199,186), Linea (151,199,190,193),
        Linea (173,177,171,211), Linea (207,177,211,192)
        )   
fotoDePezMuerto.visible = False
def dibujarRio(estáContaminado, estáLimpio):
    Rect(0,0,400,400, relleno = gradiente ('cianClaro','azur', inicio='inferior'))
    Rect(0,250,250,150, relleno=gradiente('azulCieloClaro','azulCieloClaro','azulCieloProfundo','azulGandul','azulReal', inicio='superior'))
    Poligono(165,400, 210,384, 226,371, 205,357, 185,337, 228,314, 209,300, 198,276, 203,262, 189,248, 201,229, 224,225, 289,231, 351,236,
    400,250, 400, 400, relleno=gradiente('limaVerde','verdeBosque','verde','marVerde', inicio='izquierda-superior'))
    Rect(240,100,20,20, relleno=gradiente('durazno', 'mocasin', inicio='izquierda'))
    Circulo(250,60,50, relleno=gradiente('durazno', 'mocasin', inicio='izquierda'))
    Óvalo(250,70,30,20)
    Óvalo(250,65,30,20, relleno=gradiente('durazno', 'mocasin', inicio='izquierda'))
    Óvalo(250,150,50,80, relleno='limaVerde')
    Rect(225,150,50,50, relleno='limaVerde')
    Rect(225,200,20,40, relleno='rojoOscuro')
    Rect(250,200,20,40, relleno='rojoOscuro')
    Óvalo(233,243,30,10)
    Óvalo(260,243,30,10)

    cubeta = Grupo(Óvalo(187,190,30,50, relleno='plateado', borde='gris'),
    Rect(185,165,80,50, relleno=gradiente('plateado', 'grisOscuro', 'gris', inicio='izquierda')),
    Óvalo(260,190,30,50, relleno='gris'))

    Poligono(275,150, 298,162, 260,190, 283,164,273,159, relleno=gradiente('durazno', 'mocasin', inicio='derecha'))
    Poligono(225,150, 185,165, 225,159, relleno=gradiente('durazno', 'mocasin', inicio='derecha'))
    Poligono(186,392, 185,337, 205,357, 226,371, 210,384, relleno=gradiente('naranjaMarron','tierra', inicio='superior'))
    Poligono(203,328, 198,276, 209,300, 228,314, relleno=gradiente('naranjaMarron','tierra', inicio='superior'))

    if estáContaminado == True:
        fotoDePezMuerto.ancho, fotoDePezMuerto.altura = 100, 100
        fotoDePezMuerto.izquierda, fotoDePezMuerto.superior, fotoDePezMuerto.rotarAngulo = 90, 275, 5
        fotoDePezMuerto.alFrente()
        fotoDePezMuerto.visible = True
    if estáLimpio == True:
        cubeta.visible = False
        
# Escena 4 - Soluciones
def dibujarReunion():
    Rect(0,0,400,400, relleno=gradiente('blanco', 'gris', 'blanco'))
    suelo.alFrente()
    suelo.relleno = gradiente('blanco', 'nieve')
    
    tablero = Rect(60,60,280,140,relleno='blancoFantasma',borde='plateado',anchuraDeBorde=5)
    Rotulo('¿Como evitar estos problemas?',200,80, tamaño=12)

    fotoDeProhibirTalaDeArboles = Grupo(
    Arco(200,200,235,235,140,125, relleno=rgb(103,153,102)),
    Poligono(200,200,280,300,265,300,190,205,130,205,83,210, relleno='blanco'),
    Circulo(200,200,140, relleno=None, borde='rojo', anchuraDeBorde=3),
    Rect(197,187,9,40,rotarAngulo=40,relleno=gradiente('marronCuero', 'marron'), borde='marronCuero', anchuraDeBorde=1),
    Ovalo(189,222,10,5,rotarAngulo=40,relleno=gradiente('salmonClaro', 'salmonClaro', 'marron', 'salmonOscuro', 'salmonOscuro', inicio='superior')),
    Linea(120,100,280,300, relleno='rojo', anchuraDeLinea=10),
    Rect(103,195,8,20, relleno=gradiente('marronCuero', 'marron'), borde='marronCuero', anchuraDeBorde=1),
    Rect(151,193,8,20, relleno=gradiente('marronCuero', 'marron'), borde='marronCuero', anchuraDeBorde=1),
    Rect(126,217,10,22,relleno=gradiente('marronCuero', 'marron'), borde='marronCuero', anchuraDeBorde=1),
    Rect(175,235,10,29,relleno=gradiente('marronCuero', 'marron'), rotarAngulo=3,borde='marronCuero', anchuraDeBorde=1),
    Ovalo(131,217,10,3,relleno=gradiente('salmonClaro', 'salmonClaro', 'marron', 'salmonOscuro', 'salmonOscuro', inicio='superior')),
    Ovalo(181,235,12,3,relleno=gradiente('salmonClaro', 'salmonClaro', 'marron', 'salmonOscuro', 'salmonOscuro', inicio='superior')),
    Ovalo(131,239,10,3,relleno=gradiente('marronCuero', 'marron'), borde='marronCuero', anchuraDeBorde=1),
    Ovalo(179,265,10,3,relleno=gradiente('marronCuero', 'marron'), borde='marronCuero', anchuraDeBorde=1),
    Poligono(316,60,236,109,294,160, relleno='verdeBosque'),
    Poligono(284,110,213,144,260,190, relleno='verdeBosque'),
    Poligono(245,153,233,214,190,175, relleno='verdeBosque')
    )

    fotoDeProhibirTalaDeArboles.ancho, fotoDeProhibirTalaDeArboles.altura = 60, 60
    fotoDeProhibirTalaDeArboles.izquierda, fotoDeProhibirTalaDeArboles.superior, fotoDeProhibirTalaDeArboles.rotarAngulo = 240, 110, -15

    Lider = Grupo(
        Linea(200,180,200,240,anchuraDeLinea=40,relleno='azulMedio'),
        Linea(218,181,240,230,anchuraDeLinea=4),
        Ovalo(200,200,45,80,relleno='azulMedio'),
        Circulo(200,145,20),
        Linea(181,181,145,145,anchuraDeLinea=4))   
    
def dibujarIntegrantes(x,y, color):
    Linea(x,y-15,x,y+95,relleno=color,anchuraDeLinea=40),
    Ovalo(x,y,45,80,relleno=color),
    Circulo(x,y-55,20)

def enTeclaPresionada(tecla):
    if tecla == 'espacio':
        crearEscenaDelBosque(False, True, False, False)
    elif tecla == 'a':
        crearEscenaDelBosque(False, False, False, True)
        sol.alFrente()
    elif tecla == 'b':
        esBosque = True
        if esBosque == True:
            crearEscenaDelBosque(False, False, True, False)
            cenizas.alFrente()
            app.probarFuego = True
    elif tecla == 'c':
        dibujarRio(True, False)
    elif tecla == 'd':
        dibujarReunion()
        dibujarIntegrantes(80, 340, 'indigo')
        dibujarIntegrantes(140, 340, 'limaVerde')
        dibujarIntegrantes(180, 340, 'fucsia')
        dibujarIntegrantes(240, 340, 'oro')
        dibujarIntegrantes(280, 340, 'caquiOscuro')
        dibujarIntegrantes(340, 340, 'granate')
    elif tecla == 'e':
        crearEscenaDelBosque(True, False, False, False)
    elif tecla == 'f':
        dibujarRio(False, True)
    elif tecla == 'g':
        pass

def cenizas_en_el_aire():
    if app.probarFuego == True:
        while True:
            posicion_x_de_cenizas = random.randint(0,400)
            posicion_y_de_cenizas = random.randint(0,400)
            ceniza = Circulo(posicion_x_de_cenizas, posicion_y_de_cenizas, 2, relleno='gris')
            app.cenizas_totales += 1
            print(app.cenizas_totales)
            if app.cenizas_totales > 100:
                cenizas.clear()
                app.cenizas_totales = 0
                print(app.cenizas_totales)
            return ceniza

def enPaso():
    sol.puntos += 1
    # Escena 1
    if esBosque == False:
        carro_1.centroX -= 10
        if carro_1.centroX == -600:
            carro_1.centroX = 440
        carro_2.centroX -= 7
        if carro_2.centroX == -600:
            carro_2.centroX = 540
        carro_3.centroX -= 5
        if carro_3.centroX == -600:
            carro_3.centroX = 690
        carro_4.centroX += 10
        if carro_4.centroX == 600:
            carro_4.centroX = -40
        carro_5.centroX += 7
        if carro_5.centroX == 600:
            carro_5.centroX = -240
        carro_6.centroX += 5
        if carro_6.centroX == 600:
            carro_6.centroX = -440
    # Escena 2
    if app.probarFuego == True:
        cenizas.agregar(cenizas_en_el_aire())
        cenizas.centroY += 5
    
titulo = Rotulo('Comprende los problemas que nos destruyen', 200,90, relleno='negro', tamaño=16, anchuraDeBorde=4)
titulo = Rotulo('nuestro planeta', 200,210, relleno='negro', tamaño=16, anchuraDeBorde=4)

cmu_graphics.run()