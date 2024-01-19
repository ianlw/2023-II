from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle = 0.0 

def initGL():
    glClearColor (0.9 ,0.92 , 0.95 , 1.0) # Fondo

def idle():
    global angle
  
    angle += 0.2
    glutPostRedisplay()

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)  
    glLoadIdentity()  

    glPushMatrix() 
    glTranslatef(-0.5, 0.4, 0.0)  
    glRotatef(angle, 0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glColor3f (0.5 , 0.3 , 0.9) # Color1
    glVertex2f(-0.3, -0.3)
    glVertex2f(0.3, -0.3)
    glVertex2f(0.3, 0.3)
    glVertex2f(-0.3, 0.3)
    glEnd()
    glPopMatrix() 

    glPushMatrix() 
    glTranslatef(-0.4, -0.3, 0.0) 
    glRotatef(angle, 0.0, 0.0, 1.0) 
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.26, 1.0) # Color2
    glVertex2f(-0.3, -0.3)
    glVertex2f(0.3, -0.3)
    glVertex2f(0.3, 0.3)
    glVertex2f(-0.3, 0.3)
    glEnd()
    glPopMatrix() 

    glutSwapBuffers()  

def main():
    import sys
    glutInit(sys.argv)  
    glutInitDisplayMode(GLUT_DOUBLE) 
    glutInitWindowSize(540, 480)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Animation via Idle Function".encode("ascii"))
    glutDisplayFunc(display)
    glutIdleFunc(idle)  
    initGL() 
    glutMainLoop() 

if __name__ == "__main__":
    main()

