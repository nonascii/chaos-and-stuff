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
    glOrtho(-400.0, 400.0, -400.0, 400.0, -400,400)


 
class Point:
    def __init__(self, x, y, z, w):
        self._x = x
        self._y = y
        self._z = z
        self._w = w

        self._red = random.uniform(0,1)
        self._blue = random.uniform(0,1)
        self._green = random.uniform(0,1)

    def swap(self,dt):
        self._x , self._y, self._z, self._w = self._x + 0.5 * (self._y + self._z + self._w) * (dt * dt),\
                                     self._y + 0.5 * (-self._x + self._z + self._w)* (dt * dt) ,\
                                     self._z + 0.5 * (-self._x - self._y + self._w) *(dt*dt),\
                                     self._w + 0.5 * (-self._x - self._y - self._z) *(dt*dt) 
        return self._x, self._y, self._z




def drawAxes():

            glBegin(GL_LINES)
            
            glColor3f(0,0,1)
            glVertex3f(0,0,0)
            glVertex3f(300,0,0)

            glColor3f(0,1,0)
            glVertex3f(0,0,0)
            glVertex3f(0,300,0)

            glColor3f(0,1,1)
            glVertex3f(0,0,0)
            glVertex3f(0,0,300)
    
            glColor3f(1,0,0)
            glVertex3f(300,0,300)
            glVertex3f(0,0,300)
    
            glColor3f(1,0,1)
            glVertex3f(300,0,0)
            glVertex3f(300,0,300)
    
            glColor3f(1,1,0)
            glVertex3f(300,0,0)
            glVertex3f(300,300,0)
            
            glColor3f(.5,1,1)
            glVertex3f(300,300,0)
            glVertex3f(0,300,0)
            
            glColor3f(1,.5,1)
            glVertex3f(0,0,300)
            glVertex3f(0,300,300)
            
            glColor3f(1,1,.5)
            glVertex3f(0,300,300)
            glVertex3f(0,300,0)
            
            glEnd()
    


def displayFun():
    while True:
        age = 0 
        points = []
        for x in range(-200, 200, 30): 
            for y in range(-200,200, 30):
                for z in range(-200,200,30):
                    for w in range(-200,200,30):
                        if math.sqrt(math.fabs(x*x + y*y + z*z + w*w)) <= x + y + z + w: 
                            points.append(Point(x,y,z,w))
#                    pass
#        points.append(Point(1.09,1.81,1.70))

#        sigma = 0
#        sigma += 1
        glClear(GL_COLOR_BUFFER_BIT)
        while True:
    
            glClear(GL_COLOR_BUFFER_BIT)
            drawAxes()
            
            
            glBegin(GL_LINES)
            for point in points:
                glColor3f(point._red, point._green, point._blue)
                glVertex3f( point._x, point._y, point._z )
#                glVertex3f( point._z, point._w, point._x )
#                glVertex3f( point._w, point._x, point._y )
            
                nx,ny,nz =  point.swap(random.uniform(0.1,0.1))
                glVertex3f(nx,ny,nz)

#            time.sleep(0.1)
            glEnd()
            glFlush()
            age = age + 0.001
#            if age >= 1:
#                break
            glRotatef(1, 90, 180,270)



if __name__ == '__main__':
    glutInit()   
    glutInitWindowSize(1280,1900)
    glutCreateWindow("Scatter")
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
