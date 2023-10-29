# Proyecto final #
# Librerias que estamos utilizando #
from cmu_graphics import * # Libreria de CMU GRAPHICS
import time # Libreria de tiempo
import random # Libreria de aleatorio

# Propiedades de app para el funcionamiebto del código y de cada escena
## Estado actual de la app, antes de pasar a la primera escena
app.estado = 'en inicio' # Define que la app no está pasado la primera escena
## Fondo de la app, basado en cada escena cambiará el fondo
app.fondo = 'azulCieloProfundo' # El fondo actual de la pantalla inicial

# Elementos de para cada escena, algunos definidos de uno a uno, otros en grupos que se irán llamando de uno en uno por escena
sol = Star(200,0,100,100, relleno = gradient('caqui', 'amarillo', 'oro'), visible = False) # El sol
nube_1 = Group(Circle(45,45,25, relleno='blanco'), Circle(80,45,25, relleno='blanco'), Circle(115,45,25, relleno='blanco')) # Nube grande
nube_2 = Group(Circle(245,60,20, relleno='blanco'), Circle(270,60,20, relleno='blanco'), Circle(295,60,20, relleno='blanco')) # Nube pequeña
nube_1.visible, nube_2.visible = False, False # Modificación para ocultar las nubes en la pantalla del inicio
suelo = Rect(0,260,400,140, relleno='azulCieloProfundo', visible = False) # Suelo de las escenas
río = Polygon()

# Para Escena 0 - Escena de introducción
panelDeTexto = Rect(20,175,360,50, relleno=gradient('plateado', 'grisClaro'), borde='gris', anchuraDeBorde=2) # Fondo del titulo para evitar contraluz
titulo = Label('Comprende los problemas que destruyen', 200,190, relleno='rojo', tamaño=16, anchuraDeBorde=6) # Titulo del proyecto
subtitulo = Label('nuestro planeta y afectan nuestro cuerpo', 200,210, relleno='rojo', tamaño=16, anchuraDeBorde=6) # Subtitulo del proyecto
indicacion = Label('Presiona la tecla derecha para continuar', 200,380, relleno='negro', tamaño=16, anchuraDeBorde=4) # Indicación de uso del proyecto
introducción = Group(panelDeTexto, titulo, subtitulo, indicacion) # Grupo de pantalla de introducción

# Para Escena 1 - Escena de ciudad #
## Funciones para crear edificios ##

### Para crear ventanas para cada edificio ###
ventanas = Group() # Grupo para guardar las ventanas
def crearVentanas(x,y):
    # Agrega las ventanas dibujadas al grupo de ventanas
    ventanas.agregar(Rect(x+10,y+15,15,15, relleno='grisClaro',borde='negro'), Rect(x+35,y+15,15,15, relleno='grisClaro',borde='negro'),
                     Rect(x+10,y+40,15,15, relleno='grisClaro',borde='negro'), Rect(x+35,y+40,15,15, relleno='grisClaro',borde='negro'),
                     Rect(x+10,y+65,15,15, relleno='grisClaro',borde='negro'), Rect(x+35,y+65,15,15, relleno='grisClaro',borde='negro'))
    #return ventanas 

### Para crear un edificio
def dibujarEdificio(x,y,color,colorBorde):
    # Crea un edificio en una coordenada con un color para el relleno y en borde para la puerta
    edificio = Group(Rect(x,y,60,150, relleno=color), Rect(x+15,y+105,30,45,relleno='gainsboro',borde=colorBorde)) # Grupo del edificio
    crearVentanas(x,y) # Dibuja las ventanas del edificio
    return edificio # Retorna el grupo edificio para guardarlo en una variable

### Para crear un local
def dibujarLocal(x,y,color1,color2,valor):
    # Crea un local en una coordenada con dos colores y el nombre de dicho negocio
    local = Group(Rect(x,y,55,90, relleno=color1), Rect(x+12,y+50,30,40,relleno=color2, borde='negro'), Rect(x+8,y+10,40,20, relleno='ruborLavanda'),
                             Label(valor,x+28,y+20,tamaño=10,negrito=True)) # Grupo del local
    return local # Retorna el grupo local para guardarlo en una variable

