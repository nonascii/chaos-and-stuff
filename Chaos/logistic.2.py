from OpenGL.GL   import *
from OpenGL.GLUT import *
from OpenGL.GLU  import *
from OpenGL.arrays import vbo
import ctypes

from time   import sleep
from random import uniform,randint
from numpy  import sin, cos, log, pi, array, random, full, concatenate

# Define screen size.
width  = 1920
height = 1200
aspect = width / height

age  = 0


f = lambda k, x    :         (x *x) + k


def u( a, b ):
    return uniform( a, b )


k = u(0,1) + 1j*u(0,1)
x_points = random.random_sample( 10000 )
y_points = random.random_sample( 10000 )
x_points = x_points - 1j*y_points

def displayFun():    
    global age
    global poly
    global x_points
    glColor3f( 1,1,1 )
    

    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT| GL_STENCIL_BUFFER_BIT)          
    glBegin(GL_POINTS)

    
        
    x_points = f ( k, x_points )
       
    
    
    
    for i in x_points:
        #glColor3f( .01 + j, .01 + i, 0 )
        
        glVertex3f( 100*cos(i.real)*sin(i.imag), 100*sin(i.real)*cos(i.imag), 100*cos(i.imag) )


       

    glEnd()
    glutPostRedisplay()
    glutSwapBuffers()  
    glFlush()

    glRotatef(.5, 1,-1,1)
    sleep(0.03)



def initFun():
    glClearColor   ( 0.0, 0.0, 0.0, 0.0  )
    glColor3f      ( 0.0, 0.0, 0.0       )
    glPointSize    ( 1.0                 )
    glViewport     ( 0, 0, width, height )
    glMatrixMode   ( GL_PROJECTION       )
    glLoadIdentity ()

    gluOrtho2D     ( -1.0 * aspect,
                      1.0 * aspect,
                     -1.0,  1.0   )

    glClear        (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT| GL_STENCIL_BUFFER_BIT) 

    #glTranslatef   ( -.9, -.9, 0 )
    glScalef       ( .01, .01, 0 )
  

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(1200, 1920)
    glutCreateWindow("Logistic Map kx(1-x)")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
