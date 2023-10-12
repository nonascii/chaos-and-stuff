from OpenGL.GL   import *
from OpenGL.GLUT import *
from OpenGL.GLU  import *

from time   import sleep
from random import uniform,randint
from numpy  import sin, cos, log, pi, array, random, full, concatenate

# Define screen size.
width  = 1920
height = 1200
aspect = width / height

age  = 0
step = .0


f = lambda k, x    :      k *   x * (1.0 - x ) 
g = lambda k, x, y : abs( k * ( 1 -  2.0 * k*x ) ) * y



def u( a, b ):
    return uniform( a, b )

def displayFun():    
    global age
    glColor3f( 1,1,1 )

    y =  u( age, age + step )
    k =   3.44949

    x_points = random.random_sample( 25000 )
    y_points = full( 25000, y )

    # cx = 100*  x_points
    # cy = 100*  y_points



    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT| GL_STENCIL_BUFFER_BIT)          
    glBegin(GL_POINTS)

    for a in range( randint( 5, 9) ):
        y_points = g ( k, x_points, y_points )
        x_points = f ( k, x_points )
       
        
    for i, j in zip( x_points, y_points):
        glVertex2f( i, j)


       

    glEnd()
    glutPostRedisplay()
    glutSwapBuffers()  
    glFlush()
    age  += .001

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

    glTranslatef   ( -.9, -.9, 0 )
    #glScalef       ( .1, .1, 0 )
  

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(1200, 1920)
    glutCreateWindow("Logistic Map kx(1-x)")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
