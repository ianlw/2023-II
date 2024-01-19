from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def cuadrado():
    # Dibujar el Cuadrado 
    glBegin(GL_QUADS)
    glVertex2f(250.0, 100.0)
    glVertex2f(350.0, 100.0)
    glVertex2f(350.0, 200.0)
    glVertex2f(250.0, 200.0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f (0.5 , 0.3 , 0.9) # Color1
    cuadrado()
    # Trasladar y rotar el cuadrado
    glRotatef(45, 0, 0, 1)
    glTranslatef(80.0, 20.0, 0.0)
    glColor3f(0.8, 0.26, 1.0) # Color2
    cuadrado()
    glFlush() 

def myinit():
    glClearColor (0.9 ,0.92 , 0.95 , 1.0) # Fondo
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity() 
    gluOrtho2D(0.0, 499.0, 0.0, 499.0)

def main():
    # Inicializacion GLUT estándar
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500) 
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Transformaciones con OpenGL")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    main()


