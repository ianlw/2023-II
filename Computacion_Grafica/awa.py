from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

Xmin, Ymin, Xmax, Ymax = 3, 3, 15,12
x0, y0, x1, y1 = 7, 4, 12, 10

def comparacion(x0, y0, x1, y1, Xmin, Ymin, Xmax, Ymax):
    u = 0
    if Xmin <= x0 <= Xmax:
        u = u + 1
    if Ymin <= y0 <= Ymax:
        u = u + 1
    if Xmin <= x1 <= Xmax:
        u = u + 1
    if Ymin <= y1 <= Ymax:
        u = u + 1

    if u == 4:
        line_clipping1(x0, y0, x1, y1, Xmin, Ymin, Xmax, Ymax)
    elif u == 3:
        line_clipping2(x0, y0, x1, y1, Xmin, Ymin, Xmax, Ymax)
    elif u <= 2:
        line_clipping3(x0, y0, x1, y1, Xmin, Ymin, Xmax, Ymax)

def line_clipping1(x0, y0, x1, y1, Xmin, Ymin, Xmax, Ymax):
    print("dibujar todo")

def line_clipping2(x0, y0, x1, y1, Xmin, Ymin, Xmax, Ymax):
    # Coeficientes del lado izquierdo
    A = np.array([[(x1-x0), -(Xmax - Xmin)], [(y1-y0), -(Ymin - Ymin)]])

    # Coeficientes del lado derecho
    b = np.array([(Xmin-x0), (Ymin-y0)])

    # Resolver el sistema de ecuaciones
    solucion = np.linalg.solve(A, b)

    x = Xmin + solucion[0] * (x1-x0)
    y = Ymin + solucion[1] * (y1-y0)
    # dibujar x0, y0 a x, y
    print("dibujar x0, y0 a x, y")

puntos = []
def line_clipping3(x0, y0, x1, y1, Xmin, Ymin, Xmax, Ymax):
    ##########################################
    #    Intersecta con el borde inferior    #
    ##########################################
    # Coeficientes del lado izquierdo
    A = np.array([[(x1-x0), -(Xmax - Xmin)], [(y1-y0), -(Ymin - Ymin)]])

    # Coeficientes del lado derecho
    b = np.array([(Xmin-x0), (Ymin-y0)])

    # Resolver el sistema de ecuaciones
    solucion = np.linalg.solve(A, b)
    if 0 <= solucion[0] <= 1:
        X = x0 + solucion[0] * (x1-x0)
        Y = y0 + solucion[0] * (y1-y0)
        puntos.append(X)
        puntos.append(Y)
    # dibujar x0, y0 a x, y

    ##########################################
    #    Intersecta con el borde superior    #
    ##########################################
    A = np.array([[(x1-x0), -(Xmax - Xmin)], [(y1-y0), -(Ymax - Ymax)]])

    # Coeficientes del lado derecho
    b = np.array([(Xmin-x0), (Ymax-y0)])

    # Resolver el sistema de ecuaciones
    solucion = np.linalg.solve(A, b)

    if 0 <= solucion[0] <= 1:
        X = x0 + solucion[0] * (x1-x0)
        Y = y0 + solucion[0] * (y1-y0)
        # print(X,Y)
        puntos.append(X)
        puntos.append(Y)

    ###########################################
    #    Intersecta con el borde izquierdo    #
    ########################################### 
    A = np.array([[(x1-x0), -(Xmin - Xmin)], [(y1-y0), -(Ymax - Ymin)]])

    # Coeficientes del lado derecho
    b = np.array([(Xmin-x0), (Ymin-y0)])

    # Resolver el sistema de ecuaciones
    solucion = np.linalg.solve(A, b)

    if 0 <= solucion[0] <= 1:
        X = x0 + solucion[0] * (x1-x0)
        Y = y0 + solucion[0] * (y1-y0)
        puntos.append(X)
        puntos.append(Y)

    #########################################
    #    Intersecta con el borde derecho    #
    ######################################### 
    A = np.array([[(x1-x0), -(Xmax - Xmax)], [(y1-y0), -(Ymax - Ymin)]])

    # Coeficientes del lado derecho
    b = np.array([(Xmax-x0), (Ymin-y0)])

    # Resolver el sistema de ecuaciones
    solucion = np.linalg.solve(A, b)
    # print(f"La solución es 4: x = {solucion[0]}, y = {solucion[1]}\n")

    if 0 <= solucion[0] <= 1:
        X = x0 + solucion[0] * (x1-x0)
        Y = y0 + solucion[0] * (y1-y0)
        puntos.append(X)
        puntos.append(Y)
    print(puntos)

def init():
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(0,100,0,100)

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,1.0)
    # Dibuja el rectángulo de corte
    glBegin(GL_LINE_LOOP)
    glVertex2f(Xmin, Ymin)
    glVertex2f(Xmax, Ymin)
    glVertex2f(Xmax, Ymax)
    glVertex2f(Xmin, Ymax)
    glEnd()

    # Dibuja las líneas sin cortar
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(x0, y0)
    glVertex2f(x1, y1)
    glEnd()
    glFlush()

def drawFunc2():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,1.0)
    # Dibuja el rectángulo de corte
    glBegin(GL_LINE_LOOP)
    glVertex2f(Xmin, Ymin)
    glVertex2f(Xmax, Ymin)
    glVertex2f(Xmax, Ymax)
    glVertex2f(Xmin, Ymax)
    glEnd()

    # Dibuja las líneas cortadas
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    # Aquí debes usar los puntos de intersección calculados en tu función de recorte
    glVertex2f(x0, y0)
    glVertex2f(x1, y1)
    glEnd()
    glFlush()

# Crea la primera ventana
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL")
glutDisplayFunc(drawFunc)
init()

# Crea la segunda ventana
glutInitWindowSize(500, 500)
glutInitWindowPosition(500, 0)
wind = glutCreateWindow("OpenGL")
glutDisplayFunc(drawFunc2)
init()

glutMainLoop()

