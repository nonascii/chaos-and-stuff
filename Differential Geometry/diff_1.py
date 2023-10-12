from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from random import randint, uniform
import time
from math import sin, cos, e, tan

def initFun():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10000.0, 10000.0, -10000.0, 10000.0, -10000.0, 10000.0)

class Point:
    def __init__(self, x, y, z, r, g, b):
        self._x = float(x)
        self._y = float(y)
        self._z = float(z)

        #self.function()
        self._dx = self._x
        self._dy = self._y
        self._dz = self._z

        self._red   = float(r)
        self._blue  = float(g)
        self._green = float(b)

        self._a = randint(1, 10)
        self._b = randint(1, 2)


    def getColor(self):
        return self._red, self._green, self._blue


    def function(self, a, b, t):
        # return a*cos(t), a*sin(t), b*t
        # t = float(tt)
        # print tt
        # print  1.0 + t
        # print  1.0 + t*t
        # print  1.0 + t*t*t
        # return (3.0*a*t)/(1.0 + t*t), (3.0*a*t**2)/(1.0 + t*t), 0
        # return (3.0*a*t)/(1.0 + t*t*t), (3.0*a*t**2)/(1.0 + t*t*t), 0
        return a * (e**(sin(1.0/b*t))), a * sin(t), float(t)


    def derivative(self, a, b, t):
        return a*( -1 * sin(t)), a*cos(t), b  


    def swap(self, t):
        xx, yy, zz = self.function(  self._a, self._b, t)
        #dx, dy, dz = self.derivative(self._a, self._b, t)
        self._x  , self._y , self._z  = self._x + xx, self._y + yy, self._z + zz
        #self._dx , self._dy, self._dz = self._x +  xx + dx, self._y + yy + dy, self._z+zz + dz


def displayCube(m):
    glBegin(GL_LINES)

    glColor3f(0,0,1)
    glVertex3f(0,0,0)
    glVertex3f(m,0,0)

    glColor3f(0,1,0)
    glVertex3f(0,0,0)
    glVertex3f(0,m,0)

    glColor3f(0,1,1)
    glVertex3f(0,0,0)
    glVertex3f(0,0,m)

    glColor3f(1,0,0)
    glVertex3f(m,0,m)
    glVertex3f(0,0,m)

    glColor3f(1,0,1)
    glVertex3f(m,0,0)
    glVertex3f(m,0,m)

    glColor3f(1,1,0)
    glVertex3f(m,0,0)
    glVertex3f(m,m,0)

    glColor3f(1,1,1)
    glVertex3f(m,m,0)
    glVertex3f(0,m,0)

    glColor3f(1,1,1)
    glVertex3f(0,0,m)
    glVertex3f(0,m,m)

    glColor3f(1,1,1)
    glVertex3f(0,m,m)
    glVertex3f(0,m,0)
    glEnd()

def displayFun():
    while True:
        age = -1.0
        points = []
        older  = []
        for i in range(0,100):
            points.append( Point(uniform(0,1000),
                                 uniform(0,1000),
                                 uniform(0,1000),
                                 uniform(0.5,1), uniform(0.5,1), uniform(0.5,1) ) )

        glClear(GL_COLOR_BUFFER_BIT)
        while True:
            glClear(GL_COLOR_BUFFER_BIT)
            displayCube(5000)            

            glBegin(GL_POINTS)
            # glBegin(GL_LINES)
            for point in points:
                glColor3f( *point.getColor() )
                glVertex3f( point._x, point._y, point._z )
                # glVertex3f( point._dx, point._dy, point._dz )
                older.append( Point(point._x, point._y, point._z, point._red, point._green, point._blue))
                # older.append( Point(point._dx, point._dy, point._dz, point._red, point._green, point._blue))
                point.swap(age)

            glEnd()
            glBegin(GL_POINTS)
            
            for point in older:
                glColor3f( *point.getColor() )
                glVertex3f( point._x, point._y, point._z )

            glEnd()
            glFlush()
            age = age + 0.1
            time.sleep(0.05)
            
            #glRotatef(10, 0, 0,100)

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(1200,1920)
    glutCreateWindow("Scatter")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    gluLookAt(30.0,30.0,30.0, 0.0,0.0,0.0, 0.0,0.0,1.0)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
