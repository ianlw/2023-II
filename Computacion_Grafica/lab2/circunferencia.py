import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Función para dibujar un punto
def plot(ix, iy):
    glPointSize (1)
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
        plot(x0 + x, y0+ y)
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

def circulo8vias(x0, y0, r):
    plot (x0, y0 + r)
    plot (x0, y0 - r)
    plot (x0 + r, y0)
    plot (x0 - r, y0)
    x=1
    y = math.floor(math.sqrt(r * r - x * x) + 0.5)

    while x < y:
        plot (x0 + x, y0 + y)

        plot(x0 + x, y0 - y)
        plot(x0 - x, y0 + y)
        plot(x0 - x, y0 - y)
        plot(x0 + y, y0 + x)
        plot(x0 + y, y0 - x)
        plot(x0 - y, y0 + x)
        plot(x0 - y, y0 - x)

        x = x + 1
        y = math.floor(math.sqrt(r * r - x * x) + 0.5)
    
    if x == y: 
        plot(x0 + x, y0 + y)
        plot(x0 + x, y0 - y)
        plot(x0 - x, y0 + y)
        plot(x0 - x, y0 - y)

def circuloPtoMEdio(x0, y0, r):
    hm, x, y = 5/4 - r, 0, -r
    plot(x0, y0 +r )
    plot(x0, y0 - r)
    plot(x0 + r, y0)
    plot(x0 - r, y0)

    while x < - (y+1):
        if hm < 0:
            hm = hm + 2 * x + 3
        else:
            hm =hm +2 * x +2*y +5
            y= y+1
        x =x +1
        plot(x0 + x, y0 + y)
        plot(x0 + x, y0 - y)
        plot(x0 - x, y0 + y)
        plot(x0 - x, y0 - y)
        plot(x0 + y, y0 + x)
        plot(x0 + y, y0 - x)
        plot(x0 - y, y0 + x)
        plot(x0 - y, y0 - x)

        
def DDA(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    # Valor absoluto de la pendiente
    if abs(dx) >= abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    # Incrementos en x e y
    x_increment = dx / steps
    y_increment = dy / steps

    x = x0
    y = y0

    for _ in range(steps + 1):
        plot(int(x), int(y))
        x += x_increment
        y += y_increment

def lineas(x0, y0, r, n_puntos):
    # Calcularemos el ángulo inicial de la primera linea
    angulo_inicial = 360 / n_puntos
    puntos_interseccion = []

    for i in range(n_puntos):
        # El ángulo incrementará a cada linea que se quiera dibujar 
        angulo = i * angulo_inicial
        # Calcularemos los puntos que intersectancon la circunferencia
        angulo_radianes = math.radians(angulo)
        x = x0 + r * math.cos(angulo_radianes)
        y = y0 + r * math.sin(angulo_radianes)

        #Dibujar las lineas desde el origen hasta un punto de la circunferencia
        DDA(x0, y0, int(x), int(y)) 
        puntos_interseccion.append((x, y))

    for a in range(n_puntos):
        # Conenctar las anteriores lineas para formar un polígono regular (dodecágono) 
        DDA(int(puntos_interseccion[a][0]), int(puntos_interseccion[a][1]), int(puntos_interseccion[(a + 1) % n_puntos][0]), int(puntos_interseccion[(a + 1) % n_puntos][1]))

# + Función para mostrar el gráfico
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    circuloPtoMEdio(250, 250, 150)
    glColor3f(0.5, 0.3, 0.9) 
    lineas(250, 250, 150, 12)
    glFlush()

def myinit():
    glClearColor(0.9058823529411765, 0.9215686274509803, 0.9568627450980393, 1.0)
    # glColor3f(1.0, 0.0, 0.0)
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
    myinit ()
    glutMainLoop ()

if __name__ == "__main__":
    main()
