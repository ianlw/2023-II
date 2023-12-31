
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

# Lista para almacenar todos los puntos
aea = []

def DDA(x0, y0, x1, y1):
    m = (y1 - y0) / (x1 - x0)
    y = y0
    for x in range(x0, x1 + 1):
        plot(x, int(y))
        aea.append((x, int(y)))
        y = round(y + m, 2)

def swap(x, y):
    aux = x
    x = y
    y = aux

def Bresenham(x0, y0, x1, y1):
    dy = 0
    x, y, error = 0, 0, 0
    delta_x, delta_y = 0, 0
    steep = abs(y1 - y0) > abs(x1 - x0)

    if steep:
        swap(x0, y0)
        swap(x1, y1)

    if x0 > y1:
        swap(x0, y0)
        swap(x1, y1)

    if y0 > y1:
        dy = -1
    else:
        dy = 1

    delta_x = x1 - x0
    delta_y = abs(y1 - y0)
    y = y0
    error = 0

    for x in range(x0, x1 + 1):
        if steep:
            plot(y, x)
        else:
            plot(x, y)
        error = error + delta_y

        if 2 * error >= delta_x:
            y = y + dy
            error = error - delta_x

def PtoMedio(x0, y0, x1, y1):
    delta_x = x1 - x0
    delta_y = y1 - y0
    dm = 2 * delta_y - delta_x
    dm_p1 = 2 * delta_y
    dm_p2 = 2 * delta_y - 2 * delta_x
    y = y0

    for x in range(x0, x1 + 1):
        plot(x, y)
        if dm <= 0:
            dm = dm + dm_p1
        else:
            dm = dm + dm_p2
            y = y + 1

def plot(ix, iy):
    glBegin(GL_POINTS)
    glVertex2i(ix, iy)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    aea.clear()

    for _ in range(5):
        x0 = random.randint(10, 150)
        y0 = random.randint(10, 150)
        x1 = random.randint(250, 499)
        y1 = random.randint(250, 499)
        DDA(x0, y0, x1, y1)

    # Crear una lista para almacenar los puntos duplicados
    duplicates = []

    # Crear un conjunto para llevar un registro de los puntos únicos que hemos visto
    unique_points = set()

    for point in aea:
        if point in unique_points:
            # Si el punto ya se ha visto antes, agregarlo a la lista de duplicados
            duplicates.append(point)
        else:
            # Si es la primera vez que vemos el punto, agregarlo al conjunto de puntos únicos
            unique_points.add(point)

    # Cambiar el color a negro para dibujar los puntos duplicados
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(3)

    # Recorre la lista de duplicados y dibuja un punto en cada uno
    for point in duplicates:
        x, y = point
        plot(x, y)

    glFlush()

def myinit():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPointSize(3.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 499.0, 0.0, 499.0)

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, width, 0.0, height)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Algoritmo DDA")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    main()
