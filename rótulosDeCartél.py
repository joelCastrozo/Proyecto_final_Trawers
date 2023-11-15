from cmu_graphics import *

cadenasDeCartél = Group()

def crearCadenaDeCartél(x, y):
    uniónDeCadenaDeCartél = Group(Circle(172,200,5, relleno='blanco', borde='negro'), 
                            Circle(187,200,5, relleno='blanco', borde='negro'),
                            Rect(172,195,15,10, relleno='blanco', borde='negro'),
                            Rect(172,197,15,6, relleno='blanco'))
                            
    baseDeCadenaDeCartél = Group(Circle(160,200,10, relleno='blanco', borde='negro'),
                            Circle(170,200,10, relleno='blanco', borde='negro'), 
                            Rect(157,190,15,20, relleno='blanco', borde='negro'), Rect(157,192,15,16, relleno='blanco'), 
                            Circle(160,200,4, relleno=app.fondo, borde='negro'), 
                            Circle(170,200,4, relleno=app.fondo, borde='negro'), Rect(161,196,8,8, relleno=app.fondo, borde='negro'),
                            Rect(161,198,8,4, relleno=app.fondo))
                            
    uniónDeCadenaDeCartél.altura -= 2
    uniónDeCadenaDeCartél.ancho -= 6
    uniónDeCadenaDeCartél.izquierda -= 14.5
    uniónDeCadenaDeCartél.centroY += 10
    uniónDeCadenaDeCartél.rotarAngulo = 90
    uniónDeCadenaDeCartél.centroX, uniónDeCadenaDeCartél.centroY = x, y + 8.5
    baseDeCadenaDeCartél.rotarAngulo = 90
    baseDeCadenaDeCartél.altura -= 2
    baseDeCadenaDeCartél.ancho -= 7
    baseDeCadenaDeCartél.centroX, baseDeCadenaDeCartél.centroY = x, y
    
    cadenaDeCartel = Group(baseDeCadenaDeCartél, uniónDeCadenaDeCartél)
    return cadenaDeCartel

for i in range(7):
    cadena_izq = crearCadenaDeCartél(60, 0 + 17 * i)
    cadena_izq.ancho -= 3
    cadena_izq.altura -= 7
    cadena_der = crearCadenaDeCartél(340, 0 + 17 * i)
    cadena_der.ancho -= 3
    cadena_der.altura -= 7
    cadenasDeCartél.agregar(cadena_izq, cadena_der)
    cadena_izq.alFondo(), cadena_der.alFondo()

texto_arriba = Label('',200, 125, italica=True, tamaño=12)
texto_en_medio = Label('',200, 147.5, italica=True, tamaño=12)
texto_abajo = Label('',200, 170, italica=True, tamaño=12)

cartélDeRótulos = Group(cadenasDeCartél, 
                    Rect(45,107,310,80, relleno=gradiente('gris', 'gainsboro', inicio='superior'), borde='marron'),
                    texto_arriba, texto_en_medio, texto_abajo)

cartélDeRótulos.superior = -300

def bajarCartél():
    if cartélDeRótulos.centroY < 65:
        cartélDeRótulos.centroY += 9
        
def subirCartél():
    if cartélDeRótulos.centroY > -300:
        cartélDeRótulos.centroY -= 9

mensajes = ['La contaminación es la presencia de sustancias', 
            'o agentes fisicos en el medio ambiente. Estos',
            'causan daños y alteraciones en los ecosistemas.',
            'El calentamiento global es producido principalmente',
            'por la acumulación de gases de efecto invernadero',
            'en la atmósfera, como el dióxido de carbono (CO2).',
            'Y como resultado, algunas actividades humanas',
            'como la quema de combustibles fósiles u otros',
            'son los culpables de algunos incendios forestales.',
            'Al afectar significativamente, tiende a haber',
            'escacez de bosques y muchas veces el humo que',
            'se forma queda atrapado en el aire.',
            'La tala de arbóles es un acto destructivo que',
            'contribuye a la deforestación y al cambio climatico',
            'causando que el aire disminuya su pureza.',
            'Otra forma de contaminar, es lanzar desechos tóxicos',
            'o materias primas que son peligrosas tanto para las',
            'especies marinas como para la raza humana.',
            'Son perjudiciales ya que la sociedad se alimenta de',
            'algunas especies marinas y estas pueden estar',
            'infestadas de químicos u sustancias muy peligrosas.',
            '',
            '',
            '',
            'Una gran solución es, promover, sembrar y mantener',
            'brotes en huertas, para luego plantarlos en lugares',
            'afectados por los incendios y el calentamiento global.',
            'Otra puede ser, recoger los desechos y basura que se',
            'lanzan a diario en los ríos y mares, para promover la',
            'protección de los océanos y de la vida marina.',
            'Materialización de una recolección de la',
            'basura que invadía los ríos.',
            '¡¡Tú también puedes ayudar a promover esto!!',
            'Utilizar los recursos de tiendas sostenibles puede',
            'ser una buena opción, junto al uso de energía solar',
            'puede mejorar el uso excesivo de energía y químicos.',
            'Insentivar la protección de los bosques, para disminuir',
            'la tasa de mortalidad de los mismos, y promover',
            'la re-plantación de arbóles cuando sean talados.',
            'Crear campañas de reciclaje para promover las tres r:',
            '¡Reduce, Recicla, Reutiliza!',
            'Para disminuir el porcentaje de desechos en la Tierra.']

def vaciarRótulo():
    texto_arriba.valor = ''
    texto_abajo.valor = ''
    texto_en_medio.valor = ''

def llenarRótulos(textoADrenar, drenador):
    if cartélDeRótulos.centroY > 65:
        drenador.opacidad = 100
        if len(drenador.valor) < len(textoADrenar):
            for letra in textoADrenar:
                drenador.valor += letra
    elif drenador.opacidad > 0:
        drenador.opacidad -= 25

def front():
    cartélDeRótulos.alFrente()

def borrarCartél():
    cartélDeRótulos.centroY = 80000

def devolverCartél():
    cartélDeRótulos.centroY = -300

cmu_graphics.run()