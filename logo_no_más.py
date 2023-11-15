from cmu_graphics import *
fotoDeProhibirTalaDeArboles = Grupo(
    Arco(200,200,235,235,140,125, relleno=rgb(103,153,102)),
    Poligono(200,200,280,300,265,300,190,205,130,205,83,210, relleno='blanco'),
    Circulo(200,200,140, relleno=None, borde='rojo', anchuraDeBorde=2),
    Rect(197,187,9,40,rotarAngulo=40,relleno=gradiente('marronCuero', 'marron'), borde='marronCuero', anchuraDeBorde=1),
    Ovalo(189,222,10,5,rotarAngulo=40,relleno=gradiente('salmonClaro', 'salmonClaro', 'marron', 'salmonOscuro', 'salmonOscuro', inicio='superior')),
    Linea(120,100,280,300, relleno='rojo', anchuraDeLinea=12),
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

fotoDeProhibirTalaDeArboles.ancho = 70
fotoDeProhibirTalaDeArboles.altura = 70
fotoDeProhibirTalaDeArboles.centroX = 120
fotoDeProhibirTalaDeArboles.centroY = 130

def modulo_de_logo():
    fotoDeProhibirTalaDeArboles.centroX = 20000

cmu_graphics.run()