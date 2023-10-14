from cmu_graphics import *

import random
app.fondo = gradiente('azulCieloProfundo','azulCieloClaro', inicio='superior')
suelo = Rect(0,260,400,140, relleno=gradiente('gris', 'gainsboro', inicio='inferior'))
sol = Estrella(200,0,100,100, relleno=gradiente('oro', 'amarillo', 'tierra'))

def dibujarArbolesSecos(x,y):
    Polígono(x, y, x+5, y-15, x-5, y-15, x+5, y-30, x, y-40, x-5, y-65, x+5, y-85, x, y-45, x+5, y-50, x+10, y-50, x+5, y-40, x+10, y-10, x+15, y, relleno=gradiente(rgb(180,160,140), 'negro', inicio='inferior'))
def dibujarBrotes(x,y):
    Linea(x,y,x-3,y-10, relleno=gradiente('verde', 'limaVerde', inicio='superior'))
    Linea(x,y,x+3,y-10, relleno=gradiente('verde', 'verdeBosque', inicio='superior'))
    Ovalo(x,y,10,6, relleno='tierra')
    
app.cuentaDeArboles = 0
def crearEscenaDelBosque(estáSembrado, estáArdiendo, estáSeco, estáCreciendo):
    sol.alFrente()
    suelo.relleno = gradiente('verdeBosque', 'verde', inicio='inferior')
    if estáSembrado == True:
        Rect(230,280,40,70, relleno=gradiente('salmonClaro', 'tierra', 'salmonOscuro', inicio='superior'), borde='negro')
        Rect(280,280,40,70, relleno=gradiente('salmonClaro', 'tierra', 'salmonOscuro', inicio='superior'), borde='negro')
        Rect(330,280,40,70, relleno=gradiente('salmonClaro', 'tierra', 'salmonOscuro', inicio='superior'), borde='negro')
        Rect(230,355,140,40, relleno=gradiente('salmonClaro', 'tierra', 'salmonOscuro', inicio='superior'), borde='negro')
        dibujarBrotes(250,290), dibujarBrotes(250,310), dibujarBrotes(250,330), dibujarBrotes(250,370)
        dibujarBrotes(300,290), dibujarBrotes(300,310), dibujarBrotes(300,330), dibujarBrotes(300,370)
        dibujarBrotes(350,290), dibujarBrotes(350,310), dibujarBrotes(350,330), dibujarBrotes(350,370)
        dibujarBrotes(270,380), dibujarBrotes(330,380)
    if estáArdiendo == True:
        suelo.relleno = gradiente('oro', 'naranja', 'rojoNaranja', inicio='inferior')
        sol.relleno=gradiente('oro', 'amarillo', 'amarillo', 'rojo', 'rojo', 'amarillo')
    if estáSeco == True:
        suelo.relleno = gradiente('salmonClaro', 'negro', 'salmonClaro', 'negro', inicio='superior')
        while app.cuentaDeArboles < 99:
            posicion_x_de_arbol = random.randint(10,390)
            posicion_y_de_arbol = random.randint(320,385)
            app.cuentaDeArboles += 1
            dibujarArbolesSecos(posicion_x_de_arbol,posicion_y_de_arbol)
    if estáCreciendo == True:
        pass

    return estáArdiendo if estáArdiendo == True else False 
cenizas = Group()
app.cenizas_totales = 0
probarFuego = crearEscenaDelBosque(False, True, True, False)

def cenizas_en_el_aire():
    if probarFuego == True:
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
    if probarFuego == True:
        cenizas.agregar(cenizas_en_el_aire())
        cenizas.centroY += 5

cmu_graphics.run()