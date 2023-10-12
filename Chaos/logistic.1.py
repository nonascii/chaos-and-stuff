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


k = 2.4 

f = lambda k, x    :      k*x*(1.0 - x) 
#g = lambda k, x, y : abs( k * ( 1.0 -  2.0 *k* x ) ) * y

def drawArray(someArray):

    vertPoints = someArray[:,:2].flatten().astype(ctypes.c_float)
    vertices_gl = vertPoints.ctypes.data_as(ctypes.POINTER(ctypes.c_float))

    vertColors = someArray[:,2:].flatten().astype(ctypes.c_float)
    colors_gl = vertColors.ctypes.data_as(ctypes.POINTER(ctypes.c_float))

    glVertexPointer( 2,  GL_FLOAT, 0, vertices_gl)
    glColorPointer(  3,  GL_FLOAT, 0, colors_gl)
    glDrawArrays(    GL_POINTS,    0, len(vertPoints) // 2)


def u( a, b ):
    return uniform( a, b )


def displayFun():    
    global k

    glColor3f( 1,1,1 )
    x_points = random.random_sample( 2500 )

    glBegin(GL_POINTS)

    for a in range( 100 ):
        x_points = f ( k, x_points )

    for i in x_points:
        glVertex2f( k, i )
    
    glEnd()
    glutPostRedisplay()
    glutSwapBuffers()  
    glFlush()
    k += 0.001
    #sleep(0.03)


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

    glTranslatef   ( -7, -1, 0 )
    glScalef       ( 2, 2, 0 )
   # glTranslatef   ( -19.0, -2.0, 0 )
    #glScalef       (   5.5,  5.5, 0 )

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(1200, 1920)
    glutCreateWindow("Logistic Map kx(1-x)")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
