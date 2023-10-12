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
    glOrtho(-300.0, 300.0, -300.0, 300.0, -300.0, 300.0)


 
class Point:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

        self._red = random.uniform(0,1)
        self._blue = random.uniform(0,1)
        self._green = random.uniform(0,1)

    def swap(self,dt):
        self._x , self._y, self._z = self._x + (40*(self._y-self._x) + (0.16*self._x*self._z) ) * (dt) ,\
                                     self._y + ((55*self._x) -1*(self._x*self._z) + (20 *self._y)) * (dt),\
                                     self._z + ((1.833 * self._z) + ( self._x *self._y ) -1*(0.65*self._x*self._x)) * (dt)
    


def displayFun():
    while True:
        age = 0 
        points = []
        for x in range(-40, 40, 2): 
            for y in range(-40, 40, 2):
                for z in range(-40, 40, 2):
                    if math.sqrt(math.fabs(x*x + y*y + z*z)) <= 100: 
                     points.append(Point(x,y,z))
        
        glClear(GL_COLOR_BUFFER_BIT)
        while True:
    
            glClear(GL_COLOR_BUFFER_BIT)
            
    
            
            glBegin(GL_POINTS)
            for point in points:
                glColor3f(point._red, point._green, point._blue)
                glVertex3f( point._x, point._y, point._z )
                point.swap(0.01)

#            time.sleep(0.01)
            glEnd()
            glFlush()
            age = age + 0.001
#            if age >= 1:
#                break
            glRotatef(1, 90, 180,270)



if __name__ == '__main__':
    glutInit()   
    glutInitWindowSize(1200,1920)
    glutCreateWindow("Scatter")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
