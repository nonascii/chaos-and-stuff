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
    glOrtho(-50.0, 50.0, -50.0, 50.0, -50.0,50.0)


 
class Point:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

        self._red = random.uniform(0,1)
        self._blue = random.uniform(0,1)
        self._green = random.uniform(0,1)

    def swap(self,dt):
        self._x , self._y, self._z = self._x + (10.0 * (self._y - self._x)) * (dt) ,\
                                     self._y + ((self._x)* (28.0 - self._z) - self._y) * (dt),\
                                     self._z + ((8.0/3.0) * (-self._z) + self._x * self._y) * (dt)
    


def displayFun():
    while True:
        age = 0 
        points = []
        for x in range(-40, 40, 4): 
            for y in range(-40, 40, 4):
                for z in range(-40, 40, 4):
                    if math.sqrt(math.fabs(x*x + y*y + z*z)) <= 100: 
                     points.append(Point(x,y,z))
        
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
                glColor3f(point._red, point._green, point._blue)
                glVertex3f( point._x, point._y, point._z )
                point.swap(0.01)

#            time.sleep(0.01)
            glEnd()
            glFlush()
            age = age + 0.001
#            if age >= 1:
#                break
            glRotatef(-0.1, 90, 180,270)



if __name__ == '__main__':
    glutInit()   
    glutInitWindowSize(800,800)
    glutCreateWindow("Scatter")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
