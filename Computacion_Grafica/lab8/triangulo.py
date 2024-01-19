from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def Transformar():
    # Triangulo antes de rotar y trasladar
    glColor3f (0.5 , 0.3 , 0.9) # Color1
    glBegin(GL_TRIANGLES)
    glVertex2f(100.0, 100.0)
    glVertex2f(200.0, 100.0)
    glVertex2f(150.0, 150.0)
    glEnd()

    # Triangulo después de escalar, rotar y trasladar
    glTranslatef(80.0, 20.0, 0.0)
    glRotatef(30, 0, 0, 1)
    glScalef(2.0, 2.0, 0)

    glBegin(GL_TRIANGLES)
    glColor3f(0.8, 0.26, 1.0) # Color2
    glVertex2f(100.0, 100.0)
    glVertex2f(200.0, 100.0)
    glVertex2f(150.0, 150.0)
    glEnd()
    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    Transformar()
    glFlush() 

def myinit():
    glClearColor (0.9 ,0.92 , 0.95 , 1.0) # Fondo
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity() 
    gluOrtho2D(0.0, 499.0, 0.0, 499.0)

def main():
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
