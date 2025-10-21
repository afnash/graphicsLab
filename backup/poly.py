from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
def init():
 glClearColor(0,0,0,1)
 glOrtho(-10,10,-10,10,-1,1)
def Polygon():
 glClear(GL_COLOR_BUFFER_BIT)
 glColor3f(1,0,1)
 sides = 6
 radius = 5
 angle_step = 2*math.pi/sides
 
 glBegin(GL_POLYGON)
 for i in range(sides):
  angle=i*angle_step
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
 glutCreateWindow(b"Polygon")
 glutDisplayFunc(Polygon)
 init()
 glutMainLoop()
main()   
