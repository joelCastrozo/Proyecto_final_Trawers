# Proyecto final #
# Librerias que estamos utilizando #
from cmu_graphics import * # Libreria de CMU GRAPHICS
import random # Libreria de aleatorio

# Propiedades de app para el funcionamiento del código y de cada escena

## Estado actual de la app, antes de pasar a la primera escena
app.estado = 'Apagada' # Define que la app aún no ha pasadp la primera escena

## Fondo del app, basado en que escena este en pantalla cambiará
app.fondo = gradient(rgb(35,40,48), rgb(48,66,70), rgb(82,100,102), rgb(109, 135,150), inicio='superior') # El fondo inicial/actual de la pantalla de inicio

## Propiedad del app, basado en si el cartél de escenas está abajo o arriba
app.cartel_estado = 'Oculto' # El estado inicial del cartél de rótulos

## Propiedad para textos, basado en sí mostramos o no un texto explicativo de escena
app.valoresDeTexto_up, app.valoresDeTexto_mid, app.valoresDeTexto_down = 0, 1, 2 # Declara el estado actual del texto explicativo de las escenas

# Objetos para todas las escenas
## Variables
sol = Star(200,0,100,100, fill=gradient('caqui', rgb(255, 255, 0), 'oro'), visible=False) # El sol
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
fondo_montañoso = Group(Polygon(-30,260, 20,215, 90,260, fill=gradient('azulCadete', 'azulGandul', 'gris', inicio='izquierda-inferior'), opacity=40),
                    Polygon(0,260, 100,210, 200,235, 240,260, fill=gradient('azulCadete', 'azulGandul', 'gris', inicio='izquierda-inferior'), opacity=60),
                    Polygon(140,260, 220,210, 300,230, 340,210, 400,260, fill=gradient('azulCadete', 'azulGandul', 'gris', inicio='izquierda-inferior'), opacity=60),
                    Polygon(340,260, 410,215, 440,260, fill=gradient('azulCadete', 'azulGandul', 'gris', inicio='izquierda-inferior'), opacity=40)) # Fondo de montañas

## Propiedad visible de grupos
nube_1.visible, nube_2.visible, fondo_montañoso.visible = False, False, False # Modificar visibilidad de los grupos

# Para Escena 0 - Escena de introducción
## Funciones y variables para escena 0

### Cubierta
cubierta_superior = Rect(0,0,400,200) # Cubierta arriba
cubierta_inferior = Rect(0,200,400,200) # Cubierta abajo
print('>> ¡Presione espacio para encender!')

### Grupo para las cadenas de cartél
cadenas_de_cartél = Group() # Grupo vacío para guardar las cadenas

### Para crear cadenas
def crearCadena(x=196, y=85):
    # Crea la unión de la cadena y la base y las agrega al grupo de cadenas de cartél
    unión_de_cadena = Group(Circle(x+1.5, y+9, 5.5),
        Rect(x-4, y+12, 11, 92), Circle(x+1.5, y+107, 5.5)) # Unión entre cadenas
    cadena_base = Group(Oval(x,y+115,96,115, fill='gris', borde='negro'),
            Oval(x,y+116,60,73, fill=rgb(35,40,48), borde='negro'),
            Oval(x,y,96,115, fill='gris', borde='negro'), 
            Oval(x,y,60,73, fill=rgb(35,40,48), borde='negro')) # Parte principal de la cadena
    cadena = Group(cadena_base, unión_de_cadena) # Grupo para guardar la cadena
    cadena.ancho, cadena.altura = 20, 50 # Modificación del tamaño de la cadena
    cadenas_de_cartél.agregar(cadena) # Añadir cadena al grupo de cadenas del cartél
    
for i in range(-45, 120, 50):
    # Para dibujar las cadenas del cartél a sus dos extremos
    crearCadena(55, i) # Cadena izquierda del cartél
    crearCadena(345, i) # Cadena derecha del cartél

### Cartél
panelDeTexto = Group(Rect(20,175,360,60, relleno=gradient('azur', 'grisClaro'), borde='marron', anchuraDeBorde=5)) # Fondo del titulo para evitar contraluz
titulo = Label('¡Hoy veremos los problemas que causan', 200,195, relleno='negro', italica=True, tamaño=16, anchuraDeBorde=6, negrito=True) # Titulo del proyecto
subtitulo = Label('daños en el entorno natural y en nosotros!', 200,215, relleno='negro', italica=True, tamaño=16, anchuraDeBorde=6, negrito=True) # Subtitulo del proyecto
indicacion = Label('Presiona la tecla arriba para continuar', 200,380, relleno='negro', italica=True, tamaño=16, anchuraDeBorde=4) # Indicación de uso del proyecto
introducción = Group(cadenas_de_cartél, panelDeTexto, titulo, subtitulo, indicacion, cubierta_superior, cubierta_inferior) # Grupo de pantalla de introducción

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
escenaDeCiudad = Group(fondo_montañoso, edificio_1, edificio_2, edificio_3, edificio_4, edificio_5, ventanas, suelo, basuraDeCalle, basura,
    Rect(-20,320,440,80, relleno='grisOscuro', borde='gris', anchuraDeBorde=5), # Base de carretera
    Line(0,360,410,360, relleno=gradient('negro', 'grisOscuro', 'negro'), anchuraDeLinea=4, guion=(5,6)), carro_1, carro_2, carro_3, carro_4, carro_5, carro_6) # División de carretera

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
## Funciones y variables para recrear la escena del bosque quemandose

