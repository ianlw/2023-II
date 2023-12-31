import sympy as sp
import random
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from sympy.logic.inference import pl_true

lista_puntos = []

# Función para dibujar un punto
def plot(ix, iy):
    # glPointSize (1)
    glBegin (GL_POINTS)
    glVertex2i (ix, iy)
    glEnd()

# + Implementación del algoritmo de círculos
def circulo2vias(x0, y0, r):
    y=0
    plot(x0 + r, y0)
    plot(x0 - r, y0)

    for x in range(-r + 1, r):
        y = int(math.floor(math.sqrt(r * r - x * x) + 0.5))
        plot(x0 + x, y0 + y)
        plot(x0 + x, y0 - y)

def circulo4vias(x0, y0, r):
    y=0
    plot (x0, y0 + r)
    plot (x0, y0 - r)
    plot (x0 + r, y0)
    plot (x0 - r, y0)

    for x in range(1, r):
        y = math.floor (math.sqrt (r * r - x * x) + 0.5)
        plot (x0 + x, y0 + y)
        plot (x0 + x, y0 - y)
        plot(x0 - x, y0 + y)
        plot (x0 - x, y0 - y)

puntos8=[]
def circulo8vias(x0, y0, r):
    plot (x0, y0 + r)
    puntos8.append((x0, y0 + r))
    plot (x0, y0 - r)
    puntos8.append((x0, y0 - r))
    plot (x0 + r, y0)
    puntos8.append((x0 + r, y0))
    plot (x0 - r, y0)
    puntos8.append((x0 - r, y0))
    x=1
    y = math.floor(math.sqrt(r * r - x * x) + 0.5)

    while x < y:
        plot(x0 + x, y0 + y)
        puntos8.append((x0 + x, y0 + y))
        plot(x0 + x, y0 - y)
        puntos8.append((x0 + x, y0 - y))
        plot(x0 - x, y0 + y)
        puntos8.append((x0 - x, y0 + y))
        plot(x0 - x, y0 - y)
        puntos8.append((x0 - x, y0 - y))
        plot(x0 + y, y0 + x)
        puntos8.append((x0 + y, y0 + x))
        plot(x0 + y, y0 - x)
        puntos8.append((x0 + y, y0 - x))
        plot(x0 - y, y0 + x)
        puntos8.append((x0 - y, y0 + x))
        plot(x0 - y, y0 - x)
        puntos8.append((x0 - y, y0 - x))

        x = x + 1
        y = math.floor(math.sqrt(r * r - x * x) + 0.5)
    
    if x == y: 
        plot(x0 + x, y0 + y)
        puntos8.append((x0 + x, y0 + y))
        plot(x0 + x, y0 - y)
        puntos8.append((x0 + x, y0 - y))
        plot(x0 - x, y0 + y)
        puntos8.append((x0 - x, y0 + y))
        plot(x0 - x, y0 - y)
        puntos8.append((x0 - x, y0 - y))

puntosa = []
def circuloPtoMEdio(x0, y0, r):
    hm, x, y = 5/4 - r, 0, -r
    plot(x0, y0 +r )
    puntosa.append((x0,y0 + r))
    plot(x0, y0 - r)
    puntosa.append((x0,y0 - r))
    plot(x0 + r, y0)
    puntosa.append((x0 + r,y0))
    plot(x0 - r, y0)
    puntosa.append((x0 - r,y0))

    while x < - (y+1):
        if hm < 0:
            hm = hm + 2 * x + 3
        else:
            hm =hm +2 * x +2*y +5
            y= y+1
        x =x +1
        plot(x0 + x, y0 + y)
        puntosa.append((x0 + x, y0 + y))

        plot(x0 + x, y0 - y)
        puntosa.append((x0 + x, y0 - y))

        plot(x0 - x, y0 + y)
        puntosa.append((x0 - x, y0 + y))
        
        plot(x0 - x, y0 - y)
        puntosa.append((x0 - x, y0 - y))
        
        plot(x0 + y, y0 + x)
        puntosa.append((x0 + y, y0 + x))
        
        plot(x0 + y, y0 - x)
        puntosa.append((x0 + y, y0 - x))
        
        plot(x0 - y, y0 + x)
        puntosa.append((x0 - y, y0 + x))
        
        plot(x0 - y, y0 - x)
        puntosa.append((x0 - y, y0 - x))

        

# Función para mostrar el gráfico
def display_2vias():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize (1)
    glColor3f(0.5, 0.3, 0.9) 
    circulo2vias(150, 250, 100)
    circulo2vias(350, 250, 100)
    circulo2vias(250, 350, 100)
    circulo2vias(250, 150, 100)
    glFlush()

def display_4vias():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize (1)
    glColor3f(0.5, 0.3, 0.9) 
    circulo4vias(150, 250, 100)
    circulo4vias(350, 250, 100)
    circulo4vias(250, 350, 100)
    circulo4vias(250, 150, 100)
    glFlush()
def display_PtoMedio():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize (1)
    glColor3f(0.5, 0.3, 0.9) 
    circuloPtoMEdio(150, 250, 100)
    circuloPtoMEdio(350, 250, 100)
    circuloPtoMEdio(250, 350, 100)
    circuloPtoMEdio(250, 150, 100)
    glFlush()
def display_8vias():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize (1)
    glColor3f(0.5, 0.3, 0.9) 
    circulo8vias(150, 250, 100)
    circulo8vias(350, 250, 100)
    circulo8vias(250, 350, 100)
    circulo8vias(250, 150, 100)
    glFlush()
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize (1)
    puntos8.clear()
    glColor3f(0.5, 0.3, 0.9) 

    for _ in range(5):
        r = random.randint(50, 100)
        # Para asegurar que los círculos se dibujen dentro de los límites establecidos
        x0 = random.randint(r, 499-r)
        y0 = random.randint(r, 499-r)
        circulo8vias(x0, y0, r)

    # Lista para los puntos duplicado (intersección) 
    interseccion = []
    # Crear un conjunto para llevar un registro de los puntos únicos que hemos visto
    puntos_unicos = set()

    # Recorremos la lista de puntos
    for punto in puntos8:
        if punto in puntos_unicos:
            # Si los puntos se encuentran en el conjunto, se añaden a la lista intersección. Inicialmente no hay elementos en el conjunto 
            interseccion.append(punto)
        else:
            # Si no se encuentra el punto en el conjunto, entonces este se añade al mismo conjunto que se utilicará en la próxima iteración
            puntos_unicos.add(punto)
    print("Puntos de intersección de las lineas:", interseccion)

    # Pintar de negro los puntos de intersección
    glColor3f(0.05, 0.08, 0.1) 
    # glColor3f(0.0, 0.0, 0.0)
    glPointSize(4)

    # Recorrer la lista de duplicados para dibujarlos 
    for punto in interseccion:
        x, y = punto
        plot(x, y)
    glPointSize(1)
    glFlush()

def myinit():
    glClearColor(0.9058823529411765, 0.9215686274509803, 0.9568627450980393, 1.0)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    gluOrtho2D(0.0, 499.0, 0.0, 499.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow (b"Algoritmo de circulos")
    glutDisplayFunc (display)
    # glutDisplayFunc (display_2vias)
    # glutDisplayFunc (display_4vias)
    # glutDisplayFunc (display_8vias)
    # glutDisplayFunc (display_PtoMedio)
    myinit ()
    glutMainLoop ()

if __name__ == "__main__":
    main()
