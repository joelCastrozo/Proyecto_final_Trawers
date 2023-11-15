from cmu_graphics import *
suelo = Rect(0,310,400,90, relleno='grisTurbio')

def dibujarCaneca(cx=200, cy=200, color_base='rojo', color_secundario='ladrillo', texto='None'):
    caneca = Group(Poligono(cx-170,cy+100,cx-160,cy+200,cx-80,cy+200,cx-70,cy+100,relleno=color_base),
    Rect(cx-173,cy+90,105,10,relleno=color_secundario),
    Poligono(cx-165,cy+90,cx-160,cy+60,cx-80,cy+60,cx-75,cy+90,relleno='negro',borde=color_base,anchuraDeBorde=5),
    Circulo(cx-120,cy+140,30,relleno='blanco'))
    Rotulo(texto,cx-120,cy+140,tamaño=10,negrito=True)
    caneca.ancho -= 20
    caneca.altura -= 20
    return caneca

canecaDeVidrios = dibujarCaneca(170,160,'verde', 'verdeBosque', 'Vidrio')
canecaDePapel =  dibujarCaneca(270,160,'oro', 'amarillo','Papel')
canecaDeMetales = dibujarCaneca(370,160,'azulGandul', 'azualAciano','Metal')
canecaDePlastico = dibujarCaneca(471,160,'salmon', 'salmonOscuro','Plastico')

papel = Rect(165, 20, 70, 80, relleno='nieve', rotarAngulo = -30, borde='negro', anchuraDeBorde=0.3, visible=False)
cartón = Rect(165, 20, 70, 80, relleno='marron', rotarAngulo = -30, visible=False)
cristal = Rect(165, 20, 70, 80, relleno='azur', rotarAngulo = -30, visible=False)
botellaDeVidrio = Rect(165, 20, 70, 80, relleno='verde', rotarAngulo = -30, visible=False)
bolsaPlastica = Rect(165, 20, 70, 80, relleno='negro', rotarAngulo = -30, visible=False)
botellaPlastica = Rect(165, 20, 70, 80, relleno='azur', rotarAngulo = -30, visible=False)
bateria = Rect(165, 20, 70, 80, relleno='azul', rotarAngulo = -30, visible=False)
barra = Rect(165, 20, 70, 80, relleno='gainsboro', rotarAngulo = -30, visible=False)
lata = Rect(165, 20, 70, 80, relleno='rojo', rotarAngulo = -30, visible=False)

texto = Rotulo('¡¡Recicle bucle, consiste en ordenar por tipos!!',200,210,tamaño=14, negrito=True)

app.basura = [papel, cartón, cristal, botellaDeVidrio, bolsaPlastica, botellaPlastica, bateria, barra, lata]
app.esBasura = False
app.correcto = 'Iniciando'
app.objeto = Grupo()
app.objeto.visible = False
app.elección = -1

def ruleta():
    for i in range(len(app.basura)):
        if app.esBasura == False and app.elección < 8:
            app.elección += 1
            app.objeto.agregar(app.basura[app.elección])
            app.objeto.visible = True
            app.esBasura = True

def enRatónArrastrado(x,y):
    ruleta()
    if app.objeto.contiene(x, y):
        app.objeto.centroX = x
        app.objeto.centroY = y
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
            i = rangoAleatorio(0, 7)
            texto.valor = palabrasDeAnimo[i]
            texto.relleno = 'cespedVerde'

def vaciarJuego():
    app.grupo.vaciar()

cmu_graphics.run()