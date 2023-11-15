from cmu_graphics import *
vallaDeGranja = Group()

def dibujarValla(x, y):
    valla= Group(
        Rect(x,y-40,20,80, relleno=gradient(rgb(168, 157,104), rgb(121, 108,73))),
        Rect(x+100,y-40,20,80, relleno=gradient(rgb(168, 157,104), rgb(121, 108,73))),
        Rect(x+20,y-30,80,20, relleno=gradient(rgb(123, 110,79), rgb(139, 123,91))),
        Rect(x+20,y,80,20, relleno=gradient(rgb(123, 110,79), rgb(139, 123,91))))
    valla.ancho = 40
    valla.altura = 20
    return valla

for i in range(15):
    vallaDeGranja.agregar(dibujarValla(-55 + 30 * i,260))

def quitarVallas():
    vallaDeGranja.vaciar()
         
cmu_graphics.run()