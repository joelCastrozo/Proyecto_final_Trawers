# Proyecto final #
# Librerias que estamos utilizando #
from cmu_graphics import * # Libreria de CMU GRAPHICS
import random # Libreria de aleatorio

# Propiedades de app para el funcionamiento del código y de cada escena
## Estado actual de la app, antes de pasar a la primera escena
app.estado = 'Apagada' # Define que la app aún no ha pasadp la primera escena

## Fondo del app, basado en que escena este en pantalla cambiará
app.fondo = 'azulPizarraOscuro' # El fondo inicial/actual de la pantalla de inicio

# Propiedad para textos, basado en sí mostramos o no un texto explicativo de escena
app.textoEnPantalla = True # Declara el estado actual del texto explicativo de escenas

# Objetos para todas las escenas
## Variables
sol = Star(200,0,100,100, fill=gradient('caqui', 'amarillo', 'oro'), visible=False) # El sol
suelo = Rect(0,260,400,140, relleno='azulPizarraOscuro', visible=False) # Suelo de las escenas
camino = Polygon(0,290, 100,295, 200,290, 300,295, 400,300, 400,340, 300,335, 200,330, 100,335, 0,330,
                    fill=gradient('marronCuero', 'tierra', inicio='inferior'), visible=False) # Camino de tierra para los bosques
río = Polygon(-10,400, -10,310, 190,330, 410,365, 410,400, fill=rgb(19,93,139), border='gainsboro', visible=False) # Río base para escenas de río
ola = Oval(220,400,700,80, fill=rgb(16,93,179), borde=rgb(12,113,161), rotateAngle=6, opacity=50, visible=False) # Ola para el río

## Grupos
nube_1 = Group(Circle(45,45,25, fill='white'), 
            Circle(80,45,25, fill='white'), Circle(115,45,25, fill='white')) # Nube grande
nube_2 = Group(Circle(245,60,20, fill='white'),
            Circle(270,60,20, fill='white'), Circle(295,60,20, fill='white')) # Nube pequeña
fondo_montañoso = Group(Polygon(-30,260, 20,215, 90,260, 
                    fill=gradient('azulCadete', 'azulGandul', 'gris', inicio='izquierda-inferior'), opacity=40),
                    Polygon(0,260, 100,210, 200,235, 240,260,
                    fill=gradient('azulCadete', 'azulGandul', 'gris', inicio='izquierda-inferior'), opacity=60),
                    Polygon(140,260, 220,210, 300,230, 340,210, 400,260, 
                    fill=gradient('azulCadete', 'azulGandul', 'gris', inicio='izquierda-inferior'), opacity=60),
                    Polygon(340,260, 410,215, 440,260, 
                    fill=gradient('azulCadete', 'azulGandul', 'gris', inicio='izquierda-inferior'), opacity=40))

## Propiedad visible de grupos
nube_1.visible, nube_2.visible, fondo_montañoso.visible = False, False, False

# Para Escena 0 - Escena de introducción
cubierta_arriba = Rect(0,0,400,200)
cubierta_abajo = Rect(0,200,400,200)

# Crear cadenas de cartél
cadenas_de_cartél = Group()

def crearCadena(x=196, y=85):
    unión_de_cadena = Group(Circle(x+1.5, y+9, 5.5),
        Rect(x-4, y+12, 11, 92), Circle(x+1.5, y+107, 5.5))
    cadena_base = Group(Oval(x,y+115,96,115, fill='gris', borde='negro'),
            Oval(x,y+116,60,73, fill='azulPizarraOscuro', borde='negro'),
            Oval(x,y,96,115, fill='gris', borde='negro'),
            Oval(x,y,60,73, fill='azulPizarraOscuro', borde='negro'))
    cadena = Group(cadena_base, unión_de_cadena)
    cadena.ancho, cadena.altura = 20, 50
    cadenas_de_cartél.agregar(cadena)
    
for i in range(-45, 120, 50):
    crearCadena(55, i) # Cadena izquierda del cartél
    crearCadena(345, i) # Cadena derecha del cartél

panelDeTexto = Group(Rect(20,175,360,60, relleno=gradient('azur', 'grisClaro'), borde='marron', anchuraDeBorde=5)) # Fondo del titulo para evitar contraluz

titulo = Label('¡Hoy veremos los problemas que causan', 200,195, relleno='negro', italica=True, tamaño=16, anchuraDeBorde=6, negrito=True) # Titulo del proyecto
subtitulo = Label('daños en el entorno natural y en nosotros!', 200,215, relleno='negro', italica=True, tamaño=16, anchuraDeBorde=6, negrito=True) # Subtitulo del proyecto
indicacion = Label('Presiona la tecla arriba para continuar', 200,380, relleno='negro', italica=True, tamaño=16, anchuraDeBorde=4) # Indicación de uso del proyecto
introducción = Group(cadenas_de_cartél, panelDeTexto, titulo, subtitulo, indicacion, cubierta_arriba, cubierta_abajo) # Grupo de pantalla de introducción

