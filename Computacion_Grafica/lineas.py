from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import random

lista_puntos = []

# def DDA(x0, y0, x1, y1):
#     m= (y1 - y0) / (x1 - x0)
#     y = y0
#     for x in range(x0, x1 + 1):
#         plot(x, int(y))
#         lista_puntos.append((x, int(y)))
#         # print(x, int(y))
#         y=y+m

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

def swap(x, y):
    aux = x
    x = y
    y = aux

def Bresenham(x0, y0, x1, y1):
    dy = 0
    x, y, error = 0, 0, 0
    delta_x, delta_y = 0, 0
    steep = abs(y1 - y0 ) > abs(x1 - x0)

    if steep:
        swap(x0,y0)
        swap(x1,y1)

    if x0 > y1:
        swap(x0,y0)
        swap(x1,y1)

    if y0 > y1:
        dy = -1
    else:
        dy = 1

    delta_x =x1 - x0
    delta_y = abs(y1 - y0)
    y = y0
    error = 0

    for x in range(x0, x1 +1):
        if steep:
            plot(y,x)
        else: 
            plot(x, y)
        error = error + delta_y

        if 2* error >= delta_x:
            y = y + dy
            error = error - delta_x


def PtoMedio(x0, y0, x1, y1):
    delta_x = x1 - x0
    delta_y = y1 - y0
    dm = 2 * delta_y - delta_x
    dm_p1 =  2 * delta_y
    dm_p2 =  2 * delta_y - 2 * delta_x
    y = y0

    for x in range(x0, x1 + 1):
        plot(x,y)
        if dm <= 0:
            dm = dm + dm_p1
        else:
            dm = dm + dm_p2
            y = y + 1


def plot(ix, iy):
    glBegin(GL_POINTS)
    glVertex2i(ix, iy)
    glEnd()

def displays():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)

    # Limpiar la lista de puntos
    lista_puntos.clear()

    # Dibujar 5 líneas aleatorias
    for _ in range(5):
        x0 = random.randint(10, 150)
        y0 = random.randint(10, 150)
        x1 = random.randint(250, 499)
        y1 = random.randint(250, 499)
        DDA(x0, y0, x1, y1)

    # Lista para los puntos duplicado (intersección) 
    interseccion = []

    # Crear un conjunto para llevar un registro de los puntos únicos que hemos visto
    puntos_unicos = set()

    # Recorremos la lista de puntos
    for punto in lista_puntos:
        if punto in puntos_unicos:
            # Si los puntos se encuentran en el conjunto, se añaden a la lista intersección. Inicialmente no hay elementos en el conjunto 
            interseccion.append(punto)
        else:
            # Si no se encuentra el punto en el conjunto, entonces este se añade al mismo conjunto que se utilicará en la próxima iteración
            puntos_unicos.add(punto)
    print("Puntos de intersección de las lineas:", interseccion)

    # Pintar de negro los puntos de intersección
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(3)

    # Recorrer la lista de duplicados para dibujarlos 
    for punto in interseccion:
        x, y = punto
        plot(x, y)
    glPointSize(1)
    glFlush()

def display_Bresenham():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    Bresenham(100, 100, 450, 450)
    # Bresenham(100, 300, 200, 450)
    Bresenham(200, 450, 450, 450)
    glFlush()

def display_DDA():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    DDA(100, 100, 450, 450)
    DDA(100, 100, 200, 450)
    DDA(200, 450, 450, 450)
    glFlush()

def display_PtoMedio():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    PtoMedio(100, 100, 450, 450)
    PtoMedio(100, 100, 200, 450)
    PtoMedio(200, 450, 450, 450)
    glFlush()

def myinit():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPointSize(1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 499.0, 0.0, 499.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Algoritmo DDA")
    # glutDisplayFunc(displays)
    # glutDisplayFunc(display_Bresenham)
    # glutDisplayFunc(display_DDA)
    glutDisplayFunc(display_PtoMedio)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    main()
