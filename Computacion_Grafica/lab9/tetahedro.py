from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective, gluLookAt
import numpy as np

ANCHO, ALTO = 400, 400

def rotar_alrededor_del_eje(vertices, eje, angulo):
    angulo_radianes = np.radians(angulo)
    cos_theta = np.cos(angulo_radianes)
    sin_theta = np.sin(angulo_radianes)

    eje = np.array(eje, dtype=np.float64)
    eje /= np.linalg.norm(eje)

    vertices_rotados = []
    for vertex in vertices:
        u, v, w = eje
        x_rot = (u * (u * vertex[0] + v * vertex[1] + w * vertex[2]) * (1 - cos_theta) +
                 vertex[0] * cos_theta + (-w * vertex[1] + v * vertex[2]) * sin_theta)
        
        y_rot = (v * (u * vertex[0] + v * vertex[1] + w * vertex[2]) * (1 - cos_theta) +
                 vertex[1] * cos_theta + (w * vertex[0] - u * vertex[2]) * sin_theta)
        
        z_rot = (w * (u * vertex[0] + v * vertex[1] + w * vertex[2]) * (1 - cos_theta) +
                 vertex[2] * cos_theta + (-v * vertex[0] + u * vertex[1]) * sin_theta)
        
        vertices_rotados.append([x_rot, y_rot, z_rot])

    return vertices_rotados

def dibujar_tetraedro(vertices, color):
    glColor3fv(color)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLES)
    glVertex3fv(vertices[0])  # Triángulo ABC
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[2])
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex3fv(vertices[0])  # Triángulo ABD
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[3])
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex3fv(vertices[0])  # Triángulo ACD
    glVertex3fv(vertices[2])
    glVertex3fv(vertices[3])
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex3fv(vertices[1])  # Triángulo BCD
    glVertex3fv(vertices[2])
    glVertex3fv(vertices[3])
    glEnd()

def ejes():
    glBegin(GL_LINES)
    glColor3f (0.4 , 0.4 , 0.3) # Color3
    glVertex3i(0, 0, 0)  # eje Y
    glVertex3i(0, 50, 0)
    glVertex3i(0, 0, 0)  # eje X
    glVertex3i(50, 0, 0)
    glVertex3i(0, 0, 0)  # eje Z
    glVertex3i(0, 0, 50)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    ejes()

    A = [0.0, 10.0, 0.0]
    B = [10.0, -10.0, 0.0]
    C = [-10.0, -10.0, 0.0]
    D = [0.0, 0.0, 10.0]

    vertices = [A, B, C, D]

    # Dibuja el tetraedro original en color azul
    dibujar_tetraedro(vertices, [0.5 , 0.3 , 0.9])

    # Aplica rotación alrededor de [4, 4, 0] con un ángulo de 45 grados y dibuja el tetraedro rotado en color verde
    vertices_rotados = rotar_alrededor_del_eje(vertices, [4, 4, 0], 45)
    dibujar_tetraedro(vertices_rotados, [0.8, 0.26, 1.0])

    glutSwapBuffers()

def inicializar():
    glClearColor (0.9 ,0.92 , 0.95 , 1.0) # Fondo
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0, 2.0, -2.0, 2.0, -2.0, 2.0)
    gluPerspective(45.0, float(ANCHO) / float(ALTO), 1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(30, 30, 30, 0, 0, 0, 0, 1, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(ANCHO, ALTO)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Rotación 3D")
    glutDisplayFunc(display)
    inicializar()
    glEnable(GL_DEPTH_TEST)
    glutMainLoop()

if __name__ == "__main__":
    main()