# Para Escena 1 - Escena de ciudad #
## Funciones y variables para recrear la escena de la ciudad ##

### Para crear ventanas para cada edificio
ventanas = Group() # Grupo para guardar las ventanas
def crearVentanas(x,y):
    # Agrega las ventanas dibujadas al grupo de ventanas
    ventanas.agregar(Rect(x+10,y+15,15,15, relleno='grisClaro',borde='negro'), Rect(x+35,y+15,15,15, relleno='grisClaro',borde='negro'),
                     Rect(x+10,y+40,15,15, relleno='grisClaro',borde='negro'), Rect(x+35,y+40,15,15, relleno='grisClaro',borde='negro'),
                     Rect(x+10,y+65,15,15, relleno='grisClaro',borde='negro'), Rect(x+35,y+65,15,15, relleno='grisClaro',borde='negro'))

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

### Variables de cada edificios en la escena de ciudad
edificio_1 = dibujarEdificio(20,110,'azulOscuro','grisTurbio') # Edificio de la izquierda
edificio_2 = dibujarEdificio(180,110,'caquiOscuro','rojoOscuro') # Edificio del centro
edificio_3 = dibujarEdificio(330,110,'grisPizarraClaro','blanco') # Edificio de la derecha
edificio_4 = dibujarLocal(100,170,'rojoOscuro','marronCuero','MALL') # Local entre el edificio de la izquierda y el del centro
edificio_5 = dibujarLocal(260,170,'varillaDorada','marron','SHOES') # Local entre el edificio del centro y el de la derecha

### Variables para el grupo de canasta de basura y sus propiedades
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

### Grupo basura de la calle
basuraDeCalle = Group() # Grupo para guardar la basura de la calle

### Para crear basura en posiciones aleatorias del suelo y contar la cantidad de ellas
# Propiedades para la basura
contadorDeBasura = 0 # Cuenta de basura
app.basuraTotal = 50 # Cuenta máxima de basura

# Bucle para dibujar basura del suelo
while contadorDeBasura < app.basuraTotal: # Bucle para dibujar la basura
    contadorDeBasura += 1 # Suma de 1 para cada basura
    pos_x_de_papel, pos_y_de_papel = random.randint(5,395), random.randint(270,310) # Número aleatorio de coordenada para los papeles
    pos_x_de_botella, pos_y_de_botella = random.randint(5,395), random.randint(270,310) # Número aleatorio de coordenada para las botellas
    papel = Star(pos_x_de_papel, pos_y_de_papel, 3, 8, relleno='blanco', borde='negro', anchuraDeBorde = 0.2, guion=True) # Dibujar papeles en el suelo
    botella = Rect(pos_x_de_botella, pos_y_de_botella, 2, 7, relleno='azulClaro') # Dibujar botellas en el suelo
    basuraDeCalle.agregar(papel, botella) # Agrega cada botella y papel al grupo de basura

### Para ocultar el grupo de basura de calle
basuraDeCalle.opacidad = 0

### Para dibujar un carro, con parametros de color, punto de partida y dirección a la que se dirige
def crearAutos(color, partida, direccion):
    # Crea los autos, les da un color, ubica en donde iniciaran su trayectoria y hacia que dirección se moverán
    base = Rect(partida, direccion-30, 70, 30, relleno=color) # Dibuja la parte inferior o soporte del carro
    capo = Rect(partida+10, direccion-50, 50, 20, relleno=color) # Dibuja la parte superior o cubierta del carro
    ruedaIzq = Circle(partida+15, direccion, 10) # Dibuja la llanta izquierda del carro
    ruedaDer = Circle(partida+55, direccion, 10) # Dibuja la llanta derecha del carro
    carro = Group(capo, base, ruedaIzq, ruedaDer) # Grupo con todas las partes del carro
    return carro #  Retorna el carro para guardarlo en una variable

