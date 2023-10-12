from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from random import randint, uniform
import time
from math import sin, cos

def initFun():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    ortho = 50000.0
    glOrtho(-1.0*ortho, ortho, -1.0*ortho, ortho, -1.0*ortho, ortho)

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

        self._a = randint(-500, 500)
        self._b = randint(1, 10)


    def getColor(self):
        return self._red, self._green, self._blue


    def function(self, a, b, t):
        t = t/10.0
        return a*cos(t), a*(sin(t)), b*t


    def derivative(self, a, b, t):
        return 3, 6*t, 6*(t**2)  


    def swap(self, t):
        self._a = randint(-1000, 1000) 
        #self._b = randint(1, 10)
        xx, yy, zz = self.function(  self._a, self._b, t)
        # dx, dy, dz = self.derivative(self._a, self._b, t)
        self._x  , self._y , self._z  =self._x + xx, self._y + yy, 0
        # self._dx , self._dy, self._dz =  dx, dy, dz



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
        age = 0
        points = []
        older = []
        #create points loop
        for i in range(0,10):
            points.append( Point(uniform(0,10000), uniform(0,10000), uniform(0,0),
                                 uniform(0.1,1), uniform(0.1,1), uniform(.1,1) ) )

        glClear(GL_COLOR_BUFFER_BIT)
        while True:
            
            #glClear(GL_COLOR_BUFFER_BIT)
            #displayCube(500)            

            
            glBegin(GL_POINTS)
            for point in points:
                glColor3f( *point.getColor() )
                glVertex3f( point._x, point._y, point._z )
              #  glVertex3f( point._dx, point._dy, point._dz )
                
               # older.append( Point(point._dx, point._dy, point._dz, point._red, point._green, point._blue))
                point.swap(age)
                
                # if age % 100 == 1:
                #     older.append( Point(point._x, point._y, point._z,uniform(0.1,1), uniform(0.1,1), uniform(.1,1)))
                    #points.append(Point(point._x, point._y, point._z, point._red, point._green, point._blue))
                

            
            # for point in older:
            #     glColor3f( *point.getColor() )
            #     glVertex3f( point._x, point._y, point._z )
            #     point.swap(age)
            # points = points + older
            # older = []

            glEnd()
            glFlush()
            age = age + 1
            time.sleep(0.03)
            
            #glRotatef(10, 0, 0,100)

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(1200,1920)
    glutCreateWindow("Scatter")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    gluLookAt(90.0,90.0,90.0, 0.0,0.0,0.0, 0.0,0.0,1.0)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