### Grupo arbóles quemados
arbóles_quemados = Group()
arbóles_quemados.visible = False

### Bucle for para arbóles
for i in range(5): # Da una posición en cuanto a cada paso y crea el árbol quemandose
    arból_quemado_1 = crearArbóles(115 + i * 82.6, 300, 60, 90, 100, 'grisOscuro') # Llamada a la función crearArbóles para crear el arból grande
    arból_quemado_2 = crearArbóles(70 + i * 82.5, 320, 35, 50, 80, 'gris') # Llamada a la función crearArbóles para crear el arból del medio
    arból_quemado_3 = crearArbóles(90 + i * 82, 325, 15, 30, 70, 'grisOscuro') # Llamada a la función crearArbóles para crear el arból pequeño izquierdo
    arból_quemado_4 = crearArbóles(135+ i * 82.5, 325, 15, 30, 70, 'gris') # Llamada a la función crearArbóles para crear el arból derecho
    arbóles_quemados.agregar(arból_quemado_1, arból_quemado_2, arból_quemado_3, arból_quemado_4) # Agrega los arbóles quemados al grupo de arbóles

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
arbóles_talados.visible = False

### Para dibujar arból talado
def dibujarArbólTalado(x=200, y=200, ancho=79, altura=103):
    arból_talado = Group(Polygon(185,74,182,94,181,97,175,107,186,105,190,116,213,109,228,115,232,110,254,110,253,103,250,98,248,74,
    relleno=gradient('marronCuero','naranjaMarrón', 'marronCuero', 'tierra', 'naranjaMarrón', 'marronCuero', 'tierra', 
    'naranjaMarrón', 'marronCuero', 'tierra', inicio='izquierda')),
    Rect(185, 23, 62.5, 81, relleno=gradient('naranjaMarrón', 'marronCuero', 'tierra', 'naranjaMarrón', 'marronCuero', 'tierra', 'naranjaMarrón', 
    'marronCuero', 'tierra', inicio='izquierda')),
    Oval(216.7,22,63,18, relleno='tierra'), Oval(216.7,22,53,12, relleno='caqui'),
    Oval(216.7,22,43,8, relleno='naranjaMarrón'), Oval(216.7,22,33,4, relleno='caqui'), Oval(216.7,22,23,2, relleno='marronCuero'))
    arból_talado.centroX, arból_talado.inferior = x, y
    arból_talado.ancho, arból_talado.altura = ancho, altura
    return arból_talado

### Bucle for para crear y ubicar el bosque talado
for i in range(6): # Bucle for para dibujar arbóles talados
    arból_talado_1 = dibujarArbólTalado(15 + i * 82.6, 320, 35, 25) # Llamada a la función crearArbóles para crear el arból grande
    arból_talado_2 = dibujarArbólTalado(50 + i * 82.5, 330, 25, 15) # Llamada a la función crearArbóles para crear el arból del medio
    arból_talado_3 = dibujarArbólTalado(70 + i * 82, 318, 20, 10) # Llamada a la función crearArbóles para crear el arból pequeño izquierdo
    arbóles_talados.agregar(arból_talado_1, arból_talado_2, arból_talado_3) # Agrega los arbóles al grupo de arbóles

## Grupo 5 - Escena de bosque talado
### Grupo para escena de bosque talado
escenaDeBosqueTalado = Group()

### Propiedad de visible para escena de bosque talado
escenaDeBosqueTalado.visible = False

# Para Escena 6 - Río siendo afectado por el hombre #
## Funciones y variables para recrear la escena del río cuando está siendo contaminado ##

### Grupo de fondo de ciudad
fondo_de_río = Group()
papelera = Group()

### Propiedad visible para fondo de escena de río
fondo_de_río.visible = False