### Variables de cada carro en la escena
carro_1 = crearAutos(gradient('azulReal', 'azulGandul', inicio='inferior'), 440, 340) # Carro en vía alterna hacia el norte
carro_2 = crearAutos(gradient('violetaRojoMedio', 'violeta', inicio='inferior'), 540, 340) # Carro en vía alterna hacia el norte
carro_3 = crearAutos(gradient('grisOscuro', 'grisClaro', inicio='inferior'), 690, 340) # Carro en vía alterna hacia el norte
carro_4 = crearAutos(gradient('verde', 'limaVerde', inicio='inferior'), -40, 380) # Carro en vía alterna hacia el sur
carro_5 = crearAutos(gradient('rojo', 'carmesi', inicio='inferior'), -240, 380) # Carro en vía alterna hacia el sur
carro_6 = crearAutos(gradient('naranja', 'oro', inicio='inferior'), -440, 380) # Carro en vía alterna hacia el sur

## Grupo 1 - Escena de ciudad
### Grupo de la escena de la ciudad con sus elementos respectivos
escenaDeCiudad = Group(fondo_montañoso, edificio_1, edificio_2, edificio_3, edificio_4, edificio_5, ventanas, suelo, basura, basuraDeCalle,
    Rect(-20,320,440,80, relleno='grisOscuro', borde='gris', anchuraDeBorde=5), 
    Line(0,360,410,360, relleno=gradient('negro', 'grisOscuro', 'negro'), anchuraDeLinea=4, guion=(5,6)), carro_1, carro_2, carro_3, carro_4, carro_5, carro_6)

### Propiedad para el grupo de la escena de la ciudad
escenaDeCiudad.visible = False # Oculta la escena

# Para Escena 2 - Bosque verde #
## Funciones y variables para recrear la escena del bosque verde ##

### Grupo de arbóles para el bosque verde
arbóles = Group() # Group para guardar los arbóles generados

### Propiedad visible del grupo de arbóles
arbóles.visible = False # Oculta los arbóles creados

### Para dibujar un arból
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
### Grupo de la escena del bosque verde vacío
escenaDeBosqueVerde = Group() # Grupo de escena de bosque verde

### Propiedad del grupo de escena de bosque verde
escenaDeBosqueVerde.visible = False # Oculta el grupo de bosque verde

# Para Escena 3 - Bosque deteriorandose o quemandose
## Funciones y variables para recrear la escena del bosque quemandose ##

### Para crear las cenizas
def cenizas_en_el_aire():
    # Crea las cenizas que deja el bosque al calcinarse
    posicion_x_de_cenizas, posicion_y_de_cenizas  = random.randint(0,400), random.randint(0, 400) # Posición al azar del centroX y centroY de la ceniza
    ceniza = Circle(posicion_x_de_cenizas, posicion_y_de_cenizas, 2, relleno='gris') # La ceniza con sus propiedades
    return ceniza # Retorna la ceniza a un grupo

### Grupo para guardar las cenizas en el aire
cenizas = Group() # Grupo de cenizas

## Grupo 3 - Escena de bosque deteriorandose
escenaDeBosqueQuemandose = Group() # Grupo para bosque incendiado

### Propiedad visible para grupo de escena de bosque quemandose
escenaDeBosqueQuemandose.visible = False # Ocultar bosque incendiado

# Para Escena 4 - Bosque seco, ya muerto
## Funciones y variables para recrear la escena del bosque seco ##

### Grupo para arbóles secos
arbóles_secos = Group() # Grupo para guardar cada arból

### Propiedad visible para grupo de arbóles secos
arbóles_secos.visible = False # Ocultar bosque totalmente seco

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
    arbóles_secos.agregar(rastro_1, rastro_2, rastro_3, rastro_4, arból_seco, arból_seco_fondo_1, arból_seco_fondo_2, arból_seco_fondo_3) # Añadir todo al grupo

## Group 4 - Escena de bosque seco
###  Grupo de escena bosque seco
escenaDeBosqueSeco = Group() # Grupo del bosque totalmente seco

###  Propiedad de visible para bosque seco
escenaDeBosqueSeco.visible = False # Ocultar bosque incendiado

# Para Escena 5 - Bosque Talado
## Funciones y variables para recrear la escena del bosque talado ##

### Grupo para arbóles talados
arbóles_talados = Group() # Grupos para arbóles talados

### Para dibujar arból talado
def dibujarArbólCortado(x,y):
    pass

### Para dibujar arból caído
def dibujarArbólCaído(x,y):
    pass

### Bucle for para crear y ubicar el bosque talado
for i in range(6): # Bucle for para dibujar arbóles talados
    pass

### Bucle for para crear y ubicar los arbóles caídos
for i in range(6): # Bucle for para dibujar arbóles caídos
    pass

## Grupo 5 - Escena de bosque talado
### Grupo para escena de bosque talado
escenaDeBosqueTalado = Group()

### Propiedad de visible para escena de bosque talado
escenaDeBosqueTalado.visible = False

# Para Escena 6 - Río siendo afectado por el hombre #
## Funciones y variables para recrear la escena del río cuando está siendo contaminado ##

