from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def ptoEscaladoX(x1, x0, Sx):
    return x0 + (x1 - x0)*Sx

def ptoEscaladoY(y1, y0, Sy):
    return y0 + (y1 - y0)*Sy

def escalaTriangulo(x1, y1, x2, y2, x3, y3, Sx, Sy):
    x1e = ptoEscaladoX(x1, x3, Sx)
    y1e = ptoEscaladoY(y1, y3, Sy)
    x2e = ptoEscaladoX(x2, x3, Sx)
    y2e = ptoEscaladoY(y2, y3, Sy)

    glColor3f(0.8, 0.26, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

    glColor3f (0.5 , 0.3 , 0.9)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x1e, y1e)
    glVertex2f(x2e, y2e)
    glVertex2f(x3, y3)
    glEnd()

def display():
    x1 = 120.0
    y1 = 160.0
    x2 = 150.0
    y2 = 300.0
    x3 = 60.0
    y3 = 100.0
    Sx = 2
    Sy = 2

    glClear(GL_COLOR_BUFFER_BIT)
    escalaTriangulo(x1, y1, x2, y2, x3, y3, Sx, Sy)
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
    glutCreateWindow("Escalamiento")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    main()

