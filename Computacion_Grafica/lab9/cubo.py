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
    for face in vertices:
        rotated_face = []
        for vertex in face:
            vertex = np.array(vertex)
            u = eje[0]
            v = eje[1]
            w = eje[2]
            
            x_rot = (u * (u * vertex[0] + v * vertex[1] + w * vertex[2]) * (1 - cos_theta) +
                     vertex[0] * cos_theta + (-w * vertex[1] + v * vertex[2]) * sin_theta)
            
            y_rot = (v * (u * vertex[0] + v * vertex[1] + w * vertex[2]) * (1 - cos_theta) +
                     vertex[1] * cos_theta + (w * vertex[0] - u * vertex[2]) * sin_theta)
            
            z_rot = (w * (u * vertex[0] + v * vertex[1] + w * vertex[2]) * (1 - cos_theta) +
                     vertex[2] * cos_theta + (-v * vertex[0] + u * vertex[1]) * sin_theta)
            
            rotated_face.append([x_rot, y_rot, z_rot])

        vertices_rotados.append(rotated_face)

    return vertices_rotados

def dibujar_cubo(vertices, color):
    glColor3fv(color)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_QUADS)
    for face in vertices:
        for vertex in face:
            glVertex3fv(vertex)
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

    A1 = [-10.0, -10.0, -10.0]
    B1 = [10.0, -10.0, -10.0]
    C1 = [10.0, 10.0, -10.0]
    D1 = [-10.0, 10.0, -10.0]
    E1 = [-10.0, -10.0, 10.0]
    F1 = [10.0, -10.0, 10.0]
    G1 = [10.0, 10.0, 10.0]
    H1 = [-10.0, 10.0, 10.0]

    vertices = [
        [A1, B1, C1, D1],
        [E1, F1, G1, H1],
        [A1, B1, F1, E1],
        [D1, C1, G1, H1],
        [B1, F1, G1, C1],
        [A1, E1, H1, D1]
    ]

    # Dibuja el cubo original 
    dibujar_cubo(vertices,[0.5 , 0.3 , 0.9])

    # Aplica rotación alrededor de [7, 7, 7] con un ángulo de 30 grados
    vertices_rotados = rotar_alrededor_del_eje(vertices, [7, 7, 7], 30)
    dibujar_cubo(vertices_rotados, [0.8, 0.26, 1.0])

    glutSwapBuffers()

def inicializar():
    glClearColor (0.9 ,0.92 , 0.95 , 1.0) # Fondo
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-3.0, 2.0, -3.0, 2.0, -2.0, 2.0)
    gluPerspective(45.0, float(ANCHO) / float(ALTO), 1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(25, 25, 50, 25, 25, 0, 0, 1, 0)

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
