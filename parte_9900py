from cmu_graphics import *

app.fondo = gradiente('azulCieloProfundo','azulCieloClaro', inicio='superior')
suelo = Rect(0,260,400,140, relleno=gradiente('gris', 'gainsboro', inicio='inferior'))
sol = Estrella(200,0,100,100, relleno=gradiente('oro', 'amarillo', 'caqui'))

def dibujarEscenaDeCiudad():
    sol.alFrente()
    suelo.relleno = gradiente('gris', 'gainsboro', inicio='inferior')
    Rect(-20,320,440,80, relleno='grisOscuro', borde='gris', anchuraDeBorde=5)
    Linea(0,360,410,360, relleno=gradiente('negro', 'grisOscuro', 'negro'), anchuraDeLinea=4, guion=(5,6))
dibujarEscenaDeCiudad()

def crearAutos(color, partida, direccion):
    base = Rect(partida, direccion-30, 70, 30, relleno=color)
    capo = Rect(partida+10, direccion-50, 50, 20, relleno=color)
    ruedaIzq = Círculo(partida+15, direccion, 10)
    ruedaDer = Círculo(partida+55, direccion, 10)
    carro = Grupo(capo, base, ruedaIzq, ruedaDer)
    return carro
    
carro_2 = crearAutos(gradiente('azulReal', 'azulGandul', inicio='inferior'), 440, 320)
carro_3 = crearAutos(gradiente('violetaRojoMedio', 'violeta', inicio='inferior'), 540, 320)
carro_6 = crearAutos(gradiente('fucsia', 'rosado', inicio='inferior'), 690, 320)
carro_1 = crearAutos(gradiente('verde', 'limaVerde', inicio='inferior'), -40, 360)
carro_4 = crearAutos(gradiente('rojo', 'carmesi', inicio='inferior'), -140, 360)
carro_5 = crearAutos(gradiente('naranja', 'oro', inicio='inferior'), -240, 360)

def enPaso():
    sol.puntos += 1
    carro_1.centroX += 15
    carro_2.centroX -= 11
    carro_3.centroX -= 4
    carro_4.centroX += 8
    carro_5.centroX += 2
    carro_6.centroX -= 3

cmu_graphics.run()
