from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
 
# Deformación de rectángulo con respecto al eje X
def deformaRectanguloX(x1, y1, x2, y2, sh):
 
    #--dibujar el rectangulo original
    glColor3f (0.5 , 0.3 , 0.9) # Color1
    glBegin(GL_LINE_LOOP)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()
    # Deformar cada punto del rectangulo con respecto al eje X
    x1d = x1 + sh * y1
    y1d = y1
    x2d = x2 + sh * y1
    y2d = y1
 
    x3d = x2 + sh * y2
    y3d = y2
    x4d = x1 + sh * y2
    y4d = y2
    # Dibujar el rectangulo deformado con respecto al eje X
    glColor3f(0.8, 0.26, 1.0) # Color2
    glBegin(GL_LINE_LOOP)
    glVertex2f(x1d, y1d)
    glVertex2f(x2d, y2d)
    glVertex2f(x3d, y3d)
    glVertex2f(x4d, y4d)
    glEnd()
 
#--despliega el gráfico
def display():
    x1 = 20.0
    y1 = 50.0
    x2 = 250.0
    y2 = 200.0
    sh = 2
    glClear(GL_COLOR_BUFFER_BIT) #--establece el color de la ventana
    deformaRectanguloX(x1, y1, x2, y2, sh)
    glFlush() #--fuerza la ejecución de los comandos de OpenGL
 
def myinit():
    glClearColor (0.9 ,0.92 , 0.95 , 1.0) # Fondo
    glPointSize(1.0) #--tamño de los puntos
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 659.0, 0.0, 299.0)
 
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
