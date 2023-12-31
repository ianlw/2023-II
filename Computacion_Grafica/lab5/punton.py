from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import math

def punto():
    glColor3f(0.8, 0.26, 1.0)
    glPointSize(20) 
    glBegin(GL_POINTS)
    glVertex2f(300, 300) # Coordenadas del punto
    glEnd()

def punto_rotacion(angulo):
    glColor3f (0.5 , 0.3 , 0.9)
    # Matriz de senos y cosenos
    matriz_a = np.array([[math.cos(math.radians(angulo)), -math.sin(math.radians(angulo))], [math.sin(math.radians(angulo)), math.cos(math.radians(angulo))]])
    # Matriz de punto inicial 
    matriz_b = np.array([[300], [300]])
    resultado = np.dot(matriz_a, matriz_b) # Producto de matrices
    glBegin(GL_POINTS)
    glVertex2f(resultado[0], resultado[1])  # Coordenadas del punto rotado 
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    punto()
    punto_rotacion(-40)
    punto_rotacion(-30)
    punto_rotacion(-20)
    punto_rotacion(-10)
    punto_rotacion(10)
    punto_rotacion(20)
    punto_rotacion(30)
    punto_rotacion(40)
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(400, 400)  # Tamaño de la ventana
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Dibujar Punto rotado")
    glClearColor (0.9 ,0.92 , 0.95 , 1.0)
    gluOrtho2D(0.0, 499.0, 0.0, 499.0)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()