def papeles(x,y):
        papel = Group(Polygon(x,y,x-20,y+20,x-40,y+40,x-40,y+60,x-35,y+60,x-20,y+80,x,y+80,x+20,y+70,x+40,y+40,x+40,y+10, relleno='marfil',borde='negro'), 
                    Polygon(x+35,y+60,x+10,y+60,x,y+45,x+10,y+40,x+35,y+50, relleno='marfil',borde='negro'),  
                    Line(x-20,y+20,x,y+30), Polygon(x-20,y+80,x+5,y+30,x-5,y+40,x-35,y+60, relleno='marfil', borde='negro'), Line(x,y+30,x+10,y+25))
        papel.ancho = 10
        papel.altura = 10
        papel.centroX = x
        papel.centroY = y
        papelera.agregar(papel)
        
### Para fondo de escenas de río
def crear_edificio_de_fondo(x, h=140, o=60):
    fondo_de_río.agregar(Rect(x, h + 10, 50, 400 - h))
    for cx in range(3):
        for cy in range(12):
            fondo_de_río.agregar(Rect(x + 16.5 * cx, (h + 10) + 15 * cy, 17, 15, relleno=gradiente('azulClaro', rgb(224-cy, 255, 255-cx), inicio='inferior-izquierda'), borde='negro', anchuraDeBorde=0.1, opacidad=o/1+cx*cy))

for i in range(3):
    crear_edificio_de_fondo(0+100*i, 140-30*i)
    crear_edificio_de_fondo(50+100*i, 130-10*i)
    crear_edificio_de_fondo(300+50*i, 140-25*i)

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
tablero = Group(Rect(60,60,280,140,relleno='blancoFantasma',borde='plateado',anchuraDeBorde=5),
                Label('1. Prohibir la tala', 240, 90, tamaño=12),
                Label('2. Limpiar los ríos', 240, 110, tamaño=12),
                Label('3. Promover el reciclaje', 240, 130, tamaño=12),
                Label('4. Cuidar los bosques', 240, 150, tamaño=12),
                Label('5. Tener conciencia', 240, 170, tamaño=12))

tablero.visible = False

# Grupo 8 - Escena de reunión

### Burbuja de texto
burbujaDeTexto = Group(
    Oval(200, 160, 175, 90, relleno='blanco', borde='negro'),
    Line(400-220, 205, 400-240, 225),
    Line(400-230, 205, 400-240, 225),
    Label('¡Ahora veremos las',200,145),
    Label('soluciones escogidas',200,160),
    Label('por el equipo!',200,175))

burbujaDeTexto.inferior = 260
burbujaDeTexto.centroX = 260

burbujaDeTexto.visible = False

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
tarroDeBasura_1 = Polygon(200,200,210,195,230,200,230,245,220,250, 220,210,220,250,200,240, relleno=gradient('oro', 'amarillo', 'gris', inicio='izquierda'), visible=False)
tarroDeBasura_2 = Polygon(200,200,210,195,230,200,230,245,220,250, 220,210,220,250,200,240, relleno=gradient('carmesí', 'rojo', 'gris', inicio='izquierda'), visible=False)
tarroDeBasura_3 = Polygon(200,200,210,195,230,200,230,245,220,250, 220,210,220,250,200,240, relleno=gradient('verde', 'verdeBosque', 'gris', inicio='izquierda'), visible=False)
tarroDeBasura_1.centroX, tarroDeBasura_2.centroX, tarroDeBasura_3.centroX = 120, 160, 200
tarroDeBasura_1.centroY, tarroDeBasura_2.centroY, tarroDeBasura_3.centroY = 280, 280, 280
tarroDeBasura_1.altura, tarroDeBasura_2.altura, tarroDeBasura_3.altura = 30, 30, 30

# Grupo 10 - Río limpio
escenaDeRíoLimpio = Group()

# Para Escena 11 - Escena apertura de tienda sostenible #
## Funciones y variables para recrear la escena de la apertura de la tienda sostenible de los ambieentalistas ##

### Para dibujar

# Grupo 11 - Escena tienda sostenible
escenaDeTienda = Group()

# Para Escena 12 - Salvar el bosque #
## Funciones y variables para recrear la escena de la campaña para prohibir la tala excesiva de arbóles ##

### Variable para cartél
cartél_bosque = Group(Rect(45, 240, 300, 40, relleno='caqui', borde='negro'), 
                    Rect(60, 279, 10, 26, relleno='tierra', borde='negro'),
                    Rect(320, 279, 10, 26, relleno='tierra', borde='negro'),
                    Label('¡¡Protege el bosque!!', 200, 260, tamaño=20))

### Propiedad visible para el cartél
cartél_bosque.visible = False

### Para dibujar personas
def dibujarPersonaDePalo(x=200,y=200, ancho=0, altura=0):
    palo = Group(Line(x, y + 25, x - 15, y + 35), Line(x, y + 25, x + 15, y + 35), Circle(x, y, 15),
        Line(x, y, x, y + 50), Line(x, y + 50, x - 10, y + 75), Line(x, y + 50, x + 10, y + 75))
    palo.ancho -= ancho
    palo.altura -= altura
    return palo

