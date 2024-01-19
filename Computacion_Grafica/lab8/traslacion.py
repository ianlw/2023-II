from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def Traslada():
    # Triangulo antes de trasladar
    glBegin(GL_TRIANGLES)
    glColor3f (0.5 , 0.3 , 0.9) # Color1
    glVertex2f(100.0, 100.0)
    glVertex2f(200.0, 100.0)
    glVertex2f(150.0, 150.0)
    glEnd()

    # Triangulo después de trasladar
    glTranslatef(200.0, 200.0, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.8, 0.26, 1.0) # Color2
    glVertex3f(100.0, 100.0, 0.0)
    glVertex3f(200.0, 100.0, 0.0)
    glVertex3f(150.0, 150.0, 0.0)
    glEnd()

def Rota():
    #--triangulo antes de rotar
    glColor3f (0.5 , 0.3 , 0.9) # Color1
    glBegin(GL_TRIANGLES)
    glVertex2f(100.0, 100.0)
    glVertex2f(200.0, 100.0)
    glVertex2f(150.0, 150.0)
    glEnd()

    #--triangulo rotado
    glRotatef(45, 0, 0, 1)
    glBegin(GL_TRIANGLES)
    glColor3f(0.8, 0.26, 1.0) # Color2
    glVertex2f(100.0, 100.0)
    glVertex2f(200.0, 100.0)
    glVertex2f(150.0, 150.0)
    glEnd()
def Escala():
    #--triangulo antes de escalar
    glColor3f (0.5 , 0.3 , 0.9) # Color1
    glBegin(GL_TRIANGLES)
    glVertex2f(100.0, 100.0)
    glVertex2f(200.0, 100.0)
    glVertex2f(150.0, 150.0)
    glEnd()

    #--triangulo despues de escalar
    glScalef(2.0, 2.0, 2.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.8, 0.26, 1.0) # Color2
    glVertex2f(100.0, 100.0)
    glVertex2f(200.0, 100.0)
    glVertex2f(150.0, 150.0)
    glEnd()
    
def TransfComp():
    #--triangulo antes de rotar y trasladar
    glColor3f (0.5 , 0.3 , 0.9) # Color1
    glBegin(GL_TRIANGLES)
    glVertex2f(100.0, 100.0)
    glVertex2f(200.0, 100.0)
    glVertex2f(150.0, 150.0)
    glEnd()

    #--triangulo después de rotar y trasladar
    glRotatef(-20, 0, 0, 1)
    glTranslatef(100.0, 100.0, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.8, 0.26, 1.0) # Color2
    glVertex2f(100.0, 100.0)
    glVertex2f(200.0, 100.0)
    glVertex2f(150.0, 150.0)
    glEnd()

    glFlush()
# Despliega el gráfico
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # Traslada()
    # Rota()
    # Escala()
    TransfComp()
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

