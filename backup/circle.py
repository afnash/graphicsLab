from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
def init():
 glClearColor(0,0,0,1)
 glOrtho(-10,10,-10,10,-1,1)
def Circle():
 glClear(GL_COLOR_BUFFER_BIT)
 glColor3f(0,0,1)
 radius = 5
 segments = 100
 
 glBegin(GL_TRIANGLE_FAN)
 glVertex2f(0,0)
 for i in range(segments+1):
  angle=2*math.pi*i/segments
  x=radius*math.cos(angle)
  y=radius*math.sin(angle)
  glVertex2f(x,y)
 glEnd()
 glFlush()
def main():
 glutInit(sys.argv)
 glutInitDisplayMode(GLUT_RGB)
 glutInitWindowSize(500,500)
 glutInitWindowPosition(0,0)
 glutCreateWindow(b"Blue Circle")
 glutDisplayFunc(Circle)
 init()
 glutMainLoop()
main()   