### Dibujar cada edificios en la escena de ciudad
edificio_1 = dibujarEdificio(20,110,'azulOscuro','grisTurbio') # Edificio de la izquierda
edificio_2 = dibujarEdificio(180,110,'caquiOscuro','rojoOscuro') # Edificio del centro
edificio_3 = dibujarEdificio(330,110,'grisPizarraClaro','blanco') # Edificio de la derecha
edificio_4 = dibujarLocal(100,170,'rojoOscuro','marronCuero','MALL') # Local entre el edificio de la izquierda y el del centro
edificio_5 = dibujarLocal(260,170,'varillaDorada','marron','SHOES') # Local entre el edificio del centro y el de la derecha

### Grupo de canasta de basura
amarradura_de_bolsa = Polygon(133,175,143,166,138,163,132,158,128,159,121,160,118,162,121,171, rotarAngulo=20) # Agarradero de la chuspa de basura
basura = Group(Oval(205,94,100,70,rotarAngulo=-27), Oval(197,109,100,20,rotarAngulo=7), amarradura_de_bolsa,
               Polygon(165,128,175,245,224,245,230,128, relleno=rgb(90,172,70)), Polygon(153,128,161,245,175,245,165,128, relleno=rgb(139,198,64)),
               Polygon(153,128,152,122,247,123,239,245,224,245,230,128, relleno=rgb(58,151,67)), Polygon(148,105,149,123,164,123,164,105, relleno=rgb(139,198,64)),
               Polygon(163,105,164,123,236,123,237,105, relleno=rgb(90,172,70)), Polygon(236,105,249,105,248,123,236,123, relleno=rgb(58,151,67)),
               Rect(270,229,296-267,243-226, relleno='gris'), Rect(271,230,296-269,243-228, relleno='rojo'), Oval(144,229,70,40, relleno='verdeBosque'),
               Oval(144,227,70,36, relleno='verdeClaro'), Oval(144,225,70,32, relleno='rojo'), Circle(144,225,1.4), Circle(134,227,1.4), Circle(124,218,1.4), 
               Circle(137,219,1.4), Circle(161,222,1.4), Circle(155,232,1.4), Circle(171,227,1.4), Circle(115,224,1.4), Circle(150,214,1.4), Circle(124,233,1.4),
               Circle(141,235,1.4)) # Grupo de la canasta de la basura y su basura
amarradura_de_bolsa.centroX, amarradura_de_bolsa.centroY = basura.centroX + 46, 60 # Propiedades modificadas para la agarradera de la chuspa de basura
basura.centroX, basura.centroY, basura.ancho, basura.altura = 280,290,25,25 # Propiedades modificadas para la caneca y la basura

### Grupo basura en la calle
basuraDeCalle = Group() # Grupo para guardar la basura de la calle

### Dibujar basura en la ciudad
def dibujarBasuraEnLaCalle():
    # Crea basura en posiciones aleatorias del suelo y cuenta la cantidad de ellas
    app.contadorDeBasura = 0 # Cuenta de basura
    while app.contadorDeBasura < 50: # Bucle para dibujar la basura
        app.contadorDeBasura += 1 # Suma de 1 para cada basura
        pos_x_de_basura, pos_y_de_basura = random.randint(5,395), random.randint(270,310) # Número aleatorio de coordenada para la basura
        papel = Star(pos_x_de_basura-9, pos_y_de_basura+5, 3, 8, relleno='blanco', borde='negro', guion=True) # Dibujar papeles en el suelo
        botella = Rect(pos_x_de_basura+18, pos_y_de_basura-4, 5, 17, relleno='azulClaro') # Dibujar botellas en el suelo
        basuraDeCalle.agregar(papel, botella) # Agrega cada botella y papel al grupo de basura

