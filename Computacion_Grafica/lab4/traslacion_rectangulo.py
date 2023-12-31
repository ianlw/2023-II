from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Función que traslada una rectángulo
def trasladaRectangulo(P, T):
    glColor3f(0.8, 0.26, 1.0)
    glBegin(GL_LINES)
    # -- IZQUIERDA
    glVertex2f(P[0][0], P[0][1])
    glVertex2f(P[0][0], P[1][1])
    # -- ARRIBA
    glVertex2f(P[0][0], P[1][1])
    glVertex2f(P[1][0], P[1][1])
    # -- DERECHA
    glVertex2f(P[1][0], P[1][1])
    glVertex2f(P[1][0], P[0][1])
    # -- ABAJO
    glVertex2f(P[1][0], P[0][1])
    glVertex2f(P[0][0], P[0][1])
    glEnd()

    # Calcula las coordenadas de traslación
    P[0][0] += T[0]
    P[0][1] += T[1]
    P[1][0] += T[0]
    P[1][1] += T[1]

    glColor3f (0.5 , 0.3 , 0.9)
    # Dibuja el rectángulo trasladado
    glBegin(GL_LINES)
    # -- IZQUIERDA
    glVertex2f(P[0][0], P[0][1])
    glVertex2f(P[0][0], P[1][1])
    # -- ARRIBA
    glVertex2f(P[0][0], P[1][1])
    glVertex2f(P[1][0], P[1][1])
    # -- DERECHA
    glVertex2f(P[1][0], P[1][1])
    glVertex2f(P[1][0], P[0][1])
    # -- ABAJO
    glVertex2f(P[1][0], P[0][1])
    glVertex2f(P[0][0], P[0][1])
    glEnd()

# Despliega el gráfico
def display():
    P = [[300, 80], [120, 380]] 
    T = [20, 10]  

    glClear(GL_COLOR_BUFFER_BIT)  
    trasladaRectangulo(P, T) 
    glFlush()

# Inicializa OpenGL
def myinit():
    glClearColor (0.9058823529411765 ,0.9215686274509803 , 0.9568627450980393 , 1.0)
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
