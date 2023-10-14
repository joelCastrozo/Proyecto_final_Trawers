from cmu_graphics import *

crearArboles(215, 190)
def crearArbolesTalados():
    Talado = Group(
             Óvalo(155,324,50,30, relleno='marronCuero'),
             Rect(130,277,50,50, relleno=gradiente('tierra','marronCuero', inicio='superior')),
             Óvalo(155,277,50,30, relleno=gradiente('marronArenoso','naranjaMarron','tierra'))
        )
crearArbolesTalados()
cmu_graphics.run()