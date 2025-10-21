from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math
def draw(xc,yc,r):
        glBegin(GL_POINTS)
        x=-r
        while x<=r:
                y=math.sqrt(r**2-x**2)
                glVertex2f(xc+x,yc+y)
                glVertex2f(xc+x,yc-y)
                x+=0.001
        glEnd()
def display():
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0,0.0,0.0)
        draw(xc,yc,r)
        glFlush()

def init_gl():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-250, 250, -250, 250)            
    glColor3f(1,0,0)
    glPointSize(2)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()            
def main():
    global xc,yc,r
    xc=float(input("Enter circle center xc : "))
    yc=float(input("Enter the circle center yc : "))
    r=float(input("Raduis : "))
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"cirle using the Non-parametric eqn")
    init_gl()
    glutDisplayFunc(lambda: display())
    glutMainLoop()            
main()          

