from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Matriz de coordenadas del dibujo original
matriz_origen = [[100, 300, 200, 300, 200, 280, 100, 280],
                [100, 290, 130, 290, 130, 180, 100, 180],
                [100, 250, 160, 250, 160, 230, 100, 230],
                [100, 200, 200, 200, 200, 180, 100, 180]]

# Los componentes de esta matriz se sumarán a las cordenadas de la matriz de origen
matriz_traslacion = [50,100]

def dibujar_E():
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.26, 1.0)
    glVertex2f(matriz_origen[0][0],matriz_origen[0][1])
    glVertex2f(matriz_origen[0][2],matriz_origen[0][3])
    glVertex2f(matriz_origen[0][4],matriz_origen[0][5])
    glVertex2f(matriz_origen[0][6],matriz_origen[0][7])

    glVertex2f(matriz_origen[1][0],matriz_origen[1][1])
    glVertex2f(matriz_origen[1][2],matriz_origen[1][3])
    glVertex2f(matriz_origen[1][4],matriz_origen[1][5])
    glVertex2f(matriz_origen[1][6],matriz_origen[1][7])
    
    glVertex2f(matriz_origen[2][0],matriz_origen[2][1])
    glVertex2f(matriz_origen[2][2],matriz_origen[2][3])
    glVertex2f(matriz_origen[2][4],matriz_origen[2][5])
    glVertex2f(matriz_origen[2][6],matriz_origen[2][7])

    glVertex2f(matriz_origen[3][0],matriz_origen[3][1])
    glVertex2f(matriz_origen[3][2],matriz_origen[3][3])
    glVertex2f(matriz_origen[3][4],matriz_origen[3][5])
    glVertex2f(matriz_origen[3][6],matriz_origen[3][7])
    glEnd()

def dibujar_E_trasladado():
    glBegin(GL_QUADS)
    glColor3f (0.5 , 0.3 , 0.9)
    glVertex2f(matriz_origen[0][0] + matriz_traslacion[0],matriz_origen[0][1] + matriz_traslacion[1])
    glVertex2f(matriz_origen[0][2] + matriz_traslacion[0],matriz_origen[0][3] + matriz_traslacion[1])
    glVertex2f(matriz_origen[0][4] + matriz_traslacion[0],matriz_origen[0][5] + matriz_traslacion[1])
    glVertex2f(matriz_origen[0][6] + matriz_traslacion[0],matriz_origen[0][7] + matriz_traslacion[1])

    glVertex2f(matriz_origen[1][0] + matriz_traslacion[0],matriz_origen[1][1] + matriz_traslacion[1])
    glVertex2f(matriz_origen[1][2] + matriz_traslacion[0],matriz_origen[1][3] + matriz_traslacion[1])
    glVertex2f(matriz_origen[1][4] + matriz_traslacion[0],matriz_origen[1][5] + matriz_traslacion[1])
    glVertex2f(matriz_origen[1][6] + matriz_traslacion[0],matriz_origen[1][7] + matriz_traslacion[1])
    
    glVertex2f(matriz_origen[2][0] + matriz_traslacion[0],matriz_origen[2][1] + matriz_traslacion[1])
    glVertex2f(matriz_origen[2][2] + matriz_traslacion[0],matriz_origen[2][3] + matriz_traslacion[1])
    glVertex2f(matriz_origen[2][4] + matriz_traslacion[0],matriz_origen[2][5] + matriz_traslacion[1])
    glVertex2f(matriz_origen[2][6] + matriz_traslacion[0],matriz_origen[2][7] + matriz_traslacion[1])

    glVertex2f(matriz_origen[3][0] + matriz_traslacion[0],matriz_origen[3][1] + matriz_traslacion[1])
    glVertex2f(matriz_origen[3][2] + matriz_traslacion[0],matriz_origen[3][3] + matriz_traslacion[1])
    glVertex2f(matriz_origen[3][4] + matriz_traslacion[0],matriz_origen[3][5] + matriz_traslacion[1])
    glVertex2f(matriz_origen[3][6] + matriz_traslacion[0],matriz_origen[3][7] + matriz_traslacion[1])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor3f (0.5 , 0.3 , 0.9)
    dibujar_E()
    dibujar_E_trasladado()
    glutSwapBuffers()

def myinit():
    glClearColor (0.9 ,0.92 , 0.95 , 1.0)
    glColor3f(1.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 499.0, 0.0, 499.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Letter E")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    main()


