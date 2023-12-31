from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Configuración inicial
width, height = 500, 450
r = 0.4
change = 0
p = [[0, 0] for _ in range(6)]

# Función para dibujar círculos
def draw(tx, ty):
    global r
    glBegin(GL_LINE_LOOP)
    for i in range(1200):
        theta = 2 * math.pi * i / 1200
        x1 = r * math.cos(theta) + tx
        y1 = r * math.sin(theta) + ty
        glVertex2f(x1, y1)
    glEnd()

# Función de visualización
def display():
    global width, height, r, change, p
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.9, 0.92, 0.95, 1.0) 
    glColor3f(0.8, 0.26, 1.0)  
    glMatrixMode(GL_MODELVIEW)
    j = 0
    change = 1 - change
    glBegin(GL_LINE_LOOP)
    for i in range(1200):
        theta = 2 * math.pi * i / 1200
        x1 = r * math.cos(theta)
        y1 = r * math.sin(theta) 
        glVertex2f(x1, y1)
        if i in [100, 300, 500, 700, 900, 1100] and change == 0:
            p[j] = [x1, y1]
            j += 1
    glEnd()
    if change == 0:
        glColor3f(0.5, 0.3, 0.9)  
        for i in range(6):
            draw(p[i][0], p[i][1])
    glutSwapBuffers()

# Función principal
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutCreateWindow("circles".encode("ascii"))
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()

main()