### Función para dibujar un carro, con parametros de color, punto de partida y dirección a la que se dirige
def crearAutos(color, partida, direccion):
    # Crea los autos, les da un color, ubica en donde iniciaran su trayectoria y hacia que dirección se moverán
    base = Rect(partida, direccion-30, 70, 30, relleno=color) # Dibuja la parte inferior o soporte del carro
    capo = Rect(partida+10, direccion-50, 50, 20, relleno=color) # Dibuja la parte superior o cubierta del carro
    ruedaIzq = Circle(partida+15, direccion, 10) # Dibuja la llanta izquierda del carro
    ruedaDer = Circle(partida+55, direccion, 10) # Dibuja la llanta derecha del carro
    carro = Group(capo, base, ruedaIzq, ruedaDer) # Grupo con todas las partes del carro
    return carro #  Retorna el carro para guardarlo en una variable

### Crear carros en la escena
carro_1 = crearAutos(gradient('azulReal', 'azulGandul', inicio='inferior'), 440, 340) # Carro en vía alterna hacia el norte
carro_2 = crearAutos(gradient('violetaRojoMedio', 'violeta', inicio='inferior'), 540, 340) # Carro en vía alterna hacia el norte
carro_3 = crearAutos(gradient('grisOscuro', 'grisClaro', inicio='inferior'), 690, 340) # Carro en vía alterna hacia el norte
carro_4 = crearAutos(gradient('verde', 'limaVerde', inicio='inferior'), -40, 380) # Carro en vía alterna hacia el sur
carro_5 = crearAutos(gradient('rojo', 'carmesi', inicio='inferior'), -240, 380) # Carro en vía alterna hacia el sur
carro_6 = crearAutos(gradient('naranja', 'oro', inicio='inferior'), -440, 380) # Carro en vía alterna hacia el sur

## Grupo 1 - Escena de ciudad
### Grupo de la escena de la ciudad con sus elementos respectivos
escenaDeCiudad = Group(edificio_1, edificio_2, edificio_3, edificio_4, edificio_5, ventanas, suelo, basura, basuraDeCalle,
    Rect(-20,320,440,80, relleno='grisOscuro', borde='gris', anchuraDeBorde=5), 
    Line(0,360,410,360, relleno=gradient('negro', 'grisOscuro', 'negro'), anchuraDeLinea=4, guion=(5,6)), carro_1, carro_2, carro_3, carro_4, carro_5, carro_6)

### Propiedad para el grupo de la escena de la ciudad
escenaDeCiudad.visible = False # Oculta la escena

# Para Escena 2 - Bosque verde #
## Funciones de escena de bosque verde

### Grupo de arbóles para dibujar el bosque verde
arbóles = Group() # Group para guardar los arbóles generados

### Función para dibujar un arból
def crearArbóles(x, y, ancho, altura, opacidad, colorDeEstado = 'verdeBosque'):
    # Crea un grupo llamado arból en una posición con un color dependiendo sí se quema o no
    tronco = Polygon(x-10,y+120,x+16,y+120,x+17,y+115,x+13,y+85,x+13,y+7,x+15,y,x,y+16,x-1,y+56,x-3,y+79,x-7,y+104,x-10,y+112, 
                     relleno=gradient('tierra', 'marronCuero',inicio='inferior'))
    hojas = Group(Circle(x-80, y-80, 55, relleno=colorDeEstado, opacidad=opacidad), Circle(x-115,y-115,20, relleno=colorDeEstado, opacidad=opacidad), 
                  Circle(x-50,y-119,20, relleno=colorDeEstado, opacidad=opacidad),
                  Circle(x-61,y-29,15, relleno=colorDeEstado, opacidad=opacidad), 
                  Oval(x-129,y-86,24,30, rotarAngulo=-22,relleno=colorDeEstado, opacidad=opacidad), 
                  Oval(x-141,y-66,25,32, rotarAngulo=-25,relleno=colorDeEstado, opacidad=opacidad), 
                  Oval(x-95,y-129,25,32,relleno=colorDeEstado, opacidad=opacidad),
                  Oval(x-71,y-141,32,34, rotarAngulo=20,relleno=colorDeEstado, opacidad=opacidad), 
                  Oval(x-27,y-97,26,32, rotarAngulo=-75,relleno=colorDeEstado, opacidad=opacidad),
                  Oval(x-22,y-82,14,11, rotarAngulo=-25,relleno=colorDeEstado, opacidad=opacidad),
                  Oval(x-21,y-66,26,32, rotarAngulo=-25,relleno=colorDeEstado, opacidad=opacidad),
                  Oval(x-30,y-47,25,30, rotarAngulo=-25,relleno=colorDeEstado, opacidad=opacidad),
                  Oval(x-40,y-35,25,30, rotarAngulo=-25,relleno=colorDeEstado, opacidad=opacidad),
                  Oval(x-99,y-26,23,30, rotarAngulo=45,relleno=colorDeEstado, opacidad=opacidad),
                  Oval(x-121,y-32,25,31, rotarAngulo=45,relleno=colorDeEstado, opacidad=opacidad),
                  Oval(x-127,y-46,18,16, rotarAngulo=45,relleno=colorDeEstado, opacidad=opacidad),
                  Oval(x-129,y-54,9,15, rotarAngulo=45,relleno=colorDeEstado, opacidad=opacidad),
                  Oval(x-82,y-26,17,19,relleno=colorDeEstado, opacidad=opacidad))
    tronco.centroX, tronco.centroY = hojas.centroX-3, hojas.centroY+78
    arból = Group(tronco, hojas) # Grupo arból donde están el tronco y las hojas
    arból.ancho, arból.altura = ancho, altura
    return arból # Retorna el arból para guardarlo en una variable