# Grupo 12 - Escena de salvar el bosque
escenaDeSalvaciónDeBosque = Group()

escenaDeSalvaciónDeBosque.visible = False

# Para Escena 13 - Escena de reciclaje #
## Funciones y variables para recrear la escena de reciclaje del grupo ambientalista ##

# Grupo 13 - Escena de reciclaje
escenaDeReciclaje = Group()

# Para Escena 14 - Escena de resumén #
## Variables para recrear la escena de reciclaje del resumén ##

r1 = Label('¡Hemos finalizado la parte visual!',200,100, tamaño=16, negrito=True, visible=False)
r2 = Label('Continuamos con la sección interactiva que promueve',200,150, tamaño=12, negrito=True, visible=False)
r3 = Label('la plantación y el reciclaje',200,165, tamaño=12, negrito=True, visible=False)
r4 = Label('¡Disfruta y promueve el cuidado al medio ambiente!',200,250, tamaño=12, negrito=True, visible=False)
r5 = Label('¡No olvides compartir lo que aprendiste aquí!',200,300, tamaño=14, negrito=True, visible=False)

# Grupo 14 - Escena de resumén
# Grupo con los elementos de la escena final
escenaDeResumén = Group(r1, r2, r3, r4, r5)

escenaDeResumén.visible = False

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
    indicaciones = Group(Label('¡Mueva la semilla hacia el macetero!', 200, 43), Label('¡Plante la semilla en la plantadera y rieguela hacerla crecer!', 200,350))
    return indicaciones

# Grupo 15 - Mini juego I - ¡¡Planta!!
### Grupo de escena interactiva de minijuego 1
minijuegoEscena_1 = Group()

### Propiedad visible de escena interactiva de minijuego 1
minijuegoEscena_1.visible = False

# Para Escena Interactiva 2 - ¡Recicle bucle!
## Variables y funciones correspondientes a la escena interactiva 2

### Variables de juego 2
suelo_de_juego = Rect(0,310,400,90, relleno='grisTurbio')
papel_juego = Rect(165, 20, 70, 80, relleno='nieve', rotarAngulo = -30, borde='negro', anchuraDeBorde=0.3, visible=False)
cartón = Group(Polygon(165,20,165,100,235,100,235,20, relleno='marronCuero', borde='negro', anchuraDeBorde=0.3, rotarAngulo=-30),
    Polygon(230,22,160,21,160,35,225-30,35,215-15,101,230,101, relleno='tierra', borde='negro', anchuraDeBorde=0.3, rotarAngulo=-30))
cartón.visible = False
cristal = Rect(165, 20, 70, 80, relleno='azur', rotarAngulo = -30, visible=False)
botellaDeVidrio = Polygon(172,302,176,294,186,300,180,309,172,302,relleno='verde',borde='verdeOscuro',visible=False)
botellaDeVidrio.ancho = 40
botellaDeVidrio.altura = 35
bolsaPlastica = Group(Rect(32,323,14,15,relleno='azur',borde='nieve',anchuraDeBorde=1),
                    Line(32,323,47,337,relleno='rojo'),
                    Line(30,337,47,337,relleno='azur',anchuraDeLinea=3))
bolsaPlastica.ancho = 40
bolsaPlastica.altura = 30
bolsaPlastica.visible = False
botellaPlastica = Group(
    Polygon(220,45,164,45,168,52,168,56,138,95,134,101,135,112,134,144,139,150,134,155,134,355,146,378,167,385,181,384,197,382,208,384,218,385,223,383,230,382,235,380,240,376,244,372,247,364,251,352,251,155,246,151,251,146,251,106,249,102,247,99,217,56,217,52,relleno='azur',borde='negro'),
    Polygon(220,44,164,44,164,19,176,15,207,15,220,19))
botellaPlastica.ancho = 20
botellaPlastica.altura = 40
botellaPlastica.visible = False
bateria = Group(Rect(30,264,13,12,relleno='gris',borde='grisOscuro',visible=True),
            Line(28,275,45,275,relleno='azulReal',anchuraDeLinea=1,visible=True))
bateria.ancho = 30
bateria.altura = 50
bateria.visible = False
barra = Line(155, 20, 170, 80, relleno='gainsboro', anchuraDeLínea=12, visible=False)
lata = Rect(165, 20, 50, 30, relleno='plateado', borde='negro', rotarAngulo = -30, visible=False)

app.basura = [papel_juego, cartón, cristal, botellaDeVidrio, bolsaPlastica, botellaPlastica, bateria, barra, lata]
app.esBasura = False
app.correcto = 'Iniciando'
app.objeto = Group()
app.objeto.visible = False
app.elección = -1

app.textos = Grupo()

