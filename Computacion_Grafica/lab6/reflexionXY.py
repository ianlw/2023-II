from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Dibujar triangulo
def triangulo(vertices):
    glBegin(GL_LINE_LOOP)
    for x, y in vertices:
        glVertex2f(x, y)
    glEnd()

# Reflejar triangulo
def reflejar(vertices, matriz_reflexion):
    vertices_reflejados = []
    for x, y in vertices:
        x_reflejado = matriz_reflexion[0][0] * x + matriz_reflexion[0][1] * y
        y_reflejado = matriz_reflexion[1][0] * x + matriz_reflexion[1][1] * y
        vertices_reflejados.append((x_reflejado, y_reflejado))
    return vertices_reflejados

def display():
    vertices_originales = [(50.0, 50.0), (100.0, 150.0), (200.0, 150.0)]
    matrices_reflexion = [
        [[-1, 0], [0, 1]],   # Segundo cuadrante 
        [[1, 0], [0, 1]],     # Primer cuadrante 
        [[-1, 0], [0, -1]],  # Tercer cuadrante 
        [[1, 0], [0, -1]],]   # Cuarto cuadrante 

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f (0.5 , 0.3 , 0.9)
    # Dibujar ejes X e Y
    glBegin(GL_LINES)
    glVertex2f(-499, 0)
    glVertex2f(499, 0)
    glVertex2f(0, -499)
    glVertex2f(0, 499)
    glEnd()

    # Dibujar el triangulo original y en los diferentes cuadrantes 
    glColor3f(0.8, 0.26, 1.0)
    for matriz in matrices_reflexion:
        vertices_reflejados = reflejar(vertices_originales, matriz)
        triangulo(vertices_reflejados)
    glFlush()

def myinit():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glClearColor (0.9 ,0.92 , 0.95 , 1.0)
    glClearColor (0.9 ,0.92 , 0.95 , 1.0)
    # Valores negativos necesarios para los cuadrantes
    gluOrtho2D(-499.0, 499.0, -499.0, 499.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Reflexión en ambos ejes X e Y")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    main()