### Bucle for para arbóles
for i in range(5): # Da una posición en cuanto a cada paso y crea el árbol
    arból_1 = crearArbóles(115 + i * 82.6, 300, 60, 90, 100) # Llamada a la función crearArbóles para crear el arból grande
    arból_2 = crearArbóles(70 + i * 82.5, 320, 35, 50, 80) # Llamada a la función crearArbóles para crear el arból del medio
    arból_3 = crearArbóles(90 + i * 82, 325, 15, 30, 70) # Llamada a la función crearArbóles para crear el arból pequeño izquierdo
    arból_4 = crearArbóles(135+ i * 82.5, 325, 15, 30, 70) # Llamada a la función crearArbóles para crear el arból derecho
    arbóles.agregar(arból_1, arból_2, arból_3, arból_4) # Agrega los arbóles al grupo de arbóles

## Grupo 2 - Escena de bosque verde
escenaDeBosqueVerde = Group() # Grupo de escena de bosque verde
arbóles.visible = False # Oculta los arbóles creados
escenaDeBosqueVerde.visible = False # Oculta el grupo de bosque verde

# Para Escena 3 - Bosque deteriorandose o quemandose
## Funciones de escena de bosque deteriorandose o quemandose

### Función para cenizas
def cenizas_en_el_aire():
    # Crea las cenizas que deja el bosque al calcinarse
    posicion_x_de_cenizas, posicion_y_de_cenizas  = random.randint(0,400), random.randint(0, 400) # Posición al azar del centroX y centroY de la ceniza
    ceniza = Circle(posicion_x_de_cenizas, posicion_y_de_cenizas, 2, relleno='gris') # La ceniza con sus propiedades
    return ceniza # Retorna la ceniza a un grupo

### Grupo y contador para dibujar cenizas en el aire
cenizas = Group() # Grupo de cenizas

## Grupo 3 - Escena de bosque deteriorandose
escenaDeBosqueQuemandose = Group() # Grupo para bosque incendiado
escenaDeBosqueQuemandose.visible = False # Ocultar bosque incendiado

# Para Escena 4 - Bosque seco, ya muerto
## Funciones de escena de bosque seco

### Grupo para arbóles secos
arboles_secos = Group() # Grupo para guardar cada arból

