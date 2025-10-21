from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

def draw(xc,yc,r):
        segments=100
        glBegin(GL_LINE_LOOP)
        for i in range(segments):
                theta=(2*math.pi*i)/segments
                x=xc+r*math.cos(theta)
                y=yc+r*math.sin(theta)
                glVertex2f(x,y)
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
    xc=int(input("Enter circle center xc : "))
    yc=int(input("Enter the circle center yc : "))
    r=int(input("Raduis : "))
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"cirle using the parametric eqn")
    init_gl()
    glutDisplayFunc(lambda: display())
    glutMainLoop()
main()

