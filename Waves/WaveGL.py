from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random
import time
from math import sin, cos, e, fabs
import math


def initFun():
    glClearColor( 0.0, 0.0, 0.0, 0.0 )
    glColor3f(    0.0, 0.0, 0.0      )
    glPointSize(  1.0 ) 
    glMatrixMode( GL_PROJECTION )
    glLoadIdentity()
    glOrtho( -15.0, 15.0,
             -15.0, 15.0,
             -15.0, 15.0 )



def displayFun():
    while True:
        age = 0 
        x = 0
        y = 0
        theta = 0

        glClear(GL_COLOR_BUFFER_BIT)
        while True:
            theta = 0
            r    = 0
            glClear(GL_COLOR_BUFFER_BIT)
           

            for  i in range(0, 1000):
                glBegin(GL_POINTS)
                time.sleep(0.001)
                glColor3f( 0, fabs( cos( theta )), fabs(sin( theta )) )
                glVertex2f( r * cos( theta ), r * sin( theta ) )
                

                # z = e**(1j*theta)
                # glVertex2f( z.real, z.imag )

                theta += 0.01
                r += 0.01

                # x += 0.01
                # y += 0.01

                glEnd()
                glFlush()   

            
          
         
            time.sleep(0.01)
            # glEnd()
            # glFlush()

        #    age = age + 0.1
#            if age >= 1:
#                break
            #glRotatef(1, 90, 180,0)



if __name__ == '__main__':
    glutInit()   
    glutInitWindowSize(1200,1920)
    glutCreateWindow("Scatter")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