### Grupo de fondo de ciudad
fondo_es_río = Group()

### Propiedad visible para fondo de escena de río
fondo_es_río.visible = False

### Para fondo de escenas de río
def dibujarEdificio(x, h=140, o=60):
    fondo_río = Group(Rect(x, h + 10, 50, 400 - h, alinear='superior', relleno=gradient(rgb(150, 195, 90), rgb(195, 110, 115), inicio='izquierda'), opacidad=o),
    Polygon(x, h - 30, x - 25, h + 10, x + 25, h + 10, relleno=gradient(rgb(150, 195, 90), rgb(195, 110, 115), inicio='izquierda'), opacidad=o))
    return fondo_río
     
### Bucle para fondo de ciudad
for i in range(6):
    fondo_es_río.agregar(dibujarEdificio(80 * i))
    fondo_es_río.agregar(dibujarEdificio(40 + 80 * i, 110, 45))

### Propiedad para animar el río
app.dirección = 0

### Para crear la banca
def crearBanca(x=250, y=270):
    banca = Group(Polygon(x, y, x+80, y+5, x+75, y+30, x-5, y+25, relleno=gradient('marronArenoso', 'bronceado'), borde='marron', anchuraDeBorde=0.8),
        Polygon(x-15, y+35, x-5, y+25, x-5, y+45, relleno=gradient('marronArenoso', 'bronceado'), borde='marron', anchuraDeBorde=0.8),
        Polygon(x-5, y+25, x+75, y+30, x+65, y+40, x-15, y+35, relleno=gradient('marronArenoso', 'bronceado'), borde='marron', anchuraDeBorde=0.8),
        Polygon(x+65, y+40, x+75, y+30, x+70, y+50, relleno=gradient('marronArenoso', 'bronceado'), borde='marron', anchuraDeBorde=0.8))
    return banca

### Grupo de banca
banca = crearBanca()

### Propiedad visible para banca
banca.visible = False

## Grupo 6 - Escena contaminando río
escenaDeRíoEnsuciado = Group()

# Para Escena 7 - Río contaminado #
## Funciones y variables para recrear la escena del río muy sucio ##

# Grupo 7 - Escena de río contaminado
escenaDeRíoContaminado = Group()

# Para Escena 8 - Reunión contra la contaminación #
## Funciones y variables para recrear la escena de la reunión ambiental ##

### Tablero de reunión
tablero = Rect(60,60,280,140,relleno='blancoFantasma',borde='plateado',anchuraDeBorde=5, visible=False)

# Grupo 8 - Escena de reunión
### Grupo de reunión
escenaDeReunión = Group()

### Propiedad visible para grupo de reunión
escenaDeReunión.visible = False

# Para Escena 9 - Jardín #
## Funciones y variables para recrear la escena del jardín creado por los ambientalistas ##

### Para dibujar plantaderas pequeña y grande
def dibujar_plantadera(x, y, ancho=40, altura=70):
    # Crea las plantadera
    plantadera = Rect(x, y, ancho, altura, relleno=gradient('salmonClaro', 'tierra', 'salmonOscuro', inicio='superior'), borde='negro')
    return plantadera

### Para dibujar brotes
def dibujarBrotes(x, y):
    brote = Group(
        Line(x,y,x-3,y-10, relleno=gradient('verde', 'limaVerde', inicio='superior')),
        Line(x,y,x+3,y-10, relleno=gradient('verde', 'verdeBosque', inicio='superior')),
        Oval(x,y,10,6, relleno='tierra'))
    return brote

### Para dibujar arbustos
def arbusto(x,y,ancho,altura,opacidad=100):
    arbusto = Group(Circle(243,214,12,relleno=rgb(139,198,64)), Circle(259,191,17,relleno=rgb(139,198,64)),Circle(282,173,13,relleno=rgb(139,198,64)),
    Circle(314,161,19,relleno=rgb(139,198,64)),Oval(338,176,22,26,rotarAngulo=10,relleno=rgb(139,198,64)),Circle(364,190,16,relleno=rgb(139,198,64)),
    Oval(380,211,29,26, relleno=rgb(139,198,64)), Polygon(243,226,259,191,282,173,314,161,338,176,364,190,380,211,394,216,391,226,relleno=rgb(139,198,64)))
    arbusto.centroX, arbusto.centroY, arbusto.ancho, arbusto.altura = x, y, ancho, altura
    return arbusto

