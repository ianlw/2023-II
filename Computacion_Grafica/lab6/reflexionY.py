from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def reflejaTrianguloY(x1, y1, x2, y2, x3, y3):
    x1r, y1r, x2r, y2r, x3r, y3r = 0, 0, 0, 0, 0, 0

    # Draw X and Y axes
    glColor3f (0.5 , 0.3 , 0.9)
    glBegin(GL_LINES)
    glVertex2f(250, 0)
    glVertex2f(250, 500)
    glVertex2f(0, 50)
    glVertex2f(500, 50)
    glEnd()

    # Convert points to a new scale
    x1, y1 = x1 + 250, y1 + 50
    x2, y2 = x2 + 250, y2 + 50
    x3, y3 = x3 + 250, y3 + 50

    glColor3f(0.8, 0.26, 1.0)
    # Draw the original triangle
    glBegin(GL_LINE_LOOP)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

    # Reflect the triangle with respect to the Y axis
    x1r, y1r = -x1 + 500, y1
    x2r, y2r = -x2 + 500, y2
    x3r, y3r = -x3 + 500, y3

    # Draw the reflected triangle
    glBegin(GL_LINE_LOOP)
    glVertex2f(x1r, y1r)
    glVertex2f(x2r, y2r)
    glVertex2f(x3r, y3r)
    glEnd()

def display():
    x1, y1, x2, y2, x3, y3 = 120.0, 160.0, 100.0, 200.0, 10.0, 100.0
    glClear(GL_COLOR_BUFFER_BIT)

    reflejaTrianguloY(x1, y1, x2, y2, x3, y3)
    glFlush()

def myinit():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glClearColor (0.9 ,0.92 , 0.95 , 1.0)
    gluOrtho2D(0.0, 499.0, 0.0, 499.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Reflection")
    glutDisplayFunc(display)
    myinit()
    glutMainLoop()

if __name__ == "__main__":
    main()

