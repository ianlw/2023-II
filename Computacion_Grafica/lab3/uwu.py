import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

Xmin, Ymin, Xmax, Ymax = 90, 90, 450,360

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
    dibujaLinea(x0, y0, x1, y1)

def line_clipping2(x0, y0, x1, y1, Xmin, Ymin, Xmax, Ymax):
    # Resolviendo el sistema de ecuaciones
    A = np.array([[(x1-x0), -(Xmax - Xmin)], [(y1-y0), -(Ymin - Ymin)]])
    b = np.array([(Xmin-x0), (Ymin-y0)])
    solucion = np.linalg.solve(A, b)
    # Calcular los puntos de corte
    x = x0 + solucion[0] * (x1-x0)
    y = y0 + solucion[0] * (y1-y0)
    dibujaLinea(x0, y0, x, y)

puntos = []
def line_clipping3(x0, y0, x1, y1, Xmin, Ymin, Xmax, Ymax):
    ##########################################
    #    Intersecta con el borde inferior    #
    ##########################################
    # Resolviendo el sistema de ecuaciones
    A = np.array([[(x1-x0), -(Xmax - Xmin)], [(y1-y0), -(Ymin - Ymin)]])
    b = np.array([(Xmin-x0), (Ymin-y0)])
    solucion = np.linalg.solve(A, b)

    # Si se cumple esto entonces la linea intersecta por este borde 
    if 0 <= solucion[0] <= 1:
        X = x0 + solucion[0] * (x1-x0)
        Y = y0 + solucion[0] * (y1-y0)
        puntos.append(X)
        puntos.append(Y)

    ##########################################
    #    Intersecta con el borde superior    #
    ##########################################
    # Resolviendo el sistema de ecuaciones
    A = np.array([[(x1-x0), -(Xmax - Xmin)], [(y1-y0), -(Ymax - Ymax)]])
    b = np.array([(Xmin-x0), (Ymax-y0)])
    solucion = np.linalg.solve(A, b)

    # Si se cumple esto entonces la linea intersecta por este borde 
    if 0 <= solucion[0] <= 1:
        X = x0 + solucion[0] * (x1-x0)
        Y = y0 + solucion[0] * (y1-y0)
        puntos.append(X)
        puntos.append(Y)

    ###########################################
    #    Intersecta con el borde izquierdo    #
    ########################################### 
    # Resolviendo el sistema de ecuaciones
    A = np.array([[(x1-x0), -(Xmin - Xmin)], [(y1-y0), -(Ymax - Ymin)]])
    b = np.array([(Xmin-x0), (Ymin-y0)])
    solucion = np.linalg.solve(A, b)

    # Si se cumple esto entonces la linea intersecta por este borde 
    if 0 <= solucion[0] <= 1:
        X = x0 + solucion[0] * (x1-x0)
        Y = y0 + solucion[0] * (y1-y0)
        puntos.append(X)
        puntos.append(Y)

    #########################################
    #    Intersecta con el borde derecho    #
    ######################################### 
    # Resolviendo el sistema de ecuaciones
    A = np.array([[(x1-x0), -(Xmax - Xmax)], [(y1-y0), -(Ymax - Ymin)]])
    b = np.array([(Xmax-x0), (Ymin-y0)])
    solucion = np.linalg.solve(A, b)

    # Si se cumple esto entonces la linea intersecta por este borde 
    if 0 <= solucion[0] <= 1:
        X = x0 + solucion[0] * (x1-x0)
        Y = y0 + solucion[0] * (y1-y0)
        puntos.append(X)
        puntos.append(Y)

    # Dibujar la linea recortada con lo spuntos de intersección 
    dibujaLinea(puntos[0], puntos[1], puntos[2], puntos[3])
    glFlush()

# Necesario para dibujar las lineas
def Plot(ix, iy):
   ix = int(ix)
   iy = int(iy)
   glBegin(GL_POINTS)
   glVertex2i(ix, iy)
   glEnd()
 
def swap(x, y):
   return y, x

# Algortimo de Bresenham
def dibujaLinea(x0, y0, x1, y1):
   x0 = int(x0)
   y0 = int(y0)
   x1 = int(x1)
   y1 = int(y1)
 
   dy, x, y, error = 0, 0, 0, 0
   delta_x, delta_y = 0, 0
   steep = abs(y1 - y0) > abs(x1 - x0)
 
   if steep:
       x0, y0 = swap(x0, y0)
       x1, y1 = swap(x1, y1)
 
   if x0 > x1:
       x0, x1 = swap(x0, x1)
       y0, y1 = swap(y0, y1)
 
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
           Plot(y, x)
       else:
           Plot(x, y)
       error = error + delta_y
       if 2 * error >= delta_x:
           y = y + dy
           error = error - delta_x

def dibujaRectangulo(xmin, ymin, xmax, ymax):
   dibujaLinea(xmin, ymin, xmin, ymax)
   dibujaLinea(xmin, ymax, xmax, ymax)
   dibujaLinea(xmax, ymax, xmax, ymin)
   dibujaLinea(xmax, ymin, xmin, ymin)

# Primera venta
def display1():
   glClear(GL_COLOR_BUFFER_BIT)
   glColor3f(0.5, 0.3, 0.9) 
   glPointSize(2.0)
   dibujaRectangulo(Xmin, Ymin, Xmax, Ymax)
   glPointSize(1.0)
   glColor3f(0.8431372549019608, 0.3686274509803922, 1.0)
   # glColor3f(0.5, 0.3, 0.9) 
   dibujaLinea(180, 120, 360, 300)
   dibujaLinea(120, 120, 210, 60)
   dibujaLinea(30, 180, 300, 450)
   glFlush()

# Segunda ventana
def display2():
   glClear(GL_COLOR_BUFFER_BIT)
   glColor3f(0.5, 0.3, 0.9) 
   glPointSize(1.0)
   dibujaRectangulo(Xmin, Ymin, Xmax, Ymax)
   glPointSize(2.0)
   glColor3f(0.8, 0.26, 1.0)
   comparacion(180, 120, 360, 300, 90, 90, 450,360)
   comparacion(120, 120, 210, 60, 90, 90, 450,360)
   comparacion(30, 180, 300, 450, 90, 90, 450,360)
   glFlush()

def myinit():
   glClearColor(0.9, 0.92, 0.95, 1.0)
   glColor3f(1.0, 0.0, 0.0)
   glPointSize(1.0)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   gluOrtho2D(0.0, 499.0, 0.0, 499.0)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("LINEAS ANTES DEL RECORTE")
glutDisplayFunc(display1)
myinit()

glutInitWindowSize(500, 500)
glutInitWindowPosition(550, 0)
glutCreateWindow("LINEAS DESPUES DEL RECORTE")
glutDisplayFunc(display2)
myinit()
glutMainLoop()
