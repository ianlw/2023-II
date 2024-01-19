from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Global variable
angle = 0.0  # Current rotational angle of the shapes

# Matriz de coordenadas del dibujo original
matriz_origen = [[200, 300, 300, 300, 300, 280, 200, 280],
[200, 290, 230, 290, 230, 180, 200, 180],
[200, 250, 260, 250, 260, 230, 200, 230],
[200, 200, 300, 200, 300, 180, 200, 180]]

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

def initGL():
    # Set "clearing" or background color
    glClearColor (0.9 ,0.92 , 0.95 , 1.0) # Fondo 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity() 
    # gluOrtho2D(0.0, 599.0, 0.0, 599.0)
    # gluOrtho2D(-300.0, 900.0, -300.0, 900.0)
    gluOrtho2D(-499.0, 499.0, -499.0, 499.0)

def idle():
    global angle
    angle += 0.9
    glutPostRedisplay() 

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT) 
    glMatrixMode(GL_MODELVIEW)  
    glLoadIdentity() 

    glPushMatrix()
    glTranslatef(-0.25, -0.24, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0) 
    dibujar_E()
    glPopMatrix()  

    glutSwapBuffers()  

def main():
    import sys
    glutInit(sys.argv)  
    glutInitDisplayMode(GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Animation via Idle Function".encode("ascii"))
    glutDisplayFunc(display)
    glutIdleFunc(idle) 
    initGL() 
    glutMainLoop()

if __name__ == "__main__":
    main()

