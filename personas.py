app.fondo='azulCielo'

#persona=Grupo( 

def dibujarPersona(x,y,):
    Rect(50,300,10,40,relleno='salmonClaro')
    Rect(70,300,10,40,relleno='salmonClaro')
    Óvalo(65, 275, 50, 60)
    Arco(65,275,50,120,270,180,relleno='azul')
    Círculo(65, 200,15,relleno='salmonClaro')
    Circulo(75,200,8,relleno='blanco',borde='negro')
    Circulo(75,200,3)
    
    brazo= Línea(70, 240, 100, 260, relleno='salmonClaro', anchuraDeLínea=8)

dibujarPersona(80,200)