### Función para crear arbóles secos
def crearArbólSeco(x, y, ancho, altura, opacidad):
    # Crea un arból seco en las posiciones dadas por el usuario, el tamaño dependiendo de el caso y la opacidad para distorsionar
    arból_seco = Polygon(x-5,y+120,x+10,y+120,x+13,y+115,x+10,y+85,x+13,y+7,x+15,y,x+30,y-37,x+42,y-44,x+60,y-50,
        x+60,y-52,x+43,y-50,x+31,y-43,x+40,y-64,x+50,y-86,x+55,y-95,x+53,y-97,x+44,y-85,x+40,y-72,x+40,y-116,
        x+37,y-115,x+35,y-91,x+30,y-55,x+24,y-44,x+17,y-27,x+7,y-3,x+5,y-47,x+6,y-52,x+17,y-85,x+15,y-88,
        x+5,y-57,x+4,y-76,x+3,y-103,x+4,y-118,x+7,y-129,x+5,y-130,x+1,y-128,x-1,y-103,x-10,y-117,x-12,y-115,x-4,y-101,x-1,y-90,x-2,y-65,
        x-16,y-91,x-22,y-100,x-23,y-96,x-18,y-88,x-5,y-59,x-1,y-43,x-1,y-26,x-20,y-47,x-28,y-60,x-43,y-83,
        x-42,y-84,x-46,y-84,x-44,y-78,x-35,y-64,x-33,y-60,x-51,y-64,x-35,y-56,x-20,y-41,x-9,y-22,x,y+16,x-1,y+56,
        x-3,y+79,x-7,y+104,x-8,y+112,x-9,y+116, opacidad=opacidad) # Polygon del arból seco
    arból_seco.ancho, arból_seco.altura = ancho, altura # Propiedades del arból seco
    return arból_seco # Retorna el arból seco para usarlo en una variable

### Bucle for para crear y ubicar el bosque seco
for i in range(6): # Bucle for para dibujar arbóles secos
    arból_seco = crearArbólSeco(30 + i * 82.5, 240, 60, 90, 100) # Llamado a la función crearArbólSeco para crear el arból grande
    rastro_1 = Oval(arból_seco.centroX-1, arból_seco.centroY+45, 15, 5, relleno='tierra') # Crear un rastro de tierra bajo el arból grande
    arból_seco_fondo_1 = crearArbólSeco(70 + i * 82.5, 250, 35, 50, 80) # Llamado a la función crearArbólSeco para crear el arból mediano
    rastro_2 = Oval(arból_seco_fondo_1.centroX-1, arból_seco_fondo_1.centroY+25, 9, 4, relleno='tierra') # Crear un rastro de tierra bajo el arból mediano
    arból_seco_fondo_2 = crearArbólSeco(13 + i * 82.5, 255, 15, 30, 70) # Llamado a la función crearArbólSeco para crear el arból pequeño a la derecha
    rastro_3 = Oval(arból_seco_fondo_2.centroX-0.3, arból_seco_fondo_2.centroY+15, 4, 3, relleno='tierra') # Crear un rastro de tierra bajo el arból pequeño derecho
    arból_seco_fondo_3 = crearArbólSeco(-37 + i * 82.5, 255, 15, 30, 70) # Llamado a la función crearArbólSeco para crear el arból pequeño a la izquierda
    rastro_4 = Oval(arból_seco_fondo_3.centroX-0.3, arból_seco_fondo_3.centroY+15, 4, 3, relleno='tierra') # Crear un rastro de tierra bajo el arból pequeño izquierdo
    arboles_secos.agregar(rastro_1, rastro_2, rastro_3, rastro_4, arból_seco, arból_seco_fondo_1, arból_seco_fondo_2, arból_seco_fondo_3) # Añadir todo al grupo

## Group 4 - Escena de bosque seco
escenaDeBosqueSeco = Group() # Grupo del bosque totalmente seco
arboles_secos.visible = False # Ocultar bosque totalmente seco

# Para Escena 5 - Bosque Talado
## Funciones de escena de bosque talado

### Dibujar arból talado

## Grupo 5 - Escena de bosque talado
escenaDeBosqueTalado = Group()

# Para Escena 6 - Río siendo afectado por el hombre #
## Funciones de escena de río

