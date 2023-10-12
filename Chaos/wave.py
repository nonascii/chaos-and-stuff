from OpenGL.GL   import *
from OpenGL.GLUT import *
from OpenGL.GLU  import *

from time   import sleep
from random import uniform,randint
from numpy  import sin, cos, log, pi, e, array, random, full, concatenate, zeros

# Define screen size.
width  = 1920
height = 1200
aspect = width / height





def u( a, b ):
    return uniform( a, b )


def displayFun():    
    p = random.random_integers(-5,5, 1 )  
    s   =  0

    glColor3f( 1,1,1 )

    f  = lambda x,t   :  e ** ( 1j * ( p*x ) )
    g  = lambda x   :  ( abs(x) )**2 
    df = lambda x   :  1j*p*e ** ( 1j * ( x ) )
    no = lambda x,y :  abs(x)*y

    
    x_points = random.random_sample( 2000 )  
    y_points = random.random_sample( 2000 )  
    z_points =                zeros( 2000 )*1j
    #c_points = ( random.random_sample( 20000 ), random.random_sample( 20000 ), random.random_sample( 20000 ) )
    
    
    #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT| GL_STENCIL_BUFFER_BIT)          
    glBegin(GL_POINTS)

    iterations = randint( 5, 50 )
    for a in range( iterations ):
        
        #y_points = no ( df(x_points), y_points )
        y_points =  df(y_points)
        x_points =  f( x_points, x_points )
        
        z_points += y_points

    z_points = log( z_points ) /iterations

    x_points = g( x_points )
    #y_points = g( y_points )
    #for i,j in zip ( x_points, c_points ):
    
    # for i in x_points:
    #     s += i.real/20000.0
    
    #print s
    
    #if s >= .9:

    for i,j,k in zip( x_points, y_points, z_points ):
        #glColor4f(  i.real, k.imag, k.real, i.imag )
        glVertex2f( i.real*j.real, k.imag*j.imag )

        # glColor3f(  0,1,0 )
        # glColor4f(  j.real, j.imag, j.real, j.imag )
        
        # glColor3f(  0,0,1 )
        # glColor4f(  k.real, k.imag, k.real, k.imag )

    
    glEnd()
    
    glutPostRedisplay()
    glutSwapBuffers()  
    
    glFlush()
    
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

    #glTranslatef   ( -.9, -.9, 0 )
    glScalef       ( .0050, .0050, 0 )
  

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(1200, 1920)
    glutCreateWindow("Logistic Map kx(1-x)")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
