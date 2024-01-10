from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Polígono de 5 lados
def poligono(vertices):
    glBegin(GL_LINE_LOOP)
    for x, y in vertices:
        glVertex2f(x, y)
    glEnd()

def reflejoX(vertices):
    vertices_reflejados = [(x, -y + 500) for x, y in vertices]
    return vertices_reflejados

def poligono_reflejado(vertices):
    poligono(vertices)
    vertices_reflejados = reflejoX(vertices)
    poligono(vertices_reflejados)

def display():
    vertices = [(50.0, 50.0), (100.0, 150.0), (200.0, 150.0), (250.0, 50.0), (150.0, 0.0)]
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f (0.5 , 0.3 , 0.9)
    # Ejes X e Y
    glBegin(GL_LINES)
    glVertex2f(0, 250)
    glVertex2f(500, 250)
    glVertex2f(25, 0)
    glVertex2f(25, 500)
    glEnd()
    glColor3f(0.8, 0.26, 1.0)
    poligono_reflejado(vertices)
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
    glutCreateWindow("Poligono de 5 lados reflejado en el eje X")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    main()