### Dibujar el río
def dibujarEscenaDelRío():
    app.fondo = gradiente('azulCieloProfundo','azulCieloClaro', inicio='superior')
    suelo = Rect(0,260,400,140, relleno=gradiente('gris', 'gainsboro', inicio='superior'))
    sol = Estrella(200,0,100,100, relleno=gradiente('oro', 'amarillo', 'tierra'))
    río = Polygon(-10,400,-10,310,190,330,410,365,410,400,relleno=rgb(19,93,139), borde='gainsboro')
    ola = Óvalo(220, 400, 700, 60, relleno=rgb(16,93,179), borde=rgb(12,113,161), rotarAngulo=6, opacidad=50)
    app.dirección = 0.3

## Grupo 6 - Escena contaminando río
escenaContaminandoRío = Group()

# Grupo 7 - Escena de río contaminado
escenaDeRíoContaminado = Group()

# Grupo 8 - Escena de reunión
escenaDeReunión = Group()

# Para Escena 9 - Jardín #
## Funciones de escena de jardín

### Función para dibujar plantaderas pequeña y grande
def crear_mini_plantadera(x, y):
    # Crea la plantadera vertical
    mini_plantadera = Rect(x, y, 40, 70, relleno=gradient('salmonClaro', 'tierra', 'salmonOscuro', inicio='superior'), borde='negro')
    return mini_plantadera
        
def dibujar_plantadera(x, y):
    # Crea la plantadera horizontal
    plantadera = Rect(x, y, 140, 40, relleno=gradient('salmonClaro', 'tierra', 'salmonOscuro', inicio='superior'), borde='negro')
    return plantadera

### Función para dibujar brotes
def dibujarBrotes(x, y):
    Line(x,y,x-3,y-10, relleno=gradient('verde', 'limaVerde', inicio='superior'))
    Line(x,y,x+3,y-10, relleno=gradient('verde', 'verdeBosque', inicio='superior'))
    Oval(x,y,10,6, relleno='tierra')
    dibujarBrotes(250,290), dibujarBrotes(250,310), dibujarBrotes(250,330), dibujarBrotes(250,370)
    dibujarBrotes(300,290), dibujarBrotes(300,310), dibujarBrotes(300,330), dibujarBrotes(300,370)
    dibujarBrotes(350,290), dibujarBrotes(350,310), dibujarBrotes(350,330), dibujarBrotes(350,370)
    dibujarBrotes(270,380), dibujarBrotes(330,380)

# Grupo 9 - Escena del jardín
escenaDeJardín = Group()
escenaDeJardín.visible = False

# Para Escena 10 - Río limpio #
## Funciones de escena de río limpio


# Grupo 10 - Río limpio
escenaDeRioLimpio = Group()

# Grupo 11 - Escena tienda sostenible
escenaDeTienda = Group()

# Grupo 12 - Escena de salvar el bosque
escenaDeSalvaciónDeBosque = Group()

# Grupo 13 - Escena de reciclaje
escenaDeReciclaje = Group()

# Grupo 14 - Mini juego I - ¡¡Planta!!
minijuegoEscena__1 = Group()

# Grupo 15 - Mini juego II - ¡Recicle bucle!
minijuegoEscena_2 = Group()

# Grupo 16 - Mini juego III - ¡Riega, riega!
minijuegoEscena_3 = Group()

