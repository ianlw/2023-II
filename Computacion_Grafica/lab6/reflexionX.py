from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def reflejaTrianguloX(x1, y1, x2, y2, x3, y3):
    x1r, y1r, x2r, y2r, x3r, y3r = 0, 0, 0, 0, 0, 0

    # Dibujar ejes x e y 
    glColor3f (0.5 , 0.3 , 0.9)
    glBegin(GL_LINES)
    glVertex2f(0, 250)
    glVertex2f(500, 250)
    glVertex2f(50, 0)
    glVertex2f(50, 500)
    glEnd()

    # Puntos a nueva escala 
    x1, y1 = x1 + 50, y1 + 250
    x2, y2 = x2 + 50, y2 + 250
    x3, y3 = x3 + 50, y3 + 250

    # Dibujar triangulo original
    glColor3f(0.8, 0.26, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

    # Reflejar el triangulo 
    x1r, y1r = x1, -y1 + 500
    x2r, y2r = x2, -y2 + 500
    x3r, y3r = x3, -y3 + 500

    # Dibujar el triangulo reflejado 
    glBegin(GL_LINE_LOOP)
    glVertex2f(x1r, y1r)
    glVertex2f(x2r, y2r)
    glVertex2f(x3r, y3r)
    glEnd()

def display():
    x1, y1, x2, y2, x3, y3 = 120.0, 160.0, 100.0, 200.0, 10.0, 100.0
    glClear(GL_COLOR_BUFFER_BIT)

    reflejaTrianguloX(x1, y1, x2, y2, x3, y3)
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
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Reflection")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    main()

