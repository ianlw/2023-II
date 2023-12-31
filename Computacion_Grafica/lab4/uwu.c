#include <GL/glut.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
float width, height, r = 0.3, change = 0;
//--dibuja circulos
void draw(float tx, float ty)
{
    glBegin(GL_LINE_LOOP);
    for (int i = 1; i <= 1200; i++)
    {
        float x1, y1, theta;
        theta = (2 * 3.14159 * i) / 1200;
        x1 = r * cosf(theta) * height / width;
        y1 = r * sinf(theta);
        glVertex3f(x1, y1, 0);
    }
    glEnd();
    glTranslatef(tx, ty, 0);
}
void display()
{

    float p[6][2];
    int j = 0;
    if (change == 0)
        change = 1;
    else if (change == 1)
        change = 0;
    width = glutGet(GLUT_WINDOW_WIDTH);
    height = glutGet(GLUT_WINDOW_HEIGHT);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glColor3f(1.0f, 0.0f, 0.0f);
    glMatrixMode(GL_MODELVIEW);
    glBegin(GL_LINE_LOOP);
    for (int i = 1; i <= 1200; i++)
    {
        float theta, x1, y1;
        theta = (2 * 3.14159 * i) / 1200;
        x1 = r * cosf(theta) * height / width;
        y1 = r * sinf(theta);
        glVertex3f(x1, y1, 0);
        if (i == 100 | i == 300 | i == 500 | i == 700 | i == 900 | i == 1100)
        {
            if (change == 0)
            {
                p[j][0] = x1;
                p[j][1] = y1;
                j++;
            }
        }
    }
    glEnd();
    for (int i = 0; i < 6 && change == 0; i++)
    {
        draw(p[i][0], p[i][1]);
    }
    glutSwapBuffers();
}
void main(int argc, char *argv[])
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(700, 500);
    glutCreateWindow("circles");
    glutDisplayFunc(display);
    glutMainLoop();
}
