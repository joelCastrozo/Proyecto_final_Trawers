app.fondo = 'Durazno'

tablero = Rect(60,60,280,140,relleno='blancoFantasma',borde='plateado',anchuraDeBorde=5)
 
Lider = Grupo(
    Linea(200,180,200,240,anchuraDeLinea=40,relleno='azulMedio'),
    Linea(218,181,240,230,anchuraDeLinea=4),
    Ovalo(200,200,45,80,relleno='azulMedio'),
    Circulo(200,145,20),
    Linea(181,181,145,145,anchuraDeLinea=4))
    
integrantes = Grupo(
    Linea(50,325,50,380,relleno='indigo',anchuraDeLinea=40),
    Ovalo(50,340,45,80,relleno='indigo'),
    Circulo(50,285,20))