from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
def init():
 glClearColor(0,0,0,1)
 glOrtho(-10,10,-10,10,-1,1)
def plot_points():
 glClear(GL_COLOR_BUFFER_BIT)
 glPointSize(1)
 glColor3f(1,0,0)
 glBegin(GL_POINTS)
 glVertex2f(0,0)
 glEnd()
 glFlush()
def main():
 glutInit(sys.argv)
 glutInitDisplayMode(GLUT_RGB)
 glutInitWindowSize(500,500)
 glutInitWindowPosition(0,0)
 glutCreateWindow(b"PlotOrigin")
 glutDisplayFunc(plot_points)
 init()
 glutMainLoop()
main()   
