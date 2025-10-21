import sys
import math
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    err = dx - dy
    glColor3f(1, 0, 0)
    glLineWidth(2)
    glBegin(GL_POINTS)
    while True:
        glVertex2f(x1, y1)
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    bresenham_line(X1, Y1, X2, Y2)
    glutSwapBuffers()

def main():
    global X1,X2,Y1,Y2
    X1=float(input("enter x1 : "))    
    Y1=float(input("enter y1 : "))    
    X2=float(input("enter x2 : "))    
    Y2=float(input("enter y2 : "))
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutCreateWindow("Bresenham Line Algorithm")
    glutDisplayFunc(lambda: draw())
    init()
    glutMainLoop()

main()