### Carreta con arena
carretilla_de_arena = Group(Circle(85,160,19, relleno=rgb(161, 90, 45)), Circle(90,180,19, relleno='tierra'), Circle(70,170,19, relleno='tierra'),
        Circle(110, 215, 12, relleno=gradient('blanco', 'negro', 'negro')),
        Polygon(45, 195, 40, 175, 120, 175, 95, 210, relleno=gradient('azul', 'azulCadete', inicio='inferior'), borde='azualAciano'),
        Polygon(45, 200, 65, 205, 55, 225, relleno=None, borde='gris', anchuraDeBorde=3),
        Line(20, 190, 110, 215, relleno='gris', anchuraDeLínea=4))

### Propiedad de carreta
carretilla_de_arena.visible = False

### Grupos para arbustos, plantaderas y brotes
arbustos = Group()
plantaderas = Group()
brotes = Group()
arbustos.visible = False
plantaderas.visible = False
brotes.visible = False

### Agregar plantaderas y brotes a sus grupos correspondientes
plantaderas.agregar(dibujar_plantadera(240,280), dibujar_plantadera(290,280), dibujar_plantadera(340,280), dibujar_plantadera(240, 355, 140, 40))
brotes.agregar(dibujarBrotes(260,290), dibujarBrotes(260,310), dibujarBrotes(260,330), dibujarBrotes(260,370), dibujarBrotes(310,290), dibujarBrotes(310,310), 
               dibujarBrotes(280,380), dibujarBrotes(310,330), dibujarBrotes(310,370), dibujarBrotes(360,290), dibujarBrotes(360,310), dibujarBrotes(360,330), 
               dibujarBrotes(360,370), dibujarBrotes(340,380))

### Bucle para dibujar arbustos
for i in range(3):
    arbustos.agregar(arbusto(40 + i * 74, 280, 60, 40))

#  Grupo 9 - Escena del jardín
escenaDeJardín = Group()
escenaDeJardín.visible = False

# Para Escena 10 - Río limpio #
## Funciones y variables para recrear la escena del río siendo limpiado por los ambientalistas ##

### Para para dibujar contenedores de basura
def dibujar_contenedor(x, y):
    pass

# Grupo 10 - Río limpio
escenaDeRíoLimpio = Group()

# Para Escena 11 - Escena apertura de tienda sostenible #
## Funciones y variables para recrear la escena de la apertura de la tienda sostenible de los ambieentalistas ##

### Para dibujar

# Grupo 11 - Escena tienda sostenible
escenaDeTienda = Group()

# Para Escena 12 - Salvar el bosque #
## Funciones y variables para recrear la escena de la campaña para prohibir la tala excesiva de arbóles ##

### Para dibujar
 
# Grupo 12 - Escena de salvar el bosque
escenaDeSalvaciónDeBosque = Group()

# Para Escena 13 - Escena de reciclaje #
## Funciones y variables para recrear la escena de reciclaje del grupo ambientalista ##

# Grupo 13 - Escena de reciclaje
escenaDeReciclaje = Group()

# Para Escena Interactiva 1 - ¡¡Planta!!
## Variables y funciones correspondientes a la escena interactiva 1

### Variables de juego 1 
macetero = Polygon(220,320,260,270,380,270,340,320, relleno='tierra', borde='granate',anchuraDeBorde=5, visible = False)
semilla = Oval(80,280,35,15, relleno='chocolate', visible = False)
arbol_DE, arbol_DE.visible = Group(Line(300,220,300,285, relleno='madera',anchuraDeLinea=10), Circle(297,185,20,relleno='verdeOscuro'),
            Circle(311,187,20,relleno='verdeOscuro'),Circle(315,215,10,relleno='verdeOscuro'), Circle(289,215,10,relleno='verdeOscuro'),
            Circle(280,192,15,relleno='verdeOscuro')), False
agua = Polygon(200,45,190,65,190,70,200,76,210,70,210,65, relleno='agua', visible = False)

### Función para mostrar indicaciones de juego 1
def dibujar_indicaciones():
    indicaciones = Group(Label('Mueva la semilla hacia el macetero', 200, 33), Label('Planta una planta en la plantadera para hacer crecer la planta', 200,350))
    return indicaciones

# Grupo 14 - Mini juego I - ¡¡Planta!!
### Grupo de escena interactiva de minijuego 1
minijuegoEscena_1 = Group()
### Propiedad visible de escena interactiva de minijuego 1
minijuegoEscena_1.visible = False

# Para Escena Interactiva 2 - ¡Recicle bucle!
## Funciones correspondientes a la escena interactiva 2

### Función para dibujar

## Variables y funciones correspondientes a la escena interactiva 1

### Variables de juego 2

# Grupo 15 - Mini juego II - ¡Recicle bucle!
### Grupo de escena interactiva de minijuego 2
minijuegoEscena_2 = Group()
### Propiedad visible de escena interactiva de minijuego 2
minijuegoEscena_2.visible = False

