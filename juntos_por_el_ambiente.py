# Proyecto final
from cmu_graphics import *
import time
import random

# Portada
# Elementos para todas las escenas
app.fondo = 'azulCieloProfundo'
sol = Estrella(200,0,100,100, relleno=None)
nube1 = Grupo(Circulo(45,45,25, relleno='blanco'),Circulo(80,45,25, relleno='blanco'),Circulo(115,45,25, relleno='blanco'))
nube2 = Grupo(Circulo(245,60,20, relleno='blanco'),Circulo(270,60,20, relleno='blanco'),Circulo(295,60,20, relleno='blanco'))
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
    sol.relleno = gradiente('caqui', 'amarillo', 'oro')
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
def arbolario():
    while app.cuentaDeArbolesVerdes < 99:
        posicion_x_de_arbol_2 = random.randint(20,380)
        posicion_y_de_arbol_2 = random.randint(260,385)
        app.cuentaDeArbolesVerdes += 1
        arbol = crearArboles(posicion_x_de_arbol_2,posicion_y_de_arbol_2)
    return arbol
def crearEscenaDelBosque(estáSembrado, estáArdiendo, estáSeco, estáCrecido):
    sol.alFrente()
    suelo.relleno = gradiente('verdeBosque', 'verde', inicio='inferior')
    carretera.visible = False
    if estáSembrado == True:
        Rect(0,0,400,400, relleno=gradiente('azulCielo', 'azulCielo', 'verde', inicio='superior'))
        sol.alFrente()
        sol.relleno=gradiente('oro','amarillo','caqui')
        nube1.relleno = 'blanco'
        nube2.relleno = 'blanco'
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
        nube1.relleno = 'gris'
        nube2.relleno = 'gris'
        suelo.relleno = gradiente('gris', 'naranja', 'gainsboro', inicio='inferior')
        carretera.relleno = 'grisOscuro'
        sol.relleno=gradiente('naranja', 'naranjaOscuro', 'tomate', 'carmesi')
    if estáSeco == True:
        nube1.relleno = 'grisOscuro'
        nube2.relleno = 'grisOscuro'
        Rect(0,0,400,400, relleno=gradiente('azulCielo', 'azulCielo', 'verde', inicio='superior'))
        sol.alFrente()
        sol.relleno=gradiente('amarillo', 'oro', 'naranja', 'carmesi', 'rojo')
        suelo.relleno = gradiente('salmonClaro', 'negro', 'salmonClaro', 'negro', inicio='superior')
        suelo.alFrente()
        while app.cuentaDeArbolesSecos < 99:
            posicion_x_de_arbol = random.randint(10,390)
            posicion_y_de_arbol = random.randint(320,385)
            app.cuentaDeArbolesSecos += 1
            dibujarArbolesSecos(posicion_x_de_arbol,posicion_y_de_arbol)
    if estáCrecido == True:
        nube1.relleno = 'gainsboro'
        nube1.relleno = 'gainsboro'
        sol.alFrente()
        Rect(0,0,400,400, relleno=gradiente('azulCielo', 'azulCielo', 'verde', inicio='superior'))
        sol.relleno = gradiente('oro', 'amarillo', 'caqui')
        suelo.alFrente()
        suelo.relleno = 'verdeBosque'
        sol.relleno=gradiente('amarillo', 'oro', 'naranja', 'carmesi')
        app.cuentas = 0
        arbol = arbolario()

cenizas = Group()
app.cenizas_totales = 0
app.probarFuego = False
esBosque = False
# Escena 3 - Rio contaminado
app.contadorDeBasuraDeRio = 0

def dibujarBasuraDeRio():
    while app.contadorDeBasuraDeRio < 35:
        app.contadorDeBasuraDeRio += 1
        centroX_de_basuraDeRio, centroY_de_basuraDeRio = random.randint(40,165), random.randint(260,390)
        cantidad = random.randint(3,7)
        desechos = Grupo(
        Estrella(centroX_de_basuraDeRio-9, centroY_de_basuraDeRio+5, 3, cantidad, relleno='verde'),
        Rect(centroX_de_basuraDeRio+18, centroY_de_basuraDeRio-4, 3, 13, relleno='marVerdeOscuro'),
        Ovalo(centroX_de_basuraDeRio+30, centroY_de_basuraDeRio+3, 2, 4, relleno=gradiente('gris', 'verdeOscuro'))
        )
    return desechos

basuraDeRio = Grupo()

def dibujarRio(estáContaminado, estáLimpio):
    Rect(0,0,400,400, relleno = gradiente ('cianClaro','azur', inicio='inferior'))
    rio = Rect(0,250,250,150, relleno=gradiente('azulCieloClaro','azulCieloClaro','azulCieloProfundo','azulGandul','azulReal', inicio='superior'))
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
        basuraDeRio.agregar(dibujarBasuraDeRio())
    if estáLimpio == True:
        cubeta.visible = False
        basuraDeRio.alFondo()
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
        Linea(218,181,240,230,anchuraDeLinea=4, relleno='mocasin'),
        Ovalo(200,200,45,80,relleno='azulMedio'),
        Circulo(200,145,20, relleno='mocasin'),
        Linea(181,181,145,145,anchuraDeLinea=4, relleno='mocasin'))   
    
def dibujarIntegrantes(x,y, color):
    Linea(x,y-15,x,y+95,relleno=color,anchuraDeLinea=40),
    Ovalo(x,y,45,80,relleno=color),
    Circulo(x,y-55,20, relleno="durazno")

