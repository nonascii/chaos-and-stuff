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

        self._initx = float(z)
        self._inity = float(z)
        self._initz = float(z)

        self._endx = (2.0 * self._initx) / (1.0 + self._initx**2 + self._inity**2)
        self._endy = (2.0 * self._inity) / (1.0 + self._initx**2 + self._inity**2)
        self._endz = (-1.0 + self._initx**2 + self._inity**2) / (1.0 + self._initx**2 + self._inity**2)
        #self._endx = self._initx / (1.0 - self._initz)
        #self._endy = self._initt / (1.0 - self._initz)

        self.dx = ( self._endx - self._initx )/1
        self.dy = ( self._endy - self._inity )/1
        self.dz = ( self._endz - self._initz )/1

        self._red = random.uniform(0,1)
        self._blue = random.uniform(0,1)
        self._green = random.uniform(0,1)

    def swap(self,dt):

        self._x , self._y, self._z = (self._x,#+ self.dx,
                                     self._y,#+ self.dy,
                                     self._z)# + self.dz)
                                     #10.0 *math.e ** (-1.0 * dt *(1.0/6.28)) * math.sin(dt + self._x / self._y)\
                                     #*10.0* math.e ** (-1.0 * dt *(1.0/6.28)) * math.cos(dt + self._x*self._y)




def displayFun():
    while True:
        age = 1.0
        points = []
        static_points = []
        for x in range(-100,100, 5):
            for y in range(-100,100, 5):
                points.append(Point( x, y, 0 ))
                #points.append(Point( x, y, (x*x+y*y)/100 ))
                #static_points.append(Point( x, y, (x*x*x+y*y*y)/100 ))

        glClear(GL_COLOR_BUFFER_BIT)
        while True:
            glClear(GL_COLOR_BUFFER_BIT)
            glBegin(GL_LINES)

            glColor3f(1,0,0)
            glVertex3f(-100,0,0)
            glVertex3f(100,0,0)

            glColor3f(0,1,0)
            glVertex3f(0,-100,0)
            glVertex3f(0,100,0)

            glColor3f(0,0,1)
            glVertex3f(0,0,-100)
            glVertex3f(0,0,100)
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
            age = age + 0.1
            if age == 2.0:
                break
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
