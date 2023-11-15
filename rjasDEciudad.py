from cmu_graphics import *
rejas = Group()
def dibujaReja(vaciar=False):
    esVallaAlta = Verdadero
    for i in range(45):
        if vaciar == False:
            if esVallaAlta == Verdadero:
                _1 = Linea(10 * i, 180, 10 * i, 260, relleno = rgb(201, 199,201), anchuraDeLinea=1.5, inicioDeFlecha=True)
                _2 = Linea(10 * i, 195, 10 * i, 260, relleno = 'negro', anchuraDeLinea=1.5)
                esVallaAlta = Falso
                rejas.agregar(_1,_2)
            else:
                _3 = Linea(10 * i, 190, 10 * i, 260, relleno = rgb(201, 199,201), anchuraDeLinea=1.5, inicioDeFlecha=True)
                _4 = Linea(10 * i, 205, 10 * i, 260, relleno = 'negro', anchuraDeLinea=1.5)
                esVallaAlta = Verdadero
                rejas.agregar(_3,_4)
    sueloDeReja = Rect(0,255,400,5, relleno='gris')
    rejas.agregar(sueloDeReja)
    if vaciar == True:
        rejas.vaciar()

dibujaReja()
cmu_graphics.run()