#include<math.h>
#include<cstdlib>
#include<GL/glew.h>
#include<GL/glut.h>
#include<stdio.h>
using namespace std;

void Traslada()
{
    //--triangulo antes de trasladar
    glBegin(GL_TRIANGLES);
    glColor3f(0.5f, 1.0f, 0.7f);
    glVertex2f(100.0f, 100.0f);
    glVertex2f(200.0f, 100.0f);
    glVertex2f(150.0f, 150.0f);
    glEnd();

    //--triangulo después de trasladar
    glTranslatef(200.0f, 200.0f, 0.0f);
    glBegin(GL_TRIANGLES);
    glVertex3f(100.0f, 100.0f, 0.0f);
    glVertex3f(200.0f, 100.0f, 0.0f);
    glVertex3f(150.0f, 150.0f, 0.0f);
    glEnd();
}

//--despliega el gráfico
void display()
{
    glClear(GL_COLOR_BUFFER_BIT); //--establece el color de la ventana
    Traslada();    //--triangulo antes de trasladar
    glFlush(); //--fuerza la ejecución de los comandos de OpenGL
}

void myinit()
{
    glClearColor(1.0, 1.0, 1.0, 1.0);
    glColor3f(1.0, 0.0, 0.0);
    glPointSize(1.0); //--tamño de los puntos
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity(); //--cargar la identidad y poder hacer las
    //-- transformaciones
    gluOrtho2D(0.0, 499.0, 0.0, 499.0); // Aquí está la corrección
}

int main(int argc, char** argv)
{
    /* Inicializacion GLUT estándar*/
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500); /* ventana 500x500 pixeles */
    glutInitWindowPosition(0, 0);
    glutCreateWindow("Transformaciones con OpenGL");
    glutDisplayFunc(display);
    myinit(); /* fija o establece los atributos */
    glutMainLoop(); /* entra a un ciclo de evento */
    return 0;
}

