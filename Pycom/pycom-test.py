from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random
import time
import math
import serial



def initFun():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-150.0, 150.0, -150.0, 150.0, -150.0, 150.0)


 
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

    def swap(self,dt, p, r):
        self._x , self._y, self._z = self._x +0.001 * p * (dt) ,\
                                     self._y +0.001 *r *dt,\
                                     self._z 
    


def displayFun():
    while True:
        pitch = 0.0
        roll  = 0.0
        ser = serial.Serial('/dev/ttyACM0',9600, timeout=0.5)
        age = 0 
        points = []
        for x in range(-100, 100, 10): 
            for y in range(-100, 100, 10):
                for z in range(-100, 100, 10):
                    if math.sqrt(math.fabs(x*x + y*y + z*z)) <= 100: 
                     points.append(Point(x,y,z,x/10,y/10,z/10))
        
        glClear(GL_COLOR_BUFFER_BIT)
        while True:
            pitch = 0.0
            roll  = 0.0
            data  = ser.read(size=24)
            if ':' in data:
              
                try:
                    sdata = data.split(':')
                    print sdata
                    pitch = float(sdata[0])
                    roll = float(sdata[1])
                except ValueError:
           #         print 'value error'
                    pass
                print 'pitch ' + str(pitch)
                print 'roll' + str(roll)
                glClear(GL_COLOR_BUFFER_BIT)
                
                glBegin(GL_POINTS)
                for point in points:
                    glColor3f(point._red, point._green, point._blue)
                    glVertex3f( point._x, point._y, point._z )
                    point.swap(0.01, pitch, roll)
                
                glEnd()
                glFlush()
                age = age + 0.001
                #glRotatef(1, 90, 180,270)
         #       ser.close()


if __name__ == '__main__':
    glutInit()   
    glutInitWindowSize(1200,1920)
    glutCreateWindow("Scatter")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
