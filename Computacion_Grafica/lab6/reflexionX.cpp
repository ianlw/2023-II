#include <GL/glew.h>
#include <GL/glut.h>
#include <cstdlib>
#include <math.h>
#include <stdio.h>
using namespace std;
//--refleja un triangulo con respecto al eje X
void reflejaTrianguloX(double x1, double y1, double x2, double y2, double x3, double y3)
{
    double x1r, y1r, x2r, y2r, x3r, y3r;
    //--dibuja ejes X , Y
    glBegin(GL_LINES);
    glVertex2f(0, 250);
    glVertex2f(500, 250);
    glVertex2f(50, 0);
    glVertex2f(50, 500);
    glEnd();
    //-- convierte puntos a nueva escala
    x1 = x1 + 50;
    y1 = y1 + 250;
    x2 = x2 + 50;
    y2 = y2 + 250;
    x3 = x3 + 50;
    y3 = y3 + 250;
    //--dibujar el triangulo original
    glBegin(GL_LINE_LOOP);
    glVertex2f(x1, y1);
    glVertex2f(x2, y2);
    glVertex2f(x3, y3);
    glEnd();
    //--refleja triangulo con respecto al eje X
    x1r = x1;
    y1r = -y1 + 500;
    x2r = x2;
    y2r = -y2 + 500;
    x3r = x3;
    y3r = -y3 + 500;
    //--dibuja triangulo reflejado
    glBegin(GL_LINE_LOOP);
    glVertex2f(x1r, y1r);
    glVertex2f(x2r, y2r);
    glVertex2f(x3r, y3r);
    glEnd();
}
//--despliega el gráfico
void display()
{
    double x1, y1, x2, y2, x3, y3;
    x1 = 120.0;
    y1 = 160.0;
    x2 = 100.0;
    y2 = 200.0;
    x3 = 10.0;
    y3 = 100.0;
    glClear(GL_COLOR_BUFFER_BIT); //--establece el color de la ventana

    reflejaTrianguloX(x1, y1, x2, y2, x3, y3);
    glFlush(); //--fuerza la ejecución de los comandos de OpenGL
}
void myinit()
{
    glClearColor(1.0, 1.0, 1.0, 1.0);
    glColor3f(1.0, 0.0, 0.0);
    glPointSize(1.0);            //--tamño de los puntos
    glMatrixMode(GL_PROJECTION); //--activar la matriz de transformación
    glLoadIdentity();
    gluOrtho2D(0.0, 499.0, 0.0, 499.0); //--establece una ventana de dibujo
}
int main(int argc, char **argv)
{
    /* Inicializacion GLUT estándar*/
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500); /* ventana 500x500 pixeles */
    glutInitWindowPosition(0, 0);
    glutCreateWindow("Reflexión"); /* título de la ventana*/
    glutDisplayFunc(display);
    myinit();       /* fija o establece los atributos */
    glutMainLoop(); /* entra a un ciclo de evento */
    return 0; // Añade una declaración de retorno
}
