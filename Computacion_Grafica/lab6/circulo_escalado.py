from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def puntoEscaladoX(x, centro_x, factor_escala_x):
    return centro_x + (x - centro_x) * factor_escala_x

def puntoEscaladoY(y, centro_y, factor_escala_y):
    return centro_y + (y - centro_y) * factor_escala_y

# Algoritmo de dibujo del círculo
def dibujarCirculo(centro_x, centro_y, radio):
    glBegin(GL_LINE_LOOP)
    for i in range(800):
        theta = 2.0 * math.pi * float(i) / float(800)
        x = centro_x + radio * math.cos(theta)
        y = centro_y + radio * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

# Algoritmo de dibujo del círculo escalado
def escalaCirculo(centro_x, centro_y, radio, factor_escala_x, factor_escala_y):
    glBegin(GL_LINE_LOOP)
    for i in range(800):
        theta = 2.0 * math.pi * float(i) / float(800)
        x = centro_x + radio * math.cos(theta)
        y = centro_y + radio * math.sin(theta)
        x_escala = puntoEscaladoX(x, centro_x, factor_escala_x)
        y_escala = puntoEscaladoY(y, centro_y, factor_escala_y)
        glVertex2f(x_escala, y_escala)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Dibujar círculo original en azul
    glColor3f (0.5 , 0.3 , 0.9)
    dibujarCirculo(250, 250, 70)
    
    # Dibujar círculo escalado en rojo
    glColor3f(0.8, 0.26, 1.0)
    escalaCirculo(250, 250, 70, 2, 2)
    
    glFlush()

def myinit():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glClearColor (0.9 ,0.92 , 0.95 , 1.0)
    gluOrtho2D(0.0, 499.0, 0.0, 499.0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Escalamiento de Círculo")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    main()