# Para Escena Interctiva 3 - ¡Riega, riega!
## Funciones correspondientes a la escena interactiva 3

## Variables y funciones correspondientes a la escena interactiva 1

### Variables de juego 3

# Grupo 16 - Mini juego III - ¡Riega, riega!
### Grupo de escena interactiva de minijuego 3
minijuegoEscena_3 = Group()
### Propiedad visible de escena interactiva de minijuego 3
minijuegoEscena_3.visible = False

# Para Escenna Final - Escena de conclusión #
## Objetos de la escena final ##

### Variables para escena final
app.proximoÁngulo = 272.5
app.radio = 140
app.círculoLleno = False
app.i = -1
app.proximoÁngulo2 = 321.5
app.radio2 = -140
app.i2 = -1

# Grupo con los elementos de la escena final
escenaFinal = Group()

# Evento para cambiar entre escenas de una a una
def enTeclaPresionada(tecla):
    if tecla == 'espacio':
        app.estado = 'Mostrar animación'
    if tecla == 'arriba':
        titulo.valor = '¡El ambiente está en riesgo y nosotros'
        subtitulo.valor = 'tenemos la tarea de protegerlo y mejorarlo!'
        indicacion.valor = 'Presione la tecla derecha para la siguiente escena   '
        app.textoEnPantalla = False
        app.estado = 'En inicio'
    if app.textoEnPantalla == False and tecla == 'derecha':
        if app.estado == 'En inicio':
            escenaDeCiudad.visible, app.estado, suelo.relleno = True, 'En escena de ciudad', gradient('gris', 'gainsboro', inicio='inferior')
            escenaDeCiudad.agregar(sol, nube_1, nube_2), introducción.vaciar()
        elif app.estado == 'En escena de ciudad':
            escenaDeCiudad.vaciar(), escenaDeBosqueVerde.agregar(sol, nube_1, nube_2, suelo, camino, fondo_montañoso, arbóles)
            escenaDeBosqueVerde.visible, app.estado, suelo.relleno = True, 'En escena de bosque verde', gradient('cespedVerde', 'verdeBosque', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'nieve', 'nieve'
        elif app.estado == 'En escena de bosque verde': 
            escenaDeBosqueVerde.vaciar(), basuraDeCalle.vaciar(), escenaDeBosqueQuemandose.agregar(sol, nube_1, nube_2, suelo, camino, fondo_montañoso, cenizas)
            escenaDeBosqueQuemandose.visible, app.estado, suelo.relleno = True, 'En escena de bosque deteriorandose', gradient('verdeBosque', 'grisClaro', 'salmonClaro', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'gainsboro', 'gainsboro'
        elif app.estado == 'En escena de bosque deteriorandose': 
            escenaDeBosqueQuemandose.vaciar(), escenaDeBosqueSeco.agregar(sol, nube_1, nube_2, suelo, camino, fondo_montañoso, arbóles_secos)
            escenaDeBosqueSeco.visible, app.estado, suelo.relleno = True, 'En escena de bosque seco', gradient('gris', 'grisClaro', 'salmonClaro', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'grisClaro', 'grisClaro'
        elif app.estado == 'En escena de bosque seco': 
            escenaDeBosqueSeco.vaciar(), escenaDeBosqueTalado.agregar(sol, nube_1, nube_2, suelo, camino, fondo_montañoso, arbóles_talados)
            escenaDeBosqueTalado.visible, app.estado, suelo.relleno = True, 'En escena de bosque talado', gradient('gris', 'grisClaro', 'salmonClaro', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'grisClaro', 'grisClaro'
        elif app.estado == 'En escena de bosque talado': 
            escenaDeBosqueTalado.vaciar(), escenaDeRíoEnsuciado.agregar(fondo_es_río, sol, nube_1, nube_2, suelo, banca, río, ola)
            escenaDeRíoEnsuciado.visible, app.estado, suelo.relleno = True, 'En escena de río ensuciado', gradient('gris', 'grisClaro', 'gainsboro', inicio='inferior')
            nube_1.relleno, nube_2.relleno, app.dirección = 'grisClaro', 'grisClaro', 0.3
        elif app.estado == 'En escena de río ensuciado': 
            escenaDeRíoEnsuciado.vaciar(), escenaDeRíoContaminado.agregar(fondo_es_río, sol, nube_1, nube_2, suelo, banca, río, ola)
            escenaDeRíoContaminado.visible, app.estado, suelo.relleno = True, 'En escena de río contaminado', gradient('gris', 'grisClaro', 'gainsboro', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'grisClaro', 'grisClaro'
        elif app.estado == 'En escena de río contaminado': 
            escenaDeRíoContaminado.vaciar(), escenaDeReunión.agregar(tablero, suelo)
            escenaDeReunión.visible, app.estado, suelo.relleno, app.fondo = True, 'En escena de reunión', 'azulCadete', gradient('azulCadete', 'azulMediaNoche')
            nube_1.relleno, nube_2.relleno = 'grisClaro', 'grisClaro'
            from logo_no_más import fotoDeProhibirTalaDeArboles
        elif app.estado == 'En escena de reunión': 
            escenaDeReunión.vaciar(), escenaDeJardín.agregar(sol, nube_1, nube_2, suelo, fondo_montañoso, arbustos, carretilla_de_arena, plantaderas, brotes)
            app.fondo, carretilla_de_arena.inferior = 'azulCielo', 360
            escenaDeJardín.visible, app.estado, suelo.relleno = True, 'En escena de jardín', gradient('verde', 'verdeBosque', 'azulCadete', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'grisClaro', 'grisClaro'
            from logo_no_más import modulo_de_logo
            modulo_de_logo()
        elif app.estado == 'En escena de jardín': 
            escenaDeJardín.vaciar(), escenaDeRíoLimpio.agregar(fondo_es_río, sol, nube_1, nube_2, suelo, banca, río, ola)
            escenaDeRíoLimpio.visible, app.estado, suelo.relleno = True, 'En escena de río límpio', gradient('gris', 'grisClaro', 'gainsboro', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'grisClaro', 'grisClaro'
        elif app.estado == 'En escena de río límpio': 
            escenaDeRíoLimpio.vaciar(), escenaDeTienda.agregar(sol, nube_1, nube_2, suelo, Rect(-20,320,440,80, relleno='grisOscuro', borde='gris', anchuraDeBorde=5), 
                                                            Line(0,360,410,360, relleno=gradient('negro', 'grisOscuro', 'negro'), anchuraDeLinea=4, guion=(5,6)))
            escenaDeTienda.visible, app.estado, suelo.relleno = True, 'En escena de tienda', gradient('gris', 'blanco', 'nieve', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'gainsboro', 'gainsboro'
            from camion import camión
        elif app.estado == 'En escena de tienda': 
            escenaDeTienda.vaciar(), escenaDeSalvaciónDeBosque.agregar(sol, nube_1, nube_2, fondo_montañoso, suelo, arbóles)
            escenaDeSalvaciónDeBosque.visible, app.estado, suelo.relleno = True, 'En escena de campaña', gradient('gris', 'blanco', 'nieve', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'gainsboro', 'gainsboro'
            from camion import modulo_de_camion
            modulo_de_camion()
        elif app.estado == 'En escena de campaña': 
            escenaDeSalvaciónDeBosque.vaciar(), escenaDeReciclaje.agregar(sol, nube_1, nube_2, fondo_montañoso, suelo)
            escenaDeReciclaje.visible, app.estado, suelo.relleno = True, 'En escena de reciclaje', gradient('gris', 'blanco', 'nieve', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'nieve', 'nieve'
        elif app.estado == 'En escena de reciclaje': 
            escenaDeReciclaje.vaciar(), minijuegoEscena_1.agregar(sol, nube_1, nube_2, fondo_montañoso, suelo, macetero, semilla, dibujar_indicaciones())
            minijuegoEscena_1.visible, app.estado, suelo.relleno = True, 'En escena de minijuego I', gradient('verde', 'verdeBosque', 'verde', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'nieve', 'nieve'
        elif app.estado == 'En escena de minijuego I': 
            minijuegoEscena_1.vaciar(), minijuegoEscena_2.agregar(sol, nube_1, nube_2, fondo_montañoso, suelo)
            minijuegoEscena_2.visible, app.estado, suelo.relleno = True, 'En escena de minijuego II', gradient('verde', 'verdeBosque', 'verde', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'nieve', 'nieve'
        elif app.estado == 'En escena de minijuego II': 
            minijuegoEscena_2.vaciar(), minijuegoEscena_3.agregar(sol, nube_1, nube_2, fondo_montañoso, suelo)
            minijuegoEscena_3.visible, app.estado, suelo.relleno = True, 'En escena de minijuego III', gradient('verde', 'verdeBosque', 'verde', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'nieve', 'nieve'
        elif app.estado == 'En escena de minijuego III': 
            minijuegoEscena_3.vaciar(), minijuegoEscena_3.agregar()
            minijuegoEscena_3.visible, app.estado, suelo.relleno = True, 'En escena de resumén', gradient('verde', 'verdeBosque', 'verde', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'nieve', 'nieve'
        elif app.estado == 'En escena de resumén': 
            minijuegoEscena_3.vaciar()
            app.estado = 'En escena de final'
        
# Evento especial
def enTeclaRetenida(teclas):
    if 'espacio' in teclas and app.estado == 'En escena de ciudad':
        if basuraDeCalle.opacidad < 100:
            basuraDeCalle.opacidad += 1
        else:
            sol.relleno = gradient('caqui', 'naranja', 'oro')

# Evento para interactuar en las escenas
## enRatónArrastrado
def enRatónArrastrado(ratónX, ratónY):
    # Escena Interactiva 1
    if app.estado == 'En escena de juego I':
        if semilla.contiene(ratónX, ratónY):
            semilla.centroX = ratónX
            semilla.centroY = ratónY
        elif agua.contiene(ratónX, ratónY):
            agua.centroX = ratónX
            agua.centroY = ratónY
        if agua.tocaFigura(arbol_DE):
            if arbol_DE.altura < 160: 
                arbol_DE.inferior -= 4
                arbol_DE.altura += 5
                arbol_DE.ancho += 1
## enRatónSoltado
def enRatónSoltado(ratónX, ratónY):
    # Escena Interactiva 1
    if app.estado == 'En escena de juego I':
        if semilla.tocaFigura(macetero):
            minijuegoEscena_1.quitar(semilla)
            minijuegoEscena_1.agregar(arbol_DE)
        if arbol_DE in minijuegoEscena_1:
           minijuegoEscena_1.agregar(agua)

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
def moverCarro(carro, posición, movimiento, limite):
    carro.centroX -= movimiento
    if carro.centroX == limite:
        carro.centroX = posición

# Evento de paso para animar escenas        
def enPaso():
    # General
    llenarSol() # Animar sol
    moverNubes(500, -100) # Mover nubes
    
    # Escena 0
    if app.estado == 'Mostrar animación':
        if cubierta_arriba.inferior > 0:
            cubierta_arriba.centroY -= 5
            
        if cubierta_abajo.superior < 400:
            cubierta_abajo.centroY += 5

    # Escena 1
    if app.estado == 'En escena de ciudad':
        moverCarro(carro_1, 440, 10, -600) # Mover carro azul
        moverCarro(carro_2, 540, 7, -500) # Mover carro violeta
        moverCarro(carro_3, 690, 5, -400) # Mover carro gris
        moverCarro(carro_4, -40, -10, 500) # Mover carro verde
        moverCarro(carro_5, -240, -7, 600) # Mover carro rojo
        moverCarro(carro_6, -440, -5, 700) # Mover carro naranja
    
    #  Escena 3
    elif app.estado == 'En escena de bosque deteriorandose':
        cenizas.centroY += 5
        cenizas.agregar(cenizas_en_el_aire())
        for i in cenizas:
            if i.centroY > 355:
                cenizas.quitar(i)
    
    # Escena 6
    elif app.estado == 'En escena de río ensuciado' or app.estado == 'En escena de río contaminado' or app.estado == 'En escena de río límpio':
        ola.opacidad += 1 * app.dirección
        ola.altura += app.dirección
        río.superior += 0.1 * app.dirección
        if ola.opacidad < 50:
            app.dirección = 0.1
        elif ola.opacidad > 99:
            app.dirección = -0.3

    # Escena final
    app.planetaMostrado = False
    if app.estado == 'En escena de final':
        from tierra_foto import tierra # Módulo para el planeta tierra
        app.planetaMostrado = True
        app.pasosPorSegundo = 15
        if (app.planetaMostrado == True):
            app.proximoÁngulo += 7
            app.proximoÁngulo2 += 7
            palabras = 'Cuidemos nuestro planeta'
            próximoX, próximoY = getPointInDir(200, 200, app.proximoÁngulo, app.radio)
            if app.i < 23:
                app.i += 1
                palabra = Group(Label(palabras[app.i], próximoX, próximoY, relleno=gradient('blanco','azulClaro', inicio='superior'), 
                    tamaño=20, negrito=True, rotarÁngulo=app.proximoÁngulo))
            oración = '!!sotnuJ¡¡ '
            próximoX2, próximoY2 = getPointInDir(200, 200, app.proximoÁngulo2, app.radio2)
            if app.i2 < 9:
                app.i2 += 1
                subpalabra = Group(Label(oración[app.i2], próximoX2, próximoY2, relleno=gradient('blanco','azulClaro', inicio='superior'), 
                    tamaño=20, negrito=True, rotarÁngulo=app.proximoÁngulo2))

cmu_graphics.run()