def dibujarTienda():
    Rect(0,0,400,400, relleno=gradiente('azulCielo', 'azulCieloClaro'))
    tienda = Grupo(
        Rect(80,92,188,188,relleno='durazno'),
        Rect(70,70,210,25,relleno='durazno',borde='caquiOscuro'),
        Rect(93,103,165,165,relleno='coralClaro',borde='salmon'),
        Rect(132,42,83,43,relleno='coralClaro',borde='salmon'),
        Rotulo('Ecotienda',172,61,tamaño=12,negrito=True,fuente='cinzel',relleno='aguaMarinaMedio'),
        Rect(73,249,203,31,relleno='ladrillo'),Linea(36,273,313,273,anchuraDeLinea=15,relleno='gris'),
        Rect(200,147,50,121,relleno='durazno'),
        Rect(208,156,36,40,relleno='azulAceroClaro',opacidad=90),
        Rect(208,209,36,51,relleno='azulAceroClaro',opacidad=90),
        Rect(100,147,91,83,relleno='azulAceroClaro',opacidad=90),
        Linea(130,147,130,230,relleno='durazno'),
        Linea(160,147,160,230,relleno='durazno'),
        Linea(100,186,192,186,relleno='durazno'),
        Rect(100,147,91,85,relleno=None,borde='Durazno',anchuraDeBorde=5),
        Linea(207,204,218,204 ,relleno='marron'))
    Rect(0,280,400,120, relleno='verde')
    crearArboles(345,285)

macetero = Poligono(220,280,260,240,380,240,340,280, relleno='tierra', borde='granate',anchuraDeBorde=5, visible = False)
semilla = Ovalo(80,240,35,15, relleno='chocolate', visible = False)
arbol = Grupo(Linea(300,200,300,265, relleno='madera',anchuraDeLinea=10), Circulo(297,185,20,relleno='verdeOscuro'),
            Circulo(311,177,20,relleno='verdeOscuro'),Circulo(315,205,10,relleno='verdeOscuro'),Circulo(289,205,10,relleno='verdeOscuro'),
            Circulo(280,182,15,relleno='verdeOscuro'))
arbol.visible = False
agua = Poligono(200,35,190,55,190,60,200,66,210,60,210,55, relleno='agua', visible = False)
def dibujarJuego():
    Rect(0,0,400,400, relleno='azulCielo')
    Rect(0,220,400,200,relleno='verdeBosque')
    nube1.alFrente()
    nube2.alFrente()
    macetero.visible = True
    semilla.visible = True
    agua.visible = True
    Rotulo('Mueva la semilla hacia el macetero', 200, 33)
    Rotulo('Planta una planta en la plantadera para hacer crecer la planta', 200,350)
def enRatónArrastrado(ratónX, ratónY):
    if semilla.contiene(ratónX, ratónY):
        semilla.centroX = ratónX
        semilla.centroY = ratónY
    elif agua.contiene(ratónX, ratónY):
        agua.centroX = ratónX
        agua.centroY = ratónY
    if agua.tocaFigura(arbol):
        if arbol.altura < 160: 
            arbol.inferior -= 4
            arbol.altura += 5
            arbol.ancho += 1
def enRatónSoltado(ratónX, ratónY):
    if semilla.tocaFigura(macetero):
       semilla.visible = False
       arbol.visible = True
    if arbol.visible == True:
       agua.visible = True
    
def enTeclaPresionada(tecla):
    nube1.alFrente()
    nube2.alFrente()
    if tecla == 'a':
        crearEscenaDelBosque(False, True, False, False)
    elif tecla == 'b':
        crearEscenaDelBosque(False, False, False, True)
        sol.alFrente()
    elif tecla == 'c':
        esBosque = True
        if esBosque == True:
            crearEscenaDelBosque(False, False, True, False)
            cenizas.alFrente()
            app.probarFuego = True
    elif tecla == 'd':
        nube1.alFondo()
        nube2.alFondo()
        dibujarRio(True, False)
    elif tecla == 'e':
        dibujarReunion()
        dibujarIntegrantes(80, 340, 'indigo')
        dibujarIntegrantes(140, 340, 'limaVerde')
        dibujarIntegrantes(180, 340, 'fucsia')
        dibujarIntegrantes(240, 340, 'oro')
        dibujarIntegrantes(280, 340, 'caquiOscuro')
        dibujarIntegrantes(340, 340, 'granate')
    elif tecla == 'f':
        crearEscenaDelBosque(True, False, False, False)
    elif tecla == 'g':
        dibujarRio(False, True)
    elif tecla == 'h':
        dibujarTienda()
    elif tecla == 'i':
        dibujarJuego()

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
    # Escena final
    nube1.centroX += 3
    nube2.centroX -= 3
    if nube1.centroX > 450:
        nube1.centroX = -20
    if nube2.centroX < -20:
        nube2.centroX = 450
    
titulo = Rotulo('Comprende los problemas que nos destruyen', 200,190, relleno='rojo', tamaño=16, anchuraDeBorde=6)
subtitulo = Rotulo('nuestro planeta', 200,210, relleno='rojo', tamaño=16, anchuraDeBorde=6)
indicacion = Rotulo('Presiona teclas en orden alfabetico de la a hasta la i', 200,380, relleno='negro', tamaño=16, anchuraDeBorde=4)


"""Tenemos serios problemas de creatividad, pero está bien, somos insanos"""

cmu_graphics.run()