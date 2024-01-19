from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
 
# Matriz de coordenadas del dibujo original
matriz_origen = [[200, 300, 300, 300, 300, 280, 200, 280],
[200, 290, 230, 290, 230, 180, 200, 180],
[200, 250, 260, 250, 260, 230, 200, 230],
[200, 200, 300, 200, 300, 180, 200, 180]]
 
# Dibujar la figura original
def dibujar_E():
    glBegin(GL_QUADS)
    glColor3f (0.5 , 0.3 , 0.9) # Color1
    for i in range(4):
        for j in range(0, 8, 2):
            glVertex2f(matriz_origen[i][j], matriz_origen[i][j+1])
    glEnd()
 
def deformaPuntoX(x, y, sh):
    return x + sh * y, y
 
# Dibuajr la figura e respecto a x
def dibujar_E_deformado(sh):
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.26, 1.0) # Color2
    for i in range(4):
        for j in range(0, 8, 2):
            x, y = deformaPuntoX(matriz_origen[i][j], matriz_origen[i][j+1], sh)
            glVertex2f(x, y)
    glEnd()
 
def display():
    glClear(GL_COLOR_BUFFER_BIT) #--establece el color de la ventana
    dibujar_E()
    dibujar_E_deformado(2)
    glFlush() #--fuerza la ejecución de los comandos de OpenGL
 
def myinit():
    glClearColor (0.9 ,0.92 , 0.95 , 1.0) # Fondo
    glPointSize(1.0) #--tamño de los puntos
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 999.0, 0.0, 499.0)
 
def main():
    # Inicializacion GLUT estándar
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500) # ventana 500x500 pixeles
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Reflexión") # título de la ventana
    glutDisplayFunc(display)
    myinit() # fija o establece los atributos
    glutMainLoop() # entra a un ciclo de evento
 
if __name__ == "__main__":
    main()
