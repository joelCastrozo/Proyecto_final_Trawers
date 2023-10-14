def dibujarCalle():
    # Estas variables se usan para dibujar la línea discontinua en la autopista.
    grueso = 10
    largo = 20
    y = 400
    brechaDeLínea = 50

    # Dibuje 10 guiones en el medio de la calle usando líneas con diferentes
    # grosores y longitudes. Después de dibujar cada línea, disminuye 'y'
    # por la brechaDeLínea, el grosor por 1, la longitud por 2 y la brechaDeLínea
    # por 5.
    ### (PISTA: Cada línea debe comenzar en la coordenada y de 'y', y terminar
    #          en la coordenada y de ('y'-largo).)
    ### Pon tu código aquí ###

def dibujarLámpara(x, inferior, ancho, dirección):
    # Dibuja una lámpara con los parámetros proporcionados.
    lámpara = Grupo(
        Línea(200, 300, 200, 200, relleno='grisTurbio', anchuraDeLínea=3)
        )

    if (dirección == 'derecha'):
        lámpara.agregar(
            Línea(200, 215, 210, 200, relleno='grisTurbio', anchuraDeLínea=3),
            Línea(210, 200, 220, 200, relleno='grisTurbio', anchuraDeLínea=3),
            Círculo(220, 205, 5, relleno='grisTurbio'),
            Polígono(220, 205, 205, 300, 235, 300,
                    relleno=gradiente('naranja', 'amarillo', inicio='superior'), opacidad=30),
            Óvalo(220, 300, 30, 10, relleno='amarillo', opacidad=30)
            )
    elif (dirección == 'izquierda'):
        lámpara.agregar(
            Línea(200, 215, 190, 200, relleno='grisTurbio', anchuraDeLínea=3),
            Línea(190, 200, 180, 200, relleno='grisTurbio', anchuraDeLínea=3),
            Círculo(180, 205, 5, relleno='grisTurbio'),
            Polígono(180, 205, 165, 300, 195, 300,
                    relleno=gradiente('naranja', 'amarillo', inicio='superior'), opacidad=30),
            Óvalo(180, 300, 30, 10, relleno='amarillo', opacidad=30)
            )

    lámpara.ancho = ancho
    lámpara.altura = 3 * ancho
    lámpara.centroX = x
    lámpara.inferior = inferior

def dibujarLámparas():
    # Estas variables se usan para dibujar las lámparas en la autopista.
    derechaX = 215
    izquierdaX = 185
    xBrecha = 35
    y = 150
    yBrecha = 60
    ancho = 10

    # Dibuje 5 lámparas en cada lado de la calle usando las variables
    # proporcionadas y la función auxiliar. En cada pasada por el loop, cambie
    # la derechaX y la izquierdaX por xBrecha, a 'y' por yBrecha y el ancho por 5.
    ### (PISTA: Las lámparas en el lado izquierdo de la calle deben mirar
    #          hacia la derecha, y las lámparas en el lado derecho deben
    #          mirar hacia la izquierda.)
    ### (PISTA: No use dos loops separados para las lámparas a la izquierda y
    #          las lámparas a la derecha. ¡Es más fácil dibujar ambos en una!)
    ### Pon tu código aquí ###

dibujarCalle()

# cubierto
Rect(0, 0, 400, 400, relleno=rgb(10, 5, 30), opacidad=20)

dibujarLámparas()