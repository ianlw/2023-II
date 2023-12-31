import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
 
MAX = 20
TOP, BOTTOM, RIGHT, LEFT = 0x1, 0x2, 0x4, 0x8
ln = [[0] * 4 for _ in range(MAX)]
xmin, ymin, xmax, ymax = 0, 0, 0, 0
lnclip = [[0] * 4 for _ in range(MAX)]
n = 0
k = 0
 
def Plot(ix, iy):
   ix = int(ix)
   iy = int(iy)
   glBegin(GL_POINTS)
   glVertex2i(ix, iy)
   glEnd()
 
def swap(x, y):
   return y, x
 
def dibujaLinea(x0, y0, x1, y1):
   x0 = int(x0)
   y0 = int(y0)
   x1 = int(x1)
   y1 = int(y1)
 
   dy, x, y, error = 0, 0, 0, 0
   delta_x, delta_y = 0, 0
   steep = abs(y1 - y0) > abs(x1 - x0)
 
   if steep:
       x0, y0 = swap(x0, y0)
       x1, y1 = swap(x1, y1)
 
   if x0 > x1:
       x0, x1 = swap(x0, x1)
       y0, y1 = swap(y0, y1)
 
   if y0 > y1:
       dy = -1
   else:
       dy = 1
 
   delta_x = x1 - x0
   delta_y = abs(y1 - y0)
   y = y0
   error = 0
 
   for x in range(x0, x1 + 1):
       if steep:
           Plot(y, x)
       else:
           Plot(x, y)
       error = error + delta_y
       if 2 * error >= delta_x:
           y = y + dy
           error = error - delta_x
 
def dibujaRectangulo(xmin, ymin, xmax, ymax):
   dibujaLinea(xmin, ymin, xmin, ymax)
   dibujaLinea(xmin, ymax, xmax, ymax)
   dibujaLinea(xmax, ymax, xmax, ymin)
   dibujaLinea(xmax, ymin, xmin, ymin)
 
def calculo_outcode(x, y, xmin, ymin, xmax, ymax):
   oc = 0
   if y > ymax:
       oc |= TOP
   elif y < ymin:
       oc |= BOTTOM
   if x > xmax:
       oc |= RIGHT
   elif x < xmin:
       oc |= LEFT
   return oc
 
def cohen_sutherland(x0, y0, x1, y1, xmin, ymin, xmax, ymax):
   global k
 
   in_, done = False, False
   outcode0 = calculo_outcode(x0, y0, xmin, ymin, xmax, ymax)
   outcode1 = calculo_outcode(x1, y1, xmin, ymin, xmax, ymax)
 
   while not done:
       if (outcode0 | outcode1) == 0:
           done = True
           in_ = True
       elif (outcode0 & outcode1) != 0:
           done = True
       else:
           m = (y1 - y0) / (x1 - x0)
           x, y = 0, 0
           outcode = 0
 
           if outcode0 != 0:
               outcode = outcode0
           else:
               outcode = outcode1
 
           if (outcode0 & TOP) != 0:
               x = x0 + (ymax - y0) / m
               y = ymax
           elif (outcode & BOTTOM) != 0:
               x = x0 + (ymin - y0) / m
               y = ymin
           elif (outcode & RIGHT) != 0:
               y = y0 + m * (xmax - x0)
               x = xmax
           else:
               y = y0 + m * (xmin - x0)
               x = xmin
 
           if outcode == outcode0:
               x0, y0 = x, y
               outcode0 = calculo_outcode(x0, y0, xmin, ymin, xmax, ymax)
           else:
               x1, y1 = x, y
               outcode1 = calculo_outcode(x1, y1, xmin, ymin, xmax, ymax)
 
   print(f"{x0},{y0}---{x1},{y1}")
   if in_:
       lnclip[k][0], lnclip[k][1], lnclip[k][2], lnclip[k][3] = x0, y0, x1, y1
       k += 1
 
def display2():
   glClear(GL_COLOR_BUFFER_BIT)
   glPointSize(1.0)
   dibujaRectangulo(xmin, ymin, xmax, ymax)
   glPointSize(2.0)
   for i in range(k):
       dibujaLinea(lnclip[i][0], lnclip[i][1], lnclip[i][2], lnclip[i][3])
   glFlush()
 
def display1():
   glClear(GL_COLOR_BUFFER_BIT)
   glPointSize(2.0)
   dibujaRectangulo(xmin, ymin, xmax, ymax)
   glPointSize(1.0)
   for i in range(n):
       dibujaLinea(ln[i][0], ln[i][1], ln[i][2], ln[i][3])
   glFlush()
 
def myinit():
   glClearColor(0.9058823529411765, 0.9215686274509803, 0.9568627450980393, 1.0)
   glColor3f(0.5, 0.3, 0.9) 
   glPointSize(1.0)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   gluOrtho2D(0.0, 499.0, 0.0, 499.0)
 
def main():
   global n, xmin, ymin, xmax, ymax
 
   k = 0
   n = int(input("Ingrese el número de lineas a recortar: "))
   print("Ingrese las coordenadas x - y de los puntos extremos de las lineas:")
   for i in range(n):
       print(f"INGRESE PUNTOS DE LA LINEA {i + 1}:")
       for j in range(4):
           coord_type = "Coordenada X:" if j % 2 == 0 else "Coordenada Y:"
           ln[i][j] = int(input(coord_type))
 
   print("INGRESE LAS COORDENADAS X-Y DEL RECTANGULO DE RECORTE:")
   xmin = int(input("Ingrese Xmin: "))
   ymin = int(input("Ingrese Ymin: "))
   xmax = int(input("Ingrese Xmax: "))
   ymax = int(input("Ingrese Ymax: "))
 
   for i in range(n):
       cohen_sutherland(ln[i][0], ln[i][1], ln[i][2], ln[i][3], xmin, ymin, xmax, ymax)
 
   glutInit(sys.argv)
   glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
   glClearColor(0.9058823529411765, 0.9215686274509803, 0.9568627450980393, 1.0)
   glutInitWindowSize(500, 500)
   glutInitWindowPosition(0, 0)
   glutCreateWindow("LINEAS ANTES DEL RECORTE")
   glutDisplayFunc(display1)
   myinit()
 
   glutInitWindowSize(500, 500)
   glutInitWindowPosition(550, 0)
   glutCreateWindow("LINEAS DESPUES DEL RECORTE")
   glutDisplayFunc(display2)
   myinit()
   glutMainLoop()
if __name__ == "__main__":
   main()
