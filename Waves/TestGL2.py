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
    glOrtho(-15.0, 15.0, -15.0, 15.0, -15.0, 15.0)


 
class Point:
    def __init__(self, x, y, z, w ,h ,o):
        self._x = x
        self._y = y
        self._z = z

        #self._red = random.uniform(0,1)
        #self._blue = random.uniform(0,1)
        #self._green = random.uniform(0,1)
        self._red = w
        self._blue = h 
        self._green = o

    def swap(self,dt):
        self._x , self._y, self._z = self._x + ( math.sin(self._y /6.28 )) * (dt) ,\
                                     self._y + ( -math.sin(self._x) + (self._y*self._z)) * (dt),\
                                     self._z + (1.5-1 * (self._y*self._y)) * (dt)
    


def displayFun():
    while True:
        age = 0 
        points = []
        for x in range(-20, 20, 2): 
            for y in range(-20, 20, 2):
                for z in range(-20, 20, 2):
                    if math.sqrt(math.fabs(x*x + y*y + z*z)) <= 100: 
                     points.append(Point(x/10.0,y/10.0,z/10.0,x/10,y/10,z/10))
        
        glClear(GL_COLOR_BUFFER_BIT)
        while True:
    
            glClear(GL_COLOR_BUFFER_BIT)
            
    
            
            glBegin(GL_POINTS)
            for point in points:
                glColor3f(point._red, point._green, point._blue)
                glVertex3f( point._x, point._y, point._z )
                point.swap(0.05)

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
