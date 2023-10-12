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

class Point:
    def __init__(self, x, y, r, g, b):
        self._x     = float(x)
        self._y     = float(y)
        
        self._red   = float(r)
        self._blue  = float(g)
        self._green = float(b)
        self._ldx   = u(-.005,.005)
        self._ldy   = u(-.005,.005)
        self._ldz   = u(-.005,.005)

    def getColor(self):
        return self._red, self._green, self._blue

    def swap( self, n,m ):
        n = n
        m = m
        s = abs ( n - m )
        if s != 0 and s < 5.0:
            x = u(-n,n)
            y = u(-m,m)

            self._x  += ( x - self._ldx ) 
            self._y  += ( y - self._ldy )
            self._ldx = x
            self._ldy = y    

            a = 15
            if self._x > a:
                self._x = -a+ abs( self._x - a)
            elif self._x < -a:
                self._x = a - abs( self._x  +a)

            if self._y > a:
                self._y = -a + abs( self._y-a)
            elif self._y < -a:
                self._y = a - abs( self._y +a)
        return self._x, self._y


    def swap2(self):
        if self._ldx > .5:
            self._ldx = self._ldx/ u(2,4)
        if self._ldy > .5:
            self._ldy = self._ldy/ u(2,4)
            
        self._x += self._ldx 
        self._y += self._ldy 

        a = 15
        if self._x > a:
            self._x = -a+ abs( self._x - a)
        elif self._x < -a:
            self._x = a - abs( self._x  +a)

        if self._y > a:
            self._y = -a + abs( self._y-a)
        elif self._y < -a:
            self._y = a - abs( self._y +a)
 
        
        return self._x, self._y


    def distance (self, x,y):
        return (abs( ((self._x-x)**2) + ((self._y-y)**2)  ))**.5
    
    def color_distance (self, x,y,z):
        return (abs( ((self._red-x)**2) + ((self._green-y)**2) + (( self._blue-z )**2) ))**.5
    
    def position(self):
        return self._x, self._y


def u( a, b ):
    return uniform( a, b )


points = []
for i in range(150):
        points.append( Point( u(-9,9), u(-9,9), u(-9,9), u(0,1), u(0,1) ) )


def displayFun():    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT| GL_STENCIL_BUFFER_BIT)          
    glBegin(GL_POINTS)

    
    for x, left in enumerate(points):
        lcount = 0
        ccount = 0
        glColor3f( *left.getColor() )
        
        for y, right in enumerate(points):
            if ( left.distance(*right.position()) < .15):
                lcount += 1

            if ( left.color_distance(*right.getColor()) < 1 ):
                ccount += 1

        if lcount > 1:
            glVertex2f( *left.swap( lcount, ccount ) )
           
        else:
            glVertex2f( *left.swap2( ) )
            pass

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
    glScalef       ( .050, .050, 0 )
  

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(1200, 1920)
    glutCreateWindow("Logistic Map kx(1-x)")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
