# asientos
Rect(0, 150, 400, 120, relleno='marrónCuero', opacidad=80)
Línea(200, 148, 200, 230, relleno='tierra', anchuraDeLínea=400, opacidad=80, guión=(3, 37))

def dibujarAudiencia():
    # El código que en realidad dibuja todas estas figuras es correcto. Pero
    # las posiciones están todas mal y ¡solo 3 personas son dibujadas! Use
    # un loop para dibujar la fila de la audiencia inferior y superior y otro
    # loop para dibujar la fila del medio.
    ### Arregla tu código aquí ###
    cx = 200

    # fila superior
    cabeza1 = Círculo(cx, 150, 10, relleno='durazno')
    Arco(cx, 188, 40, 55, 270, 180, relleno='púrpuraMedio', opacidad=90)

    # fila inferior
    cabeza2 = Círculo(cx, 222, 14, relleno='durazno')
    Arco(cx, 270, 50, 65, 270, 180, relleno='marVerdeMedio', opacidad=90)

    cabezasMoviendoIzquierda.agregar(cabeza1, cabeza2)

    # fila del medio
    cabeza = Círculo(cx, 185, 12, relleno='durazno')
    Arco(cx, 228, 45, 60, 270, 180, relleno='tomate', opacidad=90)

    cabezasMoviendoDerecha.agregar(cabeza)

cabezasMoviendoIzquierda = Grupo()
cabezasMoviendoDerecha = Grupo()
dibujarAudiencia()