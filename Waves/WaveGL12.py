from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random
import time
import math

def initFun():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-150.0, 150.0, -150.0, 150.0, -150.0, 150.0)



class Point:
    def __init__(self, x, y, z):
        self._x = float(x)
        self._y = float(y)
        self._z = float(z)

        self._red = random.uniform(0,1)
        self._blue = random.uniform(0,1)
        self._green = random.uniform(0,1)

    def swap(self,dt):

        self._x , self._y, self._z = (self._x,
                                      self._y,
                                     10.0 *math.e ** (-1.0 * dt *(1.0/6.28)) * math.sin(dt * math.sqrt(self._x**2 + self._y**2) )+
                                     10.0 *math.e ** (-1.0 * dt *(1.0/6.28)) * math.sin(dt * math.sqrt(self._x**2 + self._y**2) ))
                                     #* 5.0 *  math.cos(dt + self._x + self._y)




def displayFun():
    while True:
        age = 1.0
        points = []
        for x in range(-100, 100, 2):
            for y in range(-100, 100, 2):
                points.append(Point(x, y, 0))

        glClear(GL_COLOR_BUFFER_BIT)
        while True:
            glClear(GL_COLOR_BUFFER_BIT)
            glBegin(GL_LINES)

            glColor3f(0,0,1)
            glVertex3f(0,0,0)
            glVertex3f(40,0,0)

            glColor3f(0,1,0)
            glVertex3f(0,0,0)
            glVertex3f(0,40,0)

            glColor3f(0,1,1)
            glVertex3f(0,0,0)
            glVertex3f(0,0,40)

            glColor3f(1,0,0)
            glVertex3f(40,0,40)
            glVertex3f(0,0,40)

            glColor3f(1,0,1)
            glVertex3f(40,0,0)
            glVertex3f(40,0,40)

            glColor3f(1,1,0)
            glVertex3f(40,0,0)
            glVertex3f(40,40,0)

            glColor3f(1,1,1)
            glVertex3f(40,40,0)
            glVertex3f(0,40,0)

            glColor3f(1,1,1)
            glVertex3f(0,0,40)
            glVertex3f(0,40,40)

            glColor3f(1,1,1)
            glVertex3f(0,40,40)
            glVertex3f(0,40,0)
            glEnd()


            glBegin(GL_POINTS)
            for point in points:
                if (point._x != 0.0):
                    if (point._y != 0.0):
                        if (point._z != 0.0):
                            glColor3f( 10.0/math.fabs( point._x), 10.0/math.fabs( point._y),10.0/math.fabs( point._z))
                            #glVertex3f( point._x, point._y, 0.0 )
                            glVertex3f( point._x, point._y, point._z )
                            point.swap(age)
                        else:
                            glColor3f( 10.0/math.fabs( point._x), 10.0/math.fabs( point._y),254)
                            #glVertex3f( point._x, point._y, 0.0 )
                            glVertex3f( point._x, point._y, point._z )
                            point.swap(age)



            glEnd()
            glFlush()
            age = age + 0.01
            glRotatef(-0.1, 90, 180,270)

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(1200,1920)
    glutCreateWindow("Scatter")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    gluLookAt(30.0,30.0,30.0, 0.0,0.0,0.0, 0.0,0.0,1.0)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
