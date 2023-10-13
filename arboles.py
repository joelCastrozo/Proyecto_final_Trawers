def crearArboles():
    Árbol = Group(
            Circle (210,172,15, relleno='verde'),
            Circle (229,209,15, relleno='verde'),
            Circle (195,209,15, relleno='verde'),
            Circle (190,190,25, relleno=gradiente('verde', 'limaVerde', inicio='izquierda')),
            Circle (230,190,25, relleno=gradiente('verde', 'limaVerde', inicio='derecha')),
            Rect (205,197,16,80, relleno=gradiente('tierra','granate', inicio='superior')),
            Óvalo(213,275,15,10, relleno='granate'),
            Circle (213,197,25, relleno='verdeBosque')
    )
crearArboles()
def crearArbolesTalados():
    Talado = Group(
             Óvalo(155,324,50,30, relleno='marronCuero'),
             Rect(130,277,50,50, relleno=gradiente('tierra','marronCuero', inicio='superior')),
             Óvalo(155,277,50,30, relleno=gradiente('marronArenoso','naranjaMarron','tierra'))
        )
crearArbolesTalados()
    