def dibujarCaneca(cx=200, cy=200, color_base='rojo', color_secundario='ladrillo', texto='None'):
    caneca = Group(Polygon(cx-170,cy+100,cx-160,cy+200,cx-80,cy+200,cx-70,cy+100,relleno=color_base),
    Rect(cx-173,cy+90,105,10,relleno=color_secundario),
    Polygon(cx-165,cy+90,cx-160,cy+60,cx-80,cy+60,cx-75,cy+90,relleno='negro',borde=color_base,anchuraDeBorde=5),
    Circle(cx-120,cy+140,30,relleno='blanco'))
    app.textos.agregar(Label(texto,cx-120,cy+140,tamaño=10,negrito=True))
    caneca.ancho -= 20
    caneca.visible = False
    caneca.altura -= 20
    return caneca

canecaDeVidrios = dibujarCaneca(170,160,'verde', 'verdeBosque', 'Vidrio')
canecaDePapel =  dibujarCaneca(270,160,'oro', 'amarillo','Papel')
canecaDeMetales = dibujarCaneca(370,160,'azulGandul', 'azualAciano','Metal')
canecaDePlastico = dibujarCaneca(471,160,'salmon', 'salmonOscuro','Plastico')
texto = Label('¡¡Recicle bucle, consiste en ordenar por tipos!!',200,210,tamaño=14, negrito=True)

def ruleta():
    for i in range(len(app.basura)):
        if app.esBasura == False and app.elección < 8:
            app.elección += 1
            app.objeto.agregar(app.basura[app.elección])
            app.objeto.visible = True
            app.esBasura = True

# Grupo 16 - Mini juego II - Recicle bucle!
### Grupo de escena interactiva de minijuego 2
minijuegoEscena_2 = Group(suelo_de_juego, canecaDeMetales, canecaDePapel, canecaDeVidrios, canecaDePlastico, app.objeto, texto, app.textos)
### Propiedad visible de escena interactiva de minijuego 3
minijuegoEscena_2.visible = False

# Para Escena Final - Escena final #
## Objetos de la escena final ##

### Variables para escena final
app.proximoÁngulo = 272.5
app.radio = 140
app.círculoLleno = False
app.i = -1
app.proximoÁngulo2 = 321.5
app.radio2 = -140
app.i2 = -1