# Evento para cambiar entre escenas de una a una
def enTeclaPresionada(tecla):
    if tecla == 'derecha':
        time.sleep(1)
        if app.estado == 'en inicio':
            escenaDeCiudad.visible, app.estado, suelo.relleno = True, 'en escena ciudad', gradient('gris', 'gainsboro', inicio='inferior')
            escenaDeCiudad.agregar(sol, nube_1, nube_2), introducción.vaciar()
        elif app.estado == 'en escena ciudad': 
            escenaDeCiudad.vaciar(), escenaDeBosqueVerde.agregar(sol, nube_1, nube_2, suelo, arbóles)
            escenaDeBosqueVerde.visible, app.estado, suelo.relleno = True, 'en escena bosque verde', gradient('cespedVerde', 'verdeBosque', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'nieve', 'nieve'
        elif app.estado == 'en escena bosque verde': 
            escenaDeBosqueVerde.vaciar(), escenaDeBosqueQuemandose.agregar(sol, nube_1, nube_2, suelo, cenizas)
            escenaDeBosqueQuemandose.visible, app.estado, suelo.relleno = True, 'en escena bosque deteriorandose', gradient('verdeBosque', 'grisClaro', 'salmonClaro', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'gainsboro', 'gainsboro'
        elif app.estado == 'en escena bosque deteriorandose': 
            escenaDeBosqueQuemandose.vaciar(), escenaDeBosqueSeco.agregar(sol, nube_1, nube_2, suelo, arboles_secos)
            escenaDeBosqueSeco.visible, app.estado, suelo.relleno = True, 'en escena bosque seco', gradient('gris', 'grisClaro', 'salmonClaro', inicio='inferior'),
            nube_1.relleno, nube_2.relleno = 'grisClaro', 'grisClaro'
        elif app.estado == 'en escena bosque seco': 
            escenaDeBosqueQuemandose.vaciar(), escenaDeBosqueSeco.agregar(sol, nube_1, nube_2, suelo, arboles_secos)
            escenaDeBosqueSeco.visible, app.estado, suelo.relleno = True, 'en escena bosque seco', gradient('gris', 'grisClaro', 'salmonClaro', inicio='inferior'),
            nube_1.relleno, nube_2.relleno = 'grisClaro', 'grisClaro'
        elif app.estado == 'en escena de reunión': 
            escenaDeBosqueSeco.vaciar(), escenaDeJardín.agregar(sol, nube_1, nube_2, suelo)
            escenaDeJardín.visible, app.estado, suelo.relleno = True, 'en escena jardín', gradient('verde', 'verdeBosque', 'azulCadete', inicio='inferior'),
            nube_1.relleno, nube_2.relleno = 'grisClaro', 'grisClaro'

# Funciones de movimiento en escenas
## Crear efectos del cielo, como el mvto del sol, nubes y aves

### Llenar sol, sin lagear
def llenarSol():
    sol.puntos += 1
    if sol.puntos > 400:
        sol.puntos = 300

### Mover nubes en evento
def moverNubes(limite, posición):
    nube_1.centroX += 1
    nube_2.centroX -= 1
    if nube_1.centroX > limite:
        nube_1.centroX = posición
    if nube_2.centroX < posición:
        nube_2.centroX = limite

## Mover carros de escena 1
### Mover carros hacia la izquieda
def moverCarroALaIzquierda(carro, posición, movimiento, limite):
    carro.centroX -= movimiento
    if carro.centroX == limite:
        carro.centroX = posición

### Mover carros hacia la derecha
def moverCarroALaDerecha(carro, posición, movimiento, limite):
    carro.centroX += movimiento
    if carro.centroX == limite:
        carro.centroX = posición

# Evento de paso para animar escenas        
def enPaso():
    llenarSol() # Animar sol
    moverNubes(500, -100) # Mover nubes
    
    # Escena 1
    if app.estado == 'en escena ciudad':
        moverCarroALaIzquierda(carro_1, 440, 10, -600) # Mover carro azul
        moverCarroALaIzquierda(carro_2, 540, 7, -500) # Mover carro violeta
        moverCarroALaIzquierda(carro_3, 690, 5, -400) # Mover carro gris
        moverCarroALaDerecha(carro_4, -40, 10, 500) # Mover carro verde
        moverCarroALaDerecha(carro_5, -240, 7, 600) # Mover carro rojo
        moverCarroALaDerecha(carro_6, -440, 5, 700) # Mover carro naranja
    
    #  Escena 2
    elif app.estado == 'en escena bosque deteriorandose':
        cenizas.centroY += 5
        cenizas.agregar(cenizas_en_el_aire())
        for i in cenizas:
            if i.centroY > 355:
                cenizas.quitar(i)
    # Escena 6
    elif app.estado == 'en escena río limpio':
        ola.opacidad += 1 * app.dirección
        ola.altura += app.dirección
        río.superior += 0.1 * app.dirección
        if ola.opacidad < 50:
            app.dirección = 0.1
        elif ola.opacidad > 99:
            app.dirección = -0.3

cmu_graphics.run()