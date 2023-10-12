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
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

        self._red = random.uniform(0,1)
        self._blue = random.uniform(0,1)
        self._green = random.uniform(0,1)

    def swap(self,dt):
#        self._x, self._y , self._z =  0.001 * (self._y - self._x),\
#                                     (0.025 * self._x) - self._y - (self._x * self._z) ,\
#                                      (self._x * self._y) - (1.0001* self._z) 
    #    self._x , self._y, self._z = self._x + random.randint(-1,1), self._y + random.randint(-1,1), self._z + random.randint(-1,1) 
    
        self._x , self._y, self._z = self._x + 0.5 * (self._y + self._z) * (dt * dt),\
                                     self._y - 0.1 * (self._x -self._z )* (dt * dt) * math.sin(self._z/6.28*dt),\
                                     self._z - 0.1 * (self._x + self._y) *(dt*dt) + math.cos(self._x/6.28*dt),
    


def displayFun():
    while True:
        age = 0 
        points = []
        for x in range(-200, 200, 15): 
            for y in range(-200,200, 15):
                for z in range(-200,200,15):
                    if math.sqrt(math.fabs(x*x + y*y + z*z)) <= 100: 
                     points.append(Point(x,y,z))
#                    pass
#        points.append(Point(1.09,1.81,1.70))

#        sigma = 0
#        sigma += 1
        glClear(GL_COLOR_BUFFER_BIT)
        while True:
    
            glClear(GL_COLOR_BUFFER_BIT)
            
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
            
            glColor3f(1,1,1)
            glVertex3f(300,300,0)
            glVertex3f(0,300,0)
            
            glColor3f(1,1,1)
            glVertex3f(0,0,300)
            glVertex3f(0,300,300)
            
            glColor3f(1,1,1)
            glVertex3f(0,300,300)
            glVertex3f(0,300,0)
            
            glEnd()
    
            
            glBegin(GL_POINTS)
            for point in points:
                glColor3f(point._red, point._green, point._blue)
                glVertex3f( point._x, point._y, point._z )
                point.swap(random.uniform(0.1,0.2))

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
