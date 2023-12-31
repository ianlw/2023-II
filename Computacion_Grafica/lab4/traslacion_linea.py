from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def trasladaLinea(P, T):
    # Dibuja la línea original
    glColor3f(0.8, 0.26, 1.0)
    glBegin(GL_LINES)
    glVertex2f(P[0][0], P[0][1])
    glVertex2f(P[1][0], P[1][1])
    glEnd()

    # Calcula las coordenadas de traslación
    P[0][0] += T[0]
    P[0][1] += T[1]
    P[1][0] += T[0]
    P[1][1] += T[1]

    glColor3f (0.5 , 0.3 , 0.9)
    # Dibuja la línea trasladada
    glBegin(GL_LINES)
    glVertex2f(P[0][0], P[0][1])
    glVertex2f(P[1][0], P[1][1])
    glEnd()
    glFlush()


def display():
    P = [[150, 80], [320, 380]] 
    T = [100, 60]
    glClear(GL_COLOR_BUFFER_BIT) 
    trasladaLinea(P, T) 
    glFlush() 


def myinit():
    glClearColor (0.9, 0.92, 0.95, 1.0)
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity() 
    gluOrtho2D(0.0, 499.0, 0.0, 499.0)  

# Función principal
def main():
    # Inicialización de GLUT estándar
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)  
    glutInitWindowPosition(0, 0)  
    glutCreateWindow("Traslación de líneas") 
    glutDisplayFunc(display) 
    myinit() 
    glutMainLoop() 

# Llama a la función principal
if __name__ == "__main__":
    main()