# Evento para cambiar entre escenas de una a una
def enTeclaPresionada(tecla):
    if tecla == 'espacio' and app.estado == 'Apagada':
        app.estado = 'Encendiendo'
        print('>> Encendiendo app...')
    elif tecla == 'arriba' and app.estado == 'En escena 0':
        titulo.valor = '¡El ambiente está en peligro y nosotros'
        subtitulo.valor = 'debemos luchar por protegerlo!'
        indicacion.valor = 'Presione derecha para la escena siguiente'
        app.estado = 'En escena 0.5'
        print('>> Tenga cuidado con la tecla derecha, ya que no puede regresarse')
    if tecla == 'derecha':
        if app.cartel_estado == 'Arriba':
            app.valoresDeTexto_up += 3
            app.valoresDeTexto_mid += 3
            app.valoresDeTexto_down += 3
        if app.estado == 'En escena 0.5':
            app.fondo = 'azulCielo'
            escenaDeCiudad.visible, app.estado, suelo.relleno = True, 'En escena 1 - Ciudad', gradient('gris', 'gainsboro', inicio='inferior')
            escenaDeCiudad.agregar(sol, nube_1, nube_2), introducción.vaciar()
            print('>> Presiona espacio y mira los cambios en el sol')
            print('>> Evite presionar la tecla ´ctrl´ o romperá el sistema')
            app.cartel_estado = 'Abajo'
        elif app.estado == 'En escena 1 - Ciudad':
            sol.relleno = gradient('caqui', 'naranja', 'amarillo')
            app.fondo = gradient('azulCadete', 'azulCielo', 'azulCieloProfundo', inicio='superior')
            escenaDeCiudad.vaciar(), escenaDeBosqueVerde.agregar(sol, nube_1, nube_2, suelo, camino, fondo_montañoso, arbóles)
            escenaDeBosqueVerde.visible, app.estado, suelo.relleno = True, 'Escena 2 - Bosque', gradient('cespedVerde', 'verdeBosque', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'nieve', 'nieve'
            app.cartel_estado = 'Abajo'
        elif app.estado == 'Escena 2 - Bosque': 
            escenaDeBosqueVerde.vaciar(), basuraDeCalle.vaciar(), escenaDeBosqueQuemandose.agregar(sol, nube_1, nube_2, suelo, camino, fondo_montañoso, cenizas, arbóles_quemados)
            escenaDeBosqueQuemandose.visible, app.estado, suelo.relleno = True, 'En escena de bosque deteriorandose', gradient('verdeBosque', 'grisClaro', 'salmonClaro', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'gainsboro', 'gainsboro'
            app.cartel_estado = 'Abajo'
        elif app.estado == 'En escena de bosque deteriorandose': 
            app.fondo = gradient('gris', 'azulCielo', 'azulCieloProfundo', inicio='superior')
            escenaDeBosqueQuemandose.vaciar(), escenaDeBosqueSeco.agregar(sol, nube_1, nube_2, suelo, camino, fondo_montañoso, arbóles_secos)
            escenaDeBosqueSeco.visible, app.estado, suelo.relleno = True, 'En escena de bosque seco', gradient('gris', 'grisClaro', 'salmonClaro', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'grisClaro', 'grisClaro'
            app.cartel_estado = 'Abajo'
        elif app.estado == 'En escena de bosque seco': 
            app.fondo = gradient('gris', 'azulCielo', 'azulCieloProfundo', inicio='superior')
            escenaDeBosqueSeco.vaciar(), escenaDeBosqueTalado.agregar(sol, nube_1, nube_2, suelo, camino, fondo_montañoso, arbóles_talados)
            escenaDeBosqueTalado.visible, app.estado, suelo.relleno = True, 'En escena de bosque talado', gradient('gris', 'grisClaro', 'salmonClaro', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'grisClaro', 'grisClaro'
            app.cartel_estado = 'Abajo'
        elif app.estado == 'En escena de bosque talado': 
            app.fondo = gradient('plateado', 'azulCielo', 'azulCieloProfundo', inicio='superior')
            escenaDeBosqueTalado.vaciar(), escenaDeRíoEnsuciado.agregar(fondo_de_río, sol, nube_1, nube_2, suelo, banca, río, ola, papelera)
            escenaDeRíoEnsuciado.visible, app.estado, suelo.relleno = True, 'En escena de río ensuciado', gradient('gris', 'grisClaro', 'gainsboro', inicio='inferior')
            nube_1.relleno, nube_2.relleno, app.dirección = 'grisClaro', 'grisClaro', 0.3
            app.cartel_estado = 'Abajo'
            print('>> Presiona el lienzo y mire como se crea papel en el suelo y en el río')
            from rjasDEciudad import dibujaReja
            dibujaReja()
        elif app.estado == 'En escena de río ensuciado': 
            escenaDeRíoEnsuciado.vaciar(), escenaDeRíoContaminado.agregar(fondo_de_río, sol, nube_1, nube_2, suelo, banca, río, ola, papelera)
            escenaDeRíoContaminado.visible, app.estado, suelo.relleno = True, 'En escena de río contaminado', gradient('gris', 'grisClaro', 'gainsboro', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'grisClaro', 'grisClaro'
            app.cartel_estado = 'Abajo'
            from pez import fotoDePezMuerto
        elif app.estado == 'En escena de río contaminado': 
            from rótulosDeCartél import borrarCartél # Módulo de cartél de escenas
            from rjasDEciudad import dibujaReja
            from pez import vaciar
            vaciar()
            dibujaReja(True)
            borrarCartél()
            escenaDeRíoContaminado.vaciar(), escenaDeReunión.agregar(tablero, suelo, dibujarPersonaDePalo(200,270), burbujaDeTexto)
            escenaDeReunión.visible, app.estado, suelo.relleno, app.fondo = True, 'En escena de reunión', 'azulCadete', gradient('azulCadete', 'azulMediaNoche')
            nube_1.relleno, nube_2.relleno = 'grisClaro', 'grisClaro'
            from logo_no_más import fotoDeProhibirTalaDeArboles
        elif app.estado == 'En escena de reunión': 
            app.fondo = gradient('plateado', 'azulCielo', 'azulCieloProfundo', inicio='superior')
            from rótulosDeCartél import devolverCartél # Módulo de cartél de escenas
            from logo_no_más import modulo_de_logo 
            escenaDeReunión.vaciar(), escenaDeJardín.agregar(sol, nube_1, nube_2, suelo, fondo_montañoso)
            app.fondo, carretilla_de_arena.inferior = 'azulCielo', 360
            escenaDeJardín.visible, app.estado, suelo.relleno = True, 'En escena de jardín', gradient('verde', 'verdeBosque', 'azulCadete', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'grisClaro', 'grisClaro'
            app.cartel_estado = 'Abajo'
            devolverCartél()
            modulo_de_logo()
            escenaDeJardín.agregar(arbustos, carretilla_de_arena, plantaderas, brotes)
            from vallasDeJardín import dibujarValla
            dibujarValla()
        elif app.estado == 'En escena de jardín': 
            app.fondo = gradient('gainsboro', 'azulCielo', 'azulCieloProfundo', inicio='superior')
            escenaDeJardín.vaciar(), escenaDeRíoLimpio.agregar(fondo_de_río, sol, nube_1, nube_2, suelo, banca, río, ola, tarroDeBasura_1, tarroDeBasura_2, tarroDeBasura_3)
            escenaDeRíoLimpio.visible, app.estado, suelo.relleno = True, 'En escena de río límpio', gradient('gris', 'grisClaro', 'gainsboro', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'grisClaro', 'grisClaro'
            app.cartel_estado = 'Abajo'
            from rjasDEciudad import dibujaReja
            dibujaReja()
            from vallasDeJardín import quitarVallas
            quitarVallas()
        elif app.estado == 'En escena de río límpio': 
            app.fondo = gradient('azulCadete', 'azulCielo', 'azulCieloProfundo', inicio='superior')
            from tienda_eco import tienda
            tienda()
            from rjasDEciudad import dibujaReja
            dibujaReja(True)
            from rótulosDeCartél import front
            front()
            escenaDeRíoLimpio.vaciar(), escenaDeTienda.agregar(sol, nube_1, nube_2, suelo, Rect(-20,320,440,80, relleno='grisOscuro', borde='gris', anchuraDeBorde=5), 
                                                            Line(0,360,410,360, relleno=gradient('negro', 'grisOscuro', 'negro'), anchuraDeLinea=4, guion=(5,6)))
            escenaDeTienda.visible, app.estado, suelo.relleno = True, 'En escena de tienda', gradient('gris', 'blanco', 'nieve', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'gainsboro', 'gainsboro'
            app.cartel_estado = 'Abajo'
            from camion import camión
        elif app.estado == 'En escena de tienda': 
            app.fondo = gradient('azulCielo', 'azulCieloProfundo', inicio='superior')
            escenaDeTienda.vaciar(), escenaDeSalvaciónDeBosque.agregar(sol, nube_1, nube_2, fondo_montañoso, suelo, arbóles, cartél_bosque)
            escenaDeSalvaciónDeBosque.visible, app.estado, suelo.relleno = True, 'En escena de campaña', gradient('gris', 'blanco', 'nieve', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'gainsboro', 'gainsboro'
            app.cartel_estado = 'Abajo'
            from camion import modulo_de_camion
            modulo_de_camion()
            from tienda_eco import eliminar_tienda
            eliminar_tienda()
            ### Bucle para dibujar personas y agregarlas al grupo
            for i in range(2):
                for e in range(3):
                    escenaDeSalvaciónDeBosque.agregar(dibujarPersonaDePalo(130 + 140*i, 280),
                            dibujarPersonaDePalo(60 + 140*e, 280, 2, 7))
        elif app.estado == 'En escena de campaña': 
            app.fondo = 'azulCieloProfundo'
            escenaDeSalvaciónDeBosque.vaciar(), escenaDeReciclaje.agregar(sol, nube_1, nube_2, fondo_montañoso, suelo, arbóles)
            escenaDeReciclaje.visible, app.estado, suelo.relleno = True, 'En escena de reciclaje', gradient('verde', 'verdeBosque', 'verde', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'nieve', 'nieve'
            app.cartel_estado = 'Abajo'
        elif app.estado == 'En escena de reciclaje': 
            app.fondo = 'blanco'
            escenaDeReciclaje.vaciar()
            app.estado = 'En escena de resumén I'
            escenaDeResumén.visible = True
            app.textoEnPantalla = False
            from rótulosDeCartél import borrarCartél
            borrarCartél()
        elif app.estado == 'En escena de resumén I': 
            app.grupo.vaciar()
            app.fondo = 'azulCielo'
            minijuegoEscena_1.agregar(sol, nube_1, nube_2, fondo_montañoso, suelo, macetero, semilla, dibujar_indicaciones())
            minijuegoEscena_1.visible, app.estado, suelo.relleno = True, 'En escena de minijuego I', gradient('verde', 'verdeBosque', 'verde', inicio='inferior')
            nube_1.relleno, nube_2.relleno = 'nieve', 'nieve'
        elif app.estado == 'En escena de minijuego I': 
            minijuegoEscena_1.vaciar()
            app.estado = 'En escena de minijuego II'
            app.fondo = 'marronCuero'
            minijuegoEscena_2.visible = True
        elif app.estado == 'En escena de minijuego II':
            minijuegoEscena_2.vaciar()
            app.estado = 'En escena de final'

sol.g = 255

# Evento especial
def enTeclaRetenida(teclas):
    if 'espacio' in teclas and app.estado == 'En escena 1 - Ciudad':
        if basuraDeCalle.opacidad < 100:
            basuraDeCalle.opacidad += 1
            sol.g -= 1
            sol.relleno = gradient('caqui', rgb(255, sol.g, 0), 'oro')
    if 'arriba' in teclas:
        from rótulosDeCartél import subirCartél # Módulo de cartél de escenas
        from rótulosDeCartél import vaciarRótulo # Módulo de cartél de escenas
        subirCartél()
        vaciarRótulo()
        app.cartel_estado = 'Arriba'

# Evento para interactuar en las escenas
## enRatónArrastrado
def enRatónArrastrado(ratónX, ratónY):
    # Escena Interactiva 1
    if app.estado == 'En escena de minijuego I':
        if semilla.contiene(ratónX, ratónY):
            semilla.centroX = ratónX
            semilla.centroY = ratónY
        elif agua.contiene(ratónX, ratónY):
            agua.centroX = ratónX
            agua.centroY = ratónY
        if agua.tocaFigura(arbol_DE):
            if arbol_DE.altura < 160: 
                arbol_DE.inferior -= 2
                arbol_DE.altura += 5
                arbol_DE.ancho += 2
    
    elif app.estado == 'En escena de minijuego II':
        ruleta()
        if app.objeto.contiene(ratónX, ratónY):
            app.objeto.centroX = ratónX
            app.objeto.centroY = ratónY
            if app.elección == 0 or app.elección == 1:
                if app.objeto.tocaFigura(canecaDePapel):
                    app.objeto.vaciar()
                    app.correcto = True
                    app.esBasura = False
                else:
                    app.correcto = False
            elif app.elección == 2 or app.elección == 3:
                if app.objeto.tocaFigura(canecaDeVidrios):
                    app.objeto.vaciar()
                    app.correcto = True
                    app.esBasura = False
                else:
                    app.correcto = False
            elif app.elección == 4 or app.elección == 5:
                if app.objeto.tocaFigura(canecaDePlastico):
                    app.objeto.vaciar()
                    app.correcto = True
                    app.esBasura = False
                else:
                    app.correcto = False
            elif app.elección == 6 or app.elección == 7 or app.elección == 8:
                if app.objeto.tocaFigura(canecaDeMetales):
                    app.objeto.vaciar()
                    app.correcto = True
                    app.esBasura = False
                else:
                    app.correcto = False
            else:
                app.correcto = False

            palabrasDeAnimo = ['¡Muy bien!', '¡Sigue así!', '¡En hora buena!', '¡Sabés lo que haces!', '¡Recicle bucle!', '¿Estás haciendo trampa?', '¡¡Perfecto!!']
            if app.correcto == False:
                texto.valor = '¡Mueva el objeto al grupo correcto!'
                texto.relleno = 'amarillo'
            if app.correcto == True:
                i = randrange(0, 7)
                texto.valor = palabrasDeAnimo[i]
                texto.relleno = 'cespedVerde'

## enRatónSoltado
def enRatónSoltado(ratónX, ratónY):
    # Escena Interactiva 1
    if app.estado == 'En escena de minijuego I':
        if semilla.tocaFigura(macetero):
            minijuegoEscena_1.quitar(semilla)
            minijuegoEscena_1.agregar(arbol_DE)
        if arbol_DE in minijuegoEscena_1:
           minijuegoEscena_1.agregar(agua)
    elif app.estado == 'En escena de río ensuciado' or app.estado == 'En escena de río contaminado':
        if ratónY > 260:
            papeles(ratónX, ratónY)
    elif app.estado == 'En escena de minijuego II':
        minijuegoEscena_1.vaciar()

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
    if app.estado == 'Encendiendo':
        cubierta_superior.centroY -= 5
        cubierta_inferior.centroY += 5
        if cubierta_superior.inferior < 0 and cubierta_inferior.superior > 400:
            app.estado = 'En escena 0'
            print('>> ¡¡App Encendida!')

    # Textos de escenas
    if app.cartel_estado == 'Abajo':
        from rótulosDeCartél import bajarCartél # Módulo de cartél de escenas
        from rótulosDeCartél import llenarRótulos # Módulo de cartél de escenas
        from rótulosDeCartél import mensajes # Módulo de cartél de escenas
        from rótulosDeCartél import texto_arriba # Módulo de cartél de escenas
        from rótulosDeCartél import texto_en_medio # Módulo de cartél de escenas
        from rótulosDeCartél import texto_abajo # Módulo de cartél de escenas
        bajarCartél()
        llenarRótulos(mensajes[app.valoresDeTexto_up], texto_arriba)
        llenarRótulos(mensajes[app.valoresDeTexto_mid], texto_en_medio)
        llenarRótulos(mensajes[app.valoresDeTexto_down], texto_abajo)    

    # Escena 1
    if app.estado == 'En escena 1 - Ciudad':
        moverCarro(carro_1, 440, 10, -700) # Mover carro azul
        moverCarro(carro_2, 540, 15, -600) # Mover carro violeta
        moverCarro(carro_3, 640, 5, -500) # Mover carro gris
        moverCarro(carro_4, -440, -10, 500) # Mover carro verde
        moverCarro(carro_5, -540, -15, 600) # Mover carro rojo
        moverCarro(carro_6, -640, -5, 700) # Mover carro naranja
    
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