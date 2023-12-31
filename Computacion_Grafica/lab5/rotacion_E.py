
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import math

# Variables globales para la posición de los puntos
x1 = 350
y1 = 350
x2 = 50
y2 = 50

def punto():
    glColor3f(0.8, 0.26, 1.0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)  # Coordenadas del punto inicial
    glVertex2f(x2, y2)  # Coordenadas del punto final
    glEnd()

def punto_rotacion(x1, y1,x2, y2, angulo):
    glColor3f(0.5, 0.3, 0.9)
    matriz_a = np.array([[math.cos(math.radians(angulo)), -math.sin(math.radians(angulo))],
                         [math.sin(math.radians(angulo)), math.cos(math.radians(angulo))]])
    matriz_b = np.array([[x1], [y1]])
    matriz_c = np.array([[x2], [y2]])

    resultado1 = np.dot(matriz_a, matriz_b)
    resultado2 = np.dot(matriz_a, matriz_c)

    glBegin(GL_LINES)
    glVertex2f(resultado1[0], resultado1[1])  # Coordenadas del punto inicial rotado 
    glVertex2f(resultado2[0], resultado2[1])  # Coordenadas del punto final rotado 
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    punto()
    punto_rotacion(x1, y1, x2, y2, -40)
    punto_rotacion(x1, y1, x2, y2, -30)
    punto_rotacion(x1, y1, x2, y2, -20)
    punto_rotacion(x1, y1, x2, y2, -10)
    punto_rotacion(x1, y1, x2, y2, 10)
    punto_rotacion(x1, y1, x2, y2, 20)
    punto_rotacion(x1, y1, x2, y2, 30)
    punto_rotacion(x1, y1, x2, y2, 40)
    glutSwapBuffers()

def main():
    # Declarar x y y como globales para poder modificarlas
    global x, y  

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 400)  # Tamaño de la ventana
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Dibujar Punto rotada")
    glClearColor(0.9, 0.92, 0.95, 1.0)
    gluOrtho2D(0.0, 499.0, 0.0, 499.0)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
