from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Coordenadas de el recuadro de recorte 
x_min, y_min, x_max, y_max = 100.0, 100.0, 350.0, 350.0

# Coordenadas de las lineas a recortar 
lines = [
    (50.0, 50.0, 300.0, 300.0),
    (100.0, 100.0, 400.0, 100.0),
]

def liang_barsky(x1, y1, x2, y2):
    # Distencia entre los púntos de las lineas 
    dx = x2 - x1
    dy = y2 - y1
    p = [-dx, dx, -dy, dy]
    q = [x1 - x_min, x_max - x1, y1 - y_min, y_max - y1]
    u1 = 0.0
    u2 = 1.0

    for i in range(4):
        if p[i] < 0.0:
            u1 = max(u1, q[i] / p[i])
        elif p[i] > 0.0:
            u2 = min(u2, q[i] / p[i])
        elif p[i] == 0.0 and q[i] < 0.0:
            return None

    if u1 > u2:
        return None

    return x1 + u1 * dx, y1 + u1 * dy, x1 + u2 * dx, y1 + u2 * dy

def draw_original():
    glClear(GL_COLOR_BUFFER_BIT)

    # Dibuja las líneas originales
    glColor3f(1.0, 0.0, 0.0)
    for line in lines:
        glBegin(GL_LINES)
        glVertex2f(line[0], line[1])
        glVertex2f(line[2], line[3])
        glEnd()

    # Dibuja la ventana de recorte
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x_min, y_min)
    glVertex2f(x_max, y_min)
    glVertex2f(x_max, y_max)
    glVertex2f(x_min, y_max)
    glEnd()

    glFlush()

def draw_clipped():
    glClear(GL_COLOR_BUFFER_BIT)

    # Dibuja la ventana de recorte
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x_min, y_min)
    glVertex2f(x_max, y_min)
    glVertex2f(x_max, y_max)
    glVertex2f(x_min, y_max)
    glEnd()
    # Dibuja las líneas recortadas
    glColor3f(0.0, 0.0, 1.0)
    for line in lines:
        clipped_line = liang_barsky(*line)
        if clipped_line is not None:
            glBegin(GL_LINES)
            glVertex2f(*clipped_line[:2])
            glVertex2f(*clipped_line[2:])
            glEnd()

    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)

# Crea la primera ventana y establece su función de visualización
glutCreateWindow("Liang-Barsky Original")
gluOrtho2D(0.0, 500.0, 0.0, 500.0)
glClearColor(0.9058823529411765, 0.9215686274509803, 0.9568627450980393, 1.0)
glutDisplayFunc(draw_original)

# Crea la segunda ventana y establece su función de visualización
glutCreateWindow("Liang-Barsky Clipped")
glClearColor(0.9058823529411765, 0.9215686274509803, 0.9568627450980393, 1.0)
gluOrtho2D(0.0, 500.0, 0.0, 500.0)
glutDisplayFunc(draw_clipped)

glutMainLoop()

